import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR.parent / "db" / "emerald_tablet.db"

NEW_PERSONS = [
    ("ramon_llull", "Ramon Llull", "MEDIEVAL", "PHILOSOPHER", "Catalan mystic and inventor of the Ars Magna combinatory system."),
    ("francis_mercury_van_helmont", "Francis Mercury van Helmont", "EARLY_MODERN", "PHILOSOPHER", "Flemish Christian Kabbalist and key bridge figure to Enlightenment thought."),
    ("jacob_boehme", "Jacob Boehme", "EARLY_MODERN", "PHILOSOPHER", "German Christian mystic and foundational figure of Christian Theosophy."),
    ("nicholas_of_cusa", "Nicholas of Cusa", "MEDIEVAL", "PHILOSOPHER", "German cardinal, philosopher of the coincidentia oppositorum."),
    ("al_kindi", "Al-Kindi", "MEDIEVAL", "PHILOSOPHER", "Arab philosopher whose De Radiis Stellarum theorized celestial influence."),
    ("plato", "Plato", "ANCIENT", "PHILOSOPHER", "Athenian philosopher whose Timaeus provided the cosmological framework for all later Hermeticism."),
    ("liana_saif", "Liana Saif", "MODERN", "SCHOLAR", "Historian of Arabic occult sciences and Islamic influences on Western magic."),
    ("paola_zambelli", "Paola Zambelli", "MODERN", "SCHOLAR", "Historian of Renaissance magic, astrology, and the ambiguous nature of magical philosophy.")
]

PROSE_DATA = {
    "ramon_llull": """
        <p>Ramon Llull (1232–1316) was a Catalan philosopher and mystic. While not strictly a Hermeticist himself, his computational logic system, the <i>Ars Magna</i>, became deeply entangled with Hermeticism and Kabbalah during the Renaissance.</p>
        <h2>Lullism and Magic</h2>
        <p>Llull's <i>Ars Magna</i> used rotating concentric wheels containing divine attributes to compute all possible truths about God and nature. In the Renaissance, figures like Giordano Bruno and Cornelius Agrippa hybridized Lull's wheels with Hermetic astrology and Kabbalistic letter permutation (<i>Tseruf</i>). They transformed Llull's orthodox theological computer into an operative magical engine designed to attract celestial <i>spiritus</i> and map the hidden architecture of the universe.</p>
    """,
    "francis_mercury_van_helmont": """
        <p>Francis Mercury van Helmont (1614–1698) was a Flemish philosopher, alchemist, and Christian Kabbalist. He served as a crucial bridge between the occult philosophy of the Renaissance and the rationalism of the Enlightenment.</p>
        <h2>The Kabbalah Denudata</h2>
        <p>Van Helmont worked closely with Christian Knorr von Rosenroth on the <i>Kabbala Denudata</i>, the massive Latin translation of the <i>Zohar</i> and Lurianic Kabbalah that made Jewish mysticism accessible to Christian Europe. Van Helmont synthesized this Kabbalah with Paracelsian alchemy, arguing for universal salvation (<i>apokatastasis</i>) and the transmigration of souls (<i>gilgul</i>). His friendship with Gottfried Wilhelm Leibniz profoundly influenced Leibniz's concept of the <i>Monad</i>, proving that Hermetic/Kabbalistic metaphysics were directly ancestral to Enlightenment philosophy.</p>
    """,
    "jacob_boehme": """
        <p>Jacob Boehme (1575–1624) was a German shoemaker turned mystic whose ecstatic visions birthed the movement known as Christian Theosophy.</p>
        <h2>Theosophy and Alchemy</h2>
        <p>In his masterwork <i>Aurora</i>, Boehme utilized the language of Paracelsian alchemy (the <i>Tria Prima</i>) to describe the inner life of God. He argued that God contains an inner wrath or dark fire that must be alchemically refined into love and light. Boehme shifted the focus of alchemy from laboratory metallurgy (<i>chrysopoeia</i>) to a purely spiritual, psychological cosmology. His concept of a universe born from divine tension heavily influenced later German Idealism and Romanticism.</p>
    """,
    "nicholas_of_cusa": """
        <p>Nicholas of Cusa (1401–1464) was a German cardinal whose radical Neoplatonic theology anticipated much of the Renaissance Hermetic worldview.</p>
        <h2>Coincidentia Oppositorum</h2>
        <p>Cusa is most famous for <i>De Docta Ignorantia</i> (On Learned Ignorance), where he argued that God is the infinite in which all contradictions are resolved—the <i>coincidentia oppositorum</i> (coincidence of opposites). Cusa viewed the universe as a contracted, infinite unfolding of the divine mind. His mathematical approach to theology profoundly influenced Giordano Bruno, who used Cusa's infinite universe to support his own Hermetic, heliocentric cosmology.</p>
    """,
    "al_kindi": """
        <p>Al-Kindi (801–873), the "Philosopher of the Arabs," was crucial in transmitting Hellenistic magical theory to the Islamic world and, subsequently, the Latin West.</p>
        <h2>De Radiis Stellarum</h2>
        <p>His treatise <i>De Radiis Stellarum</i> (On the Rays of the Stars) provided the ultimate physical rationale for astral magic. Al-Kindi theorized that every object in the universe emits rays of force (analogous to light) that interact with the rays of everything else. The stars emit the most powerful rays, guiding the sublunar world. The magus, using words, talismans, and intent, can emit their own rays to alter this cosmic web. This text became the scientific backbone for Renaissance magic from Ficino to John Dee.</p>
    """,
    "plato": """
        <p>Plato (c. 428–348 BC) is the foundational philosopher of Western thought. While predating the Hermetic texts, his cosmology was retroactively claimed by the Hermetic tradition through the concept of the <i>Prisca Theologia</i>.</p>
        <h2>The Timaeus and the Demiurge</h2>
        <p>Plato's dialogue the <i>Timaeus</i> describes the Demiurge crafting the physical universe by looking at eternal ideal forms. This text introduced the concept of the <i>Anima Mundi</i> (World Soul) and the mathematical structure of the elements. When the <i>Corpus Hermeticum</i> was composed centuries later in Roman Egypt, its authors utilized the vocabulary and cosmology of the <i>Timaeus</i> to translate indigenous Egyptian theology into Greek. During the Renaissance, Ficino explicitly argued that Plato was merely the Greek translator of the wisdom originally revealed by Hermes Trismegistus.</p>
    """,
    "liana_saif": """
        <p>Liana Saif is a prominent contemporary historian specializing in Arabic occult sciences and Islamic esotericism.</p>
        <h2>The Arabic Roots of Western Magic</h2>
        <p>Saif's scholarship is crucial for correcting the Eurocentric bias of the "Yates Paradigm," which often treated Renaissance magic as a sudden rediscovery of Greek texts. Saif demonstrates the profound dependence of Latin magic on Arabic transmission. Through studies of texts like the <i>Picatrix</i> (<i>Ghayat al-Hakim</i>) and the Epistles of the Brethren of Purity, she illustrates how Islamic scholars successfully synthesized late antique Hermeticism with Aristotelian physics, providing the robust theoretical framework that allowed figures like Ficino and Agrippa to practice astral magic.</p>
    """,
    "paola_zambelli": """
        <p>Paola Zambelli (1932–2019) was a distinguished Italian historian of philosophy and science, focusing on the Middle Ages and the Renaissance.</p>
        <h2>The Ambiguous Nature of Magic</h2>
        <p>Zambelli's extensive work on figures like Albertus Magnus, Cornelius Agrippa, and Giambattista della Porta highlighted the extreme ambiguity of the term "magic." She rigorously mapped the attempts of medieval and Renaissance scholars to separate licit "natural magic" from illicit "demonic magic" (necromancy). Zambelli showed that these boundaries were fluid, inherently unstable, and deeply political, fundamentally influencing how modern historiography handles the "reification" of magic.</p>
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
            print(f"Added new figure: {name}")
        except sqlite3.IntegrityError:
            pass

    print("Injecting comprehensive deep scholarship (Phase 3)...")
    for slug, prose in PROSE_DATA.items():
        cursor.execute("UPDATE persons SET bio_html = ? WHERE person_id = ?", (prose, slug))
        if cursor.rowcount == 0:
            cursor.execute("UPDATE texts SET analysis_html = ? WHERE text_id = ?", (prose, slug))
            if cursor.rowcount == 0:
                cursor.execute("UPDATE concepts SET definition_long = ? WHERE slug = ?", (prose, slug))

    conn.commit()
    conn.close()
    print("Database Expansion Phase 3 complete (Renaissance Magic Portal Raid).")

if __name__ == "__main__":
    main()
