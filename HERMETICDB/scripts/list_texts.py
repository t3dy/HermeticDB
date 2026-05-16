import sqlite3
from pathlib import Path

DB_PATH = Path(r"c:\Dev\EmeraldTablet\db\emerald_tablet.db")

def get_texts():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT title, text_type FROM texts")
    results = cursor.fetchall()
    conn.close()
    return results

if __name__ == "__main__":
    texts = get_texts()
    for t in texts:
        print(f"{t[0]} ({t[1]})")
