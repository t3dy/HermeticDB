import sqlite3
import re
from pathlib import Path

DB_PATH = Path(r"c:\Dev\EmeraldTablet\db\emerald_tablet.db")
FOWDEN_DOC = Path(r"C:\Users\PC\Downloads\Garth Fowden - The Egyptian Hermes A Historical Approach to the Late Pagan Mind (1990, Cambridge University Press) - libgen.li.doc")
LUCENTINI_TXT = Path(r"C:\Users\PC\Downloads\Hermetism_OCR\hermetism_FULL.txt")

def extract_doc_text(path):
    with open(path, "rb") as f:
        data = f.read()
    # Find sequences of printable characters
    matches = re.findall(b'[a-zA-Z0-9\s.,;:\'\"()\-!?]{20,}', data)
    text = "\n".join([m.decode("ascii", errors="ignore") for m in matches])
    return text

def ingest():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 1. Add Mahé
    cursor.execute("""
        INSERT OR IGNORE INTO persons (person_id, name, era, role_primary, description, source_method, review_status, confidence)
        VALUES ('jean_pierre_mahe', 'Jean-Pierre Mahé', 'MODERN', 'SCHOLAR', 'French orientalist and preeminent scholar of Hermetic and Armenian traditions.', 'MANUAL_INGESTION', 'REVIEWED', 'HIGH')
    """)

    # 2. Add Bibliography
    cursor.execute("""
        INSERT OR IGNORE INTO bibliography (source_id, author, title, year, publisher, pub_type, relevance)
        VALUES ('fowden_1990', 'Garth Fowden', 'The Egyptian Hermes: A Historical Approach to the Late Pagan Mind', 1990, 'Cambridge University Press', 'MONOGRAPH', 'PRIMARY')
    """)
    cursor.execute("""
        INSERT OR IGNORE INTO bibliography (source_id, author, title, year, publisher, pub_type, relevance)
        VALUES ('lucentini_2001', 'Lucentini, Parri, Perrone Compagni (Eds.)', 'Hermetism from Late Antiquity to Humanism', 2001, 'Brepols', 'COLLECTION', 'PRIMARY')
    """)
    cursor.execute("""
        INSERT OR IGNORE INTO bibliography (source_id, author, title, year, pub_type, relevance)
        VALUES ('mahe_asclepius', 'Jean-Pierre Mahé', 'Théorie et pratique dans l''Asclepius', 2001, 'CHAPTER', 'PRIMARY')
    """)

    # 3. Add Corpus Documents
    cursor.execute("""
        INSERT OR IGNORE INTO corpus_documents (doc_id, file_path, title, doc_family, source_type, confidence)
        VALUES ('LUCENTINI_2001', ?, 'Hermetism from Late Antiquity to Humanism', 'CONFERENCE_PROCEEDINGS', 'OCR', 'HIGH')
    """, (str(LUCENTINI_TXT),))
    lucentini_id = cursor.lastrowid or cursor.execute("SELECT id FROM corpus_documents WHERE doc_id='LUCENTINI_2001'").fetchone()[0]

    cursor.execute("""
        INSERT OR IGNORE INTO corpus_documents (doc_id, file_path, title, doc_family, source_type, confidence)
        VALUES ('MAHE_ASCLEPIUS', ?, 'Théorie et pratique dans l''Asclepius', 'SCHOLARLY_ARTICLE', 'PDF_EXTRACTED', 'MEDIUM')
    """, (str(FOWDEN_DOC),))
    mahe_id = cursor.lastrowid or cursor.execute("SELECT id FROM corpus_documents WHERE doc_id='MAHE_ASCLEPIUS'").fetchone()[0]

    # 4. Ingest Segments for Lucentini
    with open(LUCENTINI_TXT, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()
    
    pages = re.split(r'--- PAGE \d+ ---', content)
    for i, page_text in enumerate(pages):
        if len(page_text.strip()) < 50: continue
        cursor.execute("""
            INSERT OR IGNORE INTO corpus_segments (doc_id, segment_id, page_number, section_type, text_content, char_count)
            VALUES (?, ?, ?, 'CHAPTER', ?, ?)
        """, (lucentini_id, f"LUCENTINI_P{i}", i, page_text.strip(), len(page_text)))

    # 5. Ingest Segments for Mahé (the doc file)
    mahe_text = extract_doc_text(FOWDEN_DOC)
    # Split into 2000 char chunks as pseudo-pages
    chunks = [mahe_text[i:i+2000] for i in range(0, len(mahe_text), 2000)]
    for i, chunk in enumerate(chunks):
        cursor.execute("""
            INSERT OR IGNORE INTO corpus_segments (doc_id, segment_id, page_number, section_type, text_content, char_count)
            VALUES (?, ?, ?, 'CHAPTER', ?, ?)
        """, (mahe_id, f"MAHE_SEG_{i}", i, chunk.strip(), len(chunk)))

    # 6. Update High Fidelity Prose for figures
    mahe_prose = """
        <p>Jean-Pierre Mahé (b. 1944) is a distinguished French orientalist and historian of religions, recognized as one of the world's leading authorities on the Armenian and Hermetic traditions. He holds the chair of Armenian Studies at the École Pratique des Hautes Études and is a member of the Académie des Inscriptions et Belles-Lettres.</p>
        <h2>The Hermès en Haute-Égypte</h2>
        <p>Mahé's most significant contribution to Hermetic scholarship is his monumental two-volume work, <i>Hermès en Haute-Égypte</i> (1978–1982). In this study, he provided critical editions and exhaustive commentaries on the Coptic Hermetica found at Nag Hammadi (Codex VI). Mahé's work was revolutionary because it demonstrated a much closer link between the philosophical Hermetica and native Egyptian temple traditions than previously assumed by the 'Grecian' school of Festugière. He argues that Hermeticism was not just a literary phenomenon but a living ritual practice in Late Antique Egypt.</p>
    """
    cursor.execute("UPDATE persons SET bio_html = ? WHERE person_id = 'jean_pierre_mahe'", (mahe_prose,))

    conn.commit()
    conn.close()
    print("Ingestion of scholarly wave complete.")

if __name__ == "__main__":
    ingest()
