import sqlite3
from pathlib import Path

DB_PATH = Path(r"c:\Dev\EmeraldTablet\db\emerald_tablet.db")

RENAISSANCE_MODERN_PERSONS = [
    ("ludovico_lazzarelli", "Ludovico Lazzarelli", "RENAISSANCE", "POET", "A key figure in the 15th-century Hermetic revival and author of the Crater Hermetis.", "RENAISSANCE_EXPANSION"),
    ("francesco_patrizi", "Francesco Patrizi", "RENAISSANCE", "PHILOSOPHER", "A late Renaissance philosopher who sought to replace Aristotelianism with a Hermetic and Neoplatonic 'New Universal Philosophy'.", "RENAISSANCE_EXPANSION"),
    ("michael_maier", "Michael Maier", "EARLY_MODERN", "ALCHEMIST", "The physician and alchemist famous for his emblem book Atalanta Fugiens and his Hermetic defense of the Rosicrucians.", "RENAISSANCE_EXPANSION"),
    ("john_dee", "John Dee", "RENAISSANCE", "MATHEMATICIAN", "The Elizabethan polymath and magus who synthesized Hermeticism, Kabbalah, and angelic magic in his Monas Hieroglyphica.", "RENAISSANCE_EXPANSION"),
    ("isaac_casaubon", "Isaac Casaubon", "EARLY_MODERN", "SCHOLAR", "The brilliant philologist whose 1614 dating of the Hermetica effectively ended their status as ancient Egyptian revelations.", "RENAISSANCE_EXPANSION"),
    ("grs_mead", "G.R.S. Mead", "MODERN", "SCHOLAR", "A key figure in the Theosophical Society whose 'Thrice-Greatest Hermes' was the first comprehensive collection of Hermetic texts in English.", "RENAISSANCE_EXPANSION")
]

RENAISSANCE_MODERN_TEXTS = [
    ("crater_hermetis", "Crater Hermetis", "A dialogue by Ludovico Lazzarelli that blends Hermetic themes with Christian theology and ritual.", "PRIMARY_SOURCE", "RENAISSANCE_EXPANSION", "RENAISSANCE_HERMETICA"),
    ("monas_hieroglyphica", "Monas Hieroglyphica", "John Dee's complex esoteric treatise explaining a single symbol that encompasses all Hermetic and alchemical truth.", "TREATISE", "RENAISSANCE_EXPANSION", "RENAISSANCE_HERMETICA"),
    ("atalanta_fugiens", "Atalanta Fugiens", "Michael Maier's alchemical emblem book, combining music, image, and text in a unique Hermetic synthesis.", "TREATISE", "RENAISSANCE_EXPANSION", "RENAISSANCE_HERMETICA"),
    ("thrice_greatest_hermes", "Thrice-Greatest Hermes (Mead)", "The landmark 1906 collection and commentary by G.R.S. Mead that introduced the Hermetica to the modern English-speaking world.", "SCHOLARSHIP", "RENAISSANCE_EXPANSION", "MODERN_RECEPTION")
]

def populate():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for pid, name, era, role, desc, method in RENAISSANCE_MODERN_PERSONS:
        cursor.execute("""
            INSERT OR IGNORE INTO persons (person_id, name, era, role_primary, description, source_method)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (pid, name, era, role, desc, method))

    for slug, title, desc, ttype, method, notes in RENAISSANCE_MODERN_TEXTS:
        cursor.execute("""
            INSERT OR IGNORE INTO texts (text_id, title, description, text_type, source_method, transmission_notes)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (slug, title, desc, ttype, method, notes))

    conn.commit()
    conn.close()
    print("Renaissance, Early Modern, and Modern Hermetica populated.")

if __name__ == "__main__":
    populate()
