import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR.parent / "db" / "emerald_tablet.db"

NEW_PERSONS = [
    ("frances_yates", "Frances A. Yates", "MODERN", "SCHOLAR", "Originator of the 'Yates Paradigm' linking Hermeticism to the Scientific Revolution."),
    ("dp_walker", "D.P. Walker", "MODERN", "SCHOLAR", "Pioneering historian of spiritual and demonic magic in the Renaissance."),
    ("antoine_faivre", "Antoine Faivre", "MODERN", "SCHOLAR", "First chair of Western Esotericism at the Sorbonne; established the four-point definition of esotericism."),
    ("carlos_gilly", "Carlos Gilly", "MODERN", "SCHOLAR", "Preeminent historian of the early Rosicrucian manifestos and their historical origins."),
    ("kocku_von_stuckrad", "Kocku von Stuckrad", "MODERN", "SCHOLAR", "Proponent of a discursive approach to studying esotericism."),
    ("johannes_reuchlin", "Johannes Reuchlin", "RENAISSANCE", "SCHOLAR", "The founder of Christian Kabbalah."),
    ("johannes_trithemius", "Johannes Trithemius", "RENAISSANCE", "SCHOLAR", "Abbot, cryptographer, and theorist of angelic magic."),
    ("athanasius_kircher", "Athanasius Kircher", "EARLY_MODERN", "SCHOLAR", "Jesuit polymath who attempted to decode Egyptian hieroglyphs as Hermetic symbols."),
    ("isaac_newton", "Isaac Newton", "EARLY_MODERN", "SCHOLAR", "Key figure of the Scientific Revolution who covertly translated the Emerald Tablet and practiced alchemy."),
    ("thomas_vaughan", "Thomas Vaughan", "EARLY_MODERN", "PHILOSOPHER", "Welsh alchemist and Christian theosopher writing under the pseudonym Eugenius Philalethes."),
    ("suhrawardi", "Shihab al-Din Suhrawardi", "MEDIEVAL", "PHILOSOPHER", "Founder of Illuminationist (Ishraqi) philosophy who integrated Hermetic sages into Islamic prophecy."),
    ("abu_mashar", "Abu Ma'shar", "MEDIEVAL", "SCHOLAR", "Highly influential Persian astrologer who formalized the historical lineage of the three Hermes."),
]

NEW_TEXTS = [
    ("ch_i_poimandres", "CH I: Poimandres", "GREEK", "PRIMARY_SOURCE", 100, 300, "The foundational revelation of the Corpus Hermeticum.", "", "SEED_DATA", "REVIEWED", "HIGH"),
    ("ch_iv_krater", "CH IV: The Mixing Bowl (Krater)", "GREEK", "PRIMARY_SOURCE", 100, 300, "Treatise describing the baptism of the mind in a divine mixing bowl.", "", "SEED_DATA", "REVIEWED", "HIGH"),
    ("ch_xiii_secret_discourse", "CH XIII: The Secret Discourse on the Mountain", "GREEK", "PRIMARY_SOURCE", 100, 300, "Hermes initiates Tat into the mystery of spiritual rebirth.", "", "SEED_DATA", "REVIEWED", "HIGH"),
    ("fama_fraternitatis", "Fama Fraternitatis", "GERMAN", "MANIFESTO", 1614, 1614, "The first Rosicrucian manifesto announcing the discovery of Christian Rosenkreutz's tomb.", "", "SEED_DATA", "REVIEWED", "HIGH"),
    ("giordano_bruno_yates", "Giordano Bruno and the Hermetic Tradition", "ENGLISH", "COMPILATION", 1964, 1964, "Frances Yates's seminal work creating the Yates Paradigm.", "", "SEED_DATA", "REVIEWED", "HIGH")
]

NEW_CONCEPTS = [
    ("prisca_theologia", "Prisca Theologia", "THEOLOGICAL", "The doctrine of an ancient, singular theology given by God to early sages.", "ACTOR_TERM"),
    ("philosophia_perennis", "Philosophia Perennis", "THEOLOGICAL", "The idea of a timeless, universal philosophy underlying all religious traditions.", "ACTOR_TERM"),
    ("magia_naturalis", "Magia Naturalis", "PHILOSOPHICAL", "Natural magic; the manipulation of occult properties inherently present in nature.", "ACTOR_TERM"),
    ("pneuma", "Pneuma / Spiritus", "COSMOLOGICAL", "The subtle, airy substance that bridges the physical body and the immaterial soul.", "ACTOR_TERM"),
    ("okhema", "Okhema", "COSMOLOGICAL", "The 'vehicle' or subtle body of the soul in Neoplatonism.", "ACTOR_TERM"),
    ("lapis_philosophorum", "Lapis Philosophorum", "ALCHEMICAL", "The Philosopher's Stone.", "ACTOR_TERM"),
    ("anima_mundi", "Anima Mundi", "COSMOLOGICAL", "The World Soul; the animating spiritual principle of the universe.", "ACTOR_TERM"),
    ("yates_paradigm", "The Yates Paradigm", "HISTORIOGRAPHICAL", "The thesis that Renaissance Hermeticism caused the Scientific Revolution.", "ANALYST_TERM"),
    ("rejected_knowledge", "Rejected Knowledge", "HISTORIOGRAPHICAL", "Hanegraaff's definition of esotericism as the 'Other' constructed by Enlightenment discourse.", "ANALYST_TERM")
]

PROSE_DATA = {
    # Scholars
    "frances_yates": """
        <p>Frances A. Yates (1899–1981) was a historian at the Warburg Institute whose 1964 book, <i>Giordano Bruno and the Hermetic Tradition</i>, single-handedly catalyzed the modern academic study of Western Esotericism.</p>
        <h2>The Yates Paradigm</h2>
        <p>Yates argued that the rediscovery of the <i>Corpus Hermeticum</i> in the Renaissance fundamentally shifted the worldview of European intellectuals. By empowering the "Magus" to actively manipulate the cosmos (via natural magic and theurgy), Hermeticism broke the passive, contemplative mold of Aristotelian scholasticism. Yates controversially argued that this Hermetic operator was the direct ancestor of the modern empirical scientist, making Renaissance magic the missing link that sparked the Scientific Revolution.</p>
        <h2>Historiographical Tensions</h2>
        <p>While the "Yates Paradigm" dominated the late 20th century, modern scholars like Wouter Hanegraaff and Brian Copenhaver have dismantled its core premises. Copenhaver demonstrated that figures like Ficino were deeply rooted in orthodox scholasticism, not a separate "Hermetic religion." Nonetheless, Yates remains universally acknowledged for making the study of magic academically respectable.</p>
    """,
    "dp_walker": """
        <p>D.P. Walker (1914–1985) was a close colleague of Frances Yates at the Warburg Institute and a foundational historian of Renaissance magic. His seminal work, <i>Spiritual and Demonic Magic from Ficino to Campanella</i> (1958), fundamentally shaped the academic understanding of the mechanics of early modern occultism.</p>
        <h2>Spiritus and Demonic Magic</h2>
        <p>Unlike Yates, who painted sweeping macro-historical narratives, Walker focused meticulously on the technical mechanics of magic. He demonstrated how Ficino's <i>magia naturalis</i> relied on manipulating <i>spiritus</i> (the subtle, airy substance connecting body and soul) through music, planetary talismans, and diet. Walker traced how this seemingly innocent, medicalized magic was constantly haunted by the theological fear that planetary spirits were actually demons in disguise, leading to the severe orthodox backlash against figures like Cornelius Agrippa and Giordano Bruno.</p>
    """,
    "antoine_faivre": """
        <p>Antoine Faivre (1934–2021) was the first scholar to hold an academic chair dedicated to Western Esotericism (at the École Pratique des Hautes Études in Paris). He provided the field with its first rigorous empirical framework.</p>
        <h2>The Four-Point Definition</h2>
        <p>To prevent "esotericism" from remaining a vague, catch-all term, Faivre proposed a strict typology. For a current of thought to be classified as esoteric, it must exhibit four intrinsic characteristics: 1) A belief in universal <b>Correspondences</b> (macrocosm/microcosm), 2) The concept of a <b>Living Nature</b> (the cosmos animated by spiritual forces), 3) The necessity of <b>Imagination and Mediations</b> (rituals, angels, symbols to access the divine), and 4) The experience of <b>Transmutation</b> (inner spiritual alchemy). While highly influential, later scholars like Hanegraaff criticized this definition as being overly tailored to Renaissance Hermeticism and Christian Theosophy, excluding later secular or psychological occultisms.</p>
    """,
    
    # Historical Figures
    "johannes_reuchlin": """
        <p>Johannes Reuchlin (1455–1522) was a German humanist and the preeminent Christian scholar of Hebrew in the Renaissance. He is universally recognized as the founder of Christian Kabbalah.</p>
        <h2>Synthesizing Kabbalah and Christianity</h2>
        <p>In his major works, <i>De Verbo Mirifico</i> (On the Wonder-Working Word) and <i>De Arte Cabalistica</i> (On the Art of Kabbalah), Reuchlin expanded upon the groundwork laid by Giovanni Pico della Mirandola. He argued that the Jewish Kabbalah contained the original, uncorrupted revelation of God. Reuchlin claimed that the Tetragrammaton (YHVH) was historically unpronounceable until the incarnation of Christ inserted the letter Shin (S), creating the ultimate, wonder-working name of God: YHSVH (Jesus). This synthesis deeply intertwined Jewish mystical mechanics with Hermeticism and Neoplatonism in the minds of subsequent occult philosophers like Cornelius Agrippa.</p>
    """,
    "isaac_newton": """
        <p>Sir Isaac Newton (1642–1727) is universally renowned as the architect of classical mechanics and the Scientific Revolution. However, he was also a fiercely dedicated, clandestine alchemist.</p>
        <h2>Newton's Alchemical Phase</h2>
        <p>Newton left behind millions of words on alchemy, adopting pseudonyms like <i>Jeova Sanctus Unus</i>. He extensively studied the works of Michael Maier, George Ripley, and translated the <i>Emerald Tablet</i> into English. For Newton, alchemy was not a separate occult pursuit but an empirical investigation into the hidden "active principles" (which he later formalized mathematically as gravity) that God used to structure the cosmos. His engagement exemplifies the "Science and Religion" tension, proving that the rigid boundaries between early modern physics and Hermetic natural philosophy are retrospective analyst categories.</p>
    """,
    "abu_mashar": """
        <p>Abu Ma'shar al-Balkhi (787–886), known in the Latin West as Albumasar, was the most influential astrologer of the Abbasid court in Baghdad.</p>
        <h2>The Three Hermes</h2>
        <p>In his <i>Book of Thousands</i>, Abu Ma'shar formalized the legendary genealogy of "Hermes." To integrate Egyptian and Greek wisdom into the Islamic prophetic timeline, he proposed three distinct historical figures named Hermes. The first Hermes lived before the Flood and built the pyramids to preserve knowledge; the second was the Babylonian Hermes (identified with Pythagoras's teacher); the third was the Egyptian Hermes of Hellenistic Alexandria, who wrote on alchemy and astrology. This tripartite genealogy was immensely successful and was directly inherited by Latin Renaissance scholars.</p>
    """,

    # Texts
    "ch_i_poimandres": """
        <p>Treatise I of the <i>Corpus Hermeticum</i>, commonly known as the <i>Poimandres</i> (The Shepherd of Men), is the foundational revelation text of the Hermetic tradition.</p>
        <h2>The Hermetic Genesis</h2>
        <p>The text narrates an ecstatic vision in which an anonymous seeker (implicitly Hermes) encounters Poimandres, the divine <i>Nous</i> (Mind). Poimandres reveals the creation of the cosmos: how the elements separated from darkness, how the Demiurge crafted the seven planetary spheres, and how the primal, divine Anthropos (Man) descended through the spheres, falling in love with material Nature. The text serves as a soteriological map; it explains that because humans possess a divine mind trapped in a material body subject to planetary Fate, salvation is achieved through <i>gnosis</i>—remembering one's divine origin and reversing the descent through a cosmic ascent back to the Ogdoad.</p>
    """,
    "ch_xiii_secret_discourse": """
        <p>Treatise XIII of the <i>Corpus Hermeticum</i>, titled <i>The Secret Discourse on the Mountain</i>, represents the pinnacle of the "Way of Hermes" initiatory path.</p>
        <h2>The Mechanics of Rebirth</h2>
        <p>The dialogue features Hermes Trismegistus initiating his son, Tat. Tat complains that despite learning the general discourses, he has not experienced spiritual rebirth (<i>palingenesia</i>). Hermes explains that rebirth cannot be taught through rational discourse; it is an ecstatic, silent experience where the divine <i>Nous</i> replaces the sensory faculties. The text details a specific ritual incantation designed to drive out the twelve material torments (the Zodiac) and invite in the ten divine powers (the Ogdoad), resulting in Tat's deification and his ability to see the universe not with physical eyes, but through the singular eye of the Mind.</p>
    """,
    "fama_fraternitatis": """
        <p>The <i>Fama Fraternitatis</i> (1614) is the first of the three legendary Rosicrucian Manifestos, published anonymously (likely by a circle including Johann Valentin Andreae) in Kassel, Germany.</p>
        <h2>The Myth of Christian Rosenkreutz</h2>
        <p>The text announces the existence of a secret brotherhood founded by the mythical "Father C.R.C." (Christian Rosenkreutz), who traveled to the East (Arabia, Fez) to gather pristine alchemical and magical wisdom before returning to Europe. The manifesto calls for a "General Reformation" of both the Church and the sciences, explicitly rejecting the stale Aristotelianism of the universities and the papal authority of Rome in favor of a Paracelsian, Hermetic understanding of nature. As Carlos Gilly has shown, while the brotherhood was a literary fiction, the manifesto sparked a massive, very real intellectual frenzy across early modern Europe.</p>
    """,

    # Concepts
    "prisca_theologia": """
        <p>The <i>Prisca Theologia</i> (Ancient Theology) is a central <b>Actor Term</b> popularized by Marsilio Ficino during the Renaissance.</p>
        <h2>Lineage of Ancient Wisdom</h2>
        <p>Ficino posited a strict, historical chain of divine transmission. God imparted the ultimate truth to a series of ancient, pre-Christian sages, beginning with Zoroaster and Hermes Trismegistus, passing through Orpheus and Pythagoras, and culminating in Plato. This doctrine allowed Renaissance intellectuals to study pagan magic, Hermeticism, and Neoplatonism without heresy, as they argued these texts were not demonic paganism, but orthodox prophetic anticipations of Christianity.</p>
    """,
    "magia_naturalis": """
        <p><i>Magia Naturalis</i> (Natural Magic) is an <b>Actor Term</b> heavily deployed by Ficino, Pico, and Agrippa to legitimize their occult practices against accusations of demonic trafficking (<i>superstitio</i>).</p>
        <h2>The Mechanics of Occult Philosophy</h2>
        <p>Natural magic was theorized as a highly advanced form of natural philosophy. It posited that the universe is bound together by hidden sympathies and antipathies (e.g., the sunflower following the sun, the magnet attracting iron). The natural magician merely understands these hidden cosmic wires and utilizes natural items (stones, herbs, planetary music) to manipulate the <i>spiritus</i> (the subtle medium of the universe) to cure disease or attract celestial influences. It explicitly forbade the invocation of intelligent entities (angels or demons), separating it from ceremonial magic.</p>
    """,
    "yates_paradigm": """
        <p>The <i>Yates Paradigm</i> is a major <b>Analyst Term</b> referring to the historiographical thesis advanced by Frances Yates in 1964.</p>
        <h2>Hermeticism and the Scientific Revolution</h2>
        <p>Yates argued that Renaissance Hermeticism fundamentally changed the Western mindset by introducing the archetype of the "Magus"—the empowered operator who actively manipulates the environment. She posited that this active, operational mindset laid the necessary psychological groundwork for the empiricism of the Scientific Revolution, framing magic as the direct precursor to early modern science. While widely celebrated for bringing esotericism into mainstream academia, the paradigm has been heavily criticized by modern scholars like Hanegraaff and Copenhaver for ignoring the deeply traditional scholastic roots of figures like Ficino and drastically oversimplifying the complex relationship between magic and science.</p>
    """
}

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Insert new persons
    for pid, name, era, role, desc in NEW_PERSONS:
        try:
            cursor.execute("""
                INSERT INTO persons (person_id, name, era, role_primary, description, source_method, review_status, confidence)
                VALUES (?, ?, ?, ?, ?, 'SEED_DATA', 'REVIEWED', 'HIGH')
            """, (pid, name, era, role, desc))
            print(f"Added new figure: {name}")
        except sqlite3.IntegrityError:
            pass

    # Insert new texts
    for tid, title, lang, ttype, start, end, desc, html, source, review, conf in NEW_TEXTS:
        try:
            cursor.execute("""
                INSERT INTO texts (text_id, title, language, text_type, date_composed_start, date_composed_end, description, analysis_html, source_method, review_status, confidence)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (tid, title, lang, ttype, start, end, desc, html, source, review, conf))
            print(f"Added new text: {title}")
        except sqlite3.IntegrityError:
            pass

    # Insert new concepts
    for slug, label, category, desc, cat_type in NEW_CONCEPTS:
        try:
            cursor.execute("""
                INSERT INTO concepts (slug, label, category, definition_short, category_type, source_method)
                VALUES (?, ?, ?, ?, ?, 'SEED_DATA')
            """, (slug, label, category, desc, cat_type))
            print(f"Added new concept: {label}")
        except sqlite3.IntegrityError:
            pass

    # Update rich prose
    print("Injecting comprehensive deep scholarship...")
    for slug, prose in PROSE_DATA.items():
        cursor.execute("UPDATE persons SET bio_html = ? WHERE person_id = ?", (prose, slug))
        if cursor.rowcount == 0:
            cursor.execute("UPDATE texts SET analysis_html = ? WHERE text_id = ?", (prose, slug))
            if cursor.rowcount == 0:
                cursor.execute("UPDATE concepts SET definition_long = ? WHERE slug = ?", (prose, slug))

    conn.commit()
    conn.close()
    print("Comprehensive database expansion complete.")

if __name__ == "__main__":
    main()
