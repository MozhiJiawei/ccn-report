from __future__ import annotations

import re
import sys
from datetime import datetime
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR_RE = re.compile(
    r"^(?P<slug>[a-z0-9]+(?:-[a-z0-9]+)*)-(?P<date>\d{8})-(?P<creator>[a-z0-9]+(?:-[a-z0-9]+)*)$"
)
ALLOWED_TOP_LEVEL = {"大厂动态", "开源软件分析", "学术论文分析"}
IGNORED_NAMES = {".gitkeep"}
PROJECT_ROOT_NAMES = {".git", ".github", ".gitignore", "AGENTS.md", "README.md", "scripts"}


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
            "Move files into <report-slug>-<YYYYMMDD>-<creator>/ or rename this directory to that format.",
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
            continue

        check_archive_branch(item, errors)


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
