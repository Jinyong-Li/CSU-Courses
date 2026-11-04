#!/usr/bin/env python3
"""为已有课程的 README.md 添加「补充本课程资料」快捷入口。

在 CSU-Courses 仓库根目录运行：python scripts/add_course_shortcuts.py
仅修改根目录下包含 README.md 的课程文件夹；重复运行不会重复插入。
"""

from pathlib import Path
from urllib.parse import quote
import re

ROOT = Path(__file__).resolve().parent.parent
REPOSITORY = "https://github.com/Jinyong-Li/CSU-Courses"
SKIP = {".github", ".git", "assets", "scripts", "node_modules", ".venv", "venv"}


def insert_link(readme: str, course: str) -> str:
    if "issues/new?template=add-course.yml&course_name=" in readme:
        return readme
    link = (
        f"**[➕ 补充本课程资料（免 Fork）]"
        f"({REPOSITORY}/issues/new?template=add-course.yml"
        f"&course_name={quote(course, safe='')})**"
    )
    heading = re.search(r"^# [^\n]+", readme, flags=re.MULTILINE)
    if heading:
        return readme[:heading.end()] + "\n\n" + link + readme[heading.end():]
    return link + "\n\n" + readme


def main() -> None:
    count = 0
    for folder in sorted(ROOT.iterdir()):
        if not folder.is_dir() or folder.name.startswith(".") or folder.name in SKIP:
            continue
        readme_file = folder / "README.md"
        if not readme_file.is_file():
            continue
        original = readme_file.read_text(encoding="utf-8-sig")
        updated = insert_link(original, folder.name)
        if updated == original:
            continue
        readme_file.write_text(updated, encoding="utf-8")
        count += 1
        print(f"已添加：{readme_file.relative_to(ROOT)}")
    print(f"完成：更新 {count} 个课程 README.md")


if __name__ == "__main__":
    main()
