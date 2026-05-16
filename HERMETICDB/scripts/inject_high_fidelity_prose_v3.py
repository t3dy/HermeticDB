import sqlite3
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR.parent / "db" / "emerald_tablet.db"

SCHOLARLY_PROSE_V3 = {
    "wouter_hanegraaff": """
        <p>Wouter J. Hanegraaff (b. 1961) is the quintessential figure in the professionalization of the study of Western Esotericism. As the Professor of History of Hermetic Philosophy and Related Currents at the University of Amsterdam, he transformed what was once a marginalized "occult" topic into a rigorous, mainstream academic discipline.</p>
        <h2>Scholarly Significance</h2>
        <p>Hanegraaff’s seminal work, <i>Esotericism and the Academy: Rejected Knowledge in Western Culture</i>, argues that Western identity is defined by what it has excluded as "superstition" or "irrationality." He posits that Hermeticism, alchemy, and magic constitute a "third pillar" of Western intellectual history, alongside reason and faith. His approach—empirically grounded and phenomenologically sensitive—has established the standard for modern Hermetic studies.</p>
        <h2>Theoretical Contributions</h2>
        <p>He is responsible for the influential concept of "rejected knowledge" and has extensively explored the transitions between "Enlightenment" rationality and "Enchanted" worldviews. His work challenges the secularization thesis, showing how Hermetic themes persisted and evolved within the modern and postmodern landscape.</p>
    """,
    "brian_copenhaver": """
        <p>Brian P. Copenhaver is a distinguished professor of Philosophy and History at UCLA and one of the preeminent translators of Hermetic and magical texts. His 1992 translation of the <i>Hermetica</i> (the <i>Corpus Hermeticum</i> and the <i>Asclepius</i>) remains the definitive English scholarly edition, bridging the gap between historical philology and philosophical analysis.</p>
        <h2>Scholarly Significance</h2>
        <p>Copenhaver’s work is characterized by an uncompromising commitment to historical accuracy and linguistic precision. Beyond translation, his research into Renaissance "natural magic" and its relationship to the Scientific Revolution (particularly in the works of Newton and Boyle) has provided a nuanced view of how "mantic" and "scientific" interests were often inextricably linked in the early modern mind.</p>
        <h2>Major Works</h2>
        <p>In addition to his translation of the <i>Hermetica</i>, his work on <i>The Book of Magic</i> and various studies on Italian Renaissance Platonism have provided a robust framework for understanding the transmission of "prisca theologia" through the European intellectual elite.</p>
    """,
    "corpus_hermeticum": """
        <p>The <i>Corpus Hermeticum</i> is the foundational collection of seventeen Greek treatises attributed to Hermes Trismegistus, dating from the 1st to the 3rd centuries CE. These texts—notably the <i>Poimandres</i>—contain the core philosophical and theological revelations of the "Way of Hermes," focusing on the nature of the divine, the structure of the cosmos, and the path to human salvation through Gnosis.</p>
        <h2>Historical Context</h2>
        <p>Emerging from the syncretism of Roman Egypt, the treatises reflect a unique fusion of Middle Platonism, Stoicism, and traditional Egyptian theology. They were preserved in the Byzantine world and famously rediscovered and translated by Marsilio Ficino in the 15th century, sparking the Renaissance Hermetic revival.</p>
        <h2>Scholarly Significance</h2>
        <p>Modern scholars analyze the <i>Corpus</i> as representing a shift from ritual practice to "philosophical religion." The texts address the fundamental Hermetic dilemma: how a "divine" human soul can exist within a material world. The <i>Corpus</i> provides the theoretical grammar for all subsequent Western Hermeticism, from medieval alchemy to modern occultism.</p>
    """,
    "picatrix": """
        <p>The <i>Picatrix</i>, the latinized name for the 10th-century Arabic grimoire <i>Ghāyat al-Ḥakīm</i> (The Goal of the Wise), is the most influential manual of astral magic in world history. It provides a massive synthesis of Hermetic philosophy, Neoplatonic cosmology, and practical instructions for capturing celestial influences through talismans and ritual timing.</p>
        <h2>Historical Context</h2>
        <p>Likely composed in Al-Andalus (Muslim Spain) and attributed to the scholar al-Masriti, it was translated into Spanish and Latin at the court of Alfonso X in the 13th century. It served as a vital "technical" companion to the more philosophical <i>Corpus Hermeticum</i>, providing the actual methods for the "Natural Magic" that Renaissance magi like Agrippa and Ficino discussed in theory.</p>
        <h2>Scholarly Significance</h2>
        <p>David Pingree and later scholars have identified the <i>Picatrix</i> as a crucial vehicle for the transmission of "Sabaean" and Hermetic star-lore into the Latin West. It represents the "High Magic" tradition, where the practitioner acts as a co-creator with the heavens, utilizing the correspondences between the stars (Macrocosm) and earthly symbols (Microcosm).</p>
    """
}

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for eid, prose in SCHOLARLY_PROSE_V3.items():
        # Check if it's a person
        cursor.execute("SELECT name FROM persons WHERE person_id = ?", (eid,))
        if cursor.fetchone():
            print(f"Injecting scholarly bio for {eid}...")
            cursor.execute("UPDATE persons SET bio_html = ? WHERE person_id = ?", (prose, eid))
        else:
            # Check if it's a text
            cursor.execute("SELECT title FROM texts WHERE text_id = ?", (eid,))
            if cursor.fetchone():
                print(f"Injecting scholarly analysis for {eid}...")
                cursor.execute("UPDATE texts SET analysis_html = ? WHERE text_id = ?", (prose, eid))
    
    conn.commit()
    conn.close()
    print("Payload injection Volume 3 complete.")

if __name__ == "__main__":
    main()
