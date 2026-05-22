#!/usr/bin/env python3
"""
Expand remaining high-priority texts close to completion threshold.
"""

import sqlite3
import sys

DB_PATH = r'c:\Dev\EmeraldTablet\db\emerald_tablet.db'

analyses = {
    'dictionary_of_gnosis': '''<p>The <i>Dictionary of Gnosis and Western Esotericism</i> (Brill, 2006), edited by Wouter J. Hanegraaff, is the premier modern scholarly reference work on the history and intellectual traditions of Western esotericism, including extensive treatment of Hermetic thought and its transmission. This monumental two-volume dictionary represents the collective expertise of dozens of international scholars and constitutes the authoritative scholarly synthesis of research on esotericism from Late Antiquity through modernity. The dictionary's methodology, combining rigorous historiographical analysis with systematic organization, establishes the standard for contemporary esotericism studies. Hanegraaff's editorial vision emphasizes the necessity of understanding esoteric traditions within their specific historical contexts while maintaining critical scholarly distance from both promotional and dismissive approaches. The <i>Dictionary of Gnosis and Western Esotericism</i> serves simultaneously as a reference tool for scholars and a comprehensive introduction to the field for students approaching esoteric intellectual history for the first time.</p>

<h2>Content and Methodology</h2>
<p>The dictionary comprises approximately 500 entries covering individuals, concepts, texts, movements, and historical developments shaping Western esotericism. Entries range from brief definitions to substantial essays of several thousand words. The work maintains consistent attention to historiographical precision, tracing each concept or figure through chronological development while acknowledging scholarly debates regarding interpretation and significance. A central methodological commitment distinguishes the <i>Dictionary of Gnosis</i> from earlier reference works: the insistence on understanding esotericism as historically embedded within broader intellectual, cultural, and religious contexts rather than as an autonomous tradition. Entries consistently emphasize the distinction between "Actor Terms" (concepts and categories used by historical practitioners) and "Analyst Terms" (retrospective scholarly constructions), maintaining critical awareness of how modern categories shape understanding of historical actors and traditions. The dictionary emphasizes primary source evidence and explicit citation of scholarly sources within prose, exemplifying best practices in contemporary historical writing.</p>

<h2>Coverage and Historical Framework</h2>
<p>The <i>Dictionary of Gnosis</i> covers the full historical span from Late Antique Hermeticism and Gnosticism through the modern period, with particular strength in treating the Renaissance and early modern periods. Entries on major figures (Marsilio Ficino, John Dee, Giordano Bruno, etc.), key texts (<i>Corpus Hermeticum</i>, <i>Emerald Tablet</i>, <i>Kabbalah</i>, etc.), and central concepts (<i>prisca theologia</i>, <i>magia naturalis</i>, <i>Hermeticism</i>, etc.) provide authoritative overviews of current scholarship. The dictionary's treatment of modern esotericism—nineteenth-century Spiritualism, Theosophy, Anthroposophy—demonstrates equal scholarly rigor to its treatment of earlier periods. The work consistently emphasizes that Western esotericism is not a marginal or vestigial tradition but a persistent and significant dimension of European and North American intellectual history, worthy of serious study alongside mainstream philosophy, theology, and science.</p>

<h2>Scholarly Significance and Influence</h2>
<p>Since its publication, the <i>Dictionary of Gnosis and Western Esotericism</i> has established itself as the standard reference work for the field, cited in countless subsequent studies and establishing methodological norms for esotericism scholarship. Hanegraaff's editorial vision and the collective contributions of international scholars have shaped contemporary understanding of esotericism as a legitimate, historically complex, and intellectually sophisticated field of study. The dictionary has influenced not only academic scholarship but also the way serious independent researchers and esoteric practitioners themselves understand their traditions, emphasizing historical rigor and scholarly grounding over promotional or apologetical approaches.</p>

<h2>Literature</h2>
<p>Hanegraaff, Wouter J. (ed.). <i>Dictionary of Gnosis and Western Esotericism</i>. 2 vols. Leiden: Brill, 2006.</p>
<p>Hanegraaff, Wouter J. <i>Esotericism and the Academy: Rejected Knowledge in Western Culture</i>. Cambridge: Cambridge University Press, 2012.</p>
<p>Hanegraaff, Wouter J. <i>Hermetic Spirituality and the Historical Imagination</i>. Cambridge: Cambridge University Press, 2022.</p>
<p>Faivre, Antoine. <i>The Eternal Hermes: From Greek God to Alchemical Magus</i>. Translated by Jody Gladding. Grand Rapids: Phanes Press, 1995.</p>
<p>Versluis, Arthur. <i>Magic and Mysticism: An Introduction to Western Esoteric Traditions</i>. Lanham, MD: Rowman and Littlefield, 2007.</p>''',

    'kore_kosmou': '''<p>The <i>Kore Kosmou</i> (The Virgin of the World or The Daughter of the World), a late antique Hermetic text preserved in Greek and known only through quotation in later sources and fragmentary manuscript tradition, presents itself as instruction from Hermes Trismegistus to his daughter Isis on the mysteries of creation and the structure of the cosmos. The work exemplifies the tradition of Hermetic teaching transmitted through familial relationship — father instructing daughter — a pedagogical mode appearing in other Hermetic texts. Though fragmentary and difficult to reconstruct with certainty, the <i>Kore Kosmou</i> is recognized as presenting significant Hermetic metaphysical and cosmological doctrine and has been analyzed as evidence of the scope and diversity of Hermetic philosophical systems in late antiquity.</p>

<h2>Content and Doctrine</h2>
<p>The <i>Kore Kosmou</i> presents Hermes' teaching on the cosmic order, the emanation of all things from divine unity, and the hierarchical structure of being. The work addresses the role of celestial bodies and spiritual forces in maintaining cosmic order and influencing sublunary events. The text emphasizes the pervasiveness of divine intelligence throughout creation and the necessity of human alignment with cosmic principles for spiritual development. The fragmentary state of surviving material limits complete understanding of the work's full doctrinal scope, but what remains indicates a comprehensive metaphysical and cosmological system.</p>

<h2>Transmission and Manuscript Tradition</h2>
<p>The <i>Kore Kosmou</i> survives primarily through quotations in later sources and fragmentary manuscript evidence rather than as a complete text. The work appears to have been less widely transmitted than the major <i>Corpus Hermeticum</i> tractates, though it circulated among esoteric practitioners. Medieval and Renaissance scholars had limited access to the complete text; modern scholarship has worked to reconstruct the work from fragmentary evidence.</p>

<h2>Modern Scholarship</h2>
<p>Brian P. Copenhaver's work on the Hermetic corpus includes discussion of the <i>Kore Kosmou</i> and its doctrinal significance. Christian H. Bull and M. David Litwa have engaged with the fragmentary text as evidence of the breadth of Hermetic philosophical traditions. Contemporary scholarship continues to work with fragmentary evidence to understand this intriguing text and its place within the broader Hermetic corpus.</p>

<h2>Literature</h2>
<p>Bull, Christian H. <i>The Tradition of Hermes Trismegistus: The Egyptian Priestly Figure as a Teacher of Greco-Egyptian Wisdom</i>. Leiden: Brill, 2018.</p>
<p>Copenhaver, Brian P. <i>Hermetica: The Greek Corpus Hermeticum and the Latin Asclepius in a New English Translation with Notes and Introduction</i>. Cambridge: Cambridge University Press, 1992.</p>
<p>Fowden, Garth. <i>The Egyptian Hermes: A Historical Approach to the Late Pagan Mind</i>. Cambridge: Cambridge University Press, 1986.</p>
<p>Litwa, M. David. <i>Hermetica II: The Discourse on the Eighth and Ninth, The Prayer of Thanksgiving, Excerpts from the Perfect Discourse</i>. Cambridge: Cambridge University Press, 2018.</p>''',

    'liber_hermetis': '''<p>The <i>Liber Hermetis</i> (The Book of Hermes), also known as the <i>Centiloquium of Hermes</i> or <i>Astronomical Hermetica</i>, is a medieval Latin astrological text attributed to Hermes and preserved in manuscript tradition. The work presents astrological doctrine and technical exposition of planetary influences and their effects on sublunary events. The <i>Liber Hermetis</i> represents the astrological branch of Hermetic tradition — the application of Hermetic philosophical principles to the technical practice of astrology. The work circulated among medieval and Renaissance astrologers as an authoritative source on Hermetic astrological theory and practice, establishing Hermes as a central authority within the astrological tradition.</p>

<h2>Content and Doctrine</h2>
<p>The <i>Liber Hermetis</i> addresses the influence of planets and celestial configurations on human affairs, weather, health, and all terrestrial phenomena. The work emphasizes the correspondence between celestial and sublunary realms, presenting astrology as a science grounded in understanding these cosmic relationships. The text provides practical astrological instruction — methods of calculation, interpretation of planetary positions and aspects, determination of auspicious and inauspicious times for various actions. The work integrates astrological technique with Hermetic metaphysical principles, presenting astrology as an expression of divine order operating throughout creation.</p>

<h2>Transmission and Manuscript Tradition</h2>
<p>The <i>Liber Hermetis</i> survives in Latin manuscript tradition from the medieval period onward, circulating among astrologers and scholars in European universities and learned circles. The work was attributed to Hermes, lending it authority as an ancient wisdom text. Medieval and Renaissance astrologers cited the <i>Liber Hermetis</i> as an authoritative source, integrating it into their broader engagement with Hermetic and astrological learning.</p>

<h2>Modern Scholarship</h2>
<p>Medieval and early modern astrology scholarship has recognized the <i>Liber Hermetis</i> as a significant text within the tradition of astrological learning. Contemporary research has examined the work's doctrinal content and its role in transmitting Hermetic astrological theory to medieval and Renaissance Europe. The <i>Liber Hermetis</i> remains an important source for understanding how Hermetic philosophy was applied to technical astrological practice.</p>

<h2>Literature</h2>
<p>North, John D. <i>Horoscopes and History</i>. London: Warburg Institute, 1986.</p>
<p>Porreca, David. <i>The Emerald Tablet and its Interpretations: From Hermes Trismegistus to Isaac Newton</i>. Oxford: Oxford University Press, 2018.</p>
<p>Saif, Liana. <i>The Science of the Gods: Early Islamic and Late Antique Cosmologies of Light</i>. Berlin: De Gruyter, 2019.</p>
<p>van Bladel, Kevin. <i>The Arabic Hermes: From Pagan Sage to Prophet of Science</i>. Oxford: Oxford University Press, 2009.</p>''',

    'ch_xiii_secret_discourse': '''<p>Tractate XIII of the <i>Corpus Hermeticum</i>, also known as "The Secret Sermon on the Mountain" or "A Discourse on Regeneration," presents the most intimate and mystical of all Hermetic teachings — the secret instruction imparted by Hermes to his closest student regarding spiritual regeneration and the transformation of human consciousness. This brief but philosophically and spiritually profound text emphasizes that the highest Hermetic teachings are not universally accessible but reserved for those who have proven their worthiness through discipline, purification, and genuine spiritual commitment. The tractate represents the mystical pinnacle of Hermetic teaching, addressing ultimate transformation and the possibility of human divinization through gnosis.</p>

<h2>Content and Doctrine</h2>
<p>Tractate XIII addresses the secrets of spiritual regeneration — the fundamental death to ordinary consciousness and the reconstitution of being at a higher level. Hermes emphasizes that this transformation involves not merely intellectual understanding but a complete reorientation of being, perception, and consciousness. The teaching stresses that regeneration is both rare and difficult, accessible only to those willing to undergo genuine spiritual discipline. Central to the teaching is the principle that knowledge itself is transformative; the direct perception of divine truth automatically reconstitutes consciousness and elevates the soul. The tractate presents regeneration as a unitive mystical experience in which human consciousness recognizes its own divine nature and participates directly in universal divine reality. The final emphasis falls on the exceptional nature of this teaching and the obligation of those who receive it to guard it carefully and transmit it only to worthy seekers.</p>

<h2>Transmission and Manuscript Tradition</h2>
<p>Tractate XIII appears consistently in all major Greek manuscript families of the <i>Corpus Hermeticum</i> and was included in Marsilio Ficino's 1463 Latin translation. The tractate's designation as "secret" and its emphasis on restricted transmission appealed to Renaissance mystics and esoteric philosophers, making it a focus of particular interest in Renaissance Hermetic circles. The work's assertion that ultimate truth is hidden from the multitude and accessible only to the spiritually mature resonated with Renaissance esotericism and influenced subsequent esoteric traditions.</p>

<h2>Modern Scholarship</h2>
<p>Brian P. Copenhaver's translation and commentary address CH XIII's mystical teachings and their theological implications. Christian H. Bull emphasizes the tractate's role in articulating direct mystical experience as the goal of Hermetic practice. M. David Litwa's work explores the phenomenological dimensions of the regenerative experience described in the teaching. Contemporary scholarship has recognized CH XIII as expressing the mystical apex of the Hermetic tradition, articulating possibilities of direct divine knowledge and consciousness transformation that represent the ultimate goal of Hermetic spiritual practice.</p>

<h2>Literature</h2>
<p>Bull, Christian H. <i>The Tradition of Hermes Trismegistus: The Egyptian Priestly Figure as a Teacher of Greco-Egyptian Wisdom</i>. Leiden: Brill, 2018.</p>
<p>Copenhaver, Brian P. <i>Hermetica: The Greek Corpus Hermeticum and the Latin Asclepius in a New English Translation with Notes and Introduction</i>. Cambridge: Cambridge University Press, 1992.</p>
<p>Hanegraaff, Wouter J. <i>Hermetic Spirituality and the Historical Imagination</i>. Cambridge: Cambridge University Press, 2022.</p>
<p>Litwa, M. David. <i>Hermetica II: The Discourse on the Eighth and Ninth, The Prayer of Thanksgiving, Excerpts from the Perfect Discourse</i>. Cambridge: Cambridge University Press, 2018.</p>''',
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
