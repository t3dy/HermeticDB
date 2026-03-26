"""
validate.py — Structural and site validation.

Stage 5 (structural) and Stage 10 (site) of pipeline.

Usage:
    python scripts/validate.py              # Run all checks
    python scripts/validate.py --structural # FK integrity, enum checks, orphans only
    python scripts/validate.py --site       # Link checking on generated HTML only

Idempotent: read-only, never modifies the database.
"""

import re
import sqlite3
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "db" / "emerald_tablet.db"
SITE_DIR = BASE_DIR / "site"


def check_fk_integrity(conn):
    """Check all foreign key references resolve."""
    errors = []

    # Enable FK checking
    conn.execute("PRAGMA foreign_keys = ON")
    violations = conn.execute("PRAGMA foreign_key_check").fetchall()
    for table, rowid, parent, fkid in violations:
        errors.append(f"FK violation: {table} row {rowid} → {parent} (fk #{fkid})")

    return errors


def check_enum_values(conn):
    """Check all enum columns contain only valid values."""
    errors = []

    checks = [
        ("texts", "language", ['ARABIC','LATIN','GREEK','SYRIAC','GERMAN','ENGLISH','PERSIAN','HEBREW', None]),
        ("texts", "text_type", ['PRIMARY_SOURCE','COMMENTARY','COMPILATION','TREATISE','ENCYCLOPEDIA','TRANSLATION','PSEUDO_EPIGRAPHA', None]),
        ("texts", "review_status", ['DRAFT','REVIEWED','VERIFIED']),
        ("texts", "confidence", ['HIGH','MEDIUM','LOW']),
        ("persons", "role_primary", ['AUTHOR','TRANSLATOR','COMMENTATOR','SCHOLAR','MYTHICAL_FIGURE','COMPILER','EDITOR','PHILOSOPHER', None]),
        ("translations", "tradition", ['SIRR_AL_KHALIQA','SECRETUM_SECRETORUM','JABIRIAN','IBN_UMAYL','VULGATE','HUGO_OF_SANTALLA','INDEPENDENT','MODERN', None]),
        ("concepts", "category", ['COSMOLOGICAL','ALCHEMICAL','PHILOSOPHICAL','LINGUISTIC','THEOLOGICAL','SCIENTIFIC', None]),
        ("bibliography", "pub_type", ['MONOGRAPH','ARTICLE','EDITION','REVIEW','PRIMARY_SOURCE','COLLECTION','DISSERTATION','CHAPTER', None]),
        ("bibliography", "relevance", ['PRIMARY','DIRECT','CONTEXTUAL', None]),
        ("timeline_events", "event_type", ['COMPOSITION','TRANSLATION','COMMENTARY','PUBLICATION','SCHOLARSHIP','MANUSCRIPT','DISCOVERY','PRINTING', None]),
    ]

    for table, column, valid_values in checks:
        try:
            rows = conn.execute(f"SELECT DISTINCT [{column}] FROM [{table}]").fetchall()
            for (val,) in rows:
                if val not in valid_values:
                    errors.append(f"Invalid enum: {table}.{column} = '{val}' (not in allowed values)")
        except Exception as e:
            errors.append(f"Error checking {table}.{column}: {e}")

    return errors


def check_orphans(conn):
    """Check for orphaned records (FKs pointing to non-existent rows)."""
    errors = []

    orphan_checks = [
        ("text_relationships", "parent_text_id", "texts", "id"),
        ("text_relationships", "child_text_id", "texts", "id"),
        ("person_text_roles", "person_id", "persons", "id"),
        ("person_text_roles", "text_id", "texts", "id"),
        ("translations", "source_text_id", "texts", "id"),
        ("translations", "translator_id", "persons", "id"),
        ("translation_verses", "translation_id", "translations", "id"),
        ("concept_text_refs", "concept_id", "concepts", "id"),
        ("concept_text_refs", "text_id", "texts", "id"),
        ("concept_links", "from_concept_id", "concepts", "id"),
        ("concept_links", "to_concept_id", "concepts", "id"),
        ("commentaries", "author_id", "persons", "id"),
        ("commentaries", "target_text_id", "texts", "id"),
        ("timeline_events", "person_id", "persons", "id"),
        ("timeline_events", "text_id", "texts", "id"),
        ("timeline_events", "bib_id", "bibliography", "id"),
    ]

    for child_table, fk_col, parent_table, parent_col in orphan_checks:
        try:
            orphans = conn.execute(f"""
                SELECT COUNT(*) FROM [{child_table}]
                WHERE [{fk_col}] IS NOT NULL
                AND [{fk_col}] NOT IN (SELECT [{parent_col}] FROM [{parent_table}])
            """).fetchone()[0]
            if orphans > 0:
                errors.append(f"Orphan: {child_table}.{fk_col} has {orphans} rows pointing to missing {parent_table}")
        except Exception:
            pass  # Table might not exist yet

    return errors


def check_required_fields(conn):
    """Check that required fields are populated."""
    errors = []

    required = [
        ("texts", "text_id"),
        ("texts", "title"),
        ("persons", "person_id"),
        ("persons", "name"),
        ("translations", "translation_id"),
        ("translations", "title"),
        ("translations", "language"),
        ("concepts", "slug"),
        ("concepts", "label"),
        ("bibliography", "source_id"),
        ("bibliography", "author"),
        ("bibliography", "title"),
        ("manuscripts", "manuscript_id"),
        ("manuscripts", "shelfmark"),
    ]

    for table, column in required:
        try:
            nulls = conn.execute(f"""
                SELECT COUNT(*) FROM [{table}]
                WHERE [{column}] IS NULL OR [{column}] = ''
            """).fetchone()[0]
            if nulls > 0:
                errors.append(f"Missing required: {table}.{column} has {nulls} null/empty rows")
        except Exception:
            pass

    return errors


def check_provenance(conn):
    """Check that provenance fields are populated on all entity tables."""
    errors = []

    provenance_tables = [
        'texts', 'persons', 'translations', 'translation_verses',
        'concepts', 'commentaries', 'manuscripts',
    ]

    for table in provenance_tables:
        try:
            for field in ['source_method', 'confidence']:
                nulls = conn.execute(f"""
                    SELECT COUNT(*) FROM [{table}]
                    WHERE [{field}] IS NULL OR [{field}] = ''
                """).fetchone()[0]
                if nulls > 0:
                    errors.append(f"Missing provenance: {table}.{field} has {nulls} null rows")
        except Exception:
            pass

    return errors


def report_counts(conn):
    """Report row counts for all tables."""
    tables = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
    ).fetchall()
    print("\nRow counts:")
    for (name,) in tables:
        count = conn.execute(f"SELECT COUNT(*) FROM [{name}]").fetchone()[0]
        if count > 0:
            print(f"  {name}: {count}")


def check_site_links():
    """Check all internal links in generated HTML resolve to existing files."""
    errors = []

    if not SITE_DIR.exists():
        return ["Site directory does not exist. Run build_site.py first."]

    html_files = list(SITE_DIR.rglob("*.html"))
    if not html_files:
        return ["No HTML files found in site/"]

    link_pattern = re.compile(r'href="([^"#]+)"')
    src_pattern = re.compile(r'src="([^"#]+)"')

    for html_file in html_files:
        try:
            content = html_file.read_text(encoding='utf-8', errors='replace')
        except Exception:
            continue

        for pattern in [link_pattern, src_pattern]:
            for match in pattern.finditer(content):
                ref = match.group(1)
                # Skip external links
                if ref.startswith(('http://', 'https://', 'mailto:', '//')):
                    continue
                # Resolve relative path
                target = (html_file.parent / ref).resolve()
                if not target.exists():
                    rel_html = html_file.relative_to(SITE_DIR)
                    errors.append(f"Broken link: {rel_html} → {ref}")

    return errors


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else '--all'

    all_errors = []

    if mode in ('--structural', '--all'):
        if not DB_PATH.exists():
            print("ERROR: Database not found.")
            return

        conn = sqlite3.connect(DB_PATH)

        print("=== STRUCTURAL VALIDATION ===")

        fk_errors = check_fk_integrity(conn)
        enum_errors = check_enum_values(conn)
        orphan_errors = check_orphans(conn)
        required_errors = check_required_fields(conn)
        provenance_errors = check_provenance(conn)

        all_errors.extend(fk_errors)
        all_errors.extend(enum_errors)
        all_errors.extend(orphan_errors)
        all_errors.extend(required_errors)
        all_errors.extend(provenance_errors)

        report_counts(conn)
        conn.close()

    if mode in ('--site', '--all'):
        print("\n=== SITE VALIDATION ===")
        link_errors = check_site_links()
        all_errors.extend(link_errors)

    # Summary
    print(f"\n{'='*40}")
    if all_errors:
        print(f"VALIDATION FAILED: {len(all_errors)} errors")
        for e in all_errors:
            print(f"  ✗ {e}")
    else:
        print("VALIDATION PASSED: 0 errors")

    return len(all_errors)


if __name__ == "__main__":
    sys.exit(main() or 0)
