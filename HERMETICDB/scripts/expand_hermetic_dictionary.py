import sqlite3
from pathlib import Path

DB_PATH = Path(r"c:\Dev\EmeraldTablet\db\emerald_tablet.db")

DICTIONARY_ENTRIES = [
    ("logos", "Logos", "Word, reason, or discourse. In Hermeticism, the Logos is the creative instrument of the Mind (Nous) and the mediator between the divine and the material worlds.", "ACTOR_TERM", "PHILOSOPHICAL"),
    ("nous", "Nous", "Mind or Intellect. The supreme divine principle in Hermeticism, often personified as Poimandres. It is both the creator and the goal of human spiritual aspiration.", "ACTOR_TERM", "PHILOSOPHICAL"),
    ("pneuma", "Pneuma", "Spirit or Breath. A vital substance that permeates the cosmos and serves as the vehicle for divine influence and the soul's operations.", "ACTOR_TERM", "COSMOLOGICAL"),
    ("gnosis", "Gnosis", "Knowledge. Not mere discursive learning, but an experiential, transformative insight into the nature of God, the cosmos, and the self.", "ACTOR_TERM", "THEOLOGICAL"),
    ("eusebeia", "Eusebeia", "Piety. The proper attitude of the Hermetic practitioner towards God, often identified with the knowledge of God itself.", "ACTOR_TERM", "THEOLOGICAL"),
    ("thriskeia", "Thriskeia", "Cult or Worship. The ritual expression of piety, which in the 'Way of Hermes' often involves internal contemplation and the singing of hymns.", "ACTOR_TERM", "THEOLOGICAL"),
    ("aretalogy", "Aretalogy", "A literary genre consisting of a narrative of a god's miraculous deeds (aretai). Fowden uses this to explain the Egyptian roots of the Hermetic persona.", "ANALYST_TERM", "LINGUISTIC"),
    ("theurgy", "Theurgy", "God-working. Ritual practices aimed at achieving union with the divine, distinguished from 'lower' magic by its spiritual goals and philosophical framework.", "ACTOR_TERM", "THEOLOGICAL"),
    ("sympatheia", "Sympatheia", "Sympathy. The principle of universal interconnection that allows the technical Hermeticist to influence the material world through celestial alignments.", "ACTOR_TERM", "COSMOLOGICAL")
]

def expand():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for slug, label, definition, ctype, category in DICTIONARY_ENTRIES:
        cursor.execute("""
            INSERT OR IGNORE INTO concepts (slug, label, definition_short, category_type, category, source_method)
            VALUES (?, ?, ?, ?, ?, 'SCHOLARLY_EXPANSION')
        """, (slug, label, definition, ctype, category))
        
        # Link to Fowden if he's the primary source of this definition
        cursor.execute("SELECT id FROM texts WHERE text_id = 'FOWDEN_1986'")
        row = cursor.fetchone()
        if row:
            fid = row[0]
            cursor.execute("SELECT id FROM concepts WHERE slug = ?", (slug,))
            cid = cursor.fetchone()[0]
            cursor.execute("INSERT OR IGNORE INTO concept_text_refs (concept_id, text_id) VALUES (?, ?)", (cid, fid))

    conn.commit()
    conn.close()
    print("Hermetic Dictionary expanded.")

if __name__ == "__main__":
    expand()
