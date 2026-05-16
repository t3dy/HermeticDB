import sqlite3
import re
from pathlib import Path

DB_PATH = Path(r"c:\Dev\EmeraldTablet\db\emerald_tablet.db")

def extract():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT text_content FROM corpus_segments")
    segments = cursor.fetchall()
    all_text = " ".join([s['text_content'] for s in segments])

    # 1. Dictionary Terms (Concepts)
    concepts = [
        ("the_way_of_hermes", "The Way of Hermes", "The distinctive Hermetic path of spiritual initiation and contemplation, as described in the Corpus Hermeticum."),
        ("hermetic_persona", "Hermetic Persona", "The idealized figure of Hermes Trismegistus as a sage-prophet, used to authorize Hermetic revelation."),
        ("serapis", "Serapis", "A syncretic Greco-Egyptian deity whose cult center (the Serapeum) was a major intellectual hub in Alexandria."),
        ("book_of_thoth", "The Book of Thoth", "The legendary Egyptian source text to which many Hermetic works claimed to be related or descended."),
        ("hermetic_circles", "Hermetic Circles", "The small, informal groups of students and masters in which Hermetic teaching and ritual practice likely took place."),
        ("palingenesia", "Palingenesia", "Rebirth or regeneration. A central concept in CH XIII, describing the transformation of the soul through divine initiation.")
    ]

    for slug, label, desc in concepts:
        cursor.execute("""
            INSERT OR IGNORE INTO concepts (slug, label, definition_short, category_type, category, source_method)
            VALUES (?, ?, ?, 'ACTOR_TERM', 'THEOLOGICAL', 'SCHOLARLY_EXTRACTION')
        """, (slug, label, desc))

    # 2. Historical Context (Timeline)
    events = [
        (391, 391, 'EVENT', 'Destruction of the Serapeum', 'The Serapeum of Alexandria, a major center of Greco-Egyptian religious and intellectual life, is destroyed by a Christian mob.'),
        (200, 300, 'COMPOSITION', 'Peak of Hermetic Composition', 'The period in which the majority of the Greek Corpus Hermeticum was likely composed in Roman Egypt.')
    ]

    for start, end, etype, title, desc in events:
        cursor.execute("""
            INSERT OR IGNORE INTO timeline_events (year, year_end, event_type, title, description, confidence)
            VALUES (?, ?, ?, ?, ?, 'HIGH')
        """, (start, end, etype, title, desc))

    # 3. Locations (Geography)
    locations = [
        ("akhmim", "Akhmim (Panopolis)", 26.5667, 31.7333, "A center of Upper Egyptian culture where Zosimos and other Hermeticists were active."),
        ("hermopolis", "Hermopolis Magna", 27.7811, 30.8033, "The ancient Egyptian city dedicated to Thoth, identified as the spiritual home of Hermes Trismegistus.")
    ]

    for slug, label, lat, lng, desc in locations:
        cursor.execute("""
            INSERT OR REPLACE INTO locations (slug, lat, lng, label, description)
            VALUES (?, ?, ?, ?, ?)
        """, (slug, lat, lng, label, desc))

    conn.commit()
    conn.close()
    print("Scholarship entities extracted and populated.")

if __name__ == "__main__":
    extract()
