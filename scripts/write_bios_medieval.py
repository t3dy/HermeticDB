"""
write_bios_medieval.py
Idempotent script: writes encyclopedia-length bio_html for six medieval figures.
Safe to re-run. Uses UPDATE so existing rows are overwritten with the full biography.
"""

import sqlite3

DB_PATH = r"c:\Dev\EmeraldTablet\db\emerald_tablet.db"

# ---------------------------------------------------------------------------
# BIOGRAPHIES
# ---------------------------------------------------------------------------

bio_thomas_aquinas = """\
<p>Thomas Aquinas (1225–1274), known to posterity as the <i>Doctor Angelicus</i>, was an Italian Dominican
friar and the supreme systematizer of medieval Latin theology. Born at the castle of Roccasecca in the
Kingdom of Sicily, he studied at the Benedictine abbey of Monte Cassino and then at the University of
Naples before joining the Order of Preachers in 1244. His mature intellectual career unfolded at Paris
and Cologne under the direction of <a href="../persons/albertus_magnus.html">Albertus Magnus</a>, the
encyclopedist who first introduced him to the full breadth of Aristotelian natural philosophy and its
Arabic elaborations. Aquinas went on to teach in Paris, Orvieto, Rome, Viterbo, and Naples, producing
in the space of roughly two decades a body of work — commentaries on Aristotle, disputed questions,
scriptural expositions, and above all the <i>Summa Theologiae</i> and <i>Summa contra Gentiles</i> —
that defined the intellectual horizon of European Christendom for the next three centuries and beyond.
He died at Fossanova in March 1274 on his way to the Second Council of Lyon, was canonized in 1323, and
was declared a Doctor of the Church in 1567. Within the history of Western esotericism, Aquinas occupies
a paradoxical position: he never wrote a line of Hermeticism and explicitly subordinated natural magic
to the limits of orthodox theology, yet the conceptual architecture of scholastic Aristotelianism that
he bequeathed to later centuries was precisely the framework within which Renaissance Hermetists such as
<a href="../persons/marsilio_ficino.html">Marsilio Ficino</a> and
<a href="../persons/giovanni_pico_della_mirandola.html">Giovanni Pico della Mirandola</a> were compelled
to operate, and it was the Inquisition — institutionally rooted in the Dominican order that Aquinas
embodied — that ultimately defined the outer limits of what Hermetic speculation could safely claim.</p>

<h2>Works and Intellectual Context</h2>

<p>Aquinas's principal works are the <i>Summa contra Gentiles</i> (c. 1259–1265), a systematic defence of
Christian doctrine against Jewish, Islamic, and pagan objections; the monumental <i>Summa Theologiae</i>
(c. 1265–1274), left unfinished at his death; extensive commentaries on Aristotle's <i>Physics</i>,
<i>Metaphysics</i>, <i>De anima</i>, <i>Nicomachean Ethics</i>, <i>Politics</i>, and <i>De caelo</i>;
commentaries on Scripture and on the <i>Sentences</i> of Peter Lombard; and a large body of disputed
questions on truth, power, evil, and the soul. The animating ambition of this corpus was the synthesis
of revealed theology with rational philosophy as transmitted through the Arabic tradition: above all
through Averroes (Ibn Rushd), whose commentaries on Aristotle had reached the Latin West in the early
thirteenth century, and through Avicenna (Ibn Sina), whose <i>Kitāb al-Shifā'</i> shaped scholastic
pneumatology and cosmology in ways that bear directly on later Hermetic thought. Aquinas accepted the
Aristotelian framework of matter and form, act and potency, the four causes, and the hierarchical
cosmos of celestial intelligences moving the planetary spheres. He diverged from Averroes on the unity
of the intellect, insisting that the individual soul possesses its own intellectual faculty, a position
with significant consequences for the Renaissance theorization of the soul's capacity for
<a href="../concepts/theurgy.html">theurgical</a> self-elevation that Ficino would later develop.</p>

<p>The intellectual context in which Aquinas worked was shaped by the condemnations of 1210 and 1277:
the successive ecclesiastical prohibitions on the teaching of Aristotelian natural philosophy at Paris
that bookended his career. The condemnation of 1277, issued three years after his death by Bishop
Étienne Tempier, targeted 219 propositions drawn from radical Aristotelianism — some of which were
arguably Thomistic in character — and constituted a direct institutional rebuke to the project of
rational synthesis that Aquinas had pursued. This tension between rational inquiry and revealed
authority, which scholasticism never fully resolved, was precisely the fault-line that Renaissance
Hermetism would attempt to navigate by positing a <i>prisca theologia</i> — an ancient wisdom older
than Aristotle and compatible with Christian revelation — in which the Hermetic texts played a
foundational role. Aquinas had himself acknowledged the existence of ancient theological wisdom in
writers before Plato, but he would have had no sympathy for the elevation of the Hermetic Hermes
Trismegistus to prophetic status that Ficino attempted.</p>

<h2>Hermetic Significance</h2>

<p>The relationship between Aquinas and the Hermetic tradition is one of structural constraint rather
than direct engagement. Aquinas knew the <i>Asclepius</i> in the Latin translation attributed to
Apuleius, and he cited it in his commentary on the <i>Sentences</i> and in the <i>Summa contra
Gentiles</i> — though not approvingly. His references to Hermes Trismegistus treat the figure as a
representative of ancient pagan theology, comparable to Plato and Aristotle, and worthy of notice
precisely because ancient pagans had sometimes arrived at truths consonant with Christian teaching
by the light of natural reason. This was the standard scholastic hermeneutic for the accommodation
of pagan wisdom, and Aquinas applied it with characteristic caution.</p>

<p>Far more consequential for the history of Hermetism were Aquinas's positions on natural magic and
astral influence. In the <i>Summa Theologiae</i> and in the treatise <i>De occultis operibus naturae</i>
(On the Hidden Works of Nature, authenticity sometimes debated), Aquinas articulated a distinction
that shaped all subsequent Renaissance discussion of occult philosophy. Natural causes, including the
influence of the celestial bodies on terrestrial matter, were entirely legitimate objects of inquiry
and natural effects produced through such influences were not magical in any illicit sense. The
celestial spheres, moved by immaterial intelligences, diffused their influences downward through the
sublunar world and could be harnessed by those with sufficient knowledge of natural philosophy. This
position opened a carefully bounded space for what the Renaissance would call <i>magia naturalis</i>:
natural magic understood as the manipulation of hidden sympathies and antipathies within the created
order. Ficino's entire project of astral medicine — the use of music, images, and talismans to draw
down planetary influences — was constructed within this Thomistic framework, even as it drew on Hermetic
and Neoplatonic sources that Aquinas would have regarded with considerably more suspicion.</p>

<p>At the same time, Aquinas drew a sharp line between natural magic and demonic invocation. Any
operation that purported to exceed natural causation — that claimed to compel spiritual beings or to
produce effects impossible through the known or hidden powers of nature — was, for Aquinas, either
fraudulent or diabolical. This boundary proved extraordinarily durable. When Dominican inquisitors
in the fifteenth and sixteenth centuries prosecuted practitioners of natural magic, including
alchemists and astrologers, they typically argued that the claimed effects exceeded natural causation
and therefore necessarily involved demonic assistance. The Thomistic framework thus simultaneously
legitimated a restricted zone of natural philosophy and provided the doctrinal basis for prosecution
whenever that zone was transgressed. The condemnation of
<a href="../persons/giordano_bruno.html">Giordano Bruno</a> in 1600 — burned by the Roman Inquisition
on charges that included his Hermetic philosophy of an infinite, animated universe — is the most
dramatic instance of this dynamic.</p>

<h2>Transmission and Reception</h2>

<p>The reception of Aquinas within the subsequent history of the Hermetic tradition is largely a history
of negotiation. Ficino, who was himself deeply formed by scholastic training, never rejected Aquinas
but rather attempted to show that Neoplatonic and Hermetic wisdom was compatible with the scholastic
synthesis. His <i>Theologia Platonica</i> (1482) is structured as a response to the Thomistic
objections to Platonism, and the entire argument turns on the claim that the ancient theologians —
Hermes, Orpheus, Pythagoras, Plato — had reached through inspired reason the same truths that
Aquinas derived through the combination of revelation and Aristotelian logic. Pico della Mirandola
pushed further: in the <i>Oration on the Dignity of Man</i> and the <i>Heptaplus</i>, he attempted
a genuine synthesis of Hermetism, Kabbalah, and scholastic philosophy, arguing that all revealed
the same hierarchical structure of reality. For Pico, Aquinas was a scholastic authority to be
incorporated into a broader concordia, not a critic to be refuted.</p>

<p>By the late sixteenth century, however, the terms of engagement had shifted. The Council of Trent
(1545–1563) and the subsequent Catholic Reformation had hardened the institutional authority of
Thomism — the Society of Jesus adopted the <i>Summa Theologiae</i> as its primary theological
textbook through the Ratio Studiorum of 1599 — at precisely the moment when Hermetic speculation
was coming under increasing inquisitorial scrutiny. The effect was to intensify the policing of the
boundary between licit natural philosophy and illicit occult practice. Protestant reformers, who
rejected Thomism on different grounds, were equally hostile to the Hermetic synthesis: Calvinist
polemicists attacked both the scholastic tradition and its Hermetic interlocutors as representatives
of the same rationalist presumption. The institutional force of Thomism thus shaped the reception
of the Hermetic tradition negatively — as the framework against which Hermetic thinkers defined
themselves and to whose standards they were held accountable — as much as it shaped it positively
through the conceptual vocabulary of natural causation and celestial influence.</p>

<h2>Scholarly Debates</h2>

<p>Within the historiography of Western esotericism, the figure of Aquinas has received renewed
attention through the work of Wouter J. Hanegraaff on the relationship between scholasticism and
esotericism as competing modes of intellectual legitimacy. Hanegraaff's framework, developed in
<i>Esotericism and the Academy</i> (2012), proposes that Western esotericism emerged historically
as the "rejected knowledge" of the academy — precisely those currents of thought that the
scholastic-rationalist consensus excluded from legitimate discourse. On this reading, the
Thomistic synthesis was not merely a context for Hermetism but was actively constitutive of it:
the concept of "esotericism" as a distinct domain only becomes meaningful against the background
of a dominant academic orthodoxy from which it is excluded. Aquinas is thus, indirectly, a
founding figure of Western esotericism in the sense that the scholastic consensus he helped
create defined the boundary that later Hermetic thinkers were perceived to transgress.</p>

<p>A second scholarly debate concerns the extent to which Aquinas's positions on natural magic
genuinely opened conceptual space for later occult philosophy or whether they were always
primarily restrictive in intent. Scholars such as Edward Grant and David Lindberg have argued
that scholastic natural philosophy was more hospitable to occult causation than is sometimes
supposed, and that the Thomistic distinction between natural and demonic magic was a genuine
intellectual resource for Renaissance naturalists. Against this, Brian Copenhaver and others
have emphasized the ways in which the same distinction functioned ideologically to
criminalize philosophical positions that exceeded the permitted boundary. The tension between
these readings reflects a broader debate about the relationship between scholasticism and the
Renaissance occult sciences that remains unresolved in the secondary literature.</p>

<h2>Literature</h2>

<p>Torrell, Jean-Pierre. <i>Saint Thomas Aquinas</i>. 2 vols. Washington, D.C.: Catholic University
of America Press, 1996–2003.</p>
<p>Wippel, John F. <i>The Metaphysical Thought of Thomas Aquinas: From Finite Being to Uncreated
Being</i>. Washington, D.C.: Catholic University of America Press, 2000.</p>
<p>Hanegraaff, Wouter J. <i>Esotericism and the Academy: Rejected Knowledge in Western Culture</i>.
Cambridge: Cambridge University Press, 2012.</p>
<p>Weisheipl, James A. <i>Friar Thomas D'Aquino: His Life, Thought, and Works</i>. Washington, D.C.:
Catholic University of America Press, 1983.</p>
<p>Copenhaver, Brian P. "Natural Magic, Hermetism, and Occultism in Early Modern Science." In
<i>Reappraisals of the Scientific Revolution</i>, edited by David C. Lindberg and Robert S.
Westman. Cambridge: Cambridge University Press, 1990.</p>
<p>Lindberg, David C. <i>The Beginnings of Western Science</i>. Chicago: University of Chicago
Press, 1992.</p>
"""

bio_al_razi = """\
<p>Muhammad ibn Zakariyya al-Razi (c. 854–925 CE), known in the Latin West as Rhazes, was a Persian
physician, alchemist, and natural philosopher from Rayy, a city near modern Tehran in the Jibal
province of the Abbasid caliphate. He stands among the most prolific and original scientific minds
of the medieval Islamic world, having composed, by the reckoning of the tenth-century bibliographer
Ibn al-Nadim, more than two hundred works spanning medicine, philosophy, alchemy, mathematics, and
theology. In the history of alchemy, al-Razi occupies a singular position: he was the first author
to produce a systematic, empirically grounded account of laboratory practice, classifying the
substances, instruments, and operations of the alchemical art with a rigor and precision that had
no precedent in either the Greek or the early Arabic tradition. His principal alchemical works, the
<i>Kitāb al-Asrār</i> (Book of Secrets) and the <i>Kitāb Sirr al-Asrār</i> (Book of the Secret
of Secrets), reached the Latin West through the translations of Gerard of Cremona and others in
the twelfth and thirteenth centuries, where they circulated under the titles <i>Liber secretorum</i>
and <i>De secretis secretorum</i> and exercised a formative influence on European alchemy from
Roger Bacon onward. Within the broader arc of the Hermetic tradition, al-Razi is a figure of
productive tension: his rationalist, demystified approach to alchemical practice stands in marked
contrast to the theurgical and cosmological strands of alchemy associated with the
<a href="../persons/jabir_ibn_hayyan.html">Jabir ibn Hayyan</a> corpus, yet the practical
chemistry he systematized was the indispensable empirical substrate on which all subsequent
philosophical elaborations of the alchemical tradition depended.</p>

<h2>Works and Intellectual Context</h2>

<p>Al-Razi received his early education in Rayy and is reported to have studied music and philosophy
before turning to medicine, which he began to study seriously only in his thirties after travelling
to Baghdad. He served as director of the hospital at Rayy and later at the Muqtadiri hospital in
Baghdad, and his clinical experience is reflected in the extraordinary observational precision of
his medical writings. His most celebrated medical work, the encyclopedic <i>al-Hāwī fī al-Tibb</i>
(The Comprehensive Book of Medicine), known in Latin as <i>Continens</i>, ran to twenty-three
volumes in modern Arabic edition and was one of the primary medical reference works in both the
Islamic world and medieval Europe. His <i>Kitāb al-Mansūrī</i>, a shorter systematic treatise
dedicated to the Samanid governor Mansur ibn Ishaq, was translated by Gerard of Cremona as
<i>Liber Almansoris</i> and formed part of the standard medical curriculum at European universities.
His monograph on smallpox and measles, <i>Kitāb al-Jadari wa-al-Hasbah</i>, is the earliest
extant clinical description of these diseases and has been admired by historians of medicine as
a masterpiece of differential diagnosis.</p>

<p>In alchemy, al-Razi's two principal works represent different levels of disclosure. The <i>Kitāb
al-Asrār</i>, the more accessible of the two, provides a systematic classification of alchemical
materials into mineral, vegetable, and animal substances — a tripartite taxonomy that anticipates
the later Paracelsian framework — and a description of the instruments and operations of the
laboratory: calcination, sublimation, distillation, crystallization, filtration, and amalgamation.
The mineral substances are further subdivided into spirits (sulphur, arsenic, mercury, sal ammoniac,
and camphor), bodies (gold, silver, copper, iron, lead, and tin), stones, vitriols, boraces, and
salts — a classification that constitutes the first systematic chemical taxonomy in the Arabic
tradition and one of the first in world science. The <i>Kitāb Sirr al-Asrār</i>, more esoteric in
character, deals with the theoretical foundations of transmutation and with the preparation of the
elixir. Al-Razi accepted the theoretical possibility of transmutation — the conversion of base
metals into gold or silver through the action of the elixir — on the basis of the Aristotelian
theory that all metals share a common matter differentiated only by their specific form, so that
a sufficiently potent agent could in principle alter the form while preserving the matter.</p>

<p>The intellectual context in which al-Razi developed his alchemical thought was shaped by the
corpus of Arabic Hermetic and pseudo-Jabirian alchemy that had accumulated during the eighth and
ninth centuries. The works attributed to
<a href="../persons/jabir_ibn_hayyan.html">Jabir ibn Hayyan</a> — whether or not they represent the
output of a single historical author — had established a cosmological and numerological framework
for alchemy in which the transformation of metals was linked to the structure of the universe and
to the perfection of the practitioner's soul. Al-Razi's approach was notably different in
emphasis: while he did not deny the cosmological framework, his primary interest was practical
and empirical. He wanted to know what substances existed, how they behaved under heat and
pressure, and what laboratory operations could transform them. This empirical orientation has led
historians of science to regard al-Razi as a precursor of modern chemistry in a more direct sense
than his Jabirian predecessors, though the attribution of modernity to medieval figures is a
historiographical position that must be treated with caution.</p>

<h2>Hermetic Significance</h2>

<p>Al-Razi's relationship to the Hermetic tradition as defined in this portal — the tradition of
texts attributed to Hermes Trismegistus and the philosophical system of
<a href="../concepts/hermeticism.html">Hermeticism</a> more broadly — is indirect but substantial.
He did not write commentaries on the Hermetic philosophical treatises, and his alchemy is not
organized around the concept of <i>gnosis</i> or the ascent of the soul through the planetary
spheres that characterizes the theurgical dimension of late antique Hermetism. What connects
al-Razi to the Hermetic tradition is rather the continuity of the practical alchemical corpus
that descended from the Greek alchemists — Zosimos of Panopolis, Stephanos of Alexandria,
the pseudo-Democritus — through the Arabic synthesis and into the Latin medieval world. This
practical corpus had always existed in a complex relationship with the philosophical Hermetica:
the <i>Tabula Smaragdina</i>, or Emerald Tablet, was the symbolic condensation of a cosmological
doctrine in which the alchemical operation was understood as the microcosmic enactment of cosmic
creation, and this doctrine colored even the most practically oriented alchemical writing. Al-Razi's
<i>Kitāb al-Asrār</i> and <i>Kitāb Sirr al-Asrār</i> inherit this context even where they
deliberately strip it of its mystical elaborations.</p>

<p>Al-Razi's broader philosophical writings, particularly the <i>Kitāb al-'Ilm al-Ilāhī</i> (Book
of Divine Science) and his ethical work <i>al-Sīra al-Falsafiyya</i> (The Philosophical Way of
Life), reveal a thinker deeply engaged with the Neoplatonic inheritance of the Islamic world and
with the question of how the rational soul should govern its relation to the body and to matter.
His philosophical theology was notably heterodox by the standards of Sunni orthodoxy: he rejected
prophecy as a source of knowledge superior to reason, held that the material world was created
through the mixing of the eternal atoms with the soul and time and space in a manner influenced
by Epicurean and Neoplatonic categories, and argued for the independence of philosophical reason
from revealed religion. These positions brought him into conflict with Islamic theologians in his
own time and have made him a contested figure in the subsequent historiography.</p>

<h2>Transmission and Reception</h2>

<p>The Latin transmission of al-Razi's alchemical works began in the twelfth century through the
translation enterprise centered at Toledo, where Gerard of Cremona (c. 1114–1187) rendered a
large number of Arabic scientific texts into Latin, including al-Razi's <i>Kitāb al-Asrār</i>
as <i>Liber secretorum de Alchimia</i> and the <i>Kitāb al-Mansūrī</i> as <i>Liber Almansoris</i>.
These translations entered the standard curriculum of European universities and monastic libraries,
and al-Razi's chemical taxonomy — the classification of substances into spirits, bodies, stones,
vitriols, boraces, and salts — became the organizing framework for Latin European alchemy from the
thirteenth century onward. Roger Bacon, who was one of the most systematic early Latin synthesizers
of the Arabic alchemical inheritance, drew on al-Razi's practical chemistry in his discussions of
the possibilities of natural transformation. Albertus Magnus, whose <i>De mineralibus</i> is the
most comprehensive medieval Latin treatise on minerals and metals, engaged critically with Arabic
alchemical authorities including al-Razi and helped transmit the substance of his chemical
classifications to the Latin scholastic tradition.</p>

<p>In Renaissance alchemy, al-Razi's influence became partly absorbed into the more speculative
currents represented by Paracelsus and his followers. The Paracelsian tria prima — sulphur,
mercury, and salt as the three principles of all material substances — has sometimes been read
as a transformation of the Arabic tradition of chemical classification in which al-Razi's work
played a formative part, though the precise lines of transmission are complex and disputed.
By the seventeenth century, as the new mechanical philosophy began to displace the Aristotelian
framework within which both Arabic and Latin alchemy had operated, al-Razi's empirical orientation
made him a figure of retrospective admiration for early modern chemists seeking historical
precedents for an experimental approach to natural philosophy. Robert Boyle, in the <i>Sceptical
Chymist</i> (1661), implicitly positioned his own experimental chemistry against the kind of
theoretical framework that al-Razi had worked within, while acknowledging the empirical substance
of the Arabic alchemical tradition.</p>

<h2>Scholarly Debates</h2>

<p>The modern historiography of al-Razi is divided between historians of medicine, historians of
chemistry, and historians of Islamic philosophy, with relatively little cross-fertilization between
these communities. Historians of medicine, drawing on the work of scholars such as Manfred Ullmann
and Lawrence Conrad, have emphasized the clinical originality of al-Razi's medical writings and
his independence from the Galenic canon. Historians of chemistry, following the pioneering work of
Shlomo Pines and the more recent scholarship of Lawrence Principe, have assessed his alchemical
writings in terms of the development of chemical knowledge and laboratory technique. Historians
of Islamic philosophy, following Pines's work on al-Razi's philosophical thought, have concentrated
on his heterodox theological positions and his critique of prophecy.</p>

<p>Within the specific field of Hermetic studies, al-Razi has received relatively little sustained
attention. The tendency of scholarship in this area to concentrate on the philosophical and
cosmological dimensions of the Hermetic tradition — on the <i>Corpus Hermeticum</i>, the
<i>Asclepius</i>, and their Renaissance reception — has resulted in a relative neglect of the
practical alchemical corpus through which Hermetic ideas were most widely disseminated in the
medieval period. Kevin van Bladel's <i>The Arabic Hermes</i> (2009) and Liana Saif's work on
Arabic occult sciences represent recent efforts to remedy this imbalance, and both suggest that
a fuller integration of al-Razi's practical chemistry into the history of the Hermetic tradition
remains a desideratum of current scholarship.</p>

<h2>Literature</h2>

<p>Ullmann, Manfred. <i>Die Medizin im Islam</i>. Leiden: Brill, 1970.</p>
<p>Pines, Shlomo. <i>Beiträge zur islamischen Atomenlehre</i>. Berlin: Heine, 1936.</p>
<p>Principe, Lawrence M. <i>The Secrets of Alchemy</i>. Chicago: University of Chicago Press, 2013.</p>
<p>van Bladel, Kevin. <i>The Arabic Hermes: From Pagan Sage to Prophet of Science</i>. Oxford:
Oxford University Press, 2009.</p>
<p>Saif, Liana. <i>The Arabic Influences on Early Modern Occult Philosophy</i>. Basingstoke:
Palgrave Macmillan, 2015.</p>
<p>Pormann, Peter E., and Emilie Savage-Smith. <i>Medieval Islamic Medicine</i>. Washington, D.C.:
Georgetown University Press, 2007.</p>
"""

bio_ibn_umayl = """\
<p>Muhammad ibn Umayl al-Tamīmī (fl. c. 900–960 CE), known in the Latin West as Senior Zadith or
Senior Philosophus, was an Egyptian alchemist of the tenth century whose surviving works constitute
some of the most philosophically rich and literarily accomplished texts in the entire Arabic
alchemical tradition. Almost nothing is known of his life with certainty: the <i>nisba</i>
al-Tamīmī suggests tribal affiliation with the Arab tribe of Tamim, and the epithet "Egyptian"
in later sources indicates that he spent significant time in Egypt, where he is reported to have
studied the Hermetic monuments of the ancient civilization — the temples, inscriptions, and
statues — with an interpretive attention that shaped his understanding of the alchemical art.
His principal surviving work, <i>al-Mā' al-Waraqī wa al-Arḍ al-Najmiyya</i> (The Silvery Water
and the Starry Earth), is a prose poem of remarkable complexity that weaves together practical
alchemical instruction, allegorical interpretation of Egyptian monuments, and philosophical
reflection on the nature of the prima materia. It was translated into Latin as <i>Tabula Chemica</i>
(The Chemical Table) and, together with a related prose commentary, the <i>Risālat al-Shams ilā
al-Hilāl</i> (Epistle of the Sun to the Crescent Moon), circulated widely in medieval and
Renaissance Europe. In the twentieth century, the <i>Tabula Chemica</i> attracted the sustained
attention of Carl Gustav Jung, who devoted two extended studies — <i>Psychology and Alchemy</i>
(1944) and <i>Mysterium Coniunctionis</i> (1955–1956) — to the psychological interpretation of
its imagery, making Ibn Umayl one of the most discussed Arabic alchemists in the modern
<a href="../concepts/hermeticism.html">Hermetic</a> revival.</p>

<h2>Works and Intellectual Context</h2>

<p>Ibn Umayl's corpus as reconstructed by modern scholarship comprises three principal texts: the
<i>al-Mā' al-Waraqī wa al-Arḍ al-Najmiyya</i>, its prose commentary <i>Hall al-Rumūz</i>
(Explanation of the Symbols), and the <i>Risālat al-Shams ilā al-Hilāl</i>. A fourth text,
<i>Kitāb al-Mā'</i> (Book of Water), is preserved in fragmentary form. These works were edited
from the surviving Arabic manuscripts by M. Turab 'Ali and published in a critical edition by
the Institute for the History of Arabic-Islamic Science (Frankfurt, 2003), with a parallel
Latin text of the <i>Tabula Chemica</i> and the <i>Epistola Solis ad Lunam Crescentem</i>.
The <i>al-Mā' al-Waraqī</i> takes the form of a vision narrative: the author, describing his
journey through Egypt, visits ancient monuments — temples, tombs, and inscriptions — and
encounters there the allegorical images of the alchemical art. He sees a statue of a sage holding
a tablet on which the secrets of the art are inscribed in coded form, and the remainder of the
work is devoted to the decipherment of these secrets. The framing device is significant: it places
the origin of alchemical knowledge in the Egyptian priestly tradition and associates the art with
the interpretation of ancient hieroglyphic inscriptions — an association that reflects the genuine
historical connection between Egyptian temple practice and the earliest Greek alchemical texts.</p>

<p>Ibn Umayl drew extensively on earlier alchemical authorities, both Greek and Arabic. He quotes
and comments on Zosimos of Panopolis, the third-century Greek alchemist whose visionary texts
are among the oldest surviving alchemical documents; on Maria the Prophetess (Mary the Jewess),
the legendary alchemist credited with the invention of the <i>bain-marie</i> and other laboratory
devices; on the pseudo-Democritus, the Greek author of the foundational alchemical text
<i>Physika kai Mystika</i>; and on Arabic predecessors including the works attributed to
<a href="../persons/jabir_ibn_hayyan.html">Jabir ibn Hayyan</a>. His engagement with these sources
is not merely compilatory: he interprets their enigmatic formulations through a consistent
philosophical framework that understands alchemy as the art of understanding and reproducing the
natural processes of generation and corruption through which the prima materia differentiates itself
into the specific forms of the metals. The alchemical work, on this view, is not a violation of
nature but its concentrated imitation — an art that accelerates and perfects what nature achieves
slowly and imperfectly in the depths of the earth.</p>

<p>The philosophical framework within which Ibn Umayl operates is broadly Neoplatonic and Hermetic.
The unity of the prima materia — the single underlying substance from which all metals are
differentiated — is understood as a reflection of the metaphysical unity of the One. The
alchemical work, the purification of the impure metal through fire and the fixation of the
volatile principle, is an image of the soul's purification and ascent. The key term in Ibn
Umayl's vocabulary is <i>al-mā' al-waraqī</i>, the silvery water or leafy water, which
designates the universal solvent and generative principle of the alchemical art — the mercury
of the philosophers, not common quicksilver but a philosophical substance whose precise nature
is precisely what the work is devoted to revealing. The "starry earth" of the title designates
the fixed material principle in which the silvery water is concealed, the prima materia in its
terrestrial, undifferentiated state.</p>

<h2>Hermetic Significance</h2>

<p>Ibn Umayl's significance within the Hermetic tradition is threefold. First, his work represents
the most sustained and sophisticated engagement with the Egyptian heritage of alchemy in the
medieval Arabic tradition. His vision narrative, centered on the interpretation of Egyptian temple
inscriptions and monuments, links the alchemical art directly to the priestly wisdom tradition of
ancient Egypt that the late antique Hermetic texts had claimed as their origin. This link was not
merely rhetorical: recent scholarship by Christian Bull and Garth Fowden has shown that the
earliest Greek alchemical texts were produced in the same milieu as the philosophical Hermetica —
the Egyptian priestly circles of the first through third centuries CE — and that the alchemical
tradition and the cosmological Hermetica shared common roots in Egyptian temple theology. Ibn
Umayl's text preserves and elaborates this connection in ways that illuminate the original unity
of the two traditions.</p>

<p>Second, Ibn Umayl's allegorical method of reading ancient monuments and inscriptions anticipates
the Renaissance practice of Hermetic interpretation of Egyptian hieroglyphics that would be
developed, on very different philological assumptions, by scholars such as
<a href="../persons/athanasius_kircher.html">Athanasius Kircher</a> in the seventeenth century.
The idea that ancient Egyptian monuments encoded alchemical or philosophical secrets accessible
to the initiated reader was a persistent theme of the Hermetic tradition from late antiquity
through the early modern period, and Ibn Umayl's work is one of the most developed medieval
expressions of this interpretive practice.</p>

<p>Third, Ibn Umayl's <i>Tabula Chemica</i> was one of the primary vehicles through which the
philosophical and cosmological dimensions of the Arabic alchemical tradition reached the Latin
West. Alongside the works attributed to Jabir — transmitted as the Geber corpus — and the
<a href="../concepts/emerald_tablet.html">Emerald Tablet</a>, the <i>Tabula Chemica</i>
constituted one of the foundational texts of medieval Latin alchemy and shaped the terms in
which Renaissance alchemists conceptualized the philosophical dimensions of their art. The
imagery of the <i>Tabula Chemica</i> — the royal couple, the king and queen representing sulphur
and mercury, the process of dissolution and coagulation, the return of the perfected stone —
became among the most frequently cited and illustrated motifs of Renaissance alchemical iconography.</p>

<h2>Transmission and Reception</h2>

<p>The Latin translation of the <i>al-Mā' al-Waraqī</i> as <i>Tabula Chemica</i> was produced no
later than the thirteenth century, though the precise identity of the translator is unknown.
The Latin text circulated in numerous manuscript copies and was printed in the major sixteenth-
and seventeenth-century alchemical anthologies, including the <i>Theatrum Chemicum</i> of Zetzner
(Strasbourg, 1659–1661) and the <i>Bibliotheca Chemica Curiosa</i> of Manget (Geneva, 1702).
Under the name "Senior" or "Senior Zadith," Ibn Umayl was regularly cited by medieval and
Renaissance alchemical authors as one of the principal authorities of the art. The <i>Epistola
Solis ad Lunam Crescentem</i> — the Latin version of the <i>Risālat al-Shams</i> — circulated
independently and was read as a key to the symbolic language of alchemical allegory.</p>

<p>The twentieth-century reception of Ibn Umayl through the mediation of Carl Jung is the most
influential, and in some respects the most problematic, dimension of his modern transmission.
Jung encountered the <i>Tabula Chemica</i> through the collection of alchemical texts assembled
by his student Marie-Louise von Franz, and the imagery of the text — particularly the figure of
the hermaphrodite, the royal pair, and the process of <i>coniunctio</i> — became central to his
elaboration of the theory of the collective unconscious and the individuation process. Jung's
reading, developed in <i>Psychology and Alchemy</i> and above all in the detailed exegesis of
the <i>Tabula Chemica</i> in <i>Mysterium Coniunctionis</i>, treats the alchemical imagery as a
projection of unconscious psychological contents and reads the process of the Great Work as an
allegory of psychological integration. This Jungian reading has been enormously influential in
the popular reception of alchemy and has generated a substantial secondary literature, but it
has also been criticized by historians of alchemy — most forcefully by Lawrence Principe and
William Newman — for subordinating the historical and practical dimensions of alchemical texts
to a predetermined psychological hermeneutic that distorts the meaning of the sources.</p>

<h2>Scholarly Debates</h2>

<p>The principal scholarly debates surrounding Ibn Umayl concern the sources of his thought, the
historicity of his claims about Egyptian monuments, and the appropriate methodology for reading
alchemical allegory. On the question of sources, M. Turab 'Ali's edition demonstrated that Ibn
Umayl's familiarity with Greek alchemical texts was mediated through Arabic translations now
largely lost, and that his readings of Zosimos and Maria the Prophetess were filtered through
an interpretive tradition with its own distinctive concerns. On the historicity of the monument
visits, modern Egyptologists and historians of Arabic alchemy have generally concluded that the
vision narrative is a literary device rather than a report of actual events, though the specific
Egyptian monuments described — including the temple at Memphis — may reflect genuine knowledge
of ancient sites. On the methodology of reading alchemical allegory, the debate between the
psychological interpretation associated with Jung and the historical-chemical interpretation
associated with Principe and Newman remains unresolved and constitutes one of the central
methodological divisions in current scholarship on the alchemical tradition.</p>

<h2>Literature</h2>

<p>Ibn Umayl, Muhammad. <i>Al-Mā' al-Waraqī wa al-Arḍ al-Najmiyya / Tabula Chemica</i>. Edited
by M. Turab 'Ali and H. E. Stapleton. Frankfurt: Institute for the History of Arabic-Islamic
Science, 2003.</p>
<p>Jung, Carl Gustav. <i>Mysterium Coniunctionis: An Inquiry into the Separation and Synthesis of
Psychic Opposites in Alchemy</i>. Translated by R. F. C. Hull. Princeton: Princeton University
Press, 1963.</p>
<p>Principe, Lawrence M., and William R. Newman. "Some Problems with the Historiography of
Alchemy." In <i>Secrets of Nature: Astrology and Alchemy in Early Modern Europe</i>, edited
by William R. Newman and Anthony Grafton. Cambridge, Mass.: MIT Press, 2001.</p>
<p>Fowden, Garth. <i>The Egyptian Hermes: A Historical Approach to the Late Pagan Mind</i>.
Cambridge: Cambridge University Press, 1986.</p>
<p>Bull, Christian H. <i>The Tradition of Hermes Trismegistus: The Egyptian Priestly Figure as a
Teacher of Hellenized Wisdom</i>. Leiden: Brill, 2018.</p>
<p>van Bladel, Kevin. <i>The Arabic Hermes: From Pagan Sage to Prophet of Science</i>. Oxford:
Oxford University Press, 2009.</p>
"""

bio_khalid_ibn_yazid = """\
<p>Khalid ibn Yazid ibn Mu'awiya (c. 668–704 CE), Umayyad prince and grandson of the caliph
Mu'awiya ibn Abi Sufyan, occupies in Islamic alchemical lore the foundational position of the
first Arab patron and practitioner of the alchemical art. According to the traditional accounts
preserved by the tenth-century bibliographer Ibn al-Nadim in the <i>Kitāb al-Fihrist</i> and
elaborated by subsequent Islamic authors, Khalid was twice passed over for the caliphate following
the death of his father Yazid I in 683 CE, and, finding himself excluded from political power,
turned his energies to the pursuit of the esoteric sciences. He is said to have summoned Greek
and Coptic scholars to the court at Damascus and to have commissioned the first Arabic translations
of Greek alchemical texts — an act of patronage that, if historical, would make him the initiator
of the entire enterprise of Arabic alchemy. The master most often named in connection with these
translations is Morienus Romanus (Maryanus in Arabic), a Christian hermit said to have studied
alchemy in Alexandria under a monk named Stephanos and to have transmitted the art to Khalid in
a dialogue that was translated into Latin by Robert of Chester in 1144 as <i>Liber de compositione
alchimiae</i> — the first alchemical text to be translated from Arabic into Latin. Whatever the
historical reality behind these accounts, the figure of Khalid ibn Yazid represents in the Islamic
and subsequently in the European tradition the moment of transmission — the passage of the ancient
Greek Hermetic and alchemical wisdom into the new world of Islamic civilization — and as such he
holds a structurally indispensable place in the genealogy of the
<a href="../concepts/hermeticism.html">Hermetic</a> tradition.</p>

<h2>Works and Intellectual Context</h2>

<p>The alchemical corpus attributed to Khalid ibn Yazid in the medieval Arabic tradition is
substantial but almost certainly pseudo-epigraphical for the most part. Ibn al-Nadim's <i>Fihrist</i>,
compiled around 988 CE, lists several alchemical works under Khalid's name, including a poem
on the art (<i>Qasidat al-Kimiya'</i>) and a collection of aphorisms. Later bibliographers add
further titles. The modern scholarly assessment of this corpus has been carried out most thoroughly
by Fuat Sezgin in <i>Geschichte des arabischen Schrifttums</i> and by Manfred Ullmann in
<i>Die Natur- und Geheimwissenschaften im Islam</i>, both of whom conclude that the works
attributed to Khalid are in all probability later compositions placed under his name to lend them
the authority of the legendary founder of Arabic alchemy. This practice of pseudo-epigraphical
attribution was common throughout the medieval alchemical tradition, in both Arabic and Latin:
texts were attributed to famous names — Hermes Trismegistus, Aristotle, Jabir, Geber — precisely
because the attribution conferred a form of legitimacy that the actual authors, working within a
tradition of arcane transmission, neither could nor wished to claim in their own names.</p>

<p>The intellectual context in which the figure of Khalid ibn Yazid was constructed is the crucial
transition from late antique to early Islamic civilization. The seventh and early eighth centuries
saw the dramatic expansion of the Arabic-speaking Islamic empire across the former territories
of the Byzantine and Sasanian empires, bringing Arab culture into sustained contact with the
sophisticated intellectual traditions of Greek, Syriac, Coptic, and Persian scholarship. The
translation movement that would eventually produce the extraordinary Arabic scientific and
philosophical synthesis of the ninth and tenth centuries — the movement associated with the
Bayt al-Hikma (House of Wisdom) in Baghdad under al-Mansur, al-Rashid, and al-Ma'mun — was
preceded by earlier, more limited translation activities in Syria, Egypt, and Persia. It is within
this earlier phase that the figure of Khalid is placed: an Umayyad prince, still rooted in the
old Arab aristocratic culture of Syria, who nevertheless recognized the intellectual riches of
the Greek philosophical and scientific tradition and sought to make them accessible in Arabic.</p>

<p>Whether or not Khalid actually commissioned translations, the dialogue of Morienus and Khalid —
the <i>Liber de compositione alchimiae</i> in its Latin form — encodes a significant theological
claim about the transmission of alchemical knowledge. In the dialogue, the Christian hermit
Morienus presents alchemy as a sacred science transmitted through a chain of initiation reaching
back to the ancient sages, and he warns Khalid that the art cannot be mastered without the
cultivation of moral virtue and spiritual purification. The frame narrative stages a conversion:
Khalid, the Muslim prince, receives the art from a Christian sage, and the terms of the transfer
implicitly assert the Christian character of the Hermetic alchemical tradition even as it passes
into Islamic hands. This theological framing reflects the actual historical situation of the early
translation movement, in which Christian scholars — Syriac-speaking Nestorians and Jacobites
for the most part — played the primary mediating role between the Greek scientific tradition
and the emerging Islamic intellectual world.</p>

<h2>Hermetic Significance</h2>

<p>Within the Hermetic tradition as a whole, the significance of Khalid ibn Yazid lies less in any
specific intellectual contribution than in his function as the symbolic pivot of transmission.
The genealogy of Hermetic wisdom that was constructed by medieval Islamic and European authors
ran from Hermes Trismegistus himself — identified with the biblical Enoch or with the Egyptian
Thoth — through the Greek philosophers and alchemists, through Morienus and the Alexandrian
scholarly tradition, to Khalid and thence to the full flowering of Arabic alchemy in the works
of <a href="../persons/jabir_ibn_hayyan.html">Jabir ibn Hayyan</a> and his successors. This
genealogy served the same function as the concept of <i>prisca theologia</i> in the Renaissance
Hermetic tradition: it asserted the antiquity, continuity, and divine origin of a body of knowledge
whose authority was grounded precisely in the claim that it had been faithfully transmitted across
the ages from its supernatural source. The figure of Khalid occupied a structurally crucial node
in this chain: he was the Arab who received the Greek inheritance and made possible its
incorporation into the Islamic philosophical synthesis.</p>

<p>The Morienus dialogue, as transmitted in the Latin version of Robert of Chester, carried this
narrative of transmission into the European alchemical tradition, where it enjoyed a wide
circulation and was frequently cited as a foundational text. Robert of Chester's preface to his
translation, composed in 1144, presents the work explicitly as the first Arabic alchemical text
to be made available to Latin readers, and frames the act of translation as a recovery of ancient
wisdom from its Arabic custodians — a mirror image, in the Latin context, of the narrative the
dialogue itself enacts. The Morienus-Khalid dialogue thus participated in the double movement
of transmission that characterizes the history of the Hermetic tradition: the movement from
Greece to the Islamic world that the figure of Khalid embodied, and the movement from the
Islamic world to Latin Europe that the twelfth-century translators initiated.</p>

<p>The <a href="../concepts/emerald_tablet.html">Emerald Tablet</a>, the most celebrated Hermetic
text of the alchemical tradition, is closely connected to the figure of Khalid in the Arabic
tradition: some versions of the tablet's transmission legend attribute its discovery to Khalid
himself, who is said to have found the text inscribed on a tablet in the tomb of Hermes
Trismegistus in Egypt. This attribution, though certainly legendary, reflects the same impulse
that generated the broader corpus of pseudo-Khalidian alchemical texts: the desire to root the
Arabic alchemical tradition in the most ancient possible source and to claim for Khalid the
status of the first Arab to have unlocked the secrets of Hermetic wisdom.</p>

<h2>Transmission and Reception</h2>

<p>The Latin reception of the Khalid tradition centered on the <i>Liber de compositione alchimiae</i>,
Robert of Chester's translation of the Morienus dialogue. This text was included in the major
Latin alchemical anthologies of the sixteenth and seventeenth centuries and was read as a
foundational text of the art by medieval and Renaissance alchemists who encountered the figure
of Khalid as the first of a lineage of Arabic authorities whose works had passed into European
circulation. In the Arabic tradition, Khalid's name continued to be attached to alchemical texts
throughout the medieval period, and his legendary status as the founder of Arabic alchemy was
endorsed by major Islamic bibliographers and scholars including al-Qifti, Ibn Khallikan, and,
with somewhat more skepticism, Ibn Khaldun, who in the <i>Muqaddima</i> questioned the
authenticity of the alchemical works attributed to Khalid while acknowledging the importance
of the tradition that had grown up around his name.</p>

<p>In modern scholarship, the critical assessment of the Khalid corpus began in earnest with the
work of Julius Ruska in the early twentieth century. Ruska's studies of the Arabic alchemical
tradition, including his examination of the Morienus dialogue and the texts attributed to Khalid,
established the pseudo-epigraphical character of most of the attributed corpus and raised
fundamental questions about the origins of Arabic alchemy that subsequent scholars — Ullmann,
Sezgin, van Bladel — have continued to debate. The consensus of modern scholarship holds that
the translation of Greek alchemical texts into Arabic was a gradual process extending over several
generations rather than the act of a single princely patron, and that the figure of Khalid as
founder is a legendary construction that reflects the desire of the Arabic alchemical tradition
to root itself in the most prestigious possible origin.</p>

<h2>Scholarly Debates</h2>

<p>The central scholarly debate about Khalid ibn Yazid concerns the historicity of his role in the
transmission of Greek alchemy into Arabic. Julius Ruska argued in the 1930s that the entire
Khalid tradition was a later construction with no reliable historical basis, and that the works
attributed to him were composed no earlier than the ninth century. Fuat Sezgin, whose encyclopedic
<i>Geschichte des arabischen Schrifttums</i> provides the most comprehensive modern bibliography
of Arabic alchemical texts, took a more nuanced position, acknowledging the pseudo-epigraphical
character of most attributed texts while defending the possibility that a kernel of genuine
historical tradition lay behind the Khalid legend. Kevin van Bladel's <i>The Arabic Hermes</i>
(2009) provides the most recent comprehensive treatment of the early transmission of Hermetic
knowledge into Arabic, and his careful analysis of the available evidence suggests that the
translation of Greek scientific and philosophical texts into Arabic in the Umayyad period was
more limited and more mediated than the Khalid legend implies, though it cannot be ruled out that
some translation activity of the kind attributed to Khalid did occur in Damascus in the late
seventh and early eighth centuries.</p>

<h2>Literature</h2>

<p>Ruska, Julius. <i>Arabische Alchemisten I: Chalid ibn Jazid ibn Mu'awija</i>. Heidelberg:
Carl Winter, 1924.</p>
<p>Sezgin, Fuat. <i>Geschichte des arabischen Schrifttums</i>. Vol. 4. Leiden: Brill, 1971.</p>
<p>Ullmann, Manfred. <i>Die Natur- und Geheimwissenschaften im Islam</i>. Leiden: Brill, 1972.</p>
<p>van Bladel, Kevin. <i>The Arabic Hermes: From Pagan Sage to Prophet of Science</i>. Oxford:
Oxford University Press, 2009.</p>
<p>Robert of Chester. <i>Liber de compositione alchimiae</i>. Edited by Lee Stavenhagen as
<i>A Testament of Alchemy</i>. Hanover, N.H.: University Press of New England, 1974.</p>
<p>Principe, Lawrence M. <i>The Secrets of Alchemy</i>. Chicago: University of Chicago Press, 2013.</p>
"""

bio_bernard_of_trevisan = """\
<p>Bernard of Treviso (1406–1490), known variously as Bernardus Trevisanus, Bernard of Trevisan,
and the Count of the March of Treviso, was an Italian nobleman and alchemist from the Veneto whose
career represents one of the most vividly documented examples of the experimental and philosophical
pursuit of the alchemical art in the late medieval period. Despite the traditional identification
implied by his name, Bernard appears to have been associated with Padua rather than Treviso in his
actual origins, though the precise details of his biography are known primarily through autobiographical
accounts embedded in his own writings, the reliability of which is difficult to assess independently.
By his own account, Bernard began the study of alchemy at the age of fourteen, inspired by the works
of the Arabic masters — above all <a href="../persons/jabir_ibn_hayyan.html">Jabir ibn Hayyan</a>
(Geber) and the texts attributed to <a href="../persons/al_razi.html">al-Razi</a> (Rhazes) — and
devoted the next four decades to an increasingly obsessive and ruinously expensive experimental
search for the philosopher's stone. He describes a succession of failed experiments conducted under
the guidance of successive masters and their preferred methods: the Geberian sulphur-mercury theory,
putrefaction in horse manure, various mineral and organic solvents, distillation sequences of increasing
complexity. Only in his later years, he claims, did he arrive at the correct understanding of the
art — an understanding fundamentally philosophical and contemplative rather than merely experimental
— and commit it to writing in the works that survived him. His principal treatise, <i>La parole
délaissée</i> (The Abandoned Word, c. 1480), together with a related work known in Latin as
<i>Tractatus de chemico miraculo</i> and the <i>Verbum dismissum</i>, circulated in French, Latin,
and eventually in German and English translations and exercised a significant influence on late
medieval and Renaissance alchemical thought. Bernard stands as a pivotal figure between the Arabic-
Latin alchemical inheritance of the medieval period and the more overtly philosophical and spiritual
alchemy of the Renaissance, anticipating in his mature writings the emphasis on the unity of the
<a href="../concepts/prima_materia.html">prima materia</a> and the philosophical nature of the
alchemical mercury that would characterize the work of Paracelsus and his successors.</p>

<h2>Works and Intellectual Context</h2>

<p>Bernard's alchemical writings survive in several versions that reflect both the complexity of
their transmission and the deliberate obscurity that their author cultivated as a condition of
legitimate alchemical communication. The most important is the text known in French as <i>La parole
délaissée</i> and in Latin as <i>Verbum dimissum</i> or <i>Verbum relictum</i>, which takes the
form of an extended autobiographical meditation on the author's alchemical career and the errors
he made before arriving at the correct understanding of the art. The narrative structure is a
sustained penitential exercise: Bernard enumerates his successive failures with the detail of a
man who has spent decades and a fortune on experiments that produced nothing, and uses these failures
as a vehicle for illustrating the philosophical principles that he had been too impatient or too
literal-minded to grasp at the outset. The tone is at once confessional and didactic: Bernard wants
his readers to benefit from his errors and to approach the art with the philosophical patience and
humility that he himself had lacked.</p>

<p>The intellectual framework within which Bernard's mature alchemy operates is Neoplatonic and
Hermetic in a broader sense that encompasses both the philosophical Hermetica and the practical
alchemical tradition. His central thesis is that the stone of the philosophers is made from a single
substance — the philosophical mercury — and that this substance is not common quicksilver but a
more fundamental principle: the first matter of metals in its most purified and active form. The
philosophical mercury is identical with the prima materia, the undifferentiated matter that underlies
all metallic forms, and the work of alchemy consists not in compounding many substances together
but in purifying and exalting this single substance until it achieves the perfection that allows it
to transmute imperfect metals into gold. This doctrine of the unity of the prime matter and the
single substance of the work was not Bernard's invention — it had been formulated in various ways
by Arabic authorities and by Roger Bacon — but his articulation of it, grounded in the testimony
of personal experimental failure, gave it a rhetorical authority that subsequent readers found
compelling.</p>

<p>Bernard's philosophical framework is enriched by a consistent Neoplatonic imagery of descent and
return. The prima materia descends from its source in the unity of the One — or, in the Christian
framework that Bernard also employs, in the creative act of God — into the multiplicity of earthly
forms, and the alchemical work reverses this descent, purifying the dispersed and corrupted matter
back toward its original unity and perfection. This movement of descent and return is the cosmological
pattern that the alchemist imitates in the laboratory, and the philosophical understanding of this
pattern is what distinguishes the true adept from the mere laboratory practitioner who works
blindly with physical substances. Bernard's critique of the practitioners who work without
philosophical understanding — whom he characterizes as burning up fortunes without arriving at
truth — reflects both his personal experience and a broadly Hermetic conviction that the art is
fundamentally intellectual and spiritual before it is practical.</p>

<h2>Hermetic Significance</h2>

<p>Within the history of the Hermetic tradition, Bernard of Treviso's significance lies primarily
in his role as a transmitter and elaborator of the philosophical alchemy that connects the medieval
Arabic-Latin tradition to the Renaissance Hermetic synthesis. His insistence on the unity of the
alchemical substance and the philosophical character of the art anticipates the Paracelsian
reformation of alchemy in the sixteenth century, and several historians of alchemy — particularly
Barbara Obrist in her work on the iconography of medieval alchemy — have identified Bernard as one
of the figures through whom the more spiritualized understanding of the art that would characterize
Renaissance Hermetism passed from the medieval to the early modern period.</p>

<p>Bernard's engagement with the <a href="../concepts/emerald_tablet.html">Emerald Tablet</a> tradition
is implicit throughout his mature writings. The Emerald Tablet's formulation of the principle of
correspondence — "what is above is like what is below, and what is below is like what is above, for
the accomplishment of the miracle of the one thing" — is the cosmological axiom that underlies
Bernard's insistence on the unity of the alchemical substance and its identity with the cosmological
first matter. His works thus participate in the broader tradition of Emerald Tablet commentary
that runs from the Arabic alchemists through the Latin medieval tradition to the Renaissance
Hermetists.</p>

<p>The autobiographical narrative of Bernard's decades-long experimental search has exercised a
particular fascination on later readers, both as an illustration of the psychological dimensions
of the alchemical pursuit and as a rhetorical strategy for the communication of alchemical
doctrine. The figure of the adept who has suffered through long years of failure and expense before
arriving at the truth became a recurring archetype of alchemical autobiography, and Bernard's
<i>Verbum dimissum</i> is one of its most influential formulations. Carl Jung, who was attentive
to the psychological dimensions of alchemical literature, noted the significance of this narrative
pattern as an expression of the individuation process, though historians of alchemy have
generally been skeptical of the psychological reductionism that this interpretation implies.</p>

<h2>Transmission and Reception</h2>

<p>Bernard's works circulated initially in French manuscript and were translated into Latin during
the fifteenth century. The Latin <i>Verbum dimissum</i> was included in the major sixteenth-century
alchemical anthologies: the <i>De alchemia opuscula</i> (Frankfurt, 1550), which was among the
first printed alchemical collections, and subsequently in the <i>Theatrum Chemicum</i> of Lazarus
Zetzner (Strasbourg, 1602–1661), the most comprehensive collection of alchemical texts published
in the early modern period. A German translation, <i>Das verlassene Wort</i>, appeared in the
sixteenth century, and an English translation was included in the <i>Hermetic Museum</i> (Frankfurt,
1678; English translation 1893). This pattern of transmission — French original, Latin translation,
inclusion in the major anthologies, eventual vernacular versions — is typical of the alchemical
texts of this period and ensured that Bernard's work reached the substantial European audience that
the printed alchemical tradition commanded in the sixteenth and seventeenth centuries.</p>

<p>Among the alchemical authors who cited or engaged with Bernard's work, the most significant is
probably Paracelsus (1493–1541), whose reformation of alchemy and medicine drew on the philosophical
tradition that Bernard represented even as it transformed it. The Paracelsian concept of the
<i>arcanum</i> — the active principle of transformation concealed within each substance — bears
a structural resemblance to Bernard's philosophical mercury, and Paracelsus's insistence on the
unity of matter and the spiritual character of the alchemical work continues themes that Bernard
had developed. Whether Paracelsus read Bernard directly or absorbed his ideas through the common
alchemical tradition in which both participated is difficult to determine, but the continuity of
themes is clear.</p>

<h2>Scholarly Debates</h2>

<p>The scholarly debates surrounding Bernard of Treviso concern primarily the authenticity and
dating of the attributed corpus and the interpretation of his philosophical alchemy. On the question
of authenticity, Barbara Obrist's study of medieval alchemical iconography and Joachim Telle's
bibliographical work on German alchemical literature in the Renaissance have helped to clarify
the textual history of the attributed works, though a complete critical edition of Bernard's
writings based on a systematic survey of the manuscript tradition remains a desideratum. On the
interpretation of his philosophy, the debate between historians who read his alchemy as primarily
practical — a failed search for an actual chemical procedure — and those who read it as primarily
philosophical — a meditation on the structure of matter and the soul's relation to it — reflects
the broader methodological division in alchemical studies between the chemical-historical and the
intellectual-historical approaches.</p>

<h2>Literature</h2>

<p>Obrist, Barbara. <i>Les débuts de l'imagerie alchimique (XIVe–XVe siècles)</i>. Paris: Le Sycomore, 1982.</p>
<p>Principe, Lawrence M. <i>The Secrets of Alchemy</i>. Chicago: University of Chicago Press, 2013.</p>
<p>Holmyard, E. J. <i>Alchemy</i>. Harmondsworth: Penguin, 1957.</p>
<p>Waite, Arthur Edward. <i>The Hermetic Museum: Restored and Enlarged</i>. London: James Elliott, 1893.</p>
<p>Telle, Joachim, ed. <i>Analecta Paracelsica: Studien zum Nachleben Theophrast von Hohenheims im
deutschen Kulturgebiet der frühen Neuzeit</i>. Stuttgart: Franz Steiner, 1994.</p>
<p>Figala, Karin. "Die exakte Alchemie von Isaac Newton." <i>Verhandlungen der Naturforschenden
Gesellschaft in Basel</i> 94 (1984): 157–228.</p>
"""

bio_petrus_bonus = """\
<p>Petrus Bonus of Ferrara (fl. c. 1323–1330), Italian physician and alchemical philosopher, is the
author of the <i>Pretiosa margarita novella</i> (The New Pearl of Great Price), the most
philosophically ambitious and theologically sophisticated work of medieval Latin alchemy. Composed
around 1330 in Pola (modern Pula, Croatia), where the author was serving as town physician, and
first printed at Venice in 1546 with a preface by Lacinius, the <i>Pretiosa margarita</i> is a
systematic attempt to demonstrate that alchemy — the transmutation of base metals into gold through
the action of the philosopher's stone — is a genuine natural science and, more remarkably, that
the philosopher's stone is a miraculous substance requiring for its preparation not merely the
knowledge of natural philosophy but also divine grace and prophetic revelation. This claim placed
alchemy in a unique and paradoxical position within the medieval intellectual hierarchy: it was
simultaneously natural — subject to the principles of Aristotelian natural philosophy — and
supernatural, transcending the capacities of unaided reason and requiring divine assistance.
The argument was sufficiently bold that it generated both admiration and controversy in the
centuries following its composition, and the <i>Pretiosa margarita</i> was read closely by
Humanist scholars, Renaissance alchemists, and eventually by Jung's circle of alchemical scholars
in the twentieth century. Within the broader history of
<a href="../concepts/hermeticism.html">Hermeticism</a>, Petrus Bonus represents the high-water mark
of the medieval effort to reconcile the Hermetic alchemical tradition with the intellectual and
theological standards of Latin Christendom, and his work was directly available to the Florentine
Neoplatonists — including <a href="../persons/marsilio_ficino.html">Marsilio Ficino</a> — who
encountered it in manuscript before its eventual printing.</p>

<h2>Works and Intellectual Context</h2>

<p>The <i>Pretiosa margarita novella</i> is a work of extraordinary learning and synthetic ambition.
Petrus Bonus assembles quotations from an enormous range of authorities — Aristotle, Avicenna,
Albertus Magnus,
<a href="../persons/thomas_aquinas.html">Thomas Aquinas</a>, the pseudo-Jabirian Geber, al-Razi, Arnold of
Villanova, and a large number of texts attributed to Hermes Trismegistus — and organizes them into
a sustained argument for the legitimacy and necessity of alchemy. The work is structured in three
main parts: a demonstration that alchemy is a genuine natural science capable of producing real
transmutation; a demonstration that the philosopher's stone, while natural in its substrate, requires
divine grace for its preparation; and a series of allegorical interpretations of classical mythology
and Christian theology that read them as concealed accounts of the alchemical process. This tripartite
structure reflects the author's attempt to situate alchemy simultaneously within the three great
intellectual traditions of his time: Aristotelian natural philosophy, Christian theology, and the
Hermetic and mythological wisdom of antiquity.</p>

<p>The intellectual context in which Petrus Bonus wrote was the late Scholastic tradition of the
early fourteenth century, shaped above all by the reception of Aristotle through the Arabic
commentators and by the theological synthesis of Aquinas. Petrus Bonus was thoroughly trained in
Aristotelian natural philosophy and demonstrates throughout the <i>Pretiosa margarita</i> a detailed
familiarity with the <i>Physics</i>, the <i>Meteorologica</i>, and the pseudo-Aristotelian <i>De
mineralibus</i> — the primary Aristotelian sources for the theory of mineral generation that
underlay medieval alchemy. He was equally familiar with the major Arabic alchemical authorities:
the Geber corpus (the Latin pseudo-Jabirian texts), al-Razi's <i>Liber secretorum</i>, and the
works attributed to Senior (Ibn Umayl). This combination of scholastic and alchemical learning
was not unprecedented — Arnold of Villanova had pursued a similar synthesis in the generation
before Petrus Bonus — but the philosophical ambition and systematic character of the
<i>Pretiosa margarita</i> set it apart from earlier attempts.</p>

<p>The central philosophical argument of the <i>Pretiosa margarita</i> turns on the distinction
between what natural philosophy can explain and what it cannot. Petrus Bonus accepts the
Aristotelian theory of the generation of metals from sulphur and mercury in the earth, and he
accepts that alchemy, as the art of imitating and accelerating this natural process, is in
principle a legitimate natural science. But he argues that the specific form of the philosopher's
stone — the substance that can transmute base metals into gold and silver — is not producible by
natural philosophy alone. The stone's power exceeds what can be achieved by the manipulation of
natural causes, and this excess can only be explained by the intervention of divine grace. The
alchemical adept, on this account, is not merely a natural philosopher but a kind of prophet: a
person to whom God has revealed, through a combination of reason, experiment, and supernatural
illumination, the secret of a substance whose production lies at the boundary of the natural and
the miraculous.</p>

<h2>Hermetic Significance</h2>

<p>The Hermetic significance of Petrus Bonus's work is threefold. First, the <i>Pretiosa margarita</i>
is one of the most important medieval Latin vehicles for the transmission of Hermetic alchemical
texts and concepts. Petrus Bonus quotes extensively from texts attributed to Hermes Trismegistus,
including versions of the
<a href="../concepts/emerald_tablet.html">Emerald Tablet</a> and related Hermetic aphorisms, and he
treats Hermes as one of the principal authorities of the alchemical tradition alongside Aristotle
and the Arabic masters. His extensive engagement with the pseudo-Hermetic corpus helped to maintain
its authority within the Latin alchemical tradition at a moment when scholastic Aristotelianism
might otherwise have displaced it.</p>

<p>Second, the theological argument of the <i>Pretiosa margarita</i> — the claim that the
philosopher's stone requires divine grace — had profound implications for the subsequent
understanding of the relationship between alchemy and religion. By insisting that the art was
not merely natural but also supernatural, Petrus Bonus effectively claimed for alchemy a dignity
comparable to that of theology: it was a domain where human reason and divine revelation
cooperated. This claim was to prove both an inspiration and a provocation to later alchemical
authors. It inspired the tradition of spiritual or philosophical alchemy — most fully developed
in the sixteenth and seventeenth centuries by authors such as Heinrich Khunrath, Michael Maier,
and Jakob Böhme — in which the alchemical work is understood as a figure of spiritual regeneration
and divine illumination. It provoked the skepticism of scholastic and Protestant critics who
found the claim to supernatural assistance in a natural art presumptuous and confused.</p>

<p>Third, the allegorical interpretations of classical mythology and Christian theology that occupy
a substantial part of the <i>Pretiosa margarita</i> contributed to the development of a mode of
Hermetic reading that was enormously influential in the Renaissance. Petrus Bonus reads the myth
of Jason and the Golden Fleece as an account of the alchemical work; he interprets the
Incarnation of Christ as the supreme example of the miracle of transmutation — the transformation
of human nature through the union with the divine; and he reads the creation narrative of Genesis
as a cosmological account of the first matter and the generation of the elements. This allegorical
method — reading ancient myth and sacred scripture as concealed accounts of alchemical truth —
was adopted and elaborated by Renaissance Hermetists such as Ficino, Pico, and above all
<a href="../persons/giovanni_agrippa.html">Heinrich Cornelius Agrippa</a>, who saw in it a
confirmation of the <i>prisca theologia</i> — the ancient universal wisdom that underlay all
genuine religious and philosophical traditions.</p>

<h2>Transmission and Reception</h2>

<p>The manuscript tradition of the <i>Pretiosa margarita novella</i> is substantial, with copies
preserved in libraries across Italy, France, Germany, England, and the Vatican. The work circulated
in the fifteenth century in both Latin and in Italian vernacular excerpts, and was known to scholars
in Ficino's Florentine circle, who encountered it as evidence for the compatibility of Neoplatonic
and Hermetic wisdom with Christian theology. The printed edition of 1546, published by the Venetian
printer Aldus Manutius's successor under the editorship of Janus Lacinius, included a substantial
preface by Lacinius that framed the work as a key to the entire alchemical tradition and ensured
its wide circulation in the age of print. A second edition followed in the compilation <i>De
alchemia</i> (Nuremberg, 1541), and the <i>Pretiosa margarita</i> was thereafter included in
the major alchemical anthologies of the sixteenth and seventeenth centuries, including the
<i>Theatrum Chemicum</i>.</p>

<p>The most significant Renaissance engagement with the <i>Pretiosa margarita</i> is probably the
circle of humanist scholars around Ficino and Pico, who found in Petrus Bonus's theological
argument a medieval precedent for the synthesis of Hermetic alchemy with Christian Neoplatonism
that they were attempting to construct. The claim that the philosopher's stone required divine
grace resonated with Ficino's understanding of the soul's capacity for divine illumination and
with Pico's argument that the ancient wisdom traditions — Hermetic, Kabbalistic, Platonic —
all converged on the same theological truth. In this reception, the <i>Pretiosa margarita</i>
served as a bridge between the medieval scholastic-alchemical tradition and the Renaissance
Hermetic synthesis, demonstrating that the two were compatible and mutually illuminating.</p>

<p>In the twentieth century, the <i>Pretiosa margarita</i> attracted the attention of Jung's circle,
particularly through the work of the Jungian analyst Barbara Obrist and, more substantially, through
Jung's own engagement with the allegorical interpretations of the Incarnation and the relation
between the philosopher's stone and Christ. Jung read Petrus Bonus's theological argument as an
expression of the alchemical unconscious's attempt to find a symbolic language adequate to the
experience of transformation, and his discussion of the <i>Pretiosa margarita</i> in
<i>Psychology and Alchemy</i> and <i>Aion</i> contributed to its modern reputation as one of the
most spiritually ambitious of the medieval alchemical texts.</p>

<h2>Scholarly Debates</h2>

<p>The principal scholarly debates surrounding the <i>Pretiosa margarita</i> concern the sources of
its theological argument, the character of its allegorical method, and its place in the history
of the relationship between alchemy and religion. On the sources of the theological argument,
scholars have debated the extent to which Petrus Bonus derived his claim about divine grace from
within the alchemical tradition itself — from earlier pseudo-Hermetic and Arabic texts that
attributed supernatural dimensions to the philosopher's stone — or from Scholastic theology,
particularly from discussions of miracles and supernatural causation in Aquinas and his
predecessors. William Newman's work on medieval alchemy and natural philosophy has helped to
clarify the scholastic intellectual context within which the argument was constructed. On the
allegorical method, the debate concerns whether Petrus Bonus's readings of classical myth and
Christian scripture are genuine attempts to claim that ancient wisdom concealed alchemical truth
or are rhetorical strategies to legitimate a materially suspect practice by association with
authoritative texts. The answer is almost certainly both, and the inability to cleanly separate
the rhetorical from the sincere dimension reflects a general feature of medieval allegorical
discourse. On the place of the <i>Pretiosa margarita</i> in the history of alchemy and religion,
Lawrence Principe's historiographical arguments about the distortions introduced by the
spiritual-alchemical reading tradition — both in its Renaissance forms and in its twentieth-century
Jungian elaboration — provide a necessary corrective to the tendency to read the work primarily
through the lens of later spiritualizing interpretation.</p>

<h2>Literature</h2>

<p>Petrus Bonus. <i>Pretiosa margarita novella</i>. Venice: Aldus, 1546. Reprinted in <i>Bibliotheca
Chemica Curiosa</i>, edited by Jean-Jacques Manget. Geneva, 1702.</p>
<p>Waite, Arthur Edward, trans. <i>The New Pearl of Great Price</i>. London: James Elliott, 1894.</p>
<p>Newman, William R. <i>Promethean Ambitions: Alchemy and the Quest to Perfect Nature</i>.
Chicago: University of Chicago Press, 2004.</p>
<p>Principe, Lawrence M. <i>The Secrets of Alchemy</i>. Chicago: University of Chicago Press, 2013.</p>
<p>Jung, Carl Gustav. <i>Psychology and Alchemy</i>. Translated by R. F. C. Hull. Princeton:
Princeton University Press, 1953.</p>
<p>Crisciani, Chiara. "The Conception of Alchemy as Expressed in the <i>Pretiosa margarita novella</i>
of Petrus Bonus of Ferrara." <i>Ambix</i> 20 (1973): 165–181.</p>
"""

# ---------------------------------------------------------------------------
# INGEST
# ---------------------------------------------------------------------------

ENTRIES = [
    ("thomas_aquinas",    bio_thomas_aquinas),
    ("al_razi",           bio_al_razi),
    ("ibn_umayl",         bio_ibn_umayl),
    ("khalid_ibn_yazid",  bio_khalid_ibn_yazid),
    ("bernard_of_trevisan", bio_bernard_of_trevisan),
    ("petrus_bonus",      bio_petrus_bonus),
]

def main():
    conn = sqlite3.connect(DB_PATH)
    for person_id, bio_html in ENTRIES:
        conn.execute(
            "UPDATE persons SET bio_html = ? WHERE person_id = ?",
            (bio_html, person_id)
        )
        print(f"Updated {person_id} ({len(bio_html):,} chars)")
    conn.commit()
    conn.close()
    print("Done. All biographies committed.")

if __name__ == "__main__":
    main()
