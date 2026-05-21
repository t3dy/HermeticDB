#!/usr/bin/env python3
"""
Expand Corpus Hermeticum tractate analyses.
All CH tractates share a structural template; individual tractates vary in content focus.
"""
import sqlite3
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

DB_PATH = Path(__file__).parent.parent / "db" / "emerald_tablet.db"

# Analyses for individual CH tractates
# Each follows the standard structure: opening para, Content and Doctrine, Transmission, Modern Scholarship, Literature
CH_ANALYSES = {
    "ch_i_poimandres": """<p>The <i>Poimandres</i>, the first tractate of the Corpus Hermeticum, stands as the most philosophically sophisticated and influential Hermetic text, presenting a vision of divine emanation, cosmic order, and human redemption that became foundational to all subsequent Hermetic philosophy. Composed in Greek, likely in Egypt during the first or second century CE, the <i>Poimandres</i> ("the shepherd of men") presents itself as a revelation received by Hermes Trismegistus from the divine intellect. The tractate's vision of the cosmos as animated by a single divine principle and humanity's capacity for knowledge and ascent through contemplation directly influenced Neoplatonism, early Christianity, and all subsequent Western esotericism.</p>

<h2>Content and Doctrine</h2>
<p>The <i>Poimandres</i> begins with a vision in which Hermes, in a state of receptive contemplation, encounters a luminous being of immense size and brilliance, whom he identifies as the <i>Nous</i>, the divine intellect or mind that stands closest to the divine monad. This <i>Nous</i> reveals to Hermes the origin and structure of the cosmos: all things emanate from the transcendent god through a series of intermediary principles. The god first manifests as light, which separates from darkness; this duality generates all subsequent creation. The divine <i>Nous</i> then creates the Demiurge (the craftsman-god), who in turn orders the material cosmos. Humanity occupies a unique position in this cosmic hierarchy: the divine Intellect formed humans in its own image, endowing them with the capacity for knowledge and unity with the divine. Yet humans, distracted by material concerns and bodily desires, fall into ignorance and death. The tractate concludes with the promise of salvation through knowledge (<i>gnosis</i>) — the recovery of one's divine nature through intellectual contemplation and moral purification.</p>

<h2>Transmission and Manuscript Tradition</h2>
<p>The <i>Poimandres</i> survives primarily in Greek manuscripts and in fragmentary quotations in Christian authors, particularly Lactantius and Clement of Alexandria. The most important Greek manuscript tradition descends from a single archetype from the medieval period; modern critical editions, including Nock and Festugière's standard edition, establish the text with reasonable confidence. Marsilio Ficino's Latin translation of the <i>Poimandres</i> (the <i>Pimander</i>, completed in 1463) remained the standard European version for over a century. The Renaissance reception of the <i>Poimandres</i> emphasized its metaphysical sophistication and treated it as the voice of primordial wisdom predating Plato. Modern translations exist in English (Copenhaver's Cambridge edition, 1992) and most major European languages.</p>

<h2>Modern Scholarship</h2>
<p>Modern scholars have situated the <i>Poimandres</i> within late antique religious syncretism, demonstrating its debt to Platonic and Stoic philosophy while recognizing its engagement with Jewish mysticism and proto-Gnostic cosmology. Garth Fowden's <i>The Egyptian Hermes</i> (1986) and Brian P. Copenhaver's <i>Hermetica</i> (1992) have established the standard scholarly approach: reading the <i>Poimandres</i> as evidence for complex intellectual exchange in the Hellenistic Mediterranean world, rather than as the voice of ancient Egyptian wisdom. The tractate's Gnostic affinities have been debated; contemporary scholarship tends to emphasize its distinctness from Gnostic systems, particularly in its affirmation of material creation as fundamentally good and its emphasis on human knowledge rather than redemption from a malevolent demiurge.</p>

<h2>Literature</h2>
<p>Copenhaver, Brian P. <i>Hermetica: The Greek Corpus Hermeticum and the Latin Asclepius in a New English Translation</i>. Cambridge: Cambridge University Press, 1992.</p>
<p>Fowden, Garth. <i>The Egyptian Hermes: A Historical Approach to the Late Pagan Mind</i>. Cambridge: Cambridge University Press, 1986.</p>
<p>Festugière, A. J. <i>La Révélation d'Hermès Trismégiste</i>. 4 vols. Paris: Librairie Lecoffre, 1944–1954.</p>
<p>Litwa, M. David. <i>Hermetica II: The Latin Asclepius and the Greek Corpus Hermeticum XIII, with Coptic Texts</i>. Cambridge: Cambridge University Press, 2018.</p>
<p>Mahé, Jean-Pierre. <i>Hermès en Haute-Égypte</i>. 2 vols. Québec: Presses de l'Université Laval, 1982.</p>""",

    "ch_iv_krater": """<p>The <i>Krater</i> (Mixing Bowl) tractate, the fourth of the Corpus Hermeticum, presents one of the most systematically developed cosmological images in Hermetic thought: the vision of God pouring divinity into a great mixing bowl (krater) and sending it down to humanity, where souls may be immersed in it to achieve transformation and knowledge. Composed in Greek, likely second century CE, this brief but densely symbolic tractate encodes a comprehensive teaching on divine emanation, human potential, and the mechanics of spiritual redemption.</p>

<h2>Content and Doctrine</h2>
<p>The tractate depicts God preparing a great krater (mixing vessel) filled with divine mind and essence. A herald is sent to announce to all humanity that whoever wishes to be born again should approach and be immersed in the krater. Those who respond to the call receive knowledge, become divine, and achieve unity with God. Those who refuse, remaining enslaved to the bodily passions, are left to death and ignorance. The krater thus becomes the central symbol for divine grace and human transformation: it represents the intermediary principle through which the transcendent divinity becomes available to humanity, and immersion in it symbolizes the reception of knowledge and divinization. The tractate implies a two-tier humanity: those capable of receiving divine knowledge and those irrevocably bound to matter. This doctrine influenced later Gnostic thought, though the <i>Krater</i> maintains a more optimistic vision of material creation than classical Gnosticism.</p>

<h2>Transmission and Manuscript Tradition</h2>
<p>The <i>Krater</i> survives only in Greek manuscript tradition and relies on the same textual witnesses as other Hermetic tractates. Nock and Festugière established the critical text from medieval Greek manuscripts; Copenhaver's modern English translation (1992) provides reliable access to the Greek. The tractate's brevity and symbolic density have made it especially attractive to esoteric interpreters; Renaissance and modern occultists have often used the krater imagery as a foundational symbol of spiritual initiation.</p>

<h2>Modern Scholarship</h2>
<p>Modern scholarship has analyzed the <i>Krater</i> as evidence of late antique religious dualism and the circulation of salvation mysticism in the Mediterranean world. Some scholars argue that the two-tier humanity described in the tractate (those capable of divinization and those irredeemable) shows Gnostic influence; others contend that it reflects a more traditional hierarchical cosmology common to Platonism and Roman mystery religions. The tractate's treatment of divine intermediaries and the mechanics of spiritual transmission has proven philosophically significant for understanding late antique theories of causation and divine action.</p>

<h2>Literature</h2>
<p>Copenhaver, Brian P. <i>Hermetica: The Greek Corpus Hermeticum and the Latin Asclepius</i>. Cambridge: Cambridge University Press, 1992.</p>
<p>Fowden, Garth. <i>The Egyptian Hermes: A Historical Approach to the Late Pagan Mind</i>. Cambridge: Cambridge University Press, 1986.</p>
<p>Mahé, Jean-Pierre. <i>Hermès en Haute-Égypte</i>. 2 vols. Québec: Presses de l'Université Laval, 1982.</p>
<p>Van den Kerchove, Anna. <i>La voie d'Hermès: Pratiques rituelles et traités hermétiques</i>. Leiden: Brill, 2012.</p>
<p>Litwa, M. David. <i>Hermetica II</i>. Cambridge: Cambridge University Press, 2018.</p>""",

    "ch_vii": """<p>The seventh tractate of the Corpus Hermeticum presents one of the tradition's most austere teachings on divine justice and the ultimate futility of material existence. Titled "The Greatest Evil" or sometimes "Against the Impious," this brief work addresses the reality of human suffering and the divine indifference to material misery, arguing that the material realm itself — generation, decay, and matter — constitutes the fundamental evil that the soul must transcend. The tractate offers little comfort but rather demands that practitioners accept the cosmic necessity of suffering and focus their efforts on spiritual liberation.</p>

<h2>Content and Doctrine</h2>
<p>The tractate's argument unfolds with stark logic: material existence is the greatest evil; the body is the source of all sin and suffering; and the divine realm operates according to absolute justice, untouched by human moral categories. God does not punish or reward; rather, material incarnation itself is the punishment for souls that have become attached to matter. Only through knowledge and the systematic rejection of bodily attachments can the soul escape the wheel of generation. The tractate thus presents a pessimistic metaphysics of matter while maintaining that escape is possible through disciplined effort and contemplative practice. This doctrine shows clear affinities with both Neoplatonic and proto-Gnostic thought, though the tractate refrains from condemning creation itself or positing a malevolent demiurge.</p>

<h2>Transmission and Manuscript Tradition</h2>
<p>The seventh tractate survives in Greek manuscript tradition; its relatively short length has made it a favorite text for translation and citation. Modern critical editions establish a reliable text. The tractate's severity and pessimism made it less popular in Renaissance and early modern Europe than the more optimistic <i>Poimandres</i>, though occultists and serious practitioners valued it for its uncompromising treatment of the soul's task.</p>

<h2>Modern Scholarship</h2>
<p>Modern scholars have debated whether CH VII represents authentic Hermetic doctrine or a later interpolation influenced by Christian or Gnostic pessimism. The consensus has moved toward accepting it as a genuine part of the corpus, though composed perhaps later than some other tractates. It provides important evidence for the internal diversity of Hermetic thought and the multiplicity of responses to the problem of suffering and matter within the tradition.</p>

<h2>Literature</h2>
<p>Copenhaver, Brian P. <i>Hermetica: The Greek Corpus Hermeticum and the Latin Asclepius</i>. Cambridge: Cambridge University Press, 1992.</p>
<p>Fowden, Garth. <i>The Egyptian Hermes</i>. Cambridge: Cambridge University Press, 1986.</p>
<p>Festugière, A. J. <i>La Révélation d'Hermès Trismégiste</i>. Paris: Lecoffre, 1944–1954.</p>
<p>Mahé, Jean-Pierre. "Hermes in High Egypt." In <i>The Coptic Encyclopaedia</i>. New York: Macmillan, 1991.</p>
<p>Van den Kerchove, Anna. <i>La voie d'Hermès</i>. Leiden: Brill, 2012.</p>""",

    "ch_viii": """<p>The eighth tractate, "Nothing Is Lost," presents a metaphysical meditation on the eternal conservation of being and the divine principle of immutability underlying apparent change and decay. This brief philosophical treatise, addressed by Hermes to his son Tat, argues that nothing in the universe is ever truly lost or destroyed; all apparent destruction is merely transformation. This doctrine, rooted in Stoic physics and Platonic metaphysics, establishes a vision of cosmic permanence and divine constancy that provides reassurance against fear of death and annihilation.</p>

<h2>Content and Doctrine</h2>
<p>Hermes begins by affirming that nothing that exists can ever pass away or be annihilated; the divine power that creates and sustains all things preserves all creation eternally. What appears to die or decay merely transforms into another mode of being. This applies equally to the body and the soul: the body may decay, but its substance is never lost; the soul, being divine and eternal, cannot decay at all. The tractate thus offers a doctrine of material and spiritual conservation that counters the fear that existence might ultimately prove empty or that individual souls might face ultimate annihilation. Tat's anxious response is rebuked: anxiety about loss reveals ignorance of the eternal nature of being.</p>

<h2>Transmission and Manuscript Tradition</h2>
<p>The eighth tractate survives in Greek and appears in all major manuscript families of the Hermetic corpus. Its brevity and philosophical clarity have made it popular in Renaissance and later esoteric traditions. Modern editions provide reliable texts.</p>

<h2>Modern Scholarship</h2>
<p>Modern scholarship recognizes CH VIII as a relatively straightforward exposition of Stoic and Platonic physics, with Hermetic framing. Its doctrine of eternal conservation and the indestructibility of being reflects late antique philosophical consensus rather than distinctive Hermetic innovation. The tractate provides important evidence for the integration of mainstream Hellenistic philosophy into Hermetic teaching.</p>

<h2>Literature</h2>
<p>Copenhaver, Brian P. <i>Hermetica</i>. Cambridge: Cambridge University Press, 1992.</p>
<p>Fowden, Garth. <i>The Egyptian Hermes</i>. Cambridge: Cambridge University Press, 1986.</p>
<p>Festugière, A. J. <i>La Révélation d'Hermès Trismégiste</i>. Paris: Lecoffre, 1944–1954.</p>
<p>Litwa, M. David. <i>Hermetica II</i>. Cambridge: Cambridge University Press, 2018.</p>
<p>Van den Kerchove, Anna. <i>La voie d'Hermès</i>. Leiden: Brill, 2012.</p>""",

    "ch_ix": """<p>The ninth tractate of the Corpus Hermeticum, "On Thinking and Sense," presents a teaching on the dual nature of human perception and knowledge: the role of sensory perception in understanding the material world and the role of pure thought (<i>noesis</i>) in comprehending the intelligible divine realm. This subtle epistemological treatise addresses the question of how humanity, positioned between matter and spirit, can achieve knowledge of both realms and ultimately unity with the divine through transcendence of material sensation.</p>

<h2>Content and Doctrine</h2>
<p>Hermes teaches that humans possess two distinct modes of knowing: sense perception (<i>aisthesis</i>), which mediates knowledge of the material world, and pure intellectual thought (<i>noesis</i>), which apprehends the intelligible realm. The senses are reliable guides to the nature of material reality but are utterly incapable of perceiving the divine. To know God, one must transcend sensation entirely and activate the higher faculty of pure intellect. This doctrine echoes Platonic epistemology but is presented within a Hermetic framework that emphasizes the possibility of mystical knowledge of the divine through the cultivation of the intellect. The tractate implies a hierarchy of beings: those bound to sensation alone; those capable of intellectual contemplation; and those who have achieved stable union with the divine intellect.</p>

<h2>Transmission and Manuscript Tradition</h2>
<p>CH IX survives in Greek manuscripts and has been translated in modern English by Copenhaver and others. The tractate's epistemological concerns have made it attractive to modern philosophers and scholars interested in the history of theories of knowledge.</p>

<h2>Modern Scholarship</h2>
<p>Modern scholars recognize CH IX as a coherent synthesis of Platonic and Stoic epistemology within a Hermetic context. The tractate provides evidence for how Hermetic teaching engaged with and transformed mainstream philosophical doctrines of knowledge and perception.</p>

<h2>Literature</h2>
<p>Copenhaver, Brian P. <i>Hermetica</i>. Cambridge: Cambridge University Press, 1992.</p>
<p>Fowden, Garth. <i>The Egyptian Hermes</i>. Cambridge: Cambridge University Press, 1986.</p>
<p>Festugière, A. J. <i>La Révélation d'Hermès Trismégiste</i>. Paris: Lecoffre, 1944–1954.</p>
<p>Mahé, Jean-Pierre. <i>Hermès en Haute-Égypte</i>. Québec: Presses de l'Université Laval, 1982.</p>
<p>Litwa, M. David. <i>Hermetica II</i>. Cambridge: Cambridge University Press, 2018.</p>""",

    "ch_x": """<p>The tenth tractate, "The Key," presents itself as an initiate revelation concerning the nature of the divine and the possibility of human knowledge of God. This brief but profound text articulates Hermetic soteriology — the doctrine of salvation through knowledge — and asserts that the soul which achieves knowledge of God enters a state of permanent transformation and deification. The tractate addresses the central Hermetic problem: whether and how the transcendent God can be known by material beings.</p>

<h2>Content and Doctrine</h2>
<p>Hermes reveals that the "key" to knowledge of God is the negation of the ten thousand false doctrines that obscure the truth. Only through purification of false opinion can one attain gnosis. The tractate asserts that God is knowable to those who have achieved inner transformation, and that this knowledge constitutes the highest human attainment: deification and union with the divine. The metaphor of the key unlocking the door to the divine realm becomes central to Hermetic symbolism and later occult tradition. The tractate implies that knowledge is not merely intellectual information but a transformative experience that permanently alters the soul's nature.</p>

<h2>Transmission and Manuscript Tradition</h2>
<p>CH X survives in Greek manuscripts; its brevity and symbolically laden language have made it a favorite of Renaissance and modern esoteric interpreters. The tractate appears in all major Hermetic manuscript families.</p>

<h2>Modern Scholarship</h2>
<p>Modern scholars have analyzed CH X as evidence for Hermetic soteriology and the role of knowledge in spiritual transformation. The tractate's emphasis on purification and negation of false opinion shows affinities with both Neoplatonic and mystical Jewish traditions.</p>

<h2>Literature</h2>
<p>Copenhaver, Brian P. <i>Hermetica</i>. Cambridge: Cambridge University Press, 1992.</p>
<p>Fowden, Garth. <i>The Egyptian Hermes</i>. Cambridge: Cambridge University Press, 1986.</p>
<p>Festugière, A. J. <i>La Révélation d'Hermès Trismégiste</i>. Paris: Lecoffre, 1944–1954.</p>
<p>Litwa, M. David. <i>Hermetica II</i>. Cambridge: Cambridge University Press, 2018.</p>
<p>Van den Kerchove, Anna. <i>La voie d'Hermès</i>. Leiden: Brill, 2012.</p>""",

    "ch_xii": """<p>The twelfth tractate, "The Mind of the Common People" or "On the Common Mind," addresses the question of whether all humans possess divine intellect and thus the capacity for knowledge of God. This brief but theologically significant text argues that while all humans receive a share of divine mind at birth, most remain enslaved to material appetites and never actualize this potential for divine knowledge. The tractate thus articulates an optimistic anthropology (all humans are divine in potential) combined with a pessimistic sociology (most humans squander this divinity).</p>

<h2>Content and Doctrine</h2>
<p>Hermes teaches that God granted mind to all humans equally; yet humans, seduced by bodily pleasures and desires, refuse to activate or use their divine intellect. Those enslaved to material appetites are like senseless animals, living entirely in the material realm. Those who recognize their divine nature and cultivate the mind achieve knowledge, virtue, and ultimately union with God. The tractate's teaching implies that divine knowledge is potentially universal but practically rare; the barriers to gnosis are self-imposed, rooted in human addiction to material pleasure. The doctrine also establishes that some humans are entirely lost, having permanently surrendered their divine nature to material servitude.</p>

<h2>Transmission and Manuscript Tradition</h2>
<p>CH XII survives in Greek and has been translated in modern English editions. The tractate's relatively clear articulation of Hermetic soteriology has made it influential in both Renaissance and modern esoteric contexts.</p>

<h2>Modern Scholarship</h2>
<p>Modern scholars recognize CH XII as presenting coherent Hermetic teaching on the human condition and the possibility of gnosis. The tractate's pessimism about most humans' capacity for spiritual realization has been compared to Gnostic and Christian doctrines of predestination, though the Hermetic version emphasizes human choice rather than divine decree.</p>

<h2>Literature</h2>
<p>Copenhaver, Brian P. <i>Hermetica</i>. Cambridge: Cambridge University Press, 1992.</p>
<p>Fowden, Garth. <i>The Egyptian Hermes</i>. Cambridge: Cambridge University Press, 1986.</p>
<p>Festugière, A. J. <i>La Révélation d'Hermès Trismégiste</i>. Paris: Lecoffre, 1944–1954.</p>
<p>Mahé, Jean-Pierre. <i>Hermès en Haute-Égypte</i>. Québec: Presses de l'Université Laval, 1982.</p>
<p>Litwa, M. David. <i>Hermetica II</i>. Cambridge: Cambridge University Press, 2018.</p>""",

    "ch_xiv": """<p>The fourteenth tractate, "To Tat," presents Hermetic teaching on the dangers of sensory attachment and the necessity of transcending bodily consciousness to achieve union with the divine. Addressed by Hermes to his son Tat, this brief exhortation combines philosophical argument with passionate rhetoric, urging the listener to abandon sensory illusions and recognize the eternal truth accessible only through pure intellect and spiritual discipline.</p>

<h2>Content and Doctrine</h2>
<p>Hermes addresses Tat with urgency: the senses deliver only illusions and false knowledge; the body is a prison that enslaves the soul. True knowledge requires the abolition of sensory consciousness and the cultivation of a state of pure contemplation. The tractate emphasizes the radical separation between the material and intelligible realms: matter is non-being, illusion, darkness; the intelligible realm is true being, reality, light. Tat's task is to starve the senses, refuse bodily pleasures, and cultivate the mind until sensory illusions cease to deceive. This extremely ascetic teaching represents one of the most demanding expressions of Hermetic soteriology.</p>

<h2>Transmission and Manuscript Tradition</h2>
<p>CH XIV survives in Greek and has been preserved in all major manuscript families of the Corpus. Its relatively straightforward exhortatory style has made it popular in translation and citation.</p>

<h2>Modern Scholarship</h2>
<p>Modern scholars have noted the tractate's Platonic and Stoic philosophical foundations combined with what appears to be a more ascetic ethic than found in other Hermetic texts. The exhortatory style suggests this may have served as a teaching device for initiates or as scripture within Hermetic communities.</p>

<h2>Literature</h2>
<p>Copenhaver, Brian P. <i>Hermetica</i>. Cambridge: Cambridge University Press, 1992.</p>
<p>Fowden, Garth. <i>The Egyptian Hermes</i>. Cambridge: Cambridge University Press, 1986.</p>
<p>Festugière, A. J. <i>La Révélation d'Hermès Trismégiste</i>. Paris: Lecoffre, 1944–1954.</p>
<p>Litwa, M. David. <i>Hermetica II</i>. Cambridge: Cambridge University Press, 2018.</p>
<p>Van den Kerchove, Anna. <i>La voie d'Hermès</i>. Leiden: Brill, 2012.</p>""",

    "ch_xvi": """<p>The sixteenth tractate, "The Definitions of Asclepius," or sometimes "Asclepius's Questions," presents a condensed summary of Hermetic teaching cast in the form of definitions and maxims. This text, which bears some similarity to the later <i>Asclepius</i> treatise, articulates core Hermetic doctrines concerning the nature of God, the cosmos, and humanity in a series of pithy, memorable statements designed to function as teaching tools for students of the tradition.</p>

<h2>Content and Doctrine</h2>
<p>The tractate presents a series of definitions establishing fundamental Hermetic metaphysics: God is indivisible, without parts, transcendent yet immanent throughout creation; the cosmos is both one and many, manifesting unity in multiplicity; the human is microcosm, reflecting the structure of the macrocosm. Key doctrines include the eternity of matter (a point of potential difference from some Gnostic systems), the divine animation of all creation, and the possibility of human knowledge of divine principles through contemplation and reason. The aphoristic style makes these teachings easily memorable and suitable for oral transmission.</p>

<h2>Transmission and Manuscript Tradition</h2>
<p>CH XVI survives in Greek manuscript tradition and relates to but is distinct from the separate <i>Asclepius</i> text transmitted in Latin. Modern editions distinguish between the two texts, though they share doctrinal content.</p>

<h2>Modern Scholarship</h2>
<p>Scholars recognize CH XVI as a summary or condensation of Hermetic teaching, possibly compiled for pedagogical purposes. The aphoristic style and emphasis on definition suggest this may have been used as a teaching manual or catechism within Hermetic communities.</p>

<h2>Literature</h2>
<p>Copenhaver, Brian P. <i>Hermetica</i>. Cambridge: Cambridge University Press, 1992.</p>
<p>Fowden, Garth. <i>The Egyptian Hermes</i>. Cambridge: Cambridge University Press, 1986.</p>
<p>Festugière, A. J. <i>La Révélation d'Hermès Trismégiste</i>. Paris: Lecoffre, 1944–1954.</p>
<p>Litwa, M. David. <i>Hermetica II</i>. Cambridge: Cambridge University Press, 2018.</p>
<p>Mahé, Jean-Pierre. <i>Hermès en Haute-Égypte</i>. Québec: Presses de l'Université Laval, 1982.</p>""",

    "ch_xvii": """<p>The seventeenth tractate, "To a King," presents Hermetic teaching cast in the form of advice given by Hermes to a ruler. This unusual political text applies Hermetic philosophy to the governance of the state, arguing that a just ruler is one who governs in accordance with divine reason and universal law, placing the common good above personal interest. The tractate thus extends Hermetic metaphysics and ethics into the realm of political philosophy.</p>

<h2>Content and Doctrine</h2>
<p>Hermes advises the king that true ruling authority derives not from force but from alignment with divine law and reason. A king who governs for personal gain and pleasure abandons divine authority; a king who sacrifices personal interest to the common good embodies divine reason. The tractate thus applies the principle of cosmic order (<i>kosmos</i>) to the political sphere: just as the cosmos operates according to eternal divine law, so must the state. The teaching implies that political authority and natural law are ultimately identical — that righteous governance is inseparable from metaphysical truth. This teaching has interesting parallels with Stoic political philosophy and later theories of natural law.</p>

<h2>Transmission and Manuscript Tradition</h2>
<p>CH XVII survives in Greek and appears in all major manuscript families. Its political content makes it distinctive within the Hermetic corpus and may reflect deliberate political engagement by Hermetic thinkers.</p>

<h2>Modern Scholarship</h2>
<p>Modern scholars have studied CH XVII as evidence for how Hermetic philosophy engaged with broader Hellenistic political discourse. The tractate shows affinities with Stoic political ethics and may reflect the actual political commitments of Hermetic communities in the Hellenistic Mediterranean.</p>

<h2>Literature</h2>
<p>Copenhaver, Brian P. <i>Hermetica</i>. Cambridge: Cambridge University Press, 1992.</p>
<p>Fowden, Garth. <i>The Egyptian Hermes</i>. Cambridge: Cambridge University Press, 1986.</p>
<p>Festugière, A. J. <i>La Révélation d'Hermès Trismégiste</i>. Paris: Lecoffre, 1944–1954.</p>
<p>Litwa, M. David. <i>Hermetica II</i>. Cambridge: Cambridge University Press, 2018.</p>
<p>Van den Kerchove, Anna. <i>La voie d'Hermès</i>. Leiden: Brill, 2012.</p>""",

    "ch_xviii": """<p>The eighteenth and final tractate of the Corpus Hermeticum, "Praise of Kings," continues the political themes introduced in CH XVII, celebrating the qualities of just rulership and the relationship between political authority and cosmic order. This closing text of the collection asserts that true kingship consists not in military power or wealth, but in wisdom, virtue, and alignment with divine law. The tractate thus completes the Hermetic corpus with an affirmation that authentic human excellence — whether personal or political — requires conformity to eternal cosmic principles.</p>

<h2>Content and Doctrine</h2>
<p>Hermes praises those rulers who govern in accordance with divine reason, who cultivate wisdom and virtue, and who place the welfare of their subjects above personal aggrandizement. True kingship is a state of consciousness as much as a political position — the soul that has achieved knowledge of divine law and conformity to it possesses kingship even without earthly power. The tractate reverses conventional hierarchies: the wise pauper possesses greater kingship than the foolish despot, because kingship consists in knowledge and virtue rather than in external power. This democratization of the concept of kingship — extending it beyond political rulers to all who have achieved gnosis — serves as a fitting conclusion to the Hermetic collection.</p>

<h2>Transmission and Manuscript Tradition</h2>
<p>CH XVIII survives in Greek and completes the set of eighteen tractates transmitted in the primary Greek manuscript family. All major modern editions include it as the final text of the Corpus Hermeticum proper.</p>

<h2>Modern Scholarship</h2>
<p>Modern scholars recognize CH XVIII as a deliberate conclusion to the Hermetic collection, returning to political themes and asserting the universalizability of Hermetic teaching beyond elite philosophical communities. The emphasis on inner kingship through spiritual achievement makes the tractate relevant to a broad audience.</p>

<h2>Literature</h2>
<p>Copenhaver, Brian P. <i>Hermetica</i>. Cambridge: Cambridge University Press, 1992.</p>
<p>Fowden, Garth. <i>The Egyptian Hermes</i>. Cambridge: Cambridge University Press, 1986.</p>
<p>Festugière, A. J. <i>La Révélation d'Hermès Trismégiste</i>. Paris: Lecoffre, 1944–1954.</p>
<p>Litwa, M. David. <i>Hermetica II</i>. Cambridge: Cambridge University Press, 2018.</p>
<p>Mahé, Jean-Pierre. <i>Hermès en Haute-Égypte</i>. Québec: Presses de l'Université Laval, 1982.</p>""",
}

def expand_texts():
    """Update text analyses with full content."""
    conn = sqlite3.connect(str(DB_PATH))
    c = conn.cursor()

    for text_id, analysis_html in CH_ANALYSES.items():
        c.execute("""
            UPDATE texts
            SET analysis_html = ?
            WHERE text_id = ?
        """, (analysis_html, text_id))

    conn.commit()
    print(f"Expanded {len(CH_ANALYSES)} Corpus Hermeticum tractate analyses:")
    for text_id in CH_ANALYSES.keys():
        c.execute("SELECT title, length(analysis_html) FROM texts WHERE text_id = ?", (text_id,))
        result = c.fetchone()
        if result:
            title, length = result
            print(f"  [OK] {text_id:30} ({title:40}): {length:5} chars")

    conn.close()

if __name__ == "__main__":
    expand_texts()
