import sqlite3
from pathlib import Path

DB_PATH = Path(r"c:\Dev\EmeraldTablet\db\emerald_tablet.db")

SCHOLARSHIP_SUMMARIES = {
    "hanegraaff_dgwe": """
        <p>The <i>Dictionary of Gnosis and Western Esotericism</i> is the definitive reference work for the field. Edited by Wouter J. Hanegraaff in collaboration with Antoine Faivre, Roelof van den Broek, and Jean-Pierre Brach, it contains over 400 entries by world-leading experts.</p>
        <p>The DGWE established the historiographical standard for Hermetic studies, emphasizing 'terminological self-awareness' and the distinction between actor and analyst categories.</p>
    """,
    "yates_bruno": """
        <p>Frances Yates's <i>Giordano Bruno and the Hermetic Tradition</i> (1964) is the book that 'launched' the modern study of Hermeticism. Yates argued that the Hermetica were the key to understanding the Renaissance world-view, scientific revolution, and the figure of the 'Magus'.</p>
        <p>While the 'Yates Paradigm' has been refined and critiqued by later scholars (notably for its over-emphasis on a coherent 'tradition'), it remains the starting point for any study of Renaissance Hermeticism.</p>
    """,
    "copenhaver_hermetica": """
        <p>Brian Copenhaver's <i>Hermetica</i> (1992) provides the standard English translation of the <i>Corpus Hermeticum</i> and the <i>Asclepius</i>. His extensive introduction and notes are essential for understanding the Greek and Latin textual traditions and their philosophical nuances.</p>
    """,
    "ebeling_hermes": """
        <p>Florian Ebeling's <i>The Secret History of Hermes Trismegistus</i> (2007) provides a concise and brilliant overview of the reception of Hermes from Antiquity to the present day, with a particular focus on the shifting 'image' of Hermes in the Enlightenment and beyond.</p>
    """
}

def enrich():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for slug, summary in SCHOLARSHIP_SUMMARIES.items():
        cursor.execute("UPDATE texts SET analysis_html = ? WHERE text_id = ?", (summary, slug))

    conn.commit()
    conn.close()
    print("Scholarship text summaries enriched.")

if __name__ == "__main__":
    enrich()
