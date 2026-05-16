import sqlite3
import sys
from pathlib import Path

# Force UTF-8 for Windows console
if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR.parent / "db" / "emerald_tablet.db"

ENTITIES = {
    "persons": [
        # (LATE ANTIQUITY)
        ("hermes_trismegistus", "Hermes Trismegistus", "LATE_ANTIQUITY", "MYTHICAL_FIGURE", "Progenitor of the Hermetic arts."),
        ("zosimos_of_panopolis", "Zosimos of Panopolis", "LATE_ANTIQUITY", "PHILOSOPHER", "Pivotal Greco-Egyptian alchemist of the 3rd century."),
        ("iamblichus", "Iamblichus of Chalcis", "LATE_ANTIQUITY", "PHILOSOPHER", "Founder of theurgical Neoplatonism."),
        ("porphyry", "Porphyry of Tyre", "LATE_ANTIQUITY", "PHILOSOPHER", "Student of Plotinus and critic of theurgy."),
        ("plotinus", "Plotinus", "LATE_ANTIQUITY", "PHILOSOPHER", "Founder of Neoplatonism."),
        ("proclus", "Proclus Lycaeus", "LATE_ANTIQUITY", "PHILOSOPHER", "The last great major figure of Neoplatonism."),
        ("balinas", "Apollonius of Tyana (Balinas)", "LATE_ANTIQUITY", "MYTHICAL_FIGURE", "Legendary sage associated with the Emerald Tablet discovery."),
        ("stephen_of_alexandria", "Stephen of Alexandria", "LATE_ANTIQUITY", "PHILOSOPHER", "7th-century scholar-alchemist in the Byzantine court."),
        ("julian_the_apostate", "Emperor Julian", "LATE_ANTIQUITY", "AUTHOR", "Roman emperor who attempted a Neoplatonic restoration."),
        ("jabir_ibn_hayyan", "Jābir ibn Ḥayyān (Geber)", "MEDIEVAL", "PHILOSOPHER", "The most influential figure in Arabic alchemy."),
        ("al_razi", "Abū Bakr al-Rāzī (Rhazes)", "MEDIEVAL", "PHILOSOPHER", "Persian polymath and experimental alchemist."),
        ("ibn_umayl", "Muḥammad ibn Umayl", "MEDIEVAL", "PHILOSOPHER", "Major author of symbolic Arabic alchemical poetry."),
        ("khalid_ibn_yazid", "Khalid ibn Yazid", "MEDIEVAL", "MYTHICAL_FIGURE", "Umayyad prince often credited as the 'first' Islamic alchemist."),
        ("albertus_magnus", "Albertus Magnus", "MEDIEVAL", "SCHOLAR", "Doctor Universalis who integrated Aristotelianism and alchemy."),
        ("thomas_aquinas", "Thomas Aquinas", "MEDIEVAL", "SCHOLAR", "Synthesized Aristotelian philosophy with Christian principles."),
        ("roger_bacon", "Roger Bacon", "MEDIEVAL", "SCHOLAR", "Early advocate of the experimental method."),
        ("petrus_bonus", "Petrus Bonus", "MEDIEVAL", "PHILOSOPHER", "Author of the 'Pretiosa Margarita Novella'."),
        ("nicolas_flamel", "Nicolas Flamel", "MEDIEVAL", "MYTHICAL_FIGURE", "Parisian scribe legendary for creating the Philosopher's Stone."),
        ("bernard_of_trevisan", "Bernard of Trevisan", "MEDIEVAL", "AUTHOR", "Aristocratic alchemist who wrote the 'Livre de la Philosophie Naturelle des Metaux'."),
        ("marsilio_ficino", "Marsilio Ficino", "RENAISSANCE", "SCHOLAR", "Translator of the Corpus Hermeticum into Latin."),
        ("giovanni_pico", "Giovanni Pico della Mirandola", "RENAISSANCE", "PHILOSOPHER", "Synthesized Hermetism, Kabbalah, and Platonism."),
        ("lodovico_lazzarelli", "Lodovico Lazzarelli", "RENAISSANCE", "AUTHOR", "Hermetic poet and author of the 'Crater Hermetis'."),
        ("cornelius_agrippa", "Heinrich Cornelius Agrippa", "RENAISSANCE", "SCHOLAR", "Author of 'De Occulta Philosophia Libri Tres'."),
        ("paracelsus", "Theophrastus Paracelsus", "RENAISSANCE", "PHILOSOPHER", "Swiss-German physician and alchemist; founder of Iatrochemistry."),
        ("john_dee", "John Dee", "RENAISSANCE", "SCHOLAR", "Elizabethan polymath and author of the 'Monas Hieroglyphica'."),
        ("giordano_bruno", "Giordano Bruno", "RENAISSANCE", "PHILOSOPHER", "Hermetic philosopher and cosmological visionary."),
        ("robert_fludd", "Robert Fludd", "RENAISSANCE", "SCHOLAR", "Engish physician and author of the 'Utriusque Cosmi Historia'."),
        ("michael_maier", "Michael Maier", "RENAISSANCE", "AUTHOR", "Alchemist and physician to Rudolf II; author of 'Atalanta Fugiens'."),
        ("basil_valentine", "Basil Valentine", "RENAISSANCE", "MYTHICAL_FIGURE", "Legendary monk-alchemist behind the 'Twelve Keys'."),
        ("heinrich_khunrath", "Heinrich Khunrath", "RENAISSANCE", "AUTHOR", "Author of the 'Amphitheatrum Sapientiae Aeternae'."),
        ("andreas_libavius", "Andreas Libavius", "RENAISSANCE", "SCHOLAR", "Critic of Paracelsus; author of the first chemistry textbook, 'Alchemia'."),
        ("brian_copenhaver", "Brian P. Copenhaver", "MODERN", "SCHOLAR", "Translator of the 'Hermetica' and major historian of magic."),
        ("wouter_hanegraaff", "Wouter J. Hanegraaff", "MODERN", "SCHOLAR", "Founder of Western Esotericism studies."),
        ("garth_fowden", "Garth Fowden", "MODERN", "SCHOLAR", "Author of 'The Egyptian Hermes'."),
        ("florian_ebeling", "Florian Ebeling", "MODERN", "SCHOLAR", "Historian profile of the Hermetic tradition."),
        ("peter_forshaw", "Peter J. Forshaw", "MODERN", "SCHOLAR", "Expert on Khunrath and Christian Cabala."),
        ("didier_kahn", "Didier Kahn", "MODERN", "SCHOLAR", "French scholar specializing in Paracelsianism and Libavius."),
        ("hereward_tilton", "Hereward Tilton", "MODERN", "SCHOLAR", "Authority on Michael Maier and Rosicrucianism."),
        ("marco_pasi", "Marco Pasi", "MODERN", "SCHOLAR", "Expert on Western Esotericism and modern occultism."),
        ("christian_bull", "Christian H. Bull", "MODERN", "SCHOLAR", "Expert on the Egyptian context of Hermetism."),
        ("david_litwa", "M. David Litwa", "MODERN", "SCHOLAR", "Translator of newly discovered Hermetic fragments."),
    ],
    "texts": [
        ("corpus_hermeticum", "Corpus Hermeticum", "LATE_ANTIQUITY", "PRIMARY_SOURCE", "A collection of 17 Greek treatises on Hermetic philosophy."),
        ("asclepius", "The Asclepius", "LATE_ANTIQUITY", "PRIMARY_SOURCE", "A dialogue on the nature of the cosmos and theurgy."),
        ("picatrix", "Picatrix (Ghayat al-Hakim)", "MEDIEVAL", "TREATISE", "Arabic grimoire of astral magic integral to the Hermetic tradition."),
        ("emerald_tablet", "The Emerald Tablet", "MEDIEVAL", "PRIMARY_SOURCE", "The foundational text of the alchemical tradition."),
        ("kitab_sirr_al_khaliqa", "Kitāb Sirr al-Khalīqa", "MEDIEVAL", "PRIMARY_SOURCE", "The earliest source of the Emerald Tablet."),
        ("aurora_consurgens", "Aurora Consurgens", "MEDIEVAL", "PRIMARY_SOURCE", "Illuminated alchemical manuscript attributed to Aquinas."),
        ("rosarium_philosophorum", "Rosarium Philosophorum", "MEDIEVAL", "TREATISE", "16th-century compilation of early alchemical authority."),
        ("monas_hieroglyphica", "Monas Hieroglyphica", "RENAISSANCE", "TREATISE", "John Dee's esoteric mathematical symbol."),
        ("de_occulta_philosophia", "De Occulta Philosophia", "RENAISSANCE", "TREATISE", "Agrippa's synthesis of Renaissance magic."),
        ("atalanta_fugiens", "Atalanta Fugiens", "RENAISSANCE", "TREATISE", "Michael Maier's emblematic and musical alchemical work."),
        ("splendor_solis", "Splendor Solis", "RENAISSANCE", "PRIMARY_SOURCE", "One of the most beautifully illustrated alchemical manuscripts."),
        ("amphitheatrum_sapientiae", "Amphitheatrum Sapientiae Aeternae", "RENAISSANCE", "TREATISE", "Khunrath's masterpiece of theosophical alchemy."),
        ("theatrum_chem_britannicum", "Theatrum Chemicum Britannicum", "RENAISSANCE", "COMPILATION", "Elias Ashmole's collection of English alchemical verse."),
    ],
    "concepts": [
        ("theurgy", "Theurgy", "THEOLOGICAL", "Ritual practices aimed at achieving union with the divine (divine work)."),
        ("gnosis", "Gnosis", "THEOLOGICAL", "Experiential knowledge of the divine and the cosmic order."),
        ("nous", "Nous", "PHILOSOPHICAL", "The supreme intellect or divine mind that structures the universe."),
        ("spagyrics", "Spagyrics", "ALCHEMICAL", "The alchemical practice of separating and reuniting plant or mineral components."),
        ("ascent", "Cosmic Ascent", "PHILOSOPHICAL", "The journey of the soul through the planetary spheres to its divine origin."),
        ("decans", "Decans", "COSMOLOGICAL", "36 ten-degree segments of the zodiac with specific spirits and influences."),
        ("prima_materia", "Prima Materia", "ALCHEMICAL", "The original, undifferentiated substance required for the Great Work."),
        ("tria_prima", "Tria Prima", "ALCHEMICAL", "The three principles of matter: Sulfur, Salt, and Mercury."),
        ("monad", "The Monad", "PHILOSOPHICAL", "The singular, indivisible principle of unity at the root of all existence."),
        ("correspondence", "Doctrine of Correspondence", "PHILOSOPHICAL", "The axiom 'As above, so below,' linking macrocosm and microcosm."),
        ("quintessence", "Quintessence", "ALCHEMICAL", "The fifth element; the ethereal substance beyond the four earthly elements."),
    ]
}

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    print("Purging existing entities to refresh the knowledge-layer...")
    cursor.execute("DELETE FROM persons")
    cursor.execute("DELETE FROM texts")
    cursor.execute("DELETE FROM concepts")
    
    for pid, name, era, role, desc in ENTITIES["persons"]:
        cursor.execute("INSERT INTO persons (person_id, name, era, role_primary, description, source_method) VALUES (?, ?, ?, ?, ?, 'SEED_DATA')", (pid, name, era, role, desc))

    for tid, title, era, ttype, desc in ENTITIES["texts"]:
        cursor.execute("INSERT INTO texts (text_id, title, date_composed_start, text_type, description, source_method) VALUES (?, ?, ?, ?, ?, 'SEED_DATA')", (tid, title, 100 if era == 'LATE_ANTIQUITY' else 800 if era == 'MEDIEVAL' else 1500, ttype, desc))

    for slug, label, category, desc in ENTITIES["concepts"]:
        cursor.execute("INSERT INTO concepts (slug, label, category, definition_short, source_method) VALUES (?, ?, ?, ?, 'SEED_DATA')", (slug, label, category, desc))

    conn.commit()
    conn.close()
    print(f"Knowledge expansion complete. {len(ENTITIES['persons'])} Figures, {len(ENTITIES['texts'])} Texts, {len(ENTITIES['concepts'])} Concepts.")

if __name__ == "__main__":
    main()
