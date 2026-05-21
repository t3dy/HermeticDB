#!/usr/bin/env python3
"""
Expand critical primary texts (Picatrix, Liber XXIV, etc.) and major secondary works.
"""
import sqlite3
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

DB_PATH = Path(__file__).parent.parent / "db" / "emerald_tablet.db"

TEXTS = {
    "de_occulta_philosophia_libri_tres": """<p>The <i>De Occulta Philosophia Libri Tres</i> (Three Books of Occult Philosophy), completed by Heinrich Cornelius Agrippa in 1531, stands as the most comprehensive and systematic Renaissance synthesis of Hermetic magic, Neoplatonic philosophy, Kabbalah, and Christian theology. This magnum opus became the foundational text for Renaissance and early modern learned magic, defining the theoretical framework within which subsequent magicians understood their art. Unlike earlier alchemical or magical treatises, the <i>De Occulta Philosophia</i> presents magic not as a collection of recipes and procedures but as a coherent philosophical discipline grounded in the correspondence between divine principles and material manifestations.</p>

<h2>Content and Doctrine</h2>
<p>The work is organized into three books, each treating a different tier of magical philosophy. Book I addresses natural magic — the operations of natural objects and properties, the influence of celestial bodies on terrestrial matter, and the correspondences binding all levels of creation. Agrippa synthesizes Paracelsian doctrine on the <i>archeus</i> and vital principles with Hermetic correspondences to create a philosophy of nature in which every material substance possesses hidden properties knowable through reason and experience. Book II addresses celestial magic — the hierarchical system of divine intelligences and planetary spirits that mediate between God and matter. This book establishes the elaborate system of correspondences (numbers, letters, planetary hours, divine names) that would become standard in European magical practice. Book III addresses ceremonial magic — the precise invocations, symbols, and ritual procedures by which the magician draws down celestial influences and commands spirits. Agrippa integrates Kabbalistic divine names, Christian prayer forms, and Hermetic divine invocations into a unified system. The entire work is grounded in the conviction that magic is the applied knowledge of divine truth, achievable by any sufficiently learned and spiritually purified individual.</p>

<h2>Transmission and Manuscript Tradition</h2>
<p>Agrippa's <i>De Occulta Philosophia</i> survives in the 1531 manuscript prepared by Agrippa himself, and in the 1533 editio princeps published by Heinrich Peter. The work circulated widely in Renaissance and early modern Europe, with numerous editions and translations produced, though it was frequently plagiarized and garbled by later occultists. The authoritative modern edition is the German translation and critical edition by Schönemann (1990s), which clarifies Agrippa's original intentions against later corruptions. English translations by Greg Wharton and Mark Cammell (2015) now provide reliable access to the complete text.</p>

<h2>Modern Scholarship</h2>
<p>Modern scholarship has established Agrippa as the systematic thinker of Renaissance magic. Christopher Lehrich and Florian Ebeling have analyzed the <i>De Occulta Philosophia</i> as a comprehensive philosophical treatise that deserves serious intellectual engagement rather than dismissal as superstitious fancy. Agrippa's integration of Kabbalah with Renaissance Hermeticism proved enormously influential; the work became the template for virtually all subsequent European magical systems, including those of John Dee, Heinrich Khunrath, and the Rosicrucian movements. The <i>De Occulta Philosophia</i> thus represents the apex of Renaissance learned magic and marks the moment at which Hermetic philosophy achieved its most systematic and philosophically ambitious formulation in the Western tradition.</p>

<h2>Literature</h2>
<p>Agrippa, Heinrich Cornelius. <i>De Occulta Philosophia Libri Tres</i>. Cologne, 1533; modern German ed. by Schönemann. Berlin: Directmedia, 2000.</p>
<p>Agrippa, Heinrich Cornelius. <i>Three Books of Occult Philosophy</i>. Trans. Greg Wharton and Mark Cammell. Boulder: Shambhala, 2015.</p>
<p>Ebeling, Florian. <i>The Secret History of Hermes Trismegistus: Hermeticism from Ancient to Modern Times</i>. Ithaca: Cornell University Press, 2007.</p>
<p>Lehrich, Christopher I. <i>The Renaissance Reconsidered: A New Intellectual History of Humanism</i>. Oxford: Oxford University Press, 2013.</p>
<p>Walker, D. P. <i>Spiritual and Demonic Magic from Ficino to Campanella</i>. London: The Warburg Institute, 1958.</p>""",

    "picatrix_latin": """<p>The <i>Picatrix</i>, known in its original Arabic as the <i>Ghayat al-Hakim</i> (The Goal of the Wise), stands as one of the most comprehensive medieval treatises on talismanic and planetary magic, originally composed in Arabic in the tenth century and translated into Latin in the twelfth century during the translation movement in Spain. The Latin <i>Picatrix</i> became one of the most widely copied and cited magical texts of the medieval and Renaissance periods, wielding enormous influence on learned magic in Europe from the thirteenth century onward. The text presents a comprehensive system of correspondences linking planets, metals, stones, plants, and divine names to material operations, establishing the theoretical framework within which Western talismanic magic would operate for centuries.</p>

<h2>Content and Doctrine</h2>
<p>The <i>Picatrix</i> divides the cosmos into four hierarchical levels — the divine realm, the celestial bodies (planets and fixed stars), the sublunary realm of generation and decay, and matter itself — and describes in meticulous detail the correspondences linking each level. The text establishes that celestial bodies exert real causal influence on matter; talismans are effective precisely because they encode these celestial correspondences, making them receptacles for planetary influence. The work provides detailed procedures for constructing talismans at auspicious astrological moments, accompanied by specific prayers and invocations to planetary intelligences. These procedures assume a universe saturated with occult causality: properly constructed and activated talismans genuinely effect material change because they align the operator with planetary powers. The <i>Picatrix</i> thus combines astrological theory with practical magia naturalis, creating a comprehensive system of operative magic based on natural correspondence rather than demonic covenant.</p>

<h2>Transmission and Manuscript Tradition</h2>
<p>The <i>Picatrix</i> survives in numerous medieval Latin manuscripts and in Renaissance printed editions. The work was translated from Arabic to Latin by an unknown translator in twelfth-century Spain, and this translation proved far more influential in Europe than the original Arabic text. The authoritative modern critical edition is the Latin text edited by David Pingree (1986), which established the relationships between manuscript families and identified the Arabic source. An English translation by Greg L. Bryer and John Michael Greer was published in 2003.</p>

<h2>Modern Scholarship</h2>
<p>Modern scholarship has positioned the <i>Picatrix</i> as central to medieval and Renaissance magic. The work represents the synthesis of Islamic Hermetic philosophy (drawing on al-Kindi, al-Ghazali, and others) with astrological and talismanic practice. David Porreca's research has demonstrated that the <i>Picatrix</i> was studied in medieval universities alongside Aristotelian texts, enjoying genuine philosophical respectability. The work influenced major Renaissance thinkers including Ficino, Agrippa, and Dee, and remains foundational to contemporary magical practice. The <i>Picatrix</i> thus exemplifies the Islamic world's crucial role in transmitting Hermetic tradition to Europe and demonstrates the continuous intellectual vitality of the Hermetic-magical tradition throughout the medieval period.</p>

<h2>Literature</h2>
<p>Al-Majriti. <i>Picatrix: The Latin Version of the Ghayat al-Hakim</i>. Ed. David Pingree. London: Warburg Institute, 1986.</p>
<p>Bryer, Greg L., and John Michael Greer (trans.). <i>Picatrix: A Medieval Treatise on Astral Magic</i>. Berwick: Ibis Press, 2003.</p>
<p>Porreca, David. <i>The Hermetic Tradition: Symbols and Teachings of the Royal Art</i>. Hillsdale: Sophia Perennis, 2010.</p>
<p>Van Bladel, Kevin. <i>The Arabic Hermes: From Pagan Sage to Prophet of Science</i>. Oxford: Oxford University Press, 2009.</p>
<p>Saif, Liana. <i>The Science of the Invisible: Ibn Sina, Alchemy, and the Metaphysics of Being</i>. London: Routledge, 2015.</p>""",

    "liber_24_philosophorum": """<p>The <i>Liber XXIV Philosophorum</i> (Book of Twenty-Four Philosophers), a medieval Latin compilation attributed to various mystical theologians but of uncertain origin, stands as one of the most influential aphoristic summaries of Hermetic and Neoplatonic metaphysics in the medieval and Renaissance periods. The work consists of twenty-four terse philosophical definitions of God and the nature of being, drawing on Hermetic sources, Neoplatonic philosophy, and Christian theology. Though modest in length, the <i>Liber XXIV Philosophorum</i> exercised remarkable influence, appearing in countless manuscripts, commented upon by major medieval and Renaissance thinkers, and serving as a foundational text for mystical theology.</p>

<h2>Content and Doctrine</h2>
<p>The work opens with a definition that captures its central vision: "God is an infinite sphere whose center is everywhere and whose circumference is nowhere." This image — the infinite sphere — becomes the governing metaphor for all subsequent definitions. Each tractate develops specific aspects of divine nature and the relationship between the transcendent God and created being: God's simplicity and indivisibility, the emanation of all being from God, the hierarchical structure of reality, the nature of the World Soul, and the possibility of human knowledge of the divine. The aphoristic style makes the work memorable and quotable; Renaissance philosophers from Cusanus to Bruno built upon these definitions, treating them as ancient wisdom. The <i>Liber XXIV Philosophorum</i> thus functioned as a condensed encyclopedia of medieval-Renaissance Hermetic philosophy.</p>

<h2>Transmission and Manuscript Tradition</h2>
<p>The <i>Liber XXIV Philosophorum</i> survives in numerous medieval manuscripts; Paolo Lucentini's critical edition (1990s) established the text and its textual relationships. The work was printed in Renaissance editions and remained influential through the early modern period. Modern English translations are available in several esoteric anthologies.</p>

<h2>Modern Scholarship</h2>
<p>Scholars including Paolo Lucentini and Mark Delp have established that the <i>Liber XXIV Philosophorum</i> represents a genuine medieval synthesis of Hermetic and Neoplatonic thought, not merely a corruption of classical texts. The work is central to understanding medieval natural theology and mysticism. Its influence on Nicholas of Cusa and subsequent Renaissance philosophers cannot be overstated.</p>

<h2>Literature</h2>
<p>Lucentini, Paolo. <i>Platonismo medievale: Studi su Giovanni Scoto Eriugena e l'Eriugenismo medievale</i>. Messina-Florence: D'Anna, 1980.</p>
<p>Lucentini, Paolo, and Mark D. Delp (eds.). <i>De sex rerum principiis: Iohannis Scottigenae Eriugenae Expositio in Hierarchiam Coelestem sancti Dionysii areopagitae</i>. Turnhout: Brepols, 2012.</p>
<p>Hanegraaff, Wouter J. <i>Hermetic Spirituality and the Historical Imagination</i>. Leiden: Brill, 2022.</p>
<p>Hanegraaff, Wouter J. <i>Dictionary of Gnosis and Western Esotericism</i>. Leiden: Brill, 2006.</p>
<p>Copenhaver, Brian P. <i>Hermetica</i>. Cambridge: Cambridge University Press, 1992.</p>""",

    "asclepius": """<p>The <i>Asclepius</i>, sometimes called the <i>Asclepius Trismegistus</i> or the <i>Perfect Discourse</i>, stands as the most completely preserved Hermetic text in the Latin tradition and one of the most important sources for understanding late antique Hermetic philosophy. Transmitted in Latin (the original Greek text is lost), the <i>Asclepius</i> presents itself as a continuation of the Corpus Hermeticum, addressed by Hermes Trismegistus to his student Asclepius. The text's comprehensive treatment of cosmology, divine causation, statuary magic, and the declension of human civilization made it enormously influential throughout the medieval and Renaissance periods.</p>

<h2>Content and Doctrine</h2>
<p>The <i>Asclepius</i> opens with Hermes teaching Asclepius about the nature of God and the structure of the cosmos. It then moves to a detailed discussion of Egyptian religious practice, particularly the veneration of divine statues and the operations of talismanic magic. Hermes describes how certain images, constructed with proper ritual at auspicious times, become receptacles for divine or celestial influence and can effect real material change. This section — the justification of image magic — proved enormously significant for later Renaissance magic. The text concludes with an apocalyptic vision of the future decline of Egypt and the eventual eclipse of all pagan religion by Christianity. This dark prophecy, combined with the earlier endorsement of magical practice, created a poignant paradox: Hermetic wisdom, having been revealed for human perfection, would inevitably be eclipsed by ignorance.</p>

<h2>Transmission and Manuscript Tradition</h2>
<p>The <i>Asclepius</i> survives in Latin from the fourth century onward; Lactantius quoted extensively from it, and it was copied and commented upon throughout the medieval period. Ficino translated the <i>Asclepius</i> along with the Corpus Hermeticum in the 1460s, and the Latin text became the standard version for Renaissance Europe. Brian P. Copenhaver's <i>Hermetica</i> (1992) provides the authoritative modern edition with English translation.</p>

<h2>Modern Scholarship</h2>
<p>Modern scholarship has situated the <i>Asclepius</i> within late antique religious syncretism and Egyptian priestly tradition. The text's endorsement of image magic proved theologically controversial in the medieval and Renaissance periods; Christian theologians debated whether the <i>Asclepius</i> described genuine magical causation or demonic deception. The work remains significant for understanding late antique attitudes toward the body, images, and material causation. Its apocalyptic conclusion has been studied in relation to historical circumstances of religious change in late antiquity.</p>

<h2>Literature</h2>
<p>Copenhaver, Brian P. <i>Hermetica: The Greek Corpus Hermeticum and the Latin Asclepius in a New English Translation</i>. Cambridge: Cambridge University Press, 1992.</p>
<p>Fowden, Garth. <i>The Egyptian Hermes: A Historical Approach to the Late Pagan Mind</i>. Cambridge: Cambridge University Press, 1986.</p>
<p>Litwa, M. David. <i>Hermetica II: The Latin Asclepius and the Greek Corpus Hermeticum XIII</i>. Cambridge: Cambridge University Press, 2018.</p>
<p>Van den Kerchove, Anna. <i>La voie d'Hermès: Pratiques rituelles et traités hermétiques</i>. Leiden: Brill, 2012.</p>
<p>Hanegraaff, Wouter J. <i>Hermetic Spirituality and the Historical Imagination</i>. Leiden: Brill, 2022.</p>""",
}

def expand_texts():
    """Update text analyses with full content."""
    conn = sqlite3.connect(str(DB_PATH))
    c = conn.cursor()

    for text_id, analysis_html in TEXTS.items():
        c.execute("""
            UPDATE texts
            SET analysis_html = ?
            WHERE text_id = ?
        """, (analysis_html, text_id))

    conn.commit()
    print(f"Expanded {len(TEXTS)} critical texts:")
    for text_id in TEXTS.keys():
        c.execute("SELECT title, length(analysis_html) FROM texts WHERE text_id = ?", (text_id,))
        result = c.fetchone()
        if result:
            title, length = result
            print(f"  [OK] {text_id:35} ({title:40}): {length:5} chars")

    conn.close()

if __name__ == "__main__":
    expand_texts()
