import sqlite3
from pathlib import Path

DB_PATH = Path(r"c:\Dev\EmeraldTablet\db\emerald_tablet.db")

PERSON_PERSON_REFS = [
    ("marsilio_ficino", "pico_della_mirandola", "INSPIRED"),
    ("isaac_casaubon", "marsilio_ficino", "CRITIQUED"),
    ("wouter_hanegraaff", "frances_yates", "CRITIQUED"),
    ("garth_fowden", "festugiere", "CRITIQUED"),
    ("thoth", "hermes_trismegistus", "SYNCRETIZED_AS"),
    ("zosimos_of_panopolis", "hermes_trismegistus", "FOLLOWER_OF"),
    ("albertus_magnus", "roger_bacon", "CONTEMPORARY")
]

TEXT_TEXT_REFS = [
    ("asclepius", "ch_i", "COMPLEMENTARY"),
    ("picatrix", "de_occulta_philosophia_libri_tres", "INFLUENCED"),
    ("yates_bruno", "hanegraaff_dgwe", "PRECEDED"),
    ("sirr_al_khaliqa", "emerald_tablet", "SOURCE_OF")
]

def setup():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 1. Person to Person
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS person_person_refs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            person_a TEXT,
            person_b TEXT,
            rel_type TEXT
        )
    """)
    for a, b, rel in PERSON_PERSON_REFS:
        cursor.execute("INSERT OR IGNORE INTO person_person_refs (person_a, person_b, rel_type) VALUES (?, ?, ?)", (a, b, rel))

    # 2. Text to Text
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS text_text_refs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text_a TEXT,
            text_b TEXT,
            rel_type TEXT
        )
    """)
    for a, b, rel in TEXT_TEXT_REFS:
        cursor.execute("INSERT OR IGNORE INTO text_text_refs (text_a, text_b, rel_type) VALUES (?, ?, ?)", (a, b, rel))

    conn.commit()
    conn.close()
    print("Granular relationship tables setup and populated.")

if __name__ == "__main__":
    setup()
