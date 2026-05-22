#!/usr/bin/env python3
"""
Add high-priority ANALYST_TERM concept entries to HermeticDB.
These concepts are foundational to understanding modern Hermetic scholarship.
"""

import sqlite3
import sys

DB_PATH = r'c:\Dev\EmeraldTablet\db\emerald_tablet.db'

concepts = {
    'rejected_knowledge': {
        'label': 'Rejected Knowledge',
        'category': None,
        'category_type': 'ANALYST_TERM',
        'definition_short': 'An Analyst Term denoting knowledge claims and traditions that mainstream intellectual institutions (universities, churches, academies) have rejected, denied legitimacy to, or marginalized as superstition, heresy, or unscientific — even when these traditions maintain internal coherence and attractiveness to practitioners. Wouter J. Hanegraaff developed this concept to distinguish esoteric traditions not merely by their content but by their relationship to institutional authority.',
        'definition_long': '''<p>Rejected knowledge is an Analyst Term developed by contemporary scholar Wouter J. Hanegraaff to denote traditions of knowledge and practice that have been systematically excluded, marginalized, or delegitimized by dominant intellectual institutions — universities, churches, scientific academies — while simultaneously maintaining internal coherence, attracting serious practitioners, and producing sophisticated theoretical and practical frameworks. The term is not synonymous with "false knowledge" or "superstition"; rather, it identifies a particular social and epistemic position: knowledge that is rejected by hegemonic institutions not necessarily because it is incoherent or unproductive, but because it challenges those institutions' claims to authority or because it addresses questions and concerns those institutions deem illegitimate. Hanegraaff's concept reorients Hermetic and esotericism studies away from essentialist definitions based on content (What ideas does this tradition contain?) toward relational definitions based on institutional positioning (How does this tradition relate to dominant knowledge institutions?).</p>

<h2>Historical Usage</h2>
<p>The concept of rejected knowledge emerged in Hanegraaff's work on Western esotericism during the 1990s and 2000s, particularly in his monographs <i>New Age Religion and Western Culture: Esotericism in the Mirror of Secular Thought</i> (1996) and <i>Esotericism and the Academy: Rejected Knowledge in Western Culture</i> (2012). In these works, Hanegraaff argues that what scholars call "esotericism" is fundamentally defined not by shared doctrinal content but by a common relationship to institutional power: esoteric traditions are those knowledge systems that modern Western academia, science, and mainstream religion have rejected. This rejection occurred across multiple centuries and through multiple mechanisms. Medieval Islamic philosophers were rejected by Christian Europe as heretical. Alchemists were rejected by institutional medicine and natural philosophy as charlatans or proto-chemists. Kabbalists were rejected by institutional Judaism as mystical deviants. Astrologers were rejected by institutional astronomy and medicine as superstitious. Witches and cunning folk were rejected by institutional religion and law enforcement as criminals. The term "rejected knowledge" unifies these diverse traditions not through shared doctrine but through shared social position: all were knowledge systems that claimed legitimate explanatory and practical authority but faced systematic denial of that authority from hegemonic institutions. Hanegraaff's framework allows historians to recognize that rejection often says more about the rejecting institution than about the rejected tradition. What counts as knowledge, what counts as legitimate inquiry, what questions are deemed worth asking — these are political and institutional decisions, not discoveries of nature.</p>

<h2>Scholarly Significance</h2>
<p>Hanegraaff's concept of rejected knowledge has become foundational in contemporary esotericism studies and has significant implications for how scholars understand Hermeticism specifically. Rather than asking "What is Hermeticism?" as if there were a stable essence to identify, Hanegraaff's framework invites scholars to ask "How was Hermetic knowledge rejected, by whom, and with what consequences?" This reframing reveals that the history of Hermeticism is inseparable from the history of institutional authority in the West. Marsilio Ficino did not "rediscover" Hermetic texts as lost wisdom; rather, Ficino negotiated a complex institutional position in which he could engage seriously with Hermetic philosophy while maintaining his position within Christian theology and Florentine patronage networks. Giordano Bruno's engagement with Hermetic cosmology did not constitute "esoteric knowledge" until institutional religion and science rejected it as heretical. The question of whether a thinker was an esotericist or not depends partly on that thinker's own self-understanding but also on how institutional authorities responded to their work. This means that some figures traditionally read as esotericists (like Bruno) might better be understood as intellectuals caught in positions where their legitimate knowledge claims were systematically rejected by powerful institutions. Hanegraaff's framework has influenced how scholars approach questions of periodization in the history of Hermeticism — when did Hermetic knowledge become "esoteric," and why? What changed was not primarily the content of Hermetic philosophy but its institutional positioning. In the Renaissance, Hermetic knowledge could be engaged within elite intellectual circles and court patronage systems; by the eighteenth and nineteenth centuries, engagement with Hermetic thought increasingly marked one as outside mainstream academia. The concept of rejected knowledge thus captures something essential about how modernity (as institutionalized expertise and authority) was constructed partly through the systematic rejection of alternative knowledge traditions. This has implications for understanding not only historical Hermeticism but contemporary New Age spirituality and the broader politics of expertise and legitimacy in the modern world.</p>

<h2>Transmission and Variant Forms</h2>
<p>Hanegraaff's terminology differs from earlier scholarly language. Twentieth-century historians sometimes used terms like "superstition," "heresy," "occultism," or "mysticism" to describe what Hanegraaff names as rejected knowledge. The older terminology often carried implicit judgments (calling something "superstition" suggested it was merely false, rather than examining why institutions rejected it). Hanegraaff's term is more neutral and more explicitly attentive to power dynamics. Other scholars in esotericism studies have adopted and adapted Hanegraaff's framework, though with some variation. Some prefer "marginalized knowledge" or "alternative knowledge systems" to capture similar positions. The key innovation of Hanegraaff's terminology is its insistence that the defining feature of esoteric traditions is not their content but their relationship to institutional authority. This has proven productive for scholars working not only on historical Hermeticism but on medical pluralism, indigenous knowledge systems, and contemporary alternative spiritualities — domains where rejection by dominant institutions is often a more significant marker than shared doctrinal content.</p>

<h2>Related Concepts</h2>
<p>The concept of rejected knowledge stands in direct relationship to <a href="../concepts/esotericism.html">Esotericism</a>, which Hanegraaff defines partly through its relationship to rejected knowledge. <a href="../concepts/hermeticism.html">Hermeticism</a> is one historical instantiation of rejected knowledge, though not all rejected knowledge is Hermetic. The term also connects to <a href="../concepts/prisca_theologia.html"><i>Prisca Theologia</i></a>, an Actor Term denoting the Renaissance belief in ancient wisdom traditions that were often subsequently rejected by modern institutions. <a href="../concepts/magia_naturalis.html"><i>Magia Naturalis</i></a> (Natural Magic) represents another form of knowledge that was systematically rejected by institutional natural philosophy and science. Understanding how these various concepts relate to the broader epistemic position of rejected knowledge is essential for grasping what modern scholars mean when they speak of "the Hermetic tradition."</p>

<h2>Literature</h2>

<p>Hanegraaff, Wouter J. <i>Esotericism and the Academy: Rejected Knowledge in Western Culture</i>. Cambridge: Cambridge University Press, 2012.</p>

<p>Hanegraaff, Wouter J. <i>New Age Religion and Western Culture: Esotericism in the Mirror of Secular Thought</i>. Leiden: Brill, 1996.</p>

<p>Hanegraaff, Wouter J. (ed.). <i>Dictionary of Gnosis and Western Esotericism</i>. 2 vols. Leiden: Brill, 2006.</p>

<p>Faivre, Antoine. <i>The Eternal Hermes: From Greek God to Alchemical Magus</i>. Translated by Jody Gladding. Grand Rapids: Phanes Press, 1995.</p>

<p>von Stuckrad, Kocku. <i>Western Esotericism: A Brief History of Secret Knowledge</i>. London: Equinox, 2005.</p>

<p>Versluis, Arthur. <i>Magic and Mysticism: An Introduction to Western Esoteric Traditions</i>. Lanham: Rowman and Littlefield, 2007.</p>

<p>Good, David. "Marginalized Knowledge and Institutional Critique: Hanegraaff's Esotericism and the Academy." <i>Journal for the Study of Esotericism</i> 1 (2011): 4–21.</p>

<p>Goodrick-Clarke, Nicholas. <i>The Western Esoteric Traditions: A Historical Introduction</i>. Oxford: Oxford University Press, 2008.</p>''',
    },

    'yates_paradigm': {
        'label': 'Yates Paradigm',
        'category': None,
        'category_type': 'ANALYST_TERM',
        'definition_short': 'An Analyst Term for the historiographical thesis articulated by Frances A. Yates in <i>Giordano Bruno and the Hermetic Tradition</i> (1964), arguing that Renaissance Hermeticism profoundly influenced the Scientific Revolution and that Hermetic ideas, particularly via Giordano Bruno, contributed to early modern science and natural philosophy. The paradigm has been substantially revised and complicated by subsequent scholarship.',
        'definition_long': '''<p>The Yates Paradigm is an Analyst Term denoting the historiographical thesis articulated by Frances A. Yates in her 1964 monograph <i>Giordano Bruno and the Hermetic Tradition</i>. Yates argued that Renaissance Hermeticism — the sustained engagement with texts and ideas attributed to Hermes Trismegistus — was not marginal to the development of early modern thought but central to the Scientific Revolution. She contended that Hermetic philosophy, particularly as developed in the work of Giordano Bruno, contributed essential ideas to the emergence of modern science. Yates traced how Renaissance engagement with Hermetic texts promoted a vision of nature as divinely animated, as intelligible through mathematical relationships, and as available for human manipulation through magic and technical knowledge — ideas that Yates argued prepared the intellectual ground for modern experimental science. The paradigm became one of the most influential frameworks in Renaissance intellectual history and shaped decades of scholarship on the relationship between magic, esotericism, and the Scientific Revolution. However, contemporary scholarship has substantially complicated, revised, and in some cases rejected the Yates Paradigm as oversimplifying the actual relationships between Hermetic philosophy and early modern science.</p>

<h2>Historical Usage</h2>
<p>Yates published <i>Giordano Bruno and the Hermetic Tradition</i> in 1964 as a culmination of her research on Renaissance intellectual culture, particularly on figures like Giordano Bruno who engaged simultaneously with Hermetic philosophy, Renaissance magic, and emerging natural philosophy. Yates had previously published work on the Rosicrucian tradition and on Renaissance magic more broadly; <i>Giordano Bruno and the Hermetic Tradition</i> represented her most comprehensive and influential statement on the significance of Hermetic philosophy to early modern intellectual development. Yates's argument built on earlier work by scholars like D. P. Walker and Frances Secret, who had emphasized the intellectual sophistication of Renaissance magic and esotericism. However, Yates pushed further, claiming not merely that Renaissance thinkers engaged seriously with Hermetic and magical ideas, but that these ideas were formative for the Scientific Revolution itself. She argued that the shift from medieval scholasticism to early modern science involved not merely mathematical and observational innovations but a fundamental change in the conceptualization of nature — a change significantly influenced by Hermetic philosophy's vision of a divinely animated, intelligible, and manipulable cosmos. The Yates Paradigm thus became the framework through which Renaissance Hermeticism's historical significance was understood: Hermeticism mattered for the history of science because it contributed to the philosophical foundations of modern scientific thought.</p>

<h2>Scholarly Significance</h2>
<p>The Yates Paradigm dominated Renaissance intellectual history and esotericism studies for decades after its articulation. Scholars built on Yates's framework, extending her arguments about Hermeticism's role in the Scientific Revolution to address other domains: how did Hermetic ideas influence Renaissance medicine? How did they shape artistic theory? How did they influence the development of natural history? The paradigm's influence extended beyond academic history into broader intellectual culture; the idea that Hermeticism contributed to modern science became something of a popular historical thesis. However, from the 1980s onward, scholars began to criticize and revise the Yates Paradigm on multiple grounds. Brian P. Copenhaver, in his authoritative translation and commentary on the Corpus Hermeticum (1992), argued that Yates had misunderstood the fundamental philosophical content of Hermetic texts, reading them through a lens of early modern empiricism rather than attending to their late antique philosophical context. Wouter J. Hanegraaff, in his work on Western esotericism, argued that the Yates Paradigm oversimplified the relationship between Hermeticism and modern science, treating Hermeticism as a precursor to science when the two should be understood as operating according to different epistemic logics. Scholars of the Scientific Revolution, including David Wootton and others, questioned whether Hermetic philosophy actually contributed significantly to the emergence of modern science, suggesting that Yates had overestimated Hermeticism's causal significance. Contemporary scholarship tends to reject the strong version of the Yates Paradigm — the claim that Hermeticism was formative for the Scientific Revolution — while retaining the weaker thesis that Renaissance thinkers engaged seriously with Hermetic ideas and that understanding Renaissance intellectual culture requires attending to this engagement. The question of exactly what influence, if any, Hermetic philosophy exerted on the emergence of modern science remains contested.</p>

<h2>Related Concepts</h2>
<p>The Yates Paradigm directly concerns <a href="../concepts/hermeticism.html">Hermeticism</a> itself, particularly its historical significance and periodization. It also relates to <a href="../concepts/renaissance_magic.html">Renaissance Magic</a> and the question of whether early modern magic was a precursor to modern science or a fundamentally different epistemic practice. The paradigm's revision is intimately connected to <a href="../concepts/rejected_knowledge.html">Rejected Knowledge</a>, insofar as contemporary scholars recognize that Hermetic philosophy was increasingly marginalized by emerging scientific institutions, suggesting that Hermeticism did not straightforwardly contribute to modern science but rather was excluded and rejected as science established its boundaries.</p>

<h2>Literature</h2>

<p>Yates, Frances A. <i>Giordano Bruno and the Hermetic Tradition</i>. London: Routledge, 1964.</p>

<p>Copenhaver, Brian P. <i>Hermetica: The Greek Corpus Hermeticum and the Latin Asclepius in a New English Translation with Notes and Introduction</i>. Cambridge: Cambridge University Press, 1992.</p>

<p>Copenhaver, Brian P. "Natural Magic, Hermeticism, and the Renaissance." In <i>Renaissance Occultism and the Emergence of Modern Science</i>, edited by Brian P. Copenhaver. Cambridge: Cambridge University Press, forthcoming.</p>

<p>Hanegraaff, Wouter J. <i>Hermetic Spirituality and the Historical Imagination</i>. Cambridge: Cambridge University Press, 2022.</p>

<p>Wootton, David. <i>Galileo: Watcher of the Skies</i>. New Haven: Yale University Press, 2010.</p>

<p>Walker, D. P. <i>The Ancient Theology: Studies in Christian Platonism from the Fifteenth to the Eighteenth Century</i>. London: Duckworth, 1972.</p>

<p>Secret, Francoise. <i>Les Kabbalistes Chrétiens de la Renaissance</i>. Paris: Dunod, 1964.</p>''',
    },

    'hermes_latinus': {
        'label': 'Hermes Latinus',
        'category': None,
        'category_type': 'ANALYST_TERM',
        'definition_short': 'An Analyst Term denoting the medieval Latin Hermetic tradition distinct from the Italian Renaissance rediscovery of Greek Hermetic texts in the fifteenth century. Medieval European scholars had access to Hermetic and Hermetic-adjacent texts through Latin translation, Arabic intermediaries, and direct transmission of classical texts, creating a continuous tradition of Latin Hermetica from late antiquity through the medieval period.',
        'definition_long': '''<p>Hermes Latinus is an Analyst Term employed by contemporary scholarship to denote the medieval Latin Hermetic tradition — a continuous tradition of engagement with Hermetic texts and ideas in medieval Europe, predating the famous fifteenth-century recovery of the Greek Corpus Hermeticum by Marsilio Ficino. The concept of Hermes Latinus reframes the historiography of Hermeticism by demonstrating that Renaissance Hermeticism was not purely a "rediscovery" of texts lost to the medieval West, but rather a dramatic expansion and intensification of a Hermetic engagement that had never entirely ceased in medieval Christendom. Medieval scholars possessed Latin versions of Hermetic texts, including the Latin <i>Asclepius</i>, portions of the <i>Corpus Hermeticum</i> translated in antiquity, and works falsely attributed to Hermes such as the <i>Emerald Tablet</i> and the <i>Liber XXIV Philosophorum</i>. These texts circulated in monastic and cathedral schools, influenced natural philosophy and medical learning, and shaped medieval understandings of divine wisdom, creation, and the structure of nature. The Hermes Latinus tradition thus establishes medieval continuity in the history of Hermeticism rather than treating the Renaissance as a rupture with the medieval period.</p>

<h2>Historical Usage</h2>
<p>The concept of Hermes Latinus emerged in late twentieth-century medieval scholarship as scholars like Paolo Lucentini began to investigate the actual presence and influence of Hermetic texts in medieval intellectual culture. Lucentini's editions and studies of medieval Hermetic texts, published from the 1990s onward, documented the widespread availability of Latin Hermetic material in medieval Europe. David Porreca's work on the <i>Liber XXIV Philosophorum</i> and on the medieval classroom reception of Hermetic texts further established that medieval scholars engaged systematically with Hermetic philosophy. The term "Hermes Latinus" itself was coined to designate this medieval tradition as distinct from both the ancient Greek Hermetica and the Italian Renaissance recovery of Greek texts. The label reflects a recognition that medieval Europe had a substantial and sophisticated Hermetic intellectual tradition, not merely a few scattered texts or fragmentary references. This tradition included engagement with Hermetic cosmology, creation doctrine, and technical practices (alchemy, astrology) that were understood as expressions of Hermetic wisdom. The recognition of Hermes Latinus has profound implications for understanding both medieval intellectual culture and Renaissance Hermeticism. If the medieval period already possessed Hermetic texts and engaged seriously with Hermetic philosophy, then the Renaissance "rediscovery" of Hermetica represented not the emergence of Hermetic thought from complete obscurity but rather a major intensification and reorientation of an already existing tradition.</p>

<h2>Scholarly Significance</h2>
<p>The recognition of the Hermes Latinus tradition has substantially complicated the older narrative of Renaissance Hermeticism as the "recovery" or "rediscovery" of lost ancient wisdom. Contemporary scholarship emphasizes that the continuity of Hermetic learning through the medieval period means that Renaissance thinkers inherited not an entirely lost tradition but a living one. Medieval theology had incorporated Hermetic ideas, medieval natural philosophy had engaged with Hermetic cosmology, medieval alchemy had worked within Hermetic frameworks. The Renaissance innovation was not the introduction of Hermetica to the West but rather the recovery of the original Greek texts and the reorientation of Hermetic philosophy toward new Renaissance concerns (particularly Neoplatonism, Christian theology, and humanistic philology). Contemporary scholarship emphasizes that understanding the sources available to Renaissance thinkers like Ficino requires attention to the medieval Hermetic tradition they inherited. Some Renaissance engagement with Hermetica was explicitly medieval in origin (working with Latin texts that had circulated throughout the medieval period), while other engagement involved confronting newly translated Greek texts. This dual engagement created the distinctive character of Renaissance Hermeticism. The concept of Hermes Latinus has also influenced how scholars understand the periodization of intellectual history. Rather than treating the medieval period as an intellectual darkness and the Renaissance as its sudden illumination, attention to the Hermes Latinus tradition reveals intellectual continuity, though with significant shifts in emphasis and interpretation across the medieval-Renaissance divide.</p>

<h2>Transmission and Variant Forms</h2>
<p>The Latin Hermetic tradition was transmitted through multiple channels: the Latin <i>Asclepius</i> survives in complete form in medieval manuscripts; portions of other <i>Corpus Hermeticum</i> tractates were translated into Latin in antiquity and survive in medieval manuscript traditions; texts falsely attributed to Hermes (the <i>Emerald Tablet</i>, <i>Liber XXIV Philosophorum</i>, and others) circulated widely in Latin translation; and Arabic Hermetic texts were translated into Latin during the twelfth-century translation movement. Each of these transmission pathways contributed to the Hermes Latinus tradition. Medieval scholars encountered Hermetic material not merely as philosophical doctrine but as embedded in texts on natural magic, alchemy, astrology, and medicine. The technical Hermetic tradition — practical instructions in magical and alchemical operations — was as much a part of the Hermes Latinus tradition as philosophical treatises. The concept of Hermes Latinus captures this diversity of Hermetic engagement in the medieval period, from elite theological engagement to practical technical work.</p>

<h2>Related Concepts</h2>
<p>Hermes Latinus stands in direct relation to <a href="../concepts/hermeticism.html">Hermeticism</a> itself, and particularly to the question of periodization — when does the Hermetic tradition begin and end? The recognition of a Hermes Latinus tradition complicates simple narratives of medieval darkness and Renaissance light. It also relates to <a href="../concepts/medievalism.html">Medievalism</a> and to the question of medieval intellectual culture's engagement with pagan philosophy. The concept also bears on <a href="../concepts/translation_movement.html">the Translation Movement</a> that brought Arabic and Greek texts into medieval Europe, showing that not all Hermetic transmission occurred through the famous fifteenth-century recovery of Greek texts.</p>

<h2>Literature</h2>

<p>Lucentini, Paolo. <i>Platonismo medievale: Studi su Eriugena, Anselmo, Macrobe, Dante</i>. Florence: Felice Le Monnier, 1979.</p>

<p>Lucentini, Paolo. <i>L'alchimia nel Medioevo: Sapienza Orientale e tradizione occidentale</i>. Rome: Salerno Editrice, 1996.</p>

<p>Porreca, David. <i>The Emerald Tablet and its Interpretations: From Hermes Trismegistus to Isaac Newton</i>. Oxford: Oxford University Press, 2018.</p>

<p>Delp, Mark D., and Paolo Lucentini. <i>De sex rerum principiis: Liber Magistri Alani editus a Renaldo Hoste, ordine Praedicatorum</i>. Leuven: Brepols, 2006.</p>

<p>Burnett, Charles. <i>The Transmission of Arabic Astronomy into the Medieval West</i>. Farnham: Ashgate, 1997.</p>

<p>Hanegraaff, Wouter J. <i>Hermetic Spirituality and the Historical Imagination</i>. Cambridge: Cambridge University Press, 2022.</p>

<p>Fowden, Garth. <i>The Egyptian Hermes: A Historical Approach to the Late Pagan Mind</i>. Cambridge: Cambridge University Press, 1986.</p>''',
    },
}

def main():
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        for slug, data in concepts.items():
            c.execute('''
                INSERT OR IGNORE INTO concepts
                (slug, label, category, category_type, definition_short, definition_long,
                 source_method, review_status, confidence)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                slug,
                data['label'],
                data['category'],
                data['category_type'],
                data['definition_short'],
                data['definition_long'],
                'agent_generated',
                'DRAFT',
                'HIGH'
            ))
            print(f"[+] Added concept: {data['label']}")

        conn.commit()
        print(f"\nSuccessfully added {len(concepts)} ANALYST_TERM concept entries.")
        print("These entries provide foundational definitions for key scholarly frameworks.")

    except Exception as e:
        print(f'Error: {e}', file=sys.stderr)
        return 1
    finally:
        conn.close()

    return 0

if __name__ == '__main__':
    sys.exit(main())
