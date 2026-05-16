import sqlite3
from pathlib import Path

DB_PATH = Path(r"c:\Dev\EmeraldTablet\db\emerald_tablet.db")
FOWDEN_TXT = Path(r"C:\Users\PC\Downloads\fowden_extracted.txt")

def ingest():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 1. Update/Add Garth Fowden Biography
    fowden_bio = """
        <p>Garth Fowden is a distinguished historian of the Late Antique and Early Islamic worlds. He is the Sultan Qaboos Professor of Abrahamic Faiths at the University of Cambridge. His work is foundational for the 'historical approach' to Hermeticism, which seeks to root the philosophical texts in the socio-cultural reality of Roman Egypt.</p>
        <h2>The Egyptian Hermes (1986)</h2>
        <p>In his landmark monograph, <i>The Egyptian Hermes: A Historical Approach to the Late Pagan Mind</i>, Fowden argued against the then-dominant view (represented by A.-J. Festugière) that Hermeticism was a purely Greek 'literary' phenomenon with no connection to actual Egyptian practice. Fowden demonstrated that the 'Way of Hermes' was a coherent path of spiritual instruction that integrated technical practices (alchemy, astrology, magic) with philosophical contemplation. He emphasized the role of the Egyptian priesthood and the temple context in the formation of the Hermetica.</p>
    """
    cursor.execute("UPDATE persons SET bio_html = ? WHERE person_id = 'garth_fowden'", (fowden_bio,))

    # 2. Add New Concepts (Topics)
    concepts = [
        ('technical_hermetica', 'Technical Hermetica', 'Scholarly category for Hermetic texts dealing with practical sciences like alchemy, astrology, and magic.', 'ANALYST_TERM', 'SCIENTIFIC'),
        ('philosophical_hermetica', 'Philosophical Hermetica', 'Scholarly category for the theoretical, philosophical, and theological treatises of the Corpus Hermeticum and Asclepius.', 'ANALYST_TERM', 'PHILOSOPHICAL'),
        ('sympatheia', 'Sympatheia', 'The Stoic and Hermetic doctrine of universal sympathy, where all parts of the cosmos are interconnected.', 'ACTOR_TERM', 'COSMOLOGICAL'),
        ('via_universalis', 'Via Universalis', 'The concept of a "universal way" of salvation or knowledge that transcends specific cultic boundaries, often associated with Hermeticism and Neoplatonism.', 'ANALYST_TERM', 'THEOLOGICAL'),
        ('aretalogy', 'Aretalogy', 'A narrative of the miraculous deeds of a god or hero, common in the Late Antique context of Isis, Asclepius, and Hermes.', 'ANALYST_TERM', 'LINGUISTIC'),
        ('theurgy', 'Theurgy', 'Ritual practices designed to invoke the presence of the divine and achieve union with the gods, prominent in late Neoplatonism and some Hermetic circles.', 'ACTOR_TERM', 'THEOLOGICAL')
    ]
    for slug, label, desc, ctype, cat in concepts:
        cursor.execute("""
            INSERT OR IGNORE INTO concepts (slug, label, definition_short, category_type, category, source_method)
            VALUES (?, ?, ?, ?, ?, 'FOWDEN_INGESTION')
        """, (slug, label, desc, ctype, cat))

    # 3. Add New Persons (Scholarly Actors)
    persons = [
        ('manetho', 'Manetho', 'ANTIQUITY', 'HISTORIAN', 'Egyptian priest and historian who wrote the Aegyptiaca (History of Egypt).', 'FOWDEN_INGESTION'),
        ('chaeremon', 'Chaeremon of Alexandria', 'ANTIQUITY', 'PHILOSOPHER', 'Stoic philosopher and Egyptian priest who served as a tutor to Nero and wrote on Egyptian religion.', 'FOWDEN_INGESTION'),
        ('bitys', 'Bitys', 'ANTIQUITY', 'ALCHEMIST', 'A legendary Egyptian priest and alchemist mentioned by Iamblichus and Zosimos as a transmitter of Hermetic secrets.', 'FOWDEN_INGESTION')
    ]
    for pid, name, era, role, desc, method in persons:
        cursor.execute("""
            INSERT OR IGNORE INTO persons (person_id, name, era, role_primary, description, source_method)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (pid, name, era, role, desc, method))

    # 4. Ingest the Document
    cursor.execute("""
        INSERT OR IGNORE INTO corpus_documents (doc_id, file_path, title, doc_family, source_type, confidence)
        VALUES ('FOWDEN_1986', ?, 'The Egyptian Hermes', 'SCHOLARLY_MONOGRAPH', 'PDF_EXTRACTED', 'HIGH')
    """, (str(FOWDEN_TXT),))
    doc_id = cursor.execute("SELECT id FROM corpus_documents WHERE doc_id='FOWDEN_1986'").fetchone()[0]

    with open(FOWDEN_TXT, "r", encoding="utf-8") as f:
        content = f.read()
    
    import re
    pages = re.split(r'--- PAGE \d+ ---', content)
    for i, page_text in enumerate(pages):
        if len(page_text.strip()) < 50: continue
        cursor.execute("""
            INSERT OR IGNORE INTO corpus_segments (doc_id, segment_id, page_number, section_type, text_content, char_count)
            VALUES (?, ?, ?, 'CHAPTER', ?, ?)
        """, (doc_id, f"FOWDEN_P{i}", i, page_text.strip(), len(page_text)))

    conn.commit()
    conn.close()
    print("Ingestion of Fowden complete.")

if __name__ == "__main__":
    ingest()
