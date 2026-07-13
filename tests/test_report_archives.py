from __future__ import annotations

import sys
import tempfile
import time
import unittest
import zipfile
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from report_archive_layout import find_report_dirs, report_date  # noqa: E402
from release_compressed_archive import (  # noqa: E402
    copy_report_dirs,
    group_reports_by_month,
    select_release_changes,
    write_full_zip,
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
            "manifest_schema_version": 4,
            "packages": [
                {"filename": paths[0].name, "sha256": "same"},
                {"filename": paths[1].name, "sha256": "old"},
            ],
            "index": {"filename": "index.html", "sha256": "index-same"},
            "full_archive": {"filename": "ccn-report-full-q70.zip", "sha256": "full-same"},
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
        }
        changed_packages, changed_assets, obsolete = select_release_changes(
            paths,
            packages,
            Path("ccn-report-full-q70.zip"),
            {"filename": "ccn-report-full-q70.zip", "sha256": "full-same"},
            Path("index.html"),
            {"filename": "index.html", "sha256": "index-same"},
            previous,
            existing,
        )
        self.assertEqual(changed_packages, [paths[1]])
        self.assertEqual(changed_assets, [paths[1]])
        self.assertEqual(
            obsolete,
            {
                "ccn-report-20260713-q70.zip",
                "ccn-report-full-q60.zip",
                "ccn-report-latest-compressed-q70.zip",
            },
        )

    def test_incremental_selection_rejects_misaligned_package_records(self) -> None:
        with self.assertRaisesRegex(RuntimeError, "different lengths"):
            select_release_changes(
                [Path("ccn-report-202607-q70.zip")],
                [],
                Path("ccn-report-full-q70.zip"),
                {},
                Path("index.html"),
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

    def test_full_zip_combines_date_roots_without_index(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            first = root / "first"
            second = root / "second"
            (first / "分类A" / "对象" / "20260712-first-report-x").mkdir(parents=True)
            (second / "分类B" / "对象" / "20260713-second-report-x").mkdir(parents=True)
            (first / "分类A" / "对象" / "20260712-first-report-x" / "a.html").write_text("a")
            (second / "分类B" / "对象" / "20260713-second-report-x" / "b.html").write_text("b")
            archive = root / "full.zip"
            write_full_zip([first, second], archive)
            with zipfile.ZipFile(archive) as handle:
                self.assertEqual(
                    handle.namelist(),
                    [
                        "分类A/对象/20260712-first-report-x/a.html",
                        "分类B/对象/20260713-second-report-x/b.html",
                    ],
                )

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
