import sqlite3
from pathlib import Path

DB_PATH = Path(r"c:\Dev\EmeraldTablet\db\emerald_tablet.db")

SCHOLAR_EXTENSIONS = {
    "frances_yates": """
        <p>Frances Amelia Yates (1899–1981) was one of the most influential historians of the 20th century. Her work at the Warburg Institute transformed the study of Renaissance intellectual history by highlighting the central role of the Hermetic tradition.</p>
        <p><b>Major Works:</b> In <i>Giordano Bruno and the Hermetic Tradition</i> (1964), Yates argued that Bruno was not a 'martyr for science' in the modern sense, but a 'Hermetic Magus' whose sun-centered cosmology was deeply rooted in the <i>Corpus Hermeticum</i>. Her other works, such as <i>The Rosicrucian Enlightenment</i> and <i>The Art of Memory</i>, further explored the intersections of magic, science, and politics.</p>
        <p><b>The Yates Paradigm:</b> Her thesis that magic was a necessary precursor to the Scientific Revolution sparked decades of debate. While modern scholarship has refined her views on 'tradition' and 'continuity,' she remains the foundational figure for the scholarly recovery of Hermeticism.</p>
    """,
    "wouter_hanegraaff": """
        <p>Wouter J. Hanegraaff is a Professor of History of Hermetic Philosophy and Related Currents at the University of Amsterdam. He has been instrumental in establishing Western Esotericism as a legitimate and rigorous academic field.</p>
        <p><b>Core Methodology:</b> Hanegraaff advocates for a 'discursive' approach that avoids the pitfalls of 'perennialism' (viewing all traditions as one) and 'religionism.' His monumental <i>Dictionary of Gnosis and Western Esotericism</i> (2005) established the standard reference for the field.</p>
        <p><b>Key Concept:</b> He coined the term 'Rejected Knowledge' to describe how the Enlightenment excluded esoteric traditions from the mainstream of Western culture, creating the 'Grand Narrative' of modern rationality by casting its shadow elsewhere.</p>
    """,
    "garth_fowden": """
        <p>Garth Fowden is a historian of Late Antiquity whose work has shifted the center of Hermetic studies back to its Egyptian origins. In his seminal book, <i>The Egyptian Hermes: A Historical Approach to the Late Pagan Mind</i> (1986), he rejected the purely 'Greek' philological reading of the texts.</p>
        <p><b>Historical Contextualization:</b> Fowden argued that the Hermetica must be understood within the social and religious world of Roman Egypt. He demonstrated that the 'philosophical' and 'technical' Hermetica (alchemy, astrology) were not separate traditions but were practiced by the same 'Hermetic circles'—small groups of seekers led by a master.</p>
    """
}

def populate():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for slug, html in SCHOLAR_EXTENSIONS.items():
        cursor.execute("UPDATE persons SET bio_html = ? WHERE person_id = ?", (html, slug))

    conn.commit()
    conn.close()
    print("Scholar extensive expansion complete.")

if __name__ == "__main__":
    populate()
