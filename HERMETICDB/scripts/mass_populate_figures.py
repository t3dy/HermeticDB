import sqlite3
from pathlib import Path

DB_PATH = Path(r"c:\Dev\EmeraldTablet\db\emerald_tablet.db")

FIGURES = [
    # ANTIQUITY
    ("hermes_trismegistus", "Hermes Trismegistus", "ANTIQUITY", "SAGE", "The legendary founder of the Hermetic tradition, identified with Thoth."),
    ("asclepius_sage", "Asclepius", "ANTIQUITY", "SAGE", "The mythical student of Hermes and a central interlocutor in the Hermetica."),
    ("tat", "Tat", "ANTIQUITY", "SAGE", "The son and student of Hermes in many philosophical discourses."),
    ("ammon", "Ammon", "ANTIQUITY", "SAGE", "The Egyptian king and student of Hermes mentioned in CH XVI."),
    ("agathodaimon", "Agathodaimon", "ANTIQUITY", "SAGE", "A divine or legendary figure often identified as the teacher of Hermes."),
    ("thoth", "Thoth", "ANTIQUITY", "DEITY", "The Egyptian god of wisdom and writing, the primary root of the Hermes persona."),
    ("isis", "Isis", "ANTIQUITY", "DEITY", "The Egyptian goddess who appears as a teacher of Hermes in the Kore Kosmou."),
    ("zosimos_of_panopolis", "Zosimos of Panopolis", "ANTIQUITY", "ALCHEMIST", "The first historical alchemist, a Hermetic priest and practitioner."),
    ("theosebeia", "Theosebeia", "ANTIQUITY", "ALCHEMIST", "The sister or companion of Zosimos, recipient of his alchemical instructions."),
    ("iamblichus", "Iamblichus", "ANTIQUITY", "PHILOSOPHER", "Neoplatonist who defended Hermeticism and theurgy in De Mysteriis."),
    ("porphyry", "Porphyry", "ANTIQUITY", "PHILOSOPHER", "Neoplatonist whose 'Letter to Anebo' prompted Iamblichus's defense of Hermes."),
    ("manetho", "Manetho", "ANTIQUITY", "PRIEST", "Egyptian priest whose work is cited as the source of Hermetic wisdom."),
    ("chaeremon", "Chaeremon", "ANTIQUITY", "PRIEST", "Stoic priest of Alexandria who sought to explain Egyptian religion philosophically."),
    ("bolos_of_mendes", "Bolos of Mendes", "ANTIQUITY", "ALCHEMIST", "The 'Pseudo-Democritus' who authored early technical alchemical works."),
    ("maria_the_jewess", "Maria the Jewess", "ANTIQUITY", "ALCHEMIST", "A legendary early alchemist mentioned in the Zosimos corpus."),
    ("cleopatra_alchemist", "Cleopatra the Alchemist", "ANTIQUITY", "ALCHEMIST", "One of the few female alchemists of Late Antiquity, author of Chrysopoeia."),
    ("olympiodorus", "Olympiodorus", "ANTIQUITY", "PHILOSOPHER", "Neoplatonic commentator on alchemical and Hermetic themes."),
    
    # MEDIEVAL
    ("al_kindi", "Al-Kindi", "MEDIEVAL", "PHILOSOPHER", "The 'Philosopher of the Arabs' who studied Hermetic astrology and science."),
    ("al_razi", "Al-Razi (Rhazes)", "MEDIEVAL", "ALCHEMIST", "A major physician and alchemist who integrated Hermetic lore into medical practice."),
    ("robert_of_chester", "Robert of Chester", "MEDIEVAL", "TRANSLATOR", "The first translator of an alchemical text from Arabic into Latin (1144)."),
    ("gerard_of_cremona", "Gerard of Cremona", "MEDIEVAL", "TRANSLATOR", "Prolific translator of Arabic scientific and Hermetic works."),
    ("arnald_of_villanova", "Arnald of Villanova", "MEDIEVAL", "ALCHEMIST", "Physician and alchemist associated with the 'Pseudo-Arnaldian' Hermetic corpus."),
    ("raymond_lull", "Raymond Lull (Pseudo)", "MEDIEVAL", "ALCHEMIST", "The Catalan mystic whose name was attached to a massive alchemical-Hermetic corpus."),
    
    # RENAISSANCE
    ("paracelsus", "Paracelsus", "RENAISSANCE", "ALCHEMIST", "The revolutionary physician who synthesized Hermeticism, alchemy, and folk medicine."),
    ("tommaso_campanella", "Tommaso Campanella", "RENAISSANCE", "PHILOSOPHER", "Dominican monk and magus, author of 'The City of the Sun', rooted in Hermetic ideals."),
    ("robert_fludd", "Robert Fludd", "RENAISSANCE", "PHYSICIAN", "The Rosicrucian apologist and author of 'Utriusque Cosmi Historia', a massive Hermetic encyclopedia."),
    ("heinrich_khunrath", "Heinrich Khunrath", "RENAISSANCE", "ALCHEMIST", "Author of the 'Amphitheatrum Sapientiae Aeternae', a visual masterpiece of Hermetic alchemy."),
    ("athanasius_kircher", "Athanasius Kircher", "EARLY_MODERN", "SCHOLAR", "The Jesuit polymath who studied Egyptian hieroglyphs through a Hermetic lens in 'Oedipus Aegyptiacus'.")
]

def populate():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for pid, name, era, role, desc in FIGURES:
        cursor.execute("""
            INSERT OR IGNORE INTO persons (person_id, name, era, role_primary, description, source_method)
            VALUES (?, ?, ?, ?, ?, 'MASS_POPULATION')
        """, (pid, name, era, role, desc))

    conn.commit()
    conn.close()
    print("Mass population of figures complete.")

if __name__ == "__main__":
    populate()
