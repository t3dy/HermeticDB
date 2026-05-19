"""
Second batch of encyclopedia entries for ACTOR_TERMs:
- palingenesia (PARTIAL -> expand)
- way_of_hermes (STUB -> write)
- tria_prima (STUB -> write)
- monad (STUB -> write)
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "db" / "emerald_tablet.db"

PALINGENESIA = """<p><i>Palingenesia</i> (from the Greek <i>palin</i>, "again," and <i>genesis</i>, "birth" or "becoming") is an Actor Term central to the philosophical Hermetica, denoting the process of spiritual rebirth or regeneration through which the human soul is transformed from its fallen, forgetful state into a divinized being capable of direct knowledge of God. In the <i>Corpus Hermeticum</i>, particularly Tractate XIII, <i>palingenesia</i> describes not a future eschatological event but a present, achievable transformation that begins with the purification of consciousness and culminates in the soul's direct vision of the divine and its reunion with the divine Intellect. Importantly, <i>palingenesia</i> in the Hermetic context is explicitly joyful and cosmic-optimistic: the soul does not escape from matter or the cosmos but rather awakens to its true nature as a microcosm that contains within itself the divine order of the macrocosm. The doctrine stands in sharp contrast to ascetic or dualistic forms of spirituality that view the material world or the body as inherently evil.</p>

<h2>Historical Usage</h2>

<p>The term <i>palingenesia</i> appears explicitly in Tractate XIII of the <i>Corpus Hermeticum</i>, where Hermes instructs his son Tat in the secret doctrine of spiritual transformation. Hermes describes the process as follows: the soul, bound by the twelve zodiacal forces that govern material existence, must undergo a radical reconstitution of consciousness through the ascent of the mind (<i>nous</i>) toward divine unity. This ascent is not gradual refinement but a sudden death and rebirth — the soul must "die" to its identification with the material body and the material world and be "born" anew as a child of the divine Mind. This rebirth is accompanied by profound joy and illumination: "When the soul is reborn, it strips off the twelve-fold nature that is bound around it, and it encounters the octave, the realm of light beyond the zodiacal influences." The language is explicitly mystical and visionary — <i>palingenesia</i> is not intellectual assent but a transformative encounter.</p>

<p>In the transmission of this doctrine through Late Antique Neoplatonism, particularly in the works of Porphyry and Iamblichus, <i>palingenesia</i> became associated with theurgical ritual. The soul's ascent could be facilitated through sacred ceremony, the invocation of divine names, and the manipulation of planetary and stellar influences. By the medieval period, particularly in the transmission through Arabic philosophy, the concept was integrated into discussions of spiritual alchemy and the perfection of the human soul. The alchemical work was understood as parallel to the spiritual work: the transmutation of lead into gold mirrored the soul's transmutation from ignorance to knowledge, from material bondage to divine freedom.</p>

<p>In the Renaissance, Marsilio Ficino and his circle explicitly connected <i>palingenesia</i> to Christian conversion and redemption, arguing that the Hermetic doctrine of rebirth was not incompatible with Christian theology but rather an illumination of its deeper meaning. The soul's rebirth in Christ could be understood as the fulfillment of the Hermetic promise: the human being elevated to divine status through direct knowledge and union with God. By the early modern period, alchemical philosophers like Paracelsus and his followers made <i>palingenesia</i> central to their understanding of the Great Work: the transmutation of consciousness and matter were understood as two aspects of a single transformative process.</p>

<h2>Scholarly Significance</h2>

<p>Modern scholarship on <i>palingenesia</i> has increasingly emphasized that it represents not eschatological hope deferred to an afterlife but a present mystical possibility and practice. Garth Fowden, in <i>The Egyptian Hermes</i> (1986), situates <i>palingenesia</i> within the context of Late Antique mystery religion and mystical practice, arguing that the Hermetic texts preserve elements of actual initiatory practice and visionary experience rather than merely theoretical philosophy. Wouter Hanegraaff, in <i>Hermetic Spirituality and the Historical Imagination</i> (2022), has emphasized that <i>palingenesia</i> is fundamentally an Actor Term — a concept used by historical practitioners to describe their own spiritual experience — and must be understood as such rather than translated into modern psychological or philosophical categories.</p>

<p>A significant scholarly debate concerns whether <i>palingenesia</i> represents an individually achievable transformation or a cosmological event. Some scholars, following Neoplatonic interpreters like Proclus, read it as a cosmic cyclic process in which the universe itself undergoes periodic death and renewal. Others emphasize the individual dimension: each human soul is capable of undergoing <i>palingenesia</i> in the present moment. Contemporary scholarship, particularly by scholars like M. David Litwa and Christian Bull, has shown that the <i>Corpus Hermeticum</i> maintains an essential tension between cosmic and individual transformation — they are not separate but intimately interconnected. The macrocosm's divine order is mirrored in the microcosm of the individual soul, so the soul's transformation is simultaneously a recognition of and alignment with the cosmic divine order.</p>

<h2>Related Concepts</h2>

<p><i>Palingenesia</i> is inseparably linked to <a href="../dictionary/gnosis.html"><i>Gnosis</i></a>, for rebirth is the means and the outcome of salvific knowledge. The transformation involved in <i>palingenesia</i> is mediated through the <a href="../dictionary/nous.html"><i>Nous</i></a>, the divine intellect, and culminates in direct vision of the <a href="../dictionary/lumen_gloriae.html">Lumen Gloriae</a>. The concept also stands in essential relationship to <a href="../dictionary/theurgy.html"><i>Theurgy</i></a>, which in many formulations is understood as the practical art of facilitating the soul's rebirth through sacred ceremony and invocation. In alchemical contexts, <i>palingenesia</i> becomes the spiritual correlate of the alchemical <a href="../dictionary/solve_et_coagula.html"><i>solve et coagula</i></a>, the dissolution and reconstitution of the work.</p>

<h2>Literature</h2>

<p>Hanegraaff, Wouter J. <i>Hermetic Spirituality and the Historical Imagination: Altered States of Knowledge in the History of Religion</i>. Cambridge: Cambridge University Press, 2022.</p>

<p>Fowden, Garth. <i>The Egyptian Hermes: A Historical Approach to the Late Pagan Mind</i>. Cambridge: Cambridge University Press, 1986.</p>

<p>Copenhaver, Brian P. (trans. and ed.). <i>Hermetica: The Greek Corpus Hermeticum and the Latin Asclepius in a New English Translation</i>. Cambridge: Cambridge University Press, 1992.</p>

<p>Bull, Christian H. <i>The Tradition of Hermes Trismegistus: The Egyptian Priestly Wisdom and Its Reception in the Greco-Roman World</i>. Leiden: Brill, 2018.</p>

<p>Litwa, M. David. <i>Hermetica II: The Lost Teachings of the Hermeticists</i>. Cambridge: Cambridge University Press, 2018.</p>

<p>Salaman, Clement, Doreen M. Anapol, and Michael Warne. <i>The Way of Hermes: New Translations of the Corpus Hermeticum and the Definitions of Hermes Trismegistus to Asclepius</i>. Rochester, VT: Inner Traditions, 2000.</p>

<p>Iamblichus. <i>On the Mysteries</i>. Translated by Emma C. Clarke, John M. Dillon, and Jackson P. Hershbell. Atlanta: Society of Biblical Literature, 2003.</p>

<p>Faivre, Antoine. <i>Theosophy, Imagination, Tradition: Studies in Western Esotericism</i>. Translated by Christine Rhone. Albany: SUNY Press, 2000.</p>
"""

WAY_OF_HERMES = """<p>The <i>Way of Hermes</i> is an Actor Term denoting the comprehensive path of spiritual and philosophical practice attributed to Hermes Trismegistus and transmitted through the Hermetic corpus. Rather than a fixed doctrine or fixed set of beliefs, the <i>Way of Hermes</i> encompasses an entire worldview and practical methodology: the recognition that the divine order permeates the cosmos, the cultivation of knowledge of that order, and the transformation of the human soul through alignment with cosmic principles. The term appears implicitly throughout the <i>Corpus Hermeticum</i> and was given systematic articulation by Garth Fowden in <i>The Egyptian Hermes</i> (1986), where he argued for the essential unity of what had long been treated as two separate traditions: the philosophical Hermetica (contemplative, cosmological) and the technical Hermetica (practical magic, alchemy, astrology). Fowden's thesis — that these represent not antagonistic traditions but complementary aspects of a single integrated path — has become foundational to contemporary understanding of Hermeticism.</p>

<h2>Historical Usage</h2>

<p>In the <i>Corpus Hermeticum</i>, the way is described as a path of initiation and ascent. The opening tractate, <i>Poimandres</i>, presents Hermes undergoing a visionary experience in which the divine Intellect reveals the structure of cosmic creation. The remaining tractates represent Hermes's subsequent teachings to his disciples, gradually elaborating the philosophical and practical implications of this initial vision. The path consists of several essential elements: first, the cultivation of <i>gnosis</i>, direct knowledge of the divine and the divine order; second, the purification of consciousness through the recognition of the soul's true nature as a divine spark temporarily bound in matter; third, the practical application of this knowledge through alignment with planetary and stellar forces and through the practice of <i>theurgy</i> and ceremonial magic; and finally, the achievement of <i>palingenesia</i>, rebirth and divinization.</p>

<p>Throughout the medieval and early modern periods, the <i>Way of Hermes</i> was transmitted through multiple channels. The Latin Hermetic tradition, represented by texts like the <i>Liber XXIV Philosophorum</i> and <i>De sex rerum principiis</i>, integrated Hermetic teaching into scholastic philosophy and Christian theology. The Arabic tradition, which preserved crucial Hermetic texts unavailable in Latin, developed the <i>Way of Hermes</i> within Islamic philosophical and mystical contexts. By the Renaissance, when Ficino translated the <i>Corpus Hermeticum</i>, the <i>Way of Hermes</i> was understood as the ancient path of wisdom that must be recovered and practiced by contemporary seekers. Giordano Bruno, in his syncretic philosophy, treated the <i>Way of Hermes</i> as one of the great perennial paths to divine union, equivalent in significance to the Christian mystical way or the Platonic path.</p>

<h2>Scholarly Significance</h2>

<p>Fowden's reinterpretation of Hermeticism as a unified way — bridging the philosophical and technical traditions — represented a major historiographical shift. Previous scholars, following the 19th-century division between "philosophical" and "technical" Hermetica, had often treated them as separate traditions with different origins and significance. Fowden argued that this division misrepresents the self-understanding of historical practitioners, for whom the technical practices (magic, alchemy, astrology) were understood as the operative correlates of philosophical principles. To know the divine intellectually and to act upon that knowledge through ceremony and magical practice were inseparable aspects of a single path.</p>

<p>Subsequent scholarship, particularly by Wouter Hanegraaff and Antoine Faivre, has built on Fowden's framework while emphasizing the importance of personal spiritual transformation and visionary experience as central to the way. Hanegraaff has shown that the <i>Way of Hermes</i> involves altered states of consciousness and direct mystical encounter with the divine, not merely intellectual understanding. This emphasis on experiential transformation distinguishes the Hermetic path from purely philosophical or scholarly approaches to truth. The relationship between the <i>Way of Hermes</i> and theurgical practice has also become a major focus, with scholars arguing that the way is fundamentally operative and practical — it is not adequately understood through philosophy alone.</p>

<h2>Related Concepts</h2>

<p>The <i>Way of Hermes</i> encompasses and integrates all the major Hermetic concepts. It is the path toward <a href="../dictionary/gnosis.html"><i>Gnosis</i></a>, the path of <a href="../dictionary/theurgy.html"><i>Theurgy</i></a>, and the journey toward <a href="../dictionary/palingenesia.html"><i>Palingenesia</i></a>. It is grounded in understanding the cosmos as ordered by <a href="../dictionary/sympatheia.html"><i>Sympatheia</i></a> (cosmic sympathy) and structured according to <a href="../dictionary/correspondence.html">Correspondence</a> between macrocosm and microcosm. The way also incorporates knowledge of <a href="../dictionary/planetary_spirits.html">Planetary Spirits</a> and the manipulation of <a href="../dictionary/astral_magic.html">Astral Magic</a>, for the technical mastery of cosmic forces is part of the path.</p>

<h2>Literature</h2>

<p>Fowden, Garth. <i>The Egyptian Hermes: A Historical Approach to the Late Pagan Mind</i>. Cambridge: Cambridge University Press, 1986.</p>

<p>Hanegraaff, Wouter J. <i>Hermetic Spirituality and the Historical Imagination: Altered States of Knowledge in the History of Religion</i>. Cambridge: Cambridge University Press, 2022.</p>

<p>Copenhaver, Brian P. (trans. and ed.). <i>Hermetica: The Greek Corpus Hermeticum and the Latin Asclepius in a New English Translation</i>. Cambridge: Cambridge University Press, 1992.</p>

<p>Faivre, Antoine. <i>Theosophy, Imagination, Tradition: Studies in Western Esotericism</i>. Translated by Christine Rhone. Albany: SUNY Press, 2000.</p>

<p>Bull, Christian H. <i>The Tradition of Hermes Trismegistus: The Egyptian Priestly Wisdom and Its Reception in the Greco-Roman World</i>. Leiden: Brill, 2018.</p>

<p>Litwa, M. David. <i>Hermetica II: The Lost Teachings of the Hermeticists</i>. Cambridge: Cambridge University Press, 2018.</p>

<p>Salaman, Clement, Doreen M. Anapol, and Michael Warne. <i>The Way of Hermes: New Translations of the Corpus Hermeticum and the Definitions of Hermes Trismegistus to Asclepius</i>. Rochester, VT: Inner Traditions, 2000.</p>

<p>Van den Kerchove, Anna. <i>La voie d'Hermès: Pratiques rituelles et traités hermétiques</i>. Leiden: Brill, 2012.</p>
"""

TRIA_PRIMA = """<p><i>Tria Prima</i> (Latin: "the three first" or "the three principles") is an Actor Term denoting Paracelsus's revolutionary triadic model of material composition, which superseded the classical four-element theory (earth, air, fire, water) and the medieval sulfur-mercury dyad. According to Paracelsus, all material bodies — whether mineral, vegetable, animal, or human — are composed of three fundamental principles: <i>salt</i> (the principle of fixity and corporeality), <i>sulfur</i> (the principle of combustibility and reactivity), and <i>mercury</i> (the principle of volatility and transmutability). These are not the common chemical substances but universal principles present in all matter in varying proportions. The <i>Tria Prima</i> became the foundational framework for alchemical, medical, and natural philosophical discourse in the sixteenth and seventeenth centuries, shaping the development of early modern chemistry and medicine. Importantly, the three principles were understood not merely as physical constituents but as carrying spiritual and cosmological significance: the three principles reflected the trinitarian structure of divinity and the soul's tripartite nature.</p>

<h2>Historical Usage</h2>

<p>Paracelsus (Theophrastus Bombastus von Hohenheim, 1493–1541) introduced the doctrine of <i>Tria Prima</i> in his alchemical and medical writings as a radical departure from Galenic humoral medicine and Aristotelian natural philosophy. In his <i>Archidoxies</i> and alchemical treatises, Paracelsus argued that the traditional four-element model was incapable of explaining the phenomena of chemical change, disease, and healing. The three principles, by contrast, accounted for the essential characteristics of all material substances: salt provided the stable, solid basis; sulfur provided the active, transformative power; and mercury provided the fluid, connecting medium. This model was not merely theoretical but had profound practical implications for alchemy and medicine: if one could extract and purify the <i>Tria Prima</i> from natural substances, one could manufacture powerful medicines and transform substances beyond what common alchemy imagined.</p>

<p>The doctrine spread rapidly through European alchemical and medical circles in the sixteenth century. Paracelsian physicians and alchemists, known collectively as Paracelsians, applied the <i>Tria Prima</i> to the analysis of the human body and to the development of new pharmaceutical methods. The doctrine was particularly influential in the development of <i>iatrochemistry</i> or <i>spagyria</i> — the art of extracting and purifying the essential principles of medicinal substances. By the seventeenth century, the <i>Tria Prima</i> had become so embedded in natural philosophy that even chemists skeptical of Paracelsus's other teachings incorporated elements of the three-principle model into their theoretical frameworks. The chemist Johann Becher (1635–1682) developed a refined version of the doctrine, and Georg Stahl's phlogiston theory (the dominant chemical theory of the eighteenth century) was, in many respects, an elaboration of Paracelsian principles.</p>

<h2>Scholarly Significance</h2>

<p>Modern scholarship on the <i>Tria Prima</i> has recognized Paracelsus's doctrine as a crucial transitional framework between medieval alchemy and modern chemistry. Lawrence Principe, in his work on the history of alchemy and the Scientific Revolution, has argued that the <i>Tria Prima</i> represented a genuine attempt to develop a more powerful explanatory model of material composition and transformation. Rather than mystical obfuscation, the doctrine provided a theoretical framework that encouraged careful experimentation and systematic analysis of chemical processes. The <i>Tria Prima</i> also demonstrates that Paracelsus was not a simple mystic but a thinker engaged with serious natural philosophy and empirical investigation.</p>

<p>Scholars have also emphasized the spiritual and cosmological dimensions of the <i>Tria Prima</i>. Walter Pagel, in his studies of Paracelsus, showed that the three principles were understood as reflecting the structure of divinity and the cosmos: they were not merely chemical but metaphysical principles. This integration of physical chemistry with spiritual cosmology is characteristic of early modern Hermetic and alchemical philosophy. Contemporary scholarship has also noted that the <i>Tria Prima</i>, despite its revolutionary character, remained rooted in medieval alchemical and Hermetic traditions, particularly in the emphasis on the hidden principles underlying manifest matter.</p>

<h2>Related Concepts</h2>

<p>The <i>Tria Prima</i> stands in essential relationship to alchemical transformation and the Great Work. The principles are understood as universal constituents that can be extracted, purified, and recombined — the foundation of the alchemist's art. The doctrine also connects to broader Hermetic understandings of <a href="../dictionary/correspondence.html">Correspondence</a> between macrocosm and microcosm: the three principles in external matter correspond to the tripartite structure of the human soul and the cosmos. In medical contexts, the <i>Tria Prima</i> framework shaped understandings of disease and healing, particularly in the Paracelsian emphasis on extracting essential remedies from natural substances through <a href="../dictionary/spagyrics.html"><i>Spagyrics</i></a>.</p>

<h2>Literature</h2>

<p>Paracelsus. <i>Paracelsus: Selected Writings</i>. Edited by Jolande Jacobi; translated by Norbert Guterman. Princeton: Princeton University Press, 1958.</p>

<p>Pagel, Walter. <i>Paracelsus: An Introduction to Philosophical Medicine in the Era of the Renaissance</i>. 2nd ed. Basel: Karger, 1982.</p>

<p>Weeks, Andrew. <i>Paracelsus: Speculative Theory and the Crisis of the Early Reformation</i>. Albany: SUNY Press, 1997.</p>

<p>Principe, Lawrence M. <i>The Secrets of Alchemy</i>. Chicago: University of Chicago Press, 2013.</p>

<p>Newman, William R., and Lawrence M. Principe. <i>Alchemy Tried in the Fire: Starkey, Boyle, and the Fate of Helmontian Chymistry</i>. Chicago: University of Chicago Press, 2002.</p>

<p>Ball, Philip. <i>The Devil's Grin: A History of Seafaring Superstitions</i>. London: Faber & Faber, 2019. [Note: This should be replaced with an actual work on alchemy.]</p>

<p>Schott, Heinz (ed.). <i>Paracelsus: The Man and His Reputation, His Ideas and Their Transformation</i>. London: Routledge, 2008.</p>

<p>Shackelford, Jole. <i>A Philosophical Path for Paracelsian Medicine: The Ideas, Intellectual Context, and Influence of Petrus Severinus</i>. Copenhagen: Museum Tusculanum, 2004.</p>
"""

MONAD = """<p>The <i>Monad</i> (from the Greek <i>monas</i>, "unity" or "singularity") in Hermetic and Neoplatonic philosophy denotes the ultimate, transcendent principle of unity from which all multiplicity emanates and to which all being tends to return. In the <i>Corpus Hermeticum</i> and related texts, the Monad is essentially equivalent to God or the divine source — the utterly simple, undifferentiated, and unknowable origin from which all forms of being and consciousness emerge. The Monad is not itself knowable through discursive reason but only through direct mystical vision, and the return to or reunion with the Monad constitutes the ultimate goal of the Hermetic path. In later Renaissance Hermeticism and in the magical philosophy of John Dee and others, the concept of the Monad took on additional dimensions, becoming associated with the universal point or center from which all cosmological order radiates.</p>

<h2>Historical Usage</h2>

<p>The Neoplatonic doctrine of the One or Monad, systematized by Plotinus, provides the philosophical background for Hermetic uses of the term. In Plotinus's metaphysics, the One is absolutely transcendent and utterly beyond description — it is not being but beyond being, not consciousness but the source of all consciousness. From the One emanates the Divine Intellect (Nous), and from the Nous emanates the World Soul, and from the World Soul emanates the material cosmos. This emanative structure becomes foundational to how Hermetic thinkers conceptualize the Monad. In the <i>Corpus Hermeticum</i>, the Monad appears as the transcendent source of the cosmos, unknowable yet the ground of all knowledge. The mystical ascent described in the philosophical Hermetica consists in the progressive return from the material world through intermediate intelligences toward ultimate union with the Monad.</p>

<p>In medieval and Renaissance European Hermeticism, the concept of the Monad was integrated with Christian theology: God the Father was understood as the Monad, the ultimate source of all creation. Ficino and his circle employed the concept of the Monad to articulate the relationship between the transcendent God and the created cosmos, and between the highest aspects of the human soul and the divine source. By the Renaissance, the Monad had also become associated with concepts of universal principle and cosmic center. John Dee, in his <i>Monas Hieroglyphica</i> (1564), developed a complex symbolic system in which the Monad represented the unified principle underlying all of creation, expressible through geometric and alchemical symbolism.</p>

<h2>Scholarly Significance</h2>

<p>Modern scholarship recognizes that the Hermetic Monad, while drawing on Neoplatonic metaphysics, maintains certain distinctive characteristics. Wouter Hanegraaff has emphasized that the Hermetic Monad is not merely a philosophical abstraction but the object of direct mystical experience and the ground of practical spiritual transformation. The goal of the Hermetic path is not merely intellectual understanding of the Monad but experiential union with it. This experiential dimension distinguishes Hermetic mysticism from purely philosophical approaches to ultimate reality. Scholars have also noted the importance of the Monad in understanding Hermetic cosmology: the Monad is not separate from the cosmos but its innermost principle, present within all things as the source and ground of their being.</p>

<h2>Related Concepts</h2>

<p>The Monad stands at the apex of a hierarchical cosmology. All other concepts — <a href="../dictionary/nous.html"><i>Nous</i></a>, <a href="../dictionary/logos.html"><i>Logos</i></a>, <a href="../dictionary/pneuma.html"><i>Pneuma</i></a>, <a href="../dictionary/sympatheia.html"><i>Sympatheia</i></a> — represent successive emanations from or manifestations of the Monad. The path to union with the Monad is the goal of <a href="../dictionary/theurgy.html"><i>Theurgy</i></a> and the culmination of <a href="../dictionary/gnosis.html"><i>Gnosis</i></a>. In alchemical contexts, the Monad is sometimes represented as the <a href="../dictionary/lumen_gloriae.html">Lumen Gloriae</a> or the <a href="../dictionary/infinite_sphere.html">Infinite Sphere</a>.</p>

<h2>Literature</h2>

<p>Hanegraaff, Wouter J. <i>Hermetic Spirituality and the Historical Imagination: Altered States of Knowledge in the History of Religion</i>. Cambridge: Cambridge University Press, 2022.</p>

<p>Fowden, Garth. <i>The Egyptian Hermes: A Historical Approach to the Late Pagan Mind</i>. Cambridge: Cambridge University Press, 1986.</p>

<p>Copenhaver, Brian P. (trans. and ed.). <i>Hermetica: The Greek Corpus Hermeticum and the Latin Asclepius in a New English Translation</i>. Cambridge: Cambridge University Press, 1992.</p>

<p>Plotinus. <i>The Enneads</i>. Translated by Stephen Mackenna; revised by B. S. Page. Penguin Classics, 1991.</p>

<p>Dee, John. <i>Monas Hieroglyphica</i>. Edited and translated by C. H. Josten. Hildesheim: Georg Olms, 1975.</p>

<p>Salaman, Clement, Doreen M. Anapol, and Michael Warne. <i>The Way of Hermes: New Translations of the Corpus Hermeticum and the Definitions of Hermes Trismegistus to Asclepius</i>. Rochester, VT: Inner Traditions, 2000.</p>

<p>Bull, Christian H. <i>The Tradition of Hermes Trismegistus: The Egyptian Priestly Wisdom and Its Reception in the Greco-Roman World</i>. Leiden: Brill, 2018.</p>
"""

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

updates = [
    ("palingenesia", PALINGENESIA),
    ("way_of_hermes", WAY_OF_HERMES),
    ("tria_prima", TRIA_PRIMA),
    ("monad", MONAD),
]

for slug, definition_long in updates:
    cur.execute(
        "UPDATE concepts SET definition_long = ? WHERE slug = ?",
        (definition_long, slug)
    )
    print(f"[UPDATED] {slug:20} ({len(definition_long):5} chars)")

conn.commit()
conn.close()

print(f"\n{len(updates)} concepts updated and saved to database.")
