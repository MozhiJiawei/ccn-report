from __future__ import annotations

import re
import json
import sys
from pathlib import Path

from report_archive_layout import IGNORED_DIRECTORY_NAMES, is_valid_report_dir_name


REPO_ROOT = Path(__file__).resolve().parents[1]
IGNORED_NAMES = {".gitkeep"}
ALLOWED_ROOT_FILE_NAMES = {
    ".gitattributes",
    ".gitignore",
    "AGENTS.md",
    "README.md",
}
ALLOWED_REPORT_SUFFIXES = {".html", ".pptx"}
ALLOWED_REPORT_FILENAMES = {"README.md"}
LOCAL_TEMP_URL_RE = re.compile(r"(?:http://(?:127\.0\.0\.1|localhost):\d+|file://)", re.IGNORECASE)


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def check_repo_root(errors: list[str]) -> None:
    categories = load_categories()
    for item in REPO_ROOT.iterdir():
        if item.name in IGNORED_NAMES:
            continue
        if item.name in ALLOWED_ROOT_FILE_NAMES or item.name in IGNORED_DIRECTORY_NAMES:
            continue
        if not item.is_dir():
            fail(f"Repository root contains an unexpected file: {item.relative_to(REPO_ROOT)}", errors)
            continue
        if is_valid_report_dir_name(item.name):
            fail(
                f"Report directories must be at least two levels below the repository root: {item.relative_to(REPO_ROOT)}",
                errors,
            )
        elif item.name not in categories:
            fail(f"Unknown primary category: {item.name}", errors)


def load_categories() -> dict[str, list[str]]:
    return json.loads((REPO_ROOT / "classification" / "categories.json").read_text(encoding="utf-8"))


def check_archive_branch(branch: Path, errors: list[str]) -> None:
    if branch.parent == REPO_ROOT and branch.name in IGNORED_DIRECTORY_NAMES:
        return
    parts = branch.relative_to(REPO_ROOT).parts
    categories = load_categories()
    if parts[0] not in categories:
        return  # Reported by the root check.
    if len(parts) > 2 or (len(parts) == 2 and parts[1] not in categories[parts[0]]):
        fail(f"Invalid category or extra classification level: {branch.relative_to(REPO_ROOT)}", errors)
        return
    items = list(branch.iterdir())
    direct_files = [item for item in items if item.is_file() and item.name not in IGNORED_NAMES]
    if direct_files:
        fail(
            f"Directory contains files but is not a valid report directory: {branch.relative_to(REPO_ROOT)}. "
            "Move files into <YYYYMMDD>-<report-slug>-<creator>/ or rename this directory to that format.",
            errors,
        )

    for item in items:
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
    readme = report_dir / "README.md"
    if not readme.is_file():
        fail(f"Report is missing README.md: {report_dir.relative_to(REPO_ROOT)}", errors)
    elif len(report_dir.relative_to(REPO_ROOT).parts) == 2:
        text = readme.read_text(encoding="utf-8")
        primary = report_dir.relative_to(REPO_ROOT).parts[0]
        required = [r"文章类型：\s*综述／综合", r"一级分类：\s*" + re.escape(primary) + r"\s*(?:\n|$)", r"一级直归理由：[^\n\s][^\n]+"]
        if not all(re.search(pattern, text) for pattern in required):
            fail(f"Primary-level report needs survey classification and reason: {report_dir.relative_to(REPO_ROOT)}", errors)
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

    for item in REPO_ROOT.iterdir():
        if item.is_dir() and item.name not in IGNORED_DIRECTORY_NAMES:
            check_archive_branch(item, errors)

    if errors:
        print("Report archive validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Report archive validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
