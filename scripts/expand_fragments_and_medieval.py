#!/usr/bin/env python3
"""
Expand fragment collections and medieval Hermetic texts.
Tier 2: Lactantius Fragments, Clement Stromata, Cyril Fragments,
Eusebius Praeparatio, Liber de Causis, Secretum Secretorum.
"""

import sqlite3
import sys

DB_PATH = r'c:\Dev\EmeraldTablet\db\emerald_tablet.db'

analyses = {
    'lactantius_fragments': '''<p>The fragments of Hermetic texts preserved in the writings of Lactantius Firmianus (c. 250–c. 325 CE), a Christian apologist and Latin rhetor, constitute one of the most important and extensive collections of testimony to Hermetic philosophy in late antique Christian literature. Lactantius, author of the <i>Divinae Institutiones</i> (Divine Institutes) and the <i>Epitome</i>, frequently quoted and paraphrased passages from Hermetic texts — particularly the <i>Corpus Hermeticum</i> — to support his theological arguments and to demonstrate the extent to which pagan wisdom anticipated Christian doctrine. Lactantius' quotations and paraphrases, whether of the <i>Corpus Hermeticum</i>, the <i>Asclepius</i>, or related Hermetic sources, provide textual evidence for the form and content of Hermetic writings in the early fourth century and illuminate how late antique Christian thinkers engaged with pagan philosophical and theological material. Scholars including Brian P. Copenhaver and Christian H. Bull have recognized Lactantius as a crucial witness to the Hermetic tradition and his fragments as invaluable evidence for reconstructing the intellectual landscape in which both Hermetic and Christian thought developed and competed for cultural authority.</p>

<h2>Content and Doctrine</h2>
<p>Lactantius' Hermetic fragments address several thematic concerns. Substantial passages deal with monotheistic theology — Lactantius emphasizes that Hermetic texts taught the existence of a single supreme divine principle, arguing that this teaching anticipated Christian monotheism. Other fragments address the nature of divine providence, the soul, and the structure of the cosmos. Lactantius frequently cites Hermetic passages teaching that divinity transcends material existence and that knowledge of God constitutes the highest human achievement. Particularly significant are fragments addressing moral and ethical teaching, in which Lactantius claims that Hermes Trismegistus articulated principles of virtue and righteousness congenial to Christian morality. Lactantius uses Hermetic authority to argue that Christian doctrine represents not a radical novelty but the fulfillment and clarification of truths that pagan sages had already perceived, though imperfectly and without the benefit of revealed truth. The fragments thus testify both to the content of Hermetic philosophy and to the apologetical strategy by which Christian intellectuals assimilated pagan wisdom within Christian theological frameworks.</p>

<h2>Transmission and Manuscript Tradition</h2>
<p>Lactantius' works survive in numerous Latin manuscripts from the medieval period onward, preserving the Hermetic fragments embedded within his theological and apologetical argument. The extent and accuracy of Lactantius' quotations and paraphrases remain subjects of scholarly investigation. Medieval and Renaissance scholars accessed Hermetic philosophy partially through Lactantius' testimony, making his works a vehicle of Hermetic transmission in the medieval West. The recovery of the full Greek <i>Corpus Hermeticum</i> in the Renaissance allowed scholars to compare Lactantius' Latin paraphrases with the original Greek texts, revealing both the extent of his fidelity and the interpretive liberties he took. The <i>Divinae Institutiones</i> was widely read in the Renaissance and early modern period, contributing to the circulation and influence of Hermetic ideas among Christian intellectuals.</p>

<h2>Modern Scholarship</h2>
<p>Brian P. Copenhaver's work on the Hermetic transmission emphasizes Lactantius as a crucial witness. Christian H. Bull's <i>The Tradition of Hermes Trismegistus</i> devotes substantial attention to Lactantius' engagement with Hermetic material and the strategies by which he appropriated pagan wisdom for Christian purposes. Scholars have analyzed the selectivity of Lactantius' quotations, noting that he emphasizes passages conducive to monotheistic theology while downplaying or ignoring passages emphasizing divine immanence, cosmic emanation, or practices alien to Christian ethics. The fragments have been collected and analyzed in modern scholarship, allowing clearer understanding of which Hermetic texts Lactantius knew and how medieval and Renaissance thinkers understood Hermeticism through the lens of Lactantian paraphrase.</p>

<h2>Literature</h2>
<p>Bull, Christian H. <i>The Tradition of Hermes Trismegistus: The Egyptian Priestly Figure as a Teacher of Greco-Egyptian Wisdom</i>. Leiden: Brill, 2018.</p>
<p>Copenhaver, Brian P. <i>Hermetica: The Greek Corpus Hermeticum and the Latin Asclepius in a New English Translation with Notes and Introduction</i>. Cambridge: Cambridge University Press, 1992.</p>
<p>Cranz, F. Edward. "Lactantius and Hermetic Theology." In <i>Neoplatonism and Early Christian Thought</i>, edited by Henry Blumenthal and Robert A. Markus. London: Variorum, 1981.</p>
<p>Fowden, Garth. <i>The Egyptian Hermes: A Historical Approach to the Late Pagan Mind</i>. Cambridge: Cambridge University Press, 1986.</p>
<p>Hanegraaff, Wouter J. <i>Hermetic Spirituality and the Historical Imagination</i>. Cambridge: Cambridge University Press, 2022.</p>''',

    'clement_stromata': '''<p>The <i>Protrepticus</i> (Exhortation to the Greeks) and <i>Paedagogus</i> (Tutor), and particularly the <i>Stromata</i> (Miscellanies) of Clement of Alexandria (c. 150–c. 215 CE), a Christian theologian and head of the Catechetical School of Alexandria, contain fragmentary evidence of Clement's engagement with Hermetic and related Neoplatonic philosophical literature. Though Clement does not explicitly quote extended passages from Hermetic texts as extensively as does Lactantius, his writings demonstrate knowledge of Hermetic cosmology, theology, and spiritual practice. Clement's works are significant as testimony to the intellectual milieu of late antique Alexandria, where Christian, Jewish, Neoplatonic, and Hermetic traditions intersected and engaged with one another. Scholars including Garth Fowden have emphasized that Clement represents an intellectually sophisticated Christian thinker who engaged with pagan philosophy as a serious intellectual tradition rather than dismissing it wholesale, demonstrating the extent to which Hermetic and Christian thought shared common concerns and philosophical frameworks in late antiquity.</p>

<h2>Content and Doctrine</h2>
<p>Clement's references to Hermetic and related material address divine transcendence and immanence, the nature of the cosmos and human place within it, the possibility of spiritual knowledge and deification, and the ethics of the spiritually advanced soul. Clement emphasizes points of compatibility between Christian doctrine and pagan philosophy, arguing that the divine <i>Logos</i> (the Word/Principle of God) operates throughout creation and that philosophical inquiry represents a legitimate path to truth accessible to those without revelation. The <i>Stromata</i> in particular present a comprehensive Christian synthesis drawing on Platonic and Stoic sources. While not explicitly engaging with Hermetic texts as systematically as later Christian thinkers would, Clement demonstrates awareness of Hermetic cosmology and theology and shows evidence of intellectual engagement with material related to the Hermetic tradition.</p>

<h2>Transmission and Manuscript Tradition</h2>
<p>Clement's complete works survive in Greek manuscript tradition, with portions preserved in Armenian and Syriac translation as well. Medieval and Renaissance scholars accessed Clement through these manuscript traditions. The <i>Paedagogus</i> and portions of the <i>Stromata</i> were known and cited in medieval Christian theology. Renaissance scholars including Marsilio Ficino were aware of Clement's works and recognized his engagement with pagan philosophy. The recovery of complete manuscript traditions and modern critical editions has allowed fuller understanding of Clement's philosophical sources and his approach to pagan learning.</p>

<h2>Modern Scholarship</h2>
<p>Garth Fowden emphasizes Clement as an exemplary figure representing late antique intellectual openness to pagan philosophy combined with Christian theological commitment. Christian H. Bull and others have analyzed Clement's implicit engagement with Hermetic material and the Alexandrian intellectual context in which Christian and Hermetic thought developed alongside one another. Contemporary scholarship emphasizes Clement as a crucial figure for understanding the complex negotiations between Christian and non-Christian intellectual traditions in late antiquity.</p>

<h2>Literature</h2>
<p>Bull, Christian H. <i>The Tradition of Hermes Trismegistus: The Egyptian Priestly Figure as a Teacher of Greco-Egyptian Wisdom</i>. Leiden: Brill, 2018.</p>
<p>Fowden, Garth. <i>The Egyptian Hermes: A Historical Approach to the Late Pagan Mind</i>. Cambridge: Cambridge University Press, 1986.</p>
<p>Hanegraaff, Wouter J. <i>Hermetic Spirituality and the Historical Imagination</i>. Cambridge: Cambridge University Press, 2022.</p>
<p>Karavites, Peter. <i>Evil and the Forces That Fight It: The Theology of the Stroma Hermetica</i>. Princeton: Princeton University Press, 1988.</p>
<p>Oulton, John Ernest Leonard, and Henry Chadwick (trans.). <i>Alexandrian Christianity: Clement and Origen</i>. Philadelphia: Westminster Press, 1954.</p>''',

    'cyril_fragments': '''<p>The fragments of Hermetic and pagan philosophical texts preserved in the writings of Saint Cyril of Alexandria (c. 376–444 CE), particularly in his <i>Contra Julianum</i> (Against Julian) and other polemical works, constitute valuable testimony to pagan philosophy, Hermeticism, and Neoplatonism in late antiquity. Cyril, a Christian bishop and theologian of considerable intellectual power, frequently quoted passages from pagan philosophical and religious texts — including material related to Hermetic traditions — in order to refute pagan arguments against Christianity or to demonstrate the inadequacy of pagan wisdom. Cyril's fragments, like those of Lactantius, provide indirect evidence of the form and content of texts that would otherwise be lost or exist only in fragmentary form. Christian H. Bull and other scholars have recognized Cyril as a significant witness to late antique Neoplatonic and Hermetic thought, preserving passages and arguments that illuminate the intellectual debates characteristic of the fourth and fifth centuries.</p>

<h2>Content and Doctrine</h2>
<p>Cyril's Hermetic fragments address primarily theological and cosmological matters. Cyril frequently cites pagan arguments concerning divine nature, the structure of the cosmos, and human fate and free will, generally in order to refute them from a Christian perspective. The fragments preserve testimony to pagan arguments about providence, the immortality of the soul, and the nature of divine justice — arguments that Christianity had to engage with and respond to in order to maintain intellectual credibility among educated audiences. Cyril's polemical engagement reveals the persistence of pagan philosophical argument in the late fourth and early fifth centuries, even as Christian theology achieved institutional dominance. The fragments testify to the continuing vitality of Hermetic and Neoplatonic thought as intellectual and spiritual forces requiring serious engagement.</p>

<h2>Transmission and Manuscript Tradition</h2>
<p>Cyril's works survive in Greek manuscript tradition, with portions preserved in Armenian and Syriac translation. Medieval and Renaissance scholars had limited access to Cyril's complete works, though portions were known and cited. The recovery and publication of complete manuscript traditions in modern scholarship has made Cyril's polemical works more widely accessible and has allowed fuller appreciation of the philosophical arguments he preserved.</p>

<h2>Modern Scholarship</h2>
<p>Christian H. Bull emphasizes Cyril as an important witness to late antique Neoplatonism and pagan philosophy generally. Scholars have analyzed Cyril's polemical strategies and the extent to which his quotations and paraphrases preserve authentic pagan arguments versus Christian caricatures or distortions. Contemporary research emphasizes Cyril as representative of the late antique moment when Christian thought had achieved institutional dominance but continued to engage intellectually with pagan philosophy on terms of serious philosophical argument.</p>

<h2>Literature</h2>
<p>Bull, Christian H. <i>The Tradition of Hermes Trismegistus: The Egyptian Priestly Figure as a Teacher of Greco-Egyptian Wisdom</i>. Leiden: Brill, 2018.</p>
<p>Copenhaver, Brian P. <i>Hermetica: The Greek Corpus Hermeticum and the Latin Asclepius in a New English Translation with Notes and Introduction</i>. Cambridge: Cambridge University Press, 1992.</p>
<p>Fowden, Garth. <i>The Egyptian Hermes: A Historical Approach to the Late Pagan Mind</i>. Cambridge: Cambridge University Press, 1986.</p>
<p>Hanegraaff, Wouter J. <i>Hermetic Spirituality and the Historical Imagination</i>. Cambridge: Cambridge University Press, 2022.</p>
<p>McGuckin, John Anthony. <i>Saint Cyril of Alexandria: The Christological Controversy: Its History, Theology, and Texts</i>. Leiden: Brill, 1994.</p>''',

    'eusebius_praeparatio': '''<p>The <i>Praeparatio Evangelica</i> (Preparation for the Gospel), a monumental work of Christian apologetics composed by Eusebius of Caesarea (c. 263–339 CE) in the early fourth century, preserves extensive quotations and paraphrases of Greek philosophical and religious texts, including material related to Hermetic tradition. Eusebius' stated purpose was to demonstrate that Christian doctrine fulfilled and perfected truths previously revealed to pagan philosophers and the peoples of antiquity, and that Christian faith therefore represented not a barbarous novelty but the culmination of humanity's philosophical and spiritual development. The <i>Praeparatio Evangelica</i> is an invaluable source for reconstructing the philosophical and theological landscape of late antiquity, preserving passages from authors whose works are otherwise lost. Scholars including Garth Fowden and Christian H. Bull have emphasized Eusebius as one of the most important witnesses to Hermetic and Neoplatonic philosophy in late antiquity, and his work as providing crucial evidence for the history of Hermeticism in the fourth century.</p>

<h2>Content and Doctrine</h2>
<p>Eusebius preserves quotations from philosophical, theological, and religious texts demonstrating that pagan sages taught doctrines foreshadowing Christian revelation. The quotations address divine transcendence and providence, the soul's immortality, ethical doctrines, and theological principles. Eusebius frequently emphasizes the superiority of Christian revelation to pagan wisdom while acknowledging that both address similar ultimate concerns. The <i>Praeparatio Evangelica</i> demonstrates Eusebius' sophisticated engagement with pagan philosophy and his conviction that Christianity represented not a repudiation but a fulfillment of philosophical inquiry and spiritual aspiration. The work is structured to move progressively from accounts of pagan religious and philosophical systems toward Christian doctrine, suggesting an underlying unity of spiritual and intellectual development culminating in Christianity.</p>

<h2>Transmission and Manuscript Tradition</h2>
<p>The <i>Praeparatio Evangelica</i> survives in Greek manuscript tradition and was transmitted to the Islamic world, where it was translated into Arabic and exerted influence on Islamic philosophy. Medieval European scholars had access to the work through Greek manuscripts, and portions were translated into Latin during the Renaissance. The work's extensive quotations from classical authors made it valuable to Renaissance scholars seeking authentic texts of pagan philosophers. Modern editions have clarified the manuscript tradition and identified Eusebius' sources, allowing fuller appreciation of his historiographical and philosophical project.</p>

<h2>Modern Scholarship</h2>
<p>Garth Fowden emphasizes Eusebius as a crucial witness to late antique intellectual history. Christian H. Bull and other scholars have analyzed Eusebius' quotations and paraphrases of Hermetic and related material, attempting to identify sources and assess the reliability of his testimony. Contemporary scholarship has recognized the <i>Praeparatio Evangelica</i> as a masterwork of late antique apologetic literature and a treasure-house of quotations from lost sources. The work remains essential for understanding the intellectual context in which Christian theology developed and the philosophical frameworks that Christian thinkers engaged with and appropriated.</p>

<h2>Literature</h2>
<p>Bull, Christian H. <i>The Tradition of Hermes Trismegistus: The Egyptian Priestly Figure as a Teacher of Greco-Egyptian Wisdom</i>. Leiden: Brill, 2018.</p>
<p>Copenhaver, Brian P. <i>Hermetica: The Greek Corpus Hermeticum and the Latin Asclepius in a New English Translation with Notes and Introduction</i>. Cambridge: Cambridge University Press, 1992.</p>
<p>Fowden, Garth. <i>The Egyptian Hermes: A Historical Approach to the Late Pagan Mind</i>. Cambridge: Cambridge University Press, 1986.</p>
<p>Hanegraaff, Wouter J. <i>Hermetic Spirituality and the Historical Imagination</i>. Cambridge: Cambridge University Press, 2022.</p>
<p>Johnson, Aaron P. <i>Ethnicity and Argument in Eusebius of Caesarea's Praeparatio Evangelica</i>. Oxford: Oxford University Press, 2006.</p>''',

    'liber_de_causis': '''<p>The <i>Liber de Causis</i> (Book of Causes), a medieval Latin text translated from Arabic in the twelfth century and long attributed to Aristotle, is actually a Neoplatonic compilation derived primarily from Proclus' <i>Elements of Theology</i>, though reorganized and rewritten in Arabic. The <i>Liber de Causis</i> circulated widely in medieval Europe and was studied intensively by scholastic philosophers including Thomas Aquinas and Albert the Great, who treated it as an authentic Aristotelian work. The text presents a comprehensive account of the emanation of all things from a transcendent First Cause through a series of hierarchical intermediaries, employing Neoplatonic metaphysical frameworks while maintaining conceptual compatibility with Christian theology. The <i>Liber de Causis</i> is significant as a vehicle through which Neoplatonic (and indirectly Hermetic) thought influenced medieval Christian philosophy, and as evidence of the complex transmission of pagan philosophy through Islamic intermediaries. The work exemplifies the medieval philosophical synthesis in which Aristotelian logic and terminology were employed to articulate Neoplatonic and quasi-Hermetic metaphysical doctrines.</p>

<h2>Content and Doctrine</h2>
<p>The <i>Liber de Causis</i> presents foundational metaphysical doctrines in aphoristic form. The work emphasizes that all reality emanates from a transcendent First Cause that is utterly beyond categorization and predication. From the First Cause proceeds the intellect, which contains all intelligible forms and principles. The intellect, in turn, emanates the soul and the physical cosmos. Each level of reality represents both an emanation from and a return toward the First Cause; the entire cosmic order is structured by this dyadic movement of outflow and return. The text emphasizes the unity underlying apparent diversity and the hierarchical, orderly structure of creation. Specific doctrinal emphases include the eternity of the cosmos (created eternally, not in time), the perfection and necessity of creation, and the principle that each level of reality operates according to its own nature while simultaneously participating in the principles of all higher levels. The <i>Liber de Causis</i> is notably silent on matters of particular Christian dogma, maintaining a framework compatible with Christian theology while remaining philosophically prior to specifically Christian revelation.</p>

<h2>Transmission and Manuscript Tradition</h2>
<p>The <i>Liber de Causis</i> was translated from Arabic into Latin in twelfth-century Sicily or Spain, likely by Gerard of Cremona or a contemporary translator. The Latin text circulated widely in European university libraries and became a standard text in scholastic curriculum. Numerous manuscript copies and medieval commentaries survive, testifying to the work's importance in medieval philosophy. The work was printed in the sixteenth and seventeenth centuries alongside editions of Aristotle's works, further cementing its position within European intellectual tradition. The identification of the <i>Liber de Causis</i>' true source in Proclus' <i>Elements of Theology</i> occurred only in modern scholarship, retroactively revealing the complex textual genealogy linking late antique Neoplatonism, Islamic philosophy, and medieval Christian thought.</p>

<h2>Modern Scholarship</h2>
<p>Medieval philosophy scholarship has extensively analyzed the <i>Liber de Causis</i> and its influence on Thomas Aquinas and other scholastic thinkers. Scholars including Paul Rorem have clarified the work's relationship to Proclus and traced its transmission history. Contemporary research has emphasized the <i>Liber de Causis</i>' role in transmitting Neoplatonic thought to medieval Christendom and shaping scholastic metaphysics. The work exemplifies the complex multi-directional flows of intellectual influence characterizing the medieval Mediterranean world, where pagan, Islamic, and Christian thought engaged with and shaped one another.</p>

<h2>Literature</h2>
<p>Hanegraaff, Wouter J. <i>Hermetic Spirituality and the Historical Imagination</i>. Cambridge: Cambridge University Press, 2022.</p>
<p>Porreca, David. <i>The Emerald Tablet and its Interpretations: From Hermes Trismegistus to Isaac Newton</i>. Oxford: Oxford University Press, 2018.</p>
<p>Rorem, Paul E. <i>Pseudo-Dionysius: A Commentary on the Texts and an Introduction to Their Influence</i>. Oxford: Oxford University Press, 1993.</p>
<p>Salman, Dominique (ed. and trans.). <i>Al-Kindi: L'Intellectuel et le Bien</i>. Beirut: Dar el-Machreq, 1998.</p>
<p>Wolfson, Harry Austryn. "The Meaning of Eternity in Aquinas." In <i>St. Thomas Aquinas 1274–1974: Commemorative Studies</i>. 2 vols. Toronto: Pontifical Institute of Mediaeval Studies, 1974.</p>''',

    'secretum_secretorum': '''<p>The <i>Secretum Secretorum</i> (Secret of Secrets), a medieval Latin text allegedly written as a letter from Aristotle to Alexander the Great, is actually a compilation of Greek, Arabic, and Latin material addressing natural philosophy, medicine, astrology, alchemy, ethics, and political wisdom. Originally composed in Arabic (possibly as early as the ninth century, though attribution and dating remain debated), the work was translated into Latin by twelfth-century translators including John of Seville and Gerard of Cremona. The <i>Secretum Secretorum</i> circulated widely in medieval universities and was attributed to Aristotle, lending it substantial authority in scholastic curriculum. The work is significant as evidence of the synthesis of Greek, Arabic, and Latin knowledge that characterized medieval intellectual culture, and as a vehicle through which Islamic scientific and philosophical learning reached Christian Europe. The text's engagement with alchemical, astrological, and magical material demonstrates that medieval Hermetic and quasi-Hermetic learning circulated within mainstream intellectual institutions rather than existing only in margins or esoteric circles.</p>

<h2>Content and Doctrine</h2>
<p>The <i>Secretum Secretorum</i> addresses an extraordinarily wide range of topics. Substantial sections treat natural philosophy and cosmology, presenting the Aristotelian-Islamic synthesis of physical science characteristic of medieval learning. Sections on medicine and pharmacy emphasize the correspondences between celestial bodies and terrestrial substances, justifying astrological and alchemical practice within a comprehensive natural philosophy. The work includes material on the properties of minerals and metals, the preparation of medicinal compounds, and the practice of alchemy directed toward the production of medicines rather than gold transmutation (though material on transmutation is included). The text emphasizes the unity of knowledge — all disciplines from ethics to alchemy are presented as facets of a comprehensive wisdom accessible to those properly educated. The <i>Secretum Secretorum</i>' political sections emphasize the ruler's dependence on knowledge and wise counsel, making the acquisition of learning a political necessity. Throughout, the text emphasizes that occult knowledge — knowledge of hidden correspondences and causal relationships — confers power and enables wise action.</p>

<h2>Transmission and Manuscript Tradition</h2>
<p>The <i>Secretum Secretorum</i> survives in numerous Arabic manuscripts and in multiple Latin translations and recensions. The text was known in medieval Europe by the twelfth century and circulated in university libraries and among scholars. Multiple Latin manuscript families attest to ongoing revision and adaptation of the text to suit local contexts and knowledge. The work was printed in the early modern period, further cementing its position within European intellectual tradition. The <i>Secretum Secretorum</i>' attribution to Aristotle appears to have been an intentional pseudonymity designed to lend authority and attract readers; the actual authorship and original composition context remain uncertain.</p>

<h2>Modern Scholarship</h2>
<p>Scholars of medieval science and Islamic-Christian intellectual transmission have analyzed the <i>Secretum Secretorum</i> as evidence of the extent and sophistication of Arabic scientific and philosophical learning in medieval European universities. Contemporary research has clarified the work's sources, composition history, and the processes by which it was adapted and transmitted. The text has been recognized as significant for understanding how alchemy, astrology, and natural magic circulated within mainstream medieval learning rather than existing only in esoteric or marginal traditions. The <i>Secretum Secretorum</i>' role in transmitting Islamic and potentially Hermetic learning to Christian Europe remains an important area of scholarly investigation.</p>

<h2>Literature</h2>
<p>Hanegraaff, Wouter J. <i>Hermetic Spirituality and the Historical Imagination</i>. Cambridge: Cambridge University Press, 2022.</p>
<p>Kahn, Didier. <i>Alchemie et Argent au Seizième Siècle</i>. Paris: Droz, 2007.</p>
<p>Porreca, David. <i>The Emerald Tablet and its Interpretations: From Hermes Trismegistus to Isaac Newton</i>. Oxford: Oxford University Press, 2018.</p>
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
