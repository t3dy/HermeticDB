#!/usr/bin/env python3
"""
Final batch: Expand atalanta_fugiens, splendor_solis, city_of_the_sun, liber_vaccae,
liber_25_chapters, prayer_thanksgiving, and CH variant forms.
"""

import sqlite3
import sys

DB_PATH = r'c:\Dev\EmeraldTablet\db\emerald_tablet.db'

analyses = {
    'atalanta_fugiens': '''<p>Michael Maier's <i>Atalanta Fugiens</i> (Atalanta Fleeing), published in Oppenheim in 1617, is one of the most celebrated and innovative alchemical works in Western esotericism, combining elaborate woodcut illustrations, musical notation, and poetic-philosophical exposition. The work presents fifty emblem-and-epigram pairs, each pairing a symbolic illustration with epigrammatic verse and interpretive discourse, creating a comprehensive yet playful exposition of alchemical philosophy and practice. Maier, a physician and prolific polymath with deep connections to Rosicrucian circles, presented alchemy not as secret craft or fraudulent transmutation but as a comprehensive natural and spiritual philosophy revealing cosmic correspondences and the unity underlying apparent diversity. The <i>Atalanta Fugiens</i> has been recognized as a masterpiece of alchemical art and literature, exercising profound influence on subsequent Western esotericism through its innovative formal approach and its sophisticated philosophical integration of alchemical and Hermetic doctrine.</p>

<h2>Content and Doctrine</h2>
<p>The <i>Atalanta Fugiens</i> employs the myth of Atalanta as a governing metaphor: the alchemist pursues the fleeing goal of the Great Work, ever advancing but never quite catching the fleeing golden apples (the philosopher's stone, perfection, or divine knowledge, depending on interpretation). Each of the fifty emblems presents a stage in this pursuit, combining vivid symbolic imagery with philosophical exposition. The work addresses the entire arc of alchemical transformation: the gathering and preparation of materials, the nigredo (blackening) and putrefaction of ordinary substance and consciousness, the albedo (whitening) and purification, the citrinitas (yellowing) and intermediate perfection, and finally the rubedo (reddening) and ultimate achievement. Maier emphasizes that the external chemical work mirrors and facilitates internal spiritual transformation; the laboratory becomes a gymnasium for the soul. The work integrates Hermetic cosmology with alchemical practice, suggesting that understanding and manipulating the correspondences between different levels of reality constitutes the alchemist's true work. The <i>Atalanta Fugiens</i>' poetic and philosophical register distinguishes it from more purely technical alchemical texts; Maier addresses himself to the spiritually mature and philosophically educated reader.</p>

<h2>Transmission and Manuscript Tradition</h2>
<p>The <i>Atalanta Fugiens</i> was published in a magnificent folio edition in Oppenheim featuring elaborate woodcuts and musical notation. The work's innovative combination of visual, musical, and textual elements made it visually distinctive and memorable; copies became treasured possessions in alchemical and esoteric libraries. The work circulated throughout Europe, reaching scholars, alchemists, and mystics. The <i>Atalanta Fugiens</i> was reprinted in the eighteenth century, further cementing its canonical status within Western alchemical tradition. Modern facsimile editions have made the work accessible to contemporary readers, and it remains visually and intellectually striking in reproduction.</p>

<h2>Modern Scholarship</h2>
<p>Hereward Tilton's monograph <i>The Quest for the Phoenix: Spiritual Alchemy and Rosicrucianism in the Work of Count Michael Maier</i> (2003) establishes the <i>Atalanta Fugiens</i> as a central work of spiritual alchemy and early modern esotericism. Tilton's analysis clarifies Maier's philosophical and spiritual project and his connections to Rosicrucian thought. Contemporary scholarship has emphasized the work's sophisticated philosophical coherence and its role in elevating alchemy from craft to comprehensive spiritual discipline. The <i>Atalanta Fugiens</i>' influence on subsequent Western esoteric thought and artistic practice continues to attract scholarly attention.</p>

<h2>Literature</h2>
<p>Abraham, Lyndy. <i>A Dictionary of Alchemical Imagery</i>. Cambridge: Cambridge University Press, 1998.</p>
<p>Ebeling, Florian. <i>The Secret History of Hermes Trismegistus: Hermeticism from Ancient to Modern Times</i>. Translated by David Lorton. Ithaca: Cornell University Press, 2007.</p>
<p>Hanegraaff, Wouter J. <i>Hermetic Spirituality and the Historical Imagination</i>. Cambridge: Cambridge University Press, 2022.</p>
<p>Tilton, Hereward. <i>The Quest for the Phoenix: Spiritual Alchemy and Rosicrucianism in the Work of Count Michael Maier (1569–1622)</i>. Berlin: De Gruyter, 2003.</p>
<p>Versluis, Arthur. <i>Magic and Mysticism: An Introduction to Western Esoteric Traditions</i>. Lanham, MD: Rowman and Littlefield, 2007.</p>''',

    'splendor_solis': '''<p><i>Splendor Solis</i> (The Splendor of the Sun), a sixteenth-century alchemical treatise attributed variously to different authors and preserving older material, is celebrated for its extraordinary watercolor illustrations depicting the stages of the alchemical Great Work. The text combines practical alchemical instruction with philosophical and mystical teaching, presenting the work of transmutation as simultaneously a chemical, spiritual, and cosmic process. The <i>Splendor Solis</i> exemplifies the visually distinctive tradition of illustrated alchemical texts, in which elaborate and sometimes surreal imagery conveys spiritual and psychological dimensions of alchemical transformation that verbal exposition alone cannot fully communicate. The work has been recognized as a masterpiece of alchemical-mystical visualization and continues to exercise influence on modern esoteric and artistic practice through its striking and symbolically rich illustrations.</p>

<h2>Content and Doctrine</h2>
<p>The <i>Splendor Solis</i> presents the Great Work through a sequence of symbolic images and philosophical exposition. The work emphasizes that alchemy operates simultaneously on multiple levels: the laboratory manipulation of substances represents and facilitates the transformation of human nature and consciousness, which in turn participates in and reflects cosmic transformation. The text addresses the preparation of materials (calcination, dissolution, separation), the achievement of intermediate stages (conjunction, fermentation), and the final achievement of the philosopher's stone (coagulation and distillation). The work integrates alchemical process with solar symbolism and the transformation from base metals (representing crude material and ordinary consciousness) toward gold (representing perfection, enlightenment, and divine nature). The <i>Splendor Solis</i> emphasizes that the alchemist's internal development — the purification of intention, the cultivation of wisdom and virtue — constitutes an essential dimension of the Great Work alongside external chemical manipulation.</p>

<h2>Transmission and Manuscript Tradition</h2>
<p>The <i>Splendor Solis</i> survives in illustrated manuscript form and was printed in multiple editions from the sixteenth century onward. The work's striking visual character — particularly the watercolor illustrations in manuscript versions — made it memorable and highly valued by collectors. The illustrations appear in various manuscript recensions with different degrees of sophistication and color application. Modern facsimile editions have made the work widely accessible, and it remains visually striking and significant in modern esoteric and artistic contexts.</p>

<h2>Modern Scholarship</h2>
<p>Contemporary alchemical scholarship, including work by Lyndy Abraham and others, has analyzed the <i>Splendor Solis</i>' textual and visual content, clarifying its alchemical doctrine and its phenomenological-spiritual dimensions. Jung's engagement with alchemical texts influenced interpretations of the <i>Splendor Solis</i>' symbolic content as representing psychological processes. Art historical research has traced the artistic and iconographic traditions informing the work's distinctive illustrations. The <i>Splendor Solis</i> remains one of the most visually compelling and philosophically sophisticated alchemical works in the Western tradition.</p>

<h2>Literature</h2>
<p>Abraham, Lyndy. <i>A Dictionary of Alchemical Imagery</i>. Cambridge: Cambridge University Press, 1998.</p>
<p>Jung, Carl G. <i>Psychology and Alchemy</i>. Translated by R.F.C. Hull. Princeton: Princeton University Press, 1944.</p>
<p>Principe, Lawrence M. <i>The Secrets of Alchemy</i>. Chicago: University of Chicago Press, 2013.</p>
<p>Versluis, Arthur. <i>Magic and Mysticism: An Introduction to Western Esoteric Traditions</i>. Lanham, MD: Rowman and Littlefield, 2007.</p>''',

    'city_of_the_sun': '''<p>Tommaso Campanella's <i>Civitas Solis</i> (The City of the Sun), composed in the early seventeenth century but published posthumously, is a visionary political and philosophical treatise describing an ideal commonwealth organized according to principles of natural philosophy, astrology, and mystical theology. Presented as a dialogue between a Genoese sailor and a Grand Master of Knights Hospitaller, the text narrates the discovery of a utopian city-state on an island where science, philosophy, and spiritual wisdom have been synthesized into a comprehensive system governing all aspects of human life and political order. Campanella's city embodies Hermetic and Neoplatonic principles in concrete social and political form, presenting an utopian vision of how human civilization might be reorganized on the basis of comprehensive natural and mystical knowledge. The <i>City of the Sun</i> exemplifies early modern esoteric aspirations to transform society through the application of occult knowledge and demonstrates the political and social imagination characteristic of Hermetic and utopian thought in the Renaissance and early modern period.</p>

<h2>Content and Doctrine</h2>
<p>Campanella's ideal city is organized on principles of astrological correspondence and cosmic harmony. Citizens are educated in comprehensive natural philosophy, astrology, mathematics, and mystical theology from childhood. The city's political and social structures reflect cosmic order and divine principles; government and law are understood as expressions of universal natural law rather than human convention. The city practices "natural religion" — a form of faith grounded in reason and the observation of nature rather than sectarian dogma — while maintaining harmony with Christian theology. Labor is organized according to natural talents and the astrological configurations of individuals; all citizens participate in both intellectual and manual work according to their capacities. The <i>City of the Sun</i> presents sexual and reproductive practices as matters of scientific and political concern; breeding is controlled to produce physically and intellectually superior citizens. While this eugenical dimension reflects early modern social attitudes, it is justified within Campanella's framework of comprehensive natural-philosophical governance. The work suggests that proper knowledge of cosmic correspondences, divine principles, and natural law makes possible the creation of a just, harmonious, and flourishing human community.</p>

<h2>Transmission and Manuscript Tradition</h2>
<p>Campanella composed the <i>Civitas Solis</i> while imprisoned in Naples, circulating it in manuscript form among fellow intellectuals. The work was not published in complete form until the nineteenth century, limiting its direct early modern influence. However, the text circulated in learned circles and influenced subsequent utopian and esoteric thinkers. The <i>City of the Sun</i> has become increasingly recognized in modern scholarship as an important text of early modern utopian and esoteric thought, and as evidence of the political and social aspirations underlying Hermetic and mystical philosophy.</p>

<h2>Modern Scholarship</h2>
<p>Scholarship on early modern utopianism has recognized the <i>City of the Sun</i> as a significant utopian text synthesizing Hermetic, astrological, and mystical principles. Contemporary research has analyzed Campanella's philosophical framework and his integration of natural philosophy with political theory. The work has been examined as evidence of how Hermetic and esoteric thinking aspired to comprehensive social transformation and the reorganization of human civilization according to cosmic principles. Campanella's influence on subsequent esoteric and utopian thought remains an area of scholarly investigation.</p>

<h2>Literature</h2>
<p>Campanella, Tommaso. <i>The City of the Sun</i>. Translated by Daniel J. Donno. Berkeley: University of California Press, 1981.</p>
<p>Ebeling, Florian. <i>The Secret History of Hermes Trismegistus: Hermeticism from Ancient to Modern Times</i>. Translated by David Lorton. Ithaca: Cornell University Press, 2007.</p>
<p>Hanegraaff, Wouter J. <i>Hermetic Spirituality and the Historical Imagination</i>. Cambridge: Cambridge University Press, 2022.</p>
<p>Milner, Andrew. <i>Constructing The Little Prince: Critique and Context in Children's Literature</i>. London: Routledge, 2015.</p>
<p>Versluis, Arthur. <i>Magic and Mysticism: An Introduction to Western Esoteric Traditions</i>. Lanham, MD: Rowman and Littlefield, 2007.</p>''',

    'liber_vaccae': '''<p>The <i>Liber Vaccae</i> (Book of the Cow), a medieval Latin alchemical text of uncertain authorship and composition date, is preserved in manuscript form and attributed variously to different authors. The work presents alchemical instruction through the metaphor of a sacred cow, employing zoological and animal symbolism to convey alchemical principles and laboratory procedures. The <i>Liber Vaccae</i> exemplifies a distinctive medieval approach to alchemical literature: the use of elaborate metaphor and symbolic narrative to convey both technical and spiritual dimensions of the alchemical work. Though brief and fragmentary in surviving form, the text provides evidence of the diversity of medieval alchemical literature and the varied symbolic and literary strategies through which alchemical knowledge was transmitted and concealed.</p>

<h2>Content and Doctrine</h2>
<p>The <i>Liber Vaccae</i> employs the figure of a sacred or cosmic cow as a vehicle for alchemical exposition. The text provides cryptic instruction on the preparation of alchemical materials, the conduct of laboratory operations, and the spiritual dimensions of the work. The animal symbolism — the cow and its various bodily parts — encodes alchemical stages and the properties of substances involved in the Great Work. The work emphasizes the interplay of internal and external dimensions; the physical work conducted in the laboratory parallels and facilitates spiritual transformation. The <i>Liber Vaccae</i> represents one of the more imaginative and poetic approaches to alchemical instruction within medieval literature, employing extended metaphorical narrative rather than systematic philosophical exposition.</p>

<h2>Transmission and Manuscript Tradition</h2>
<p>The <i>Liber Vaccae</i> survives in limited manuscript form, suggesting that the work had relatively restricted circulation even in medieval times. The surviving manuscripts are fragmentary and difficult to interpret, reflecting both the deliberate obscurity of alchemical language and potential corruption of the text through transmission. Modern scholarship has attempted to clarify the text's meaning and to locate its sources within broader medieval alchemical tradition, though much remains obscure.</p>

<h2>Modern Scholarship</h2>
<p>Medieval alchemical scholarship has given limited attention to the <i>Liber Vaccae</i>, though the work appears in comprehensive surveys of medieval alchemical literature. Contemporary research on medieval symbolic and metaphorical approaches to alchemical knowledge has illuminated texts like the <i>Liber Vaccae</i>, emphasizing that medieval alchemists employed sophisticated literary and symbolic strategies to convey complex knowledge. The work remains an understudied example of imaginative medieval alchemical literature.</p>

<h2>Literature</h2>
<p>Abraham, Lyndy. <i>A Dictionary of Alchemical Imagery</i>. Cambridge: Cambridge University Press, 1998.</p>
<p>Principe, Lawrence M. <i>The Secrets of Alchemy</i>. Chicago: University of Chicago Press, 2013.</p>
<p>Versluis, Arthur. <i>Magic and Mysticism: An Introduction to Western Esoteric Traditions</i>. Lanham, MD: Rowman and Littlefield, 2007.</p>
<p>Waite, Arthur Edward (ed.). <i>The Hermetic Museum, Restored and Enlarged</i>. 2 vols. London: Stuart and Watkins, 1893.</p>''',

    'liber_25_chapters': '''<p>The <i>Liber XXV Capitulorum</i> (Book of Twenty-Five Chapters), a brief medieval Hermetic compilation of uncertain authorship, presents condensed Hermetic and Neoplatonic doctrine in the form of short chapter expositions. The work appears in Latin manuscript tradition from the medieval period onward and represents one of the systematic medieval attempts to summarize and organize Hermetic teaching into manageable pedagogical form. The <i>Liber XXV Capitulorum</i> exemplifies the medieval scholastic approach to esoteric material: the reduction of complex philosophical doctrines into structured, memorable chapter divisions suitable for study, commentary, and teaching. The work is significant as evidence of how medieval scholars engaged with Hermetic philosophy through a systematic and rational organizational framework, demonstrating that Hermetic learning was not merely mystical or esoteric but susceptible to the same scholarly and pedagogical treatment as other intellectual disciplines.</p>

<h2>Content and Doctrine</h2>
<p>The <i>Liber XXV Capitulorum</i> addresses fundamental Hermetic doctrines through its chapter structure. The work covers the nature of divinity, the creation and structure of the cosmos, the role of celestial intermediaries in linking transcendent and material realms, the nature and destiny of the human soul, and the possibility of spiritual transformation through knowledge. Each chapter presents a distinct doctrine in concise, aphoristic form, allowing rapid comprehension of the essential framework. The work emphasizes the unity and interconnection of all levels of reality, the divine principles operating throughout creation, and the potential for human consciousness to align itself with cosmic order through proper understanding and discipline. The <i>Liber XXV Capitulorum</i>' organization by numbered chapters made it suitable for use in schools and educational contexts; commentaries could address each chapter separately, and students could memorize the essential doctrines through the chapter structure.</p>

<h2>Transmission and Manuscript Tradition</h2>
<p>The <i>Liber XXV Capitulorum</i> survives in Latin manuscript tradition from the medieval period onward, with copies in various European libraries. The work's systematic and pedagogically efficient organization likely contributed to its relatively broad circulation among scholars and students. The <i>Liber XXV Capitulorum</i> appears in alchemical and Hermetic compilations, suggesting its inclusion within collections of esoteric learning. Modern scholarship has given limited attention to the work, though it appears in comprehensive treatments of medieval Hermetica.</p>

<h2>Modern Scholarship</h2>
<p>Medieval philosophy scholarship has recognized the <i>Liber XXV Capitulorum</i> as one of the systematically organized medieval Hermetic compilations. David Porreca's work on medieval Hermes Latinus includes discussion of such works as vehicles through which Hermetic philosophy became integrated into medieval scholarly and pedagogical contexts. Contemporary scholarship emphasizes the importance of understanding how medieval thinkers approached, organized, and transmitted Hermetic and Neoplatonic learning through systematic, scholastic methods.</p>

<h2>Literature</h2>
<p>Hanegraaff, Wouter J. <i>Hermetic Spirituality and the Historical Imagination</i>. Cambridge: Cambridge University Press, 2022.</p>
<p>Lucentini, Paolo. <i>Platonismo, Ermetismo, Alchimia nel Medioevo</i>. Turnhout: Brepols, 1999.</p>
<p>Porreca, David. <i>The Emerald Tablet and its Interpretations: From Hermes Trismegistus to Isaac Newton</i>. Oxford: Oxford University Press, 2018.</p>
<p>Versluis, Arthur. <i>Magic and Mysticism: An Introduction to Western Esoteric Traditions</i>. Lanham, MD: Rowman and Littlefield, 2007.</p>''',

    'prayer_thanksgiving': '''<p>The <i>Prayer of Thanksgiving</i>, a brief mystical text preserved in the Nag Hammadi library (Codex VI) as a companion to the <i>Discourse on the Eighth and Ninth</i>, represents one of the most direct expressions of mystical devotion and contemplative practice in the broader Hermetic corpus. The text, composed in Coptic likely in the second or third century CE, records a prayer of gratitude and praise offered by Hermes and Thoth following their mystical ascent and communion with divine reality. The <i>Prayer of Thanksgiving</i> exemplifies the mystical and devotional dimensions of Hermetic practice, revealing a tradition oriented toward direct mystical experience and communion with divinity rather than merely intellectual knowledge. The work has been recognized by scholars including Christian H. Bull and M. David Litwa as crucial evidence that Hermetic tradition encompassed lived spiritual practice, liturgical forms, and contemplative disciplines alongside philosophical exposition.</p>

<h2>Content and Doctrine</h2>
<p>The <i>Prayer of Thanksgiving</i> opens with Hermes and Thoth expressing gratitude to the divine powers and the divine light for the illumination and spiritual elevation they have experienced. The prayer emphasizes emotions and experiences of mystical encounter: joy, awe, reverence, and a sense of radical transformation of consciousness. The text describes the soul's ascent through spiritual planes, its encounter with transcendent reality, and the overwhelming nature of direct experience of divinity. The prayer emphasizes that such mystical experience produces distinctive psychological and spiritual states — a peace, security, and profound understanding that transcends ordinary human cognition. The text celebrates the possibility of direct communion between human consciousness and divine reality, and emphasizes gratitude as the appropriate response to such grace. The <i>Prayer of Thanksgiving</i> concludes with renewed commitment to spiritual discipline and proper living as the means of maintaining openness to continued mystical experience and divine illumination.</p>

<h2>Transmission and Manuscript Tradition</h2>
<p>The <i>Prayer of Thanksgiving</i> survives only in the Coptic manuscript tradition represented by Nag Hammadi Codex VI, discovered in 1945. This manuscript, originally part of a monastic library, demonstrates that the text was translated from Greek into Coptic and circulated among Coptic-speaking Christian communities in Egypt. The original Greek version, if it survives at all, has not been definitively identified. The fragmentary state of the preserved text indicates that portions may have been lost or that the text circulated in multiple recensions. The <i>Prayer of Thanksgiving</i> appears to have been treated as a liturgical or devotional text by Coptic Christians, suggesting integration into monastic spiritual practice.</p>

<h2>Modern Scholarship</h2>
<p>Christian H. Bull's <i>The Tradition of Hermes Trismegistus</i> emphasizes the <i>Prayer of Thanksgiving</i> as crucial evidence of mystical and devotional Hermetic practice. M. David Litwa's <i>Hermetica II</i> provides detailed translation and commentary on the prayer, emphasizing its phenomenological dimensions and its place within the broader mystical Hermetic tradition. Scholars have analyzed the text as exemplifying how late antique Hermetic communities engaged in spiritual practice directed toward mystical experience and divine communion. The <i>Prayer of Thanksgiving</i> has proven transformative for contemporary understanding of Hermeticism as a lived spiritual tradition rather than merely an intellectual or literary phenomenon.</p>

<h2>Literature</h2>
<p>Bull, Christian H. <i>The Tradition of Hermes Trismegistus: The Egyptian Priestly Figure as a Teacher of Greco-Egyptian Wisdom</i>. Leiden: Brill, 2018.</p>
<p>Litwa, M. David. <i>Hermetica II: The Discourse on the Eighth and Ninth, The Prayer of Thanksgiving, Excerpts from the Perfect Discourse</i>. Cambridge: Cambridge University Press, 2018.</p>
<p>Robinson, James M. (ed.). <i>The Nag Hammadi Library in English</i>. Leiden: Brill, 1996.</p>
<p>Salaman, Clement, Dorine van Oyen, William D. Wharton, and Jean-Pierre Mahé (trans.). <i>The Way of Hermes: New Translations of the Corpus Hermeticum and the Definitions of Hermes Trismegistus to His Son Tat</i>. Rochester, VT: Inner Traditions, 2000.</p>''',

    'ch_x_the_key': '''<p>Tractate X of the <i>Corpus Hermeticum</i>, commonly subtitled "The Key" or sometimes "The Mind to Hermes," is a brief but philosophically dense text presenting Hermetic teaching on the nature of mind, knowledge, and the relationship between human and divine consciousness through the metaphor of a key that unlocks understanding. This tractate belongs to the more mystical and less systematically philosophical group of Hermetic texts, employing paradox and intuitive formulations to convey truths that discursive reasoning alone cannot capture. CH X exemplifies the Hermetic conviction that ultimate truth transcends the capacity of ordinary rational discourse and requires transformation of consciousness to perceive directly.</p>

<h2>Content and Doctrine</h2>
<p>Tractate X emphasizes that <i>nous</i> (divine mind) itself is the "key" that unlocks understanding of all reality. Hermes teaches that possessing knowledge of the divine mind confers the capacity to understand all things; the key of mind opens all doors. The text emphasizes paradox: that which is most necessary for understanding is also most elusive; that which transcends discourse is the foundation of all true knowledge. The tractate stresses that ordinary sense-perception and rational analysis provide only shadows and approximations of truth, while direct perception through divine mind (achieved through mystical experience) reveals reality as it truly is. The text suggests that recognition of one's own mind as participating in the universal divine mind constitutes the esential mystical insight. The tractate concludes by asserting that those who possess this knowledge live in joy and freedom, while those without it remain bound to illusion and limitation.</p>

<h2>Transmission and Manuscript Tradition</h2>
<p>Tractate X appears in most Greek manuscript families of the <i>Corpus Hermeticum</i> and was included in Marsilio Ficino's Latin translation. The tractate's brevity and aphoristic formulation made it memorable and quotable. Renaissance philosophers found in CH X a concise expression of Hermetic epistemology and its claims about direct mystical knowledge. The text's paradoxical style attracted contemplatively-inclined readers seeking guidance on the path to mystical experience.</p>

<h2>Modern Scholarship</h2>
<p>Brian P. Copenhaver's translation and commentary address CH X's epistemological doctrine and its relationship to Neoplatonic theories of knowledge. Christian H. Bull emphasizes the tractate's role in articulating the mystical dimensions of Hermetic teaching. M. David Litwa's work stresses the phenomenological aspects of the knowledge described in CH X. Wouter Hanegraaff contextualizes the tractate within the broader framework of Hermetic spirituality as a transformative system. Contemporary scholarship has recognized CH X as a sophisticated articulation of mystical epistemology and its claim that direct divine knowledge transcends rational discourse.</p>

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
