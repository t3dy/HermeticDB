"""
segment_texts.py — Split indexed documents into page-level segments.

Stage 3 of pipeline. Reads each corpus_document, splits on ## Page N headers,
stores each page as a corpus_segment.

Idempotent: uses INSERT OR IGNORE on (doc_id, segment_id).
Prerequisite: index_corpus.py must have run.
"""

import re
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "db" / "emerald_tablet.db"


def split_into_pages(content):
    """Split markdown content on ## Page N headers. Returns list of (page_num, text)."""
    # Pattern: ## Page 42
    pattern = re.compile(r'^## Page (\d+)\s*$', re.MULTILINE)
    matches = list(pattern.finditer(content))

    if not matches:
        # No page headers — treat entire document as one segment
        return [(1, content.strip())] if content.strip() else []

    pages = []
    for i, match in enumerate(matches):
        page_num = int(match.group(1))
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        text = content[start:end].strip()
        if text:
            pages.append((page_num, text))

    return pages


def main():
    if not DB_PATH.exists():
        print("ERROR: Database not found. Run init_db.py + migrate_v2.py + index_corpus.py first.")
        return

    conn = sqlite3.connect(DB_PATH)

    # Get all indexed documents
    docs = conn.execute("""
        SELECT id, doc_id, file_path FROM corpus_documents
        ORDER BY doc_id
    """).fetchall()

    if not docs:
        print("No documents indexed. Run index_corpus.py first.")
        conn.close()
        return

    total_segments = 0
    docs_processed = 0

    for doc_row_id, doc_id, file_path in docs:
        full_path = BASE_DIR / file_path
        if not full_path.exists():
            continue

        try:
            content = full_path.read_text(encoding='utf-8', errors='replace')
        except Exception:
            continue

        pages = split_into_pages(content)
        if not pages:
            continue

        for page_num, text in pages:
            segment_id = f"{doc_id}:page_{page_num}"
            char_count = len(text)

            conn.execute("""
                INSERT OR IGNORE INTO corpus_segments
                    (doc_id, segment_id, page_number, text_content, char_count,
                     source_method, confidence)
                VALUES (?, ?, ?, ?, ?, 'DETERMINISTIC', 'HIGH')
            """, (doc_row_id, segment_id, page_num, text, char_count))
            total_segments += 1

        docs_processed += 1

    conn.commit()

    # Report
    total_in_db = conn.execute("SELECT COUNT(*) FROM corpus_segments").fetchone()[0]
    print(f"Processed: {docs_processed} documents")
    print(f"Segments created: {total_segments}")
    print(f"Total corpus_segments: {total_in_db}")

    # Stats
    avg = conn.execute("SELECT AVG(char_count) FROM corpus_segments").fetchone()[0]
    max_c = conn.execute("SELECT MAX(char_count) FROM corpus_segments").fetchone()[0]
    print(f"Avg chars/segment: {avg:.0f}" if avg else "")
    print(f"Max chars/segment: {max_c}" if max_c else "")

    conn.close()


if __name__ == "__main__":
    main()
