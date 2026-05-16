import sqlite3
from pathlib import Path

DB_PATH = Path(r"c:\Dev\EmeraldTablet\db\emerald_tablet.db")

MEDIEVAL_PERSONS = [
    ("jabir_ibn_hayyan", "Jabir ibn Hayyan (Geber)", "MEDIEVAL", "ALCHEMIST", "The foundational figure of Islamic alchemy, whose corpus is deeply permeated by Hermetic philosophy and the 'Balance' of nature.", "MEDIEVAL_EXPANSION"),
    ("ibn_umayl", "Ibn Umayl (Senior Zadith)", "MEDIEVAL", "ALCHEMIST", "An influential 10th-century alchemist whose 'Silvery Water' preserves profound Hermetic symbolisms and commentaries.", "MEDIEVAL_EXPANSION"),
    ("abu_mashar", "Abu Ma'shar (Albumasar)", "MEDIEVAL", "ASTROLOGER", "The most famous astrologer of the Islamic world, who identified Hermes with the prophet Idris/Enoch.", "MEDIEVAL_EXPANSION"),
    ("maslama_al_majriti", "Maslama al-Majriti (Pseudo)", "MEDIEVAL", "MAGE", "The traditional author of the Ghayat al-Hakim (Picatrix), associated with the Hermetic circles of Al-Andalus.", "MEDIEVAL_EXPANSION"),
    ("albertus_magnus", "Albertus Magnus", "MEDIEVAL", "THEOLOGIAN", "The 'Doctor Universalis' who commented on Hermetic alchemical and magical texts in the 13th century.", "MEDIEVAL_EXPANSION"),
    ("hugo_of_santalla", "Hugo of Santalla", "MEDIEVAL", "TRANSLATOR", "A 12th-century translator from Arabic to Latin, responsible for introducing many Hermetic texts to Europe.", "MEDIEVAL_EXPANSION")
]

MEDIEVAL_TEXTS = [
    ("sirr_al_khaliqa", "Sirr al-Khaliqa (The Secret of Creation)", "The earliest Arabic text to preserve the Emerald Tablet, attributed to Balinas (Apollonius of Tyana).", "TREATISE", "MEDIEVAL_EXPANSION", "ARABIC_HERMETICA"),
    ("mushaf_al_suwar", "Mushaf al-Suwar (The Book of Pictures)", "A famous Arabic alchemical work attributed to Zosimos, filled with Hermetic allegorical illustrations.", "TREATISE", "MEDIEVAL_EXPANSION", "ARABIC_HERMETICA"),
    ("liber_24_philosophorum", "Liber XXIV philosophorum", "A Medieval Latin text containing 24 definitions of God, often cited for the Hermetic definition of God as an infinite sphere.", "PRIMARY_SOURCE", "MEDIEVAL_EXPANSION", "LATIN_MEDIEVAL"),
    ("secretum_secretorum", "Secretum Secretorum (Secret of Secrets)", "A pseudo-Aristotelian work that includes Hermetic medical, astrological, and alchemical lore.", "TREATISE", "MEDIEVAL_EXPANSION", "LATIN_MEDIEVAL")
]

def populate():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for pid, name, era, role, desc, method in MEDIEVAL_PERSONS:
        cursor.execute("""
            INSERT OR IGNORE INTO persons (person_id, name, era, role_primary, description, source_method)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (pid, name, era, role, desc, method))

    for slug, title, desc, ttype, method, notes in MEDIEVAL_TEXTS:
        cursor.execute("""
            INSERT OR IGNORE INTO texts (text_id, title, description, text_type, source_method, transmission_notes)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (slug, title, desc, ttype, method, notes))

    conn.commit()
    conn.close()
    print("Medieval Hermetica (Arabic & Latin) populated.")

if __name__ == "__main__":
    populate()
