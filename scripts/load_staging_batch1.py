"""Load staging batch 1: scholar essays + concept_links into the database."""
import json
import sqlite3
from pathlib import Path

DB_PATH = r"C:\Dev\EmeraldTablet\db\emerald_tablet.db"
SCHOLARS_JSON = r"C:\Dev\EmeraldTablet\staging\persons\scholar_essays_batch1.json"
LINKS_JSON = r"C:\Dev\EmeraldTablet\staging\concept_links\concept_links_batch1.json"


def load_scholar_essays(conn):
    cur = conn.cursor()
    with open(SCHOLARS_JSON, encoding="utf-8") as f:
        persons = json.load(f)

    for p in persons:
        pid = p["person_id"]
        bio = p.get("bio_html", "")
        desc = p.get("description", "")
        word_count = len(bio.split())
        if word_count < 600:
            print(f"  WARN: {pid} bio_html only {word_count} words — skipping")
            continue
        cur.execute(
            "UPDATE persons SET bio_html=?, description=? WHERE person_id=?",
            (bio, desc, pid),
        )
        status = f"updated ({word_count} words)" if cur.rowcount else "NOT FOUND in DB"
        print(f"  {pid}: {status}")

    conn.commit()
    print(f"Scholar essays loaded: {len(persons)} entries processed.")


def load_concept_links(conn):
    cur = conn.cursor()
    with open(LINKS_JSON, encoding="utf-8") as f:
        data = json.load(f)

    links = data["links"]
    inserted = 0
    skipped = 0
    for link in links:
        from_id = link["from_concept_id"]
        to_id = link["to_concept_id"]
        rel = link["relationship"]
        try:
            cur.execute(
                """INSERT OR IGNORE INTO concept_links
                   (from_concept_id, to_concept_id, relationship)
                   VALUES (?, ?, ?)""",
                (from_id, to_id, rel),
            )
            if cur.rowcount:
                inserted += 1
            else:
                skipped += 1
        except sqlite3.Error as e:
            print(f"  ERROR on {from_id}->{to_id}: {e}")
            skipped += 1

    conn.commit()
    print(f"Concept links: {inserted} inserted, {skipped} skipped (already existed).")


def main():
    conn = sqlite3.connect(DB_PATH)
    print("=== Loading scholar essays ===")
    load_scholar_essays(conn)
    print("\n=== Loading concept links ===")
    load_concept_links(conn)
    conn.close()
    print("\nDone. Run DEPLOY_PORTAL.py to rebuild the site.")


if __name__ == "__main__":
    main()
