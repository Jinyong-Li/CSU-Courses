#!/usr/bin/env python3
"""为已有课程 README 增加或更新「补充本课程资料」链接，一次性执行即可。"""

from pathlib import Path
from urllib.parse import quote
import re

ROOT = Path(__file__).resolve().parent.parent
REPO = "https://github.com/Jinyong-Li/CSU-Courses"
SKIP = {".github", ".git", "assets", "scripts", "node_modules", ".venv", "venv"}
OLD = re.compile(
    r"(?m)^\*\*\[➕ 补充本课程资料（免 Fork）\]"
    r"\(https://github\.com/Jinyong-Li/CSU-Courses/issues/new\?"
    r"template=(?:add-course|supplement-course)\.yml&"
    r"(?:course_name|existing_course)=[^\n)]+\)\*\*$"
)


def insert_link(source: str, course: str) -> str:
    url = f"{REPO}/issues/new?template=supplement-course.yml&existing_course={quote(course, safe='')}"
    link = f"**[➕ 补充本课程资料（免 Fork）]({url})**"
    if OLD.search(source):
        return OLD.sub(link, source)
    if "issues/new?template=supplement-course.yml&existing_course=" in source:
        return source
    heading = re.search(r"^# [^\n]+", source, re.MULTILINE)
    if heading:
        return source[:heading.end()] + "\n\n" + link + source[heading.end():]
    return link + "\n\n" + source


def main() -> None:
    changes = 0
    for folder in sorted(ROOT.iterdir()):
        if not folder.is_dir() or folder.name.startswith(".") or folder.name in SKIP:
            continue
        readme = folder / "README.md"
        if not readme.is_file():
            continue
        original = readme.read_text(encoding="utf-8-sig")
        updated = insert_link(original, folder.name)
        if updated != original:
            readme.write_text(updated, encoding="utf-8")
            print("已更新：", readme.relative_to(ROOT))
            changes += 1
    print(f"完成：更新 {changes} 个课程 README")


if __name__ == "__main__":
    main()
