import sqlite3
from pathlib import Path

DB_PATH = Path(r"c:\Dev\EmeraldTablet\db\emerald_tablet.db")

SCHOLARSHIP_ENTRIES = {
    "lodovico_lazzarelli": """
        <p>Lodovico Lazzarelli (1447–1500) was a pivotal figure in the Renaissance Hermetic revival, representing a more 'experiential' and initiatory strand of Hermeticism than the purely philosophical approach of Marsilio Ficino. A poet and scholar, Lazzarelli believed that the Hermetic texts were not just ancient wisdom but a guide to a radical spiritual transformation.</p>
        <ul>
            <li><b>Works:</b> His most famous work, the <i>Crater Hermetis</i> (The Mixing-Bowl of Hermes), describes a dialogue between himself and King Ferdinand of Naples, where he explains the process of spiritual generation and the creation of the 'divine man.'</li>
            <li><b>Translations:</b> He translated the final treatises of the <i>Corpus Hermeticum</i> (CH XVI–XVIII), which he titled the <i>Diffinitiones Asclepii</i>. These were published posthumously in 1507 by Symphorien Champier.</li>
            <li><b>Influence:</b> Lazzarelli was a direct influence on the young Cornelius Agrippa, and his focus on 'rebirth' (palingenesia) through the indwelling of the divine Mind (Nous) remains a cornerstone of the Lazzarellian Hermetic tradition.</li>
        </ul>
    """,
    "pietro_pomponazzi": """
        <p>Pietro Pomponazzi (1462–1525) was a leading Aristotelian philosopher of the Renaissance whose work, <i>De incantationibus</i> (On Incantations, 1520), offered a radical naturalistic challenge to the belief in demons and miracles.</p>
        <ul>
            <li><b>Stellar Determinism:</b> Pomponazzi argued that all 'miraculous' events, including the myths of Circe and magical transformations, were not the work of demons but the result of the necessary and impersonal movements of the celestial bodies (the stars).</li>
            <li><b>Materialism:</b> Following his controversial <i>De immortalitate animae</i>, he viewed the human soul as a <i>forma materialis</i>, entirely subject to the laws of nature and stellar causality.</li>
            <li><b>Natural Magic:</b> He redefined magic as a legitimate 'technical' science based on the manipulation of <i>virtus loci</i> (the power of place) and the hidden sympathetic links within the cosmos, effectively 'disenchanting' the supernatural into the natural.</li>
        </ul>
    """,
    "symphorien_champier": """
        <p>Symphorien Champier (1471–1539) was a French physician and humanist who played a crucial role in the dissemination of Hermeticism in France. He was a student of Lefèvre d'Étaples and a bridge between the Italian Renaissance and Northern humanism.</p>
        <p><b>Publication of Lazzarelli:</b> Champier is primarily known in Hermetic history for publishing Lodovico Lazzarelli's <i>Diffinitiones Asclepii</i> in 1507. Although he was sometimes critical of the more 'magical' aspects of the tradition, his works attempted to harmonize the 'Ancient Theology' of Hermes with Christian doctrine and Galenic medicine.</p>
    """,
    "ochema": """
        <p>The <i>Ochēma-Pneuma</i> (Spirit-Vehicle) is a central concept in Neoplatonic and Hermetic psychology. It is the 'fine' or 'subtle' body that serves as the intermediary between the immaterial soul and the physical body.</p>
        <p><b>Function in Theurgy:</b> In theurgical practice, the <i>ochēma</i> is the part of the human constitution that is 'illuminated' by the divine <i>pneuma</i>. Through ritual and 'inhaling' the rays of the sun/divinity, the vehicle is purified and made radiant, allowing the soul to ascend through the planetary spheres to union with the divine.</p>
    """,
    "phantasmata": """
        <p><i>Phantasmata</i> refers to the stream of mental images, emotional projections, and sensory 'shadows' that fill the human mind. In the analytical framework of Wouter Hanegraaff (2022), the 'Way of Hermes' is understood as a training regime designed to control and move beyond these hallucinatory veils.</p>
        <p><b>Spiritual Significance:</b> Hermeticism teaches that the ordinary human state is one of 'drunkenness' or 'sleep' caused by the unruly <i>phantasmata</i> of the material world. Gnosis involves the radical alteration of consciousness required to 'see through' these phantoms and perceive the true, luminous nature of reality.</p>
    """,
    "virtus_loci": """
        <p><i>Virtus Loci</i> (Power of Place) is a concept in natural magic and astrology, prominently discussed by Pietro Pomponazzi. It refers to the idea that specific geographic locations possess unique qualities or 'virtues' determined by their relationship to the celestial spheres.</p>
        <p><b>Magical Application:</b> The <i>virtus loci</i> explains why certain rituals or natural phenomena (like the transformations associated with Circe) only occur in specific places. It is a key element of the 'technical' Hermetica, where the practitioner must match the time (astrology) with the place (geography) to achieve a desired effect.</p>
    """
}

def populate():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for slug, html in SCHOLARSHIP_ENTRIES.items():
        # Check concepts
        cursor.execute("SELECT 1 FROM concepts WHERE slug = ?", (slug,))
        if cursor.fetchone():
            cursor.execute("UPDATE concepts SET definition_long = ? WHERE slug = ?", (html, slug))
        else:
            # Check persons
            cursor.execute("SELECT 1 FROM persons WHERE person_id = ?", (slug,))
            if cursor.fetchone():
                cursor.execute("UPDATE persons SET bio_html = ? WHERE person_id = ?", (html, slug))
            else:
                # Add if missing? No, user wants population of *existing* or *listed* figures.
                # I'll check if they exist first.
                cursor.execute("INSERT OR IGNORE INTO persons (person_id, name, bio_html) VALUES (?, ?, ?)", 
                             (slug, slug.replace('_', ' ').title(), html))
                cursor.execute("INSERT OR IGNORE INTO concepts (slug, label, definition_long) VALUES (?, ?, ?)", 
                             (slug, slug.replace('_', ' ').title(), html))

    conn.commit()
    conn.close()
    print("Scholarship-driven extensive population complete.")

if __name__ == "__main__":
    populate()
