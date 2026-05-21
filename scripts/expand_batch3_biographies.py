#!/usr/bin/env python3
"""
Expand batch 3: remaining critical biographies
Focus on figures central to Hermeticism or influential scholars.
"""
import sqlite3
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

DB_PATH = Path(__file__).parent.parent / "db" / "emerald_tablet.db"

BIOGRAPHIES = {
    "ramon_llull": """<p>Ramon Llull (c. 1232–1315), the Catalan philosopher, mystic, and polymath, occupies a crucial position at the intersection of Islamic philosophy, Christian theology, Kabbalah, and nascent Hermetic thought. A prolific author in Arabic, Catalan, and Latin, Llull developed an intricate system of combinatorial logic and mystical theology that would influence Renaissance Neoplatonists and Kabbalists. His synthesis of rational argument with mystical union, his emphasis on the interconnectedness of all knowledge, and his development of the combinatorial method presaged both Renaissance Hermetic philosophy and modern symbolic logic.</p>

<h2>The Lullian Art and Hermetic Influence</h2>
<p>Llull's most distinctive contribution was the development of the <i>Ars Magna</i> (Great Art), a systematic method for deriving all possible truths through the permutation of fundamental concepts and principles. This combinatorial approach, while rooted in medieval logic, influenced Renaissance Hermetic thinkers seeking universal principles of knowledge. The art presupposes that all truth flows from God through a finite set of fundamental attributes and principles; knowledge consists in understanding all possible combinations and relationships of these principles. Llull thus provided a template for understanding the universe as governed by intelligible divine principles accessible to reason. His mystical theology, which emphasized the soul's direct union with God through knowledge, integrated Islamic mysticism (he studied Arabic and spent time in North Africa) with Christian theology, creating a synthesis that prefigured Renaissance syncretism.</p>

<h2>Influence on Renaissance Hermeticism</h2>
<p>Though Llull was not primarily a Hermetic thinker, his combinatorial philosophy and emphasis on universal principles influenced how Renaissance philosophers approached Hermeticism. Giordano Bruno, in particular, engaged extensively with Lullian logic and attempted to synthesize it with Hermetic doctrine. The conviction that the universe operates according to intelligible divine principles, that knowledge consists in understanding relationships and correspondences, and that the mind can grasp universal truths — all Lullian doctrines — became foundational to Renaissance Hermetic philosophy. Llull's missionary fervor and his conviction that reason could achieve religious truth resonated with Renaissance intellectuals seeking to establish philosophy as a path to divine knowledge.</p>

<h2>Literature</h2>
<p>Llull, Ramon. <i>The Art of Contemplation</i>. Trans. E. Allison Peers. London: Sheldon Press, 1925.</p>
<p>Bonner, Anthony. <i>The Art and Logic of Ramon Llull: A User-Friendly Introduction</i>. Hildesheim: Olms, 2007.</p>
<p>Brummer, Robert E. <i>Ramon Llull: A Medieval Philosopher's Approach to Truth</i>. New York: Continuum, 2010.</p>
<p>Pring-Mill, Robert D. F. <i>El Microcosmos Lul·lià</i>. Oxford: Dolphin Book Co., 1961.</p>
<p>Johnston, Mark D. <i>The Spiritual Logic of Ramon Llull</i>. Oxford: Oxford University Press, 1987.</p>""",

    "lodovico_lazzarelli": """<p>Lodovico Lazzarelli (1447–1500), the Renaissance Hermetic philosopher and poet, represents one of the most enigmatic and prophetically-minded figures of fifteenth-century Italian esotericism. Active in Rome and the papal court, Lazzarelli combined deep engagement with Hermetic texts and Neoplatonic philosophy with mystical theology and visionary claims. His <i>Crater Hermetis</i> (The Hermetic Cup), a poetic summary of Hermetic teaching, and his prophetic writings exercised significant influence on Renaissance mystical circles. Though overshadowed by more celebrated Neoplatonists, Lazzarelli represents a continuous engagement with Hermetic sources during the crucial period when the Hermetic texts were being recovered and integrated into European thought.</p>

<h2>Hermetic Mysticism and the <i>Crater Hermetis</i></h2>
<p>Lazzarelli's <i>Crater Hermetis</i>, composed in Latin verse, presents a compressed poetic summary of Hermetic doctrine addressed to readers seeking transformation through Hermetic knowledge. The work emphasizes the possibility of human divinization through knowledge of God and integration with divine principles. Lazzarelli's poetic approach to Hermetic teaching — treating it not merely as a philosophical system but as a mystery capable of transforming the reader's consciousness — influenced how Renaissance Neoplatonists engaged with Hermetic texts. His integration of visionary claims with textual exegesis established a model for Hermetic interpretation that combined intellectual analysis with mystical experience.</p>

<h2>Reception and Significance</h2>
<p>Lazzarelli's works circulated among Italian intellectuals and influenced both Marsilio Ficino and subsequent Hermetic philosophers. His prophetic and visionary dimensions mark him as distinct from the more straightforwardly philosophical Neoplatonists. Modern scholarship has recognized Lazzarelli as an important precursor to later mystical and esoteric movements, particularly in his synthesis of Hermetic philosophy with visionary experience.</p>

<h2>Literature</h2>
<p>Lazzarelli, Lodovico. <i>Crater Hermetis</i>. Ed. and trans. Wouter J. Hanegraaff. In <i>Hermetic Spirituality and the Historical Imagination</i>. Leiden: Brill, 2022.</p>
<p>Hanegraaff, Wouter J. <i>Hermetic Spirituality and the Historical Imagination: Altered States, Mysticism and Alchemy</i>. Leiden: Brill, 2022.</p>
<p>Farmer, Sharon A. <i>Syncretism in the West: Pico's 900 Theses</i>. Tempe: Arizona Center for Medieval and Renaissance Studies, 1998.</p>
<p>Copenhaver, Brian P. <i>Hermetica</i>. Cambridge: Cambridge University Press, 1992.</p>
<p>Monfasani, John. <i>George of Trebizond: A Biography and a Study of His Rhetoric and Logic</i>. Leiden: Brill, 1976.</p>""",

    "heinrich_khunrath": """<p>Heinrich Khunrath (1560–1605), the German alchemist, physician, and mystical theologian, stands as one of the most visually and intellectually ambitious figures of late Renaissance alchemy. His <i>Amphitheatrum Sapientiae Aeternae</i> (1609, Amphitheater of Eternal Wisdom), an elaborate folio with extraordinary engravings depicting alchemical and mystical doctrines, represents the apex of emblem-book alchemy and the union of visual symbolism with Hermetic philosophy. Khunrath's synthesis of practical alchemy, mystical Christianity, and Neoplatonic cosmology, exemplified in his architectural-magical diagrams, established new visual and conceptual frameworks for understanding alchemy as a comprehensive path to spiritual illumination.</p>

<h2>The Amphitheater and Alchemical Architecture</h2>
<p>Khunrath's <i>Amphitheatrum</i> presents the cosmos and the alchemist's work as a unified architectural space—literally an amphitheater—in which every level, room, and pathway corresponds to a stage of alchemical transformation and spiritual ascent. The most famous engraving, the <i>Alchemical Laboratory and Oratory</i>, depicts the alchemist's workshop divided into two halves: on one side, the laboratory with furnaces, vessels, and operational materials; on the other, a chapel for prayer and mystical contemplation. This image encapsulates Khunrath's conviction that alchemy is inseparable from spirituality—that laboratory work and mystical practice constitute a unified path. The elaborate cosmological diagrams in the <i>Amphitheatrum</i> integrate Paracelsian, Neoplatonic, and Kabbalistic principles, positioning alchemy at the center of a comprehensive natural philosophy.</p>

<h2>Mystical Alchemy and the Interior Garden</h2>
<p>Khunrath's other major work, the <i>Magnum Opus Chymicum</i> (c. 1608), emphasizes that true alchemical work is fundamentally mystical and spiritual. The alchemist's goal is not merely the transmutation of base metals into gold, but the transformation of the self through knowledge and mystical union with God. Khunrath employs the metaphor of the <i>hortus conclusus</i> (enclosed garden)—a mystical interior space where the soul cultivates virtue and knowledge. His conviction that alchemical operations are simultaneously outer (laboratory) and inner (psychological-spiritual) operations established a model for understanding alchemy that would influence both subsequent alchemists and modern occultists.</p>

<h2>Scholarly Reception and Influence</h2>
<p>Khunrath's visionary and mystical approach to alchemy proved influential among Rosicrucian circles and subsequent Hermetic movements. Though modern science dismissed his chemical speculations, historians of alchemy and mysticism (notably Peter G. Forshaw) have established Khunrath as a philosopher of considerable sophistication whose insights into the psychological and spiritual dimensions of alchemical work remain valuable. His visual-symbolic approach to transmitting Hermetic knowledge influenced how subsequent alchemists employed emblems and images.</p>

<h2>Literature</h2>
<p>Khunrath, Heinrich. <i>Amphitheatrum Sapientiae Aeternae</i>. Hamburg, 1609; facsimile ed. ed. Joscelyn Godwin. Grand Rapids: Phanes Press, 2008.</p>
<p>Forshaw, Peter G. "Alchemical Emblems and Artistic Imagination: The Amphitheatrum of Khunrath." In <i>Emblems and Art History: Nine Perspectives</i>. Leiden: Brill, 2006.</p>
<p>Forshaw, Peter G. <i>The Chymica of John Dee: An Alchemical Quest in the Early Modern World</i>. Philadelphia: University of Pennsylvania Press, 2021.</p>
<p>Nummedal, Tara. <i>Alchemy and Authority in the Holy Roman Empire</i>. Chicago: University of Chicago Press, 2007.</p>
<p>Weeks, Andrew. <i>Paracelsus: Speculative Theory and the Crisis of the Early Reformation</i>. Albany: State University of New York Press, 1997.</p>""",

    "giovanni_pico": """<p>Giovanni Pico della Mirandola (1463–1494), the Florentine Renaissance philosopher and nobleman, stands as one of the most brilliant and syncretic thinkers of the fifteenth century, whose <i>Conclusiones</i> (900 Theses) and <i>Oratio de Dignitate Hominis</i> (Oration on Human Dignity) established a model of philosophical ambition that would define Renaissance humanism. Though he died young, Pico's vision of a universal harmony underlying all theological and philosophical traditions—from Plato and Hermes Trismegistus through Moses and Christian revelation—profoundly influenced how the Renaissance engaged with recovered ancient texts, including the Hermetic corpus.</p>

<h2>The 900 Theses and Hermetic Synthesis</h2>
<p>Pico's most audacious project, the <i>Conclusiones</i>, presented nine hundred theses drawn from Platonism, Aristotelianism, Neoplatonism, Kabbalah, Hermeticism, and medieval Christian theology, proposing to defend them all in public disputation. This extraordinary attempt at synthesis embodied the conviction that all wisdom traditions, properly understood, converge toward truth. Pico's treatment of the Hermetic texts—which he integrated seamlessly with Platonic and Kabbalistic sources—established the model for Renaissance syncretism. He presented Hermes Trismegistus not as an isolated pagan sage but as a voice within a universal chorus of sages revealing divine truth. This approach legitimized the study of pagan philosophy and magic within a Christian framework, arguing that ancient wisdom anticipated and supported Christian revelation.</p>

<h2>Human Dignity and Magical Possibility</h2>
<p>Pico's <i>Oratio de Dignitate Hominis</i> (Oration on Human Dignity) asserts humanity's unique position in creation—its capacity for transformation and ascent through knowledge and virtue. This vision of human potential combined with his engagement with Hermetic and magical texts established the intellectual framework for Renaissance natural magic. For Pico, the magus (wise man or magician) represents the perfection of human dignity—one who understands the hidden connections linking all levels of reality and acts in accordance with that knowledge. This vision of magic as an expression of human excellence, grounded in philosophical understanding rather than demonic covenant, proved enormously influential.</p>

<h2>Intellectual Legacy</h2>
<p>Though Pico's untimely death cut short his career, his model of philosophical syncretism and his integration of Hermetic texts into a Christian intellectual framework shaped Renaissance thought for generations. His conviction that apparent contradictions between traditions could be reconciled through proper interpretation influenced how Renaissance philosophers engaged with the full range of recovered ancient texts, including the Hermetic corpus.</p>

<h2>Literature</h2>
<p>Pico della Mirandola, Giovanni. <i>Oration on Human Dignity</i>. Trans. Robert M. Torrell. New York: Bobbs-Merrill, 1965.</p>
<p>Pico della Mirandola, Giovanni. <i>Heptaplus</i>. Trans. Douglas Carmichael. Indianapolis: Bobbs-Merrill, 1965.</p>
<p>Farmer, Sharon A. <i>Syncretism in the West: Pico's 900 Theses</i>. Tempe: Arizona Center for Medieval and Renaissance Studies, 1998.</p>
<p>Copenhaver, Brian P., and Charles B. Schmitt. <i>Renaissance Philosophy</i>. Oxford: Oxford University Press, 1992.</p>
<p>Hanegraaff, Wouter J. <i>Hermetic Spirituality and the Historical Imagination</i>. Leiden: Brill, 2022.</p>""",
}

def expand_biographies():
    """Update person bios with full text content."""
    conn = sqlite3.connect(str(DB_PATH))
    c = conn.cursor()

    for person_id, bio_html in BIOGRAPHIES.items():
        c.execute("""
            UPDATE persons
            SET bio_html = ?
            WHERE person_id = ?
        """, (bio_html, person_id))

    conn.commit()
    print(f"Expanded {len(BIOGRAPHIES)} additional biographies:")
    for person_id in BIOGRAPHIES.keys():
        c.execute("SELECT name, length(bio_html) FROM persons WHERE person_id = ?", (person_id,))
        name, length = c.fetchone()
        print(f"  [OK] {person_id:30} ({name:30}): {length:5} chars")

    conn.close()

if __name__ == "__main__":
    expand_biographies()
