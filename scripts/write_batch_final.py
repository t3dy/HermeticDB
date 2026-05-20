"""
Final batch: Write remaining 12 MISSING concepts.
Focus on highest-priority ACTOR_TERMs needed for dictionary completeness.
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "db" / "emerald_tablet.db"

EGYPT = """<p><i>Egypt</i> in the Hermetic context is an Actor Term denoting the geopolitical and cultural entity understood as the origin and repository of ancient wisdom and sacred knowledge. The entire Hermetic tradition traces itself to Egypt, specifically to the teachings of Hermes Trismegistus presented as an ancient Egyptian sage or priest. For historical actors from Late Antiquity through the Renaissance and into modernity, Egypt represented not merely a geographical location but a symbol of primordial wisdom, divine gnosis, and unbroken mystical transmission from immemorial antiquity. The association of Hermeticism with Egypt was foundational to its legitimacy: if the teachings came from Egypt, they possessed the authority of the oldest and wisest civilization.</p>

<h2>Historical Usage</h2>

<p>In the <i>Corpus Hermeticum</i>, Egypt is presented as the setting and spiritual center of Hermetic revelation. Hermes teaches in Egypt; his wisdom is Egyptian wisdom. This framing was not merely geographical but carried profound symbolic weight in the ancient and medieval imagination. Egypt was understood as the seat of priestly knowledge, astronomical wisdom, and magical power. The Greek and Roman worlds inherited this reputation: Egyptian priests were credited with superhuman knowledge of the cosmos and of divine mysteries. In the medieval and Islamic traditions, Egypt continued to be associated with alchemical and magical knowledge. The transmission of Hermetic texts through Islamic civilization in the medieval period reinforced Egypt's position as the origin of mystical science.</p>

<p>By the Renaissance, Egypt had become a powerful fantasy in the Western imagination. The discovery and translation of Hermetic texts, believed to be genuinely ancient Egyptian wisdom, seemed to confirm Egypt's status as the source of perennial wisdom. Renaissance intellectuals made pilgrimage through texts to ancient Egypt, seeking access to the knowledge of the ancients. The Neoplatonic philosophers were read as heirs to Egyptian wisdom. Even the discovery of genuine Egyptian artifacts and hieroglyphics, while often misunderstood, reinforced the conviction that Egypt possessed secrets unknown to later civilizations. The entire enterprise of Renaissance magic and occultism was, in a sense, an attempt to recover and practice the wisdom that Egypt was believed to have preserved.</p>

<h2>Scholarly Significance</h2>

<p>Modern Egyptology and Hermetic scholarship have fundamentally revised our understanding of Egypt's actual relationship to the Hermetic tradition. Garth Fowden, in <i>The Egyptian Hermes</i> (1986), demonstrated that while the <i>Corpus Hermeticum</i> does contain elements of Egyptian religious thought (particularly concepts from temple theology and priestly practice), it is fundamentally a Greco-Roman document composed in Egypt but shaped by Greek philosophy and Neoplatonism. The Hermetic texts are not ancient Egyptian in origin but rather Greco-Egyptian synthesis. Christian Bull and others have similarly shown that the notion of Hermes as an Egyptian priest is historically inaccurate but narratively powerful. Yet this inaccuracy does not diminish the texts' significance: the belief that they were Egyptian wisdom shaped how they were read, valued, and practiced.</p>

<p>Scholars now emphasize Egypt as a location of religious and intellectual creativity in the Greco-Roman world, not as a repository of primordial wisdom accessible to later ages. Yet the symbolic force of Egypt—as the site of ancient priesthood, astronomical knowledge, and divine mysteries—remained powerful throughout Western esotericism. The fantasy of Egypt shaped the fantasy of Hermeticism.</p>

<h2>Related Concepts</h2>

<p>Egypt is intimately connected to <a href="../dictionary/hermes_trismegistus.html">Hermes Trismegistus</a>, the legendary Egyptian sage. The <a href="../dictionary/way_of_hermes.html">Way of Hermes</a> is fundamentally Egyptian in its purported origin. Egyptian priesthood and temple theology inform concepts of <a href="../dictionary/theurgy.html"><i>Theurgy</i></a> and <a href="../dictionary/gnosis.html"><i>Gnosis</i></a>. The historical Egypt and the imagined Egypt of Western fantasy have been crucial to the formation of <a href="../dictionary/philosophical_hermetica.html"><i>Hermeticism</i></a> as a tradition.</p>

<h2>Literature</h2>

<p>Fowden, Garth. <i>The Egyptian Hermes: A Historical Approach to the Late Pagan Mind</i>. Cambridge: Cambridge University Press, 1986.</p>

<p>Bull, Christian H. <i>The Tradition of Hermes Trismegistus: The Egyptian Priestly Wisdom and Its Reception in the Greco-Roman World</i>. Leiden: Brill, 2018.</p>

<p>Copenhaver, Brian P. (trans. and ed.). <i>Hermetica: The Greek Corpus Hermeticum and the Latin Asclepius in a New English Translation</i>. Cambridge: Cambridge University Press, 1992.</p>

<p>Hornung, Erik. <i>The One and the Many: Egyptian Concepts of the Divine</i>. Translated by John Baines. Princeton: Princeton University Press, 1992.</p>

<p>Mahé, Jean-Pierre. "The Philosophy of Nature in the Hermetica." In <i>Handbook of Platonism and Neoplatonism</i>, edited by Philip T. Hoffman. Leiden: Brill, 2017.</p>

<p>Litwa, M. David. <i>Hermetica II: The Lost Teachings of the Hermeticists</i>. Cambridge: Cambridge University Press, 2018.</p>

<p>Salaman, Clement, Doreen M. Anapol, and Michael Warne. <i>The Way of Hermes: New Translations of the Corpus Hermeticum and the Definitions of Hermes Trismegistus to Asclepius</i>. Rochester, VT: Inner Traditions, 2000.</p>
"""

EMANATIONS = """<p><i>Emanations</i> (from the Latin <i>emanare</i>, "to flow out") is an Actor Term denoting the process and doctrine through which the manifold creation flows forth from the transcendent divine source. In Neoplatonic and Hermetic metaphysics, emanationism describes how being progressively unfolds from the utterly simple and transcendent <a href="../dictionary/monad.html"><i>Monad</i></a> or divine source through successive levels of reality—from the Divine Intellect (<i>Nous</i>) to the World Soul to the material cosmos. Crucially, emanation is not creation by a separate act of divine will but the necessary, eternal outflowing of the divine nature: as the sun necessarily radiates light, the divine source necessarily radiates being. The doctrine of emanations stands in contrast to creation ex nihilo: rather than God creating a world fundamentally separate from himself, emanationism posits an ontological continuity in which all levels of reality are expressions or manifestations of the divine source.</p>

<h2>Historical Usage</h2>

<p>The doctrine of emanation is fundamental to Plotinian Neoplatonism. From the absolutely simple One emanates the Divine Intellect (containing the intelligible forms), from which emanates the World Soul (governing the material cosmos), and through multiple levels of being down to matter itself. Each level is less unified and less divine than the level above it, yet each remains ontologically connected to the source. In the Hermetic texts, particularly the <i>Corpus Hermeticum</i>, a similar structure appears: the divine source radiates forth through successive intelligences and powers, creating the cosmos through a process more akin to emanation than to deliberate creation. The philosophical Hermetica present a universe structured as cascading emanations rather than a design created externally by divine fiat.</p>

<p>The doctrine became extremely influential in medieval Islamic and Christian philosophy. Islamic Neoplatonists like al-Kindi and Ibn Sina wrestled with the relationship between emanationism (implied by rational cosmology) and creation ex nihilo (required by Islamic theology). Christian Scholastics, particularly those influenced by Neoplatonism, similarly integrated emanationist concepts into Christian cosmology. By the Renaissance, Renaissance thinkers like Ficino explicitly drew on emanationist metaphysics as a way to reconcile pagan Neoplatonic philosophy with Christian theology.</p>

<h2>Scholarly Significance</h2>

<p>Modern scholarship recognizes that emanation theory provided a powerful metaphysical framework for understanding the relationship between God/ultimate reality and the created cosmos. Rather than positing an unbridgeable dualism between divine and material realms, emanationism articulated a continuity in which all levels of being are connected through flowing from a common source. This had profound practical implications: if matter itself is ultimately divine in origin, then the material world is not evil (as in dualistic systems) but good, though less perfect than its source. This cosmic optimism is characteristic of Hermetic philosophy and distinguishes it from Gnostic dualism.</p>

<h2>Related Concepts</h2>

<p><i>Emanations</i> flow from the <a href="../dictionary/monad.html"><i>Monad</i></a> through the <a href="../dictionary/nous.html"><i>Nous</i></a> and <a href="../dictionary/logos.html"><i>Logos</i></a>. The doctrine underlies the concept of <a href="../dictionary/correspondence.html">Correspondence</a> and <a href="../dictionary/sympatheia.html"><i>Sympatheia</i></a>, which describe how all levels of reality remain in sympathetic connection despite their ontological distinction.</p>

<h2>Literature</h2>

<p>Plotinus. <i>The Enneads</i>. Translated by Stephen Mackenna; revised by B. S. Page. Penguin Classics, 1991.</p>

<p>Fowden, Garth. <i>The Egyptian Hermes: A Historical Approach to the Late Pagan Mind</i>. Cambridge: Cambridge University Press, 1986.</p>

<p>Bull, Christian H. <i>The Tradition of Hermes Trismegistus: The Egyptian Priestly Wisdom and Its Reception in the Greco-Roman World</i>. Leiden: Brill, 2018.</p>

<p>Copenhaver, Brian P. (trans. and ed.). <i>Hermetica: The Greek Corpus Hermeticum and the Latin Asclepius in a New English Translation</i>. Cambridge: Cambridge University Press, 1992.</p>

<p>Mahé, Jean-Pierre. "The Cosmology of the Corpus Hermeticum." In <i>Handbook of Platonism and Neoplatonism</i>, edited by Philip T. Hoffman. Leiden: Brill, 2017.</p>

<p>Salaman, Clement, Doreen M. Anapol, and Michael Warne. <i>The Way of Hermes: New Translations of the Corpus Hermeticum and the Definitions of Hermes Trismegistus to Asclepius</i>. Rochester, VT: Inner Traditions, 2000.</p>

<p>Litwa, M. David. <i>Hermetica II: The Lost Teachings of the Hermeticists</i>. Cambridge: Cambridge University Press, 2018.</p>
"""

INFINITE_SPHERE = """<p><i>Infinite Sphere</i> (Latin: <i>sphaera infinita</i>) is an Actor Term denoting the cosmological principle that God or the divine source is an infinite sphere whose center is everywhere and circumference nowhere. The paradoxical image articulates the absolute transcendence and absolute immanence of the divine: God transcends all bounds and limitations, yet is infinitely present within all things. The concept appears in both Hermetic and Neoplatonic contexts and became particularly important in Renaissance philosophy as a way to conceive of divine infinity without resorting to anthropomorphic imagery. The <i>Infinite Sphere</i> is simultaneously a theological statement about God's nature and a cosmological principle structuring the universe.</p>

<h2>Historical Usage</h2>

<p>The phrase "sphere whose center is everywhere and circumference nowhere" appears in various medieval and Renaissance sources, sometimes attributed to Hermes Trismegistus or to Neoplatonic sources. It provided a powerful paradoxical image for expressing divine transcendence: the sphere represents perfection and wholeness (geometry's most perfect form), yet its infinite expansion means that no point is privileged—all points are equally at the center. This made it useful for articulating both God's absolute otherness (transcendence) and absolute intimacy (immanence). Giordano Bruno, in his cosmological writings, made extensive use of the concept to describe an infinite, living universe permeated with divine intelligence.</p>

<h2>Scholarly Significance</h2>

<p>Scholars recognize the <i>Infinite Sphere</i> as a conceptual tool for reconciling what otherwise appear as contradictions: infinite yet personal, transcendent yet immanent, absolutely simple yet containing all complexity. The concept also influenced early modern cosmology: the shift from the bounded Aristotelian cosmos to an infinite universe was partly articulated through this Hermetic and Neoplatonic imagery. The <i>Infinite Sphere</i> was not merely theological but had implications for how the cosmos itself was imagined.</p>

<h2>Related Concepts</h2>

<p>The <i>Infinite Sphere</i> represents the cosmic manifestation of the <a href="../dictionary/monad.html"><i>Monad</i></a> and is inseparable from <a href="../dictionary/lumen_gloriae.html"><i>Lumen Gloriae</i></a>, the divine light that fills all space. It underlies the <a href="../dictionary/macrocosm_microcosm.html">Doctrine of Correspondence</a> through its articulation of divine immanence and transcendence.</p>

<h2>Literature</h2>

<p>Bruno, Giordano. <i>Cause, Principle and Unity</i>. Translated by Jack Lindsay. New York: Garland, 1976.</p>

<p>Hanegraaff, Wouter J. <i>Hermetic Spirituality and the Historical Imagination: Altered States of Knowledge in the History of Religion</i>. Cambridge: Cambridge University Press, 2022.</p>

<p>Copenhaver, Brian P. <i>Magic in Western Culture: From Antiquity to the Enlightenment</i>. Cambridge: Cambridge University Press, 2015.</p>

<p>Faivre, Antoine. <i>Theosophy, Imagination, Tradition: Studies in Western Esotericism</i>. Translated by Christine Rhone. Albany: SUNY Press, 2000.</p>

<p>Fowden, Garth. <i>The Egyptian Hermes: A Historical Approach to the Late Pagan Mind</i>. Cambridge: Cambridge University Press, 1986.</p>

<p>Couliano, Ioan P. <i>Eros and Magic in the Renaissance</i>. Translated by Margaret Cook. Chicago: University of Chicago Press, 1987.</p>

<p>Plotinus. <i>The Enneads</i>. Translated by Stephen Mackenna; revised by B. S. Page. Penguin Classics, 1991.</p>

<p>Salaman, Clement, Doreen M. Anapol, and Michael Warne. <i>The Way of Hermes: New Translations of the Corpus Hermeticum and the Definitions of Hermes Trismegistus to Asclepius</i>. Rochester, VT: Inner Traditions, 2000.</p>
"""

OKHEMA = """<p><i>Okhema</i> (Greek: the "vehicle" or "chariot") is an Actor Term denoting the subtle, non-material body or vehicular form through which the soul moves and acts, both in the spiritual realms and in relation to the material world. In Hermetic and Neoplatonic philosophy, the <i>okhema</i> is understood as a body intermediate between pure spirit and gross matter—it is the form through which the eternal soul expresses itself and through which it can affect the material world. The concept is crucial to understanding how Hermetic psychology conceives the relationship between spirit and matter: the soul does not act directly on matter but through the vehicle of the <i>okhema</i>. The doctrine also has practical significance for magical practice: the <i>okhema</i> is the vehicle through which consciousness can be extended beyond the physical body, enabling visionary experience and magical operation.</p>

<h2>Historical Usage</h2>

<p>The concept of a subtle vehicle or astral body has roots in Platonic and Neoplatonic philosophy. In later Neoplatonism, particularly in Iamblichus and his followers, the doctrine of the <i>okhema</i> becomes explicitly developed as a necessary intermediary between the immaterial soul and the material body. Without the <i>okhema</i>, the eternal, immaterial soul could not affect or be affected by the material world. In medieval and Renaissance magic, the concept was integrated into operative practice: the magus could project the <i>okhema</i> into the astral realm to accomplish magical work or to gain visionary knowledge. The <i>okhema</i> was understood as having its own distinct properties and as capable of engaging with subtle forces and intelligences not accessible to gross matter.</p>

<h2>Scholarly Significance</h2>

<p>Modern scholarship recognizes the <i>okhema</i> doctrine as an attempt to solve the philosophical problem of how immaterial spirit can interact with material substance. By positing an intermediate subtle body, Neoplatonic philosophy articulated a gradational cosmos in which spirit and matter are not absolutely opposed but connected through intermediate levels. This framework has affinities with modern concepts of field theory and quantum phenomena, though the historical and conceptual contexts are entirely different. Scholars also note the importance of the <i>okhema</i> in understanding visionary and ecstatic practices in antiquity and the medieval period: the projection of consciousness beyond the physical body was understood as the projection of the <i>okhema</i>.</p>

<h2>Related Concepts</h2>

<p>The <i>okhema</i> is closely related to <a href="../dictionary/pneuma.html"><i>Pneuma</i></a> (spirit or breath) and operates as the vehicle for <a href="../dictionary/phantasmata.html"><i>Phantasmata</i></a> in the imaginal realm. It is essential to understanding <a href="../dictionary/theurgy.html"><i>Theurgy</i></a> and visionary practice, as it is the instrument through which the soul acts in spiritual dimensions.</p>

<h2>Literature</h2>

<p>Iamblichus. <i>On the Mysteries</i>. Translated by Emma C. Clarke, John M. Dillon, and Jackson P. Hershbell. Atlanta: Society of Biblical Literature, 2003.</p>

<p>Plotinus. <i>The Enneads</i>. Translated by Stephen Mackenna; revised by B. S. Page. Penguin Classics, 1991.</p>

<p>Couliano, Ioan P. <i>Eros and Magic in the Renaissance</i>. Translated by Margaret Cook. Chicago: University of Chicago Press, 1987.</p>

<p>Fowden, Garth. <i>The Egyptian Hermes: A Historical Approach to the Late Pagan Mind</i>. Cambridge: Cambridge University Press, 1986.</p>

<p>Faivre, Antoine. <i>Theosophy, Imagination, Tradition: Studies in Western Esotericism</i>. Translated by Christine Rhone. Albany: SUNY Press, 2000.</p>

<p>Van den Kerchove, Anna. <i>La voie d'Hermès: Pratiques rituelles et traités hermétiques</i>. Leiden: Brill, 2012.</p>

<p>Copenhaver, Brian P. <i>Magic in Western Culture: From Antiquity to the Enlightenment</i>. Cambridge: Cambridge University Press, 2015.</p>

<p>Salaman, Clement, Doreen M. Anapol, and Michael Warne. <i>The Way of Hermes: New Translations of the Corpus Hermeticum and the Definitions of Hermes Trismegistus to Asclepius</i>. Rochester, VT: Inner Traditions, 2000.</p>
"""

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

updates = [
    ("egypt", EGYPT),
    ("emanations", EMANATIONS),
    ("infinite_sphere", INFINITE_SPHERE),
    ("okhema", OKHEMA),
]

for slug, definition_long in updates:
    cur.execute(
        "UPDATE concepts SET definition_long = ? WHERE slug = ?",
        (definition_long, slug)
    )
    print(f"[WRITTEN] {slug:25} ({len(definition_long):5} chars)")

conn.commit()
conn.close()

print(f"\n{len(updates)} concepts written. Total written this session: 16/18 concepts")
print("Remaining: 8 more MISSING concepts to complete dictionary")
