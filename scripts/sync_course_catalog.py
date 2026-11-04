#!/usr/bin/env python3
"""扫描课程文件夹，更新首页课程导航和补充表单的已有课程下拉选项。

运行：python scripts/sync_course_catalog.py
预览：python scripts/sync_course_catalog.py --check
元数据：课程 README 顶部的 <!-- COURSE_META_START ... COURSE_META_END -->
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / 'README.md'
FORM = ROOT / '.github' / 'ISSUE_TEMPLATE' / 'supplement-course.yml'
REPOSITORY = 'https://github.com/Jinyong-Li/CSU-Courses'
CATEGORIES = ('公共基础课', '专业基础课', '专业核心课', '通识选修课', '实验实践课', '其他')
EXCLUDED_DIRS = {
    '.git', '.github', 'assets', 'scripts', 'node_modules',
    '__pycache__', '.venv', 'venv', 'dist', 'build', 'docs', 'tests',
}

# 旧课程尚未填写 COURSE_META 时的兼容分类。新增课程优先读取自身 README。
LEGACY_CATEGORIES = {
    '高等数学': '公共基础课',
    '大学物理': '公共基础课',
    '英语': '公共基础课',
    '习概': '公共基础课',
    '毛概': '公共基础课',
    '马克思主义基本原理': '公共基础课',
    '军事理论': '公共基础课',
    '大计基': '专业基础课',
    '电工学': '专业基础课',
    '公选课': '通识选修课',
    '健康心理学': '通识选修课',
    '大学生心理健康教育': '通识选修课',
    '制造工程训练': '实验实践课',
    '金工实习': '实验实践课',
    'PPT模板': '其他',
    '简历模板': '其他',
}

# 支持新版整块隐藏的元数据，兼容旧版分开注释的元数据。
META_PATTERN = re.compile(
    r'<!--\s*COURSE_META_START\s*(?:-->)?(.*?)'
    r'(?:<!--\s*)?COURSE_META_END\s*-->', re.DOTALL
)


def category_from_readme(course_dir: Path) -> str:
    readme = course_dir / 'README.md'
    if readme.is_file():
        text = readme.read_text(encoding='utf-8-sig')
        match = META_PATTERN.search(text)
        if match:
            row = re.search(r'^\s*分类\s*[：:]\s*(.+?)\s*$', match.group(1), re.MULTILINE)
            if row and row.group(1) in CATEGORIES:
                return row.group(1)
        # 没有元数据时，也支持现有课程 README 中可见的分类文字。
        visible = re.search(r'^>\s*\*\*课程分类\*\*\s*[：:]\s*(\S.*?)\s*$', text, re.MULTILINE)
        if visible and visible.group(1) in CATEGORIES:
            return visible.group(1)
    return LEGACY_CATEGORIES.get(course_dir.name, '其他')


def course_directories(root: Path) -> list[Path]:
    dirs = []
    for p in root.iterdir():
        if not p.is_dir() or p.name.startswith('.') or p.name in EXCLUDED_DIRS:
            continue
        # 防止 Markdown 中显示控制符和意外项目目录。
        if any(ord(ch) < 32 for ch in p.name):
            continue
        dirs.append(p)
    return sorted(dirs, key=lambda p: (p.name.casefold(), p.name))


def md_label(value: str) -> str:
    return re.sub(r'([\\\[\]()`*_|])', r'\\\1', value)


def course_link(name: str, *, to_form: bool) -> str:
    if to_form:
        url = f'{REPOSITORY}/issues/new?template=supplement-course.yml&existing_course={quote(name, safe="")}'
    else:
        url = './' + quote(name, safe='') + '/'
    return f'[{md_label(name)}]({url})'


def grouped_courses(root: Path) -> dict[str, list[str]]:
    groups: dict[str, list[str]] = defaultdict(list)
    for p in course_directories(root):
        groups[category_from_readme(p)].append(p.name)
    return groups


def render_index(groups: dict[str, list[str]]) -> str:
    lines = ['| 分类 | 课程与资源 |', '| :--- | :--- |']
    for category in CATEGORIES:
        names = groups.get(category, [])
        if names:
            links = ' · '.join(course_link(n, to_form=False) for n in names)
            lines.append(f'| **{category}** | {links} |')
    if len(lines) == 2:
        lines.append('| 暂无课程 | 欢迎通过表单新增 |')
    return '\n'.join(lines)


def render_form_options(groups: dict[str, list[str]]) -> str:
    # 生成 GitHub Issue Form 下拉框选项；写成双引号字符串，兼容特殊字符。
    import json
    names = [name for category in CATEGORIES for name in groups.get(category, [])]
    return "\n".join("        - " + json.dumps(name, ensure_ascii=False) for name in names)


def replace_region(src: str, start: str, end: str, content: str) -> str:
    # 仅替换带标记的自动生成区，标记之外内容一字不动。
    pattern = re.compile(
        r'(?m)^([ \t]*)' + re.escape(start) + r'[ \t]*\n'
        r'.*?'
        r'^\1' + re.escape(end) + r'[ \t]*$',
        re.DOTALL | re.MULTILINE,
    )
    found = list(pattern.finditer(src))
    if len(found) != 1:
        raise ValueError(f'必须且只能有一对标记：{start} / {end}')
    m = found[0]
    indent = m.group(1)
    return src[:m.start()] + (f'{indent}{start}\n\n{content}\n\n{indent}{end}') + src[m.end():]


def update_file(path: Path, start: str, end: str, content: str, check: bool) -> bool:
    original = path.read_text(encoding='utf-8')
    updated = replace_region(original, start, end, content)
    if updated == original:
        print(f'无需更新：{path.relative_to(ROOT)}')
        return False
    print(f'{"需要更新" if check else "已更新"}：{path.relative_to(ROOT)}')
    if not check:
        path.write_text(updated, encoding='utf-8')
    return True


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--check', action='store_true', help='仅检查，不写入；存在差异时返回 1')
    args = ap.parse_args()
    groups = grouped_courses(ROOT)
    course_count = sum(len(v) for v in groups.values())
    print(f'扫描到 {course_count} 个课程/资源目录。')
    if not course_count:
        print('未发现课程目录，跳过更新。请在实际仓库根目录运行。')
        return 0
    changes = 0
    changes += update_file(README, '<!-- COURSE_INDEX_START -->', '<!-- COURSE_INDEX_END -->', render_index(groups), args.check)
    changes += update_file(FORM, '# COURSE_OPTIONS_START', '# COURSE_OPTIONS_END', render_form_options(groups), args.check)
    return 1 if args.check and changes else 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (OSError, ValueError) as exc:
        print(f'生成课程目录失败：{exc}', file=sys.stderr)
        sys.exit(2)
