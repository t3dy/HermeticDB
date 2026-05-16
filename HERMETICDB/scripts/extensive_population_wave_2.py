import sqlite3
from pathlib import Path

DB_PATH = Path(r"c:\Dev\EmeraldTablet\db\emerald_tablet.db")

EXTENSIVE_SUMMARIES_2 = {
    "ch_xiii": """
        <p>CH XIII, <i>On Rebirth and the Promise of Silence</i>, is one of the most significant initiatory discourses in the <i>Corpus Hermeticum</i>. It describes a secret conversation between Hermes and his son Tat on the mountain.</p>
        <ul>
            <li><b>The Necessity of Rebirth:</b> Hermes explains that the 'Inner Man' must be reborn to see the divine world. This is not a physical birth, but a spiritual transformation through the descent of the divine powers.</li>
            <li><b>The Twelve Torments:</b> Hermes identifies twelve 'torments' (negative emotional and physical states) that must be cast out by the ten divine 'powers' (such as Truth, Joy, and Temperance).</li>
            <li><b>The Hymn of Regeneration:</b> The discourse culminates in a silent hymn of praise to the 'All-One,' emphasizing the practitioner's union with the elements and the cosmos.</li>
        </ul>
    """,
    "picatrix": """
        <p>The <i>Ghayat al-Hakim</i> (The Goal of the Wise), known in Latin as the <i>Picatrix</i>, is the most important textbook of astral magic from the Medieval period. Attributed to Maslama al-Majriti (Pseudo), it synthesizes Hermetic, Sabian, and Aristotelian lore into a practical manual.</p>
        <ul>
            <li><b>Book I & II:</b> Establish the philosophical foundations of magic, focusing on the nature of the heavens, the planetary decans, and the concept of <i>Sympatheia</i>.</li>
            <li><b>Book III & IV:</b> Provide detailed recipes for talismans, fumigations, and rituals designed to capture the influences of specific planetary configurations for various purposes.</li>
        </ul>
        <p><b>Transmission:</b> Translated from Arabic into Spanish and then into Latin at the court of Alfonso the Wise in the 13th century, it became the 'forbidden' bible of Renaissance mages like Agrippa and Bruno.</p>
    """,
    "monas_hieroglyphica": """
        <p>The <i>Monas Hieroglyphica</i> (1564) is the magnum opus of the Elizabethan polymath John Dee. It is a dense, mathematical, and Hermetic exposition of a single complex symbol—the 'Hieroglyphic Monad'.</p>
        <p><b>Symbolic Anatomy:</b> Dee explains how the symbol contains the Moon, the Sun, the Cross (representing the elements), and the sign of Aries (representing fire and transformation). He argues that understanding the Monad allows the practitioner to understand the unity of all creation and the mathematical laws governing the cosmos.</p>
    """,
    "pico_della_mirandola": """
        <p>Giovanni Pico della Mirandola (1463–1494) was the first major figure to synthesize Hermeticism with the Hebrew Kabbalah. A brilliant polymath and student of Ficino, his 'Oration on the Dignity of Man' is the definitive manifesto of the Renaissance world-view.</p>
        <p><b>Christian Kabbalah:</b> Pico argued that Hermeticism and Kabbalah both provided ancient evidence for the truth of Christianity. His 900 Theses attempted to harmonize all philosophical and religious systems into a single 'New Universal Philosophy'.</p>
    """,
    "cornelius_agrippa": """
        <p>Heinrich Cornelius Agrippa (1486–1535) was the preeminent synthesizer of Renaissance occult philosophy. His three-volume <i>De Occulta Philosophia Libri Tres</i> is the definitive encyclopedia of magic, alchemy, and Hermeticism.</p>
        <p><b>The Three Worlds:</b> Agrippa organized his work into three levels: Elementary (Natural Magic), Celestial (Mathematical/Astral Magic), and Intellectual (Ceremonial/Angelic Magic). He sought to prove that magic was a pious and noble pursuit that led the soul to God.</p>
    """
}

def populate():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for slug, html in EXTENSIVE_SUMMARIES_2.items():
        cursor.execute("UPDATE texts SET analysis_html = ? WHERE text_id = ?", (html, slug))
        cursor.execute("UPDATE persons SET bio_html = ? WHERE person_id = ?", (html, slug))

    conn.commit()
    conn.close()
    print("Extensive summaries wave 2 complete.")

if __name__ == "__main__":
    populate()
