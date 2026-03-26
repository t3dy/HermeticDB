"""
convert_pdfs_to_md.py — Batch convert PDFs to markdown.

Scans hermetic/ folder and project root for PDFs.
Uses PyMuPDF (fitz) for text extraction.
Reports which PDFs are scanned images (need OCR) vs text-extractable.

Output: .md files alongside the source PDFs.
Idempotent: skips PDFs that already have a .md companion.
"""

import fitz  # PyMuPDF
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
HERMETIC_DIR = BASE_DIR / "hermetic"

# Minimum chars per page to consider it "has text"
MIN_CHARS_PER_PAGE = 50
# Sample first N pages to check for text
SAMPLE_PAGES = 5


def slugify_filename(pdf_path):
    """Create a clean .md filename from the PDF name."""
    stem = pdf_path.stem
    # Truncate very long filenames
    if len(stem) > 120:
        stem = stem[:120]
    return stem + ".md"


def extract_text(pdf_path):
    """Extract text from a PDF. Returns (text, page_count, text_pages, empty_pages)."""
    doc = fitz.open(str(pdf_path))
    page_count = len(doc)
    lines = []
    text_pages = 0
    empty_pages = 0

    for i in range(page_count):
        page = doc[i]
        text = page.get_text().strip()
        if len(text) >= MIN_CHARS_PER_PAGE:
            text_pages += 1
            lines.append(f"## Page {i + 1}\n")
            lines.append(text)
            lines.append("")
        else:
            empty_pages += 1

    doc.close()
    return "\n".join(lines), page_count, text_pages, empty_pages


def guess_title(pdf_path):
    """Extract a reasonable title from the filename."""
    name = pdf_path.stem
    # Strip common suffixes
    name = re.sub(r'\s*-?\s*libgen[\._]li$', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\{[^}]*\}', '', name)  # Remove {metadata}
    name = re.sub(r'\[[\d\._]+\]', '', name)  # Remove [DOI]
    name = re.sub(r'\(\d{4}[^)]*\)', '', name)  # Remove (year, publisher)
    name = re.sub(r'\s+', ' ', name).strip()
    # Truncate
    if len(name) > 200:
        name = name[:200] + "..."
    return name


def convert_pdf(pdf_path, output_dir=None, force=False):
    """Convert a single PDF to markdown. Returns status dict."""
    if output_dir is None:
        output_dir = pdf_path.parent

    md_filename = slugify_filename(pdf_path)
    md_path = output_dir / md_filename

    if md_path.exists() and not force:
        return {"status": "skipped", "path": str(pdf_path), "reason": "md already exists"}

    try:
        text, page_count, text_pages, empty_pages = extract_text(pdf_path)
    except Exception as e:
        return {"status": "error", "path": str(pdf_path), "error": str(e)}

    text_ratio = text_pages / page_count if page_count > 0 else 0

    if text_pages == 0:
        return {
            "status": "scanned",
            "path": str(pdf_path),
            "pages": page_count,
            "reason": "No extractable text (scanned images). Needs OCR."
        }

    title = guess_title(pdf_path)
    header = f"# {title}\n\n"
    header += f"*Source: {pdf_path.name}*\n"
    header += f"*Pages: {page_count} total, {text_pages} with text, {empty_pages} empty/scanned*\n\n"

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(header)
        f.write(text)

    return {
        "status": "converted",
        "path": str(pdf_path),
        "output": str(md_path),
        "pages": page_count,
        "text_pages": text_pages,
        "empty_pages": empty_pages,
        "text_ratio": f"{text_ratio:.0%}"
    }


def main():
    force = "--force" in sys.argv

    # Collect all PDFs
    pdfs = []

    # Root directory PDFs (skip already-converted ones)
    for pdf in sorted(BASE_DIR.glob("*.pdf")):
        pdfs.append(pdf)

    # Hermetic folder PDFs
    if HERMETIC_DIR.exists():
        for pdf in sorted(HERMETIC_DIR.glob("*.pdf")):
            pdfs.append(pdf)

    print(f"Found {len(pdfs)} PDFs to process\n")

    converted = []
    skipped = []
    scanned = []
    errors = []

    for i, pdf in enumerate(pdfs, 1):
        size_mb = pdf.stat().st_size / (1024 * 1024)
        safe_name = pdf.name[:80].encode('ascii', errors='replace').decode('ascii')
        print(f"[{i}/{len(pdfs)}] ({size_mb:.1f} MB) {safe_name}...")

        # Skip very large scanned PDFs (>100MB) — they'll be slow and likely scanned
        if size_mb > 100:
            result = {"status": "skipped_large", "path": str(pdf), "size_mb": f"{size_mb:.0f}",
                      "reason": f"Skipped: {size_mb:.0f}MB — too large, likely scanned. Convert manually if needed."}
            skipped.append(result)
            print(f"  SKIPPED (>{100}MB)")
            continue

        result = convert_pdf(pdf, force=force)
        status = result["status"]

        if status == "converted":
            converted.append(result)
            print(f"  CONVERTED ({result['text_pages']}/{result['pages']} pages, {result['text_ratio']})")
        elif status == "skipped":
            skipped.append(result)
            print(f"  SKIPPED (already exists)")
        elif status == "scanned":
            scanned.append(result)
            print(f"  SCANNED ({result['pages']} pages — needs OCR)")
        elif status == "skipped_large":
            skipped.append(result)
        else:
            errors.append(result)
            print(f"  ERROR: {result.get('error', 'unknown')}")

    # Summary
    print(f"\n{'='*60}")
    print(f"CONVERSION SUMMARY")
    print(f"{'='*60}")
    print(f"  Converted:    {len(converted)}")
    print(f"  Skipped:      {len(skipped)}")
    print(f"  Scanned/OCR:  {len(scanned)}")
    print(f"  Errors:       {len(errors)}")

    if scanned:
        print(f"\nSCANNED PDFs (need OCR):")
        for s in scanned:
            name = Path(s['path']).name[:80].encode('ascii', errors='replace').decode('ascii')
            print(f"  [{s['pages']} pages] {name}")

    if errors:
        print(f"\nERRORS:")
        for e in errors:
            name = Path(e['path']).name[:80].encode('ascii', errors='replace').decode('ascii')
            print(f"  {name}: {e.get('error')}")


if __name__ == "__main__":
    main()
