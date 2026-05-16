import sqlite3
from pathlib import Path

DB_PATH = Path(r"c:\Dev\EmeraldTablet\db\emerald_tablet.db")

EXTENSIVE_SUMMARIES = {
    "ch_i": """
        <p>The <i>Poimandres</i> is the foundational vision of the Hermetic corpus. It describes the encounter between Hermes and Poimandres, the 'Mind of Absolute Sovereignty' (Nous). The text unfolds in several critical phases:</p>
        <ul>
            <li><b>The Vision of Light and Darkness:</b> Hermes witnesses the emergence of the cosmos from a watery substance, preceded by a holy Word (Logos).</li>
            <li><b>The Creation of the Demiurge:</b> Nous creates a second Mind, the Demiurge, who fashions the seven governors (planetary spheres) to encompass the sensible world.</li>
            <li><b>The Fall of the Anthropos:</b> The primordial Human (Anthropos), desiring to create, breaks through the spheres and falls into Nature, resulting in the dual nature of humanity (mortal body, immortal soul).</li>
            <li><b>The Way of Ascent:</b> The soul's journey after death involves shedding the 'garments' of the planetary influences at each sphere to reach the Ogdoad and final union with God.</li>
        </ul>
    """,
    "asclepius": """
        <p>The <i>Asclepius</i> (or <i>The Perfect Discourse</i>) is the longest and most complex text in the Latin Hermetica. It is famous for several distinct themes:</p>
        <ul>
            <li><b>Man as the Third God:</b> The text defines humanity as a 'great miracle,' a being capable of mediating between the divine and the material.</li>
            <li><b>Theurgy and God-Making:</b> A controversial section describes the ritual animation of statues, where divine powers are 'drawn down' into material forms.</li>
            <li><b>The Lament:</b> A prophetic passage describing the future decline of Egypt, the departure of the gods, and the eventual restoration of the cosmos by God.</li>
        </ul>
    """,
    "emerald_tablet": """
        <p>The <i>Tabula Smaragdina</i> is the most famous text in the history of alchemy. Attributed to Hermes Trismegistus, it provides the cryptic formula for the creation of the Philosopher's Stone.</p>
        <p><b>Key Doctrine:</b> The tablet establishes the principle of <i>Sympatheia</i> with its opening lines: 'That which is below is like that which is above.' It describes the 'Operation of the Sun' and the separation of the subtle from the gross. Its transmission from Arabic sources (the <i>Sirr al-Khaliqa</i>) into Medieval Latin fundamentally shaped Western occult science.</p>
    """,
    "zosimos_of_panopolis": """
        <p>Zosimos of Panopolis (fl. 300 CE) is the first historical alchemist whose writings have survived. A Hermeticist and a Gnostic, his work blends laboratory practice with profound spiritual allegory.</p>
        <p><b>The Visions:</b> Zosimos is famous for his recorded dreams, such as the vision of the 'Altar' and the 'Priest of the Sanctuary,' which describe alchemical processes as the dismemberment and spiritualization of the body. He emphasizes the 'Inner Man' and the need for the alchemist to be free from material attachments.</p>
    """,
    "marsilio_ficino": """
        <p>Marsilio Ficino (1433–1499) was the architect of the Renaissance Hermetic revival. Commissioned by Cosimo de' Medici to translate the <i>Corpus Hermeticum</i> before the works of Plato, Ficino introduced Hermes to the Latin West as a contemporary of Moses and the founder of the <i>Prisca Theologia</i>.</p>
        <p><b>Contributions:</b> Ficino's Latin translation (the <i>Pimander</i>, 1471) became an instant bestseller, shaping the thought of Pico della Mirandola, Agrippa, and Bruno. His work attempted to harmonize Hermeticism with Christian theology, viewing Hermes as a prophet of the Trinity.</p>
    """
}

def populate():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for slug, html in EXTENSIVE_SUMMARIES.items():
        # Update texts
        cursor.execute("UPDATE texts SET analysis_html = ? WHERE text_id = ?", (html, slug))
        # Update persons
        cursor.execute("UPDATE persons SET bio_html = ? WHERE person_id = ?", (html, slug))

    conn.commit()
    conn.close()
    print("Extensive summaries wave 1 complete.")

if __name__ == "__main__":
    populate()
