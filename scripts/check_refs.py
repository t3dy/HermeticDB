import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "db" / "emerald_tablet.db"

db = sqlite3.connect(DB_PATH)
cur = db.cursor()

cur.execute("SELECT COUNT(*) FROM concept_text_refs")
count = cur.fetchone()[0]
print(f"Total concept_text_refs: {count}")

cur.execute("SELECT COUNT(*) FROM concepts WHERE id IN (SELECT DISTINCT concept_id FROM concept_text_refs)")
concepts_with_refs = cur.fetchone()[0]
print(f"Concepts with text references: {concepts_with_refs}")

# Check gnosis specifically
cur.execute("SELECT COUNT(*) FROM concept_text_refs WHERE concept_id = (SELECT id FROM concepts WHERE slug = 'gnosis')")
gnosis_refs = cur.fetchone()[0]
print(f"References for gnosis: {gnosis_refs}")

db.close()
