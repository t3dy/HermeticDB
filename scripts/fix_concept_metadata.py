"""
fix_concept_metadata.py — Fix NULL category and category_type on 14 concepts.

Based on GAP_REPORT.md recommendations, assigns scholarly category_type
and category to concepts that were missing metadata.

Idempotent: safe to re-run.
"""

import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "db" / "emerald_tablet.db"

# Mappings from GAP_REPORT.md lines 209-224
FIXES = [
    ("alchemy", "ACTOR_TERM", "ALCHEMICAL"),
    ("anthropos", "ACTOR_TERM", "THEOLOGICAL"),
    ("deification", "ACTOR_TERM", "THEOLOGICAL"),
    ("egypt", "ACTOR_TERM", "COSMOLOGICAL"),
    ("emanations", "ACTOR_TERM", "COSMOLOGICAL"),
    ("god_making", "ACTOR_TERM", "THEOLOGICAL"),
    ("ochema", "ACTOR_TERM", "PHILOSOPHICAL"),
    ("palingenesia", "ACTOR_TERM", "THEOLOGICAL"),
    ("prophecy", "ACTOR_TERM", "THEOLOGICAL"),
    ("regeneration", "ACTOR_TERM", "THEOLOGICAL"),
    ("talismans", "ACTOR_TERM", "SCIENTIFIC"),
    ("virtus_loci", "ACTOR_TERM", "PHILOSOPHICAL"),
    ("phantasmata", "ACTOR_TERM", "PHILOSOPHICAL"),
]

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

for slug, category_type, category in FIXES:
    cur.execute(
        """
        UPDATE concepts
        SET category_type = ?, category = ?
        WHERE slug = ? AND (category_type IS NULL OR category IS NULL)
        """,
        (category_type, category, slug),
    )
    rows_affected = cur.rowcount
    if rows_affected > 0:
        print(f"✓ {slug:20} → {category_type:12} / {category}")
    else:
        print(f"  {slug:20} (already fixed or not found)")

conn.commit()
conn.close()

print(f"\nDone. Updated {sum(1 for _ in FIXES)} concept metadata entries.")
