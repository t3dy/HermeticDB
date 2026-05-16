import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR.parent / "db" / "emerald_tablet.db"

NEW_PERSONS = [
    ("tommaso_campanella", "Tommaso Campanella", "RENAISSANCE", "PHILOSOPHER", "Dominican friar and author of 'The City of the Sun', imprisoned for magic and heresy."),
    ("guillaume_postel", "Guillaume Postel", "RENAISSANCE", "SCHOLAR", "French linguist and Christian Kabbalist who translated the Zohar and Sefer Yetzirah."),
    ("francesco_patrizi", "Francesco Patrizi", "RENAISSANCE", "PHILOSOPHER", "Attempted to replace Aristotle with Hermes Trismegistus in Catholic university curricula."),
    ("arthur_versluis", "Arthur Versluis", "MODERN", "SCHOLAR", "Expert on Christian Theosophy and American Transcendental esotericism."),
    ("nicholas_goodrick_clarke", "Nicholas Goodrick-Clarke", "MODERN", "SCHOLAR", "Historian of modern occultism, Ariosophy, and Paracelsianism."),
    ("moshe_idel", "Moshe Idel", "MODERN", "SCHOLAR", "Preeminent scholar of Kabbalah, focusing on ecstatic and magical dimensions."),
    ("johann_valentin_andreae", "Johann Valentin Andreae", "EARLY_MODERN", "AUTHOR", "Lutheran theologian and putative author of the Rosicrucian manifestos."),
    ("robert_boyle", "Robert Boyle", "EARLY_MODERN", "SCHOLAR", "Pioneer of modern chemistry who simultaneously practiced highly secretive alchemy."),
    ("elias_ashmole", "Elias Ashmole", "EARLY_MODERN", "COMPILER", "English antiquary and author of the 'Theatrum Chemicum Britannicum'."),
    ("heinrich_cornelius_agrippa", "Heinrich Cornelius Agrippa", "RENAISSANCE", "PHILOSOPHER", "Author of the encyclopedic 'De Occulta Philosophia'.") # Just in case not present fully
]

NEW_TEXTS = [
    ("ch_x_the_key", "CH X: The Key", "GREEK", "PRIMARY_SOURCE", 100, 300, "Hermetic treatise summarizing the entire philosophy and mapping the descent of the soul.", "", "SEED_DATA", "REVIEWED", "HIGH"),
    ("kore_kosmou", "Kore Kosmou (Virgin of the World)", "GREEK", "PRIMARY_SOURCE", 100, 300, "Massive Stobaean fragment where Isis teaches Horus the secrets of cosmic animation.", "", "SEED_DATA", "REVIEWED", "HIGH"),
    ("turba_philosophorum", "Turba Philosophorum", "LATIN", "COMPILATION", 900, 1000, "The 'Assembly of the Philosophers', translating Arabic alchemy into a Greek philosophical framework.", "", "SEED_DATA", "REVIEWED", "HIGH"),
    ("chymical_wedding", "The Chymical Wedding of Christian Rosenkreutz", "GERMAN", "MANIFESTO", 1616, 1616, "The third Rosicrucian manifesto; an allegorical romance of spiritual alchemy.", "", "SEED_DATA", "REVIEWED", "HIGH"),
    ("sefer_yetzirah", "Sefer Yetzirah", "HEBREW", "PRIMARY_SOURCE", 200, 600, "The 'Book of Creation', foundational text of Jewish esotericism mapping creation via language.", "", "SEED_DATA", "REVIEWED", "HIGH"),
    ("city_of_the_sun", "The City of the Sun", "LATIN", "TREATISE", 1602, 1602, "Campanella's utopian vision of a society governed by astral magic and Hermetic priests.", "", "SEED_DATA", "REVIEWED", "HIGH"),
    ("de_occulta_philosophia_libri_tres", "De Occulta Philosophia Libri Tres", "LATIN", "TREATISE", 1533, 1533, "Agrippa's massive synthesis of natural, celestial, and ceremonial magic.", "", "SEED_DATA", "REVIEWED", "HIGH")
]

NEW_CONCEPTS = [
    ("macrocosm_microcosm", "Macrocosm and Microcosm", "COSMOLOGICAL", "The structural mirror between the universe (macro) and the human body (micro).", "ACTOR_TERM"),
    ("emanationism", "Emanationism", "COSMOLOGICAL", "The Neoplatonic model of creation overflowing from the One like light from the sun.", "ACTOR_TERM"),
    ("christian_kabbalah", "Christian Kabbalah", "THEOLOGICAL", "The Renaissance synthesis of Jewish mysticism to prove Christian dogma.", "ANALYST_TERM"),
    ("astral_magic", "Astral Magic", "PHILOSOPHICAL", "The practice of drawing down planetary forces into talismans or the human spiritus.", "ACTOR_TERM"),
    ("religionism", "Religionism", "HISTORIOGRAPHICAL", "The approach to studying esotericism that assumes the metaphysical truth of the traditions.", "ANALYST_TERM"),
    ("individuation", "Individuation", "PSYCHOLOGICAL", "Jung's psychological term mapped onto the alchemical magnum opus.", "ANALYST_TERM"),
    ("theosophy", "Christian Theosophy", "THEOLOGICAL", "A post-Reformation current originating with Böhme focusing on the inner life of God and nature.", "ANALYST_TERM"),
    ("chrysopoeia", "Chrysopoeia", "ALCHEMICAL", "The strictly metallurgical practice of transmuting base metals into gold.", "ACTOR_TERM")
]

PROSE_DATA = {
    # Scholars
    "moshe_idel": """
        <p>Moshe Idel (b. 1947) is a preeminent scholar of Jewish mysticism and Kabbalah, recognized for fundamentally revising the paradigm established by Gershom Scholem.</p>
        <h2>Ecstatic and Magical Kabbalah</h2>
        <p>While Scholem focused heavily on the theosophical and mythological aspects of Kabbalah (such as the <i>Zohar</i>), Idel's methodology brings the "Ecstatic Kabbalah" (specifically of Abraham Abulafia) and magical practices to the forefront. Idel demonstrates that Kabbalah was not purely theoretical; it involved intense, somatic meditative practices utilizing the permutation of divine names (<i>Tseruf</i>) to achieve mystical union. Idel's work is crucial for understanding Renaissance Christian Kabbalists like Pico della Mirandola, who were heavily influenced by these active, magical interpretations of Jewish mysticism.</p>
    """,
    "carlos_gilly": """
        <p>Carlos Gilly is a leading historian of early modern esotericism, universally recognized as the foremost authority on the historical origins of the Rosicrucian movement.</p>
        <h2>Dismantling the Rosicrucian Myth</h2>
        <p>Gilly's meticulous archival research fundamentally dismantled the idea that a literal, ancient "Brotherhood of the Rosy Cross" existed. He traced the drafting of the Rosicrucian manifestos (the <i>Fama</i> and <i>Confessio</i>) directly to a small circle of young Lutheran intellectuals in Tübingen, centered around Johann Valentin Andreae. Gilly demonstrated that the manifestos were intended as a <i>ludibrium</i> (a theatrical joke or serious play) designed to spark a genuine "General Reformation" of European science and religion by blending Paracelsian alchemy with radical Protestant theology. Through his work, the "Invisible College" is understood not as a secret society, but as a brilliant, viral literary phenomenon.</p>
    """,
    
    # Figures
    "tommaso_campanella": """
        <p>Tommaso Campanella (1568–1639) was a Dominican friar, philosopher, and poet whose radical synthesis of Hermetic magic, astrology, and political utopianism led to his imprisonment by the Inquisition for 27 years.</p>
        <h2>The City of the Sun and Astral Magic</h2>
        <p>Campanella is most famous for <i>The City of the Sun</i> (1602), a utopian text describing a society governed entirely by Hermetic principles. The city is designed as a massive talisman: its walls are painted with all human knowledge, and its citizens govern their lives, marriages, and labor according to precise astrological timing to draw down optimal planetary <i>spiritus</i>. Campanella famously attempted to put his theories into practice, performing a secret anti-eclipse magic ritual with Pope Urban VIII in 1628, sealing a room, lighting specific planetary fires, and drinking distilled liquors to ward off the baleful influence of a solar eclipse.</p>
    """,
    "francesco_patrizi": """
        <p>Francesco Patrizi (1529–1597) was a brilliant Renaissance philosopher who launched one of the most ambitious, yet ultimately doomed, attempts to institutionalize Hermeticism.</p>
        <h2>Replacing Aristotle with Hermes</h2>
        <p>In his <i>Nova de Universis Philosophia</i> (1591), Patrizi formally petitioned Pope Gregory XIV to completely eradicate the teaching of Aristotle in Catholic universities. Patrizi argued that Aristotle's materialism and denial of a creator God bred atheism and heresy. In Aristotle's place, Patrizi demanded that the Pope mandate the study of Hermes Trismegistus, Zoroaster, and the Neoplatonists, arguing that the <i>Corpus Hermeticum</i> was the purest, most ancient theology that perfectly harmonized with the Catholic faith. The Church responded by placing his work on the <i>Index of Prohibited Books</i>.</p>
    """,
    "robert_boyle": """
        <p>Robert Boyle (1627–1691) is celebrated as a founding father of modern chemistry and the pioneer of the experimental scientific method, yet he was also deeply immersed in highly secretive alchemical networks.</p>
        <h2>The "Science and Religion" Tension</h2>
        <p>Boyle's career explicitly shatters the modern distinction between rational science and esoteric alchemy. While he famously critiqued the Paracelsian <i>Tria Prima</i> in <i>The Sceptical Chymist</i>, Boyle simultaneously sought out adept alchemists, established communication with secretive figures like George Starkey (Eirenaeus Philalethes), and spent decades trying to physically witness the transmutation of base metals into gold via the Philosopher's Stone. For Boyle, alchemy was the highest echelon of empirical science—the ultimate proof of God's mechanical, particulate orchestration of nature.</p>
    """,

    # Texts
    "ch_x_the_key": """
        <p>Treatise X of the <i>Corpus Hermeticum</i>, commonly titled <i>The Key</i>, is often viewed as a summary or capstone of the philosophical Hermetica, synthesizing cosmology, psychology, and theology.</p>
        <h2>The Structure of the Cosmos and the Soul</h2>
        <p>The text is structured as a dialogue between Hermes and his son Tat. Hermes explicitly maps the architecture of reality: God is the Good; Nous (Mind) emanates from God; the Soul emanates from Nous; and the material world is ordered by the Soul. <i>The Key</i> is famous for its detailed explanation of the "subtle body" (<i>okhema</i>) or the <i>spiritus</i>, describing how the divine intellect wraps itself in fiery and airy envelopes to descend into the physical body. It teaches that humans are amphibious—mortal in body but immortal in mind—and that realizing this dual nature is the "Key" to salvation.</p>
    """,
    "kore_kosmou": """
        <p>The <i>Kore Kosmou</i> (Virgin of the World) is the longest and most spectacular of the Hermetic fragments preserved by John of Stobi (Stobaeus) in the 5th century.</p>
        <h2>Isis, Horus, and the Animation of Souls</h2>
        <p>Unlike the philosophical, Greek-leaning treatises of the <i>Corpus Hermeticum</i>, the <i>Kore Kosmou</i> is intensely mythological and explicitly Egyptian. It features the goddess Isis initiating her son Horus into the secret history of the universe. The text describes God creating souls in a divine cauldron, but the souls rebel through hubris and are subsequently imprisoned in human bodies as a punishment. God then sends down Osiris and Isis to establish laws, civilization, and the sacred Hermetic rites to guide the souls back to heaven. As scholars like Garth Fowden note, it perfectly represents the highly ritualistic, native Egyptian milieu of Hermeticism.</p>
    """,
    "turba_philosophorum": """
        <p>The <i>Turba Philosophorum</i> (The Assembly of the Philosophers) is one of the earliest and most foundational Latin alchemical texts, translated from an original Arabic treatise dating to around 900 AD.</p>
        <h2>Synthesizing Alchemy and Philosophy</h2>
        <p>The text is framed as a grand convention of pre-Socratic Greek philosophers (including Pythagoras, Anaxagoras, and Parmenides) gathering to debate the nature of matter. However, they are discussing these philosophical principles entirely through the lens of Islamic alchemy. The <i>Turba</i> was historically crucial because it introduced the Latin West not just to practical chemical recipes, but to the theoretical framework that alchemy was the practical application of Greek cosmology. It firmly established the concept that the alchemical work mimics God's creation of the universe from the four elements.</p>
    """,

    # Concepts
    "macrocosm_microcosm": """
        <p>The doctrine of the <i>Macrocosm and Microcosm</i> is a foundational <b>Actor Term</b> across all branches of Western Esotericism, alchemy, and Renaissance magic.</p>
        <h2>As Above, So Below</h2>
        <p>The concept asserts a direct, structural correspondence between the universe as a whole (the macrocosm) and the human being (the microcosm). Because man contains a miniature version of all the stars, planets, and elements found in the universe, an occult sympathy exists between them. This is the theoretical engine of all Renaissance magic: by manipulating the microcosm (through diet, imagination, or ritual), the magus can attract and influence the massive forces of the macrocosm. In alchemy, the transmutation of metals in the flask (microcosm) mirrors the perfection of the entire cosmos.</p>
    """,
    "christian_kabbalah": """
        <p><i>Christian Kabbalah</i> is an <b>Analyst Term</b> (though actors sometimes used variants) describing the Renaissance appropriation of Jewish mystical texts to prove Christian theological dogma.</p>
        <h2>The Renaissance Synthesis</h2>
        <p>Initiated by Giovanni Pico della Mirandola and formalized by Johannes Reuchlin, Christian Kabbalah argued that the secret, unwritten tradition given to Moses on Mount Sinai (the Kabbalah) contained the ultimate proof of the Christian Trinity and the Incarnation of Christ. Practitioners utilized complex Jewish exegetical techniques—like <i>Gematria</i> (numerology) and <i>Notarikon</i> (acronyms)—to decode the Old Testament. By the time of Cornelius Agrippa, Christian Kabbalah had been thoroughly fused with Hermeticism and Neoplatonism, forming the backbone of the "Occult Philosophy" that dominated early modern esoteric thought.</p>
    """,
    "astral_magic": """
        <p><i>Astral Magic</i> is an <b>Actor Term</b> describing the technical practice of drawing down specific planetary and celestial powers into the material world.</p>
        <h2>The Mechanics of Talismans</h2>
        <p>Based heavily on Arabic texts like the <i>Picatrix</i> and formalized in the West by Marsilio Ficino, astral magic requires precise astrological timing. The magus must wait for a planet (e.g., Venus) to be in a highly dignified, powerful position in the sky. Then, utilizing the doctrine of correspondence, the magus surrounds himself with items sympathetic to Venus (copper, roses, specific music) and inscribes a talisman with the planet's image or angelic name. This process captures the planetary <i>spiritus</i>, turning the talisman into a radiating battery of celestial power that can be used for healing, luck, or spiritual ascent.</p>
    """
}

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for pid, name, era, role, desc in NEW_PERSONS:
        try:
            cursor.execute("""
                INSERT INTO persons (person_id, name, era, role_primary, description, source_method, review_status, confidence)
                VALUES (?, ?, ?, ?, ?, 'SEED_DATA', 'REVIEWED', 'HIGH')
            """, (pid, name, era, role, desc))
        except sqlite3.IntegrityError:
            pass

    for tid, title, lang, ttype, start, end, desc, html, source, review, conf in NEW_TEXTS:
        try:
            cursor.execute("""
                INSERT INTO texts (text_id, title, language, text_type, date_composed_start, date_composed_end, description, analysis_html, source_method, review_status, confidence)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (tid, title, lang, ttype, start, end, desc, html, source, review, conf))
        except sqlite3.IntegrityError:
            pass

    for slug, label, category, desc, cat_type in NEW_CONCEPTS:
        try:
            cursor.execute("""
                INSERT INTO concepts (slug, label, category, definition_short, category_type, source_method)
                VALUES (?, ?, ?, ?, ?, 'SEED_DATA')
            """, (slug, label, category, desc, cat_type))
        except sqlite3.IntegrityError:
            pass

    for slug, prose in PROSE_DATA.items():
        cursor.execute("UPDATE persons SET bio_html = ? WHERE person_id = ?", (prose, slug))
        if cursor.rowcount == 0:
            cursor.execute("UPDATE texts SET analysis_html = ? WHERE text_id = ?", (prose, slug))
            if cursor.rowcount == 0:
                cursor.execute("UPDATE concepts SET definition_long = ? WHERE slug = ?", (prose, slug))

    conn.commit()
    conn.close()
    print("Comprehensive database expansion Phase 2 complete.")

if __name__ == "__main__":
    main()
