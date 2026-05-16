import sqlite3
from pathlib import Path

DB_PATH = Path(r"c:\Dev\EmeraldTablet\db\emerald_tablet.db")

EXTENSIVE_SUMMARIES_4 = {
    "thoth": """
        <p>Thoth (Djehuty) is the ancient Egyptian god of wisdom, writing, and the moon, who serves as the divine archetype for the later figure of Hermes Trismegistus. In Egyptian mythology, Thoth is the 'scribe of the gods' and the measurer of time and the cosmos.</p>
        <p><b>Role in Hermeticism:</b> The transition from the Egyptian Thoth to the Greek Hermes occurred in the Ptolemaic period, where Thoth's attributes as the author of all knowledge were synthesized with Hermes's role as the messenger of the gods. Hermetic texts often refer to Thoth as the teacher who inscribed his wisdom on stelae before the Flood.</p>
    """,
    "sh_fragments": """
        <p>The <i>Stobaean Fragments</i> (Anthologium of John Stobaeus, 5th century CE) preserve over 40 distinct fragments of otherwise lost Hermetic dialogues. These fragments are essential for understanding the full scope of the 'philosophical' Hermetica beyond the 17 treatises of the Greek Corpus.</p>
        <ul>
            <li><b>Key Teachings:</b> The fragments contain profound discourses on the nature of the soul, the hierarchy of the cosmos, the role of fate (Heimarmene), and the relationship between the creator and the creation.</li>
            <li><b>Kore Kosmou:</b> The most famous fragment in this collection is the <i>Kore Kosmou</i> (Virgin of the World), a long cosmological myth describing the creation of souls and the mission of Isis and Osiris to bring culture and law to humanity.</li>
        </ul>
    """,
    "nag_hammadi_hermetica": """
        <p>The discovery of the Nag Hammadi Library in 1945 included several previously unknown Hermetic texts in Coptic translation (Codex VI). These 'Gnostic Hermetica' provide rare evidence for the ritual and initiatory life of Hermetic communities in Roman Egypt.</p>
        <ul>
            <li><b>The Discourse on the Eighth and Ninth:</b> A vivid description of a ritual initiation where a master leads a student from the planetary spheres (the seven) to the Ogdoad (the eighth) and Ennead (the ninth).</li>
            <li><b>The Prayer of Thanksgiving:</b> A beautiful communal prayer that emphasizes the practitioner's gratitude for the 'light of Gnosis'.</li>
        </ul>
    """,
    "palingenesia": """
        <p><i>Palingenesia</i> (Rebirth or Regeneration) is a central concept in the initiatory Hermetica, specifically in <i>CH XIII</i>. It describes the ontological transformation of the practitioner, where the material self is 'dissolved' and the divine self is 'born' through the indwelling of the divine powers.</p>
        <p><b>Metaphysical Meaning:</b> This is not a metaphor for moral improvement, but a literal change in being. The 'reborn' practitioner no longer perceives with the physical eyes but with the Mind (Nous), seeing the cosmos as it truly is—a manifestation of God.</p>
    """
}

def populate():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for slug, html in EXTENSIVE_SUMMARIES_4.items():
        cursor.execute("SELECT 1 FROM concepts WHERE slug = ?", (slug,))
        if cursor.fetchone():
            cursor.execute("UPDATE concepts SET definition_long = ? WHERE slug = ?", (html, slug))
        else:
            cursor.execute("UPDATE texts SET analysis_html = ? WHERE text_id = ?", (html, slug))
            cursor.execute("UPDATE persons SET bio_html = ? WHERE person_id = ?", (html, slug))

    conn.commit()
    conn.close()
    print("Extensive summaries wave 4 complete.")

if __name__ == "__main__":
    populate()
