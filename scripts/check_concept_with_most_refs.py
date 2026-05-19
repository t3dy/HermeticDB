import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "db" / "emerald_tablet.db"

db = sqlite3.connect(DB_PATH)
cur = db.cursor()

cur.execute("""
SELECT c.slug, c.label, COUNT(*) as ref_count
FROM concept_text_refs ctr
JOIN concepts c ON ctr.concept_id = c.id
GROUP BY c.id
ORDER BY ref_count DESC
LIMIT 10
""")

print("Concepts with most text references:")
for slug, label, count in cur.fetchall():
    print(f"  {slug:30} {label:40} ({count} refs)")

db.close()
