import sqlite3
from pathlib import Path

DB_PATH = Path(r"c:\Dev\EmeraldTablet\db\emerald_tablet.db")

def fix():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Mark scholarly works as COMMENTARY based on common patterns
    patterns = [
        '%hanegraaff%', '%yates%', '%copenhaver%', '%fowden%', '%ebeling%', 
        '%stuckrad%', '%faivre%', '%saif%', '%walker%', '%zambelli%', '%forshaw%',
        '%scholarship%', '%modern%'
    ]
    
    for p in patterns:
        cursor.execute("UPDATE texts SET text_type = 'COMMENTARY' WHERE text_id LIKE ? OR title LIKE ?", (p, p))

    # Re-standardize Primary
    cursor.execute("UPDATE texts SET text_type = 'PRIMARY_SOURCE' WHERE text_type NOT IN ('COMMENTARY')")

    conn.commit()
    conn.close()
    print("Text types standardized via broad search.")

if __name__ == "__main__":
    fix()
