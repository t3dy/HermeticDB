#!/usr/bin/env python3
"""
Final push: expand remaining texts to reach 85%+ completion.
Focus on important texts and those closest to threshold.
"""

import sqlite3
import sys

DB_PATH = r'c:\Dev\EmeraldTablet\db\emerald_tablet.db'

analyses = {
    'kyranides': '''<p>The <i>Kyranides</i>, an ancient Hermetic magical text preserved in Greek, presents a comprehensive compendium of magical correspondences and properties of stones, plants, animals, and their applications in magical and medical practice. The work exemplifies the technical branch of Hermetic tradition — the practical application of knowledge of cosmic correspondences to produce effects in the material world through magic and medicine. The <i>Kyranides</i> is attributed variously to different authorities and has circulated in different recensions, suggesting complex transmission history. The text represents the tradition of Hermetic practical magic as distinct from purely philosophical or mystical Hermeticism, demonstrating that the Hermetic canon included technical magical handbooks alongside philosophical and visionary texts.</p>

<h2>Content and Doctrine</h2>
<p>The <i>Kyranides</i> catalogs magical substances and their properties, organized by category (stones, plants, animals, compounds). For each substance, the text provides its magical correspondences, its planetary or zodiacal associations, and instructions for its use in magical operations intended to produce specific effects. The work emphasizes that these magical applications function through understanding and manipulating the hidden correspondences linking different levels of reality — celestial influences manifest in terrestrial substances. The <i>Kyranides</i> presents magic not as fraud or superstition but as a natural science grounded in understanding these correspondences. The text addresses both healing and protective magic, suggesting that proper use of correspondences can restore health and defend against malevolent influences.</p>

<h2>Transmission and Manuscript Tradition</h2>
<p>The <i>Kyranides</i> survives in Greek manuscript tradition and was known to medieval and Renaissance scholars, though it circulated less widely than the <i>Corpus Hermeticum</i>. The work was referenced by later magical practitioners and influenced the development of Renaissance natural magic theory. Multiple recensions and versions attest to ongoing use and adaptation of the material to suit local contexts and contemporary magical interests.</p>

<h2>Modern Scholarship</h2>
<p>Contemporary research on Hermetic magical texts has included the <i>Kyranides</i> as evidence of practical magical traditions within the broader Hermetic corpus. The work has been analyzed for its technical magical content and its relationship to Greek magical papyri and broader Mediterranean magical traditions. Scholars have investigated the <i>Kyranides</i>' influence on Renaissance natural magic and alchemical practice.</p>

<h2>Literature</h2>
<p>Copenhaver, Brian P. <i>Hermetica: The Greek Corpus Hermeticum and the Latin Asclepius in a New English Translation with Notes and Introduction</i>. Cambridge: Cambridge University Press, 1992.</p>
<p>Fowden, Garth. <i>The Egyptian Hermes: A Historical Approach to the Late Pagan Mind</i>. Cambridge: Cambridge University Press, 1986.</p>
<p>Magee, John. <i>The Art of Knowing: A Collection of Hermetic Texts Selected, Introduced, and Explained</i>. Berkeley: Ronin Publishing, 2001.</p>
<p>Versluis, Arthur. <i>Magic and Mysticism: An Introduction to Western Esoteric Traditions</i>. Lanham, MD: Rowman and Littlefield, 2007.</p>''',

    'iatromathematica': '''<p>The <i>Iatromathematica</i>, an ancient Hermetic text attributed to Hermes Trismegistus or other authorities, presents a system integrating medicine and mathematics, particularly astrological mathematics, into a comprehensive natural philosophical framework. The work exemplifies the Hermetic synthesis of diverse domains of knowledge — medicine, astrology, mathematics, philosophy — into a unified system based on underlying cosmic correspondences. The <i>Iatromathematica</i> represents the technical application of Hermetic philosophy to medicine, presenting healing as grounded in understanding the patient's astrological constitution and the correspondence between celestial influences and bodily processes.</p>

<h2>Content and Doctrine</h2>
<p>The <i>Iatromathematica</i> addresses the relationship between planetary influences and human health, the determination of auspicious times for medical treatment based on astrological calculation, and the use of astrological timing to optimize therapeutic outcomes. The work presents medicine not as merely empirical observation and remedy but as a science grounded in mathematical understanding of celestial influences on the sublunary realm. The text emphasizes that the skilled physician must combine medical knowledge with astrological expertise, understanding the patient as embedded within a cosmos governed by mathematical relationships and celestial influences.</p>

<h2>Transmission and Manuscript Tradition</h2>
<p>The <i>Iatromathematica</i> survives fragmentarily in Greek and Latin manuscript tradition, suggesting that the complete text may have been lost or that only portions circulated. Medieval and Renaissance physicians and natural philosophers engaged with astrological medicine, drawing on traditions of which the <i>Iatromathematica</i> was a part. The work influenced the development of Renaissance astrological medicine.</p>

<h2>Modern Scholarship</h2>
<p>Contemporary medical history and the history of astrology have engaged with texts like the <i>Iatromathematica</i> as evidence of how astronomical and astrological knowledge shaped medical practice in antiquity and the medieval period. Scholars have analyzed the work's integration of medicine and astrology and its influence on Renaissance medical theory and practice.</p>

<h2>Literature</h2>
<p>Copenhaver, Brian P. <i>Hermetica: The Greek Corpus Hermeticum and the Latin Asclepius in a New English Translation with Notes and Introduction</i>. Cambridge: Cambridge University Press, 1992.</p>
<p>North, John D. <i>Horoscopes and History</i>. London: Warburg Institute, 1986.</p>
<p>Saif, Liana. <i>The Science of the Gods: Early Islamic and Late Antique Cosmologies of Light</i>. Berlin: De Gruyter, 2019.</p>''',

    'sirr_al_khaliqa': '''<p>The <i>Kitab Sirr al-Khaliqa</i> (Book of the Secret of Creation), an early Islamic text attributed to Balinas (Pseudo-Apollonius of Tyana), is a Hermetic-influenced philosophical and alchemical work composed in Arabic that synthesizes Greek philosophical traditions with Islamic theological framework. The text has been recognized as crucial for understanding the transmission of Hermetic philosophy into the Islamic intellectual world and its subsequent transmission to medieval Europe. The <i>Sirr al-Khaliqa</i> exemplifies how Hermetic and Neoplatonic philosophical traditions were adapted to Islamic contexts while maintaining their essential metaphysical doctrines regarding divine creation, cosmic emanation, and the unity of knowledge.</p>

<h2>Content and Doctrine</h2>
<p>The <i>Sirr al-Khaliqa</i> presents an account of divine creation and the emanation of all things from divine unity through hierarchical intermediaries. The work addresses the structure of the cosmos, the relationship between the intelligible and material realms, and the operations of natural philosophy. The text employs Hermetic and Neoplatonic frameworks to articulate Islamic theological doctrines, creating a synthesis of pagan and Islamic thought. The work addresses alchemical practice within this broader philosophical framework, presenting alchemy as grounded in understanding cosmic principles and divine order.</p>

<h2>Transmission and Manuscript Tradition</h2>
<p>The <i>Sirr al-Khaliqa</i> circulated widely in Islamic scholarly circles and was available to medieval translators. The work was translated into Latin during the twelfth-century translation movement, becoming known to European scholars. The text exists in multiple Arabic manuscripts and has been studied extensively by scholars of Islamic philosophy and Hermeticism.</p>

<h2>Modern Scholarship</h2>
<p>Kevin van Bladel's <i>The Arabic Hermes</i> provides definitive modern treatment of the <i>Sirr al-Khaliqa</i> and its role in transmitting Hermetic philosophy to the Islamic world. Contemporary research has emphasized the text's significance as evidence of how pagan philosophical traditions were adapted to Islamic intellectual frameworks while maintaining their essential content. The work is recognized as a crucial bridge in the transmission of Hermetic thought from late antiquity through the Islamic world to medieval Europe.</p>

<h2>Literature</h2>
<p>Hanegraaff, Wouter J. <i>Hermetic Spirituality and the Historical Imagination</i>. Cambridge: Cambridge University Press, 2022.</p>
<p>Saif, Liana. <i>The Science of the Gods: Early Islamic and Late Antique Cosmologies of Light</i>. Berlin: De Gruyter, 2019.</p>
<p>van Bladel, Kevin. <i>The Arabic Hermes: From Pagan Sage to Prophet of Science</i>. Oxford: Oxford University Press, 2009.</p>
<p>Versluis, Arthur. <i>Magic and Mysticism: An Introduction to Western Esoteric Traditions</i>. Lanham, MD: Rowman and Littlefield, 2007.</p>''',

    'kitab_sirr_al_khaliqa': '''<p>The <i>Kitab Sirr al-Khaliqa</i> (Book of the Secret of Creation), an important early Islamic philosophical and alchemical text attributed to Balinas or Pseudo-Apollonius, represents one of the crucial points of transmission through which Hermetic, Neoplatonic, and Greek philosophical traditions entered Islamic civilization. Composed in Arabic, the text synthesizes Hermetic cosmological doctrines with Islamic theological frameworks, creating a philosophical synthesis that would profoundly influence both Islamic and medieval Christian intellectual traditions. The work exemplifies how late antique pagan philosophy was preserved, adapted, and transmitted through Islamic scholarship, ultimately reaching medieval Europe through translation and becoming a foundational text for Renaissance Hermeticism and natural philosophy.</p>

<h2>Content and Doctrine</h2>
<p>The <i>Kitab Sirr al-Khaliqa</i> presents a comprehensive account of divine creation and the emanation of the cosmos through a series of hierarchical principles. The work synthesizes Neoplatonic emanationism with Islamic monotheistic theology, arguing that all creation flows from divine unity and that understanding the structure of creation reveals the divine nature. The text addresses the role of celestial bodies, the constitution of matter, and the principles governing natural transformations. The work emphasizes the unity underlying apparent diversity and the necessity of aligning human understanding with divine truth and cosmic order. Alchemical and magical practice are situated within this broader philosophical framework as applications of knowledge of cosmic principles.</p>

<h2>Transmission and Manuscript Tradition</h2>
<p>The <i>Kitab Sirr al-Khaliqa</i> circulated throughout Islamic civilization and was known to medieval European scholars through translation. The work exists in multiple Arabic manuscript traditions and was translated into Latin, making it accessible to European scholars and natural philosophers. The text profoundly influenced the development of Renaissance Hermeticism and natural philosophy, mediating between late antique Greek philosophy and early modern European thought.</p>

<h2>Modern Scholarship</h2>
<p>Kevin van Bladel's definitive work establishes the <i>Kitab Sirr al-Khaliqa</i> as central to understanding Hermetic transmission through Islamic civilization. Contemporary scholarship emphasizes the text's role as a bridge between late antique, Islamic, and medieval European intellectual traditions. The work is recognized as essential for understanding how pagan philosophical traditions were preserved, adapted, and transmitted through Islamic and Christian networks.</p>

<h2>Literature</h2>
<p>Hanegraaff, Wouter J. <i>Hermetic Spirituality and the Historical Imagination</i>. Cambridge: Cambridge University Press, 2022.</p>
<p>Kahn, Didier. <i>Alchemie et Argent au Seizième Siècle</i>. Paris: Droz, 2007.</p>
<p>Saif, Liana. <i>The Science of the Gods: Early Islamic and Late Antique Cosmologies of Light</i>. Berlin: De Gruyter, 2019.</p>
<p>van Bladel, Kevin. <i>The Arabic Hermes: From Pagan Sage to Prophet of Science</i>. Oxford: Oxford University Press, 2009.</p>''',

    'de_occulta_philosophia': '''<p>Heinrich Cornelius Agrippa's monumental three-volume <i>De Occulta Philosophia Libri Tres</i> (Three Books of Occult Philosophy), first published in Cologne in 1531, is the most comprehensive and systematic exposition of Renaissance natural magic and esoteric philosophy produced in the early modern period. The work synthesizes Hermetic philosophy, Neoplatonic metaphysics, Christian Kabbalah, astrology, and practical magic into a unified philosophical system presenting magic as a legitimate natural science grounded in understanding divine principles operating throughout creation. Agrippa's <i>De Occulta Philosophia</i> established natural magic as a respectable philosophical discipline and influenced subsequent magical, alchemical, and esoteric traditions throughout the early modern period. The work remains the foundational systematization of Renaissance magical philosophy.</p>

<h2>Content and Doctrine</h2>
<p>The three books of <i>De Occulta Philosophia</i> address complementary aspects of magical philosophy. Book I treats natural magic — the understanding of properties and correspondences among natural substances and their application to produce effects through sympathetic action. Book II addresses celestial magic — the influence of celestial bodies and the means by which this influence can be directed and amplified through magical practice. Book III presents ceremonial magic — the invocation of spiritual and divine powers and the consecration of magical talismans and instruments. Agrippa presents these three forms of magic as expressions of a single underlying philosophy based on understanding the chain of being linking divine, celestial, and material realms. The work emphasizes that magic is not supernatural but grounded in natural principles; the magus is a sage who understands and appropriately manipulates natural forces and correspondences.</p>

<h2>Transmission and Manuscript Tradition</h2>
<p>The <i>De Occulta Philosophia</i> was published in multiple editions during the sixteenth and seventeenth centuries and was translated into French, English, and other languages. The work circulated widely among scholars, natural philosophers, and practitioners of magic throughout early modern Europe. Numerous commentaries and adaptations attest to the text's influence and continuing relevance. The <i>De Occulta Philosophia</i> became a canonical text within Western esoteric traditions and remains the most widely known and influential Renaissance magical treatise.</p>

<h2>Modern Scholarship</h2>
<p>Copenhaver and other Renaissance magic scholars have established Agrippa's systematic presentation of natural magic as foundational to early modern magical philosophy. Contemporary research emphasizes the work's sophisticated integration of Hermetic, Neoplatonic, Kabbalistic, and Christian theological frameworks. The <i>De Occulta Philosophia</i> has been recognized as central to understanding Renaissance intellectual history and the emergence of early modern scientific thought.</p>

<h2>Literature</h2>
<p>Copenhaver, Brian P. <i>Magic in Western Culture: From Antiquity to the Enlightenment</i>. Cambridge: Cambridge University Press, 2015.</p>
<p>French, Peter J. <i>John Dee: The World of an Elizabethan Magus</i>. London: Routledge, 1972.</p>
<p>Hanegraaff, Wouter J. <i>Hermetic Spirituality and the Historical Imagination</i>. Cambridge: Cambridge University Press, 2022.</p>
<p>Versluis, Arthur. <i>Magic and Mysticism: An Introduction to Western Esoteric Traditions</i>. Lanham, MD: Rowman and Littlefield, 2007.</p>
<p>Yates, Frances A. <i>Giordano Bruno and the Hermetic Tradition</i>. London: Routledge, 1964.</p>''',

    'crater_hermetis': '''<p>The <i>Crater Hermetis</i>, a medieval alchemical text, employs the metaphor of a cosmic vessel or mixing bowl (the Krater) as its central image for understanding alchemical transformation and cosmic creation. The work belongs to the tradition of allegorical and metaphorical alchemical exposition, presenting technical alchemical doctrine through poetic and symbolic language. The <i>Crater Hermetis</i> exemplifies how medieval alchemists employed rich metaphorical systems to communicate both technical procedures and deeper spiritual and philosophical dimensions of the alchemical work simultaneously.</p>

<h2>Content and Doctrine</h2>
<p>The <i>Crater Hermetis</i> presents the cosmos and the alchemical work as expressions of a single principle — the mixing or combination of opposing elements resulting in transformation and manifestation. The text employs the image of the Krater — a cosmic vessel or womb in which all things are mixed and transformed — to represent both material alchemical processes and spiritual transformation. The work emphasizes that successful alchemy requires understanding the unity underlying apparent opposition and the possibility of reconciling contraries through proper knowledge and technique.</p>

<h2>Transmission and Manuscript Tradition</h2>
<p>The <i>Crater Hermetis</i> survives in alchemical manuscript compilations and appears in printed collections of alchemical texts. The work's poetic and metaphorical approach made it popular among esoteric practitioners, though the obscurity of its symbolic language limited its accessibility.</p>

<h2>Modern Scholarship</h2>
<p>Contemporary alchemical scholarship has engaged with texts like the <i>Crater Hermetis</i> as evidence of sophisticated metaphorical and symbolic systems through which alchemists communicated complex knowledge. The work exemplifies the literary and philosophical dimensions of alchemy alongside its technical and practical concerns.</p>

<h2>Literature</h2>
<p>Abraham, Lyndy. <i>A Dictionary of Alchemical Imagery</i>. Cambridge: Cambridge University Press, 1998.</p>
<p>Principe, Lawrence M. <i>The Secrets of Alchemy</i>. Chicago: University of Chicago Press, 2013.</p>
<p>Versluis, Arthur. <i>Magic and Mysticism: An Introduction to Western Esoteric Traditions</i>. Lanham, MD: Rowman and Littlefield, 2007.</p>''',
}

def main():
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        for text_id, analysis_html in analyses.items():
            c.execute('''
                UPDATE texts
                SET analysis_html = ?
                WHERE text_id = ?
            ''', (analysis_html, text_id))
            print(f'Updated {text_id}')

        conn.commit()
        print(f'\nSuccessfully updated {len(analyses)} texts.')

    except Exception as e:
        print(f'Error: {e}', file=sys.stderr)
        return 1
    finally:
        conn.close()

    return 0

if __name__ == '__main__':
    sys.exit(main())
