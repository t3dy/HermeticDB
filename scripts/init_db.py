"""
init_db.py — Create the full schema for the EmeraldTablet knowledge portal.

14 tables covering: texts, persons, translations, concepts, commentaries,
bibliography, manuscripts, timeline events, and their relationships.

Idempotent: safe to re-run.
"""

import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_DIR = BASE_DIR / "db"
DB_PATH = DB_DIR / "emerald_tablet.db"

SCHEMA = """
-- ============================================================
-- EMERALD TABLET KNOWLEDGE PORTAL — Full Schema v1
-- 14 tables: 8 core entities, 4 join/relationship tables,
--            1 commentary table, 1 infrastructure table
-- ============================================================

-- Primary sources, treatises, compilations, encyclopedias
CREATE TABLE IF NOT EXISTS texts (
    id                  INTEGER PRIMARY KEY,
    text_id             TEXT UNIQUE NOT NULL,
    title               TEXT NOT NULL,
    title_original      TEXT,
    language            TEXT CHECK(language IN ('ARABIC','LATIN','GREEK','SYRIAC','GERMAN','ENGLISH','PERSIAN','HEBREW') OR language IS NULL),
    text_type           TEXT CHECK(text_type IN ('PRIMARY_SOURCE','COMMENTARY','COMPILATION','TREATISE','ENCYCLOPEDIA','TRANSLATION','PSEUDO_EPIGRAPHA') OR text_type IS NULL),
    date_composed_start INTEGER,
    date_composed_end   INTEGER,
    description         TEXT,
    analysis_html       TEXT,
    transmission_notes  TEXT,
    source_method       TEXT DEFAULT 'SEED_DATA',
    review_status       TEXT DEFAULT 'DRAFT' CHECK(review_status IN ('DRAFT','REVIEWED','VERIFIED')),
    confidence          TEXT DEFAULT 'MEDIUM' CHECK(confidence IN ('HIGH','MEDIUM','LOW'))
);

-- Containment, derivation, and translation relationships between texts
CREATE TABLE IF NOT EXISTS text_relationships (
    id                  INTEGER PRIMARY KEY,
    parent_text_id      INTEGER NOT NULL REFERENCES texts(id),
    child_text_id       INTEGER NOT NULL REFERENCES texts(id),
    relationship_type   TEXT NOT NULL CHECK(relationship_type IN ('CONTAINS','DERIVES_FROM','COMMENTARY_ON','TRANSLATION_OF','RECENSION_OF','RELATED_TO')),
    notes               TEXT,
    UNIQUE(parent_text_id, child_text_id, relationship_type)
);

-- Historical, mythical, and modern scholarly figures
CREATE TABLE IF NOT EXISTS persons (
    id                  INTEGER PRIMARY KEY,
    person_id           TEXT UNIQUE NOT NULL,
    name                TEXT NOT NULL,
    name_alt            TEXT,
    birth_year          INTEGER,
    death_year          INTEGER,
    era                 TEXT,
    role_primary        TEXT CHECK(role_primary IN ('AUTHOR','TRANSLATOR','COMMENTATOR','SCHOLAR','MYTHICAL_FIGURE','COMPILER','EDITOR','PHILOSOPHER') OR role_primary IS NULL),
    description         TEXT,
    bio_html            TEXT,
    source_method       TEXT DEFAULT 'SEED_DATA',
    review_status       TEXT DEFAULT 'DRAFT' CHECK(review_status IN ('DRAFT','REVIEWED','VERIFIED')),
    confidence          TEXT DEFAULT 'MEDIUM' CHECK(confidence IN ('HIGH','MEDIUM','LOW'))
);

-- Join: who did what with which text
CREATE TABLE IF NOT EXISTS person_text_roles (
    id                  INTEGER PRIMARY KEY,
    person_id           INTEGER NOT NULL REFERENCES persons(id),
    text_id             INTEGER NOT NULL REFERENCES texts(id),
    role                TEXT NOT NULL CHECK(role IN ('AUTHOR','ATTRIBUTED_AUTHOR','TRANSLATOR','COMMENTATOR','EDITOR','DISCOVERER','COMPILER')),
    notes               TEXT,
    confidence          TEXT DEFAULT 'MEDIUM' CHECK(confidence IN ('HIGH','MEDIUM','LOW')),
    UNIQUE(person_id, text_id, role)
);

-- Named translations of texts (especially the Emerald Tablet)
CREATE TABLE IF NOT EXISTS translations (
    id                  INTEGER PRIMARY KEY,
    translation_id      TEXT UNIQUE NOT NULL,
    source_text_id      INTEGER REFERENCES texts(id),
    translator_id       INTEGER REFERENCES persons(id),
    title               TEXT NOT NULL,
    language            TEXT NOT NULL CHECK(language IN ('ARABIC','LATIN','ENGLISH','GERMAN','FRENCH','PHOENICIAN','CHALDEAN','CHINESE','GREEK','SYRIAC','PERSIAN')),
    date_approximate    TEXT,
    date_year           INTEGER,
    source_citation     TEXT,
    tradition           TEXT CHECK(tradition IN ('SIRR_AL_KHALIQA','SECRETUM_SECRETORUM','JABIRIAN','IBN_UMAYL','VULGATE','HUGO_OF_SANTALLA','INDEPENDENT','MODERN') OR tradition IS NULL),
    notes               TEXT,
    source_method       TEXT DEFAULT 'SEED_DATA',
    review_status       TEXT DEFAULT 'DRAFT' CHECK(review_status IN ('DRAFT','REVIEWED','VERIFIED')),
    confidence          TEXT DEFAULT 'MEDIUM' CHECK(confidence IN ('HIGH','MEDIUM','LOW'))
);

-- Verse-level text for parallel translation display
CREATE TABLE IF NOT EXISTS translation_verses (
    id                  INTEGER PRIMARY KEY,
    translation_id      INTEGER NOT NULL REFERENCES translations(id),
    verse_number        TEXT NOT NULL,
    verse_sub           TEXT,
    verse_text          TEXT NOT NULL,
    notes               TEXT,
    source_method       TEXT DEFAULT 'CORPUS_EXTRACTION',
    confidence          TEXT DEFAULT 'HIGH' CHECK(confidence IN ('HIGH','MEDIUM','LOW')),
    UNIQUE(translation_id, verse_number, verse_sub)
);

-- Alchemical, philosophical, cosmological, and linguistic concepts
CREATE TABLE IF NOT EXISTS concepts (
    id                  INTEGER PRIMARY KEY,
    slug                TEXT UNIQUE NOT NULL,
    label               TEXT NOT NULL,
    label_alt           TEXT,
    category            TEXT CHECK(category IN ('COSMOLOGICAL','ALCHEMICAL','PHILOSOPHICAL','LINGUISTIC','THEOLOGICAL','SCIENTIFIC') OR category IS NULL),
    definition_short    TEXT,
    definition_long     TEXT,
    significance        TEXT,
    source_method       TEXT DEFAULT 'SEED_DATA',
    review_status       TEXT DEFAULT 'DRAFT' CHECK(review_status IN ('DRAFT','REVIEWED','VERIFIED')),
    confidence          TEXT DEFAULT 'MEDIUM' CHECK(confidence IN ('HIGH','MEDIUM','LOW'))
);

-- Concepts referenced in texts
CREATE TABLE IF NOT EXISTS concept_text_refs (
    id                  INTEGER PRIMARY KEY,
    concept_id          INTEGER NOT NULL REFERENCES concepts(id),
    text_id             INTEGER NOT NULL REFERENCES texts(id),
    notes               TEXT,
    UNIQUE(concept_id, text_id)
);

-- Cross-references between concepts
CREATE TABLE IF NOT EXISTS concept_links (
    id                  INTEGER PRIMARY KEY,
    from_concept_id     INTEGER NOT NULL REFERENCES concepts(id),
    to_concept_id       INTEGER NOT NULL REFERENCES concepts(id),
    relationship        TEXT NOT NULL CHECK(relationship IN ('RELATED','SUBSET_OF','OPPOSED_TO','DERIVED_FROM','EXPLAINS')),
    UNIQUE(from_concept_id, to_concept_id)
);

-- Named commentaries on texts
CREATE TABLE IF NOT EXISTS commentaries (
    id                  INTEGER PRIMARY KEY,
    commentary_id       TEXT UNIQUE NOT NULL,
    title               TEXT NOT NULL,
    author_id           INTEGER REFERENCES persons(id),
    target_text_id      INTEGER REFERENCES texts(id),
    date_approximate    TEXT,
    date_year           INTEGER,
    description         TEXT,
    analysis_html       TEXT,
    manuscript_id       INTEGER REFERENCES manuscripts(id),
    source_method       TEXT DEFAULT 'SEED_DATA',
    review_status       TEXT DEFAULT 'DRAFT' CHECK(review_status IN ('DRAFT','REVIEWED','VERIFIED')),
    confidence          TEXT DEFAULT 'MEDIUM' CHECK(confidence IN ('HIGH','MEDIUM','LOW'))
);

-- Scholarly works and references
CREATE TABLE IF NOT EXISTS bibliography (
    id                  INTEGER PRIMARY KEY,
    source_id           TEXT UNIQUE NOT NULL,
    author              TEXT NOT NULL,
    title               TEXT NOT NULL,
    year                INTEGER,
    journal             TEXT,
    publisher           TEXT,
    pub_type            TEXT CHECK(pub_type IN ('MONOGRAPH','ARTICLE','EDITION','REVIEW','PRIMARY_SOURCE','COLLECTION','DISSERTATION','CHAPTER') OR pub_type IS NULL),
    relevance           TEXT CHECK(relevance IN ('PRIMARY','DIRECT','CONTEXTUAL') OR relevance IS NULL),
    in_collection       INTEGER DEFAULT 0,
    notes               TEXT
);

-- Physical manuscript witnesses
CREATE TABLE IF NOT EXISTS manuscripts (
    id                  INTEGER PRIMARY KEY,
    manuscript_id       TEXT UNIQUE NOT NULL,
    shelfmark           TEXT NOT NULL,
    repository          TEXT,
    city                TEXT,
    date_approximate    TEXT,
    date_year           INTEGER,
    language            TEXT,
    contents_summary    TEXT,
    significance        TEXT,
    image_folder        TEXT,
    source_method       TEXT DEFAULT 'SEED_DATA',
    review_status       TEXT DEFAULT 'DRAFT' CHECK(review_status IN ('DRAFT','REVIEWED','VERIFIED')),
    confidence          TEXT DEFAULT 'MEDIUM' CHECK(confidence IN ('HIGH','MEDIUM','LOW'))
);

-- Dated historical events
CREATE TABLE IF NOT EXISTS timeline_events (
    id                  INTEGER PRIMARY KEY,
    year                INTEGER NOT NULL,
    year_end            INTEGER,
    event_type          TEXT CHECK(event_type IN ('COMPOSITION','TRANSLATION','COMMENTARY','PUBLICATION','SCHOLARSHIP','MANUSCRIPT','DISCOVERY','PRINTING') OR event_type IS NULL),
    title               TEXT NOT NULL,
    description         TEXT,
    description_long    TEXT,
    person_id           INTEGER REFERENCES persons(id),
    text_id             INTEGER REFERENCES texts(id),
    bib_id              INTEGER REFERENCES bibliography(id),
    confidence          TEXT DEFAULT 'MEDIUM' CHECK(confidence IN ('HIGH','MEDIUM','LOW'))
);

-- Schema version tracking
CREATE TABLE IF NOT EXISTS schema_version (
    version             INTEGER PRIMARY KEY,
    applied_at          TEXT DEFAULT (datetime('now')),
    description         TEXT
);
"""


def main():
    DB_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.executescript(SCHEMA)

    # Record schema version
    existing = conn.execute("SELECT MAX(version) FROM schema_version").fetchone()[0]
    if existing is None or existing < 1:
        conn.execute(
            "INSERT OR IGNORE INTO schema_version (version, description) VALUES (1, 'Initial full schema — 14 tables')"
        )

    conn.commit()

    # Report
    tables = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
    ).fetchall()
    print(f"Database: {DB_PATH}")
    print(f"Tables created: {len(tables)}")
    for t in tables:
        count = conn.execute(f"SELECT COUNT(*) FROM [{t[0]}]").fetchone()[0]
        print(f"  {t[0]}: {count} rows")

    conn.close()


if __name__ == "__main__":
    main()
