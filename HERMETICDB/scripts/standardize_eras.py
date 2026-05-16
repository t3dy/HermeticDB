import sqlite3
from pathlib import Path

DB_PATH = Path(r"c:\Dev\EmeraldTablet\db\emerald_tablet.db")

def standardize():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Standardize to ANTIQUITY
    cursor.execute("UPDATE persons SET era = 'ANTIQUITY' WHERE era IN ('LATE_ANTIQUITY', 'ANCIENT', 'Late Antiquity')")
    
    # Standardize to MEDIEVAL
    cursor.execute("UPDATE persons SET era = 'MEDIEVAL' WHERE era IN ('Medieval')")
    
    # Standardize to RENAISSANCE
    cursor.execute("UPDATE persons SET era = 'RENAISSANCE' WHERE era IN ('Renaissance')")
    
    # Standardize to EARLY_MODERN
    cursor.execute("UPDATE persons SET era = 'EARLY_MODERN' WHERE era IN ('Early Modern')")
    
    # Standardize to MODERN
    cursor.execute("UPDATE persons SET era = 'MODERN' WHERE era IN ('Modern')")

    conn.commit()
    conn.close()
    print("Eras standardized.")

if __name__ == "__main__":
    standardize()
