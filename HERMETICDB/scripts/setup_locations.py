import sqlite3
from pathlib import Path

DB_PATH = Path(r"c:\Dev\EmeraldTablet\db\emerald_tablet.db")

LOCATIONS = [
    ("alexandria", "Alexandria, Egypt", 31.2001, 29.9187, "The intellectual cradle of the philosophical Hermetica and the center of the Greco-Egyptian synthesis."),
    ("panopolis", "Panopolis (Akhmim), Egypt", 26.5667, 31.7333, "The hometown of Zosimos of Panopolis, where technical Hermeticism (alchemy) was deeply rooted."),
    ("harran", "Harran, Turkey", 36.8617, 39.0306, "Home of the Sabians, who preserved Hermetic and Neoplatonic traditions into the Islamic era."),
    ("baghdad", "Baghdad, Iraq", 33.3152, 44.3661, "The heart of the Abbasid translation movement, where Hermetic texts were translated into Arabic."),
    ("florence", "Florence, Italy", 43.7696, 11.2558, "The site of Marsilio Ficino's 1463 translation of the Corpus Hermeticum, sparking the Renaissance revival."),
    ("prague", "Prague, Czech Republic", 50.0755, 14.4378, "The 'Alchemical Capital' of Europe under the patronage of Emperor Rudolf II."),
    ("london", "London, United Kingdom", 51.5074, -0.1278, "A major center for early modern Hermetic and Rosicrucian studies, home to John Dee and Robert Fludd.")
]

def setup():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS locations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            slug TEXT UNIQUE,
            label TEXT,
            lat REAL,
            lng REAL,
            description TEXT
        )
    """)

    for slug, label, lat, lng, desc in LOCATIONS:
        cursor.execute("""
            INSERT OR REPLACE INTO locations (slug, label, lat, lng, description)
            VALUES (?, ?, ?, ?, ?)
        """, (slug, label, lat, lng, desc))

    conn.commit()
    conn.close()
    print("Locations table setup and populated.")

if __name__ == "__main__":
    setup()
