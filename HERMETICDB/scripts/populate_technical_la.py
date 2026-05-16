import sqlite3
from pathlib import Path

DB_PATH = Path(r"c:\Dev\EmeraldTablet\db\emerald_tablet.db")

TECHNICAL_LA = [
    ("brontologion", "The Brontologion of Hermes", "A Late Antique technical treatise on thunder-divination attributed to Hermes Trismegistus."),
    ("iatromathematica", "Iatromathematica of Hermes", "A collection of Hermetic texts on medical astrology, linking planetary decans to bodily ailments."),
    ("salmeschoiniaka", "The Salmeschoiniaka", "An ancient Egyptian-Hermetic work on the decans and their influence on human fate and health."),
    ("liber_vaccae", "Liber Vaccae (The Book of the Cow)", "A notorious Late Antique/Medieval work of 'astral' and 'natural' magic attributed to Hermes, involving extreme biological operations.")
]

def populate():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for slug, title, desc in TECHNICAL_LA:
        cursor.execute("""
            INSERT OR IGNORE INTO texts (text_id, title, description, text_type, source_method, transmission_notes)
            VALUES (?, ?, ?, 'TREATISE', 'SEED_DATA', 'TECHNICAL_HERMETICA')
        """, (slug, title, desc))

    conn.commit()
    conn.close()
    print("Technical Late Antique Hermetica populated.")

if __name__ == "__main__":
    populate()
