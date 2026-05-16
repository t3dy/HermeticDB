import sqlite3
from pathlib import Path

DB_PATH = Path(r"c:\Dev\EmeraldTablet\db\emerald_tablet.db")

def sync():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM bibliography")
    bibs = cursor.fetchall()

    for b in bibs:
        sid, title, author = b['source_id'], b['title'], b['author']
        cursor.execute("""
            INSERT OR IGNORE INTO texts (text_id, title, description, text_type, source_method)
            VALUES (?, ?, ?, 'COMMENTARY', 'BIBLIOGRAPHY_SYNC')
        """, (sid, title, f"Scholarly work by {author}."))

    conn.commit()
    conn.close()
    print("Bibliography synced to Texts as COMMENTARY.")

if __name__ == "__main__":
    sync()
