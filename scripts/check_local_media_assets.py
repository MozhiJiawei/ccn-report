from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


REPO_ROOT = Path(__file__).resolve().parents[1]
REPORT_ROOTS = ("大厂动态", "开源软件分析", "学术论文分析")
DOCUMENT_EXTENSIONS = {".html", ".htm", ".md", ".markdown"}
IMAGE_EXTENSIONS = {
    ".avif",
    ".bmp",
    ".gif",
    ".ico",
    ".jpeg",
    ".jpg",
    ".png",
    ".svg",
    ".webp",
}
EXTERNAL_SCHEMES = {
    "about",
    "blob",
    "chrome",
    "cid",
    "data",
    "http",
    "https",
    "javascript",
    "mailto",
    "tel",
}
CSS_URL_RE = re.compile(r"url\(\s*(?P<quote>['\"]?)(?P<url>.*?)(?P=quote)\s*\)", re.IGNORECASE | re.DOTALL)
QUOTED_IMAGE_PATH_RE = re.compile(
    r"(?P<quote>['\"])(?P<url>(?:\.{0,2}[\\/]|[^'\"]*[\\/])[^'\"]+\.(?:avif|bmp|gif|ico|jpe?g|png|svg|webp)(?:[?#][^'\"]*)?)(?P=quote)",
    re.IGNORECASE,
)
MARKDOWN_INLINE_IMAGE_RE = re.compile(r"!\[[^\]]*\]\(\s*(?P<url><[^>]+>|[^)\n]+?)\s*\)")
MARKDOWN_REFERENCE_IMAGE_RE = re.compile(r"!\[[^\]]*\]\[(?P<label>[^\]]*)\]")
MARKDOWN_REFERENCE_DEF_RE = re.compile(r"^\s*\[(?P<label>[^\]]+)\]:\s*(?P<url><[^>]+>|\S+)", re.MULTILINE)
MAX_DISPLAYED_ERRORS = 100


@dataclass(frozen=True)
class Reference:
    document_path: Path
    raw_url: str
    line: int
    source: str


class LocalImageReferenceParser(HTMLParser):
    def __init__(self, document_path: Path) -> None:
        super().__init__(convert_charrefs=True)
        self.document_path = document_path
        self.references: list[Reference] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self._collect_tag_references(tag.lower(), attrs)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self._collect_tag_references(tag.lower(), attrs)

    def _collect_tag_references(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        line, _ = self.getpos()
        attr_map = {name.lower(): value for name, value in attrs if value is not None}

        if tag in {"img", "image"}:
            self._add_attr(attr_map, "src", line, f"<{tag}> src")
            self._add_attr(attr_map, "href", line, f"<{tag}> href")
            self._add_attr(attr_map, "xlink:href", line, f"<{tag}> xlink:href")
            self._add_srcset(attr_map.get("srcset"), line, f"<{tag}> srcset")
            return

        if tag == "source":
            self._add_srcset(attr_map.get("srcset"), line, "<source> srcset")
            if (attr_map.get("type") or "").lower().startswith("image/"):
                self._add_attr(attr_map, "src", line, "<source> src")
            return

        if tag == "input" and (attr_map.get("type") or "").lower() == "image":
            self._add_attr(attr_map, "src", line, "<input type=image> src")
            return

        if tag == "video":
            self._add_attr(attr_map, "poster", line, "<video> poster")
            return

        if tag == "link":
            rel = (attr_map.get("rel") or "").lower()
            content_type = (attr_map.get("type") or "").lower()
            if "icon" in rel or content_type.startswith("image/"):
                self._add_attr(attr_map, "href", line, "<link> href")

    def _add_attr(self, attr_map: dict[str, str], attr_name: str, line: int, source: str) -> None:
        value = attr_map.get(attr_name)
        if value:
            self.references.append(Reference(self.document_path, value, line, source))

    def _add_srcset(self, value: str | None, line: int, source: str) -> None:
        if not value:
            return
        for candidate in parse_srcset(value):
            self.references.append(Reference(self.document_path, candidate, line, source))


def parse_srcset(value: str) -> list[str]:
    candidates: list[str] = []
    for part in value.split(","):
        stripped = part.strip()
        if stripped:
            candidates.append(stripped.split()[0])
    return candidates


def strip_markdown_angle_brackets(raw_url: str) -> str:
    stripped = raw_url.strip()
    if stripped.startswith("<") and stripped.endswith(">"):
        return stripped[1:-1].strip()
    return stripped


def strip_markdown_title(raw_url: str) -> str:
    stripped = strip_markdown_angle_brackets(raw_url)
    title_match = re.match(r"^(?P<url>.+?)\s+(['\"]).*\2\s*$", stripped)
    if title_match and has_image_extension(clean_local_url(title_match.group("url"))):
        return title_match.group("url")
    return stripped


def is_probably_template_url(raw_url: str) -> bool:
    return "${" in raw_url or "{{" in raw_url or "}}" in raw_url


def is_external_or_inline(raw_url: str) -> bool:
    stripped = strip_markdown_title(raw_url)
    if not stripped or stripped.startswith("#") or stripped.startswith("//"):
        return True
    split = urlsplit(stripped)
    scheme = split.scheme.lower()
    return scheme in EXTERNAL_SCHEMES


def clean_local_url(raw_url: str) -> str:
    stripped = strip_markdown_angle_brackets(raw_url)
    drive_path_match = re.match(r"^[A-Za-z]:[\\/]", stripped)
    if drive_path_match:
        return stripped
    split = urlsplit(stripped)
    return unquote(split.path)


def has_image_extension(url_path: str) -> bool:
    return Path(url_path).suffix.lower() in IMAGE_EXTENSIONS


def resolve_local_path(document_path: Path, raw_url: str) -> Path | None:
    url_path = clean_local_url(raw_url)
    if not url_path:
        return None

    normalized = url_path.replace("\\", "/")
    if normalized.startswith("/"):
        return None

    candidate = Path(url_path)
    if candidate.is_absolute():
        return candidate.resolve()
    return (document_path.parent / normalized).resolve()


def is_inside_repo(path: Path) -> bool:
    try:
        path.relative_to(REPO_ROOT)
    except ValueError:
        return False
    return True


def is_file(path: Path) -> bool:
    if path.is_file():
        return True
    if sys.platform == "win32":
        return Path("\\\\?\\" + str(path)).is_file()
    return False


def line_for_match(text: str, start_index: int) -> int:
    return text.count("\n", 0, start_index) + 1


def collect_html_references(document_path: Path, text: str) -> list[Reference]:
    parser = LocalImageReferenceParser(document_path)
    parser.feed(text)
    return parser.references


def collect_css_url_references(document_path: Path, text: str) -> list[Reference]:
    references: list[Reference] = []
    for match in CSS_URL_RE.finditer(text):
        raw_url = match.group("url").strip()
        if has_image_extension(clean_local_url(raw_url)):
            references.append(Reference(document_path, raw_url, line_for_match(text, match.start()), "CSS url()"))
    return references


def collect_quoted_image_path_references(document_path: Path, text: str) -> list[Reference]:
    references: list[Reference] = []
    for match in QUOTED_IMAGE_PATH_RE.finditer(text):
        references.append(
            Reference(
                document_path,
                match.group("url"),
                line_for_match(text, match.start()),
                "quoted image path",
            )
        )
    return references


def collect_markdown_image_references(document_path: Path, text: str) -> list[Reference]:
    references: list[Reference] = []

    reference_defs: dict[str, tuple[str, int]] = {}
    for match in MARKDOWN_REFERENCE_DEF_RE.finditer(text):
        label = match.group("label").strip().lower()
        reference_defs[label] = (
            strip_markdown_angle_brackets(match.group("url")),
            line_for_match(text, match.start()),
        )

    for match in MARKDOWN_INLINE_IMAGE_RE.finditer(text):
        references.append(
            Reference(
                document_path,
                strip_markdown_title(match.group("url")),
                line_for_match(text, match.start()),
                "Markdown image",
            )
        )

    for match in MARKDOWN_REFERENCE_IMAGE_RE.finditer(text):
        label = match.group("label").strip().lower()
        if not label:
            alt_start = text.rfind("![", 0, match.start())
            alt_text = text[alt_start + 2 : match.start()] if alt_start >= 0 else ""
            label = alt_text.strip().lower()
        definition = reference_defs.get(label)
        if definition:
            raw_url, definition_line = definition
            references.append(Reference(document_path, raw_url, definition_line, "Markdown reference image"))

    return references


def collect_references(document_path: Path) -> list[Reference]:
    text = document_path.read_text(encoding="utf-8", errors="replace")
    references = [*collect_html_references(document_path, text), *collect_css_url_references(document_path, text)]

    if document_path.suffix.lower() in {".html", ".htm"}:
        references.extend(collect_quoted_image_path_references(document_path, text))
    else:
        references.extend(collect_markdown_image_references(document_path, text))

    return references


def should_check_reference(reference: Reference) -> bool:
    if is_probably_template_url(reference.raw_url) or is_external_or_inline(reference.raw_url):
        return False
    return has_image_extension(clean_local_url(reference.raw_url))


def validate_reference(reference: Reference) -> str | None:
    raw_url = reference.raw_url.strip()
    url_path = clean_local_url(raw_url)

    if url_path.replace("\\", "/").startswith("/"):
        return (
            f"{reference.document_path.relative_to(REPO_ROOT)}:{reference.line}: "
            f"{reference.source} uses root-absolute local image path {raw_url!r}. "
            "Use a relative path and archive the image with the report."
        )

    target = resolve_local_path(reference.document_path, raw_url)
    if target is None:
        return None
    if not is_inside_repo(target):
        return (
            f"{reference.document_path.relative_to(REPO_ROOT)}:{reference.line}: "
            f"{reference.source} points outside ccn-report: {raw_url!r}. "
            "Copy the image into the report directory and reference it with a relative path."
        )
    if not is_file(target):
        return (
            f"{reference.document_path.relative_to(REPO_ROOT)}:{reference.line}: "
            f"{reference.source} references missing local image {raw_url!r}."
        )
    return None


def iter_documents() -> list[Path]:
    documents: list[Path] = []
    for root_name in REPORT_ROOTS:
        root = REPO_ROOT / root_name
        if root.is_dir():
            documents.extend(path for path in root.rglob("*") if path.is_file() and path.suffix.lower() in DOCUMENT_EXTENSIONS)
    return sorted(documents)


def main() -> int:
    errors: list[str] = []
    seen: set[tuple[Path, int, str]] = set()

    for document_path in iter_documents():
        for reference in collect_references(document_path):
            if not should_check_reference(reference):
                continue
            key = (reference.document_path, reference.line, reference.raw_url)
            if key in seen:
                continue
            seen.add(key)
            error = validate_reference(reference)
            if error:
                errors.append(error)

    if errors:
        print("Local media asset validation failed:")
        for error in errors[:MAX_DISPLAYED_ERRORS]:
            print(f"- {error}")
        if len(errors) > MAX_DISPLAYED_ERRORS:
            print(f"- ... {len(errors) - MAX_DISPLAYED_ERRORS} more missing or invalid local image references")
        return 1

    print("Local media asset validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
