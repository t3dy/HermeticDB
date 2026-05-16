import sqlite3
from pathlib import Path

DB_PATH = Path(r"c:\Dev\EmeraldTablet\db\emerald_tablet.db")

TECHNICAL_SUMMARIES = {
    "liber_hermetis": """
        <p>The <i>Liber Hermetis</i> (The Book of Hermes) is one of the most important compendiums of Hermetic astrology. It is preserved in a 5th-century Latin translation of a much older Greek original, possibly dating back to the late Hellenistic period.</p>
        <ul>
            <li><b>The 36 Decans:</b> The text provides a detailed description of the 36 decans (ten-degree segments of the zodiac), each associated with a specific deity, physical appearance, and influence over human health and destiny.</li>
            <li><b>Individual Degrees:</b> It includes rare material on the 'monomoiria' (individual degrees of the zodiac) and their specific properties.</li>
            <li><b>Synthesis:</b> The <i>Liber Hermetis</i> represents the peak of 'technical' Hermeticism, where the philosophical concept of <i>Heimarmene</i> (Fate) is applied with mathematical precision to the lives of individuals.</li>
        </ul>
    """,
    "liber_beibeniis": """
        <p>The <i>Liber de stellis beibeniis</i> (The Book of the Fixed Stars) is a foundational text on the influence of the 'beibenia'—a specific set of powerful fixed stars (such as Regulus, Sirius, and Algol) used in Hermetic astrology.</p>
        <p><b>Core Doctrine:</b> Unlike the wandering planets, the beibenia are considered 'fixed' and represent the highest, most stable tier of astral influence. The text describes how to calculate their positions and their impact on the character and longevity of the native, often viewing them as indicators of exceptional or divine destiny.</p>
    """,
    "iatromathematica": """
        <p>Iatromathematica (Medical Astrology) is the Hermetic science of applying astrological principles to the diagnosis and treatment of diseases. It is based on the doctrine of <b>Melothesia</b>—the correspondence between the signs of the zodiac/planets and the various parts and organs of the human body.</p>
        <p><b>Practice:</b> An iatromathematician would cast a horoscope for the 'decumbiture' (the moment the patient fell ill) to determine the celestial cause of the ailment and then prescribe remedies (herbs, stones, talismans) that possessed the 'sympathetic' qualities needed to restore balance.</p>
    """,
    "kyranides": """
        <p>The <i>Cyranides</i> (or <i>Kyranides</i>) is a massive encyclopedia of natural magic and universal sympathy. It is structured around the 'four categories'—plants, stones, birds, and fish—that correspond to the letters of the alphabet.</p>
        <p><b>Magical Technology:</b> The text provides thousands of recipes for amulets and physical cures based on the principle that every animal, plant, and mineral possesses a specific 'occult virtue' (dynamis). It represents the 'practical' side of Hermeticism, where the practitioner manipulates the physical world through a deep understanding of its hidden spiritual links.</p>
    """,
    "decans": """
        <p>The Decans are 36 groups of stars (asterisms) used in Egyptian and Hermetic astrology to divide the 360 degrees of the zodiac into ten-degree segments. In Hermeticism, the Decans are viewed as powerful 'governors' or 'daimons' who execute the <i>Heimarmene</i> (Fate) upon the material world.</p>
        <p><b>Significance:</b> Each decan has a specific name, appearance, and power. They are central to both technical astrology (for predicting events) and theurgic magic (for creating talismans to mitigate their influence). The <i>Salmeschoiniaka</i> is one of the primary sources for the earliest Hermetic decanic lore.</p>
    """,
    "melothesia": """
        <p>Melothesia is the Hermetic doctrine of astrological anatomy, which maps the signs of the zodiac and the seven planets onto the human body. (e.g., Aries governs the head, Leo the heart, Pisces the feet).</p>
        <p><b>Theory:</b> This system reinforces the 'As Above, So Below' principle, viewing the human body as a 'microcosm' that reflects the 'macrocosm' of the heavens. In iatromathematica, melothesia is used to determine which celestial force is causing a specific physical affliction.</p>
    """,
    "nechepso_petosiris": """
        <p>Nechepso (the King) and Petosiris (the Priest) are the legendary semi-mythical founders of Greco-Egyptian astrology. In Hermetic tradition, they are said to have received the secrets of the stars directly from Hermes Trismegistus.</p>
        <p><b>Influence:</b> The works attributed to them (the <i>Nechepso-Petosiris Corpus</i>) were the primary sources for Hellenistic astrology. They are cited by almost every major astrologer of antiquity as the ultimate authorities on the calculation of horoscopes and the interpretation of omens.</p>
    """
}

def populate():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for slug, html in TECHNICAL_SUMMARIES.items():
        cursor.execute("SELECT 1 FROM concepts WHERE slug = ?", (slug,))
        if cursor.fetchone():
            cursor.execute("UPDATE concepts SET definition_long = ? WHERE slug = ?", (html, slug))
        else:
            cursor.execute("UPDATE texts SET analysis_html = ? WHERE text_id = ?", (html, slug))
            cursor.execute("UPDATE persons SET bio_html = ? WHERE person_id = ?", (html, slug))

    conn.commit()
    conn.close()
    print("Technical Hermetica extensive population complete.")

if __name__ == "__main__":
    populate()
