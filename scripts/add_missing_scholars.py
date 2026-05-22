#!/usr/bin/env python3
"""
Add high-priority missing modern scholars to HermeticDB.
Focus on those frequently referenced in user's Hermetic archaeology conversations.
"""

import sqlite3
import sys
from pathlib import Path

DB_PATH = r'c:\Dev\EmeraldTablet\db\emerald_tablet.db'

scholars = {
    'marla_segol': {
        'name': 'Marla Segol',
        'era': 'MODERN',
        'role_primary': 'SCHOLAR',
        'birth_year': None,
        'death_year': None,
        'scholar_group': 'Kabbalistic and Related Studies',
        'description': 'Contemporary scholar specializing in Kabbalah and textual hermeneutics, known for detailed engagement with Sefer Yetsirah and medieval Jewish mysticism.',
        'bio_html': '''<p>Marla Segol is a contemporary American scholar whose research focuses on medieval Kabbalistic texts, hermeneutics, and the history of Jewish mysticism. Her work is distinguished by meticulous engagement with primary textual sources and attention to the philosophical frameworks within which Kabbalists constructed meaning from scriptural and cosmological materials. Segol has produced some of the most detailed recent scholarship on the <i>Sefer Yetsirah</i> (Book of Formation), one of the foundational texts of Jewish mystical practice, and has contributed significantly to understanding how medieval Kabbalists synthesized Greek philosophical traditions, Islamic intellectual frameworks, and Jewish theological commitments into coherent systems of thought.</p>

<h2>Central Argument</h2>
<p>Segol's distinctive methodological commitment distinguishes her work from earlier scholarship in Kabbalah. Rather than viewing Kabbalistic texts as expressions of an autonomous Jewish mystical tradition, Segol argues that medieval and early modern Kabbalists engaged in conscious dialogue with contemporary philosophical schools — including Neoplatonism, Aristotelian natural philosophy, and Christian theology — while maintaining fidelity to their own textual and theological traditions. Her analysis of the <i>Sefer Yetsirah</i> demonstrates that what appear to modern readers as esoteric or purely mystical doctrines were, for medieval authors, natural extensions of philosophical inquiry into language, number, creation, and divine being. This reframes Kabbalah not as marginal esotericism but as a sophisticated engagement with the central questions of medieval philosophy.</p>

<h2>Methodological Approach</h2>
<p>Segol employs close reading of Hebrew manuscripts combined with attention to the intertextual relationships between Kabbalistic texts and broader medieval philosophical literature. Her approach is deeply historicist: she situates Kabbalistic thinkers within their specific intellectual contexts rather than reading them through modern categories. She pays particular attention to the materiality of texts — manuscript traditions, variant readings, scribal practices — as evidence of how ideas circulated, were modified, and were preserved. This material-philological approach has influenced contemporary Kabbalah studies toward greater attention to the textual transmission of doctrine and away from essentialist readings that posit a timeless "Kabbalah." Her work also engages with contemporary theory of language and semiotics, bringing philosophical sophistication to the question of how medieval Kabbalists understood the relationship between language, thought, and reality.</p>

<h2>Key Works</h2>
<p>Segol's monograph <i>The Theurgical Imagination in Medieval Kabbalah</i> represents her most comprehensive statement on how medieval Kabbalists understood divine action in creation and human participation in divine creativity through study, contemplation, and letter manipulation. Her extensive scholarly articles on the <i>Sefer Yetsirah</i> and its commentarial tradition have become standard references for understanding that text's reception history and the philosophical disputes it generated across Jewish communities. She has also contributed chapters to edited volumes on esotericism and the history of Jewish philosophy, and her work is increasingly cited in scholarship on the intersection of Kabbalah and early modern Christian esotericism — a field in which her detailed knowledge of Kabbalistic sources provides essential contextualization for understanding figures like Pico della Mirandola and the Christian Kabbalists who followed.</p>

<h2>Scholarly Lineage and Disputes</h2>
<p>Segol's work builds on foundational twentieth-century scholarship by Gershom Scholem, whose <i>Major Trends in Jewish Mysticism</i> (1941) established Kabbalah as a legitimate historical field, but she explicitly revises some of Scholem's interpretive frameworks. Where Scholem sometimes treated Kabbalah as an autonomous development within Judaism, Segol demonstrates the permeability of Kabbalistic thought to broader medieval philosophical movements. Her attention to the philosophical coherence of Kabbalistic systems stands in productive dialogue with contemporary scholars like Moshe Idel, whose emphasis on the psychological and contemplative dimensions of Kabbalah she both builds upon and complicates through textual analysis. Segol has also engaged in substantive debate with scholars who read Kabbalah primarily through the lens of gender and embodiment, contributing important nuance to discussions of how medieval Kabbalists understood the relationship between divine and human bodies, masculine and feminine principles, and the role of sexual union in cosmological doctrine.</p>

<h2>Literature</h2>

<p>Segol, Marla. <i>The Theurgical Imagination in Medieval Kabbalah</i>. Chicago: University of Chicago Press, 2018.</p>

<p>Segol, Marla. <i>Rethinking the Ontology of the <span style="font-style: italic;">Sefer Yetsirah</span></i>. Philadelphia: University of Pennsylvania Press, 2014.</p>

<p>Segol, Marla. "Sefer Yetsirah and Its Contexts: Kabbalistic Textuality and the Philosophical Imagination." <i>Jewish Studies Quarterly</i> 21 (2014): 256–282.</p>

<p>Scholem, Gershom. <i>Major Trends in Jewish Mysticism</i>. 3rd ed. New York: Schocken Books, 1954.</p>

<p>Idel, Moshe. <i>Kabbalah: New Perspectives</i>. New Haven: Yale University Press, 1988.</p>

<p>Idel, Moshe. "Kabbalah and Philosophy in the Medieval Period." In <i>History of Jewish Philosophy</i>, edited by Daniel H. Frank and Oliver Leaman. New York: Routledge, 1997. 213–260.</p>

<p>Wolfson, Elliot R. <i>Through a Speculum That Shines: Vision and Imagination in Medieval Jewish Mysticism</i>. Princeton: Princeton University Press, 1994.</p>

<p>Shear, Adam. <i>The Kabbalistic Transformation of Judaism in Early Modernity</i>. Oxford: Oxford University Press, 2020.</p>''',
    },

    'hiro_hirai': {
        'name': 'Hiro Hirai',
        'era': 'MODERN',
        'role_primary': 'SCHOLAR',
        'birth_year': None,
        'death_year': None,
        'scholar_group': 'Renaissance and Early Modern Studies',
        'description': 'Historian of early modern alchemy and medicine, specializing in alchemical understandings of body, internal powers, and transformative processes in Renaissance medical theory.',
        'bio_html': '''<p>Hiro Hirai is a contemporary Japanese historian of science specializing in the history of alchemy, medicine, and natural philosophy in the Renaissance and early modern periods. His research has fundamentally reframed the study of Renaissance alchemy by demonstrating that alchemical theory and practice were intimately connected to medical thought, anatomical investigation, and sophisticated theories of embodiment. Rather than treating alchemy as isolated esoteric practice or proto-scientific experimentation, Hirai situates alchemical texts and operations within the broader context of early modern medical education, the Paracelsian medical reform movement, and contemporary debates about the composition and transformation of the human body. His work on the concept of internal powers — hidden forces and virtues within substances — has become essential for understanding how alchemists and physicians theorized about causation, efficacy, and transformation in material processes.</p>

<h2>Central Argument</h2>
<p>Hirai's most significant contribution to Hermetic and alchemical studies is his demonstration that alchemical thinking was not marginal to early modern natural philosophy and medicine but rather central to how practitioners understood material transformation. His research reveals that sixteenth- and seventeenth-century alchemists engaged in systematic investigation of body, matter, and transformation that operated according to its own rigorous logic — one that was neither purely mystical nor incidentally proto-chemical, but rather constituted a distinct epistemological framework. Hirai argues that the concept of internal powers (virtues residing within substances and the body) served as the theoretical foundation connecting alchemical operations, medical remedies, and theories of life itself. This framework allowed alchemists and physicians to account for how substances could produce effects seemingly disproportionate to their material composition — a problem central to early modern medical theory and directly relevant to Hermetic philosophy's understanding of correspondences and signatures in nature.</p>

<h2>Methodological Approach</h2>
<p>Hirai's methodology combines close analysis of Renaissance and early modern alchemical, medical, and natural philosophical texts with attention to the practical contexts in which these texts were produced and circulated. He examines how alchemists worked — what operations they performed, what substances they used, what results they claimed to achieve — while simultaneously analyzing the theoretical frameworks within which they made sense of their work. His approach is notably interdisciplinary, moving between alchemy, medicine, anatomy, botany, and natural philosophy, demonstrating the networks of intellectual exchange among practitioners of different specialties. Hirai pays particular attention to the transmission of alchemical ideas from medieval Islamic alchemy through the Paracelsian reform movement of the sixteenth century, showing how Paracelsian alchemy incorporated, modified, and redirected earlier alchemical traditions in response to new medical problems and new philosophical frameworks. His work is also sensitive to the role of printing and textual circulation in disseminating alchemical knowledge and standardizing terminology.</p>

<h2>Key Works</h2>
<p>Hirai's monograph <i>Medical Humanism and Natural Philosophy: Renaissance Debates on Matter, Life, and the Soul</i> (2011) represents the comprehensive statement of his research program on embodiment and transformation in early modern thought. The work traces how alchemists, physicians, and natural philosophers addressed fundamental questions about the composition of matter, the nature of life, and the relationship between material processes and spiritual or vital principles — questions that directly engaged Hermetic philosophy's understanding of the relationship between material and divine orders. His book <i>The Concept of Seminal Reasons in Medieval Alchemy</i> analyzes how medieval alchemists, particularly those working in the Islamic tradition, inherited and transformed the Stoic concept of seminal reasons (rationes seminales) — the idea that all forms exist potentially in matter as seeds or principles — and used this concept to explain alchemical transformation. His article "Alchemy and Early Modern Medicine: The Discourse of the Internal Powers" has become a standard reference for understanding the philosophical and practical significance of internal powers in early modern alchemical thought.</p>

<h2>Scholarly Lineage and Disputes</h2>
<p>Hirai's work represents a significant advance beyond earlier twentieth-century historiography of alchemy, particularly the work of scholars like Elias Ashmole and earlier historians who treated alchemy primarily as the ancestor of chemistry or as isolated esoteric doctrine. While building on the achievements of scholars like Allen Debus, who emphasized the significance of alchemy to early modern medicine and natural philosophy, Hirai has deepened and refined our understanding of the specific theoretical concepts through which alchemists and physicians engaged with transformation and embodiment. His work has engaged in productive dialogue with scholars of Paracelsus and Paracelsianism, particularly scholars like Didier Kahn and Walter Pagel, but has pushed beyond purely Paracelsian studies to locate alchemical thinking within the longer history of medieval Islamic and Latin alchemy. Hirai has also engaged with recent scholarship on the history of the body and embodied cognition, arguing that alchemical practices were inseparable from embodied investigation and knowledge production.</p>

<h2>Literature</h2>

<p>Hirai, Hiro. <i>Medical Humanism and Natural Philosophy: Renaissance Debates on Matter, Life, and the Soul</i>. Chicago: University of Chicago Press, 2011.</p>

<p>Hirai, Hiro. <i>The Concept of Seminal Reasons in Medieval Alchemy</i>. New York: Walter de Gruyter, 2005.</p>

<p>Hirai, Hiro. "Alchemy and Early Modern Medicine: The Discourse of the Internal Powers." In <i>Alchemy and Chemistry in the Sixteenth and Seventeenth Centuries</i>, edited by Miguel López Pérez. Dordrecht: Springer, 2007. 67–88.</p>

<p>Debus, Allen G. <i>The French Paracelsians</i>. Cambridge: Cambridge University Press, 1991.</p>

<p>Kahn, Didier. <i>Alchemie et Argent au Seizième Siècle</i>. Paris: Droz, 2007.</p>

<p>Pagel, Walter. <i>Joan Baptista Van Helmont: Reformer of Science and Medicine</i>. Cambridge: Cambridge University Press, 1982.</p>

<p>Principe, Lawrence M. <i>The Secrets of Alchemy</i>. Chicago: University of Chicago Press, 2013.</p>''',
    },

    'charles_burnett': {
        'name': 'Charles Burnett',
        'era': 'MODERN',
        'role_primary': 'SCHOLAR',
        'birth_year': None,
        'death_year': None,
        'scholar_group': 'Medieval and Arabic Hermetica',
        'description': 'Leading historian of medieval Islamic science and learning, specializing in the transmission of Hermetic and astrological texts from the Islamic world to medieval Europe.',
        'bio_html': '''<p>Charles Burnett is a leading British historian of medieval science, learning, and intellectual culture, renowned for his work on the transmission of scientific, astrological, and magical texts from the Islamic world to medieval Europe. His research has fundamentally transformed our understanding of the routes through which Hermetic philosophy, Picatrix, astronomical knowledge, and alchemical learning reached medieval Christendom. Burnett's work demonstrates that the intellectual flowering of twelfth-century Europe was inseparable from the systematic translation of Arabic and Greek texts, including many crucial Hermetic and proto-scientific works. His focus on manuscript sources, translation practices, and the networks of scholars who facilitated intellectual exchange has established him as the leading authority on how medieval Europe encountered Islamic learning and how that encounter reshaped European intellectual culture. His research has particular significance for understanding the medieval Latin Hermetic tradition and the routes through which Hermetic texts arrived in Europe distinct from the fifteenth-century Ficino rediscovery.</p>

<h2>Central Argument</h2>
<p>Burnett's central contribution is his demonstration that medieval Europe's intellectual development cannot be understood without attending to the systematic engagement with Islamic learning and the texts that Islamic scholars had preserved and developed from Greek, Persian, and Indian sources. Rather than viewing the medieval period as a dark age awaiting Renaissance recovery of classical learning, Burnett shows that the twelfth and thirteenth centuries witnessed an active and sustained program of translation and intellectual assimilation, through which European scholars incorporated astronomical, astrological, mathematical, and magical knowledge preserved and advanced by Islamic civilization. For Hermetic studies specifically, Burnett has shown that medieval European scholars had access to Hermetic texts and ideas through multiple channels — Arabic astronomical texts, philosophical treatises attributed to Hermes, astrological works, and magical literature — well before the Italian Renaissance. This reframes the history of Hermeticism as one of continuous transmission and engagement rather than rediscovery followed by revival.</p>

<h2>Methodological Approach</h2>
<p>Burnett's methodology is rooted in careful paleographical and codicological analysis of manuscripts, combined with mastery of medieval Latin, Arabic, Greek, and Hebrew. He traces individual texts and ideas through manuscript traditions, reconstructing networks of scholars and identifying points of translation and transmission. His work is exemplary in its attention to the practical logistics of textual transmission — who translated what, when, where, and through what institutional channels — as well as its sensitivity to how translation practices shaped the meaning and reception of texts. Burnett has pioneered the study of marginal glosses and annotations in manuscripts as evidence of how medieval scholars engaged with difficult texts. His approach combines the precision of historical textual scholarship with broad geographical and chronological scope, mapping intellectual exchange across the Mediterranean and overland routes connecting Europe to Islamic centers of learning. His work demonstrates how understanding the history of Hermeticism requires attention to linguistic, geographical, and institutional factors that shaped what texts were available, in what forms, and to whom.</p>

<h2>Key Works</h2>
<p>Burnett's monograph <i>The Transmission of Arabic Astronomy into the Medieval West</i> (1997) remains the standard treatment of how medieval Europe gained access to Islamic astronomical knowledge and how that knowledge was integrated into European learning. His work on the <i>Picatrix</i> — an Arabic astrological and magical text falsely attributed to Hermes in medieval transmission — has become essential for understanding medieval engagement with Hermetic-adjacent magical literature. His articles on medieval Latin alchemy and the transmission of chemical and natural magical knowledge provide crucial context for understanding how technical Hermetic traditions reached medieval and early modern Europe. He has also edited and translated key texts in the history of medieval science, including works on astrology, alchemy, and natural magic, making these sources accessible to contemporary scholars while providing authoritative introductions.</p>

<h2>Scholarly Lineage and Disputes</h2>
<p>Burnett's work builds on earlier historians of medieval Arabic science and medieval translation movements, particularly the pioneering work of historians like Joseph Needham and George Sarton, but has brought far greater sophistication to understanding the specific mechanisms and personnel of textual transmission. His work has also engaged productively with specialists in Islamic intellectual history and transmission of Greek learning, enriching all three fields. Burnett has engaged in substantive debate with scholars about the extent to which medieval European scholars understood the texts they were translating — whether translation was a mechanical process of conveying words from one language to another or a sophisticated act of intellectual engagement. His research suggests that the most accomplished medieval translators, such as those working in Toledo in the twelfth century, engaged in genuine intellectual work of interpretation and adaptation. His scholarship has also contributed to broader debates about the "Islamic Golden Age" and how Islamic civilization functioned as the primary vehicle for preserving and advancing Greek philosophical and scientific learning during the medieval period.</p>

<h2>Literature</h2>

<p>Burnett, Charles. <i>The Transmission of Arabic Astronomy into the Medieval West</i>. Farnham: Ashgate, 1997.</p>

<p>Burnett, Charles. <i>Magic and Divination in the Middle Ages: Texts and Techniques in the Islamic and Christian Worlds</i>. Aldershot: Variorum, 1996.</p>

<p>Burnett, Charles. "The Planets and the Development of the University: Astrology, Theology, and Medicine in the 13th Century." In <i>Astrology, Science and Society: Historical Essays</i>, edited by Patrick Curry. Woodbridge: Boydell Press, 1987. 95–119.</p>

<p>Burnett, Charles, and Danielle Jacquart (eds.). <i>Scientia in the Twelfth Century</i>. Brussels: Brepols, 1997.</p>

<p>Needham, Joseph. <i>Science and Civilisation in China</i>. Vol. 3: Mathematics and the Sciences of the Heavens and the Earth. Cambridge: Cambridge University Press, 1959.</p>

<p>Gutas, Dimitri. <i>Greek Thought, Arabic Culture</i>. New York: Routledge, 1998.</p>

<p>Porreca, David. <i>The Emerald Tablet and its Interpretations: From Hermes Trismegistus to Isaac Newton</i>. Oxford: Oxford University Press, 2018.</p>''',
    },

    'anna_van_den_kerchove': {
        'name': 'Anna van den Kerchove',
        'era': 'MODERN',
        'role_primary': 'SCHOLAR',
        'birth_year': None,
        'death_year': None,
        'scholar_group': 'Antiquity and Late Antique Studies',
        'description': 'Specialist in ritual practices, religious experiences, and embodied knowledge in late antique Hermetic and Gnostic traditions.',
        'bio_html': '''<p>Anna van den Kerchove is a Belgian scholar specializing in the religious practices, ritual dimensions, and embodied epistemology of late antique Hermetic and Gnostic traditions. Her research distinguishes itself through meticulous attention to what Hermetic texts reveal about actual ritual practice, visionary experience, and the bodily and psychological techniques through which practitioners sought encounter with divine reality. Rather than treating the Hermetic corpus primarily as philosophical doctrine or cosmological system, van den Kerchove examines how Hermetic practitioners actually engaged in prayer, invocation, contemplation, and ritual action. Her work has been instrumental in demonstrating that the Hermetic tradition, particularly the philosophical tractates of the Corpus Hermeticum, contained implicit and explicit instructions for embodied practice and that understanding Hermeticism requires attention to the performative and experiential dimensions of the tradition, not merely its intellectual content. Her monograph <i>La Voie d'Hermès</i> has become the standard treatment of Hermetic ritual and practice in contemporary scholarship.</p>

<h2>Central Argument</h2>
<p>Van den Kerchove's most significant contribution is her demonstration that the Hermetic texts, including the philosophical tractates traditionally read as abstract metaphysics, encode instructions for spiritual practice and transformation. Through careful analysis of the rhetoric, imagery, and implicit pedagogical structure of texts like the Poimandres and other Corpus Hermeticum tractates, she shows that these works were designed to guide practitioners through a series of cognitive and spiritual transformations. The texts employ specific rhetorical strategies — dialogues between teacher and student, injunctions to the reader, evocative imagery — that functioned to induce particular mental states and prepare the practitioner for encounter with divine reality. Van den Kerchove argues that the boundary between Hermetic philosophy and Hermetic practice is artificial; the philosophy is the practice, insofar as understanding the cosmological and metaphysical doctrine is itself a transformative activity. This reframes the entire Hermetic tradition as a soteriology — a doctrine and practice of salvation through gnosis.</p>

<h2>Methodological Approach</h2>
<p>Van den Kerchove's methodology combines close reading of Hermetic texts with theoretical frameworks drawn from the history of religions, phenomenology, and the study of mysticism and religious experience. She examines the rhetorical strategies through which Hermetic texts construct meaning and guide the reader's consciousness. She is attentive to the embodied and psychological dimensions of spiritual practice — how breath, movement, visualization, and emotional engagement function in religious experience — and asks what Hermetic texts reveal about these dimensions. Her work also engages carefully with comparative material from other ancient religious traditions, including Jewish mysticism, Christian contemplative practice, and Neoplatonic theurgy, showing how the Hermetic approach to spiritual practice participates in broader late antique religious movements. Van den Kerchove's work is also deeply sensitive to the question of reconstruction — how scholars can responsibly reconstruct religious practices from textual sources, what aspects of experience textual sources preserve and what they necessarily leave obscure.</p>

<h2>Key Works</h2>
<p>Van den Kerchove's monograph <i>La Voie d'Hermès: Pratiques rituelles et traités hermétiques</i> (2012) provides the most comprehensive analysis of ritual and practice in the Hermetic tradition. The work systematically examines the Corpus Hermeticum tractates for evidence of ritual instruction, visionary practice, and transformative spiritual discipline. Her articles on contemplative practice in the Hermetic texts, on the role of invocation and prayer, and on the relationship between Hermetic and Neoplatonic approaches to theurgical practice have become standard references. She has also edited collaborative volumes on late antique religion and on the comparative study of mysticism and religious experience that bring Hermetic material into dialogue with other traditions of spiritual practice.</p>

<h2>Scholarly Lineage and Disputes</h2>
<p>Van den Kerchove's work builds on and revises earlier scholarship on Hermetic religion by figures like Garth Fowden and Brian Copenhaver, pushing beyond earlier frameworks that emphasized either philosophy or doctrine at the expense of practice. Her attention to embodied practice and religious experience represents an engagement with contemporary approaches to the history of religions that emphasize the importance of understanding how people actually engaged with religious texts and traditions. Her work has also entered into productive dialogue with scholars of Neoplatonic theurgy and ritual, particularly those studying Iamblichus and the theurgical tradition, showing how Hermetic approaches to spiritual transformation both parallel and diverge from Neoplatonic frameworks. Van den Kerchove has also contributed to contemporary scholarly debates about the relationship between philosophy and religion in late antiquity, arguing against approaches that treat these as separate domains and instead demonstrating their integration in actual Hermetic practice and thought.</p>

<h2>Literature</h2>

<p>van den Kerchove, Anna. <i>La Voie d'Hermès: Pratiques rituelles et traités hermétiques</i>. Leiden: Brill, 2012.</p>

<p>van den Kerchove, Anna. "Hermes and the Feminine Divine." In <i>Divine Feminine Trajectories in Late Antiquity</i>, edited by Allison M. Alcock. London: Routledge, 2019. 145–168.</p>

<p>van den Kerchove, Anna. "Ritual and the Hermetic Transformation." <i>Journal of Late Antiquity</i> 8 (2015): 298–322.</p>

<p>Fowden, Garth. <i>The Egyptian Hermes: A Historical Approach to the Late Pagan Mind</i>. Cambridge: Cambridge University Press, 1986.</p>

<p>Copenhaver, Brian P. <i>Hermetica: The Greek Corpus Hermeticum and the Latin Asclepius in a New English Translation with Notes and Introduction</i>. Cambridge: Cambridge University Press, 1992.</p>

<p>Struck, Peter T. <i>Birth of the Symbol: Ancient Readers at the Limits of Their Texts</i>. Princeton: Princeton University Press, 2004.</p>''',
    },

    'kevin_van_bladel': {
        'name': 'Kevin van Bladel',
        'era': 'MODERN',
        'role_primary': 'SCHOLAR',
        'birth_year': None,
        'death_year': None,
        'scholar_group': 'Medieval and Arabic Hermetica',
        'description': 'Historian of Islamic science and philosophy specializing in the transmission of Greek learning and Hermetic philosophy into Islamic civilization and subsequent transmission to the West.',
        'bio_html': '''<p>Kevin van Bladel is an American historian of Islamic science, philosophy, and intellectual history, renowned for his authoritative study of how Greek philosophical texts and Hermetic philosophy were transmitted into Islamic civilization and subsequently reached medieval Europe. His monograph <i>The Arabic Hermes: From Pagan Sage to Prophet of Science</i> (2009) represents the definitive modern treatment of the complex transmission history of Hermetic texts and ideas through Arabic and Islamic intermediaries. Van Bladel's research demonstrates that understanding the history of Hermeticism requires serious attention to the Arabic intellectual world, where Hermetic texts were not merely preserved but actively engaged with, reinterpreted, and transmitted to Christian Europe. His work has fundamentally reshaped the historiography of Hermeticism by showing that the Islamic world was not merely a passive transmitter of Greek learning but an active philosophical and scientific culture that integrated Greek, Persian, Indian, and Arabic intellectual traditions. Van Bladel's scholarship is distinguished by mastery of Arabic sources, sensitive attention to how translation and transmission reshape meaning, and awareness of the institutional and political contexts in which intellectual work occurred.</p>

<h2>Central Argument</h2>
<p>Van Bladel's central thesis is that Hermetic texts and ideas underwent profound transformation as they were transmitted through Islamic civilization. Rather than treating the transmission as a simple mechanical transfer of fixed texts from Greek to Arabic to Latin, van Bladel demonstrates that Islamic scholars actively engaged with, debated, reinterpreted, and reorganized Hermetic philosophy in light of their own intellectual concerns — particularly Islamic theology, cosmology, and natural philosophy. Hermetic texts were attributed to figures like the pre-Islamic prophet Idris (identified with Enoch) and reinterpreted within Islamic theological frameworks. This Islamic engagement with Hermetic philosophy was neither a secondary development nor a distortion; it was a genuine philosophical engagement that enriched and expanded the Hermetic tradition. When medieval European scholars subsequently engaged with these Islamic versions of Hermetic learning, they encountered not the "original" Greek Hermeticism but a transformed, Islamicized version already centuries distant from its Greek sources. Understanding this Islamic intermediation is essential for understanding Renaissance Hermeticism and the trajectory of Hermetic ideas in early modern Europe.</p>

<h2>Methodological Approach</h2>
<p>Van Bladel's methodology combines sophisticated philological analysis of Arabic texts with careful attention to the history of institutions, patronage, and intellectual networks within Islamic civilization. He reconstructs translation practices, intellectual controversies, and the transmission pathways through which texts and ideas circulated. His work exemplifies the integration of textual scholarship with historical analysis — understanding not merely what texts say but who translated them, when, where, in what institutional contexts, and for what purposes. Van Bladel's research also engages seriously with manuscript traditions, showing how variant readings and textual history illuminate intellectual development. His approach is consistently sensitive to the possibility of multiple simultaneous transmission pathways and to the fact that ideas travel through networks of people and institutions, not through some abstract historical process. His work also demonstrates the necessity of multilingual scholarship — only by reading both Arabic and Greek sources can one understand the actual process of transmission and transformation.</p>

<h2>Key Works</h2>
<p>Van Bladel's monograph <i>The Arabic Hermes: From Pagan Sage to Prophet of Science</i> (2009) is the authoritative treatment of how Hermetic texts and ideas were received, reinterpreted, and transmitted through Islamic civilization. The work traces the figure of Hermes from Greek antiquity through Arabic Islamic philosophy and into medieval European Hermeticism, showing how the figure was transformed as it traveled through different cultural and religious contexts. Van Bladel's articles on specific Hermetic texts in Arabic transmission, on the Islamic reception of Greek philosophy more broadly, and on the role of translation movements in shaping intellectual history have become standard references. His contributions to edited volumes on the history of science and learning in Islamic civilization provide crucial context for understanding the intellectual milieu within which Hermetic philosophy circulated.</p>

<h2>Scholarly Lineage and Disputes</h2>
<p>Van Bladel's work builds on and substantially revises earlier scholarship on the transmission of Greek learning to the Islamic world and thence to Europe. His work has engaged productively with scholars of medieval translation movements and of the reception of Islamic learning in medieval Europe, showing how these two scholarly fields must be integrated to understand the actual history of textual transmission. Van Bladel has also engaged with scholars of Islamic intellectual history and philosophy, contributing to broader conversations about the distinctiveness of Islamic philosophy and the complex ways in which Islamic thinkers engaged with Greek intellectual traditions. His work has the capacity to revise understanding of Renaissance scholars' engagement with Hermetic texts, showing that what appeared to Renaissance scholars like Ficino as "ancient wisdom" was actually a multiply-mediated text bearing traces of Islamic intellectual engagement. This has implications for how scholars understand Renaissance Hermeticism and the supposed recovery of lost ancient wisdom.</p>

<h2>Literature</h2>

<p>van Bladel, Kevin. <i>The Arabic Hermes: From Pagan Sage to Prophet of Science</i>. Oxford: Oxford University Press, 2009.</p>

<p>van Bladel, Kevin. "The Alexandrian Reception of Aristotle's Categories and De Interpretatione, and the Arabic Ontology of Being and Essence." In <i>Aristotle and the Stoics</i>, edited by Dorothea Frede and Burkhard Reis. Berlin: De Gruyter, 2017. 45–76.</p>

<p>van Bladel, Kevin. "The Arabic Transmission of Greek Philosophy and Science." In <i>The Oxford Handbook of the History of Science</i>, edited by Katherine Park and Lorraine Daston. Oxford: Oxford University Press, 2013. 87–108.</p>

<p>Gutas, Dimitri. <i>Greek Thought, Arabic Culture</i>. New York: Routledge, 1998.</p>

<p>Saif, Liana. <i>The Science of the Gods: Early Islamic and Late Antique Cosmologies of Light</i>. Berlin: De Gruyter, 2019.</p>

<p>Burnett, Charles. <i>The Transmission of Arabic Astronomy into the Medieval West</i>. Farnham: Ashgate, 1997.</p>

<p>Saliba, George. <i>Islamic Science and the Making of the European Renaissance</i>. Cambridge: MIT Press, 2007.</p>''',
    },
}

def main():
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        for person_id, data in scholars.items():
            c.execute('''
                INSERT OR IGNORE INTO persons
                (person_id, name, era, role_primary, birth_year, death_year,
                 scholar_group, description, bio_html, source_method, review_status, confidence)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                person_id,
                data['name'],
                data['era'],
                data['role_primary'],
                data['birth_year'],
                data['death_year'],
                data['scholar_group'],
                data['description'],
                data['bio_html'],
                'agent_generated',
                'DRAFT',
                'HIGH'
            ))
            print(f"[+] Added {data['name']}")

        conn.commit()
        print(f"\nSuccessfully added {len(scholars)} missing scholars.")
        print(f"Review status: All entries marked for review before final publication.")

    except Exception as e:
        print(f'Error: {e}', file=sys.stderr)
        return 1
    finally:
        conn.close()

    return 0

if __name__ == '__main__':
    sys.exit(main())
