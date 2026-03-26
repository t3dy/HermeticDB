"""
migrate_v2.py — Add corpus layer tables (corpus_documents, corpus_segments).

Implements the missing middle layer between raw corpus files and entity extraction.
Idempotent: checks for table existence before creating.
"""

import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "db" / "emerald_tablet.db"

MIGRATION = """
-- ============================================================
-- MIGRATION v2: Corpus Layer Tables
-- Implements: CORPUS → INDEX → SEGMENTS → MARKS
-- ============================================================

-- Registry of every corpus file (markdown, txt, research notes)
CREATE TABLE IF NOT EXISTS corpus_documents (
    id              INTEGER PRIMARY KEY,
    doc_id          TEXT UNIQUE NOT NULL,
    file_path       TEXT NOT NULL,
    title           TEXT,
    doc_family      TEXT CHECK(doc_family IN (
        'HERMETIC_CORPUS','ALCHEMICAL','SCHOLARLY_MONOGRAPH','SCHOLARLY_ARTICLE',
        'BOOK_REVIEW','RESEARCH_NOTES','CHAT_SUMMARY','CONFERENCE_PROCEEDINGS',
        'CRITICAL_EDITION','PRIMARY_SOURCE','REFERENCE_WORK','MAIER_EXTRACT'
    ) OR doc_family IS NULL),
    language        TEXT,
    text_quality    TEXT CHECK(text_quality IN ('HIGH','MEDIUM','LOW','EMPTY') OR text_quality IS NULL),
    source_type     TEXT CHECK(source_type IN (
        'PDF_EXTRACTED','OCR','CHAT_EXPORT','RESEARCH_NOTES','MAIER_EXTRACT'
    ) OR source_type IS NULL),
    page_count      INTEGER,
    indexed_at      TEXT DEFAULT (datetime('now')),
    source_method   TEXT DEFAULT 'DETERMINISTIC',
    confidence      TEXT DEFAULT 'HIGH' CHECK(confidence IN ('HIGH','MEDIUM','LOW'))
);

-- Page/section-level segments of each document
CREATE TABLE IF NOT EXISTS corpus_segments (
    id              INTEGER PRIMARY KEY,
    doc_id          INTEGER NOT NULL REFERENCES corpus_documents(id),
    segment_id      TEXT NOT NULL,
    page_number     INTEGER,
    section_type    TEXT CHECK(section_type IN (
        'FRONT_MATTER','CHAPTER','SECTION','BIBLIOGRAPHY','INDEX',
        'APPENDIX','APPARATUS','NOTES','UNKNOWN'
    ) OR section_type IS NULL),
    section_title   TEXT,
    text_content    TEXT NOT NULL,
    char_count      INTEGER DEFAULT 0,
    language        TEXT,
    relevance_score INTEGER DEFAULT 0,
    has_emerald_tablet INTEGER DEFAULT 0,
    persons_mentioned TEXT,
    concepts_mentioned TEXT,
    source_method   TEXT DEFAULT 'DETERMINISTIC',
    confidence      TEXT DEFAULT 'HIGH' CHECK(confidence IN ('HIGH','MEDIUM','LOW')),
    UNIQUE(doc_id, segment_id)
);

-- Index for fast keyword search on segments
CREATE INDEX IF NOT EXISTS idx_segments_relevance ON corpus_segments(relevance_score DESC);
CREATE INDEX IF NOT EXISTS idx_segments_doc ON corpus_segments(doc_id);
CREATE INDEX IF NOT EXISTS idx_segments_type ON corpus_segments(section_type);
"""


def main():
    if not DB_PATH.exists():
        print(f"ERROR: Database not found at {DB_PATH}. Run init_db.py first.")
        return

    conn = sqlite3.connect(DB_PATH)

    # Check current schema version
    current = conn.execute("SELECT MAX(version) FROM schema_version").fetchone()[0] or 0

    if current >= 2:
        print(f"Migration v2 already applied (current version: {current}). Skipping.")
        # Still run CREATE IF NOT EXISTS for safety
        conn.executescript(MIGRATION)
        conn.close()
        return

    conn.executescript(MIGRATION)

    conn.execute(
        "INSERT INTO schema_version (version, description) VALUES (2, 'Corpus layer — corpus_documents + corpus_segments')"
    )
    conn.commit()

    # Report
    for table in ['corpus_documents', 'corpus_segments']:
        cols = conn.execute(f"PRAGMA table_info({table})").fetchall()
        print(f"  {table}: {len(cols)} columns")

    print("Migration v2 applied successfully.")
    conn.close()


if __name__ == "__main__":
    main()
