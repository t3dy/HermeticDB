import sqlite3
from pathlib import Path

DB_PATH = Path(r"c:\Dev\EmeraldTablet\db\emerald_tablet.db")

def audit():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    gaps = []

    # 1. Persons without summaries
    cursor.execute("SELECT name FROM persons WHERE description IS NULL OR description = ''")
    rows = cursor.fetchall()
    if rows: gaps.append(f"MISSING SUMMARIES (PERSONS): {[r['name'] for r in rows]}")

    # 2. Texts without summaries
    cursor.execute("SELECT title FROM texts WHERE analysis_html IS NULL OR analysis_html = ''")
    rows = cursor.fetchall()
    if rows: gaps.append(f"MISSING SUMMARIES (TEXTS): {[r['title'] for r in rows]}")

    # 3. Persons with no connections (not in person_text_refs and not in person_person_refs)
    cursor.execute("""
        SELECT person_id, name FROM persons 
        WHERE person_id NOT IN (SELECT person_id FROM person_text_refs)
        AND person_id NOT IN (SELECT person_a FROM person_person_refs)
        AND person_id NOT IN (SELECT person_b FROM person_person_refs)
    """)
    rows = cursor.fetchall()
    if rows: gaps.append(f"ORPHANED PERSONS (NO LINKS): {[r['name'] for r in rows]}")

    # 4. Texts with no connections (not in person_text_refs, not in text_text_refs, not in concept_text_refs)
    cursor.execute("""
        SELECT text_id, title FROM texts 
        WHERE text_id NOT IN (SELECT text_id FROM person_text_refs)
        AND text_id NOT IN (SELECT text_a FROM text_text_refs)
        AND text_id NOT IN (SELECT text_b FROM text_text_refs)
        AND id NOT IN (SELECT text_id FROM concept_text_refs)
    """)
    rows = cursor.fetchall()
    if rows: gaps.append(f"ORPHANED TEXTS (NO LINKS): {[r['title'] for r in rows]}")

    # 5. Empty Eras (Already checked, but good for audit)
    for era in ['ANTIQUITY', 'MEDIEVAL', 'RENAISSANCE', 'EARLY_MODERN', 'MODERN']:
        cursor.execute("SELECT COUNT(*) FROM persons WHERE era = ?", (era,))
        if cursor.fetchone()[0] == 0:
            gaps.append(f"EMPTY ERA: {era}")

    # 6. Timeline Gaps (Long stretches > 200 years)
    cursor.execute("SELECT year FROM timeline_events ORDER BY year")
    years = [r[0] for r in cursor.fetchall()]
    for i in range(len(years)-1):
        if years[i+1] - years[i] > 300:
            gaps.append(f"TIMELINE GAP: {years[i]} to {years[i+1]} ({years[i+1]-years[i]} years)")

    conn.close()
    return gaps

if __name__ == "__main__":
    results = audit()
    for r in results:
        print(r)
