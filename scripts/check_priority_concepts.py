import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "db" / "emerald_tablet.db"

db = sqlite3.connect(DB_PATH)
cur = db.cursor()

# Top 10 priority ACTOR_TERMs from GAP_REPORT
priority = ["gnosis", "nous", "prisca_theologia", "magia_naturalis", "theurgy",
            "spiritus", "logos", "sympatheia", "pneuma", "lumen_gloriae"]

print("TOP 10 PRIORITY ACTOR_TERMs — Content Status")
print("=" * 80)

for slug in priority:
    cur.execute("""
        SELECT slug, label,
               COALESCE(LENGTH(definition_long), 0) as def_len,
               CASE
                   WHEN definition_long IS NULL OR LENGTH(COALESCE(definition_long, '')) = 0 THEN 'MISSING'
                   WHEN LENGTH(COALESCE(definition_long, '')) < 500 THEN 'STUB'
                   WHEN LENGTH(COALESCE(definition_long, '')) < 1500 THEN 'PARTIAL'
                   ELSE 'OK'
               END as status
        FROM concepts
        WHERE slug = ?
    """, (slug,))
    row = cur.fetchone()
    if row:
        slug, label, length, status = row
        print(f"{status:10} {slug:25} {label:35} ({length:5} chars)")
    else:
        print(f"NOT FOUND {slug}")

db.close()
