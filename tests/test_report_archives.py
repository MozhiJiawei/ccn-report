from __future__ import annotations

import sys
import subprocess
import tempfile
import time
import unittest
import zipfile
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from report_archive_layout import find_report_dirs, report_date  # noqa: E402
from download_full_archive import extract_packages, package_records, safe_member_path  # noqa: E402
from release_compressed_archive import (  # noqa: E402
    copy_report_dirs,
    group_reports_by_month,
    select_release_changes,
    write_zip,
)


class ReportArchiveLayoutTests(unittest.TestCase):
    def test_discovers_reports_under_arbitrary_roots_and_stops_at_report(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            first = root / "新分类" / "对象" / "20260713-first-report-mozhi"
            second = root / "另一个分类" / "多层" / "方向" / "20260713-second-report-墨之"
            nested_fake = first / "assets" / "20260714-not-a-separate-report-codex"
            invalid = root / "新分类" / "对象" / "20260230-invalid-date-mozhi"
            for directory in (first, second, nested_fake, invalid, root / ".git" / "x" / "20260713-hidden-report-x"):
                directory.mkdir(parents=True)

            self.assertEqual(find_report_dirs(root), [second, first])
            self.assertEqual(report_date(first.name), "20260713")
            self.assertIsNone(report_date(invalid.name))

    def test_root_report_directory_is_not_discovered(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "20260713-root-report-x").mkdir()
            shallow = root / "category" / "20260713-valid-shallow-x"
            shallow.mkdir(parents=True)
            valid = root / "category" / "subject" / "20260713-valid-report-x"
            valid.mkdir(parents=True)
            self.assertEqual(find_report_dirs(root), [shallow, valid])


class MonthlyPackageTests(unittest.TestCase):
    def test_release_helpers_import_without_pillow_installed(self) -> None:
        script = """
import importlib.abc
import sys
class BlockPillow(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path, target=None):
        if fullname == 'PIL' or fullname.startswith('PIL.'):
            raise ModuleNotFoundError("blocked Pillow for test")
        return None
sys.meta_path.insert(0, BlockPillow())
import release_compressed_archive
"""
        completed = subprocess.run(
            [sys.executable, "-c", script],
            cwd=SCRIPTS,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)

    def test_zip_preserves_repository_relative_paths_without_wrapper(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / "repo"
            report = root / "任意分类" / "对象" / "20260713-demo-report-x"
            report.mkdir(parents=True)
            (report / "report.html").write_text("ok", encoding="utf-8")
            package_root = Path(temporary) / "package"
            copy_report_dirs(root, package_root, [report])
            archive = Path(temporary) / "date.zip"
            write_zip(package_root, archive)
            with zipfile.ZipFile(archive) as handle:
                self.assertEqual(handle.namelist(), ["任意分类/对象/20260713-demo-report-x/report.html"])

    def test_incremental_selection_skips_unchanged_and_removes_old_big_zip(self) -> None:
        paths = [Path("ccn-report-202606-q70.zip"), Path("ccn-report-202607-q70.zip")]
        packages = [
            {"filename": paths[0].name, "sha256": "same"},
            {"filename": paths[1].name, "sha256": "new"},
        ]
        previous = {
            # Schema 4 used the same monthly package records and can be reused
            # during the one-time migration that removes the full archive.
            "manifest_schema_version": 4,
            "packages": [
                {"filename": paths[0].name, "sha256": "same"},
                {"filename": paths[1].name, "sha256": "old"},
            ],
            "index": {"filename": "index.html", "sha256": "index-same"},
            "assembler": {"filename": "download_full_archive.py", "sha256": "assembler-same"},
        }
        existing = {
            paths[0].name,
            paths[1].name,
            "index.html",
            "ccn-report-latest-compressed-q70.zip",
            "unrelated-download.zip",
            "ccn-report-full-q70.zip",
            "ccn-report-full-q60.zip",
            "ccn-report-20260713-q70.zip",
            "download_full_archive.py",
        }
        changed_packages, changed_assets, obsolete = select_release_changes(
            paths,
            packages,
            Path("index.html"),
            {"filename": "index.html", "sha256": "index-same"},
            Path("download_full_archive.py"),
            {"filename": "download_full_archive.py", "sha256": "assembler-same"},
            previous,
            existing,
        )
        self.assertEqual(changed_packages, [paths[1]])
        self.assertEqual(changed_assets, [paths[1]])
        self.assertEqual(
            obsolete,
            {
                "ccn-report-20260713-q70.zip",
                "ccn-report-full-q70.zip",
                "ccn-report-full-q60.zip",
                "ccn-report-latest-compressed-q70.zip",
            },
        )

    def test_incremental_selection_rejects_misaligned_package_records(self) -> None:
        with self.assertRaisesRegex(RuntimeError, "different lengths"):
            select_release_changes(
                [Path("ccn-report-202607-q70.zip")],
                [],
                Path("index.html"),
                {},
                Path("download_full_archive.py"),
                {},
                {},
                set(),
            )

    def test_groups_reports_from_the_same_month_together(self) -> None:
        reports = [
            Path("分类/对象/20260702-first-report-x"),
            Path("其他/对象/20260731-second-report-x"),
            Path("分类/对象/20260801-third-report-x"),
        ]
        self.assertEqual(
            group_reports_by_month(reports),
            {"202607": reports[:2], "202608": reports[2:]},
        )

    def test_downloaded_packages_combine_into_full_tree(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            first = root / "first.zip"
            second = root / "second.zip"
            with zipfile.ZipFile(first, "w") as archive:
                archive.writestr("分类A/对象/20260712-first-report-x/a.html", "a")
            with zipfile.ZipFile(second, "w") as archive:
                archive.writestr("分类B/对象/20260713-second-report-x/b.html", "b")
            destination = root / "full"
            destination.mkdir()
            self.assertEqual(extract_packages([first, second], destination), 2)
            self.assertEqual(
                sorted(path.relative_to(destination).as_posix() for path in destination.rglob("*") if path.is_file()),
                [
                    "分类A/对象/20260712-first-report-x/a.html",
                    "分类B/对象/20260713-second-report-x/b.html",
                ],
            )

    def test_download_manifest_package_records_are_validated(self) -> None:
        digest = "a" * 64
        self.assertEqual(
            package_records({"packages": [{"filename": "ccn-report-202607-q70.zip", "sha256": digest}]}),
            [("ccn-report-202607-q70.zip", digest)],
        )
        with self.assertRaisesRegex(RuntimeError, "unsafe or duplicate"):
            package_records({"packages": [{"filename": "../archive.zip", "sha256": digest}]})

    def test_download_extraction_rejects_traversal(self) -> None:
        with self.assertRaisesRegex(RuntimeError, "unsafe ZIP entry"):
            safe_member_path("../outside.txt")

    def test_zip_hash_is_stable_when_file_mtime_changes(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / "tree"
            root.mkdir()
            source = root / "report.html"
            source.write_text("same content", encoding="utf-8")
            first = Path(temporary) / "first.zip"
            second = Path(temporary) / "second.zip"
            write_zip(root, first)
            time.sleep(0.01)
            source.touch()
            write_zip(root, second)
            self.assertEqual(first.read_bytes(), second.read_bytes())


if __name__ == "__main__":
    unittest.main()
