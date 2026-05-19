import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "db" / "emerald_tablet.db"

db = sqlite3.connect(DB_PATH)
cur = db.cursor()

# Get STUB and PARTIAL entries by length
cur.execute("""
    SELECT slug, label, category_type,
           CASE
               WHEN LENGTH(COALESCE(definition_long, '')) < 500 THEN 'STUB'
               WHEN LENGTH(COALESCE(definition_long, '')) < 1500 THEN 'PARTIAL'
           END as status,
           LENGTH(COALESCE(definition_long, '')) as length
    FROM concepts
    WHERE LENGTH(COALESCE(definition_long, '')) BETWEEN 100 AND 1499
    ORDER BY category_type DESC, length DESC
""")

print("STUB + PARTIAL entries (100-1499 chars) — Priority for next pass:")
print("=" * 100)

stub_count = 0
partial_count = 0

for slug, label, cat_type, status, length in cur.fetchall():
    if status == 'STUB':
        stub_count += 1
        marker = "[STUB]"
    else:
        partial_count += 1
        marker = "[PARTIAL]"

    print(f"{marker:10} {slug:30} {label:35} ({length:5} chars) [{cat_type}]")

print(f"\nTotal STUB entries: {stub_count}")
print(f"Total PARTIAL entries: {partial_count}")
print(f"Total to expand: {stub_count + partial_count}")

db.close()
