import sqlite3
from pathlib import Path

DB_PATH = Path(r"c:\Dev\EmeraldTablet\db\emerald_tablet.db")

EDGES = [
    ("hermes_trismegistus", "ch_i", "AUTHOR"),
    ("hermes_trismegistus", "asclepius", "AUTHOR"),
    ("hermes_trismegistus", "emerald_tablet", "AUTHOR"),
    ("zosimos_of_panopolis", "mushaf_al_suwar", "AUTHOR"),
    ("jabir_ibn_hayyan", "sirr_al_khaliqa", "SCHOLAR"),
    ("marsilio_ficino", "ch_i", "TRANSLATOR"),
    ("giordano_bruno", "ch_i", "SCHOLAR"),
    ("john_dee", "monas_hieroglyphica", "AUTHOR"),
    ("garth_fowden", "FOWDEN_1986", "AUTHOR"),
    ("garth_fowden", "ch_i", "SCHOLAR"),
    ("wouter_hanegraaff", "hanegraaff_dgwe", "AUTHOR"),
    ("frances_yates", "yates_bruno", "AUTHOR"),
    ("brian_copenhaver", "copenhaver_hermetica", "AUTHOR"),
    ("jean-pierre_mahe", "asclepius", "SCHOLAR"),
    ("zosimos_of_panopolis", "ch_i", "SCHOLAR")
]

def setup():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS person_text_refs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            person_id TEXT,
            text_id TEXT,
            rel_type TEXT
        )
    """)

    for pid, tid, rel in EDGES:
        cursor.execute("""
            INSERT OR IGNORE INTO person_text_refs (person_id, text_id, rel_type)
            VALUES (?, ?, ?)
        """, (pid, tid, rel))

    conn.commit()
    conn.close()
    print("Graph edges table setup and populated.")

if __name__ == "__main__":
    setup()
