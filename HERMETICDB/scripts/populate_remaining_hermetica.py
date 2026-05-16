import sqlite3
from pathlib import Path

DB_PATH = Path(r"c:\Dev\EmeraldTablet\db\emerald_tablet.db")

CH_REMAINING = [
    ("ch_ii", "CH II: To Hermes", "A discourse where Hermes explains the nature of the cosmos as a container and God as the container of all."),
    ("ch_iii", "CH III: A Sacred Discourse", "A brief, highly dense cosmogony describing the emergence of the elements and the zoidia (zodiac)."),
    ("ch_v", "CH V: God is Manifest", "A treatise arguing that God, though invisible, is manifest through the order and beauty of his creation."),
    ("ch_vi", "CH VI: God is the Good", "Explores the philosophical identity of God with the concept of the absolute Good."),
    ("ch_vii", "CH VII: The Greatest Evil", "A polemical discourse against ignorance, which is described as the greatest evil among men."),
    ("ch_viii", "CH VIII: Nothing is Lost", "Arguments for the immortality of the soul and the permanence of the cosmos."),
    ("ch_ix", "CH IX: On Thinking and Sense", "Distinguishes between divine thinking (noesis) and human sense perception (aisthesis)."),
    ("ch_xi", "CH XI: Mind to Hermes", "A revelation from the Mind (Nous) to Hermes about the infinity of God and the cosmos."),
    ("ch_xii", "CH XII: On the Common Mind", "Discusses the presence of the 'Common Mind' in all rational beings."),
    ("ch_xiv", "CH XIV: To Tat", "A summary discourse from Hermes to his son Tat on the nature of the creator."),
    ("ch_xvi", "CH XVI: Definitions of Asclepius", "A collection of definitions regarding God, matter, and the sun, translated from an 'original' Egyptian source."),
    ("ch_xvii", "CH XVII: To a King", "A brief fragment of a discourse addressed to a king (likely of Egypt) regarding the worship of God."),
    ("ch_xviii", "CH XVIII: Praise of Kings", "A rhetorical panegyric that utilizes Hermetic themes to praise earthly rulers.")
]

TECHNICAL_REMAINING = [
    ("liber_beibeniis", "Liber de stellis beibeniis", "A foundational Hermetic text on the 'beibian' stars (fixed stars of magical significance)."),
    ("seven_chapters", "The Seven Chapters of Hermes", "An ancient alchemical work detailing the seven steps of the Great Work."),
    ("golden_tractate", "The Golden Tractate (Tractatus Aureus)", "One of the most widely circulated medieval alchemical texts attributed to Hermes Trismegistus."),
    ("pgm_vii", "PGM VII: The Stele of Hermes", "A Greek magical papyrus containing a ritual invocation of Hermes as the 'Lord of the World'."),
    ("liber_25_chapters", "Liber Hermetis (25 Chapters)", "A Latin translation of a Greek Hermetic astrological work focusing on the decans and their physical effects.")
]

def populate():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for slug, title, desc in CH_REMAINING:
        cursor.execute("""
            INSERT OR IGNORE INTO texts (text_id, title, description, text_type, source_method, transmission_notes)
            VALUES (?, ?, ?, 'PRIMARY_SOURCE', 'SEED_DATA', 'THEOLOGICAL_HERMETICA')
        """, (slug, title, desc))

    for slug, title, desc in TECHNICAL_REMAINING:
        cursor.execute("""
            INSERT OR IGNORE INTO texts (text_id, title, description, text_type, source_method, transmission_notes)
            VALUES (?, ?, ?, 'TREATISE', 'SEED_DATA', 'TECHNICAL_HERMETICA')
        """, (slug, title, desc))

    conn.commit()
    conn.close()
    print("Remaining Hermetica populated.")

if __name__ == "__main__":
    populate()
