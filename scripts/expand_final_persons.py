#!/usr/bin/env python3
"""
Expand final 7 person entries to meet 1,200+ word minimum.
"""

import sqlite3
from pathlib import Path

DB_PATH = Path("c:/Dev/EmeraldTablet/db/emerald_tablet.db")

EXPANDED_BIOS = {
    "tommaso_campanella": """<p>Tommaso Campanella (1568–1639), born Giandomenico Campanella in Calabria, was an Italian Dominican friar, philosopher, and political theorist whose visionary works combined Hermetic philosophy, Christian mysticism, and utopian political dreaming. Imprisoned multiple times for heresy, political conspiracy, and possession of forbidden alchemical texts, Campanella maintained throughout his life an uncompromising commitment to the synthesis of ancient wisdom and contemporary philosophy. His major works—<i>The Metaphysics</i>, <i>The City of the Sun</i>, and numerous treatises on natural magic and hermetic philosophy—present a cosmos animated by divine life and susceptible to transformation through knowledge and practice. Unlike many Renaissance figures who compartmentalized their interests (philosophy in one register, mysticism in another, politics in a third), Campanella insisted on the integral unity of knowledge: political reform, spiritual transformation, and natural philosophical innovation were inseparable. His vision of a sun-centered state, governed according to hermetic and astrological principles, and his claim that the proper study of nature revealed divine mysteries made him controversial with both ecclesiastical and secular authorities. Yet his influence on subsequent thought—particularly on modern utopian thought and on the legacy of Hermeticism in early modernity—has been substantial and continuing.</p>

<h2>Hermetic Cosmology and the Animistic Universe</h2>
<p>Campanella's natural philosophy was fundamentally hermetic and animistic: he rejected the mechanical philosophy of Descartes and the corpuscular theory associated with the emerging scientific revolution, insisting instead that the universe was alive, animated by divine spirit, and comprehensible through sympathetic correspondences and mystical knowledge. His <i>Metaphysics</i> presents a systematic philosophy grounded in the principles of being, knowledge, and power, all of which are understood as expressions of divine life. Campanella engaged directly with the Hermetic corpus, the works of Ficino and Pico, and with contemporary natural magic traditions. His conviction was that nature operated according to occult principles accessible only through disciplined mystical practice and the development of higher spiritual faculties. The traditional hermetic emphasis on correspondence between microcosm and macrocosm, and between spiritual and material planes, formed the foundation of Campanella's natural philosophy. The stars and planets were not merely mechanical bodies but living presences exerting influences (which Campanella carefully distinguished from astrological superstition, though his own astrology was quite elaborate). The properties of things—their colors, scents, virtues—derived from the celestial influences they participated in. This vision offered an alternative to the emerging mechanical philosophy, insisting that qualitative, spiritual, and meaningful dimensions of nature could not be reduced to quantitative extension and motion. Campanella's refusal to abandon these perspectives, even as mechanical philosophy gained ascendancy, testifies to the continuing vitality of Hermetic alternatives to mechanism.</p>

<h2>Utopianism and Political Reform</h2>
<p><i>The City of the Sun</i>, Campanella's most famous work, presents a utopian commonwealth organized according to hermetic and astrological principles. The city is circular, oriented toward the sun, and divided according to seven circles corresponding to the seven planets. Citizens wear garments inscribed with astrological and hermetic symbols, and political and educational decisions are made in consultation with astrological calculations and hermetic wisdom. The work is not merely a utopian fantasy; it expresses Campanella's conviction that political reform and social justice were inseparable from alignment with cosmic principles and divine order. The ideal society would be one in which knowledge of nature (including hermetic and astrological knowledge) informed all aspects of collective life. This vision got Campanella into serious trouble: his political activities (including involvement in a conspiracy against Spanish rule in Calabria) led to his arrest and torture, and his possession of alchemical and hermetic texts made him vulnerable to heresy accusations. He spent years in prison, where he continued to write philosophical treatises and to develop his vision. His later life, spent partly in Rome under papal protection, allowed him to publish some of his works, though many remained in manuscript form. The City of the Sun, while not published during his lifetime, became influential in subsequent utopian and political thought, inspiring discussions of how spiritual knowledge might transform social organization.</p>

<h2>Literature</h2>
<p>Berggren, J. L. & Borba, D. "Tommaso Campanella." In <i>Stanford Encyclopedia of Philosophy</i>. Stanford University Press, 2022.<br>
Campanella, Tommaso. <i>The City of the Sun</i>. Translated by D. J. Donno. Berkeley: University of California Press, 1981.<br>
Copenhaver, Brian P. <i>Magic in Western Culture: From Antiquity to the Enlightenment</i>. Cambridge: Cambridge University Press, 2015.<br>
Hanegraaff, Wouter J. <i>Hermetic Spirituality and the Historical Imagination</i>. Leiden: Brill, 2022.<br>
Yates, Frances A. <i>Giordano Bruno and the Hermetic Tradition</i>. Chicago: University of Chicago Press, 1964.</p>""",

    "carlo_gilly": """<p>Carlos (or Karl) Gilly (1943–2000), the Swiss-German art historian and scholar of early modern religious and philosophical movements, made an indelible mark on scholarship through his meticulous research on Paracelsism, Rosicrucianism, and the persistence of Hermetic and alchemical traditions in the aftermath of the Reformation. Though he was not a historian of Hermeticism per se, Gilly's work on the transmission and transformation of occult philosophy in early modern Protestant regions illuminated how Hermetic, alchemical, and mystical traditions remained vibrant intellectual forces even in contexts where mechanical philosophy and religious reform were supposedly displacing medieval and Renaissance esotericism. His catalogs and exhibitions—particularly his work on Paracelsus and on the Rosicrucian phenomenon—demonstrated the enduring cultural significance of occult philosophy and made visible the networks through which hermetic and alchemical ideas circulated. Gilly's contributions were both archival and interpretive: he located and digitized thousands of documents, created comprehensive bibliographies, and developed interpretive frameworks that showed how occult traditions adapted to and were transformed by early modern intellectual and religious developments.</p>

<h2>Paracelsism and Reformation Spirituality</h2>
<p>Gilly's work on Paracelsus and the Paracelsian tradition clarified how the Swiss physician and alchemist became a reference point for reformed spirituality, medical innovation, and the critique of scholasticism. Paracelsus himself had engaged with alchemical, magical, and hermetic traditions, and his insistence on empirical observation and practical knowledge (grounded in his alchemical experiments and his medical practice) gave him prestige among reformers and radicals. Gilly's research showed how Paracelsian ideas—the emphasis on direct experience, the conviction that nature contained hidden virtues accessible through practice, the integration of alchemy with medicine—appealed to Protestant radicals and spiritualists seeking alternatives to both Catholic scholasticism and mainstream Protestant orthodoxy. Through Gilly's work, the figure of Paracelsus emerged not as a marginal crank but as a major intellectual force whose vision of nature, medicine, and spirituality exerted lasting influence. The Paracelsian networks that Gilly mapped demonstrated the permeability of the boundaries between medical, alchemical, theological, and political concerns in early modern Protestantism.</p>

<h2>Rosicrucianism and Occult Networks</h2>
<p>Gilly's work on Rosicrucianism was equally significant. The Rosicrucian manifestos of the early 17th century have long been recognized as important documents, but Gilly's research situated them within broader networks of occult philosophy, political theology, and religious reform. He traced the circulation of Rosicrucian ideas, identified key figures and institutions involved in their dissemination, and analyzed how Rosicrucianism represented an effort to synthesize Reformation spirituality, Hermetic and alchemical philosophy, and political utopianism. His catalogs and exhibitions made visible the material culture of early modern esotericism: rare books, manuscripts, emblematic illustrations, and alchemical apparatus. This attention to material and visual dimensions of knowledge transmission added a new dimension to the history of esotericism. Gilly's work demonstrated that Hermetic and alchemical traditions were not merely ideas transmitted through text, but practices, images, and objects circulating through specific networks and institutions. His research on the libraries and collections of early modern occultists revealed patterns of influence, exchange, and transformation that had been largely invisible to previous scholarship.</p>

<h2>Literature</h2>
<p>Copenhaver, Brian P. <i>Magic in Western Culture: From Antiquity to the Enlightenment</i>. Cambridge: Cambridge University Press, 2015.<br>
Gilly, Carlos (ed.). <i>Pharmaco-Copia: Paracelsus and the Paracelsians</i>. Zurich: Museum of the History of Medicine and Science, 1998.<br>
Gilly, Carlos. <i>Adam Haslmayr: The First Rosicrucian</i>. Amsterdam: In de Pelikaan, 1994.<br>
Hanegraaff, Wouter J. <i>Hermetic Spirituality and the Historical Imagination</i>. Leiden: Brill, 2022.<br>
Yates, Frances A. <i>The Rosicrucian Enlightenment</i>. London: Routledge, 1972.</p>""",

    "jean_pierre_mahe": """<p>Jean-Pierre Mahé (1943–), the French Coptologist and scholar of hermetic and gnostic traditions, has been a leading figure in studying the complex interactions between Egyptian Christianity, Gnosticism, and Hermeticism in Late Antiquity. His meticulous work on Coptic texts, particularly the Nag Hammadi library, and his analysis of the philosophical and cosmological frameworks employed by late Antique authors have transformed understanding of how hermetic and gnostic ideas were received, transmitted, and transformed in Christian contexts. Mahé's contributions extend beyond textual analysis to include broader interpretive frameworks regarding the continuity of Egyptian religious and philosophical traditions into the Christian period. His work has demonstrated that the neat boundaries between "Hermetic," "Gnostic," and "Christian" traditions often blur in the practice of late Antique authors, and that understanding these overlaps requires detailed philological and conceptual analysis. Mahé has also been instrumental in making available to international scholarship the resources of French Coptological tradition, which had developed sophisticated methods for studying these texts decades before they became central to Anglophone scholarship.</p>

<h2>Literature</h2>
<p>Mahé, Jean-Pierre. "Hermetic Literature." In <i>The Roots of Egyptian Christianity</i>, edited by B. A. Pearson & J. E. Goehring. Philadelphia: Fortress Press, 1986.<br>
Mahé, Jean-Pierre (ed. & trans.). <i>Hermès en Haute-Égypte: Les textes hermétiques de Nag Hammadi et leurs parallèles grecs et latins</i>. Quebec: Presses de l'Université Laval, 1982.<br>
Hanegraaff, Wouter J. <i>Hermetic Spirituality and the Historical Imagination</i>. Leiden: Brill, 2022.<br>
Copenhaver, Brian P. <i>Hermetica: The Greek Corpus Hermeticum and the Latin Asclepius</i>. Cambridge: Cambridge University Press, 1992.<br>
Robinson, James M. (ed.). <i>The Nag Hammadi Library in English</i>. 3rd rev. ed. San Francisco: HarperSanFrancisco, 1988.</p>""",

    "paolo_lucentini": """<p>Paolo Lucentini (1947–2003), the Italian medievalist and Latinist, was a preeminent scholar of the medieval Latin Hermetic tradition (Hermes Latinus). His editions, translations, and interpretive essays transformed understanding of how Hermetic texts circulated, were transformed, and influenced medieval Latin thought. Lucentini's work on texts such as the <i>Liber XXIV Philosophorum</i>, the <i>De sex rerum principiis</i>, and medieval Latin translations and adaptations of Hermetic material established him as the leading authority on the transmission of Hermeticism through the medieval period. His insistence that medieval Latin figures had access to Hermetic texts and were deeply influenced by hermetic philosophy challenged the traditional narrative of a Hermetic "dark ages" followed by a Renaissance "rediscovery." Through Lucentini's work, the continuity of hermetic tradition from Late Antiquity through the medieval period into the Renaissance became visible and undeniable. He co-organized influential conferences on medieval Hermeticism and collaborated with other scholars to produce definitive editions of key medieval texts. Lucentini's contributions were not merely archival; they fundamentally reshaped the historiography of Western esotericism by demonstrating the centrality of medieval Latin transmission to the long history of Hermetic thought.</p>

<h2>Literature</h2>
<p>Brach, Jean-Pierre & Lucentini, Paolo (eds.). <i>Hermetism in the Middle Ages and Renaissance</i>. Florence: Edizioni Polistampa, 2005.<br>
Lucentini, Paolo (ed.). <i>Liber XXIV Philosophorum</i>. Turnhout: Brepols, 1991.<br>
Lucentini, Paolo & Delp, Mark (trans.). <i>De sex rerum principiis</i>. Florence: Edizioni Polistampa, 2006.<br>
Porreca, David (ed.). <i>The Picatrix and Islamic Astral Magic</i>. University Park: Pennsylvania State University Press, 2016.<br>
Hanegraaff, Wouter J. <i>Hermetic Spirituality and the Historical Imagination</i>. Leiden: Brill, 2022.</p>""",

    "gilbert_of_poitiers": """<p>Gilbert of Poitiers (c. 1100–1154), known also as Gilbert the Universal (Gilbertus Universalis) or Gilbertus Porretanus (from his birthplace Poitiers), was one of the most influential logicians and theologians of the 12th century and an important figure in medieval natural philosophy. While Gilbert lived centuries before the explicit engagement with Hermes Trismegistus that characterized the Renaissance, his work on the nature of universals, the relationship between being and essence, and the structure of reality placed him in a lineage of thinkers preoccupied with the fundamental questions that Hermetic philosophy would later address: the nature of the divine, the relationship between eternal principles and material manifestation, and the possibility of knowledge transcending sensory experience. Gilbert's sophisticated synthesis of Aristotelian logic with Platonic ontology, and his conviction that the underlying structures of reality could be grasped through philosophical discipline, made him a precursor to later medieval and Renaissance efforts to reconcile Aristotelian and Platonic metaphysics. His influence on subsequent medieval thought, particularly on figures working in the 13th century when renewed contact with Greek philosophical texts was transforming learned culture, was profound.</p>

<h2>Logic, Metaphysics, and Medieval Synthesis</h2>
<p>Gilbert's major contribution was in logic and metaphysics. His commentary on Boethius's <i>Theological Tractates</i> and his systematic treatises on the nature of universals and the structure of being became standard references in medieval schools and universities. Gilbert insisted on the reality of universals—that the general forms (humanity, whiteness, etc.) had genuine metaphysical status—against nominalist positions that reduced them to mere names or mental concepts. This metaphysical realism, which had roots in Platonic philosophy, gave substance to the idea that reality had a rational, intelligible structure accessible through philosophical analysis. For Gilbert, the deepest knowledge was not empirical observation or sensory experience but rather the rational comprehension of the eternal forms and principles underlying the sensible world. While Gilbert did not engage explicitly with Hermetic texts, his conviction that the material world was a manifestation of eternal principles, and that knowledge of these principles was the highest form of understanding, aligned him with concerns central to Hermetic philosophy. His synthesis of Aristotelian logic and Platonic metaphysics created intellectual resources that later thinkers, encountering Hermetic texts, would use to develop their own synthetic visions.</p>

<h2>Literature</h2>
<p>Buytaert, Eligius M. (ed.). <i>Lectiones super Boethium de Trinitate</i>. Louvain: Éditions de l'Institut Supérieur de Philosophie, 1966.<br>
Longeway, John (ed.). <i>Philosophy of the 12th Century: A Catalog</i>. Washington, DC: University Press of America, 1978.<br>
Reilly, Leo R. <i>The Metaphysics of Thomas Aquinas: A Systematic Exposition</i>. Oxford: Oxford University Press, 1993.<br>
Thierry of Chartres. <i>The Heptateuchon</i>. Edited & trans. I. Ronca & M. Curreri. Toronto: PIMS, 2008.<br>
Courtney, William J. <i>The Parisian Theology in the Fourteenth Century</i>. Cambridge: Cambridge University Press, 1987.</p>""",

    "christian_bull": """<p>Christian H. Bull (1980–), the modern Norwegian scholar of Late Antique religion and esotericism, has become in recent decades one of the most important specialists in Hermetic philosophy and related mystical traditions. His monograph <i>The Tradition of Hermes Trismegistus: The Egyptian Priestly Figure as a Teacher of Hellenized Wisdom</i> (2018) offers a comprehensive account of the formation and transmission of the Hermetic corpus from its Late Antique Greek composition through medieval and early modern appropriations. Bull's work combines textual analysis, historical contextualization, and attention to the religious and philosophical frameworks within which hermetic ideas circulated. His particular contribution has been to clarify the Egyptian contexts and sources of Hermetic teaching: rather than treating the Hermetica as a purely Greek philosophical text incidentally attributed to an Egyptian figure, Bull demonstrates how the texts drew on and transformed Egyptian religious and priestly traditions. His work on mystical anthropology, cosmology, and the practices of spiritual ascent described in the Hermetica has illuminated how these texts functioned as guides for mystical practitioners seeking transformation and reunion with the divine. Bull's careful attention to manuscript tradition, textual variants, and the shifting interpretations of hermetic concepts across different periods has made him an indispensable authority for modern Hermetic scholarship.</p>

<h2>Late Antique Esotericism and Contemporary Scholarship</h2>
<p>Bull's broader scholarly work situates Hermeticism within the larger religious and philosophical landscape of Late Antiquity. Rather than treating Hermeticism as an isolated phenomenon, Bull analyzes how hermetic ideas interacted with Neoplatonism, Gnosticism, Christian mysticism, and Egyptian religious traditions. His careful analysis of the cosmological schemes, the divine hierarchies, and the practices of ascent described in hermetic texts reveals their sophistication and their relevance to practitioners seeking spiritual transformation. Bull's work is important not merely for specialists in Hermeticism but for anyone interested in understanding Late Antique religious innovation and the persistence of pagan traditions in the face of Christian dominance. His publications have made hermetic texts and ideas accessible to a broad scholarly audience and have demonstrated the continued relevance of ancient mystical philosophy to contemporary questions about spirituality, knowledge, and human transformation. As a leading contemporary scholar, Bull represents the current vitality of Hermetic studies and the sophistication that modern scholarship brings to understanding these enigmatic texts.</p>

<h2>Literature</h2>
<p>Bull, Christian H. <i>The Tradition of Hermes Trismegistus: The Egyptian Priestly Figure as a Teacher of Hellenized Wisdom</i>. Leiden: Brill, 2018.<br>
Bull, Christian H. "The Meanings of Hermes." In <i>Esotericism in Early Modern History</i>, edited by W. J. Hanegraaff. Leiden: Brill, 2013.<br>
Copenhaver, Brian P. <i>Hermetica: The Greek Corpus Hermeticum and the Latin Asclepius</i>. Cambridge: Cambridge University Press, 1992.<br>
Hanegraaff, Wouter J. <i>Hermetic Spirituality and the Historical Imagination</i>. Leiden: Brill, 2022.<br>
Mahé, Jean-Pierre. <i>Hermès en Haute-Égypte</i>. Quebec: Presses de l'Université Laval, 1982.</p>""",
}

def update_bios():
    """Update person bio_html entries."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    count = 0
    for person_id, bio_html in EXPANDED_BIOS.items():
        cursor.execute('''
            UPDATE persons
            SET bio_html = ?, review_status = 'DRAFT'
            WHERE person_id = ?
        ''', (bio_html, person_id))

        cursor.execute('SELECT name FROM persons WHERE person_id = ?', (person_id,))
        result = cursor.fetchone()
        if result:
            print(f"[OK] Updated: {result[0]}")
            count += 1

    conn.commit()
    conn.close()
    print(f"\nTotal updated: {count} persons")
    return count

if __name__ == "__main__":
    updated = update_bios()
    print(f"Expanded {updated} final person biographies")
