import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR.parent / "db" / "emerald_tablet.db"

NEW_TEXTS = [
    ("dictionary_of_gnosis", "Dictionary of Gnosis and Western Esotericism", "ENGLISH", "COMPILATION", 2006, 2006, "Edited by Wouter Hanegraaff.", "Scholarly encyclopedic reference.", "SEED_DATA", "REVIEWED", "HIGH"),
    ("copenhaver_hermetica", "Hermetica: The Greek Corpus Hermeticum and the Latin Asclepius", "ENGLISH", "TRANSLATION", 1992, 1992, "Translated and introduced by Brian P. Copenhaver.", "The standard English academic translation.", "SEED_DATA", "REVIEWED", "HIGH")
]

PROSE_DATA = {
    # Hanegraaff
    "wouter_hanegraaff": """
        <p>Wouter J. Hanegraaff (b. 1961) is the foundational figure in the institutionalization of Western Esotericism as a recognized academic discipline. As the first Professor of the History of Hermetic Philosophy and Related Currents at the University of Amsterdam, he has fundamentally shifted the historiography of Renaissance magic and Hermeticism.</p>
        <h2>The 'Rejected Knowledge' Paradigm</h2>
        <p>Hanegraaff's most crucial theoretical contribution, fully articulated in <i>Esotericism and the Academy: Rejected Knowledge in Western Culture</i> (2012), is the argument that 'esotericism' is not a coherent historical tradition. Instead, it is a polemical wastebasket category created by Enlightenment rationalists and Protestant theologians to exclude forms of thought they deemed irrational or heretical (such as magic, alchemy, and Hermeticism). By studying esotericism, scholars are not uncovering a secret tradition, but rather the 'Other' against which modern Western identity constructed itself.</p>
        <h2>The Dictionary of Gnosis and Western Esotericism</h2>
        <p>In 2006, Hanegraaff edited the monumental <i>Dictionary of Gnosis and Western Esotericism</i>. This work explicitly combated the 'reification' problem (treating scholarly categories as real, bounded traditions) by emphasizing continuous historical evolution, the multi-dimensionality of actors (e.g., separating John Dee the mathematician from John Dee the angel-conjuror), and strict periodization.</p>
    """,
    # Copenhaver
    "brian_copenhaver": """
        <p>Brian P. Copenhaver is a leading historian of Renaissance philosophy, magic, and science, best known for his definitive English translation of the <i>Corpus Hermeticum</i> and the <i>Asclepius</i> (1992).</p>
        <h2>Reframing Renaissance Magic</h2>
        <p>Copenhaver serves as a crucial corrective to the 'Yates Paradigm'. While Frances Yates posited a coherent 'Hermetic Tradition' that directly sparked the Scientific Revolution, Copenhaver demonstrated through meticulous philological and philosophical analysis that Renaissance 'magic' was not a monolith. He heavily emphasizes the Aristotelian and scholastic roots of occult qualities, showing that figures like Marsilio Ficino and Giovanni Pico della Mirandola were engaged in complex, orthodox philosophical problems, rather than simply reviving an Egyptian counter-religion.</p>
        <h2>The Translation of the Hermetica</h2>
        <p>Copenhaver's 1992 <i>Hermetica</i> replaced the earlier translation by Walter Scott, which was notorious for aggressively restructuring and 'correcting' the Greek text. Copenhaver's edition preserved the textual difficulties and contradictions of the original treatises, recognizing them not as corrupted philosophy, but as authentic traces of a diverse, Late Antique Egyptian religious milieu grappling with Hellenistic philosophy.</p>
    """,
    # The Texts
    "dictionary_of_gnosis": """
        <p>The <i>Dictionary of Gnosis and Western Esotericism</i> (2006), edited by Wouter J. Hanegraaff alongside Antoine Faivre, Roelof van den Broek, and Jean-Pierre Brach, is the definitive academic reference work for the field of esoteric studies.</p>
        <h2>Historiographical Methodology</h2>
        <p>The Dictionary is famous for its rigorous structural methodology. It explicitly rejects the 'religionism' of earlier occultists, instead adopting an empirical, historical approach. Entries are characterized by terminological self-awareness, acknowledging that labels like 'Hermeticism' or 'Magic' are often retrospective scholarly constructions rather than terms used by the historical actors themselves. It enforces strict periodization (e.g., distinguishing between Late Antique Hermeticism and Renaissance Hermeticism) and concludes each entry with a comprehensive bibliography split between primary sources and secondary literature.</p>
    """,
    "copenhaver_hermetica": """
        <p>Brian P. Copenhaver's 1992 publication, <i>Hermetica: The Greek Corpus Hermeticum and the Latin Asclepius in a New English Translation, with Notes and Introduction</i>, is the standard modern English translation of the canonical Hermetic texts.</p>
        <h2>Scholarly Apparatus and Impact</h2>
        <p>Based largely on the authoritative French critical edition by A.D. Nock and A.-J. Festugière (1945–1954), Copenhaver's translation is lauded for its exhaustive introduction and massive critical notes. Copenhaver meticulously contextualized the treatises within Middle Platonism, Stoicism, and indigenous Egyptian religion. His translation permanently elevated the study of the Hermetica in the English-speaking academic world, providing the precise textual grounding necessary to evaluate the bold claims made by Frances Yates regarding the influence of these texts on the Renaissance.</p>
    """
}

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 1. Insert new texts
    for tid, title, lang, ttype, start, end, desc, html, source, review, conf in NEW_TEXTS:
        try:
            cursor.execute("""
                INSERT INTO texts (text_id, title, language, text_type, date_composed_start, date_composed_end, description, analysis_html, source_method, review_status, confidence)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (tid, title, lang, ttype, start, end, desc, html, source, review, conf))
        except sqlite3.IntegrityError:
            pass # Already exists

    # 2. Update prose
    for slug, prose in PROSE_DATA.items():
        cursor.execute("UPDATE persons SET bio_html = ? WHERE person_id = ?", (prose, slug))
        if cursor.rowcount == 0:
            cursor.execute("UPDATE texts SET analysis_html = ? WHERE text_id = ?", (prose, slug))
    
    # 3. Add Hanegraaff's category_type logic to the schema definition internally
    # In a real system, we would ALTER TABLE concepts ADD COLUMN category_type TEXT CHECK(...)
    try:
        cursor.execute("ALTER TABLE concepts ADD COLUMN category_type TEXT CHECK(category_type IN ('ACTOR_TERM', 'ANALYST_TERM', 'HYBRID'))")
    except sqlite3.OperationalError:
        pass # Already added

    # Update some concepts with category types
    cursor.execute("UPDATE concepts SET category_type = 'ACTOR_TERM' WHERE slug IN ('theurgy', 'tria_prima', 'nous', 'prima_materia')")
    cursor.execute("UPDATE concepts SET category_type = 'ANALYST_TERM' WHERE slug IN ('hermetism', 'esotericism', 'occultism')")
    
    conn.commit()
    conn.close()
    print("Copenhaver/Hanegraaff expansion complete.")

if __name__ == "__main__":
    main()
