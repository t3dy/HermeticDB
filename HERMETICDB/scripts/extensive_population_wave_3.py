import sqlite3
from pathlib import Path

DB_PATH = Path(r"c:\Dev\EmeraldTablet\db\emerald_tablet.db")

EXTENSIVE_SUMMARIES_3 = {
    "jabir_ibn_hayyan": """
        <p>Jabir ibn Hayyan (fl. 8th-9th century), known in Latin as Geber, is the most celebrated alchemist of the Islamic world. The vast 'Jabirian Corpus' (which includes hundreds of treatises) is the primary vehicle through which Hermetic alchemical theory was preserved and expanded in the Middle Ages.</p>
        <ul>
            <li><b>The Science of Balance (Mizan):</b> Jabir's central philosophical contribution was the idea that all material substances are composed of four qualities (Hot, Cold, Dry, Moist) and that the alchemist's goal is to find the perfect numerical balance between them.</li>
            <li><b>Sulfur-Mercury Theory:</b> He formalized the theory that all metals are composed of varying proportions of sulfur and mercury, a doctrine that dominated European alchemy for centuries.</li>
            <li><b>Hermetic Lineage:</b> Jabir explicitly identified himself as a student of the Imam Ja'far al-Sadiq and a follower of the 'Master' Hermes, whom he viewed as the source of all scientific and spiritual knowledge.</li>
        </ul>
    """,
    "sirr_al_khaliqa": """
        <p>The <i>Sirr al-Khaliqa</i> (The Secret of Creation), also known as the <i>Kitab al-Ilal</i> (The Book of Causes), is an Arabic Hermetic encyclopedia attributed to Balinas (Apollonius of Tyana). It is the earliest known source to preserve the full text of the <b>Emerald Tablet</b>.</p>
        <p><b>Content and Scope:</b> The text provides a comprehensive cosmology and mineralogy, explaining the emergence of the cosmos from the elements. It frames the Emerald Tablet as a revelation discovered by Balinas in a hidden chamber beneath a statue of Hermes in Tyana. The work served as a bridge between Late Antique Neopythagoreanism and the developing Islamic occult sciences.</p>
    """,
    "sabians_harran": """
        <p>The Sabians of Harran were a community of pagans in Upper Mesopotamia who, when challenged by the Caliph al-Ma'mun in 830 CE, identified themselves as 'Sabians' (a group mentioned in the Quran) to achieve legal protection. They claimed Hermes Trismegistus (whom they identified with the prophet Idris) as their prophet and the <i>Corpus Hermeticum</i> as their scripture.</p>
        <p><b>Significance:</b> The Sabians were the primary guardians of Hermetic, Neoplatonic, and scientific lore in the early Islamic world. Scholars like Thabit ibn Qurra brought this knowledge to Baghdad, where it fueled the Abbasid translation movement and the development of Arabic alchemy and astrology.</p>
    """,
    "mizan": """
        <p>The <i>Mizan</i> (Balance) is the core philosophical concept of the Jabirian alchemical system. It holds that the physical world is governed by a numerical and qualitative harmony that can be understood and manipulated by the alchemist.</p>
        <p><b>Theory:</b> Every substance is seen as a combination of four 'natures' (Heat, Cold, Dryness, Humidity), both external and internal. The 'Balance' involves adjusting these natures through laboratory processes to achieve the 'Elixir' or the perfection of the metal. It represents a profound Hermetic attempt to apply mathematical rigor to the mystical transformation of matter.</p>
    """
}

def populate():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for slug, html in EXTENSIVE_SUMMARIES_3.items():
        # Check if it's a concept or person/text
        cursor.execute("SELECT 1 FROM concepts WHERE slug = ?", (slug,))
        if cursor.fetchone():
            cursor.execute("UPDATE concepts SET definition_long = ? WHERE slug = ?", (html, slug))
        else:
            cursor.execute("UPDATE texts SET analysis_html = ? WHERE text_id = ?", (html, slug))
            cursor.execute("UPDATE persons SET bio_html = ? WHERE person_id = ?", (html, slug))

    conn.commit()
    conn.close()
    print("Extensive summaries wave 3 complete.")

if __name__ == "__main__":
    populate()
