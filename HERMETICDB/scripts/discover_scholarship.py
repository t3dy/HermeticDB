import sqlite3
import re
from pathlib import Path

DB_PATH = Path(r"c:\Dev\EmeraldTablet\db\emerald_tablet.db")

def discover():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # 1. Broad search for scholars mentioned in scholarship segments
    cursor.execute("SELECT text_content FROM corpus_segments")
    segments = cursor.fetchall()
    
    all_text = " ".join([s['text_content'] for s in segments])
    
    # Discovery patterns
    scholars = set(re.findall(r'([A-Z][a-z]+ [A-Z][a-z]+) \(\d{4}\)', all_text))
    # Add some known giants manually if not found
    giants = ["Frances Yates", "D.P. Walker", "Antoine Faivre", "Wouter Hanegraaff", "Brian Copenhaver", 
              "Peter Forshaw", "Florian Ebeling", "Liana Saif", "Paola Zambelli", "Moshe Idel", 
              "Kocku von Stuckrad", "Nicholas Goodrick-Clarke"]
    for g in giants: scholars.add(g)

    for name in scholars:
        slug = name.lower().replace(" ", "_").replace(".", "")
        cursor.execute("""
            INSERT OR IGNORE INTO persons (person_id, name, era, role_primary, source_method)
            VALUES (?, ?, 'MODERN', 'SCHOLAR', 'SCHOLARLY_DISCOVERY')
        """, (slug, name))

    # 2. Add Important Scholarly Texts (The user wants exhaustive)
    scholarship_texts = [
        ("hanegraaff_dgwe", "Wouter Hanegraaff", "Dictionary of Gnosis and Western Esotericism", 2005, "Brill"),
        ("yates_bruno", "Frances Yates", "Giordano Bruno and the Hermetic Tradition", 1964, "University of Chicago Press"),
        ("copenhaver_hermetica", "Brian Copenhaver", "Hermetica: The Greek Corpus Hermeticum and the Latin Asclepius", 1992, "Cambridge University Press"),
        ("faivre_esotericism", "Antoine Faivre", "Access to Western Esotericism", 1994, "SUNY Press"),
        ("ebeling_hermes", "Florian Ebeling", "The Secret History of Hermes Trismegistus", 2007, "Cornell University Press"),
        ("stuckrad_esotericism", "Kocku von Stuckrad", "Western Esotericism: A Brief History of Secret Knowledge", 2005, "Equinox"),
        ("saif_arabic_hermes", "Liana Saif", "The Arabic Influences on Early Modern Occult Philosophy", 2015, "Palgrave Macmillan"),
        ("walker_magic", "D.P. Walker", "Spiritual and Demonic Magic: From Ficino to Campanella", 1958, "Warburg Institute"),
        ("zambelli_white_magic", "Paola Zambelli", "White Magic, Black Magic in the European Renaissance", 2007, "Brill"),
        ("forshaw_khunrath", "Peter Forshaw", "The Alchemical Amphitheatre: Heinrich Khunrath and the Magical Citadel", 2006, "Thesis/Various")
    ]

    for sid, author, title, year, pub in scholarship_texts:
        cursor.execute("""
            INSERT OR IGNORE INTO bibliography (source_id, author, title, year, publisher, pub_type, relevance)
            VALUES (?, ?, ?, ?, ?, 'MONOGRAPH', 'PRIMARY')
        """, (sid, author, title, year, pub))
        
        # Also add to texts for the relational browser
        cursor.execute("""
            INSERT OR IGNORE INTO texts (text_id, title, description, text_type, source_method, transmission_notes)
            VALUES (?, ?, ?, 'SCHOLARSHIP', 'SCHOLARLY_DISCOVERY', 'MODERN_ANALYSIS')
        """, (sid, title, f"Foundational scholarly work by {author}."))

    # 3. Add Contextual Primary Texts mentioned in Fowden/Lucentini
    primary_context = [
        ("iamblichus_mysteriis", "Iamblichus: De Mysteriis", "On the Mysteries of the Egyptians, Chaldeans, and Assyrians. A key defense of theurgy."),
        ("manetho_aegyptiaca", "Manetho: Aegyptiaca", "The History of Egypt, used as a primary source for Egyptian chronological and religious transmission."),
        ("chaeremon_fragments", "Chaeremon: Fragments", "The writings of the Stoic priest-philosopher of Alexandria, key for the Egyptian-Greek synthesis."),
        ("clement_stromata", "Clement of Alexandria: Stromata", "A key early Christian source that preserves descriptions of the Hermetic procession and books."),
        ("eusebius_praeparatio", "Eusebius: Praeparatio Evangelica", "A massive work preserving numerous fragments of lost pagan and Hermetic works."),
        ("lactantius_divinae", "Lactantius: Divinae Institutiones", "The Divine Institutes, where Hermes is cited as an ancient prophet of monotheism.")
    ]

    for slug, title, desc in primary_context:
        cursor.execute("""
            INSERT OR IGNORE INTO texts (text_id, title, description, text_type, source_method, transmission_notes)
            VALUES (?, ?, ?, 'PRIMARY_SOURCE', 'SCHOLARLY_DISCOVERY', 'CONTEXTUAL_PAGAN')
        """, (slug, title, desc))

    conn.commit()
    conn.close()
    print("Scholarship discovery and population complete.")

if __name__ == "__main__":
    discover()
