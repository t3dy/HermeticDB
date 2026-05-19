import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "db" / "emerald_tablet.db"

db = sqlite3.connect(DB_PATH)
cur = db.cursor()

cur.execute("SELECT COUNT(*) FROM concepts WHERE definition_short IS NULL OR definition_short = ''")
count = cur.fetchone()[0]
print(f'Concepts with missing/empty definition_short: {count}')

cur.execute("SELECT slug, label, category_type FROM concepts WHERE definition_short IS NULL OR definition_short = '' ORDER BY slug")
missing = cur.fetchall()
print("\nMissing definition_short concepts:")
for slug, label, cat_type in missing:
    print(f"  {slug:30} {label:30} [{cat_type or 'UNCATEGORIZED'}]")

db.close()
