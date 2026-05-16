import sqlite3
from pathlib import Path

DB_PATH = Path(r"c:\Dev\EmeraldTablet\db\emerald_tablet.db")

MID_TIMELINE = [
    (529, 529, 'SCHOLARSHIP', 'Closure of the Platonic Academy', 'Justinian closes the Academy in Athens; Damascius and other Neoplatonists (some carrying Hermetic texts) flee to the Sassanid court.'),
    (750, 800, 'COMPOSITION', 'Composition of the Sirr al-Khaliqa', 'The earliest Arabic Hermetic synthesis, containing the Emerald Tablet, is attributed to Balinas.'),
    (830, 830, 'SCHOLARSHIP', 'The Sabians of Harran identified as Hermeticists', 'The community at Harran adopts the name "Sabians" and identifies Hermes (Idris) as their prophet to achieve "People of the Book" status under Al-Ma\'mun.'),
    (950, 980, 'PUBLICATION', 'Epistles of the Brethren of Purity', 'The Ikhwan al-Safa (Brethren of Purity) compile their encyclopedia, synthesizing Neoplatonism, Pythagoreanism, and Hermeticism.')
]

def fill():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for start, end, etype, title, desc in MID_TIMELINE:
        cursor.execute("""
            INSERT OR IGNORE INTO timeline_events (year, year_end, event_type, title, description, confidence)
            VALUES (?, ?, ?, ?, ?, 'HIGH')
        """, (start, end, etype, title, desc))

    conn.commit()
    conn.close()
    print("Timeline gaps filled.")

if __name__ == "__main__":
    fill()
