import sqlite3
from pathlib import Path

DB_PATH = Path(r"c:\Dev\EmeraldTablet\db\emerald_tablet.db")

PHILOSOPHICAL = [
    ("ch_i", "CH I: Poimandres", "The opening revelation of the Corpus Hermeticum."),
    ("ch_iv", "CH IV: The Mixing Bowl (Krater)", "Treatise on the immersion in the Mind."),
    ("ch_x", "CH X: The Key", "A comprehensive summary of Hermetic doctrine."),
    ("ch_xiii", "CH XIII: On Rebirth", "A ritual-dialogue on the secret discourse of the mountain."),
    ("asclepius", "The Asclepius", "The Perfect Sermon, preserved in Latin, discussing the nature of the gods and man-made idols."),
    ("kore_kosmou", "The Kore Kosmou (Virgin of the World)", "A massive cosmological and mythological fragment preserved by Stobaeus."),
    ("ogdoad_ennead", "The Discourse on the Eighth and Ninth", "A Coptic Hermetic text from Nag Hammadi (NHC VI, 6) describing a ritual initiation.")
]

TECHNICAL = [
    ("emerald_tablet", "The Emerald Tablet (Tabula Smaragdina)", "The foundational text of Western Alchemy, emphasizing the correspondence of Macrocosm and Microcosm."),
    ("kyranides", "The Cyranides (Kyranides)", "A massive compendium of Hermetic natural magic, lapidaries, and herbalism."),
    ("liber_hermetis", "Liber Hermetis", "An extensive Latin Hermetic astrological treatise on the decans and lots."),
    ("picatrix", "The Picatrix (Ghayat al-Hakim)", "The definitive medieval manual of astral magic, heavily attributed to Hermetic roots."),
    ("centiloquium", "The Centiloquium (Hermetic)", "A collection of 100 astrological aphorisms attributed to Hermes.")
]

def populate():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Ensure text_type and tradition columns can handle our classification
    # Based on schema: tradition CHECK(tradition IN ('SIRR_AL_KHALIQA','SECRETUM_SECRETORUM','JABIRIAN','IBN_UMAYL','VULGATE','HUGO_OF_SANTALLA','INDEPENDENT','MODERN') OR tradition IS NULL)
    
    for slug, title, desc in PHILOSOPHICAL:
        cursor.execute("""
            INSERT OR IGNORE INTO texts (text_id, title, description, text_type, source_method, transmission_notes)
            VALUES (?, ?, ?, 'PRIMARY_SOURCE', 'SEED_DATA', 'THEOLOGICAL_HERMETICA')
        """, (slug, title, desc))

    for slug, title, desc in TECHNICAL:
        cursor.execute("""
            INSERT OR IGNORE INTO texts (text_id, title, description, text_type, source_method, transmission_notes)
            VALUES (?, ?, ?, 'TREATISE', 'SEED_DATA', 'TECHNICAL_HERMETICA')
        """, (slug, title, desc))

    conn.commit()
    conn.close()
    print("Hermetic Corpus Map data populated.")

if __name__ == "__main__":
    populate()
