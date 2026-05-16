import sqlite3
from pathlib import Path

DB_PATH = Path(r"c:\Dev\EmeraldTablet\db\emerald_tablet.db")

TREATISE_DATA = {
    "ch_i": {
        "summary": """
            <p>The <i>Poimandres</i> is the most famous treatise of the Corpus Hermeticum, providing a cosmogonic revelation from the 'Mind of Absolute Power' (Poimandres) to Hermes. It describes the creation of the world from Light and Darkness, the fall of the Primal Man (Anthropos) into Nature, and the subsequent ascent of the soul through the seven planetary spheres to return to the Father.</p>
            <h3>Key Scholarly Note</h3>
            <p>Fowden emphasizes that the <i>Poimandres</i> reflects a fusion of Platonic, Stoic, and Jewish ideas with a distinctively Egyptian priestly perspective on the 'Nous'.</p>
        """,
        "themes": ["nous", "ascent", "emanations", "anthropos"]
    },
    "ch_xiii": {
        "summary": """
            <p>CH XIII is a secret discourse on the mountain where Hermes instructs Tat in the mystery of rebirth (<i>palingenesia</i>). It is a highly ritualized dialogue where Hermes reveals that the 'Self' is born of God's will and that the physical body is a prison of the twelve 'punishments' (vices) which must be driven out by the ten 'powers' (virtues).</p>
        """,
        "themes": ["regeneration", "theurgy", "palingenesia", "deification"]
    },
    "asclepius": {
        "summary": """
            <p>Preserved in Latin, the <i>Asclepius</i> (or <i>Perfect Sermon</i>) is a vast dialogue discussing the hierarchy of gods, the nature of man as the 'third god', and the controversial practice of 'god-making' (drawing spirits into statues). It contains a famous 'Lament' for the future of Egypt, prophesying the departure of the gods.</p>
        """,
        "themes": ["egypt", "god_making", "pneuma", "prophecy"]
    },
    "emerald_tablet": {
        "summary": """
            <p>The <i>Tabula Smaragdina</i> is the quintessential alchemical text. Its cryptic thirteen sentences contain the core principle of Hermetic science: 'That which is below is as that which is above.' It describes the operation of the 'Sun' and 'Moon' and the creation of the 'One Thing' (the Stone) that can penetrate every solid thing.</p>
        """,
        "themes": ["correspondence", "alchemy", "chrysopoeia", "prima_materia"]
    },
    "picatrix": {
        "summary": """
            <p>The <i>Picatrix</i> (Ghayat al-Hakim) is a massive Arabic manual of astral magic and talismans. It justifies magical operations through the Hermetic theory of <i>sympatheia</i>, arguing that the mage can channel celestial influences by aligning terrestrial materials with planetary archetypes.</p>
        """,
        "themes": ["astral_magic", "sympatheia", "talismans"]
    }
}

def enrich():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for slug, data in TREATISE_DATA.items():
        # Update Summary
        cursor.execute("UPDATE texts SET analysis_html = ? WHERE text_id = ?", (data["summary"], slug))
        
        # Get Text ID
        text_id_row = cursor.execute("SELECT id FROM texts WHERE text_id = ?", (slug,)).fetchone()
        if not text_id_row: continue
        tid = text_id_row[0]

        # Link Themes
        for theme_slug in data["themes"]:
            # Ensure concept exists (basic entry)
            cursor.execute("""
                INSERT OR IGNORE INTO concepts (slug, label, source_method)
                VALUES (?, ?, 'AUTO_ENRICH')
            """, (theme_slug, theme_slug.replace("_", " ").title()))
            
            concept_id_row = cursor.execute("SELECT id FROM concepts WHERE slug = ?", (theme_slug,)).fetchone()
            if concept_id_row:
                cid = concept_id_row[0]
                cursor.execute("""
                    INSERT OR IGNORE INTO concept_text_refs (concept_id, text_id)
                    VALUES (?, ?)
                """, (cid, tid))

    conn.commit()
    conn.close()
    print("Treatise enrichment complete.")

if __name__ == "__main__":
    enrich()
