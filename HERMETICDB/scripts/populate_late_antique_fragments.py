import sqlite3
from pathlib import Path

DB_PATH = Path(r"c:\Dev\EmeraldTablet\db\emerald_tablet.db")

FRAGMENTS = [
    ("sh_fragments", "The Stobaean Fragments (SH 1-29)", "A collection of 29 fragments of Hermetic treatises preserved by the 5th-century anthologist John of Stobi (Stobaeus)."),
    ("armenian_definitions", "Definitions of Hermes to Asclepius (Armenian)", "A collection of Hermetic definitions preserved in Armenian, reflecting an early stage of the tradition."),
    ("prayer_thanksgiving", "The Prayer of Thanksgiving (NHC VI, 7)", "A liturgical prayer found at Nag Hammadi, also known from the Latin Asclepius and a Greek papyrus."),
    ("vienne_fragment", "The Vienne Fragment", "A Greek fragment of a Hermetic treatise discovered in Vienne, dealing with the nature of the soul."),
    ("lactantius_fragments", "Hermetic Fragments in Lactantius", "Quotes and summaries of lost Hermetic works preserved in the Divine Institutes of the Christian apologist Lactantius."),
    ("cyril_fragments", "Hermetic Fragments in Cyril of Alexandria", "Fragments preserved in Cyril's 'Against Julian', often providing Greek originals for texts known only in translation.")
]

def populate():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for slug, title, desc in FRAGMENTS:
        cursor.execute("""
            INSERT OR IGNORE INTO texts (text_id, title, description, text_type, source_method, transmission_notes)
            VALUES (?, ?, ?, 'PRIMARY_SOURCE', 'SEED_DATA', 'THEOLOGICAL_HERMETICA')
        """, (slug, title, desc))

    conn.commit()
    conn.close()
    print("Late Antique Hermetic fragments populated.")

if __name__ == "__main__":
    populate()
