#!/usr/bin/env python3
"""Export local HTML files as dependency-free SingleFile HTML archives.

This is a generic exporter: it serves a chosen local root through HTTP, lets
SingleFile capture pages from that HTTP URL, optionally follows local HTML links,
rewrites captured local HTTP links back to relative file links, and writes a
manifest. It does not discover ccn-report reports and it does not clean source
directories; migration-specific orchestration belongs in separate one-off scripts.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import html
import http.server
import json
import mimetypes
import os
import re
import shutil
import subprocess
import tempfile
import threading
import time
from dataclasses import asdict, dataclass
from fnmatch import fnmatch
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit

try:
    from PIL import Image
except Exception:  # pragma: no cover - optional optimization.
    Image = None


SCRIPT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_WORK_DIR = Path(tempfile.gettempdir()) / "singlefile-html-archive"

HTML_EXTENSIONS = {".html", ".htm"}
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png"}
HREF_RE = re.compile(
    r"""href\s*=\s*(?:(?P<quote>["'])(?P<url_q>.*?)(?P=quote)|(?P<url_u>[^"'\s>]+))""",
    re.IGNORECASE | re.DOTALL,
)
LOCAL_HTTP_URL_RE = re.compile(r"""http://(?:127\.0\.0\.1|localhost):\d+/(?P<path>[^"'<>\s)]*)""")
LOCAL_CANONICAL_RE = re.compile(
    r"""<link\b(?=[^>]*\brel\s*=\s*["']?canonical\b)(?=[^>]*\bhref\s*=\s*["']?http://(?:127\.0\.0\.1|localhost):\d+/)[^>]*>""",
    re.IGNORECASE,
)


@dataclass
class ExportResult:
    status: str
    input: str
    output: str
    original_size: int
    output_size: int
    duration_seconds: float
    q70_converted: int
    q70_original_bytes: int
    q70_webp_bytes: int
    depth: int
    error: str = ""


class ArchiveHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    server_version = "SingleFileArchiveHTTP/1.0"

    def __init__(self, *args, directory: str, image_quality: int, image_cache: Path, **kwargs):
        self.image_quality = image_quality
        self.image_cache = image_cache
        super().__init__(*args, directory=directory, **kwargs)

    def log_message(self, format: str, *args: object) -> None:
        return

    def guess_type(self, path: str) -> str:
        return mimetypes.guess_type(path)[0] or "application/octet-stream"

    def send_head(self):  # noqa: N802 - stdlib API name.
        path = Path(self.translate_path(self.path))
        if path.is_dir():
            path = path / "index.html"
        compressed = compressed_image_for(path, self.image_quality, self.image_cache)
        if compressed:
            path = compressed
        if not path.exists() or not path.is_file():
            self.send_error(404, "File not found")
            return None
        try:
            handle = path.open("rb")
        except OSError:
            self.send_error(404, "File not found")
            return None
        self.send_response(200)
        self.send_header("Content-type", "image/webp" if compressed else self.guess_type(str(path)))
        self.send_header("Content-Length", str(path.stat().st_size))
        self.end_headers()
        return handle


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inputs", nargs="*", type=Path, help="HTML files to export.")
    parser.add_argument("--input-list", type=Path, help="UTF-8 text file containing HTML paths.")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Local root served over HTTP.")
    parser.add_argument("--output-dir", type=Path, help="Directory for exported HTML, mirroring --root paths.")
    parser.add_argument("--recursive-linked-html", action="store_true", help="Also export local HTML pages linked by inputs.")
    parser.add_argument("--max-depth", type=int, default=None, help="Maximum linked HTML recursion depth.")
    parser.add_argument(
        "--link-root",
        type=Path,
        help="Only follow linked HTML under this root. Defaults to --root.",
    )
    parser.add_argument(
        "--exclude-html-glob",
        action="append",
        default=[],
        help="Glob, relative to --root, for linked HTML to exclude. Can be repeated.",
    )
    parser.add_argument(
        "--unexported-html-link-action",
        choices=("keep", "hash"),
        default="keep",
        help="How to handle local HTML links that were not exported.",
    )
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--node-bin", default="node", help="Node.js executable used to run SingleFile.")
    parser.add_argument(
        "--single-file-node",
        type=Path,
        help="Path to single-file-cli/single-file-node.js. Defaults to SINGLEFILE_NODE or Node require.resolve().",
    )
    parser.add_argument("--quality", type=int, default=70, help="PNG/JPEG pre-compression WebP quality.")
    parser.add_argument("--timeout", type=int, default=120, help="SingleFile timeout per page, in seconds.")
    parser.add_argument("--work-dir", type=Path, default=DEFAULT_WORK_DIR, help="Temporary work directory.")
    parser.add_argument("--manifest", type=Path, help="Manifest path. Defaults to <work-dir>/manifest.json.")
    return parser.parse_args()


def is_remote_or_special(url: str) -> bool:
    lowered = url.strip().lower()
    return (
        not lowered
        or lowered.startswith(("#", "data:", "mailto:", "tel:", "javascript:", "about:", "http://", "https://", "//"))
    )


def href_value(match: re.Match[str]) -> str:
    return match.group("url_q") if match.group("url_q") is not None else match.group("url_u")


def href_attr(new_url: str, match: re.Match[str]) -> str:
    quote_char = match.group("quote")
    return f"href={quote_char}{new_url}{quote_char}" if quote_char else f"href={new_url}"


def ensure_under(path: Path, root: Path) -> Path | None:
    try:
        resolved = path.resolve()
        resolved.relative_to(root.resolve())
        return resolved
    except Exception:
        return None


def resolve_local(owner: Path, url: str, root: Path) -> Path | None:
    if is_remote_or_special(url):
        return None
    split = urlsplit(html.unescape(url.strip()))
    if split.scheme and split.scheme != "file":
        return None
    raw_path = unquote(split.path)
    candidate = root / raw_path.lstrip("/\\") if raw_path.startswith(("/", "\\")) else owner.parent / raw_path
    resolved = ensure_under(candidate, root)
    if not resolved:
        return None
    if resolved.is_dir():
        resolved = resolved / "index.html"
    return resolved if resolved.exists() else None


def read_inputs(args: argparse.Namespace, root: Path) -> list[Path]:
    raw_paths = list(args.inputs)
    if args.input_list:
        for line in args.input_list.read_text(encoding="utf-8-sig").splitlines():
            stripped = line.strip()
            if stripped and not stripped.startswith("#"):
                raw_paths.append(Path(stripped))
    inputs: list[Path] = []
    for raw in raw_paths:
        candidate = raw if raw.is_absolute() else root / raw
        resolved = ensure_under(candidate, root)
        if resolved and resolved.exists() and resolved.suffix.lower() in HTML_EXTENSIONS:
            inputs.append(resolved)
    return unique_sorted(inputs, root)


def unique_sorted(paths: list[Path], root: Path) -> list[Path]:
    seen: set[Path] = set()
    unique: list[Path] = []
    for path in paths:
        resolved = path.resolve()
        if resolved not in seen:
            seen.add(resolved)
            unique.append(resolved)
    return sorted(unique, key=lambda item: item.relative_to(root).as_posix().lower())


def is_excluded(path: Path, root: Path, patterns: list[str]) -> bool:
    rel = path.relative_to(root).as_posix()
    return any(fnmatch(rel, pattern) or fnmatch(path.name, pattern) for pattern in patterns)


def expand_linked_html(
    inputs: list[Path],
    root: Path,
    link_root: Path,
    max_depth: int | None,
    exclude_patterns: list[str],
) -> dict[Path, int]:
    depths = {path.resolve(): 0 for path in inputs}
    if max_depth == 0:
        return depths
    queue = list(depths)
    while queue:
        path = queue.pop(0)
        depth = depths[path]
        if max_depth is not None and depth >= max_depth:
            continue
        try:
            content = path.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        for match in HREF_RE.finditer(content):
            target = resolve_local(path, href_value(match), root)
            if not target or target.suffix.lower() not in HTML_EXTENSIONS:
                continue
            if not ensure_under(target, link_root):
                continue
            if is_excluded(target, root, exclude_patterns):
                continue
            target = target.resolve()
            if target not in depths:
                depths[target] = depth + 1
                queue.append(target)
    return dict(sorted(depths.items(), key=lambda item: item[0].relative_to(root).as_posix().lower()))


def cache_name(path: Path, quality: int) -> str:
    stat = path.stat()
    key = f"{path.resolve()}|{stat.st_mtime_ns}|{stat.st_size}|q{quality}"
    return hashlib.sha1(key.encode("utf-8")).hexdigest()


def compressed_image_for(path: Path, quality: int, cache_dir: Path) -> Path | None:
    if Image is None or path.suffix.lower() not in IMAGE_EXTENSIONS or not path.exists():
        return None
    cache_dir.mkdir(parents=True, exist_ok=True)
    target = cache_dir / f"{cache_name(path, quality)}.webp"
    meta = target.with_suffix(".json")
    if not meta.exists():
        original_size = path.stat().st_size
        tmp = target.with_suffix(".tmp")
        result = {"use_compressed": False, "original_size": original_size, "webp_size": 0, "source": str(path)}
        try:
            with Image.open(path) as image:
                if image.mode not in {"RGB", "RGBA"}:
                    image = image.convert("RGBA" if "A" in image.getbands() else "RGB")
                image.save(tmp, "WEBP", quality=quality, method=6)
            webp_size = tmp.stat().st_size
            result["webp_size"] = webp_size
            if webp_size < original_size:
                tmp.replace(target)
                result["use_compressed"] = True
            else:
                tmp.unlink(missing_ok=True)
        except Exception as exc:
            tmp.unlink(missing_ok=True)
            result["error"] = str(exc)
        meta.write_text(json.dumps(result, ensure_ascii=False), encoding="utf-8")
    result = json.loads(meta.read_text(encoding="utf-8"))
    return target if result.get("use_compressed") and target.exists() else None


def image_cache_stats(cache_dir: Path) -> tuple[int, int, int]:
    converted = 0
    original = 0
    webp = 0
    for meta in cache_dir.glob("*.json"):
        try:
            data = json.loads(meta.read_text(encoding="utf-8"))
        except Exception:
            continue
        if data.get("use_compressed"):
            converted += 1
            original += int(data.get("original_size") or 0)
            webp += int(data.get("webp_size") or 0)
    return converted, original, webp


def start_server(root: Path, quality: int, cache_dir: Path) -> tuple[http.server.ThreadingHTTPServer, str]:
    def factory(*args, **kwargs):
        return ArchiveHTTPRequestHandler(*args, directory=str(root), image_quality=quality, image_cache=cache_dir, **kwargs)

    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), factory)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server, f"http://127.0.0.1:{server.server_port}"


def resolve_single_file_node(args: argparse.Namespace) -> Path:
    if args.single_file_node:
        candidate = args.single_file_node.resolve()
        if candidate.exists():
            return candidate
        raise SystemExit(f"SingleFile node entry not found: {candidate}")

    env_value = os.environ.get("SINGLEFILE_NODE")
    if env_value:
        candidate = Path(env_value).expanduser().resolve()
        if candidate.exists():
            return candidate
        raise SystemExit(f"SINGLEFILE_NODE does not exist: {candidate}")

    node_bin = shutil.which(args.node_bin) or args.node_bin
    probe = "console.log(require.resolve('single-file-cli/single-file-node.js'))"
    probe_dirs: list[Path] = []
    seen_dirs: set[Path] = set()
    for candidate in (Path.cwd(), SCRIPT_ROOT, args.root):
        resolved = candidate.resolve()
        if resolved not in seen_dirs:
            seen_dirs.add(resolved)
            probe_dirs.append(resolved)
    for cwd in probe_dirs:
        completed = subprocess.run(
            [node_bin, "-e", probe],
            cwd=cwd,
            text=True,
            capture_output=True,
            timeout=10,
            check=False,
        )
        if completed.returncode == 0:
            candidate = Path(completed.stdout.strip()).resolve()
            if candidate.exists():
                return candidate

    raise SystemExit(
        "SingleFile node entry not found. Install single-file-cli where Node can resolve it, "
        "set SINGLEFILE_NODE, or pass --single-file-node."
    )


def singlefile_args(url: str, output: Path) -> list[str]:
    return [
        url,
        str(output),
        "--filename-conflict-action=overwrite",
        "--browser-wait-until=load",
        "--browser-load-max-time=30000",
        "--browser-capture-max-time=30000",
        "--block-scripts=false",
        "--block-fonts=false",
        "--remove-hidden-elements=false",
        "--remove-unused-styles=false",
        "--insert-single-file-comment=false",
        "--remove-saved-date=true",
    ]


def artifact_path(kind: str, path: Path, root: Path, work_dir: Path) -> Path:
    rel = path.relative_to(root).as_posix()
    digest = hashlib.sha1(rel.encode("utf-8")).hexdigest()[:16]
    return work_dir / kind / f"{digest}-{path.name}"


def output_path_for(path: Path, args: argparse.Namespace, root: Path) -> Path:
    if not args.output_dir:
        raise ValueError("Use --output-dir.")
    return args.output_dir.resolve() / path.relative_to(root)


def rewrite_local_http_links(html_path: Path, owner: Path, root: Path) -> None:
    try:
        content = html_path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return

    def replace(match: re.Match[str]) -> str:
        raw = match.group("path")
        split = urlsplit(raw)
        target_rel = unquote(split.path)
        target = (root / target_rel).resolve()
        try:
            target.relative_to(root.resolve())
        except ValueError:
            return match.group(0)
        if target == root.resolve():
            return "#"
        rel = os.path.relpath(target, owner.parent).replace("\\", "/")
        if split.query:
            rel += f"?{split.query}"
        if split.fragment:
            rel += f"#{split.fragment}"
        return rel

    rewritten = LOCAL_CANONICAL_RE.sub("", content)
    rewritten = LOCAL_HTTP_URL_RE.sub(replace, rewritten)
    if rewritten != content:
        html_path.write_text(rewritten, encoding="utf-8")


def rewrite_unexported_html_links(output: Path, source: Path, root: Path, exported_sources: set[Path], action: str) -> None:
    if action == "keep":
        return
    try:
        content = output.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return

    def replace(match: re.Match[str]) -> str:
        quote_char = match.group("quote")
        url = href_value(match)
        target = resolve_local(source, url, root)
        if not target or target.suffix.lower() not in HTML_EXTENSIONS:
            return match.group(0)
        if target.resolve() in exported_sources:
            return match.group(0)
        return href_attr("#", match)

    rewritten = HREF_RE.sub(replace, content)
    if rewritten != content:
        output.write_text(rewritten, encoding="utf-8")


def export_one(path: Path, depth: int, base_url: str, args: argparse.Namespace, root: Path, cache_dir: Path) -> ExportResult:
    rel = path.relative_to(root).as_posix()
    url = f"{base_url}/{quote(rel, safe='/')}"
    final_output = output_path_for(path, args, root)
    temp_output = artifact_path("outputs", path, root, args.work_dir)
    temp_output.parent.mkdir(parents=True, exist_ok=True)
    original_size = path.stat().st_size
    before = image_cache_stats(cache_dir)
    started = time.perf_counter()
    try:
        if not args.dry_run:
            node_bin = shutil.which(args.node_bin) or args.node_bin
            completed = subprocess.run(
                [node_bin, str(args.single_file_node), *singlefile_args(url, temp_output)],
                cwd=args.root,
                text=True,
                capture_output=True,
                timeout=args.timeout,
                check=False,
            )
            if completed.returncode or not temp_output.exists():
                raise RuntimeError((completed.stderr or completed.stdout or "SingleFile failed").strip()[:2000])
            rewrite_local_http_links(temp_output, path, root)
            final_output.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(temp_output, final_output)
        after = image_cache_stats(cache_dir)
        return ExportResult(
            status="ok",
            input=str(path),
            output=str(final_output),
            original_size=original_size,
            output_size=final_output.stat().st_size if final_output.exists() else 0,
            duration_seconds=round(time.perf_counter() - started, 3),
            q70_converted=after[0] - before[0],
            q70_original_bytes=after[1] - before[1],
            q70_webp_bytes=after[2] - before[2],
            depth=depth,
        )
    except Exception as exc:
        return ExportResult(
            status="failed",
            input=str(path),
            output=str(final_output),
            original_size=original_size,
            output_size=final_output.stat().st_size if final_output.exists() else 0,
            duration_seconds=round(time.perf_counter() - started, 3),
            q70_converted=0,
            q70_original_bytes=0,
            q70_webp_bytes=0,
            depth=depth,
            error=str(exc),
        )


def write_manifest(results: list[ExportResult], args: argparse.Namespace) -> None:
    args.manifest.parent.mkdir(parents=True, exist_ok=True)
    data = {
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "root": str(args.root.resolve()),
        "quality": args.quality,
        "recursive_linked_html": args.recursive_linked_html,
        "max_depth": args.max_depth,
        "counts": {
            "total": len(results),
            "ok": sum(1 for item in results if item.status == "ok"),
            "failed": sum(1 for item in results if item.status != "ok"),
        },
        "results": [asdict(item) for item in results],
    }
    args.manifest.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    csv_path = args.manifest.with_suffix(".csv")
    with csv_path.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(asdict(results[0]).keys()) if results else ["status"])
        writer.writeheader()
        for result in results:
            writer.writerow(asdict(result))


def main() -> int:
    args = parse_args()
    args.root = args.root.resolve()
    args.work_dir = args.work_dir.resolve()
    args.manifest = (args.manifest or args.work_dir / "manifest.json").resolve()
    if not args.output_dir:
        raise SystemExit("Use --output-dir.")
    args.single_file_node = resolve_single_file_node(args)

    inputs = read_inputs(args, args.root)
    if not inputs:
        raise SystemExit("No input HTML files found.")
    link_root = (args.link_root or args.root).resolve()
    depths = (
        expand_linked_html(inputs, args.root, link_root, args.max_depth, args.exclude_html_glob)
        if args.recursive_linked_html
        else {path: 0 for path in inputs}
    )

    cache_dir = args.work_dir / "image-cache"
    server, base_url = start_server(args.root, args.quality, cache_dir)
    try:
        results = [export_one(path, depth, base_url, args, args.root, cache_dir) for path, depth in depths.items()]
    finally:
        server.shutdown()
    exported_sources = {path.resolve() for path, _ in depths.items()}
    if args.unexported_html_link_action != "keep":
        for result in results:
            if result.status != "ok":
                continue
            rewrite_unexported_html_links(
                Path(result.output),
                Path(result.input),
                args.root,
                exported_sources,
                args.unexported_html_link_action,
            )
    write_manifest(results, args)
    print(
        json.dumps(
            {
                "total": len(results),
                "ok": sum(1 for item in results if item.status == "ok"),
                "failed": sum(1 for item in results if item.status != "ok"),
            },
            ensure_ascii=False,
        )
    )
    return 0 if all(item.status == "ok" for item in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
