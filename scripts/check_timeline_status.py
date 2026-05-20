import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "db" / "emerald_tablet.db"

db = sqlite3.connect(DB_PATH)
cur = db.cursor()

# Check timeline_events status
cur.execute("""
    SELECT
        COUNT(*) as total,
        SUM(CASE WHEN LENGTH(COALESCE(description, '')) = 0 THEN 1 ELSE 0 END) as missing,
        SUM(CASE WHEN LENGTH(COALESCE(description, '')) BETWEEN 1 AND 100 THEN 1 ELSE 0 END) as stub,
        SUM(CASE WHEN LENGTH(COALESCE(description, '')) BETWEEN 101 AND 250 THEN 1 ELSE 0 END) as partial,
        SUM(CASE WHEN LENGTH(COALESCE(description, '')) > 250 THEN 1 ELSE 0 END) as ok
    FROM timeline_events
""")

total, missing, stub, partial, ok = cur.fetchone()

print("TIMELINE EVENTS (Map Entries) STATUS")
print("=" * 80)
print(f"Total events: {total}")
print(f"  OK (>250 chars):        {ok}")
print(f"  PARTIAL (101-250):      {partial}")
print(f"  STUB (1-100):           {stub}")
print(f"  MISSING (0 chars):      {missing}")
print(f"\nTotal needing expansion: {stub + partial} of {total}")

print("\nSTUB TIMELINE EVENTS (1-100 chars) — Expand to 100-250:")
cur.execute("""
    SELECT year, title, LENGTH(COALESCE(description, '')) as length
    FROM timeline_events
    WHERE LENGTH(COALESCE(description, '')) BETWEEN 1 AND 100
    ORDER BY year DESC
    LIMIT 15
""")

for year, title, length in cur.fetchall():
    print(f"  {year:4} {title:50} ({length:3} chars)")

print("\nPARTIAL TIMELINE EVENTS (101-250 chars) — Expand to 250+:")
cur.execute("""
    SELECT year, title, LENGTH(COALESCE(description, '')) as length
    FROM timeline_events
    WHERE LENGTH(COALESCE(description, '')) BETWEEN 101 AND 250
    ORDER BY year DESC
    LIMIT 10
""")

for year, title, length in cur.fetchall():
    print(f"  {year:4} {title:50} ({length:3} chars)")

db.close()
