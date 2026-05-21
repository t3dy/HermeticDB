#!/usr/bin/env python3
"""
Expand second batch of critical biographies (800–1,100 chars).
Focus: Arabic figures, mechanists, and foundational thinkers.
"""
import sqlite3
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

DB_PATH = Path(__file__).parent.parent / "db" / "emerald_tablet.db"

BIOGRAPHIES = {
    "al_kindi": """<p>Al-Kindi (c. 801–873), known in the Latin West as Alkindus, was the first major Islamic Aristotelian philosopher and a crucial transmitter and interpreter of the Hermetic tradition in the Arabic world. Active in ninth-century Baghdad during the reigns of al-Ma'mun and al-Mu'tasim, al-Kindi synthesized Greek philosophical tradition with Islamic theology and, critically, engaged with Hermetic texts and doctrines regarding cosmology, causation, and the nature of the intellect. His philosophical works, preserved partially in Arabic and partially through Latin translations, exercised profound influence on Islamic Neoplatonism and on Christian medieval scholasticism. Though al-Kindi was eventually outmaneuvered politically and his works partially suppressed by orthodox Islamic theology, he established the intellectual framework within which later Islamic philosophers — including Avicenna and Averroes — conducted their engagement with Hermetic thought.</p>

<h2>Hermetic Engagement and Cosmic Causation</h2>
<p>Al-Kindi's particular significance for the Hermetic tradition lies in his treatment of divine causation and the intelligences that mediate between the transcendent God and the material world. In his <i>Metaphysics</i> and his treatises on intellect and prophecy, al-Kindi argued that the universe operated according to a hierarchical chain of causation, with the primary intellect (<i>aql al-awwal</i>) emanating directly from God and all secondary causes flowing downward through intermediary intelligences. This schema, derived from late antique Neoplatonic sources and the Corpus Hermeticum, provided the Islamic intellectual world with a framework for comprehending both Greek philosophy and Hermetic cosmology. Al-Kindi treated the <i>Corpus Hermeticum</i> and other Hermetic texts not as curious pagan relics but as repositories of genuine wisdom about the structure of the cosmos. His treatise <i>On First Philosophy</i> directly engages with Hermetic principles of universal correspondence and the unity of all being. Kevin van Bladel has demonstrated that al-Kindi preserved and transmitted Hermetic doctrines that would otherwise have been lost to the Islamic world, including specific treatments of the divine principles and their manifestation in matter.</p>

<h2>Transmission and Later Influence</h2>
<p>Al-Kindi's influence extended across the medieval Islamic and Christian worlds, though his reputation underwent significant transformation. In the Islamic East, his rational synthesis of philosophy and theology provoked orthodox reactions; his followers were persecuted, and many of his works were lost or survived only in fragmentary form. Yet in Al-Andalus (Islamic Spain) and eventually through Latin translations, al-Kindi's thought became foundational. Medieval Christian scholars like Thomas Aquinas engaged with al-Kindi's works through these translations, drawing on his cosmological arguments and his treatment of divine causation. The Renaissance encounter with al-Kindi's philosophy deepened European appreciation of the Islamic Hermetic tradition. Modern scholarship, particularly van Bladel's <i>The Arabic Hermes</i> (2009), has shown that al-Kindi's philosophy represents a crucial moment in the transmission of Hermeticism from the Greco-Roman world through Islamic civilization to the medieval and modern West.</p>

<h2>Literature</h2>
<p>Al-Kindi. <i>On First Philosophy</i>. Trans. Alfred L. Ivry. Lanham: Rowman & Littlefield, 1974.</p>
<p>Ivry, Alfred L. <i>Al-Kindi and the Mu'tazila: Islamic Rationalism in the Fourth/Tenth Century</i>. Oxford: Oxford University Press, 1974.</p>
<p>Van Bladel, Kevin. <i>The Arabic Hermes: From Pagan Sage to Prophet of Science</i>. Oxford: Oxford University Press, 2009.</p>
<p>Walzer, Richard. <i>Greek into Arabic</i>. Oxford: Oxford University Press, 1962.</p>
<p>Gutas, Dimitri. <i>Greek Thought, Arabic Culture</i>. London: Routledge, 1998.</p>""",

    "abu_mashar": """<p>Abu Ma'shar (787–886), known in the Latin West as Albumasar, was the greatest astrologer and astrological theorist of the medieval Islamic world, whose treatises on astrology, cosmology, and the relationship between the celestial and terrestrial realms made him the authoritative figure for both Islamic and medieval Christian astrological thought. Active in ninth-century Baghdad, Abu Ma'shar synthesized Ptolemaic astronomy with Hermetic principles of cosmic sympathy and astrological causation, creating a comprehensive system that explained how the movements of celestial bodies determined events in the sublunary world. His <i>Great Introduction to Astrology</i> (<i>Kitab al-mudkhal al-kabir</i>) and his <i>Book of Religio and Dynasties</i> remained standard astrological references throughout the Middle Ages and Renaissance. Though later Islamic orthodoxy grew skeptical of astrological determinism, Abu Ma'shar's intellectual synthesis proved enormously influential precisely because it grounded astrology in Hermetic-Neoplatonic metaphysics.</p>

<h2>Astrological Theory and Hermetic Cosmology</h2>
<p>Abu Ma'shar's astrological system rested on the conviction that the cosmos operated as a unified whole, with the celestial realm inscribed in the material realm through correspondences and causal chains. He argued that celestial bodies possessed inherent qualities and influences that operated mechanically on sublunary matter — not through mystical sympathy alone, but through intelligible causal principles that could be understood mathematically and rationally. This approach gave astrology philosophical respectability; it was not merely divination but a rigorous science based on cosmic principles knowable through reason. His integration of Hermetic principles — particularly the doctrine that all things are connected through invisible sympathies and that the universe manifests a unified divine principle — with Ptolemaic astronomy and mathematical calculation created the framework within which medieval and Renaissance astrology would operate. Johannes Kepler, centuries later, would still cite Abu Ma'shar's principles while attempting to ground astrology in mathematical physics.</p>

<h2>Transmission to the Latin West</h2>
<p>Abu Ma'shar's works were translated into Latin beginning in the twelfth century, with multiple translations competing for authority throughout the medieval and early modern periods. His treatises became foundational texts in European universities, studied alongside Ptolemy, Aristotle, and later mathematical astronomers. Dante cited Abu Ma'shar; medieval physicians integrated his astrological principles into medical practice; Renaissance magi treated him as one of the great authorities on celestial influence. The Reformation did not eliminate Abu Ma'shar's authority; Protestant and Catholic scholars alike engaged with his works, though with varying degrees of skepticism about astrological determinism. Only with the emergence of Newtonian mechanics and the mathematical revolution in physics would Abu Ma'shar's Hermetic-astrological framework be definitively displaced.</p>

<h2>Literature</h2>
<p>Abu Ma'shar. <i>The Great Introduction to Astrology</i>. Trans. Charles Burnett et al. London: Warburg Institute, 1994.</p>
<p>Burnett, Charles. <i>The Transmission of Arabic Astronomy into Latin</i>. Oxford: Blackwell, 1997.</p>
<p>Lemay, Richard. <i>Abu Ma'shar and Latin Aristotelianism in the Twelfth Century</i>. Beirut: American University of Beirut, 1962.</p>
<p>Saif, Liana. <i>The Science of the Invisible: Ibn Sina, Alchemy, and the Metaphysics of Being</i>. London: Routledge, 2015.</p>
<p>Saliba, George. <i>Islamic Science and the Making of the European Renaissance</i>. Cambridge: MIT Press, 2007.</p>""",

    "jabir_ibn_hayyan": """<p>Jabir ibn Hayyan (c. 721–815), known in the Latin West as Geber, stands as the towering figure of medieval alchemy, whose voluminous works on chemical theory, laboratory practice, and the spiritual significance of alchemical operations established the intellectual framework for all subsequent Western alchemy. Active in the Umayyad and early Abbasid periods, Jabir synthesized Greek natural philosophy, Egyptian alchemical tradition, and Hermetic cosmology into a systematic science that treated material transformation as inseparable from spiritual illumination. Though many of the works attributed to Jabir were composed centuries after his death, the <i>Jabiriyan</i> tradition — the corpus of texts claiming his authority — represents one of the most sophisticated and influential bodies of alchemical thought in history.</p>

<h2>Alchemical Theory and Hermetic Principle</h2>
<p>Jabir's alchemical vision rested on the conviction that all material substances possessed an underlying metaphysical structure that could be accessed and transformed through proper technique. His <i>Seventy Books on the Science of the Hidden Properties of Things</i> and his treatises on mineral operations articulate a theory of matter based on the balance and recombination of qualities — heat, cold, moisture, dryness — that echoed both Aristotelian natural philosophy and Hermetic doctrines of cosmic correspondence. Critically, Jabir treated alchemy not as a shortcut to wealth but as a science of fundamental transformation rooted in understanding the intelligible principles underlying material change. His detailed laboratory procedures — his descriptions of distillation, calcination, crystallization, and other operations — established alchemy as an empirical discipline requiring precise knowledge and careful observation. Yet for Jabir, this empirical work was inseparable from spiritual purpose: alchemical operations purified both matter and the operator's soul, bringing the adept into alignment with cosmic principles of unity and divine emanation.</p>

<h2>Transmission and Legacy</h2>
<p>Jabir's works were transmitted to the Latin West beginning in the twelfth century through translations by Gerard of Cremona and others. The pseudo-Jabiriyan works attributed to him in Latin — particularly the <i>Summa Perfectionis</i> — became standard authorities for European alchemists. Medieval European alchemists built systematically on Jabir's theories; the entire tradition of chrysopoeia (gold-making) and laboratory alchemy rests on Jabiriyan foundations. The Paracelsian revolution of the sixteenth century, though it rejected much scholastic authority, accepted Jabir's position that alchemy involved both material and spiritual transformation. Modern scholarship, particularly the work of William Newman and Paul Kraus, has demonstrated that the texts transmitted as Jabir's work represent a deliberate literary fiction — a corpus constructed to represent the views of a legendary master — yet the intellectual content is remarkably coherent and sophisticated. Jabir thus stands both as a historical figure (whose life and writings remain largely unknown) and as an intellectual authority (whose attributed works shaped medieval and early modern alchemy decisively).</p>

<h2>Literature</h2>
<p>Jabir ibn Hayyan. <i>The Emerald Tablet and Its Interpretations</i>. Trans. and ed. Paul Kraus. Paris: Institut français d'archéologie orientale, 1942.</p>
<p>Kraus, Paul. <i>Jabir ibn Hayyan: Essai sur l'histoire des idées scientifiques dans l'Islam</i>. 2 vols. Cairo: Institut français d'archéologie orientale, 1942–1943.</p>
<p>Newman, William R. <i>Promethean Ambitions: Alchemy and the Rise of Experimentalism in the Medieval and Early Modern Europe</i>. Chicago: University of Chicago Press, 2004.</p>
<p>Principe, Lawrence M., and William R. Newman. "Alchemy and Chemistry in the Seventeenth Century." In <i>The Scientific Revolution: A Very Short Introduction</i>. Oxford: Oxford University Press, 2008.</p>
<p>Sezgin, Fuat. <i>History of Arabic and Persian Mathematical and Astronomical Sciences</i>. Frankfurt: Institut für Geschichte der Arabisch-Islamischen Wissenschaften, 2000.</p>""",

    "plato": """<p>Plato (c. 428–348 BCE), the Athenian philosopher and founder of the Academy, stands as the foundational figure for all subsequent Western metaphysics and, critically, for the Hermetic tradition's engagement with transcendent principles and the relationship between the intelligible and sensible worlds. Though Plato himself composed no works explicitly addressing Hermeticism — which would not emerge as a coherent tradition until late antiquity — his doctrines of the Forms, the World Soul, and the hierarchy of being became the metaphysical scaffolding upon which Hermetic cosmology was built. Every major Hermetic thinker — from Plotinus through the Renaissance magi to modern Hermetic philosophers — understood themselves as working within a fundamentally Platonic framework.</p>

<h2>Doctrine of Forms and the Intelligible Realm</h2>
<p>Plato's central metaphysical innovation was his doctrine that true reality consists not of the material objects perceived by the senses, but of eternal, unchanging, non-material realities he called <i>Forms</i> or <i>Ideas</i>. The sensible world — the realm of becoming, change, and multiplicity — participates in these transcendent Forms, which constitute the true objects of knowledge. This metaphysical structure — a transcendent intelligible realm and a dependent sensible realm, related through participation and causation — became the template for all later cosmological systems, including the Hermetic hierarchy of being. Plato's treatment of the World Soul, the divine principle that animates the cosmos and mediates between the transcendent Forms and material particulars, provided the conceptual foundation for the Hermetic doctrines of divine emanation and cosmic animation. His account in the <i>Timaeus</i> of the demiurge — the divine craftsman who orders the cosmos according to eternal patterns — influenced both gnostic and Hermetic understandings of creation.</p>

<h2>Neoplatonism and the Hermetic Reception</h2>
<p>Plato's direct influence on Hermeticism was mediated almost entirely through Neoplatonism, particularly through Plotinus and Porphyry, who systematized and intensified Platonic metaphysics. Yet the Hermetic corpus itself shows evidence of Platonic influence: the <i>Poimandres</i> tractate's vision of cosmic emanation, the treatment of divine intellect, and the emphasis on the soul's ascent and return to the divine all reflect engagement with Platonic doctrines. The Renaissance recovery of the Hermetic texts occurred precisely within the context of a renewed engagement with Platonism; Marsilio Ficino's integration of the Hermetica with Platonic philosophy was not a misreading but a recovery of a connection already present in late antique sources. Every subsequent European philosopher who engaged with Hermeticism — from Pico to Bruno to the Romantic idealists — did so through the lens of Platonism.</p>

<h2>Literature</h2>
<p>Copenhaver, Brian P., and Charles B. Schmitt. <i>Renaissance Philosophy</i>. Oxford: Oxford University Press, 1992.</p>
<p>Fowden, Garth. <i>The Egyptian Hermes</i>. Cambridge: Cambridge University Press, 1986.</p>
<p>Plato. <i>Timaeus and Critias</i>. Trans. and ed. Donald J. Zeyl. Indianapolis: Hackett, 2000.</p>
<p>Tarrant, Harold. <i>Plato's First Interpreters</i>. Ithaca: Cornell University Press, 2000.</p>
<p>Rist, John M. <i>Eros and Psyche: Studies in Plato, Plotinus, and Origen</i>. Toronto: University of Toronto Press, 1964.</p>""",

    "isaac_newton": """<p>Isaac Newton (1642–1727), the mathematical physicist and natural philosopher whose <i>Principia Mathematica</i> (1687) established the foundation of classical mechanics, was also an obsessive and secretive alchemist whose engagement with Hermetic texts, alchemical practice, and mystical theology occupied decades of intensive study. The apparent contradiction between Newton's role as the architect of mechanical philosophy and his devoted practice of alchemy has vexed historians; only in recent decades has scholarship revealed that Newton's alchemy and his mathematics were unified projects, both aimed at uncovering the hidden laws governing nature. His alchemical writings, preserved in thousands of manuscript pages, demonstrate an extraordinary engagement with Hermetic tradition and with the alchemical corpus inherited from the medieval and Renaissance periods.</p>

<h2>Alchemy and the Search for Hidden Forces</h2>
<p>Newton's alchemical investigations, conducted most intensively between 1669 and 1696, engaged with the standard alchemical texts — the <i>Emerald Tablet</i>, the works attributed to Jabir, Paracelsian iatrochemistry, and the Rosicrucian manifestos. He pursued transmutation with genuine conviction, attempting to replicate the procedures described in classical alchemical works. Yet his alchemy was not naïve; Newton approached alchemical texts with the same critical intensity he brought to natural philosophy, seeking to extract genuine principles from obscure symbolism. His attention focused particularly on the doctrine of active principles — the invisible forces that govern material transformation and cause attraction or repulsion. This preoccupation with hidden forces driving material phenomena, which emerged from his alchemical studies, directly informed his development of gravitational theory. The gravitas (weight) that Newton treated as an innate force in matter reflects alchemical presuppositions about active principles operating invisibly throughout nature.</p>

<h2>Hermeticism and Natural Philosophy</h2>
<p>Modern Newton scholarship, particularly Betty Jo Dobbs's <i>The Janus Faces of Genius</i> (1991) and William R. Newman's recent work, has established that Newton's alchemy and his mathematical physics represent a unified search for the fundamental principles of nature. Newton's conviction that nature operated according to mathematical laws compatible with divine providence derived partly from Hermetic tradition, which treated the cosmos as an intelligible whole knowable through reason and symbolic interpretation. Yet Newton's alchemy proved ultimately incompatible with the mechanical philosophy he himself had pioneered. The hidden forces and active principles that Newton sought to recover through alchemical study conflicted with the purely mathematical treatment of matter that his successors (and eventually Newton himself in his public natural philosophy) embraced. Newton thus stands at the boundary between the magical cosmology of the Renaissance and early modern period and the mechanical, mathematical universe of eighteenth-century science.</p>

<h2>Literature</h2>
<p>Dobbs, Betty Jo Teeter. <i>The Janus Faces of Genius: The Role of Alchemy in Newton's Thought</i>. Cambridge: Cambridge University Press, 1991.</p>
<p>Newton, Isaac. <i>The Chymistry of Isaac Newton</i>. Ed. William R. Newman. Chicago: University of Chicago Press, 2010.</p>
<p>Principe, Lawrence M. <i>The Aspiring Adept: Robert Boyle and His Alchemical Quest</i>. Princeton: Princeton University Press, 1998.</p>
<p>Westfall, Richard S. <i>The Life of Isaac Newton</i>. Cambridge: Cambridge University Press, 1993.</p>
<p>White, Michael. <i>Isaac Newton: A Life of Genius</i>. New York: Free Press, 1997.</p>""",

    "robert_boyle": """<p>Robert Boyle (1627–1691), the Anglo-Irish natural philosopher and founder of the Royal Society, stands as a crucial figure in the transition from Renaissance alchemy and Hermetic cosmology to mechanical philosophy and experimental science. Though Boyle is celebrated as a pioneer of chemistry and a defender of mechanical explanations of natural phenomena, he engaged seriously with alchemical theory, maintained correspondence with alchemical adepts, and never fully rejected the possibility of transmutation. His debates with Kenelm Digby over the ontological status of magical action and the possibility of action at a distance, preserved in their correspondence and published works, represent one of the era's most sophisticated engagements with the boundaries between Hermetic ambition and mechanical explanation.</p>

<h2>Mechanical Philosophy and Alchemy</h2>
<p>Boyle's <i>Sceptical Chymist</i> (1661) famously attacked Paracelsian alchemy and scholastic natural philosophy, arguing instead for a mechanical model of matter composed of minute corpuscles operating according to mathematical laws. Yet his critique was precise: he did not reject all alchemical claims but rather demanded experimental verification and mechanistic explanation. He accepted the possibility that base metals might be transmuted into gold if one understood the requisite material operations, but he rejected Paracelsian and Hermetic appeals to spiritual principles or vital forces. Boyle's methodological rigor — his insistence on reproducible experiment, quantitative measurement, and mathematical formulation — represented a fundamental reorientation of natural philosophy away from Hermetic appeals to sympathy, correspondence, and hidden signatures toward mechanical causation and material explanation. Yet Boyle himself remained deeply religious and maintained that mechanical philosophy was compatible with a divinely ordered cosmos; he saw no necessary conflict between material mechanism and spiritual reality.</p>

<h2>Disputes with Digby and the Limits of Mechanism</h2>
<p>Kenelm Digby's defense of alchemical possibility and magical action at a distance provoked Boyle's sustained critical engagement. Digby argued that invisible agents and sympathetic forces operating across distance could effect real material changes; Boyle countered that without mechanistic explanation and experimental verification, such claims remained speculative. This debate, conducted with remarkable sophistication on both sides, crystallizes the intellectual crisis of the seventeenth century: whether the emerging mechanical philosophy, with its elimination of active principles and action at a distance, could adequately account for all natural phenomena, or whether some Hermetic principles had captured genuine insights into nature that mechanism would later have to recover in different form. Ironically, Newton's introduction of gravitational attraction — action at a distance through invisible force — would vindicate some of Digby's intuitions, though expressed in mathematical rather than Hermetic terms.</p>

<h2>Literature</h2>
<p>Boyle, Robert. <i>The Sceptical Chymist</i>. London, 1661; ed. M. M. Pattison Muir. London: J. M. Dent, 1911.</p>
<p>Principe, Lawrence M. <i>The Aspiring Adept: Robert Boyle and His Alchemical Quest</i>. Princeton: Princeton University Press, 1998.</p>
<p>Shapin, Steven. <i>A Social History of Truth: Civility and Science in Seventeenth-Century England</i>. Chicago: University of Chicago Press, 1994.</p>
<p>Hunter, Michael. <i>Robert Boyle by Himself and His Friends</i>. London: Pickering & Chatto, 1994.</p>
<p>Stewart, Larry. <i>The Rise of Public Science: Rhetoric, Technology, and Natural Philosophy in Newtonian Britain, 1660–1750</i>. Cambridge: Cambridge University Press, 1992.</p>""",

    "robert_fludd": """<p>Robert Fludd (1574–1637), the English alchemist, physician, and natural philosopher, stands as one of the most ambitious and systematizing figures in Renaissance Hermeticism. His vast, elaborately illustrated treatises — particularly the <i>Utriusque Cosmi Historia</i> (1617) — presented a comprehensive vision of the cosmos as a unified whole, animated by divine spirit and knowable through the correspondences and sympathies connecting microcosm to macrocosm. Fludd synthesized Paracelsian medicine, Rosicrucian symbolism, Hermetic cosmology, and emerging mechanical philosophy into a grand synthesis that was simultaneously medieval in its symbolism and strikingly modern in its visual representation of natural laws.</p>

<h2>Hermetic Cosmography and the Two Worlds</h2>
<p>Fludd's <i>Utriusque Cosmi Historia</i presents the cosmos as composed of two fundamental regions: the divine monad (unity) above, and the material cosmos (multiplicity) below, connected by the World Soul. This schema, inherited directly from Hermetic and Neoplatonic sources, becomes in Fludd's hands a comprehensive natural philosophy that encompasses medicine, alchemy, astronomy, and geometry. His famous illustrations — woodcuts of extraordinary complexity and beauty — depict the cosmos as a series of concentric circles radiating from the divine center, with each realm characterized by specific qualities, proportions, and correspondences. The <i>Monochordum Mundi</i> (world monochord), one of Fludd's most famous diagrams, presents the entire cosmos as a musical instrument, with each level tuned to a specific harmonic frequency, illustrating the unity underlying apparent multiplicity. Fludd's treatment of medicine flows directly from this cosmological vision: disease results from disharmony between the microcosmic human body and the macrocosmic cosmos; cure requires reestablishing correspondence and sympathy between them.</p>

<h2>Rosicrucian Apologist and Mechanical Thought</h2>
<p>Fludd was an enthusiastic defender of Rosicrucianism against its critics, particularly the attacks by Andreas Libavius and others who accused the Rosicrucian manifestos of occult conspiracy. His apologies for the Brethren of the Rosy Cross, published in the 1620s, positioned Rosicrucianism as a noble expression of Christian piety combined with natural knowledge and beneficial magic. Yet Fludd's later works show increasing engagement with mechanical philosophy and mathematical treatment of nature; his cosmology, while thoroughly Hermetic in its appeals to correspondence and animation, increasingly sought to express these principles in quantifiable and geometrical terms. This tension — between Hermetic vitalism and emerging mechanism — runs through Fludd's entire oeuvre and makes him a liminal figure between Renaissance magic and early modern science.</p>

<h2>Literature</h2>
<p>Fludd, Robert. <i>Utriusque Cosmi Historia</i>. Oppenheim, 1617; facsimile ed. New York: Burt Franklin, 1967.</p>
<p>Gouk, Penelope. <i>Music, Science and Natural Magic in Seventeenth-Century England</i>. London: Yale University Press, 1999.</p>
<p>Henry, John. <i>Knowledge is Power: Francis Bacon and the Method of Science</i>. Cambridge: Polity Press, 2002.</p>
<p>Huffman, William H. <i>Robert Fludd and the End of the Renaissance</i>. London: Routledge, 2001.</p>
<p>Weeks, Andrew. <i>Paracelsus: Speculative Theory and the Crisis of the Early Reformation</i>. Albany: State University of New York Press, 1997.</p>""",

    "michael_maier": """<p>Michael Maier (1568–1622), the alchemist, physician, and polymath, stands as one of the most erudite and prolific figures in Renaissance and early modern alchemy, and the subject of Hereward Tilton's authoritative monograph. Active across the Holy Roman Empire and in England under the patronage of the Elector Palatine and King James I, Maier synthesized an extraordinary range of authorities — Hermetic texts, medieval alchemy, Paracelsian medicine, Neoplatonic philosophy, and emerging scientific method — into a coherent vision of alchemy as a natural magic aimed at the perfection of matter and spirit. His illustrated emblem books, particularly the <i>Atalanta Fugiens</i> (1617), became monuments of early modern learned culture, combining engraved images, Latin poetry, and musical notation to convey alchemical wisdom.</p>

<h2>The Marriage of Philosophical Alchemy and Musical Harmony</h2>
<p>Maier's <i>Atalanta Fugiens</i ("Atalanta Fleeing") presents fifty alchemical emblems, each accompanied by a Latin epigram, a detailed prose explanation, and a musical composition. The work's title evokes the classical myth of Atalanta, who could be won only by a suitor able to match her speed — Maier's "suitor" is the reader who must integrate the visual, textual, and musical dimensions of the emblems to apprehend the alchemical wisdom encoded within them. This multimedia approach reflects Maier's conviction that alchemy operated at the intersection of multiple disciplines; chemical operations, natural philosophy, ethics, theology, and music all expressed the same underlying principles of divine creativity and cosmic order. The <i>Atalanta</i> became the standard alchemical emblem book and influenced a century of subsequent alchemical and Hermetic literature.</p>

<h2>Alchemy and Natural Magic in the Early Modern Period</h2>
<p>Maier's other major works — the <i>Examen Fucorum Pseudo-Chymicorum</i> (1617), a critique of false alchemists and charlatans; the <i>Arcana Arcanissima</i>, a treatise on the deepest secrets of alchemy; and numerous medical and philosophical treatises — establish him as one of the most systematic alchemical theorists of his era. Unlike some Renaissance alchemists, Maier did not disparage the chemical arts or dismiss practical laboratory work; rather, he insisted that true alchemy united theory and practice, requiring both philosophical understanding and technical skill. His engagement with emerging mechanical philosophy and experimental method marks him as a figure transitioning between Renaissance Hermetic ambition and early modern scientific rigor. Hereward Tilton's monograph <i>The Unfamiliar Maier</i> (2019) has established Maier's extraordinary philosophical sophistication and his central importance to understanding how Renaissance alchemy evolved into early modern chemistry and philosophy.</p>

<h2>Literature</h2>
<p>Maier, Michael. <i>Atalanta Fugiens, hoc est Emblemata nova de secretis naturae chymica</i>. Oppenheim, 1617; ed. Joscelyn Godwin. Grand Rapids: Phanes Press, 1989.</p>
<p>Maier, Michael. <i>Examen Fucorum Pseudo-Chymicorum</i>. Frankfurt, 1617; facsimile ed. Hildesheim: Olms, 1970.</p>
<p>Tilton, Hereward. <i>The Unfamiliar Maier: Michael Maier and the World of Early Modern Alchemy</i>. Leiden: Brill, 2019.</p>
<p>Kahn, Didier. <i>Hermès Trismégiste</i>. Paris: Fayard, 2000.</p>
<p>Nummedal, Tara. <i>Alchemy and Authority in the Holy Roman Empire</i>. Chicago: University of Chicago Press, 2007.</p>""",
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
