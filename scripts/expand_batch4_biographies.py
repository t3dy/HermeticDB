#!/usr/bin/env python3
"""
Expand batch 4: scholars and additional critical figures.
"""
import sqlite3
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

DB_PATH = Path(__file__).parent.parent / "db" / "emerald_tablet.db"

BIOGRAPHIES = {
    "david_litwa": """<p>M. David Litwa (b. 1979), the contemporary classical philologist and Hermetic scholar, stands as one of the leading authorities on the Greek Corpus Hermeticum and late antique religious thought. His <i>Hermetica II</i> (2018), a comprehensive edition and translation of the Latin Asclepius and isolated Greek Hermetic fragments, has become the standard scholarly reference work. Litwa's meticulous philological approach, combined with his deep engagement with late antique religious syncretism, has established him as a central figure in contemporary Hermetic studies.</p>

<h2>Scholarly Method and the Greek Sources</h2>
<p>Litwa's contributions have focused on recovering the authentic textual tradition of Hermetic sources and clarifying the relationships between Greek and Latin manuscript families. His edition of the Stobaean fragments—Greek quotations of Hermetic texts preserved by the ancient anthologist Stobaeus—has proven invaluable for understanding how Hermetic philosophy circulated in late antiquity. Litwa's insistence on rigorous philological method and careful attention to manuscript evidence represents contemporary scholarship at its most demanding. His work demonstrates that the Hermetic texts, properly understood through careful textual analysis, reveal a coherent philosophical tradition grounded in late antique religion and philosophy.</p>

<h2>Contribution to Hermetic Understanding</h2>
<p>Litwa's scholarship has advanced understanding of the Corpus Hermeticum's relationship to Platonism, Stoicism, and early Christian thought. His treatment of Egyptian influences on Hermetic philosophy has shown how authentic Egyptian religious traditions, filtered through Greco-Roman cultural frameworks, informed the textual tradition. Litwa's work exemplifies contemporary academic Hermetic studies at its most sophisticated.</p>

<h2>Literature</h2>
<p>Litwa, M. David. <i>Hermetica II: The Latin Asclepius and the Greek Corpus Hermeticum XIII, with Coptic Texts</i>. Cambridge: Cambridge University Press, 2018.</p>
<p>Copenhaver, Brian P. <i>Hermetica: The Greek Corpus Hermeticum and the Latin Asclepius</i>. Cambridge: Cambridge University Press, 1992.</p>
<p>Fowden, Garth. <i>The Egyptian Hermes</i>. Cambridge: Cambridge University Press, 1986.</p>
<p>Hanegraaff, Wouter J. <i>Hermetic Spirituality and the Historical Imagination</i>. Leiden: Brill, 2022.</p>
<p>Van den Kerchove, Anna. <i>La voie d'Hermès: Pratiques rituelles et traités hermétiques</i>. Leiden: Brill, 2012.</p>""",

    "didier_kahn": """<p>Didier Kahn (b. 1963), the French historian of alchemy and chemical philosophy, has emerged as one of the foremost contemporary authorities on the history of alchemy, its practitioners, and its relationship to the emergence of modern chemistry. His extensive research into alchemical manuscripts, biographical studies of major alchemists, and analyses of alchemical theory have fundamentally reshaped contemporary understanding of alchemy as a coherent intellectual and practical tradition. Kahn's work combines archival research of extraordinary depth with theoretical sophistication, establishing alchemy as a central concern of early modern intellectual history.</p>

<h2>Alchemy and Chemical Philosophy</h2>
<p>Kahn's major works, including his extensive studies of Renaissance and early modern alchemists and his <i>Alchimie et argent au temps de Louis XIV</i>, demonstrate that alchemy was not a marginal pursuit of cranks and charlatans but a serious intellectual endeavor practiced by physicians, natural philosophers, and aristocrats. His analysis of the relationship between alchemical theory and practice, and between alchemy and the emergence of chemistry, has established him as the leading contemporary scholar on this crucial transition. Kahn's insistence that alchemists engaged seriously with natural philosophy and material operations has proved influential in academic circles previously dismissive of alchemy.</p>

<h2>Archival Scholarship and Hermetic Connections</h2>
<p>Kahn's research into alchemical manuscripts has revealed the continuous circulation of Hermetic texts and ideas through the medieval and early modern periods. His work on the transmission of Jabiriyan alchemy through Islamic and European traditions has clarified how Hermetic philosophy informed alchemical practice. Kahn exemplifies how rigorous historical scholarship can recover the intellectual coherence and serious intent of traditions (like alchemy) that modernity had dismissed as superstition.</p>

<h2>Literature</h2>
<p>Kahn, Didier. <i>Alchimie et argent au temps de Louis XIV: Essai d'histoire économique et sociale</i>. Paris: Guénégaud, 2007.</p>
<p>Kahn, Didier. <i>Hermès Trismégiste: Histoire de l'hermétisme de l'Antiquité à la Renaissance</i>. Paris: Éditions du Seuil, 2000.</p>
<p>Principe, Lawrence M., and William R. Newman. "Alchemy and Chemistry in the Seventeenth Century." In <i>The Scientific Revolution: A Very Short Introduction</i>. Oxford: Oxford University Press, 2008.</p>
<p>Newman, William R. <i>Promethean Ambitions: Alchemy and the Rise of Experimentalism in the Medieval and Early Modern Europe</i>. Chicago: University of Chicago Press, 2004.</p>
<p>Nummedal, Tara. <i>Alchemy and Authority in the Holy Roman Empire</i>. Chicago: University of Chicago Press, 2007.</p>""",

    "hereward_tilton": """<p>Hereward Tilton (b. 1968), the contemporary English-language scholar of Renaissance and early modern alchemy and Hermeticism, has produced the most comprehensive and philosophically sophisticated study of Michael Maier and Renaissance alchemical thought. His <i>The Unfamiliar Maier</i> (2019) and extensive published articles have established him as a leading contemporary authority on early modern alchemy, its philosophical dimensions, and its relationship to emerging mechanical philosophy. Tilton's work combines careful textual analysis with genuine philosophical engagement with alchemical ideas.</p>

<h2>Michael Maier and Alchemical Philosophy</h2>
<p>Tilton's monograph on Michael Maier, the 16th-17th century alchemist and physician, represents the most thorough study of a single major alchemist in contemporary scholarship. Through meticulous analysis of Maier's <i>Atalanta Fugiens</i> and other works, Tilton demonstrates the philosophical coherence and intentionality of Maier's alchemical vision. Tilton's treatment of how Maier synthesized practical alchemy with natural magic, Paracelsian medicine, and natural philosophy establishes him as a figure of considerable intellectual sophistication. His work models how Renaissance alchemy should be studied: not as primitive proto-chemistry but as a philosophical and practical tradition with its own internal logic and goals.</p>

<h2>Alchemy and Early Modernity</h2>
<p>Tilton's broader scholarly work addresses how Renaissance and early modern alchemy engaged with emerging mechanical philosophy and the Scientific Revolution. His insistence that alchemy represented a genuine alternative to mechanical explanation—one that has much to teach about the history of science and the limits of mechanistic worldviews—has influenced contemporary scholarship on the history of science.</p>

<h2>Literature</h2>
<p>Tilton, Hereward. <i>The Unfamiliar Maier: Michael Maier and the World of Early Modern Alchemy</i>. Leiden: Brill, 2019.</p>
<p>Maier, Michael. <i>Atalanta Fugiens</i>. Oppenheim, 1617; ed. Joscelyn Godwin. Grand Rapids: Phanes Press, 1989.</p>
<p>Nummedal, Tara. <i>Alchemy and Authority in the Holy Roman Empire</i>. Chicago: University of Chicago Press, 2007.</p>
<p>Kahn, Didier. <i>Hermès Trismégiste</i>. Paris: Éditions du Seuil, 2000.</p>
<p>Webster, Charles. <i>Paracelsus: Medicine, Magic, and Mission at the End of Time</i>. New Haven: Yale University Press, 2008.</p>""",

    "nicholas_of_cusa": """<p>Nicholas of Cusa (1401–1464), the German cardinal, theologian, and natural philosopher, stands as one of the crucial transitional figures between medieval scholasticism and Renaissance Neoplatonism, whose philosophical innovations profoundly influenced how later thinkers engaged with Hermetic texts and magical philosophy. His doctrine of the <i>coincidentia oppositorum</i> (coincidence of opposites)—the vision that contradictions dissolve in the divine unity—provided a philosophical framework for understanding the unity underlying apparent multiplicity in the cosmos. This doctrine, combined with his mystical theology and natural philosophy, made Cusa an essential predecessor to Renaissance Hermeticism.</p>

<h2>Mystical Theology and Infinite Cosmology</h2>
<p>Cusa's <i>De Docta Ignorantia</i> (On Learned Ignorance) proposes that true knowledge of God consists not in rational demonstration but in the recognition that all rational categories fail before infinite divine reality. This paradoxical vision—that wisdom consists in understanding the limitations of knowledge—shaped Renaissance approaches to mystery and the unknowable aspects of divinity. Cusa's cosmological innovations, particularly his assertion that the universe is infinite and that the Earth is not at the center, prefigured Copernican revolution while retaining metaphysical rather than merely mechanical motivations. His vision of an infinite universe animated by God resonated profoundly with later Hermetic thinkers like Giordano Bruno, who extended Cusa's infinity of worlds into a comprehensive Hermetic cosmology.</p>

<h2>Influence on Renaissance Platonism</h2>
<p>Cusa's emphasis on the incomprehensibility of infinite divinity combined with the possibility of human knowledge through mystical experience provided a framework for understanding the Hermetic corpus. The conviction that multiplicity emanates from and returns to divine unity, that the human possesses divine capacities, and that nature itself is animated by divine principles—all Cusan doctrines—became central to Renaissance Hermetic philosophy. Marsilio Ficino and subsequent Neoplatonists integrated Cusan thought with Platonic and Hermetic sources.</p>

<h2>Literature</h2>
<p>Nicholas of Cusa. <i>On Learned Ignorance</i>. Trans. Jasper Hopkins. Minneapolis: Arthur J. Banning Press, 1981.</p>
<p>Nicholas of Cusa. <i>The Vision of God</i>. Trans. Emma Gurney Salter. New York: Frederick Ungar, 1960.</p>
<p>Hanegraaff, Wouter J. <i>Hermetic Spirituality and the Historical Imagination</i>. Leiden: Brill, 2022.</p>
<p>Copenhaver, Brian P., and Charles B. Schmitt. <i>Renaissance Philosophy</i>. Oxford: Oxford University Press, 1992.</p>
<p>Cassirer, Ernst. <i>The Individual and the Cosmos in Renaissance Philosophy</i>. Philadelphia: University of Pennsylvania Press, 1963.</p>""",

    "albertus_magnus": """<p>Albertus Magnus (c. 1200–1280), the German Dominican friar and bishop, stands as one of the most learned medieval scholars, whose encyclopedic synthesis of Aristotelian natural philosophy with Christian theology gave intellectual respectability to the study of natural science, alchemy, and the occult sciences in the medieval West. Though primarily known as a scholastic theologian and the teacher of Thomas Aquinas, Albertus engaged seriously with alchemy, astrology, and natural magic, treating them as legitimate pursuits grounded in the understanding of natural principles. His willingness to integrate diverse sources—Greek, Islamic, and Jewish philosophy alongside Christian theology—and to defend the possibility of genuine natural knowledge established him as a crucial precursor to Renaissance philosophical syncretism.</p>

<h2>Natural Philosophy and the Occult Sciences</h2>
<p>Albertus Magnus's extensive writings on natural philosophy, particularly his commentaries on the pseudo-Aristotelian <i>Liber de Causis</i> (Book of Causes, a Neoplatonic text) and his treatises on minerals and alchemy, demonstrate his conviction that the natural world operated according to intelligible principles knowable through reason and observation. Though he approached alchemy cautiously, skeptical of transmutation claims, he defended the legitimacy of alchemical investigation and integrated alchemical concepts into his natural philosophy. His recognition of occult qualities and hidden properties in natural substances provided the framework within which subsequent medieval and Renaissance thinkers developed theories of natural magic. Albertus's emphasis on the correspondence between the celestial and terrestrial realms, and his treatment of astrology as a legitimate natural science, established patterns of thought that would become foundational to Renaissance Hermeticism.</p>

<h2>Bridge Between Antiquity and Modernity</h2>
<p>Albertus Magnus represents the crucial medieval moment at which Islamic and Greek learning, preserved and transmitted through Islamic sources, became integrated into Christian European thought. His synthesis—grounded in scholastic method but open to the full range of ancient philosophical and mystical sources—provided a template for the Renaissance engagement with recovered Hermetic texts. His student Thomas Aquinas would refine Albertus's integration of philosophy and theology, but it was Albertus who pioneered the method.</p>

<h2>Literature</h2>
<p>Albertus Magnus. <i>Book of Minerals</i>. Trans. Dorothy Wyckoff. Oxford: Clarendon Press, 1967.</p>
<p>Weisheipl, James A. <i>Albertus Magnus and the Sciences: Commemorative Essays</i>. Toronto: PIMS, 1980.</p>
<p>Burnett, Charles. <i>Adelard of Bath: An English Scientist and Arabist of the Early Twelfth Century</i>. London: Warburg Institute, 1987.</p>
<p>Hanegraaff, Wouter J. <i>Hermetic Spirituality and the Historical Imagination</i>. Leiden: Brill, 2022.</p>
<p>Lindberg, David C. <i>The Beginnings of Western Science</i>. Chicago: University of Chicago Press, 2007.</p>""",
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
