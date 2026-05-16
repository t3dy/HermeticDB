import sqlite3
from pathlib import Path

DB_PATH = Path(r"c:\Dev\EmeraldTablet\db\emerald_tablet.db")

SCHOLARLY_EVENTS = [
    (1471, 1471, 'PUBLICATION', 'Ficino: Pimander', 'Marsilio Ficino publishes the first Latin translation of the Corpus Hermeticum (CH I-XIV), initiating the Renaissance Hermetic revival.'),
    (1614, 1614, 'SCHOLARSHIP', 'Casaubon: Redating of the Hermetica', 'Isaac Casaubon demonstrates that the Hermetica are not ancient Egyptian but post-Christian, utilizing philological evidence.'),
    (1906, 1906, 'SCHOLARSHIP', 'Reitzenstein: Poimandres', 'Richard Reitzenstein publishes Poimandres: Studien zur griechisch-agyptischen und fruhchristlichen Literatur, founding modern philological research.'),
    (1945, 1954, 'SCHOLARSHIP', 'Festugière: La Révélation', 'A.-J. Festugière publishes his four-volume masterpiece La Révélation d\'Hermès Trismégiste, providing a comprehensive "Greek" reading.'),
    (1964, 1964, 'PUBLICATION', 'Yates: Giordano Bruno', 'Frances Yates publishes Giordano Bruno and the Hermetic Tradition, bringing Hermeticism into the mainstream of intellectual history.'),
    (1986, 1986, 'PUBLICATION', 'Fowden: The Egyptian Hermes', 'Garth Fowden publishes The Egyptian Hermes, arguing for the local Egyptian context of the tradition.'),
    (2005, 2005, 'PUBLICATION', 'Hanegraaff: DGWE', 'The Dictionary of Gnosis and Western Esotericism is published, establishing the field as a formal academic discipline.')
]

def update():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for start, end, etype, title, desc in SCHOLARLY_EVENTS:
        cursor.execute("""
            INSERT OR IGNORE INTO timeline_events (year, year_end, event_type, title, description, confidence)
            VALUES (?, ?, ?, ?, ?, 'HIGH')
        """, (start, end, etype, title, desc))

    conn.commit()
    conn.close()
    print("Scholarly timeline events updated.")

if __name__ == "__main__":
    update()
