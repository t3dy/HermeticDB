"""
write_bios_renaissance_em.py
----------------------------
Writes encyclopedia-length bio_html entries for five figures:
  - giovanni_pico       (RENAISSANCE)
  - nicholas_of_cusa    (RENAISSANCE)
  - jacob_boehme        (EARLY_MODERN)
  - kenelm_digby        (EARLY_MODERN)
  - nicolas_flamel      (MEDIEVAL)

Safe to re-run (idempotent UPDATE).
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(r"c:\Dev\EmeraldTablet\db\emerald_tablet.db")

# ---------------------------------------------------------------------------
# 1. GIOVANNI PICO DELLA MIRANDOLA
# ---------------------------------------------------------------------------
BIO_GIOVANNI_PICO = """
<p>Giovanni Pico della Mirandola (1463–1494) stands as the most audacious intellect of the
Italian Renaissance, a philosopher who attempted nothing less than the harmonisation of every
major stream of ancient and medieval wisdom — Platonic, Aristotelian, Hermetic, Kabbalistic,
Zoroastrian, and Arabic — into a single architectonic synthesis. Born at Mirandola in the
Este duchy of northern Italy, Pico received an education that was from the beginning
exceptional in its breadth: canon law at Bologna was followed by intensive study of Aristotelian
philosophy at Ferrara and Padua, then by Greek and Latin literature at Florence, where he
entered the orbit of <a href="../persons/marsilio_ficino.html">Marsilio Ficino</a> and the
Platonic Academy. He subsequently mastered Hebrew, Aramaic, and Arabic — a polyglot
accomplishment without parallel among his contemporaries — in order to read the Kabbalah, the
Talmud, the Arabic philosophers, and the Zoroastrian <i>Oracula Chaldaica</i> in their
original tongues. When he composed his nine hundred <i>Conclusiones philosophicae, cabalasticae
et theologicae</i> in 1486 and proposed to defend them publicly in Rome before all the learned
men of Christendom, he was twenty-three years old. The disputation was never held: Pope Innocent
VIII appointed a commission that condemned thirteen of the theses as heretical, and Pico's
subsequent flight to France, his arrest, and his eventual return to Florence under Medici
protection transformed him overnight from an ambitious young courtier-philosopher into the most
controversial thinker in Europe. He died in Florence on 17 November 1494 — the very day that
Charles VIII of France entered the city — at the age of thirty-one, almost certainly of
arsenic poisoning, though the circumstances remain disputed. His life was brief; his influence
was immense and enduring.</p>

<h2>Works and Intellectual Context</h2>

<p>The <i>Conclusiones</i> of 1486 remain the most extraordinary intellectual document of the
fifteenth century. In nine hundred theses drawn from more than twenty discrete philosophical
and theological traditions, Pico proposed a prismatic unity beneath the apparent diversity of
human wisdom. The organization of the text is itself significant: Pico distinguishes between
theses that summarize the views of earlier authorities (<i>secundum opinionem alienam</i>) and
those that represent his own novel conclusions (<i>secundum opinionem propriam</i>). Among the
latter are the twenty-six Orphic magical conclusions and the seventy-two Kabbalistic
conclusions, which together constitute the first systematic attempt to fuse the operative
traditions of ancient theurgy, Hermetic natural magic, and Jewish mysticism within a Christian
philosophical framework. Pico's Hermetic theses — drawing primarily on the
<i>Corpus Hermeticum</i> as translated by Ficino and published in 1471 — treat Hermes
Trismegistus as a member of the chain of ancient theologians whose wisdom prefigured and
confirmed Christian truth. Hermes appears in the <i>Conclusiones</i> alongside Zoroaster,
Orpheus, Pythagoras, and Plato as a guardian of the <a href="../concepts/prisca_theologia.html"><i>prisca theologia</i></a>,
the prisca or ancient theology that Ficino had identified as the hidden unity beneath
philosophical diversity.</p>

<p>The <i>Oratio de dignitate hominis</i>, composed as the introductory address for the
planned disputation, has acquired canonical status in the historiography of the Renaissance
as the great manifesto of humanist dignity. In it Pico constructs a daring theological
anthropology: God, having exhausted all the fixed natures in creating the hierarchy of beings
from angels to minerals, placed the human being at the centre of the cosmos without a
determinate nature, free to descend toward the brutes or ascend toward the angels by the
exercise of will. This radical plasticity of the human — its capacity for self-transformation
— is grounded in Pico's synthesis of Platonic, Hermetic, and Kabbalistic sources. The
Hermetic resonance is direct: the <i>Poimandres</i> (Corpus Hermeticum I) describes the
Primal Man descending through the planetary spheres and assuming each nature in turn, while
the <i>Asclepius</i> celebrates humanity as the <i>magnum miraculum</i>, the great wonder of
creation. Pico weaves these passages into the <i>Oratio</i> without attribution, treating them
as confirming evidence for a truth already known.</p>

<p>Following the condemnation, Pico composed his <i>Apologia</i> (1487), a lengthy and
technically precise defence of the thirteen condemned theses, addressed to the Pope. The
<i>Apologia</i> is important not only as polemic but as evidence of the seriousness with which
Pico took the distinction between philosophical speculation and theological determination: he
insisted repeatedly that the Kabbalistic and magical conclusions were philosophical
<i>opiniones</i>, not assertions of faith. His later works show a partial withdrawal from the
more adventurous claims of 1486. The <i>Heptaplus</i> (1489), a seven-fold commentary on the
opening verses of Genesis, employs a structure derived from the seven planetary spheres but
works primarily within the Neoplatonic and Kabbalistic traditions rather than the Hermetic.
<i>De ente et uno</i> (1491) engages the scholastic debate between Thomism and Scotism about
the transcendentals of being and unity, and represents Pico's most technically Aristotelian
work. The posthumous <i>Disputationes adversus astrologiam divinatricem</i>, edited by his
nephew Gianfrancesco, is a massive critique of judicial astrology that draws on empirical,
philosophical, and theological arguments; it was enormously influential in undermining the
prestige of astrological prediction in the following century.</p>

<h2>Hermetic Significance and the Kabbalah Synthesis</h2>

<p>Pico's place in the history of Hermeticism is secured primarily by two contributions. The
first is the systematisation of Christian Kabbalah as a philosophical method. Pico was the
first Christian thinker to study the Kabbalah intensively from primary Hebrew sources, guided
by the convert Flavius Mithridates who translated a substantial corpus of Kabbalistic texts
into Latin for his use. In his Kabbalistic conclusions, Pico proposed that <a href="../concepts/kabbalah.html">Kabbalah</a>
confirmed the Christian doctrines of the Trinity, the incarnation, and the soul's immortality —
an argument that defined the programme of Christian Kabbalah for the next two centuries,
influencing Johannes Reuchlin, Guillaume Postel, and the entire tradition of Renaissance
syncretism. The second contribution is his integration of the Hermetic texts with this
Kabbalistic framework. For Pico, the <i>Corpus Hermeticum</i> and the Kabbalistic writings
were not competing traditions but convergent witnesses to a single ancient wisdom. This
alignment of Hermes with the Kabbalistic tradition — rather than treating Hermes purely as
a Platonic authority, as Ficino had done — gave the Hermetic texts a new valence in Christian
theological discourse: they could be cited not only as Platonic forerunners of Christian
Platonism, but as confirming evidence for specifically Jewish-Christian mystical claims about
the divine names, the angelic hierarchies, and the structure of the soul.</p>

<p>Pico's magical conclusions deserve special attention. He proposed, in his own
theses <i>de magia</i>, that no magic is operative unless it involves Kabbalah — a claim that
effectively elevated Kabbalistic letter-magic above the Hermetic and Neoplatonic theurgical
traditions. This hierarchy proved enormously influential: it shaped the understanding of
Renaissance magic in the work of Heinrich Cornelius Agrippa, whose <i>De occulta philosophia</i>
(1531) is in many respects an expansion of Pico's magical programme, and it contributed to the
Christianisation of Hermetic practice that distinguished the Renaissance Hermetic tradition
from its Late Antique antecedents.</p>

<h2>Scholarly Debates</h2>

<p>Modern scholarship on Pico is both voluminous and contested. S. A. Farmer's critical edition
and study of the <i>Conclusiones</i> (1998) demonstrated that many of the nine hundred theses
are more scholastically technical than the humanist reception of Pico had suggested, and that
the syncretism of the work is more programmatic than substantive — the different philosophical
traditions are juxtaposed rather than genuinely fused. Farmer's work challenged the idealized
image of Pico as the Renaissance philosopher of universal harmony. Brian Copenhaver and Charles
Schmitt, in their <i>Renaissance Philosophy</i> (1992), situate Pico within the scholastic
curriculum that formed him, emphasising the Aristotelian backbone of his thought and qualifying
the extent to which he broke with academic philosophy. Wouter Hanegraaff, in his analysis of
Pico's place within the Western esoteric tradition, has stressed the importance of the
actor-analyst distinction: Pico did not understand himself as practicing a unified tradition
called Hermeticism or esotericism; he understood himself as doing philosophy, and the traditions
he drew upon were for him repositories of philosophical argument, not initiatory paths. The
question of whether Pico can be said to have "created" Christian Kabbalah — or whether he merely
systematised tendencies already present in earlier syncretist thought — remains a matter of
scholarly debate, addressed most carefully by Chaim Wirszubski in his foundational study
<i>Pico della Mirandola's Encounter with Jewish Mysticism</i> (1989).</p>

<h2>Transmission and Reception</h2>

<p>The posthumous reputation of Pico was shaped decisively by his nephew Gianfrancesco Pico,
who edited and published his uncle's works and wrote a biography that emphasised Pico's
late-life turn toward Savonarolan piety. This hagiographic framing made Pico acceptable to
Counter-Reformation readers while suppressing the more dangerous implications of his magical
and Kabbalistic work. In the sixteenth century, the influence of the <i>Conclusiones</i>
ramified through Reuchlin's <i>De arte cabalistica</i>, through Agrippa's <i>De occulta
philosophia</i>, and through the entire tradition of Renaissance magic and Kabbalah. The
<i>Oratio</i> was rediscovered in the nineteenth century and gradually elevated to the status
of the defining text of Renaissance humanism — a canonical status that, as scholars like
Quentin Skinner and Eugenio Garin have noted, owes more to later interpretive traditions than
to the text's own historical reception. Pico remains a figure of perennial fascination at the
intersection of philosophy, mysticism, and the history of religion, and scholarly interest
in his work has intensified considerably since the late twentieth century.</p>

<h2>Literature</h2>

<p>Farmer, S. A. <i>Syncretism in the West: Pico's 900 Theses (1486)</i>. Tempe: Medieval and
Renaissance Texts and Studies, 1998.</p>
<p>Wirszubski, Chaim. <i>Pico della Mirandola's Encounter with Jewish Mysticism</i>. Cambridge,
MA: Harvard University Press, 1989.</p>
<p>Copenhaver, Brian P., and Charles B. Schmitt. <i>Renaissance Philosophy</i>. Oxford: Oxford
University Press, 1992.</p>
<p>Hanegraaff, Wouter J. (ed.). <i>Dictionary of Gnosis and Western Esotericism</i>. Leiden:
Brill, 2006.</p>
<p>Craven, William G. <i>Giovanni Pico della Mirandola: Symbol of His Age</i>. Geneva: Droz,
1981.</p>
<p>Wind, Edgar. <i>Pagan Mysteries in the Renaissance</i>. London: Faber and Faber, 1958.</p>
""".strip()

# ---------------------------------------------------------------------------
# 2. NICHOLAS OF CUSA
# ---------------------------------------------------------------------------
BIO_NICHOLAS_OF_CUSA = """
<p>Nicholas of Cusa (1401–1464), known in Latin as Nicolaus Cusanus and in German as
Nikolaus von Kues, was the most original systematic philosopher produced by the Latin West
in the fifteenth century, and a thinker whose cosmological and theological doctrines had
consequences that reverberated through the following two centuries of European intellectual
history. Born at Kues on the Moselle in the archdiocese of Trier, the son of a prosperous
wine merchant and river boatman, he received his early education from the Brethren of the
Common Life at Deventer — an institution that shaped many of the leading spiritual and
intellectual figures of the age — before studying canon law at Heidelberg and then
philosophy, theology, and mathematics at Padua, where he took his doctorate in 1423. His
subsequent career was simultaneously that of a churchman of the highest distinction and of
a philosopher of breathtaking speculative ambition. He rose to become a Cardinal of the
Roman Church (1448) and Prince-Bishop of Brixen in the Tyrol (1450), papal legate to the
German territories, and trusted adviser of Popes Eugenius IV and Pius II. He died at Todi
in Umbria on 11 August 1464, having never quite resolved the tension between the ecclesial
institution he served and the reformist and speculative impulses that drove his thought.
His manuscripts and library survive at the hospital he founded at Kues, constituting one of
the most important collections of late-medieval learning in existence.</p>

<h2>Philosophical Works and Core Doctrines</h2>

<p>The philosophical corpus of Cusanus is dense, technically demanding, and formally unified
by a small number of master concepts that he developed and refined across a lifetime of
writing. The foundational work is <i>De docta ignorantia</i> (<i>On Learned Ignorance</i>,
1440), composed in three books during his return voyage from the Council of Constantinople.
The first book treats the nature of the infinite maximum — God — which transcends all finite
rational categories and can be approached only by a knowing ignorance (<i>docta ignorantia</i>):
the learned recognition that the infinite exceeds all proportion to the finite, that every
positive predication of God is inadequate, and that the deepest form of knowledge consists
in the clear comprehension of this inadequacy. The second book treats the universe as a
<i>contractum maximum</i>, a contracted or finite image of the infinite: the universe is
unbounded but not infinite in the strict sense, has no fixed centre or circumference, and
every part of it reflects the whole according to its own particular mode of being. The third
book treats Christ as the absolute maximum that is also contractedly particular — the
coincidence of the infinite and the finite in a single person. The concept of
<i>coincidentia oppositorum</i> — the coincidence of opposites in the divine infinity, where
all distinctions that are absolute for finite minds are resolved — runs through the entire
work as its generative metaphysical principle.</p>

<p>The <i>De coniecturis</i> (1441–1442) develops the epistemological complement to this
metaphysics: all human knowledge is conjectural, an approximation to truth that never reaches
the absolute. The remarkable <i>Idiota</i> dialogues (<i>De sapientia</i>, <i>De mente</i>,
<i>De staticis experimentis</i>, 1450) place these doctrines in the mouth of an unlettered
layman (<i>idiota</i>) who instructs an Aristotelian philosopher and an orator in the limits
of their book-learning: wisdom is not found in the schools but in the mind's direct encounter
with its own operations. The <i>De visione Dei</i> (1453), addressed to the monks of Tegernsee,
uses the metaphor of an omnivoyant portrait — an image whose gaze seems to follow the viewer
wherever he stands — to conduct a mystical-contemplative exploration of the divine vision.
Later works, including <i>De beryllo</i> (1458) and <i>De non aliud</i> (1461–1462), refine
the conceptual vocabulary of <i>coincidentia</i> and push toward an apophatic theology of
the absolute that anticipates some features of later German Idealism.</p>

<h2>Cosmological Significance and the Connection to Bruno</h2>

<p>The second book of <i>De docta ignorantia</i> contains the cosmological theses that gave
Cusanus his most decisive historical influence. His argument that the universe has no fixed
centre — that what appears to be the centre from any point of observation is merely the local
perspective of a finite being within an unbounded whole — was taken up by
<a href="../persons/giordano_bruno.html">Giordano Bruno</a> in the 1580s and transformed into
the doctrine of the infinite, homogeneous universe composed of innumerable worlds. Bruno
acknowledged the debt explicitly, citing Cusanus as the thinker who had first grasped the
infinity of the universe. The difference between the two doctrines is, however, philosophically
significant: for Cusanus, the universe is not infinite but merely unbounded (<i>interminatum</i>),
since genuine infinity belongs to God alone; for Bruno, the universe is actually infinite and
God is identical with it. The move from Cusan interminability to Brunonian infinity is one of
the decisive transitions in early modern cosmology, and it is inseparable from the theological
differences between the two thinkers. Cusanus remained a committed Christian Neoplatonist for
whom the absolute infinity of God was non-negotiable; Bruno dissolved that distinction in a
pantheistic direction that brought him before the Inquisition.</p>

<p>The connection between Cusanus and the Neoplatonic and Hermetic traditions is also direct.
He participated in the Council of Florence of 1438–1439, at which the Byzantine delegations
— including Gemistos Plethon, whose lecture on the difference between Plato and Aristotle
catalysed <a href="../persons/marsilio_ficino.html">Marsilio Ficino</a>'s entire Platonic
project — brought the living Greek philosophical tradition into sustained contact with Latin
scholasticism. Cusanus acquired Greek manuscripts at the Council, and his library contains
copies of Platonic and Neoplatonic texts that confirm the breadth of his engagement with the
Greek tradition. His relation to Cardinal Bessarion, the most important conduit of Byzantine
<a href="../concepts/neoplatonism.html">Neoplatonism</a> to the Latin West, was close and
sustained. While Cusanus did not engage systematically with the Hermetic texts — the
<i>Corpus Hermeticum</i> was not translated into Latin until Ficino's version of 1471, seven
years after Cusanus's death — the structural affinities between his thought and the Hermetic
tradition are considerable: the doctrine of the <i>imago Dei</i> in the human mind, the
microcosm-macrocosm analogy, the centrality of the human knower within the cosmic order, and
the apophatic approach to the divine all have close counterparts in the Hermetic writings.</p>

<h2>Spiritual Practice and Mystical Theology</h2>

<p>Cusanus occupies a distinctive position at the intersection of late-medieval mystical
theology and Renaissance philosophy. His debt to Meister Eckhart — whose works he copied
and annotated — is evident throughout his writings: the language of the soul's ascent beyond
rational categories, the doctrine of the divine ground beyond all names, and the dialectical
play between knowing and not-knowing all have Eckhartian antecedents. Cusanus defended Eckhart
against charges of heresy in marginal annotations, and his own treatment of the divine
infinity as coinciding with nothing-in-particular owes much to Eckhart's theology of the
<i>Gottheit</i> (Godhead) beyond the personal God. At the same time, Cusanus's philosophical
method is more formally rigorous than Eckhart's; he employs mathematical analogies —
the relation between the polygon and the circle, the projection of a line into a point, the
proportion between finite and infinite — with a precision that reflects his genuine mathematical
competence, and his epistemology of conjecture has a systematic character that Eckhart's sermons
do not. The combination of mathematical rigour, mystical aspiration, and cosmological
speculation makes Cusanus an almost unique figure in the intellectual history of the period.</p>

<h2>Scholarly Debates and Modern Reception</h2>

<p>The modern scholarly reception of Cusanus has been shaped by several competing
interpretive frameworks. Jasper Hopkins, who produced the definitive English translations of
the complete philosophical works over several decades, has argued for reading Cusanus primarily
within the tradition of Christian Neoplatonism and apophatic theology, emphasising the
continuity with medieval sources and resisting the tendency to read him as a proto-modern.
Ernst Cassirer, in his <i>Individuum und Kosmos in der Philosophie der Renaissance</i> (1927),
placed Cusanus at the origin of Renaissance subjectivism and the modern concept of the
individual knower. Hanegraaff's analysis emphasises the ways in which Cusan doctrines were
received and transformed within the Western esoteric tradition — particularly through the
mediation of Bruno — without assimilating Cusanus himself to that tradition. The question of
Cusanus's own religious practice and inner experience remains largely opaque: unlike the
Rhineland mystics, he wrote little that is autobiographical, and his voluminous correspondence
is primarily administrative. What is not disputed is that his influence on the intellectual
history of the fifteenth and sixteenth centuries was profound and pervasive, ramifying through
Bruno, through Ficino, through the tradition of learned magic, and through the cosmological
revolutions of the early modern period.</p>

<h2>Literature</h2>

<p>Hopkins, Jasper. <i>Nicholas of Cusa on Learned Ignorance: A Translation and an Appraisal
of De Docta Ignorantia</i>. Minneapolis: Arthur J. Banning Press, 1981.</p>
<p>Cassirer, Ernst. <i>The Individual and the Cosmos in Renaissance Philosophy</i>. Translated
by Mario Domandi. New York: Harper and Row, 1963.</p>
<p>Moffitt Watts, Pauline. <i>Nicolaus Cusanus: A Fifteenth-Century Vision of Man</i>. Leiden:
Brill, 1982.</p>
<p>Hanegraaff, Wouter J. (ed.). <i>Dictionary of Gnosis and Western Esotericism</i>. Leiden:
Brill, 2006.</p>
<p>Bond, H. Lawrence (trans.). <i>Nicholas of Cusa: Selected Spiritual Writings</i>. New York:
Paulist Press, 1997.</p>
<p>Christianson, Gerald, and Thomas M. Izbicki (eds.). <i>Nicholas of Cusa in Search of God
and Wisdom</i>. Leiden: Brill, 1991.</p>
""".strip()

# ---------------------------------------------------------------------------
# 3. JAKOB BÖHME
# ---------------------------------------------------------------------------
BIO_JACOB_BOEHME = """
<p>Jakob Böhme (1575–1624) was a German Lutheran mystic and theosopher whose works constitute
one of the most remarkable bodies of speculative religious thought produced in the early modern
period. Born at Alt-Seidenberg near Görlitz in Upper Lusatia — a region that lay at the
intersection of German, Czech, and Polish cultures and was marked by unusual religious
diversity during the Reformation era — he worked throughout his life as a cobbler and small
merchant, composing his extraordinary treatises without formal academic training and in the
German vernacular at a time when philosophical and theological discourse was almost exclusively
conducted in Latin. This social marginality was not incidental to his thought: Böhme
consistently represented himself as an instrument of divine revelation rather than a learned
philosopher, and his works carry the authority of visionary experience rather than of
scholarly argument. Yet the content of his theosophy is dense with the technical vocabulary
of late-medieval mysticism, Paracelsian natural philosophy, and Lutheran biblical exegesis,
and his writings were read and used by some of the most learned minds of the following
two centuries. He died at Görlitz on 17 November 1624, having completed in just over a decade
of active writing a corpus that would shape German Idealism, English mysticism, American
Transcendentalism, and the Western esoteric tradition into the twentieth century.</p>

<h2>The Visionary Experience and Early Works</h2>

<p>Böhme described three distinct moments of illumination in his life. The first, in 1600,
came upon him while he sat in his workshop and gazed into the reflected light in a pewter dish:
he experienced a sudden expansion of perception in which the inner ground of all things was
disclosed to him as simultaneously present in every particular object. A second illumination
followed in 1610, and it was this experience that drove him to write the first and most
controversial of his works, the <i>Aurora, oder Morgenröthe im Aufgang</i> (<i>Aurora, or
the Rising of the Dawn</i>, 1612). The <i>Aurora</i> remained unfinished — Böhme's copies
were confiscated by the Görlitz town pastor Gregor Richter, who denounced him before the city
council as a heretic and fanatic — but manuscript copies circulated and reached readers far
beyond Görlitz. The work is syntactically and conceptually turbulent, full of sudden
qualitative shifts and paradoxical formulations; it explores the nature of God's self-revelation
through the struggle between contrary qualities or forces within the divine ground,
a theme that would be progressively refined in everything Böhme subsequently wrote.</p>

<p>The mature works, composed between 1619 and 1624, represent a sustained and systematic
attempt to articulate the theosophy that the visionary experiences had disclosed. <i>De
Tribus Principiis, oder Beschreibung der Drey Principien Göttliches Wesens</i> (<i>On the
Three Principles of the Divine Being</i>, 1619) distinguishes three principles that structure
all reality: the Father's dark fire-world, the Son's light-world, and the external visible
world of creation. <i>De Signatura Rerum</i> (<i>The Signature of All Things</i>, 1621)
develops the doctrine of signatures — the idea that the inner spiritual quality of every
created thing is expressed in its external form and that the adept who knows how to read
these signatures possesses a key to the inner constitution of nature. This doctrine, which
Böhme shared with <a href="../persons/paracelsus.html">Paracelsus</a> and the broader
Paracelsian tradition, connects his theosophy to the natural-philosophical concerns of the
period. <i>Mysterium Magnum</i> (1623), his longest and most systematic work, is an
allegorical commentary on Genesis that reads the creation narrative as a disclosure of the
eternal processes within the divine ground itself. It is in this work that Böhme most fully
articulates his understanding of the relationship between God's eternal self-revelation
(<i>Offenbarung</i>) and the temporal creation that proceeds from it.</p>

<h2>Theological Theosophy: God, Darkness, and Will</h2>

<p>The central and most radical feature of Böhme's theosophy is his insistence that God
encompasses both light and darkness, both love and wrath, both the ground of being and a
principle of counter-will or resistance. The divine Unground (<i>Ungrund</i>), the
primordial abyss of deity before all self-differentiation, generates within itself a
dialectical process through which God comes to know and to reveal Godself. The first
principle — associated with the Father, with fire, with darkness and contraction — is not
evil but is the necessary condition of all vitality and intensity; without it, the divine
light would be mere undifferentiated passivity. The second principle — associated with the
Son, with light, with love and expansion — proceeds from the first as its resolution and
fulfilment. The third principle — the external world of nature and history — is the field
in which this inner divine drama is externally expressed. Evil arises when creaturely will
asserts itself against the divine ground, refusing the movement from darkness to light; it
is not a separate principle but a misdirection of the very energies that, rightly ordered,
constitute the divine life.</p>

<p>This dialectical structure — the movement from identity through opposition to
reconciliation — was recognized by Friedrich Wilhelm Joseph Schelling and Georg Wilhelm
Friedrich Hegel as a direct anticipation of their own speculative systems. Schelling's
<i>Philosophische Untersuchungen über das Wesen der menschlichen Freiheit</i> (1809) draws
explicitly on Böhme's concept of the divine ground and counter-will; Hegel acknowledged
Böhme as the first genuinely German philosopher. The Böhme-Hegel-Schelling connection is
one of the most significant and well-documented instances of esoteric thought influencing
the mainstream of academic philosophy, and it has been explored in detail by scholars
including Glenn Alexander Magee and Cyril O'Regan.</p>

<h2>Sources and Intellectual Context</h2>

<p>Böhme's intellectual formation, though not academic, was wide. The most important single
influence was <a href="../persons/paracelsus.html">Paracelsus</a>, whose tripartite division
of reality into sulphur, mercury, and salt, whose doctrine of signatures, and whose
conception of the archeus or inner life-principle of natural bodies all find direct echoes
in Böhme's theosophy. The Lutheran mystical tradition, mediated by the works of Johann
Arndt and Valentin Weigel, provided the pietist and apophatic dimensions of his thought.
Weigel's doctrine that the knowing subject contains within itself the ground of all
knowledge — that to know God one must become God — is particularly close to Böhme's own
epistemological claims. The Rhineland mystical tradition of Meister Eckhart and Johannes
Tauler, available in Lutheran devotional anthologies, contributed the vocabulary of the
divine ground, the birth of the Word in the soul, and the language of the <i>Abgrund</i>
or abyss. Böhme also had access, through his Görlitz circle of educated friends — notably
the physician Balthasar Walther, who had travelled to the Near East in search of Kabbalistic
learning — to traditions of Jewish mysticism and to currents of Renaissance Neoplatonism
that might not otherwise have been available to a self-educated craftsman in a provincial
Saxon city.</p>

<h2>Transmission and Influence</h2>

<p>The transmission of Böhme's thought beyond Görlitz began during his lifetime through
manuscript copies and continued immediately after his death through the efforts of his circle.
The first printed editions appeared in Amsterdam in the 1630s and 1640s, where the relative
freedom of the Dutch press allowed works that could not be legally published in the German
Lutheran territories. English translations appeared from the 1640s onward, initiated by the
circle around John Sparrow and Charles Hotham, and Böhme rapidly became a central figure
in the spiritual underground of Interregnum England. His influence reached Henry More and
the Cambridge Platonists, who engaged critically with his theosophy; it reached the Quakers,
who found in his doctrine of the inner light a confirmation of their own experience; and it
reached <a href="../persons/francis_mercury_van_helmont.html">Francis Mercury van Helmont</a>,
through whom Böhme's ideas entered the network of learned theosophers and natural philosophers
that connected Amsterdam, London, and the German courts in the second half of the seventeenth
century. William Law's eighteenth-century edition of Böhme's collected works in English
exercised a direct influence on William Blake, in whose prophetic books the Böhmenian
dialectic of contraries — the Tiger and the Lamb, Los and Urizen — is unmistakable.</p>

<p>In the twentieth century, C. G. Jung drew on Böhme's doctrine of God's dark ground in
his psychological theology of the self, and Böhme's thought has continued to attract scholarly
attention from historians of religion, of philosophy, and of Western esotericism. Andrew Weeks's
<i>Boehme: An Intellectual Biography of the Seventeenth-Century Philosopher and Mystic</i>
(1991) remains the most thorough scholarly biography in English, while Hanegraaff's analysis
in the <i>Dictionary of Gnosis and Western Esotericism</i> situates Böhme precisely within
the historiographical framework of Western esotericism as a scholarly category.</p>

<h2>Literature</h2>

<p>Weeks, Andrew. <i>Boehme: An Intellectual Biography of the Seventeenth-Century Philosopher
and Mystic</i>. Albany: State University of New York Press, 1991.</p>
<p>Stoudt, John Joseph. <i>Sunrise to Eternity: A Study in Jacob Boehme's Life and Thought</i>.
Philadelphia: University of Pennsylvania Press, 1957.</p>
<p>Magee, Glenn Alexander. <i>Hegel and the Hermetic Tradition</i>. Ithaca: Cornell University
Press, 2001.</p>
<p>O'Regan, Cyril. <i>Gnostic Apocalypse: Jacob Boehme's Haunted Narrative</i>. Albany: State
University of New York Press, 2002.</p>
<p>Hanegraaff, Wouter J. (ed.). <i>Dictionary of Gnosis and Western Esotericism</i>. Leiden:
Brill, 2006.</p>
<p>Walsh, David. <i>The Mysticism of Innerworldly Fulfillment: A Study of Jacob Boehme</i>.
Gainesville: University Presses of Florida, 1983.</p>
""".strip()

# ---------------------------------------------------------------------------
# 4. KENELM DIGBY
# ---------------------------------------------------------------------------
BIO_KENELM_DIGBY = """
<p>Sir Kenelm Digby (1603–1665) was an English natural philosopher, alchemist, naval commander,
diplomat, and founding Fellow of the Royal Society who occupied a singular position in the
intellectual landscape of seventeenth-century Europe. His career combined achievements and
affiliations that appear, from a later perspective, almost incompatibly heterogeneous: he was
simultaneously a practitioner of Paracelsian sympathetic medicine, a reader and personal
acquaintance of René Descartes, a Catholic recusant who moved in the highest Protestant
intellectual circles, a courtier who was twice exiled from England, and a man whose
extravagant personal legend — built on his exploits at sea, his notorious grief at the death
of his beautiful wife Venetia Stanley, and his cultivation of the image of the learned
knight-errant — made him one of the most talked-about figures of his age. He was born at
Gayhurst in Buckinghamshire on 11 July 1603, the son of Sir Everard Digby, who was executed
in February 1606 for his role in the Gunpowder Plot — a beginning that made Kenelm a Catholic
orphan in a Protestant kingdom and fixed the conditions of his subsequent marginality and
resourcefulness in equal measure. He died in London on 11 June 1665. His life spans the
period from the Jacobean court to the Restoration, and his career charts the passage of
natural philosophy from the Hermetic-Paracelsian framework through the mechanical and
experimental traditions that would crystallise into the Royal Society.</p>

<h2>Naval Exploits and Early Career</h2>

<p>The extraordinary range of Digby's activities began early. After education at Oxford —
which he left without a degree, as was conventional for gentlemen — and travel in Europe,
where he acquired the languages, connections, and intellectual formation that would distinguish
his subsequent career, he undertook a private naval expedition to the Mediterranean in 1627–28,
ostensibly with royal commission but substantially self-funded. The expedition culminated in
the Battle of Scanderoon (Iskenderun) in June 1628, in which Digby's small fleet engaged and
defeated a combined Venetian-French force of superior size. The battle was celebrated in
England as a triumph of English naval courage and entrepreneurial daring, and it gave Digby
the heroic reputation that preceded him for the rest of his life. He was knighted by Charles I
on his return. The years following were marked by his marriage to Venetia Stanley (1625, after
a long and scandalous courtship) and by his growing involvement in the intellectual networks
of London and Paris. Venetia died suddenly and unexpectedly on 1 May 1633 — she was found dead
in her bed, aged thirty-two — and her death precipitated the crisis that determined the
subsequent direction of Digby's life.</p>

<h2>Natural Philosophy: Between Hermeticism and Mechanism</h2>

<p>Digby's grief at Venetia's death drove him first to a period of intense Catholic devotional
practice and then to Paris, where he settled in 1635 and remained, with intervals, until 1660.
In Paris he became a central figure in the intellectual life of the city: he attended the
circle of Marin Mersenne, the Franciscan friar who served as the clearing-house for natural
philosophical correspondence across Europe; he met René Descartes in 1637 and engaged him
in extended discussion of the soul and its relation to the body; and he produced, in
manuscript, thousands of pages of notes on natural philosophy, alchemy, and the occult
properties of bodies that have never been fully edited or published. His first major
published work, <i>Two Treatises: Of Bodies and of Man's Soul</i> (Paris, 1644), is a
systematic attempt to provide a natural-philosophical account of body and soul that is
simultaneously Aristotelian in its logical structure, Cartesian in its mechanical vocabulary,
and Paracelsian in many of its specific claims about sympathy, antipathy, and the active
properties of matter. The <i>Two Treatises</i> are not a successful synthesis — the tensions
between the competing frameworks are never resolved — but they are a fascinating document of
the moment of transition in which the older Hermetic-Paracelsian natural philosophy was being
simultaneously absorbed and displaced by the mechanical philosophy.</p>

<p>The work for which Digby became most widely known in his own lifetime, however, was his
<i>A Late Discourse Touching the Cure of Wounds by the Powder of Sympathy</i> (1658), a
French lecture subsequently translated into English and several other European languages. The
powder of sympathy — a compound of vitriol used not on the wound itself but on the weapon
or cloth that had caused it — was a widely discussed remedy in early seventeenth-century
medical practice, connected to the Paracelsian doctrine of weapon-salve and to the broader
tradition of sympathetic magic. Digby's lecture offered a mechanistic explanation of sympathetic
action in terms of corpuscles emanating from the blood on the weapon and transmitting curative
information back to the wound, thus presenting what was in effect a magical remedy in the
vocabulary of the new corpuscular philosophy. The lecture was enormously successful — it was
reprinted dozens of times across Europe — and it illustrates with particular clarity the
characteristic early modern strategy of naturalising the occult by redescribing its operations
in mechanistic terms. <a href="../persons/robert_boyle.html">Robert Boyle</a>, who knew Digby
personally and regarded him with a mixture of admiration and scepticism, engaged repeatedly
with his natural philosophy, and the relationship between Digby's broadly Paracelsian
materialism and Boyle's developing corpuscularian chemistry is one of the significant
intellectual genealogies of the period.</p>

<h2>Alchemy and the Hermetic Tradition</h2>

<p>Digby's alchemical interests, though less formally published than his natural philosophy,
were deep and sustained. His manuscript collections, preserved in part at the British Library
and elsewhere, include extensive notes on alchemical practice, recipes for the preparation
of metals, and theoretical reflections on the transmutation of substances that draw heavily
on <a href="../persons/paracelsus.html">Paracelsus</a> and on the Paracelsian tradition
mediated through figures such as Joseph du Chesne (Quercetanus) and Oswald Croll. His
<i>Discourse Concerning the Vegetation of Plants</i>, delivered at Gresham College in 1661
and published in 1669, treats the growth of plants as a model for understanding the active
principles that govern all natural change, and it draws on alchemical as well as mechanical
concepts in ways that demonstrate the continuing vitality of the Hermetic-Paracelsian
framework in the early years of the Royal Society. Betty Jo Teeter Dobbs, whose researches
into the alchemical dimensions of seventeenth-century natural philosophy established the
field, drew on Digby's work in her analysis of the broader context in which Isaac Newton
conducted his alchemical investigations; Principe's subsequent work has refined and in some
respects corrected Dobbs's account, but the centrality of Digby to the story of alchemy
in the period of the Scientific Revolution remains undisputed.</p>

<h2>Religious and Political Career</h2>

<p>Digby's Catholicism gave his intellectual career a distinctive inflection. In an
intellectual culture increasingly polarised between a Protestant natural philosophy allied
with the new science and a Counter-Reformation scholasticism suspicious of innovation,
Digby occupied a position that allowed him to move between worlds. He cultivated relations
with leading Protestant intellectuals — Mersenne, Descartes, Thomas Hobbes, and eventually
the founding Fellows of the Royal Society — while remaining a committed Catholic and a
loyal servant of the Stuart cause in exile. He served Queen Henrietta Maria as her
chancellor and as an unofficial diplomat, conducting negotiations with both the Pope and the
Spanish crown on behalf of the exiled English monarchy. His dual role as Catholic intellectual
and proto-scientific natural philosopher made him an uncomfortable figure who fit neatly into
neither the Catholic nor the Protestant intellectual establishment, and this discomfort was
productive: it forced him to develop strategies of translation and mediation between
incommensurable frameworks that are themselves historically significant.</p>

<h2>Legacy and Scholarly Debates</h2>

<p>The scholarly assessment of Digby has shifted considerably since the early twentieth century.
Earlier historians of science tended to treat him as an eccentric, a transitional figure whose
mixture of magic and mechanism was a symptom of the confusion of an age that had not yet
fully committed to the new science. More recent scholarship — particularly Dobbs, Rattansi,
and Principe — has argued that this judgement misunderstands the intellectual situation of
the mid-seventeenth century, in which the boundaries between the Hermetic-Paracelsian and
the mechanist traditions were not yet fixed, and in which serious and sophisticated thinkers
routinely operated across what later seemed an impassable divide. Digby's career is now seen
as exemplary of a broader phenomenon: the way in which the occult natural philosophy of the
Renaissance was not simply displaced by the new science but was partly absorbed into it,
its concepts translated into new vocabularies while its practical and speculative ambitions
persisted. He remains one of the most important and under-studied figures at the intersection
of Hermeticism, alchemy, and the origins of modern natural philosophy.</p>

<h2>Literature</h2>

<p>Dobbs, Betty Jo Teeter. <i>The Foundations of Newton's Alchemy: Or, "The Hunting of the
Greene Lyon"</i>. Cambridge: Cambridge University Press, 1975.</p>
<p>Rattansi, Piyo. "The Helmontian-Galenist Controversy in Restoration England."
<i>Ambix</i> 12 (1964): 1–23.</p>
<p>Principe, Lawrence M. <i>The Secrets of Alchemy</i>. Chicago: University of Chicago Press,
2013.</p>
<p>Petersson, R. T. <i>Sir Kenelm Digby: The Ornament of England, 1603–1665</i>. London:
Jonathan Cape, 1956.</p>
<p>Henry, John. "Occult Qualities and the Experimental Philosophy: Active Principles in
Pre-Newtonian Matter Theory." <i>History of Science</i> 24 (1986): 335–381.</p>
<p>Hanegraaff, Wouter J. (ed.). <i>Dictionary of Gnosis and Western Esotericism</i>. Leiden:
Brill, 2006.</p>
""".strip()

# ---------------------------------------------------------------------------
# 5. NICOLAS FLAMEL
# ---------------------------------------------------------------------------
BIO_NICOLAS_FLAMEL = """
<p>Nicolas Flamel (c. 1330–1418) is the most celebrated alchemical legend in the European
tradition — and the clearest illustration of the process by which a modest historical
individual was transformed, long after his death, into the archetypal master of the
<a href="../concepts/alchemy.html"><i>ars alchemia</i></a>. The historical Flamel was a
prosperous Parisian manuscript dealer and scrivener (<i>écrivain public</i>) whose career
spanned the reigns of Charles V and Charles VI of France. Born at Pontoise in the Île-de-France,
he established himself in Paris, where he operated from premises near the church of Saint-Jacques
la Boucherie in the district of the manuscript trade. Contemporary records document him as a
man of considerable wealth, accumulated through legitimate commercial activity in the book
trade, real estate, and lending. He and his wife Perenelle made substantial charitable
donations to Parisian churches, hospitals, and foundations; the charnel house portal of the
Cemetery of the Innocents, which Flamel commissioned in 1407, still survives in part,
incorporated into the collections of the Musée de Cluny. No document produced during his
lifetime associates him with alchemical practice. The alchemical Flamel — the man who
achieved the philosopher's stone, transmuted lead into gold, attained physical immortality
or the prolongation of life, and wandered the earth for centuries in disguise — is an
entirely posthumous construction, the creation of early seventeenth-century forgers who
exploited his historical obscurity and his demonstrated wealth to fabricate an alchemical
legend of extraordinary staying power.</p>

<h2>The Construction of the Legend</h2>

<p>The alchemical biography of Flamel was published for the first time in the volume
<i>Livre des figures hiéroglyphiques</i> (<i>Book of Hieroglyphical Figures</i>) in Paris
in 1612, almost two centuries after Flamel's death. The text purports to be Flamel's own
account of how he obtained, during the 1350s, a mysterious ancient manuscript — described
as the <i>Livre d'Abraham le Juif</i>, the Book of Abraham the Jew — from a bookseller,
and how, after years of failed attempts to decipher its symbolic images, he undertook a
pilgrimage to Santiago de Compostela, where a learned Jewish convert explained the
manuscript's alchemical meaning to him. On his return to Paris, Flamel claims to have
performed the first successful transmutation of mercury into silver on 17 January 1382, and
the transmutation of mercury into gold on 25 April of the same year. The text is accompanied
by reproductions of the allegorical images that Flamel allegedly had painted on the fourth
arch of the Cemetery of the Innocents, which were themselves interpreted as a coded record
of the alchemical process.</p>

<p>The scholarly analysis of this legend was definitively conducted in the twentieth century.
Robert Halleux, in his study of medieval alchemical texts, established that the
<i>Livre des figures hiéroglyphiques</i> bears all the marks of early seventeenth-century
forgery: its vocabulary, its rhetorical conventions, and its organizational structure are
those of the alchemical literature of 1600–1620, not of the fourteenth century. Lawrence
Principe, in <i>The Secrets of Alchemy</i> (2013), has provided the most thorough and
accessible demolition of the Flamel legend in modern scholarship, demonstrating through
palaeographic, philological, and archival analysis that the pseudo-Flamel texts are
fabrications and that the historical Flamel's wealth had entirely conventional commercial
sources. Leah DeVun, in <i>Prophecy, Alchemy, and the End of Time</i> (2009), places the
Flamel legend within the broader context of late medieval and early modern alchemical
prophecy, showing how the figure of the alchemist-as-prophet was constructed and deployed
across the tradition.</p>

<h2>The Fabrication of Alchemical Authority</h2>

<p>The Flamel legend is historically significant not despite its inauthenticity but because
of it. It illustrates with unusual clarity a mechanism that operated throughout the alchemical
tradition: the fabrication of pseudonymous authority through the attribution of texts and
achievements to figures whose historical distance made verification impossible and whose
social prestige made attribution plausible. Flamel's genuine wealth — a demonstrable fact
attested by his charitable bequests and by notarial records — was precisely what made him
a productive locus for alchemical legend-making: his money had to come from somewhere, and
in a culture that took alchemical transmutation seriously as a possibility, the hypothesis
that a wealthy Parisian manuscript dealer had achieved the philosopher's stone required only
modest credulity to seem plausible. The pseudo-Flamel texts capitalized on this credulity
and systematically filled in the blank of Flamel's historical existence with a detailed
alchemical biography that was coherent, affectively compelling, and internally consistent —
the hallmarks of effective literary forgery.</p>

<p>The use of the <i>Livre d'Abraham le Juif</i> as the trigger of Flamel's supposed
alchemical illumination is particularly significant. The attribution of alchemical wisdom
to a Jewish source — specifically to a manuscript transmitted through the kabbalistic
tradition — reflects the early modern tendency to locate the origins of alchemical knowledge
in an ancient, non-Christian wisdom tradition of the kind associated with <a href="../persons/bernard_of_trevisan.html">Bernard of Treviso</a>
and with the broader myth of the <i>prisca sapientia</i>. The figure of Abraham the Jew
connects the Flamel legend to the tradition of pseudo-ancient Hebrew wisdom that was
simultaneously being exploited in Christian Kabbalistic literature and in the Rosicrucian
manifestos of the early seventeenth century. The timing of the first publication of the
<i>Livre des figures hiéroglyphiques</i> (1612) — in the same decade as the Rosicrucian
manifestos (1614–1616) — is unlikely to be coincidental; both phenomena reflect a surge of
interest in ancient occult wisdom and in the figure of the enlightened adept who possesses
it.</p>

<h2>Transmission and Cultural Reception</h2>

<p>Despite the scholarly demolition of the legend, the figure of Nicolas Flamel has shown
extraordinary cultural vitality. The pseudo-Flamel texts were reprinted throughout the
seventeenth and eighteenth centuries and were taken seriously by a number of significant
figures: Ethan Allen Hitchcock, whose <i>Remarks upon Alchemy and the Alchemists</i> (1857)
interpreted the alchemical literature as psychological allegory, discussed Flamel at length;
and various nineteenth-century occult movements incorporated the Flamel legend into their
accounts of the history of initiatic knowledge. In the twentieth century, Flamel became
a recurring figure in popular fiction and fantasy literature — most recently as a character
in the Harry Potter series — a cultural prominence that bears no relation to his historical
significance but testifies to the imaginative power of the alchemical legend as such.</p>

<p>The historiographical importance of the Flamel case extends beyond alchemical history.
It raises in acute form the problem of source criticism in the study of esotericism: how
are scholars to assess the authenticity of texts whose transmission involves systematic
fabrication, whose authority is grounded in claims that cannot be independently verified,
and whose historical impact has been enormous regardless of their authenticity? The Flamel
case is a test case for the methodology that Wouter Hanegraaff and his collaborators have
developed for the history of Western esotericism, which insists on rigorous historical
criticism while taking seriously the cultural and intellectual significance of traditions
whose truth-claims are not themselves the object of scholarly adjudication. The legend of
Flamel is, in this perspective, a genuinely important historical phenomenon — not because
Flamel achieved the philosopher's stone, but because the construction and reception of the
legend tells us something important about the social functions of alchemical authority, the
role of pseudo-ancient texts in legitimating esoteric claims, and the mechanisms by which
obscure historical individuals are transformed into mythological archetypes.</p>

<h2>Literature</h2>

<p>Principe, Lawrence M. <i>The Secrets of Alchemy</i>. Chicago: University of Chicago Press,
2013.</p>
<p>DeVun, Leah. <i>Prophecy, Alchemy, and the End of Time: John of Rupescissa in the Late
Middle Ages</i>. New York: Columbia University Press, 2009.</p>
<p>Halleux, Robert. <i>Les textes alchimiques</i>. Turnhout: Brepols, 1979.</p>
<p>Linden, Stanton J. <i>Darke Hierogliphicks: Alchemy in English Literature from Chaucer
to the Restoration</i>. Lexington: University Press of Kentucky, 1996.</p>
<p>Hanegraaff, Wouter J. (ed.). <i>Dictionary of Gnosis and Western Esotericism</i>. Leiden:
Brill, 2006.</p>
<p>Kahn, Didier. <i>Alchimie et Paracelsisme en France à la fin de la Renaissance
(1567–1625)</i>. Geneva: Droz, 2007.</p>
""".strip()

# ---------------------------------------------------------------------------
# Main update logic
# ---------------------------------------------------------------------------

ENTRIES = [
    ("giovanni_pico",    BIO_GIOVANNI_PICO),
    ("nicholas_of_cusa", BIO_NICHOLAS_OF_CUSA),
    ("jacob_boehme",     BIO_JACOB_BOEHME),
    ("kenelm_digby",     BIO_KENELM_DIGBY),
    ("nicolas_flamel",   BIO_NICOLAS_FLAMEL),
]

def main():
    conn = sqlite3.connect(str(DB_PATH))
    try:
        for person_id, bio_html in ENTRIES:
            conn.execute(
                "UPDATE persons SET bio_html = ? WHERE person_id = ?",
                (bio_html, person_id),
            )
            char_count = len(bio_html)
            print(f"  Updated {person_id:25s}  ({char_count:,} chars)")
        conn.commit()
        print("\nAll bio_html fields committed successfully.")
    finally:
        conn.close()

if __name__ == "__main__":
    main()
