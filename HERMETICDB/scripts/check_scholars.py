import sqlite3
import os
from pathlib import Path

DB_PATH = Path(r"c:\Dev\EmeraldTablet\db\emerald_tablet.db")

def check_scholar(name):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM persons WHERE name LIKE ?", (f"%{name}%",))
    results = cursor.fetchall()
    conn.close()
    return results

if __name__ == "__main__":
    print(f"Mahé: {check_scholar('Mahé')}")
    print(f"Mahe: {check_scholar('Mahe')}")
    print(f"Fowden: {check_scholar('Fowden')}")
