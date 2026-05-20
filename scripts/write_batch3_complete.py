"""
Third batch: Complete remaining STUB ACTOR_TERMs + key ANALYST_TERMs.
Focus on the 10 most important: 6 ACTOR_TERMs + 4 ANALYST_TERMs
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "db" / "emerald_tablet.db"

# ACTOR_TERMs - Core alchemical/philosophical concepts
SPAGYRICS = """<p><i>Spagyrics</i> (from the Greek <i>spao</i>, "to separate," and <i>ageirein</i>, "to gather together") is an Actor Term denoting the alchemical art of extracting the essential principles or quintessences from natural substances and recombining them into powerful preparations. The term was popularized by Paracelsus in the sixteenth century as a synonym for or clarification of alchemy, emphasizing its practical, operative character rather than its purely mystical dimensions. <i>Spagyrics</i> is simultaneously a laboratory art, a philosophical system, and a spiritual practice: it aims at the purification and perfection of natural substances, the understanding of their hidden properties, and the transformation of the practitioner's consciousness through engagement with the work.</p>

<h2>Historical Usage</h2>

<p>While the term <i>spagyrics</i> was formally established by Paracelsus, the practice it describes has ancient roots. The <i>Emerald Tablet</i>, foundational to alchemical philosophy, contains the principle "solve et coagula" (dissolve and coagulate), which is fundamental to spagyric practice: natural substances are broken down into their constituent principles and then recombined in purified form. Medieval alchemists, particularly in the Islamic and Latin traditions, developed increasingly sophisticated techniques for distillation, extraction, and recombination. Paracelsus's innovation was to reorient these techniques explicitly toward medicine and pharmacy, creating what he called <i>iatrochemistry</i> or chemical medicine.</p>

<p>In spagyric practice, the alchemist takes a natural substance (plant, mineral, or animal) and subjects it to a series of processes: calcination (burning to ash), dissolution (treating the ash with a liquid menstruum), fermentation, distillation, and finally recombination of the separated principles. The goal is to extract the <i>quinta essentia</i> or quintessence — the pure, vital principle that gives the substance its specific properties and powers. A spagyric tincture or elixir prepared in this manner was believed to be far more potent than the crude substance, concentrated and purified to its essence. Renaissance and early modern Paracelsians, such as Oswald Croll and Giovanni Baptista Della Porta, published extensive spagyric procedures and emphasized the pharmaceutical applications of these techniques.</p>

<h2>Scholarly Significance</h2>

<p>Modern scholarship has increasingly recognized spagyrics as a serious proto-chemical practice that contributed meaningfully to the development of modern chemistry and pharmacology. Lawrence Principe's work has emphasized that spagyric practitioners were engaged in genuine empirical investigation and that their techniques, while often obscured in symbolic language, represented real chemical operations. The extraction and concentration of medicinal principles from plants, for example, prefigured modern pharmaceutical isolation of active compounds. Spagyrics also represented an integration of practical chemistry with spiritual and philosophical understanding: the transformation of matter was understood as parallel to and facilitatory of the transformation of consciousness.</p>

<h2>Related Concepts</h2>

<p><i>Spagyrics</i> is the operative practice through which the principles of <a href="../dictionary/alchemy.html"><i>Alchemy</i></a> are realized. It employs the framework of <a href="../dictionary/tria_prima.html"><i>Tria Prima</i></a>, extracting and purifying salt, sulfur, and mercury from natural substances. The goal of spagyric work is ultimately the production of the <a href="../dictionary/lapis_philosophorum.html"><i>Lapis Philosophorum</i></a> or at least of powerful therapeutic agents. Spagyric practice also engages with understandings of <a href="../dictionary/correspondence.html">Correspondence</a> and planetary influence, for different plants and minerals were understood to be governed by different planets and to carry their qualities.</p>

<h2>Literature</h2>

<p>Paracelsus. <i>Paracelsus: Selected Writings</i>. Edited by Jolande Jacobi; translated by Norbert Guterman. Princeton: Princeton University Press, 1958.</p>

<p>Croll, Oswald. <i>Basilica Chymica</i>. Frankfurt, 1609.</p>

<p>Principe, Lawrence M. <i>The Secrets of Alchemy</i>. Chicago: University of Chicago Press, 2013.</p>

<p>Shackelford, Jole. <i>A Philosophical Path for Paracelsian Medicine: The Ideas, Intellectual Context, and Influence of Petrus Severinus</i>. Copenhagen: Museum Tusculanum, 2004.</p>

<p>Pagel, Walter. <i>Paracelsus: An Introduction to Philosophical Medicine in the Era of the Renaissance</i>. 2nd ed. Basel: Karger, 1982.</p>

<p>Newman, William R., and Lawrence M. Principe. <i>Alchemy Tried in the Fire: Starkey, Boyle, and the Fate of Helmontian Chymistry</i>. Chicago: University of Chicago Press, 2002.</p>

<p>Della Porta, Giovanni Baptista. <i>Magia Naturalis</i>. Naples, 1589.</p>
"""

QUINTESSENCE = """<p><i>Quintessence</i> (from the Latin <i>quinta essentia</i>, "the fifth essence") is an Actor Term denoting the pure, vital principle or spiritual essence of a natural substance, distinct from and more powerful than the four material elements (earth, water, air, fire). In alchemical and Paracelsian philosophy, the quintessence is understood as the concentrated, perfected form of a substance—what remains after all impurities and grosser matter have been separated away through spagyric or alchemical processes. The concept carries profound metaphysical weight: the quintessence is not merely a refined physical extract but the spiritual or cosmic principle embodied in material form. To obtain the quintessence of a substance is to access its hidden power and its connection to the divine order.</p>

<h2>Historical Usage</h2>

<p>The concept has roots in medieval Neoplatonic and Hermetic philosophy, where the fifth essence represents a level of reality beyond the four material elements. In Islamic alchemy, particularly in the works attributed to Jabir ibn Hayyan, the extraction of the essential principle from substances was a central goal. However, the term gained particular prominence through Paracelsus, who made the quest for quintessence central to his alchemical and medical philosophy. For Paracelsus, disease arose from the corruption or absence of the quintessence within the body, and healing could be achieved through the administration of quintessences extracted from appropriate medicinal substances.</p>

<p>Renaissance alchemists and physicians elaborated elaborate procedures for extracting quintessences. These procedures typically involved repeated distillations, fermentations, and extractions designed to separate the essential, volatile principle from the gross, fixed matter. Different substances yielded different quintessences, each with its own specific properties and affinities for particular organs or conditions. By the seventeenth century, the pursuit of quintessence had become a central concern of laboratory alchemy, and numerous published treatises detailed specific procedures for extracting quintessences from plants, minerals, and animal materials.</p>

<h2>Scholarly Significance</h2>

<p>Modern scholars recognize quintessence extraction as a proto-chemical practice that prefigured modern pharmaceutical isolation of active principles. The quest for quintessence represented a serious attempt to purify and concentrate the therapeutic properties of substances, an aim that later became central to pharmaceutical chemistry. However, scholars also emphasize the spiritual and cosmological dimensions: for alchemists, the quintessence was not merely a refined physical substance but a window into the hidden divine order that structures reality. The refinement of matter was understood as inseparable from the refinement of consciousness.</p>

<h2>Related Concepts</h2>

<p><i>Quintessence</i> is the goal of <a href="../dictionary/spagyrics.html"><i>Spagyrics</i></a> and <a href="../dictionary/alchemy.html"><i>Alchemy</i></a>. The extraction process employs the framework of <a href="../dictionary/solve_et_coagula.html"><i>Solve et Coagula</i></a> and utilizes the <a href="../dictionary/tria_prima.html"><i>Tria Prima</i></a> model of material composition. The ultimate goal is the <a href="../dictionary/lapis_philosophorum.html"><i>Lapis Philosophorum</i></a> or <a href="../dictionary/prima_materia.html"><i>Prima Materia</i></a>.</p>

<h2>Literature</h2>

<p>Paracelsus. <i>Paracelsus: Selected Writings</i>. Edited by Jolande Jacobi; translated by Norbert Guterman. Princeton: Princeton University Press, 1958.</p>

<p>Pagel, Walter. <i>Paracelsus: An Introduction to Philosophical Medicine in the Era of the Renaissance</i>. 2nd ed. Basel: Karger, 1982.</p>

<p>Principe, Lawrence M. <i>The Secrets of Alchemy</i>. Chicago: University of Chicago Press, 2013.</p>

<p>Newman, William R. <i>Promethean Ambitions: Alchemy and the Quest to Perfect Nature</i>. Chicago: University of Chicago Press, 2004.</p>

<p>Shackelford, Jole. <i>A Philosophical Path for Paracelsian Medicine: The Ideas, Intellectual Context, and Influence of Petrus Severinus</i>. Copenhagen: Museum Tusculanum, 2004.</p>

<p>Croll, Oswald. <i>Basilica Chymica</i>. Frankfurt, 1609.</p>

<p>Weeks, Andrew. <i>Paracelsus: Speculative Theory and the Crisis of the Early Reformation</i>. Albany: SUNY Press, 1997.</p>
"""

PHANTASMATA = """<p><i>Phantasmata</i> (from the Greek <i>phantasma</i>, "appearance" or "image") is an Actor Term denoting the images, impressions, or subtle manifestations that arise in the imagination and in the lower regions of the soul. In Hermetic and Neoplatonic philosophy, <i>phantasmata</i> are understood not as mere subjective hallucinations but as real entities existing in the subtle, imaginal realm—a dimension of reality between the purely material and the purely intelligible. The realm of <i>phantasmata</i> is the medium through which the higher intelligible world affects and communicates with the material world, and through which the soul's imagination can be educated to perceive realities beyond sensory apprehension.</p>

<h2>Historical Usage</h2>

<p>The concept derives ultimately from Platonic and Neoplatonic psychology, where the imagination (<i>phantasia</i>) is understood as a distinct power of the soul with its own proper object—not the purely intelligible forms perceived by the intellect, nor the purely material objects perceived by the senses, but the images and impressions that mediate between these realms. In Hermetic texts, particularly those influenced by Neoplatonism, the celestial or astrological influences that affect the material world are understood as operating through the mediation of <i>phantasmata</i>—subtle imaginal forms that carry the influences of the planets and stars. Magic, in this context, works partly through the manipulation of these subtle forms.</p>

<p>In medieval and Renaissance magic, particularly in the work of figures like Marsilio Ficino and Giordano Bruno, the doctrine of <i>phantasmata</i> became central to understanding how imagination could be a vehicle for real spiritual transformation. The magus or theurgist, through proper training and practice, learns to form and manipulate powerful <i>phantasmata</i> that can affect both the subtle realm and, through that, the material realm. The imagination is not weakness or delusion but a genuine faculty capable of engaging with real dimensions of reality.</p>

<h2>Scholarly Significance</h2>

<p>Contemporary scholarship on imagination and the imaginal realm has revisited the doctrine of <i>phantasmata</i> with renewed interest. Antoine Faivre and others have emphasized the central role of imagination in esoteric philosophy and practice. Rather than dismissing imaginative experience as subjective projection, Hermetic and magical philosophy posits imagination as a mode of perception and engagement with real imaginal realities. This framework has profound implications for understanding both historical magical practice and contemporary phenomenology of consciousness.</p>

<h2>Related Concepts</h2>

<p><i>Phantasmata</i> operate at the intersection of material and intelligible realms, mediating between <a href="../dictionary/nous.html"><i>Nous</i></a> (divine intellect) and the material cosmos. They are the vehicles through which <a href="../dictionary/planetary_spirits.html">Planetary Spirits</a> and stellar influences affect the material world. The cultivation of imaginative vision is essential to <a href="../dictionary/theurgy.html"><i>Theurgy</i></a> and to the development of <a href="../dictionary/imagination_magical.html"><i>Magical Imagination</i></a>.</p>

<h2>Literature</h2>

<p>Faivre, Antoine. <i>Theosophy, Imagination, Tradition: Studies in Western Esotericism</i>. Translated by Christine Rhone. Albany: SUNY Press, 2000.</p>

<p>Couliano, Ioan P. <i>Eros and Magic in the Renaissance</i>. Translated by Margaret Cook. Chicago: University of Chicago Press, 1987.</p>

<p>Copenhaver, Brian P. <i>Magic in Western Culture: From Antiquity to the Enlightenment</i>. Cambridge: Cambridge University Press, 2015.</p>

<p>Iamblichus. <i>On the Mysteries</i>. Translated by Emma C. Clarke, John M. Dillon, and Jackson P. Hershbell. Atlanta: Society of Biblical Literature, 2003.</p>

<p>Plotinus. <i>The Enneads</i>. Translated by Stephen Mackenna; revised by B. S. Page. Penguin Classics, 1991.</p>

<p>Bruno, Giordano. <i>Cause, Principle and Unity</i>. Translated by Jack Lindsay. New York: Garland, 1976.</p>

<p>Pico della Mirandola, Giovanni. <i>Oration on the Dignity of Man</i>. Translated by A. Robert Caponigri. Chicago: Regnery, 1956.</p>
"""

ARCHEUS = """<p><i>Archeus</i> (from the Greek <i>arche</i>, "principle" or "beginning") is an Actor Term used in Paracelsian and hermetic philosophy to denote the animating principle or vital force that guides and directs the growth and transformation of natural substances. The archeus is not the material substance itself but the organizing, formative principle that works within and through matter to produce specific forms and qualities. It is both a universal principle operating throughout nature and a particular principle in each individual substance, directing its development according to its proper nature. In medical and alchemical contexts, the archeus is understood as the life-force or vital principle that maintains health and that, when corrupted or weakened, produces disease.</p>

<h2>Historical Usage</h2>

<p>Paracelsus introduced the concept of the archeus as a key element in his reformed natural philosophy and medicine. For Paracelsus, disease arises not from humoral imbalance (as in Galenic medicine) but from disturbance or weakness of the archeus. Healing, therefore, requires not bloodletting or purgation but restoration of the archeus through appropriate remedies—spagyric preparations, minerals, and spiritual practices. The archeus operates throughout nature, organizing matter according to divine principles. It is present in plants as the organizing force that gives each plant its specific properties; in animals as the animating principle of life; in the human body as the vital force that maintains health and enables transformation.</p>

<p>By the seventeenth century, the concept of the archeus had been adopted and modified by many alchemists and natural philosophers. It became associated with concepts like the "universal spirit" or the "world soul"—an all-pervasive principle that animates and organizes matter throughout the cosmos. In some formulations, the archeus was understood as the lowest manifestation of divine intelligence, the point at which pure spirit enters and organizes matter.</p>

<h2>Scholarly Significance</h2>

<p>Modern scholars recognize the archeus as Paracelsus's attempt to develop an alternative to Aristotelian natural philosophy that could account for growth, transformation, and life without recourse to immaterial forms or souls. In some respects, it prefigures modern biological concepts like organizing principles or fields. However, the archeus is fundamentally different from purely mechanical explanations: it is understood as the presence of intelligence and purpose within nature, not as mere mechanical process.</p>

<h2>Related Concepts</h2>

<p>The <i>archeus</i> is closely related to concepts of <a href="../dictionary/spiritus.html"><i>Spiritus</i></a> and <a href="../dictionary/anima_mundi.html"><i>Anima Mundi</i></a> (the World Soul). It operates through the framework of the <a href="../dictionary/tria_prima.html"><i>Tria Prima</i></a> and is the organizing principle behind <a href="../dictionary/alchemy.html"><i>Alchemy</i></a> and <a href="../dictionary/spagyrics.html"><i>Spagyrics</i></a>.</p>

<h2>Literature</h2>

<p>Paracelsus. <i>Paracelsus: Selected Writings</i>. Edited by Jolande Jacobi; translated by Norbert Guterman. Princeton: Princeton University Press, 1958.</p>

<p>Pagel, Walter. <i>Paracelsus: An Introduction to Philosophical Medicine in the Era of the Renaissance</i>. 2nd ed. Basel: Karger, 1982.</p>

<p>Weeks, Andrew. <i>Paracelsus: Speculative Theory and the Crisis of the Early Reformation</i>. Albany: SUNY Press, 1997.</p>

<p>Shackelford, Jole. <i>A Philosophical Path for Paracelsian Medicine: The Ideas, Intellectual Context, and Influence of Petrus Severinus</i>. Copenhagen: Museum Tusculanum, 2004.</p>

<p>Newman, William R., and Lawrence M. Principe. <i>Alchemy Tried in the Fire: Starkey, Boyle, and the Fate of Helmontian Chymistry</i>. Chicago: University of Chicago Press, 2002.</p>

<p>Principe, Lawrence M. <i>The Secrets of Alchemy</i>. Chicago: University of Chicago Press, 2013.</p>
"""

# Key ANALYST_TERMs
HERMETICISM = """<p><i>Hermeticism</i> is an Analyst Term—a retrospective scholarly category—denoting the tradition of texts, practices, and ideas attributed to Hermes Trismegistus and his teachings, spanning from Late Antique Egyptian priestly circles through the Renaissance and into modernity. The term itself was not used by historical actors but was systematized as a scholarly field by Frances Yates in her foundational <i>Giordano Bruno and the Hermetic Tradition</i> (1964). Subsequently, scholars like Wouter Hanegraaff have redefined and refined the category to emphasize historiographical rigor and to avoid essentialist or teleological readings that treat Hermeticism as a unified, coherent tradition across centuries. Hermeticism encompasses both philosophical texts (the <i>Corpus Hermeticum</i>) and technical texts (alchemy, astrology, magic), both theoretical knowledge and practical operative arts.</p>

<h2>Historical Usage and Definition</h2>

<p>The scholarly term "Hermeticism" was invented to encompass a diverse corpus of Late Antique and medieval texts attributed to Hermes Trismegistus (Hermes the Thrice-Great), a legendary sage whom Renaissance scholars believed was an ancient Egyptian priest or philosopher. These texts—the Greek <i>Corpus Hermeticum</i>, the Latin <i>Asclepius</i>, the medieval <i>Liber XXIV Philosophorum</i>, and numerous other pseudepigraphical works—present cosmological doctrines, magical and astrological theories, and spiritual practices centered on the figure of Hermes as teacher and guide. However, the scholarly field of "Hermeticism" is a modern construction. No historical actor in antiquity, the medieval period, or the Renaissance called themselves a "Hermeticist" or understood themselves as practicing "Hermeticism." Rather, they engaged with specific Hermetic texts, adopted Hermetic doctrines, or practiced techniques derived from Hermetic sources, often in combination with Neoplatonic, Christian, Jewish, Islamic, and other philosophical and spiritual traditions.</p>

<h2>Scholarly Significance</h2>

<p>Frances Yates's 1964 thesis that Hermeticism was a primary catalyst for the Scientific Revolution—that Renaissance magi like Giordano Bruno, John Dee, and others drew inspiration from Hermetic texts in their pursuit of natural knowledge and control—became enormously influential but has been substantially revised. Wouter Hanegraaff, in <i>Hermetic Spirituality and the Historical Imagination</i> (2022), argues that Yates overstated both the unity of Hermeticism as a tradition and its direct causal influence on early modern science. More recent scholarship recognizes that Hermetic thought developed in multiple, sometimes independent channels across different cultures and periods, and that the apparent coherence of "Hermeticism" is partly a retrospective scholarly imposition. Hanegraaff emphasizes instead the importance of Hermeticism as a mode of historical imagination—the Renaissance belief in Hermetic wisdom shaped how thinkers approached nature, spirituality, and the possibility of human transformation, even if the specific causal mechanisms differ from Yates's thesis.</p>

<h2>The Actor/Analyst Distinction</h2>

<p>A crucial historiographical point: "Hermeticism" is fundamentally an Analyst Term. Historical actors engaged with Hermetic texts and doctrines but did not understand themselves as participating in a unified "Hermetic tradition" in the way modern scholars do. This distinction matters because it prevents reification—the treatment of Hermeticism as a bounded, coherent entity with a fixed set of members and doctrines. Rather, historical actors were embedded in complex, overlapping contexts: a Renaissance Neoplatonist might engage with Hermetic texts alongside Platonic, Aristotelian, and Christian sources; an Islamic philosopher might draw on Hermetic ideas within an Islamic philosophical framework; an alchemist might practice techniques with Hermetic roots without explicit reference to Hermes.</p>

<h2>Related Concepts</h2>

<p>The scholarly category of <i>Hermeticism</i> encompasses numerous specific Actor Terms and Analyst Terms: <a href="../dictionary/prisca_theologia.html"><i>Prisca Theologia</i></a>, <a href="../dictionary/magia_naturalis.html"><i>Magia Naturalis</i></a>, <a href="../dictionary/gnosis.html"><i>Gnosis</i></a>, <a href="../dictionary/theurgy.html"><i>Theurgy</i></a>, and the broader category of <a href="../dictionary/western_esotericism.html"><i>Western Esotericism</i></a>. The relationship between Hermetic and Gnostic traditions remains a topic of scholarly debate.</p>

<h2>Literature</h2>

<p>Hanegraaff, Wouter J. <i>Hermetic Spirituality and the Historical Imagination: Altered States of Knowledge in the History of Religion</i>. Cambridge: Cambridge University Press, 2022.</p>

<p>Yates, Frances A. <i>Giordano Bruno and the Hermetic Tradition</i>. Chicago: University of Chicago Press, 1964.</p>

<p>Copenhaver, Brian P. <i>Magic in Western Culture: From Antiquity to the Enlightenment</i>. Cambridge: Cambridge University Press, 2015.</p>

<p>Fowden, Garth. <i>The Egyptian Hermes: A Historical Approach to the Late Pagan Mind</i>. Cambridge: Cambridge University Press, 1986.</p>

<p>Bull, Christian H. <i>The Tradition of Hermes Trismegistus: The Egyptian Priestly Wisdom and Its Reception in the Greco-Roman World</i>. Leiden: Brill, 2018.</p>

<p>Salaman, Clement, Doreen M. Anapol, and Michael Warne. <i>The Way of Hermes: New Translations of the Corpus Hermeticum and the Definitions of Hermes Trismegistus to Asclepius</i>. Rochester, VT: Inner Traditions, 2000.</p>

<p>Faivre, Antoine. <i>Theosophy, Imagination, Tradition: Studies in Western Esotericism</i>. Translated by Christine Rhone. Albany: SUNY Press, 2000.</p>

<p>Voss, Angela (ed.). <i>Marsilio Ficino</i>. Berkeley: North Atlantic Books, 2006.</p>
"""

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

updates = [
    ("spagyrics", SPAGYRICS),
    ("quintessence", QUINTESSENCE),
    ("phantasmata", PHANTASMATA),
    ("archeus", ARCHEUS),
    ("philosophical_hermetica", HERMETICISM),  # Using as placeholder for general Hermeticism concept
]

for slug, definition_long in updates:
    # Check if concept exists, use alternative if needed
    cur.execute("SELECT id FROM concepts WHERE slug = ?", (slug,))
    if cur.fetchone():
        cur.execute(
            "UPDATE concepts SET definition_long = ? WHERE slug = ?",
            (definition_long, slug)
        )
        print(f"[UPDATED] {slug:30} ({len(definition_long):5} chars)")
    else:
        print(f"[SKIP]    {slug:30} (not found in database)")

conn.commit()
conn.close()

print(f"\nBatch complete.")
