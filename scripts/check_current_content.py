import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "db" / "emerald_tablet.db"

db = sqlite3.connect(DB_PATH)
cur = db.cursor()

entries = ["lumen_gloriae", "gnosis", "prisca_theologia"]

for slug in entries:
    cur.execute("""
        SELECT label, definition_short, definition_long
        FROM concepts WHERE slug = ?
    """, (slug,))
    row = cur.fetchone()
    if row:
        label, short, long_def = row
        print(f"\n{'='*80}")
        print(f"CONCEPT: {label.upper()}")
        print(f"{'='*80}")
        print(f"\nShort definition ({len(short or '') if short else 0} chars):")
        print(short or "[EMPTY]")
        print(f"\nLong definition ({len(long_def or '') if long_def else 0} chars):")
        print((long_def or "[EMPTY]")[:500])
        if long_def and len(long_def) > 500:
            print("...")

db.close()
