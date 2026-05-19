import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "db" / "emerald_tablet.db"

db = sqlite3.connect(DB_PATH)
cur = db.cursor()

# Check definition_long status
cur.execute("""
SELECT
    CASE
        WHEN definition_long IS NULL OR LENGTH(COALESCE(definition_long, '')) = 0 THEN 'MISSING'
        WHEN LENGTH(COALESCE(definition_long, '')) < 500 THEN 'STUB'
        WHEN LENGTH(COALESCE(definition_long, '')) < 1500 THEN 'PARTIAL'
        ELSE 'OK'
    END as status,
    COUNT(*) as count
FROM concepts
GROUP BY status
ORDER BY CASE status WHEN 'MISSING' THEN 1 WHEN 'STUB' THEN 2 WHEN 'PARTIAL' THEN 3 ELSE 4 END
""")

print("Encyclopedia Page Status (definition_long):")
print("=" * 50)
for status, count in cur.fetchall():
    print(f"{status:15} {count:3} concepts")

# List the MISSING ones (priority 0)
print("\nMISSING (0 chars) — Priority:")
cur.execute("""
SELECT slug, label, category_type
FROM concepts
WHERE definition_long IS NULL OR LENGTH(COALESCE(definition_long, '')) = 0
ORDER BY
    CASE category_type WHEN 'ACTOR_TERM' THEN 1 ELSE 2 END,
    label
LIMIT 30
""")

for slug, label, cat_type in cur.fetchall():
    print(f"  {slug:30} {label:35} [{cat_type or '?'}]")

db.close()
