import sqlite3
import re
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "db" / "emerald_tablet.db"

db = sqlite3.connect(DB_PATH)
cur = db.cursor()

entries = ["lumen_gloriae", "gnosis", "prisca_theologia"]

print("WRITTEN CONTENT VERIFICATION")
print("=" * 80)

for slug in entries:
    cur.execute("""
        SELECT label, definition_long
        FROM concepts WHERE slug = ?
    """, (slug,))
    row = cur.fetchone()
    if row:
        label, content = row
        # Count words (rough estimate: strip HTML tags and count words)
        text = re.sub(r'<[^>]+>', '', content)
        words = len(text.split())

        # Check for style violations
        violations = []
        if '[' in content or ']' in content:
            violations.append("Brackets found")
        if '#' in content:
            violations.append("Hashtags found")
        if '*' in re.sub(r'<i>.*?</i>', '', content):  # ignore italics markers
            violations.append("Asterisks found")
        if '- ' in content and '<li' not in content:
            violations.append("Bullet points found")

        status = "CLEAN" if not violations else f"ISSUES: {', '.join(violations)}"

        print(f"\n{label.upper()}")
        print(f"  Characters: {len(content)}")
        print(f"  Words: {words} (target: 1500-2500)")
        print(f"  Style check: {status}")

db.close()
