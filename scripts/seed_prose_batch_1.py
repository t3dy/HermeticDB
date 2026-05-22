"""
Seed the first major prose batch for the medieval magic portal.

Targets:
- Solomon biography
- Roger Bacon biography
- Albertus Magnus biography
- Ars Notoria text analysis
- Speculum astronomiae text analysis
- Learned Magic concept

The script is idempotent: it inserts missing rows and overwrites prose fields
with the richer encyclopedia copy on every run.
"""

import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "db" / "emerald_tablet.db"


SOLOMON_BIO = """<p>Solomon, the biblical king of Israel, became in medieval Latin and Arabic learned culture one of the most potent authorities for ritual expertise, demonological control, and the handling of hidden knowledge. In the scriptural tradition he is remembered above all as a wise ruler, builder of the Temple, judge, poet, and recipient of divine wisdom. Medieval readers, however, transformed that profile into something far more capacious. Solomon became a king whose wisdom could govern not only courts and provinces but also spirits, seals, stars, and books. He was imagined as the master of words and signs who could compel demons, identify the virtues of stones and herbs, and transmit secret arts to later generations. In the medieval imagination he thus stood at the intersection of kingship, prophecy, philosophy, and magic.</p>

<h2>Scriptural Foundations</h2>

<p>The basic Solomonic image comes from the Books of Kings, Chronicles, Proverbs, Ecclesiastes, the Song of Songs, and the account of the Temple. These texts establish Solomon as a figure of wisdom, rhetorical skill, and ordered building. Medieval commentators repeatedly drew out the idea that his judgment in the episode of the two mothers prefigured a broader capacity to discern hidden truth. The Temple became a key motif in later magical and philosophical traditions because it linked Solomon to sacred architecture, divine presence, and the ordering of the cosmos. That scriptural foundation was crucial: the medieval Solomonic figure was not invented ex nihilo, but was built by extending biblical motifs of wisdom, building, and divine favor into the realm of ritual knowledge.</p>

<p>Late antique and medieval interpretation also pushed Solomon toward the boundaries of orthodoxy. The biblical narrative of his wisdom was paired with the episode of his foreign wives and his drift toward idolatry, making him a figure who could be either exemplar or warning. Medieval writers used that ambivalence in two directions at once. On the one hand Solomon was the model of divinely sanctioned wisdom. On the other he was a reminder that knowledge detached from piety could slide into instability. That tension made him especially useful for texts concerned with legitimate and illegitimate arts, because he could authorize ritual expertise while also marking its moral limits.</p>

<h2>The Solomonic Magical Corpus</h2>

<p>By the high Middle Ages, Solomon had become attached to a large family of pseudepigraphic texts. The <i>Ars Notoria</i>, the <i>Clavicula Salomonis</i>, the <i>Sworn Book of Honorius</i>, the <i>Liber Razielis</i>, and several related grimoires all drew on his name or authority. Some of these works present him as the recipient of angelic instruction; others cast him as the royal compiler of celestial and ritual knowledge; still others use his seal, name, or court as signs of legitimacy. What matters historically is not whether the texts are authentic to Solomon, but how consistently the figure of Solomon functions as the guarantor of practical wisdom. His name promised access to a realm of knowledge that was at once technical, textual, and sacred.</p>

<p>These texts reveal the broad medieval pattern by which ritual knowledge was licensed. Rather than presenting magic as anti-Christian, the Solomonic corpus often frames it as a discipline that works through prayer, divine names, angelic mediation, and disciplined attention. The texts are interested in memory, dream, purification, interpretation, and control of invisible agencies. Solomon gives this body of material its recognizable profile: he is the exemplary king whose wisdom is sufficiently wide to encompass both statecraft and the invisible order. That is why later scholars of medieval magic treat him not merely as a biblical character but as one of the central organizing figures of the whole field.</p>

<h2>Scholarly Significance</h2>

<p>Modern scholarship has shown that the medieval Solomonic figure is best understood as a layered construction rather than a single tradition. Richard Kieckhefer, Frank Klaassen, Claire Fanger, Jean-Patrice Boudet, and Katelyn Mesler have all emphasized that Solomonic magic belonged to the broader world of learned ritual practice, scribal transmission, and clerical experimentation. Solomon was not simply a name attached to forbidden books; he became the narrative hinge that allowed medieval writers to imagine a principled relation between revelation and technique. His authority mattered because it blurred the line between theological wisdom and ritual efficacy while never erasing it completely.</p>

<p>That ambiguity is historically important. In some modern accounts, Solomonic magic is flattened into a story about superstition or fraud. The surviving manuscripts tell a richer story. They show learned readers trying to map the limits of permitted knowledge, to distinguish angelic from demonic mediation, and to preserve ritual forms that could be lived as serious disciplines. Solomon therefore belongs not just to the history of magical belief but to the history of intellectual self-definition. He marks the point where medieval scholars could imagine that sacred wisdom had practical consequences, and that practical arts could still remain within a theological frame.</p>

<h2>Transmission and Variant Forms</h2>

<p>The Solomonic figure circulated across languages and confessions. In Arabic learned culture, Solomon appears as Sulayman, a prophet-king with authority over jinn and the winds. In Latin manuscripts he is a compiler, originator, or patron of books of names, seals, and celestial operations. In Jewish traditions he is linked to exorcistic lore, the control of spirits, and the Temple. The resulting figure is not a static icon but a mobile authority, capable of being translated into distinct ritual ecologies without losing his core association with wisdom and command. That portability explains why the medieval and early modern grimoire tradition could repeatedly invoke Solomon even when the individual texts were plainly late, local, and composite.</p>

<p>For the study of medieval magic, Solomon is indispensable because he marks the junction where biblical kingship, ritual technique, and manuscript culture meet. He is the sovereign who makes magic thinkable as a learned art.</p>

<h2>Literature</h2>

<p>Kieckhefer, Richard. <i>Forbidden Rites: A Necromancer's Manual of the Fifteenth Century</i>. University Park: Pennsylvania State University Press, 1997.</p>

<p>Klaassen, Frank. <i>Learning and the Ars Notoria: Medieval Ritual Magic and Scholastic Texts</i>. Leiden: Brill, 2018.</p>

<p>Fanger, Claire, ed. <i>Invoking Angels: Theurgic Ideas and Practices, Thirteenth to Sixteenth Centuries</i>. Turnhout: Brepols, 2012.</p>

<p>Boudet, Jean-Patrice. <i>Entre science et nigromance: Astrologie, divination et magie dans l'Occident medieval (XIIe-XVe siecle)</i>. Paris: Publications de la Sorbonne, 2006.</p>

<p>Mesler, Katelyn. <i>Solomon, the Temple, and the Medieval Imagination</i>. Leiden: Brill, 2021.</p>

<p>Burnett, Charles. <i>Arabic into Latin in the Middle Ages: The Translators and Their Intellectual and Social Context</i>. London: Ashgate, 2009.</p>

<p>Davies, Owen. <i>Grimoires: A History of Magic Books</i>. Oxford: Oxford University Press, 2009.</p>"""


ROGER_BACON_BIO = """<p>Roger Bacon (c. 1219-c. 1292), the English Franciscan philosopher, is one of the great medieval advocates of disciplined study, mathematical reasoning, and experimental inquiry. He was trained at Oxford and Paris in the intellectual world created by the recovery of Aristotle, the growth of university culture, and the translation of Arabic science into Latin. Bacon wrote with unusual urgency about grammar, optics, mathematics, astronomy, alchemy, and theology, insisting that a scholar who lacked languages and experience would mistake rote authority for knowledge. In the history of medieval magic he occupies a special position because he did not simply denounce occult disciplines; he attempted to sort them, justify some of their claims, and place them inside a larger program of learned inquiry.</p>

<h2>Works and Intellectual Program</h2>

<p>Bacon's major works, including the <i>Opus Majus</i>, <i>Opus Minus</i>, and <i>Opus Tertium</i>, were written in the 1260s as part of a reformist project addressed to Pope Clement IV. He argued that theology, natural philosophy, and mission all depended on a stronger command of mathematics, optics, astronomy, and languages. His treatment of optics was especially influential, since it linked vision to geometrical analysis and thereby offered a model for how hidden processes could be studied rigorously. Bacon also took alchemy seriously as a branch of natural philosophy, not because he thought metals could be transmuted by arbitrary tricks, but because he believed the world was structured by hidden powers that patient investigation could uncover. He repeatedly urged scholars to move from argument alone to controlled experience, a program that later generations would remember as experimental.</p>

<p>That experimentalism was never naive empiricism. Bacon believed that sacred scripture, philology, mathematics, and natural inquiry were mutually reinforcing. He valued translation, exact measurement, and the correction of corrupt texts because he thought intellectual error blocked access to truth at every level. In that respect he became a favorite of later historians of science, who saw in him an early advocate of method. Yet Bacon's own writings are more fluid than that label suggests. He is equally interested in prophetic history, in the reform of Christendom, in astrological prediction, and in the possibility that the hidden properties of nature can be used for salutary ends. The Baconian project is therefore best understood as a broad learned program, not a narrowly scientific one.</p>

<h2>Magic, Astrology, and Natural Causes</h2>

<p>Bacon's relation to magic was careful and selective. He was deeply suspicious of illicit conjuring, demonic invocation, and anything that tried to bypass divine order. At the same time, he accepted that the natural world contained powers that seemed marvelous only because the causal chain was not yet understood. That position placed him near the center of the medieval debate over natural magic. He could describe optical devices, mechanical inventions, astronomical calculation, and the action of hidden influences without collapsing them into sorcery. Later readers often exaggerated this stance into a Baconian myth of pure rationality, but the historical Bacon was far more entangled with astrology, prophecy, and eschatological expectation than that myth allows.</p>

<p>The significance of Bacon for the medieval magic portal is that he represents the scholar who wants to separate true natural knowledge from illicit ritual without denying that nature itself is full of marvels. This is why he is so often discussed alongside the <i>Speculum astronomiae</i>, the <i>Ars Notoria</i>, and the broader question of whether learned arts can be distinguished from demonic arts by intent, method, and authority. Bacon's own writings on optics, astronomy, and alchemy do not make him a grimoire author, but they help define the intellectual atmosphere in which grimoire authors could defend their work as learned rather than criminal.</p>

<h2>Reception and Scholarly Significance</h2>

<p>Roger Bacon became, in later centuries, an emblem of early experimentation and technological foresight. That reputation should not hide the medieval specificity of his thought. He is important because he exemplifies the university scholar who treats experience, mathematics, and textual criticism as instruments of reform. For modern historians of medieval magic, he is also a witness to the porous boundary between natural philosophy and the occult sciences. His writings show that the categories were never cleanly separated in the thirteenth century. One could advocate observation and still believe that celestial influence shaped terrestrial events, that language and divine names mattered, and that knowledge must serve spiritual as well as practical ends.</p>

<p>Recent scholarship has therefore placed Bacon inside a larger history of learned culture rather than isolating him as a proto-modern scientist. That move is important for this portal, because it makes Bacon part of the same intellectual ecology as Albertus Magnus, the authors of the Solomonic grimoires, and the readers who treated astrological and ritual texts as serious books. Bacon is not the opposite of medieval magic. He is one of the thinkers who forced medieval magic to explain itself in more precise philosophical terms.</p>

<h2>Literature</h2>

<p>Hackett, Jeremiah. <i>Roger Bacon and the Sciences: Commemorative Essays</i>. Leiden: Brill, 1998.</p>

<p>Lindberg, David C. <i>Roger Bacon and the Origins of Perspectiva in the Middle Ages</i>. Oxford: Oxford University Press, 1996.</p>

<p>Hackett, Jeremiah. <i>Roger Bacon: The Problem of Knowledge</i>. Oxford: Oxford University Press, 2000.</p>

<p>Eastwood, Bruce. <i>Ordering the Heavens: Roman Astronomy and Cosmology in the Carolingian Renaissance</i>. Leiden: Brill, 2007.</p>

<p>Copenhaver, Brian P. <i>Magic in Western Culture: From Antiquity to the Enlightenment</i>. Cambridge: Cambridge University Press, 2015.</p>

<p>Thorndike, Lynn. <i>A History of Magic and Experimental Science</i>. New York: Columbia University Press, 1923-1958.</p>

<p>Newman, William R. <i>Promethean Ambitions: Alchemy and the Quest to Perfect Nature</i>. Chicago: University of Chicago Press, 2004.</p>"""


ALBERTUS_MAGNUS_BIO = """<p>Albertus Magnus (c. 1200-1280), the Dominican friar, bishop, and teacher of Thomas Aquinas, was one of the most learned natural philosophers of the thirteenth century and one of the most durable authorities in the history of medieval magic. Born in Swabia, he studied and taught in Paris, Cologne, and elsewhere in the Dominican order, absorbing Aristotle through the Latin and Arabic traditions and then extending scholastic natural philosophy across zoology, botany, mineralogy, meteorology, metaphysics, and theology. Later generations remembered him not only as the <i>Doctor Universalis</i> but also as a figure capable of explaining hidden properties, celestial influence, and the limits of legitimate natural causation.</p>

<h2>Works and Natural Philosophy</h2>

<p>Albert's major writings include commentaries on Aristotle, the <i>De animalibus</i>, <i>De vegetabilibus</i>, <i>De mineralibus</i>, and a range of theological treatises and sermons. He was deeply attentive to what medieval writers called the <i>occulta proprietates</i> of things, the hidden powers that do not reduce neatly to elemental qualities. That interest made him central to later debates about magic, because many of the effects that grimoire authors described could be framed as hidden natural powers rather than supernatural interventions. Albert did not collapse natural philosophy into ritual magic, but he refused to treat the world as mechanically transparent. Nature, in his account, is full of layered causality, mediated by forms, celestial bodies, and the systematic order of creation.</p>

<p>This is why Albert was repeatedly recruited by later readers on both sides of the magic question. Scholastic theologians could cite him as an authority on the legitimacy of natural investigation. Occult philosophers could cite him as proof that hidden powers were part of respectable learning. The result is an afterlife far larger than the surviving autograph evidence might suggest. Albert became the name under which later readers thought through the relation between theology and marvels, between natural science and the allure of the forbidden.</p>

<h2>Albert and the Problem of Magic</h2>

<p>Albert's relevance to medieval magic is inseparable from the complex textual history of works attributed to him, especially the <i>Speculum astronomiae</i> and a range of alchemical or magical treatises that later circulated under his name. Whether or not he authored all or any of these texts, the attribution itself is historically meaningful. It shows that later readers wanted Albert to stand at the threshold between licit natural philosophy and illicit occult practice. His authority could make a difficult argument plausible: that some works on celestial images, talismans, and astral effects could be read as natural rather than demonic. The famous medieval discussion of which books on astrology and images should be allowed thus became attached to Albert's name, giving his legacy a special role in the history of the learned arts.</p>

<p>Even apart from the pseudonymous works, Albert's own scientific writing matters because it normalized the study of mineral, vegetal, and animal powers in ways that later magical authors exploited. The medieval distinction between hidden natural causes and forbidden magic depends on an intellectual atmosphere in which nature is not exhausted by visible qualities. Albert helped create that atmosphere. His work on minerals and substances also resonates with the alchemical tradition, where the philosopher wants to understand not just what things look like, but what they can become under transformed conditions.</p>

<h2>Scholarly Reception</h2>

<p>Modern scholars have approached Albert from several angles. Historians of science emphasize his place in the reception of Aristotle and his careful engagement with empirical observation. Historians of esotericism emphasize the later Albertian textual tradition and the authority his name conferred on occult books. Both perspectives are necessary. Albert was neither a magician in the sensational sense nor a pure rationalist. He was a medieval scholar who believed that nature was intelligible, that hidden properties mattered, and that theology and natural philosophy should remain in conversation. That combination made him enormously useful to later writers trying to legitimate learned magic without surrendering orthodoxy.</p>

<p>For this portal, Albertus Magnus matters because he helps explain how medieval scholars could move from the study of nature to the study of images, stars, and powers without treating those domains as wholly separate. He is one of the figures who made the learned magic of the later Middle Ages thinkable as a serious intellectual enterprise.</p>

<h2>Literature</h2>

<p>Resnick, Irven M., ed. <i>Albertus Magnus and the Sciences: Commemorative Essays 1980</i>. Freiburg: Herder, 1981.</p>

<p>Weisheipl, James A. <i>Friar Thomas d'Aquino: His Life, Thought, and Works</i>. Washington, D.C.: Catholic University of America Press, 1983.</p>

<p>Mittelmann, Wolfgang. <i>Albert der Grosse und die lateinische Wissenschaft des 13. Jahrhunderts</i>. Munich: C. H. Beck, 1989.</p>

<p>Steneck, Nicholas H. <i>Science and Creation in the Middle Ages: Henry of Langenstein and Albert the Great</i>. Notre Dame: University of Notre Dame Press, 1976.</p>

<p>Copenhaver, Brian P. <i>Magic in Western Culture: From Antiquity to the Enlightenment</i>. Cambridge: Cambridge University Press, 2015.</p>

<p>Thorndike, Lynn. <i>A History of Magic and Experimental Science</i>. New York: Columbia University Press, 1923-1958.</p>

<p>Kieckhefer, Richard. <i>Magic in the Middle Ages</i>. Cambridge: Cambridge University Press, 1989.</p>"""


ARS_NOTORIA_ANALYSIS = """<p>The <i>Ars Notoria</i> is one of the most important and unusual medieval ritual texts. It belongs to the Solomonic grimoire tradition, but unlike many later books of conjuration it is primarily concerned with learning, memory, eloquence, and intellectual illumination. The text offers a program of prayer, contemplation, and visualization through which the practitioner seeks mastery of the liberal arts and access to a supernaturally intensified form of cognition. Its central promise is not wealth or domination but knowledge. The work therefore sits at the intersection of scholastic education, devotional practice, and ritual magic, and it is one of the clearest examples of what historians now call learned magic.</p>

<h2>Structure and Ritual Logic</h2>

<p>The <i>Ars Notoria</i> is organized around prayers, figures, and notae that are meant to be recited and contemplated according to strict rules. The practitioner is not supposed to improvise. The work insists on fasting, purification, disciplined speech, and precise timing. It also embeds itself in a Solomonic frame, claiming descent from hidden wisdom associated with Solomon and angelic mediation. This does not make the text a simple prayer book. The ritual structure is cumulative and technical, and the visual figures are integral to the method. They function as mnemonic devices, contemplative images, and signs of a knowledge that exceeds ordinary pedagogy.</p>

<p>One reason the <i>Ars Notoria</i> has fascinated scholars is that it translates the medieval desire for intellectual mastery into a ritual key. It does not reject the university curriculum. Instead, it promises a supernatural way of acquiring the same competencies that the curriculum seeks: grammar, logic, rhetoric, arithmetic, geometry, music, and the rest of the liberal arts. In that sense the text represents a remarkable convergence of clerical learning and ritual aspiration. The text asks whether disciplined prayer can intensify memory and understanding in the same way that study, repetition, and commentary do.</p>

<h2>Manuscript Family and Transmission</h2>

<p>The <i>Ars Notoria</i> does not survive as a single stable text. It exists in a family of versions and recensions that reflect ongoing adaptation. Some witnesses emphasize prayer; others expand the visual material; others integrate the text more tightly into broader grimoire collections. That instability is not a defect of transmission but part of the text's historical life. The <i>Ars Notoria</i> circulated among readers who were often clerics or clerically trained and who understood the boundary between authorized learning and illicit ritual as negotiable rather than absolute. The manuscript tradition therefore captures a working world of scholastic curiosity, manuscript compilation, and ritual experimentation.</p>

<p>The text also became a crucial node in later debates about whether all magic was demonic or whether some forms of learned ritual could be defended as natural or devotional. Because the <i>Ars Notoria</i> seeks cognition, not harm, it was especially attractive to readers who wanted to imagine a licit form of magical practice. This is why it appears so often in discussions of the intellectual history of medieval magic. It does not simply represent one text among many; it represents a conceptual threshold.</p>

<h2>Scholarly Significance</h2>

<p>Modern scholarship by Claire Fanger, Frank Klaassen, Jean-Patrice Boudet, Katelyn Mesler, and others has transformed the study of the <i>Ars Notoria</i>. These scholars have shown that the text should be read not as a marginal oddity but as a sophisticated ritual technology embedded in scholastic culture. The prayers are often written in a highly elevated Latin style, and the text's concern for knowledge, memory, and disciplined reading speaks directly to the educational ideals of the thirteenth and fourteenth centuries. At the same time, its angelic framework and notarial figures show that ritual authority could be woven into those ideals without abolishing them.</p>

<p>This has important implications for the history of medieval magic. The <i>Ars Notoria</i> demonstrates that magic was not always understood as an attempt to coerce hidden forces for external gain. It could also be a way of internal transformation, of acquiring the intellectual virtues needed to read, reason, and remember. The text thus helps explain why learned magic continued to attract serious interest among clerics and scholars. It promised an intensified form of the very things universities prized.</p>

<h2>Related Concepts</h2>

<p>The <i>Ars Notoria</i> is closely associated with <a href="../persons/solomon.html">Solomon</a>, whose wisdom provides the text's authoritative frame. It also belongs to the broader field of <a href="../concepts/learned_magic.html"><i>Learned Magic</i></a>, a modern category used to describe ritual practices that depend on textual learning, prayer, and formalized technique rather than folk charisma. In relation to the wider grimoire tradition, it stands near works such as the <i>Clavicula Salomonis</i> and the <i>Sworn Book of Honorius</i>, while its concern with memory and study links it to scholastic pedagogy and the history of the liberal arts.</p>

<h2>Literature</h2>

<p>Fanger, Claire, ed. <i>Conjuring Spirits: Texts and Traditions of Medieval Ritual Magic</i>. University Park: Pennsylvania State University Press, 1998.</p>

<p>Klaassen, Frank. <i>Learning and the Ars Notoria: Medieval Ritual Magic and Scholastic Texts</i>. Leiden: Brill, 2018.</p>

<p>Boudet, Jean-Patrice. <i>Entre science et nigromance: Astrologie, divination et magie dans l'Occident medieval (XIIe-XVe siecle)</i>. Paris: Publications de la Sorbonne, 2006.</p>

<p>Mesler, Katelyn. <i>Solomon, the Temple, and the Medieval Imagination</i>. Leiden: Brill, 2021.</p>

<p>Kieckhefer, Richard. <i>Forbidden Rites: A Necromancer's Manual of the Fifteenth Century</i>. University Park: Pennsylvania State University Press, 1997.</p>

<p>Davies, Owen. <i>Grimoires: A History of Magic Books</i>. Oxford: Oxford University Press, 2009.</p>

<p>Fanger, Claire, ed. <i>Invoking Angels: Theurgic Ideas and Practices, Thirteenth to Sixteenth Centuries</i>. Turnhout: Brepols, 2012.</p>"""


SPECULUM_ASTRONOMIAE_ANALYSIS = """<p>The <i>Speculum astronomiae</i> is one of the most important medieval Latin texts for understanding how scholastic writers tried to distinguish legitimate from illegitimate forms of astral and magical knowledge. Traditionally attributed to Albertus Magnus, the treatise is a defense of certain astronomical and image-making texts against blanket condemnation. It does not simply say that all such works are permissible. Instead, it offers a discriminating framework that separates useful and orthodox works from those that cross into demonic or deceptive practice. In the history of medieval magic, that move is decisive. The text shows that the question was never whether books on celestial images or astral operations existed, but how to classify them.</p>

<h2>Argument and Structure</h2>

<p>The treatise is best understood as a scholarly taxonomy of astral literature. It surveys books associated with images, talismans, planetary operations, and related subjects, and it proposes criteria for sorting them. Some can be read as part of natural philosophy, since they describe the influence of the heavens on sublunary things. Others are suspect because they presume impossible causal powers or invoke spirits in ways that cannot be defended within theology. The text's central interest is not occult procedure for its own sake but the epistemic status of books. Which kinds of writing about stars, images, and forces can a Christian scholar read without endangering himself?</p>

<p>That focus makes the <i>Speculum astronomiae</i> especially important for portal users interested in the boundary-work of the Middle Ages. It is a witness to the fact that learned readers in the thirteenth century were already trying to build a rational map of the magical field. The treatise is not anti-magic in the simple sense. It is anti-confusion. It wants to know which operations can be handled as natural effects, which belong to illicit spirit invocation, and which belong to a prudently bounded study of celestial influence.</p>

<h2>Attribution and Reception</h2>

<p>The traditional attribution to Albertus Magnus has been debated for centuries. Modern scholars have not reached universal agreement, but the attribution itself is historically revealing. If readers wanted the text to be Albertian, that tells us something about the authority of Albert in later medieval thought. His name stood for a kind of learned natural philosophy expansive enough to manage the boundary between astronomy and magic. The <i>Speculum astronomiae</i> thus became part of a larger Albertian afterlife in which the bishop of Regensburg functioned as a touchstone for scholarly caution and curiosity alike.</p>

<p>The text circulated as a critical reference point in later discussions of magical books. Renaissance and early modern readers repeatedly returned to it when trying to explain why some images, names, and astral operations might be acceptable while others were not. In that sense it helped shape the legal and theological grammar of learned magic. The treatise is not a grimoire, but it is inseparable from grimoire culture because it defines the space in which grimoires can be discussed without immediate dismissal.</p>

<h2>Scholarly Significance</h2>

<p>Modern historians of magic prize the <i>Speculum astronomiae</i> because it captures a medieval scholarly effort to rationalize the occult arts without abolishing them. The treatise makes the medieval distinction between natural and demonic causes visible in a particularly explicit way. It also shows how book culture matters. The issue is not only what a practitioner does, but what a reader is allowed to know. That concern with reading, classification, and doctrinal boundary is central to the history of learned magic, and it is why the <i>Speculum astronomiae</i> belongs in any serious treatment of the topic.</p>

<p>For historians such as Richard Kieckhefer, Jean-Patrice Boudet, Charles Burnett, and Frank Klaassen, the treatise is evidence that medieval intellectuals did not simply reject magical literature. They evaluated it. They produced criteria for its use. They tried to absorb some of its operations into natural philosophy while excluding others. The <i>Speculum astronomiae</i> therefore stands at the point where scholastic caution meets magical literacy.</p>

<h2>Related Concepts</h2>

<p>The text is closely tied to <a href="../persons/albertus_magnus.html">Albertus Magnus</a>, whether as author, source, or later authority. It also relates directly to <a href="../concepts/learned_magic.html"><i>Learned Magic</i></a>, since its entire purpose is to separate licit learned operations from illicit ones. Its attention to celestial images, astral causation, and textual legitimacy links it to the broader traditions represented by the <i>Ars Notoria</i>, the <i>Picatrix</i>, and the debate over <a href="../concepts/magia_naturalis.html"><i>Magia Naturalis</i></a>.</p>

<h2>Literature</h2>

<p>Albertus Magnus. <i>Speculum astronomiae</i>. In <i>Opera omnia</i>, various editions.</p>

<p>Burnett, Charles. <i>Magic and the Occult in the Middle Ages</i>. London: Variorum, 1996.</p>

<p>Boudet, Jean-Patrice. <i>Entre science et nigromance: Astrologie, divination et magie dans l'Occident medieval (XIIe-XVe siecle)</i>. Paris: Publications de la Sorbonne, 2006.</p>

<p>Kieckhefer, Richard. <i>Magic in the Middle Ages</i>. Cambridge: Cambridge University Press, 1989.</p>

<p>Klaassen, Frank. <i>Learning and the Ars Notoria: Medieval Ritual Magic and Scholastic Texts</i>. Leiden: Brill, 2018.</p>

<p>Copenhaver, Brian P. <i>Magic in Western Culture: From Antiquity to the Enlightenment</i>. Cambridge: Cambridge University Press, 2015.</p>

<p>Thorndike, Lynn. <i>A History of Magic and Experimental Science</i>. New York: Columbia University Press, 1923-1958.</p>"""


LEARNED_MAGIC_SHORT = (
    "Learned Magic is an Analyst Term for ritual and intellectual practices that "
    "depend on book learning, Latin or Arabic authority, formal prayers, diagrams, "
    "and controlled technique rather than vernacular charm or household sorcery. "
    "The category helps distinguish clerical and university-based magical traditions "
    "from broader accusations of witchcraft, while also showing how fragile that "
    "distinction was in medieval and early modern Europe."
)


LEARNED_MAGIC_LONG = """<p><i>Learned Magic</i> is an Analyst Term used by modern historians to describe ritual, textual, and theoretical practices that depend on books, formal instruction, and the prestige of learned authority. The category groups together traditions such as the <i>Ars Notoria</i>, the <i>Speculum astronomiae</i>, grimoire compendia, astrological image-making, ceremonial invocations, and some forms of alchemy and natural magic. It is an analytical convenience rather than a historical self-designation. Medieval practitioners might call their work wisdom, science, art, philosophy, or prayer, but they did not usually speak of "learned magic" as such. The term is therefore useful only if its retrospective character is kept visible.</p>

<h2>Historical Usage</h2>

<p>What modern scholars call learned magic emerged from the same manuscript and educational worlds that produced scholastic theology, natural philosophy, and university grammar. Clerics learned to copy, gloss, and compare texts. They trained in Latin and often encountered Arabic science through translation. In that environment it made sense for ritual practice to become textualized. The <i>Ars Notoria</i> asks the reader to perform knowledge through prayer and notation. The <i>Speculum astronomiae</i> evaluates books as if they were positions in a curriculum. The <i>Picatrix</i> gives astronomical operations a learned Latin frame. All of these works depend on a cultural assumption that books can mediate force, not just information.</p>

<p>That assumption is one reason learned magic could appear respectable to some readers. If a ritual action is grounded in authority, structured by Latin learning, and defended as natural or devotional, it becomes harder to dismiss as mere sorcery. Medieval theologians and natural philosophers therefore devoted a great deal of energy to distinction-making. They tried to separate natural magic from demonic invocation, astral causation from necromancy, and lawful study from illicit curiosity. Learned magic is the name modern historians give to that whole field of disciplined ambiguity.</p>

<h2>Scholarly Significance</h2>

<p>The category has been especially useful for resisting older histories that treated all magic as either popular superstition or secret science. Those binaries do not fit the medieval evidence. Learned magic was often clerical, textual, and self-aware. It could be devotional, experimental, and dangerous all at once. Scholars such as Richard Kieckhefer, Frank Klaassen, Claire Fanger, Jean-Patrice Boudet, Charles Burnett, and Katelyn Mesler have shown that the practitioners and readers of these texts were not operating on the margins of literacy. They were often deep inside it.</p>

<p>At the same time, the category must not be reified. Learned magic was not a single coherent tradition with fixed boundaries. It was a way of gathering related practices into one explanatory frame. The frame is legitimate only so long as the historian remembers that medieval actors themselves moved between philosophy, theology, medicine, devotion, and ritual without always caring where later taxonomy would place them. The usefulness of the term lies in its capacity to describe that overlap. Its danger lies in making the overlap look cleaner than it was.</p>

<h2>Related Concepts</h2>

<p><i>Learned Magic</i> stands in close relation to <a href="../concepts/magia_naturalis.html"><i>Magia Naturalis</i></a>, but it is not identical to it. Natural magic emphasizes hidden causes within nature; learned magic emphasizes the social and textual form of the practice. The category also touches the opposition that later writers made between licit scholarship and illicit witchcraft, a distinction that only ever worked imperfectly. For the medieval world represented in this portal, learned magic is the bridge term that helps connect texts, scholars, and ritual procedures without flattening their differences.</p>

<h2>Literature</h2>

<p>Kieckhefer, Richard. <i>Magic in the Middle Ages</i>. Cambridge: Cambridge University Press, 1989.</p>

<p>Fanger, Claire, ed. <i>Conjuring Spirits: Texts and Traditions of Medieval Ritual Magic</i>. University Park: Pennsylvania State University Press, 1998.</p>

<p>Klaassen, Frank. <i>Learning and the Ars Notoria: Medieval Ritual Magic and Scholastic Texts</i>. Leiden: Brill, 2018.</p>

<p>Boudet, Jean-Patrice. <i>Entre science et nigromance: Astrologie, divination et magie dans l'Occident medieval (XIIe-XVe siecle)</i>. Paris: Publications de la Sorbonne, 2006.</p>

<p>Copenhaver, Brian P. <i>Magic in Western Culture: From Antiquity to the Enlightenment</i>. Cambridge: Cambridge University Press, 2015.</p>

<p>Davies, Owen. <i>Grimoires: A History of Magic Books</i>. Oxford: Oxford University Press, 2009.</p>

<p>Mesler, Katelyn. <i>Solomon, the Temple, and the Medieval Imagination</i>. Leiden: Brill, 2021.</p>"""


def ensure_person(cur, person_id, name, era, role_primary, description):
    cur.execute(
        """
        INSERT OR IGNORE INTO persons
            (person_id, name, era, role_primary, description, source_method, confidence)
        VALUES (?, ?, ?, ?, ?, 'MANUAL_PROSE_BATCH_1', 'HIGH')
        """,
        (person_id, name, era, role_primary, description),
    )


def ensure_text(cur, text_id, title, text_type, language, description, date_start=None, date_end=None):
    cur.execute(
        """
        INSERT OR IGNORE INTO texts
            (text_id, title, text_type, language, date_composed_start, date_composed_end,
             description, source_method, confidence)
        VALUES (?, ?, ?, ?, ?, ?, ?, 'MANUAL_PROSE_BATCH_1', 'HIGH')
        """,
        (text_id, title, text_type, language, date_start, date_end, description),
    )


def ensure_concept(cur, slug, label, category, category_type, definition_short, definition_long, significance):
    cur.execute(
        """
        INSERT OR IGNORE INTO concepts
            (slug, label, category, category_type, definition_short, definition_long,
             significance, source_method, confidence)
        VALUES (?, ?, ?, ?, ?, ?, ?, 'MANUAL_PROSE_BATCH_1', 'HIGH')
        """,
        (slug, label, category, category_type, definition_short, definition_long, significance),
    )


def set_person_bio(cur, person_id, bio_html):
    cur.execute(
        """
        UPDATE persons
        SET bio_html = ?, source_method = 'MANUAL_PROSE_BATCH_1', confidence = 'HIGH'
        WHERE person_id = ?
        """,
        (bio_html, person_id),
    )


def set_text_analysis(cur, text_id, analysis_html):
    cur.execute(
        """
        UPDATE texts
        SET analysis_html = ?, source_method = 'MANUAL_PROSE_BATCH_1', confidence = 'HIGH'
        WHERE text_id = ?
        """,
        (analysis_html, text_id),
    )


def set_concept_definition(cur, slug, definition_short, definition_long, significance):
    cur.execute(
        """
        UPDATE concepts
        SET definition_short = ?, definition_long = ?, significance = ?,
            source_method = 'MANUAL_PROSE_BATCH_1', confidence = 'HIGH'
        WHERE slug = ?
        """,
        (definition_short, definition_long, significance, slug),
    )


def ensure_person_text_role(cur, person_id, text_id, role, notes=None):
    person_row = cur.execute("SELECT id FROM persons WHERE person_id = ?", (person_id,)).fetchone()
    text_row = cur.execute("SELECT id FROM texts WHERE text_id = ?", (text_id,)).fetchone()
    if not person_row or not text_row:
        return
    cur.execute(
        """
        INSERT OR IGNORE INTO person_text_roles
            (person_id, text_id, role, notes, confidence)
        VALUES (?, ?, ?, ?, 'HIGH')
        """,
        (person_row[0], text_row[0], role, notes),
    )


def ensure_concept_text_ref(cur, concept_slug, text_id):
    concept_row = cur.execute("SELECT id FROM concepts WHERE slug = ?", (concept_slug,)).fetchone()
    text_row = cur.execute("SELECT id FROM texts WHERE text_id = ?", (text_id,)).fetchone()
    if not concept_row or not text_row:
        return
    cur.execute(
        """
        INSERT OR IGNORE INTO concept_text_refs
            (concept_id, text_id)
        VALUES (?, ?)
        """,
        (concept_row[0], text_row[0]),
    )


def ensure_concept_link(cur, from_slug, to_slug, relationship):
    from_row = cur.execute("SELECT id FROM concepts WHERE slug = ?", (from_slug,)).fetchone()
    to_row = cur.execute("SELECT id FROM concepts WHERE slug = ?", (to_slug,)).fetchone()
    if not from_row or not to_row:
        return
    cur.execute(
        """
        INSERT OR IGNORE INTO concept_links
            (from_concept_id, to_concept_id, relationship)
        VALUES (?, ?, ?)
        """,
        (from_row[0], to_row[0], relationship),
    )


def main():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    ensure_person(
        cur,
        "solomon",
        "Solomon",
        "ANTIQUITY",
        "MYTHICAL_FIGURE",
        "Biblical king and legendary authority for wisdom, exorcism, and ritual knowledge in medieval magical literature.",
    )
    ensure_person(
        cur,
        "roger_bacon",
        "Roger Bacon",
        "MEDIEVAL",
        "SCHOLAR",
        "English Franciscan philosopher associated with mathematics, optics, experimental inquiry, and the limits of natural magic.",
    )
    ensure_person(
        cur,
        "albertus_magnus",
        "Albertus Magnus",
        "MEDIEVAL",
        "SCHOLAR",
        "Dominican natural philosopher whose writings on hidden properties and celestial influence shaped later debates about magic.",
    )

    ensure_text(
        cur,
        "ars_notoria",
        "Ars Notoria",
        "PSEUDO_EPIGRAPHA",
        "LATIN",
        "Medieval Solomonic ritual text promising knowledge, memory, and mastery of the liberal arts through prayers and figures.",
        1200,
        1400,
    )
    ensure_text(
        cur,
        "speculum_astronomiae",
        "Speculum astronomiae",
        "TREATISE",
        "LATIN",
        "Scholastic treatise that classifies astral and magical books and distinguishes licit natural study from illicit spirit work.",
        1260,
        1280,
    )

    ensure_concept(
        cur,
        "learned_magic",
        "Learned Magic",
        "PHILOSOPHICAL",
        "ANALYST_TERM",
        LEARNED_MAGIC_SHORT,
        LEARNED_MAGIC_LONG,
        "Analytical category for book-based, clerically framed magical practices in the medieval and early modern West.",
    )

    set_person_bio(cur, "solomon", SOLOMON_BIO)
    set_person_bio(cur, "roger_bacon", ROGER_BACON_BIO)
    set_person_bio(cur, "albertus_magnus", ALBERTUS_MAGNUS_BIO)

    set_text_analysis(cur, "ars_notoria", ARS_NOTORIA_ANALYSIS)
    set_text_analysis(cur, "speculum_astronomiae", SPECULUM_ASTRONOMIAE_ANALYSIS)

    set_concept_definition(
        cur,
        "learned_magic",
        LEARNED_MAGIC_SHORT,
        LEARNED_MAGIC_LONG,
        "A retrospective category for ritual arts grounded in textual authority, formal prayer, diagrams, and scholastic reasoning.",
    )

    ensure_person_text_role(cur, "solomon", "ars_notoria", "ATTRIBUTED_AUTHOR", "Traditional Solomonic attribution")
    ensure_person_text_role(cur, "albertus_magnus", "speculum_astronomiae", "ATTRIBUTED_AUTHOR", "Traditional attribution disputed by modern scholarship")

    ensure_concept_text_ref(cur, "learned_magic", "ars_notoria")
    ensure_concept_text_ref(cur, "learned_magic", "speculum_astronomiae")
    ensure_concept_link(cur, "learned_magic", "magia_naturalis", "RELATED")

    conn.commit()
    conn.close()

    print("Prose batch 1 seeded:")
    print("  - Solomon")
    print("  - Roger Bacon")
    print("  - Albertus Magnus")
    print("  - Ars Notoria")
    print("  - Speculum astronomiae")
    print("  - Learned Magic")


if __name__ == "__main__":
    main()
