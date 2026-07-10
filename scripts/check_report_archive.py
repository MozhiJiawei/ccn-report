from __future__ import annotations

import re
import sys
from datetime import datetime
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR_RE = re.compile(
    r"^(?P<date>\d{8})-(?P<slug>[a-z0-9]+(?:-[a-z0-9]+)*)-(?P<creator>[\w\u4e00-\u9fff-]+)$"
)
ALLOWED_TOP_LEVEL = {"大厂动态", "开源软件分析", "学术论文分析"}
IGNORED_NAMES = {".gitkeep"}
PROJECT_ROOT_NAMES = {
    ".git",
    ".github",
    ".gitattributes",
    ".gitignore",
    "AGENTS.md",
    "README.md",
    "index.html",
    "scripts",
}
ALLOWED_REPORT_SUFFIXES = {".html", ".pptx"}
ALLOWED_REPORT_FILENAMES = {"README.md"}
LOCAL_TEMP_URL_RE = re.compile(r"(?:http://(?:127\.0\.0\.1|localhost):\d+|file://)", re.IGNORECASE)


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def is_valid_report_dir_name(name: str) -> bool:
    match = REPORT_DIR_RE.fullmatch(name)
    if not match:
        return False

    try:
        datetime.strptime(match.group("date"), "%Y%m%d")
    except ValueError:
        return False

    return True


def check_repo_root(errors: list[str]) -> None:
    for category_name in sorted(ALLOWED_TOP_LEVEL):
        if not (REPO_ROOT / category_name).is_dir():
            fail(f"Missing top-level category directory: {category_name}/", errors)

    for item in REPO_ROOT.iterdir():
        if item.name in IGNORED_NAMES:
            continue
        if item.name in PROJECT_ROOT_NAMES:
            continue
        if not item.is_dir():
            fail(f"Repository root contains an unexpected file: {item.relative_to(REPO_ROOT)}", errors)
            continue
        if item.name not in ALLOWED_TOP_LEVEL:
            fail(
                f"Unknown top-level category {item.relative_to(REPO_ROOT)}. "
                f"Allowed: {', '.join(sorted(ALLOWED_TOP_LEVEL))}",
                errors,
            )


def check_category(category: Path, errors: list[str]) -> None:
    for item in category.iterdir():
        if item.name in IGNORED_NAMES:
            continue
        if not item.is_dir():
            fail(f"Category directories must not contain files directly: {item.relative_to(REPO_ROOT)}", errors)
            continue
        if is_valid_report_dir_name(item.name):
            fail(
                f"Report directories must be placed under an object/direction directory: {item.relative_to(REPO_ROOT)}",
                errors,
            )
            continue

        check_archive_branch(item, errors)


def check_archive_branch(branch: Path, errors: list[str]) -> None:
    direct_files = [item for item in branch.iterdir() if item.is_file() and item.name not in IGNORED_NAMES]
    if direct_files:
        fail(
            f"Directory contains files but is not a valid report directory: {branch.relative_to(REPO_ROOT)}. "
            "Move files into <YYYYMMDD>-<report-slug>-<creator>/ or rename this directory to that format.",
            errors,
        )

    for item in branch.iterdir():
        if item.name in IGNORED_NAMES:
            continue
        if item.is_file():
            continue
        if not item.is_dir():
            fail(
                f"Archive category containers must only contain directories: {item.relative_to(REPO_ROOT)}",
                errors,
            )
            continue

        if is_valid_report_dir_name(item.name):
            check_report_contents(item, errors)
            continue

        check_archive_branch(item, errors)


def check_report_contents(report_dir: Path, errors: list[str]) -> None:
    for path in report_dir.rglob("*"):
        if not path.is_file():
            continue
        if path.name in IGNORED_NAMES:
            continue
        if path.name in ALLOWED_REPORT_FILENAMES:
            continue
        if path.suffix.lower() in ALLOWED_REPORT_SUFFIXES:
            if path.suffix.lower() == ".html":
                check_html_archive(path, errors)
            continue
        fail(
            f"Report directory contains a non-archival file: {path.relative_to(REPO_ROOT)}. "
            "Only dependency-free HTML, PPTX, and README.md are allowed.",
            errors,
        )


def check_html_archive(path: Path, errors: list[str]) -> None:
    try:
        content = path.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        fail(f"Cannot read HTML archive {path.relative_to(REPO_ROOT)}: {exc}", errors)
        return
    if LOCAL_TEMP_URL_RE.search(content):
        fail(
            f"HTML archive contains local temporary URLs: {path.relative_to(REPO_ROOT)}. "
            "Re-export with scripts/export_singlefile_archive.py.",
            errors,
        )


def main() -> int:
    errors: list[str] = []
    check_repo_root(errors)

    for category_name in sorted(ALLOWED_TOP_LEVEL):
        category = REPO_ROOT / category_name
        if category.is_dir():
            check_category(category, errors)

    if errors:
        print("Report archive validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Report archive validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
