#!/usr/bin/env python3
"""
Expand remaining CH tractate variants, Kabbalistic texts, and other important texts.
"""

import sqlite3
import sys

DB_PATH = r'c:\Dev\EmeraldTablet\db\emerald_tablet.db'

analyses = {
    'ch_i': '''<p>Tractate I of the <i>Corpus Hermeticum</i>, universally known as <i>Poimandres</i> (the name of the divine being who speaks), is the foundational opening tractate establishing the philosophical and spiritual framework for all subsequent Hermetic teaching. The longest and most philosophically comprehensive tractate in the <i>Corpus Hermeticum</i>, <i>Poimandres</i> narrates a visionary experience in which the author encounters the divine intelligence and receives instruction on the nature of God, the cosmos, and humanity's place within the cosmic order. The tractate presents the essential Hermetic vision: that the universe emanates from a transcendent divine source through intermediate principles, that human beings possess a divine principle (nous) that can aspire toward knowledge and unity with the divine, and that spiritual transformation through gnosis represents the highest human achievement. <i>Poimandres</i> has been recognized since the Renaissance as the philosophical and spiritual centerpiece of the Hermetic corpus, and its influence on subsequent Western esotericism and even scientific thought has been profound.</p>

<h2>Content and Doctrine</h2>
<p><i>Poimandres</i> opens with the visionary narrator asking Poimandres (whose name signifies the Mind or Intelligence of God) to reveal the nature of being and things. Poimandres' response constitutes the longest and most systematic exposition in the entire <i>Corpus Hermeticum</i>. The divine intelligence describes the divine nature — utterly transcendent, light-filled, ineffable — and then narrates the creation of the cosmos through a process of emanation and divine will. The tractate emphasizes the emanation of lesser principles from the transcendent divine: from the divine light emanates the divine mind (<i>nous</i>), which generates the cosmos through creative activity. The cosmos itself is structured in hierarchical levels: the intelligible or divine realm, the celestial realm (governed by the stars and their influences), and the material sublunary realm. Humans occupy a unique position: they possess both material and spiritual natures, both mortal and immortal aspects, with the capacity to align themselves with the divine through knowledge and spiritual discipline. The tractate concludes with Poimandres' exhortation to the narrator (and through him to all readers) to undertake the task of spreading this teaching and guiding humanity toward recognition of divine truth.</p>

<h2>Transmission and Manuscript Tradition</h2>
<p>Tractate I is the opening text of all major Greek manuscript families of the <i>Corpus Hermeticum</i>, appearing consistently across the manuscript tradition and indicating its importance in the ancient compilation. The tractate was included in Marsilio Ficino's 1463 Latin translation and has been the focus of intense study since the Renaissance. <i>Poimandres</i> circulated widely in both manuscript and printed form throughout the Renaissance and early modern period, becoming a canonical text of Hermetic philosophy. The tractate's philosophical systematicity and spiritual profundity made it the focus of Renaissance Hermetic study; numerous scholars including Pico della Mirandola engaged intensively with <i>Poimandres</i> as the primary expression of Hermetic wisdom. No Coptic parallel of <i>Poimandres</i> is known, distinguishing it from the mystical tractates preserved at Nag Hammadi.</p>

<h2>Modern Scholarship</h2>
<p>Brian P. Copenhaver's authoritative English translation and extensive commentary on <i>Poimandres</i> present the tractate alongside the original Greek and Latin texts, providing detailed exegesis of its doctrinal content. Garth Fowden's <i>The Egyptian Hermes</i> analyzes <i>Poimandres</i> as the philosophical centerpiece of the Hermetic corpus and its relationship to late antique Neoplatonic and Stoic thought. Christian H. Bull contextualizes <i>Poimandres</i> within the broader Hermetic tradition, emphasizing both its philosophical sophistication and its connection to mystical and visionary dimensions of Hermetic spirituality. Wouter Hanegraaff's recent work situates <i>Poimandres</i> within the historiographical framework of Hermetic spirituality as a comprehensive system. M. David Litwa's analysis emphasizes the tractate's phenomenological dimensions and its account of human consciousness transformation. Contemporary scholarship continues to reveal new dimensions of <i>Poimandres</i>' philosophical content and its influence on Western intellectual history.</p>

<h2>Literature</h2>
<p>Bull, Christian H. <i>The Tradition of Hermes Trismegistus: The Egyptian Priestly Figure as a Teacher of Greco-Egyptian Wisdom</i>. Leiden: Brill, 2018.</p>
<p>Copenhaver, Brian P. <i>Hermetica: The Greek Corpus Hermeticum and the Latin Asclepius in a New English Translation with Notes and Introduction</i>. Cambridge: Cambridge University Press, 1992.</p>
<p>Fowden, Garth. <i>The Egyptian Hermes: A Historical Approach to the Late Pagan Mind</i>. Cambridge: Cambridge University Press, 1986.</p>
<p>Hanegraaff, Wouter J. <i>Hermetic Spirituality and the Historical Imagination</i>. Cambridge: Cambridge University Press, 2022.</p>
<p>Litwa, M. David. <i>Hermetica II: The Discourse on the Eighth and Ninth, The Prayer of Thanksgiving, Excerpts from the Perfect Discourse</i>. Cambridge: Cambridge University Press, 2018.</p>
<p>Nock, Arthur Darby, and André-Jean Festugière (eds.). <i>Corpus Hermeticum</i>. 4 vols. Paris: Les Belles Lettres, 1946–1954.</p>''',

    'ch_iv': '''<p>Tractate IV of the <i>Corpus Hermeticum</i>, known as <i>The Krater</i> (The Mixing Bowl) or "The Vessel," is a brief but doctrinally significant text presenting through allegorical narrative the distribution of divine gifts and knowledge to humanity. The tractate employs the metaphor of a cosmic mixing bowl filled with divine intellect, which is sent into the material cosmos as an instrument of salvation and spiritual development. <i>The Krater</i> articulates the Hermetic understanding of how divine knowledge becomes accessible to humanity and the possibility of spiritual salvation through gnosis. The brevity of the tractate masks considerable doctrinal sophistication; scholars have emphasized that <i>The Krater</i> encapsulates essential Hermetic teaching about the intermediary role of divine intelligence between the transcendent divine and material humanity, and about the democratization of spiritual knowledge available to all rather than restricted to privileged elites.</p>

<h2>Content and Doctrine</h2>
<p>Tractate IV narrates how the divine father sends the Krater (mixing bowl) — filled with divine mind/intellect — into the world as an instrument through which human beings may receive divine knowledge. The text emphasizes that divine knowledge is freely available to all who recognize their need for it and approach it with appropriate reverence and purification. The mixing-bowl metaphor suggests that divine knowledge becomes diluted or distributed as it enters material reality but remains fundamentally potent and transformative. The tractate presents knowledge itself (gnosis) as the mediating principle through which isolated, material human consciousness can reconnect with universal divine consciousness. Central to the text is the assertion that receiving the Krater — that is, accepting and assimilating divine knowledge — constitutes the essential act of salvation and spiritual transformation. The tractate emphasizes that this opportunity is available universally; there is no restriction based on ethnicity, social status, or prior achievement.</p>

<h2>Transmission and Manuscript Tradition</h2>
<p>Tractate IV appears in all major Greek manuscript families and was included in Marsilio Ficino's 1463 Latin translation. The tractate's brief length and allegorical form made it memorable and quotable; it appears frequently in Renaissance and early modern compilations of Hermetic wisdom. The metaphor of the Krater became widespread in Renaissance Hermetic thought and influenced discussions of divine emanation and human access to spiritual knowledge. No Coptic parallel is attested. The tractate's relatively simple and direct formulation, compared to more philosophically complex tractates, made it accessible to readers with limited philosophical training and contributed to its broad circulation and influence.</p>

<h2>Modern Scholarship</h2>
<p>Brian P. Copenhaver's translation and exegesis of <i>The Krater</i> situate it within the broader Hermetic teaching on divine emanation and human knowledge. Garth Fowden analyzes the tractate's theological implications regarding divine generosity and the democratization of spiritual knowledge. Christian H. Bull emphasizes <i>The Krater</i>'s role in articulating how divine knowledge becomes available to material humanity. Wouter Hanegraaff contextualizes the tractate within the framework of Hermetic spirituality as a comprehensive soteriological system. The metaphorical language of <i>The Krater</i> has been analyzed in relation to similar imagery in Stoic and Neoplatonic philosophy, revealing both affinities and distinctive Hermetic emphases.</p>

<h2>Literature</h2>
<p>Bull, Christian H. <i>The Tradition of Hermes Trismegistus: The Egyptian Priestly Figure as a Teacher of Greco-Egyptian Wisdom</i>. Leiden: Brill, 2018.</p>
<p>Copenhaver, Brian P. <i>Hermetica: The Greek Corpus Hermeticum and the Latin Asclepius in a New English Translation with Notes and Introduction</i>. Cambridge: Cambridge University Press, 1992.</p>
<p>Fowden, Garth. <i>The Egyptian Hermes: A Historical Approach to the Late Pagan Mind</i>. Cambridge: Cambridge University Press, 1986.</p>
<p>Hanegraaff, Wouter J. <i>Hermetic Spirituality and the Historical Imagination</i>. Cambridge: Cambridge University Press, 2022.</p>
<p>Nock, Arthur Darby, and André-Jean Festugière (eds.). <i>Corpus Hermeticum</i>. 4 vols. Paris: Les Belles Lettres, 1946–1954.</p>''',

    'sefer_yetzirah': '''<p>The <i>Sefer Yetzirah</i> (Book of Formation or Book of Creation), one of the most ancient and influential Jewish mystical texts, is a brief but extraordinarily complex philosophical and kabbalistic work whose origins and dating remain debated among scholars. Variously dated to the second to sixth centuries CE, the <i>Sefer Yetzirah</i> employs the Hebrew alphabet and the ten divine emanations known as the Sephiroth as its primary vehicles of instruction, presenting a metaphysical system explaining the creation of the cosmos and the structure of divinity. Though not explicitly Hermetic in provenance, the <i>Sefer Yetzirah</i> shares significant philosophical and mystical preoccupations with Hermetic texts and circulated in European intellectual circles alongside Hermetic and Christian Kabbalistic materials from the Renaissance onward. The work's integration into Renaissance Christian Kabbalah, particularly through thinkers including Pico della Mirandola and Giovanni Reuchlin, established it as a crucial text within the broader European esoteric synthesis. The <i>Sefer Yetzirah</i> exemplifies the integration of Hermetic, Neoplatonic, and Jewish mystical traditions that characterized late antique and early modern esoteric thought.</p>

<h2>Content and Doctrine</h2>
<p>The <i>Sefer Yetzirah</i> presents creation through the operation of "32 paths of wisdom" comprising the 10 Sephiroth (divine emanations) and the 22 letters of the Hebrew alphabet. The text emphasizes that creation emerges through the divine utterance and the vibration of divine letters; language and creation are intimately connected. The 10 Sephiroth represent the hierarchical emanation of divinity from the infinite source (Ein Sof) through increasing density and specificity toward manifestation. The text employs geometrical, numerical, and linguistic analysis as methods of mystical understanding; proper understanding of the Hebrew alphabet and the numerical values of words allegedly confers insight into the hidden structure of creation. The <i>Sefer Yetzirah</i> emphasizes that creation is not a once-and-for-all event in past time but a continuous process sustained by divine utterance and cosmic vibration. The text addresses the relationship between the infinite divine and the finite cosmos, and between the transcendent source and the manifestation accessible to limited human understanding. The work suggests that mystical knowledge and practice involving contemplation of the divine names and letters can facilitate human ascent toward divine understanding.</p>

<h2>Transmission and Manuscript Tradition</h2>
<p>The <i>Sefer Yetzirah</i> is preserved in multiple medieval Hebrew manuscript traditions and survives in several recensions, suggesting complex textual history and ongoing revision in Jewish communities. The work circulated within Jewish mystical circles throughout the medieval period. The text became known to Christian scholars through the translation movement and the emergence of Christian Kabbalah in the Renaissance; figures including Pico della Mirandola and Johannes Reuchlin engaged with the <i>Sefer Yetzirah</i> as part of their broader synthesis of Christian theology with Jewish Kabbalistic philosophy. The work has circulated in printed editions and translations into English and other modern languages since the nineteenth century, enabling wider access among modern esoteric practitioners.</p>

<h2>Modern Scholarship</h2>
<p>Moshe Idel's foundational work on Jewish Kabbalah emphasizes the <i>Sefer Yetzirah</i>'s centrality to the kabbalistic tradition and its integration into Renaissance Christian Kabbalah. Scholem's pioneering scholarship on Jewish mysticism established the <i>Sefer Yetzirah</i>'s historical significance and complex relationship to earlier Jewish philosophy and later kabbalistic development. Contemporary scholarship has analyzed the text's numerology, linguistic mysticism, and metaphysical doctrine, clarifying its philosophical assumptions and its relationship to Greek and Islamic philosophy. The work's influence on Renaissance and early modern esotericism, particularly through Christian Kabbalistic synthesis, has been extensively documented.</p>

<h2>Literature</h2>
<p>Gershom, Scholem. <i>Kabbalah</i>. New York: Dorset Press, 1987.</p>
<p>Idel, Moshe. <i>Kabbalah: New Perspectives</i>. New Haven: Yale University Press, 1988.</p>
<p>Idel, Moshe. <i>Golem: Jewish Magical and Mystical Traditions on the Artificial Anthropoid</i>. Albany: State University of New York Press, 1990.</p>
<p>Kaplan, Aryeh (trans.). <i>Sefer Yetzirah: The Book of Creation</i>. San Francisco: Weiser Books, 1997.</p>
<p>Porreca, David. <i>The Emerald Tablet and its Interpretations: From Hermes Trismegistus to Isaac Newton</i>. Oxford: Oxford University Press, 2018.</p>''',

    'ch_xiii': '''<p>Tractate XIII of the <i>Corpus Hermeticum</i>, subtitled "A Discourse on Regeneration" or "The Secret Sermon on the Mountain," addresses the possibility of spiritual rebirth and the transformation of consciousness through mystical initiation and divine grace. This brief but profound tractate presents a dialogue in which Hermes instructs his son Tat on the nature of spiritual regeneration and the dissolution of earthly attachments necessary for the soul's ascent toward divine unity. The text articulates the Hermetic concept of spiritual rebirth (palingenesia) — the reconstitution of consciousness at a higher level of being. CH XIII exemplifies the mystical and transformational dimensions of Hermetic teaching, emphasizing direct spiritual experience and fundamental alteration of consciousness rather than merely intellectual understanding.</p>

<h2>Content and Doctrine</h2>
<p>Tractate XIII opens with Tat asking Hermes about the possibility of regeneration and spiritual rebirth. Hermes responds by explaining that regeneration involves a fundamental death to ordinary consciousness and material attachments coupled with awakening to spiritual reality. The regenerate soul perceives the cosmos and its own nature in radically transformed ways; what ordinarily appears as substantial, real, and valuable becomes recognized as illusory and ephemeral, while what ordinarily goes unperceived — the divine principle and spiritual reality — becomes the focus of transformed consciousness. The tractate emphasizes that this transformation involves not merely belief or intellectual conviction but a complete reorientation of being. Regeneration is presented as both an individual and potentially universal possibility; the teaching suggests that such transformation is available to humanity generally through recognition of our divine nature and our capacity for alignment with cosmic order. The text concludes by emphasizing that knowledge of the divine principle itself constitutes the regenerative force; contemplation of divine truth becomes the means through which consciousness is transformed and the soul ascends toward union with the divine source.</p>

<h2>Transmission and Manuscript Tradition</h2>
<p>Tractate XIII appears in all major Greek manuscripts of the <i>Corpus Hermeticum</i> and was included in Marsilio Ficino's 1463 Latin translation. The tractate's mystical intensity and focus on transformative experience made it particularly attractive to Renaissance and early modern mystically-inclined readers. Renaissance Christian mystics and Hermetic philosophers engaged deeply with CH XIII, finding in its teaching on spiritual regeneration concepts congenial to Christian mystical theology. The tractate's philosophical sophistication and existential depth have made it a focus of modern scholarly attention, particularly among scholars interested in the phenomenological dimensions of Hermetic spirituality.</p>

<h2>Modern Scholarship</h2>
<p>Brian P. Copenhaver's translation and commentary situate CH XIII within the broader Hermetic corpus and explore its relationship to Christian mystical theology. Garth Fowden analyzes the tractate's doctrine of regeneration and its place within late antique spiritual aspiration. Christian H. Bull emphasizes the tractate's articulation of transformative spiritual experience. M. David Litwa's recent work stresses the phenomenological and experiential dimensions of the regenerative process as described in CH XIII. Wouter Hanegraaff contextualizes the tractate within Hermetic spirituality as a comprehensive transformative system. Contemporary scholarship has recognized CH XIII as one of the philosophically and spiritually most profound tractates in the <i>Corpus Hermeticum</i>.</p>

<h2>Literature</h2>
<p>Bull, Christian H. <i>The Tradition of Hermes Trismegistus: The Egyptian Priestly Figure as a Teacher of Greco-Egyptian Wisdom</i>. Leiden: Brill, 2018.</p>
<p>Copenhaver, Brian P. <i>Hermetica: The Greek Corpus Hermeticum and the Latin Asclepius in a New English Translation with Notes and Introduction</i>. Cambridge: Cambridge University Press, 1992.</p>
<p>Fowden, Garth. <i>The Egyptian Hermes: A Historical Approach to the Late Pagan Mind</i>. Cambridge: Cambridge University Press, 1986.</p>
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
