"""
seed_from_json.py — Ingest emerald_tablet_seed.json into the database.

Populates all core tables from the curated seed data.
Idempotent: uses INSERT OR IGNORE throughout.
"""

import json
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "db" / "emerald_tablet.db"
SEED_PATH = BASE_DIR / "data" / "emerald_tablet_seed.json"


def seed_texts(conn, seed):
    """Insert texts."""
    for t in seed.get("texts", []):
        conn.execute("""
            INSERT OR IGNORE INTO texts
                (text_id, title, title_original, language, text_type,
                 date_composed_start, date_composed_end, description,
                 transmission_notes, source_method, confidence)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'SEED_DATA', 'HIGH')
        """, (
            t["text_id"], t["title"], t.get("title_original"),
            t.get("language"), t.get("text_type"),
            t.get("date_composed_start"), t.get("date_composed_end"),
            t.get("description"), t.get("transmission_notes")
        ))


def seed_persons(conn, seed):
    """Insert persons."""
    for p in seed.get("persons", []):
        conn.execute("""
            INSERT OR IGNORE INTO persons
                (person_id, name, name_alt, birth_year, death_year,
                 era, role_primary, description, source_method, confidence)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'SEED_DATA', 'HIGH')
        """, (
            p["person_id"], p["name"], p.get("name_alt"),
            p.get("birth_year"), p.get("death_year"),
            p.get("era"), p.get("role_primary"), p.get("description")
        ))


def seed_translations(conn, seed):
    """Insert translations, resolving text and person FKs."""
    for t in seed.get("translations", []):
        # Resolve source_text FK
        source_text_id = None
        if t.get("source_text"):
            row = conn.execute(
                "SELECT id FROM texts WHERE text_id = ?", (t["source_text"],)
            ).fetchone()
            if row:
                source_text_id = row[0]

        # Resolve translator FK
        translator_id = None
        if t.get("translator"):
            row = conn.execute(
                "SELECT id FROM persons WHERE person_id = ?", (t["translator"],)
            ).fetchone()
            if row:
                translator_id = row[0]

        conn.execute("""
            INSERT OR IGNORE INTO translations
                (translation_id, source_text_id, translator_id, title,
                 language, date_approximate, date_year, source_citation,
                 tradition, notes, source_method, confidence)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'SEED_DATA', 'HIGH')
        """, (
            t["translation_id"], source_text_id, translator_id,
            t["title"], t["language"], t.get("date_approximate"),
            t.get("date_year"), t.get("source_citation"),
            t.get("tradition"), t.get("notes")
        ))


def seed_concepts(conn, seed):
    """Insert concepts."""
    for c in seed.get("concepts", []):
        conn.execute("""
            INSERT OR IGNORE INTO concepts
                (slug, label, label_alt, category, definition_short,
                 definition_long, significance, source_method, confidence)
            VALUES (?, ?, ?, ?, ?, ?, ?, 'SEED_DATA', 'HIGH')
        """, (
            c["slug"], c["label"], c.get("label_alt"),
            c.get("category"), c.get("definition_short"),
            c.get("definition_long"), c.get("significance")
        ))


def seed_bibliography(conn, seed):
    """Insert bibliography entries."""
    for b in seed.get("bibliography", []):
        conn.execute("""
            INSERT OR IGNORE INTO bibliography
                (source_id, author, title, year, journal, publisher,
                 pub_type, relevance, in_collection, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            b["source_id"], b["author"], b["title"], b.get("year"),
            b.get("journal"), b.get("publisher"), b.get("pub_type"),
            b.get("relevance"), b.get("in_collection", 0), b.get("notes")
        ))


def seed_manuscripts(conn, seed):
    """Insert manuscripts."""
    for m in seed.get("manuscripts", []):
        conn.execute("""
            INSERT OR IGNORE INTO manuscripts
                (manuscript_id, shelfmark, repository, city,
                 date_approximate, date_year, language,
                 contents_summary, significance, image_folder,
                 source_method, confidence)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'SEED_DATA', 'HIGH')
        """, (
            m["manuscript_id"], m["shelfmark"], m.get("repository"),
            m.get("city"), m.get("date_approximate"), m.get("date_year"),
            m.get("language"), m.get("contents_summary"),
            m.get("significance"), m.get("image_folder")
        ))


def seed_timeline_events(conn, seed):
    """Insert timeline events, resolving person/text/bib FKs."""
    for e in seed.get("timeline_events", []):
        person_id = None
        if e.get("person"):
            row = conn.execute(
                "SELECT id FROM persons WHERE person_id = ?", (e["person"],)
            ).fetchone()
            if row:
                person_id = row[0]

        text_id = None
        if e.get("text"):
            row = conn.execute(
                "SELECT id FROM texts WHERE text_id = ?", (e["text"],)
            ).fetchone()
            if row:
                text_id = row[0]

        bib_id = None
        if e.get("bib"):
            row = conn.execute(
                "SELECT id FROM bibliography WHERE source_id = ?", (e["bib"],)
            ).fetchone()
            if row:
                bib_id = row[0]

        conn.execute("""
            INSERT OR IGNORE INTO timeline_events
                (year, year_end, event_type, title, description,
                 person_id, text_id, bib_id, confidence)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'HIGH')
        """, (
            e["year"], e.get("year_end"), e.get("event_type"),
            e["title"], e.get("description"),
            person_id, text_id, bib_id
        ))


def seed_text_relationships(conn, seed):
    """Insert text relationships, resolving text FKs."""
    for r in seed.get("text_relationships", []):
        parent = conn.execute(
            "SELECT id FROM texts WHERE text_id = ?", (r["parent"],)
        ).fetchone()
        child = conn.execute(
            "SELECT id FROM texts WHERE text_id = ?", (r["child"],)
        ).fetchone()
        if parent and child:
            conn.execute("""
                INSERT OR IGNORE INTO text_relationships
                    (parent_text_id, child_text_id, relationship_type, notes)
                VALUES (?, ?, ?, ?)
            """, (parent[0], child[0], r["type"], r.get("notes")))


def seed_concept_text_refs(conn, seed):
    """Insert concept-text references."""
    for ref in seed.get("concept_text_refs", []):
        concept = conn.execute(
            "SELECT id FROM concepts WHERE slug = ?", (ref["concept"],)
        ).fetchone()
        text = conn.execute(
            "SELECT id FROM texts WHERE text_id = ?", (ref["text"],)
        ).fetchone()
        if concept and text:
            conn.execute("""
                INSERT OR IGNORE INTO concept_text_refs
                    (concept_id, text_id)
                VALUES (?, ?)
            """, (concept[0], text[0]))


def seed_concept_links(conn, seed):
    """Insert concept cross-references."""
    for link in seed.get("concept_links", []):
        from_c = conn.execute(
            "SELECT id FROM concepts WHERE slug = ?", (link["from"],)
        ).fetchone()
        to_c = conn.execute(
            "SELECT id FROM concepts WHERE slug = ?", (link["to"],)
        ).fetchone()
        if from_c and to_c:
            conn.execute("""
                INSERT OR IGNORE INTO concept_links
                    (from_concept_id, to_concept_id, relationship)
                VALUES (?, ?, ?)
            """, (from_c[0], to_c[0], link["relationship"]))


def seed_person_text_roles(conn, seed):
    """Insert person-text role relationships."""
    for r in seed.get("person_text_roles", []):
        person = conn.execute(
            "SELECT id FROM persons WHERE person_id = ?", (r["person"],)
        ).fetchone()
        text = conn.execute(
            "SELECT id FROM texts WHERE text_id = ?", (r["text"],)
        ).fetchone()
        if person and text:
            conn.execute("""
                INSERT OR IGNORE INTO person_text_roles
                    (person_id, text_id, role, notes, confidence)
                VALUES (?, ?, ?, ?, 'HIGH')
            """, (person[0], text[0], r["role"], r.get("notes")))


def load_and_seed(conn, seed_path):
    """Load a single JSON file and seed all tables from it."""
    with open(seed_path, "r", encoding="utf-8") as f:
        seed = json.load(f)

    # Seed in dependency order (entities first, then relationships)
    seed_texts(conn, seed)
    seed_persons(conn, seed)
    seed_translations(conn, seed)
    seed_concepts(conn, seed)
    seed_bibliography(conn, seed)
    seed_manuscripts(conn, seed)
    seed_timeline_events(conn, seed)
    seed_text_relationships(conn, seed)
    seed_concept_text_refs(conn, seed)
    seed_concept_links(conn, seed)
    seed_person_text_roles(conn, seed)

    return seed_path.name


def main():
    if not DB_PATH.exists():
        print(f"ERROR: Database not found at {DB_PATH}. Run init_db.py first.")
        return

    conn = sqlite3.connect(DB_PATH)
    DATA_DIR = BASE_DIR / "data"

    # Load all JSON files in data/ directory
    json_files = sorted(DATA_DIR.glob("*.json"))
    if not json_files:
        print(f"ERROR: No JSON files found in {DATA_DIR}.")
        conn.close()
        return

    for json_path in json_files:
        name = load_and_seed(conn, json_path)
        print(f"Loaded: {name}")

    conn.commit()

    # Report
    tables = [
        "texts", "persons", "translations", "concepts",
        "bibliography", "manuscripts", "timeline_events",
        "text_relationships", "concept_text_refs", "concept_links",
        "person_text_roles"
    ]
    print("\nSeed complete:")
    for t in tables:
        count = conn.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
        print(f"  {t}: {count} rows")

    conn.close()


if __name__ == "__main__":
    main()
