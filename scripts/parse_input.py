#!/usr/bin/env python3
"""
Universal e-book / article parser for the book-reader skill.

Usage:
    python parse_input.py <file_path> [--output json|text] [--max-chars N]

Supported formats: .pdf, .epub, .docx, .txt, .md, .html, .htm
Output:
    text  - plain text (default)
    json  - { "text": "...", "metadata": { title, author, chapter_count, chapters }, "format": "..." }

Dependencies:
    pip install pdfplumber ebooklib beautifulsoup4 python-docx lxml
"""

import argparse
import json
import os
import sys
import re
from pathlib import Path


# ---------------------------------------------------------------------------
# Format-specific parsers
# ---------------------------------------------------------------------------

def parse_pdf(file_path: str) -> tuple:
    """Extract text and chapter headings from a PDF file."""
    import pdfplumber

    text_parts = []
    chapters = []

    with pdfplumber.open(file_path) as pdf:
        for i, page in enumerate(pdf.pages):
            page_text = page.extract_text() or ""
            text_parts.append(page_text)

        full_text = "\n\n".join(text_parts)

    # Heuristic chapter detection: lines that look like headings
    for line in full_text.split("\n"):
        stripped = line.strip()
        if stripped and (
            re.match(r"^(第[一二三四五六七八九十百千]+[章节篇部])", stripped)
            or re.match(r"^(Chapter|CHAPTER)\s+\d+", stripped)
            or re.match(r"^(Part|PART)\s+[IVX\d]+", stripped)
        ):
            chapters.append(stripped[:80])

    metadata = {
        "title": Path(file_path).stem,
        "author": "",
        "chapter_count": len(chapters),
        "chapters": chapters[:50],  # cap to avoid huge metadata
    }
    return full_text, metadata


def parse_epub(file_path: str) -> tuple:
    """Extract text and metadata from an EPUB file."""
    import ebooklib
    from ebooklib import epub
    from bs4 import BeautifulSoup

    book = epub.read_epub(file_path, options={"ignore_ncx": True})

    # Metadata
    titles = book.get_metadata("DC", "title")
    authors = book.get_metadata("DC", "creator")
    title = titles[0][0] if titles else Path(file_path).stem
    author = authors[0][0] if authors else ""

    text_parts = []
    chapters = []

    for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        soup = BeautifulSoup(item.get_content(), "lxml")
        body = soup.find("body")
        if not body:
            continue
        chapter_text = body.get_text(separator="\n", strip=True)
        if len(chapter_text) < 50:
            continue
        text_parts.append(chapter_text)

        # Try to extract chapter title from first heading
        heading = body.find(re.compile(r"^h[1-3]$"))
        if heading:
            chapters.append(heading.get_text(strip=True)[:80])

    full_text = "\n\n".join(text_parts)
    metadata = {
        "title": title,
        "author": author,
        "chapter_count": len(chapters),
        "chapters": chapters[:50],
    }
    return full_text, metadata


def parse_docx(file_path: str) -> tuple:
    """Extract text and heading structure from a DOCX file."""
    from docx import Document

    doc = Document(file_path)
    text_parts = []
    chapters = []

    for para in doc.paragraphs:
        text = para.text.strip()
        if not text:
            continue
        text_parts.append(text)

        # Detect headings by style
        if para.style and para.style.name and "Heading" in para.style.name:
            chapters.append(text[:80])

    full_text = "\n\n".join(text_parts)
    metadata = {
        "title": Path(file_path).stem,
        "author": "",
        "chapter_count": len(chapters),
        "chapters": chapters[:50],
    }
    return full_text, metadata


def parse_txt(file_path: str) -> tuple:
    """Read a plain text or markdown file."""
    # Try common encodings
    for encoding in ["utf-8", "utf-8-sig", "gbk", "gb2312", "latin-1"]:
        try:
            with open(file_path, "r", encoding=encoding) as f:
                text = f.read()
            break
        except (UnicodeDecodeError, UnicodeError):
            continue
    else:
        raise ValueError(f"Cannot decode file: {file_path}")

    # Try to extract title from first non-empty line
    lines = [l.strip() for l in text.split("\n") if l.strip()]
    title = lines[0][:80] if lines else Path(file_path).stem
    # Remove markdown heading markers
    if title.startswith("#"):
        title = title.lstrip("#").strip()

    # Detect markdown headings as chapters
    chapters = []
    for line in text.split("\n"):
        match = re.match(r"^#{1,3}\s+(.+)", line.strip())
        if match:
            chapters.append(match.group(1).strip()[:80])

    metadata = {
        "title": title,
        "author": "",
        "chapter_count": len(chapters),
        "chapters": chapters[:50],
    }
    return text, metadata


def parse_html(file_path: str) -> tuple:
    """Extract text from an HTML file."""
    from bs4 import BeautifulSoup

    for encoding in ["utf-8", "utf-8-sig", "gbk", "gb2312", "latin-1"]:
        try:
            with open(file_path, "r", encoding=encoding) as f:
                content = f.read()
            break
        except (UnicodeDecodeError, UnicodeError):
            continue
    else:
        raise ValueError(f"Cannot decode file: {file_path}")

    soup = BeautifulSoup(content, "lxml")

    # Extract title
    title_tag = soup.find("title")
    h1_tag = soup.find("h1")
    title = ""
    if title_tag:
        title = title_tag.get_text(strip=True)
    elif h1_tag:
        title = h1_tag.get_text(strip=True)
    else:
        title = Path(file_path).stem

    # Extract body text
    body = soup.find("body") or soup
    text = body.get_text(separator="\n", strip=True)

    # Detect headings
    chapters = []
    for h in soup.find_all(re.compile(r"^h[1-3]$")):
        chapters.append(h.get_text(strip=True)[:80])

    metadata = {
        "title": title,
        "author": "",
        "chapter_count": len(chapters),
        "chapters": chapters[:50],
    }
    return text, metadata


# ---------------------------------------------------------------------------
# Router
# ---------------------------------------------------------------------------

PARSERS = {
    ".pdf": parse_pdf,
    ".epub": parse_epub,
    ".docx": parse_docx,
    ".txt": parse_txt,
    ".md": parse_txt,
    ".html": parse_html,
    ".htm": parse_html,
}


def parse(file_path: str, max_chars: int = 0) -> dict:
    """
    Parse a file and return structured result.

    Args:
        file_path: Path to the input file.
        max_chars: If > 0, truncate text to this many characters.

    Returns:
        dict with keys: text, metadata, format
    """
    ext = Path(file_path).suffix.lower()
    if ext not in PARSERS:
        raise ValueError(f"Unsupported format: {ext}. Supported: {', '.join(PARSERS.keys())}")

    text, metadata = PARSERS[ext](file_path)

    # Clean up whitespace
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r" {2,}", " ", text)
    text = text.strip()

    original_length = len(text)
    if max_chars > 0 and len(text) > max_chars:
        text = text[:max_chars]
        metadata["truncated"] = True
        metadata["original_length"] = original_length

    return {
        "text": text,
        "metadata": metadata,
        "format": ext.lstrip("."),
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Universal e-book / article parser for book-reader skill"
    )
    parser.add_argument("file_path", help="Path to the input file")
    parser.add_argument(
        "--output", "-o",
        choices=["text", "json"],
        default="text",
        help="Output format (default: text)",
    )
    parser.add_argument(
        "--max-chars", "-m",
        type=int,
        default=0,
        help="Max characters to extract (0 = no limit)",
    )
    parser.add_argument(
        "--metadata-only",
        action="store_true",
        help="Output only metadata (JSON mode only)",
    )

    args = parser.parse_args()

    if not os.path.isfile(args.file_path):
        print(f"Error: File not found: {args.file_path}", file=sys.stderr)
        sys.exit(1)

    try:
        result = parse(args.file_path, max_chars=args.max_chars)
    except ImportError as e:
        print(f"Error: Missing dependency — {e}", file=sys.stderr)
        print("Install with: pip install pdfplumber ebooklib beautifulsoup4 python-docx lxml", file=sys.stderr)
        sys.exit(2)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    if args.output == "json":
        if args.metadata_only:
            print(json.dumps(result["metadata"], ensure_ascii=False, indent=2))
        else:
            print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(result["text"])


if __name__ == "__main__":
    main()
