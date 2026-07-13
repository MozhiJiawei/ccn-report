from __future__ import annotations

import json
import sys
import tempfile
import unittest
from argparse import Namespace
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from export_singlefile_archive import (  # noqa: E402
    ExportResult,
    referenced_local_assets,
    serving_root_for,
    validate_singlefile_output,
    write_manifest,
)


class LocalAssetDiscoveryTests(unittest.TestCase):
    def test_discovers_local_assets_outside_root_from_html_and_css_urls(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            root = workspace / "pages"
            shared = workspace / "shared"
            root.mkdir()
            shared.mkdir()
            page = root / "index.html"
            image = shared / "hero image.png"
            font = shared / "font.woff2"
            linked_html = shared / "other.html"
            for asset in (image, font, linked_html):
                asset.write_bytes(b"asset")
            page.write_text(
                """
                <img src="../shared/hero%20image.png">
                <a href="../shared/font.woff2">font</a>
                <a href="../shared/other.html">other page</a>
                <div style="background: url('../shared/hero%20image.png')"></div>
                <img src="https://example.com/remote.png">
                """,
                encoding="utf-8",
            )

            self.assertEqual(referenced_local_assets(page, root), [image.resolve(), font.resolve()])
            self.assertEqual(serving_root_for([page], root), workspace.resolve())

    def test_keeps_original_root_when_all_assets_are_inside_it(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            page = root / "index.html"
            image = root / "assets" / "hero.png"
            image.parent.mkdir()
            image.write_bytes(b"image")
            page.write_text('<img src="assets/hero.png">', encoding="utf-8")

            self.assertEqual(serving_root_for([page], root), root.resolve())


class SingleFileOutputValidationTests(unittest.TestCase):
    def test_rejects_empty_data_image(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "output.html"
            output.write_text('<img src="data:">', encoding="utf-8")
            with self.assertRaisesRegex(RuntimeError, "empty data: image"):
                validate_singlefile_output(output)

    def test_accepts_populated_data_image(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "output.html"
            output.write_text('<img src="data:image/png;base64,AAAA">', encoding="utf-8")
            validate_singlefile_output(output)


class SingleFileManifestTests(unittest.TestCase):
    def test_records_original_and_served_roots(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            root = workspace / "pages"
            serve_root = workspace
            root.mkdir()
            manifest = workspace / "manifest.json"
            args = Namespace(
                root=root,
                manifest=manifest,
                quality=70,
                recursive_linked_html=False,
                max_depth=None,
            )
            result = ExportResult("ok", "input", "output", 1, 1, 0.1, 0, 0, 0, 0)

            write_manifest([result], args, serve_root)

            data = json.loads(manifest.read_text(encoding="utf-8"))
            self.assertEqual(data["root"], str(root.resolve()))
            self.assertEqual(data["served_root"], str(serve_root.resolve()))


if __name__ == "__main__":
    unittest.main()
