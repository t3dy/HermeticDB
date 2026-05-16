import sqlite3
from pathlib import Path

DB_PATH = Path(r"c:\Dev\EmeraldTablet\db\emerald_tablet.db")

def fix():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Mark scholarly works as COMMENTARY
    scholarly_ids = [
        "hanegraaff_dgwe", "yates_bruno", "copenhaver_hermetica", "ebeling_hermes", 
        "thrice_greatest_hermes", "faivre_esotericism", "stuckrad_esotericism", 
        "saif_arabic_hermes", "walker_magic", "zambelli_white_magic", "forshaw_khunrath",
        "FOWDEN_1986"
    ]
    
    for sid in scholarly_ids:
        cursor.execute("UPDATE texts SET text_type = 'COMMENTARY' WHERE text_id = ?", (sid,))

    # Mark others as PRIMARY_SOURCE if they were TREATISE or COMPILATION
    cursor.execute("UPDATE texts SET text_type = 'PRIMARY_SOURCE' WHERE text_type IN ('TREATISE', 'COMPILATION', 'TRANSLATION')")

    conn.commit()
    conn.close()
    print("Text types standardized (Scholarship = COMMENTARY).")

if __name__ == "__main__":
    fix()
