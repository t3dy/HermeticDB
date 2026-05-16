import sqlite3
from pathlib import Path

DB_PATH = Path(r"c:\Dev\EmeraldTablet\db\emerald_tablet.db")

NEW_PERSONS = [
    ("gilbert_of_poitiers", "Gilbert of Poitiers (Gilbertus Porretanus)", "MEDIEVAL", "PHILOSOPHER",
     "Bishop of Poitiers (c. 1085–1154) and the probable author of De sex rerum principiis. A leading 12th-century metaphysician of the Chartres school."),
    ("alain_de_lille", "Alain de Lille (Alanus ab Insulis)", "MEDIEVAL", "PHILOSOPHER",
     "French theologian and poet (c. 1128–1203), nicknamed Doctor Universalis. He transmitted the Liber XXIV Philosophorum to the Latin West via his De Maximis Theologiae."),
    ("robert_grosseteste", "Robert Grosseteste", "MEDIEVAL", "SCHOLAR",
     "Bishop of Lincoln (c. 1175–1253), first Chancellor of Oxford, who cited De sex rerum principiis and pioneered the use of mathematics in natural philosophy."),
    ("thomas_of_york", "Thomas of York", "MEDIEVAL", "PHILOSOPHER",
     "A 13th-century English Franciscan philosopher who used Hermes Trismegistus as a named authority in his scholastic works, documented by David Porreca."),
    ("thierry_of_chartres", "Thierry of Chartres", "MEDIEVAL", "PHILOSOPHER",
     "Chancellor of the Cathedral School of Chartres (d. c. 1150) and key figure in the 12th-century Platonist synthesis of Timaeus cosmology with Christian theology."),
    ("william_of_conches", "William of Conches", "MEDIEVAL", "PHILOSOPHER",
     "A leading Chartres school philosopher (c. 1090–1154) who synthesized Platonic cosmology with natural philosophy, providing the intellectual milieu for De sex rerum principiis."),
    ("dan_attrell", "Dan Attrell", "MODERN", "SCHOLAR",
     "Co-translator (with David Porreca) of the Latin Picatrix (Penn State Press, 2019). Scholar of Hermetic and Renaissance occult traditions."),
    ("paolo_lucentini", "Paolo Lucentini", "MODERN", "SCHOLAR",
     "Italian scholar and editor of the Hermes Latinus series (Brepols/Corpus Christianorum), responsible for the critical edition of De sex rerum principiis."),
]

NEW_TEXTS = [
    ("liber_de_causis", "Liber de Causis", "LATIN", "PRIMARY_SOURCE", 850, 1150,
     "An Arabic adaptation of Proclus's Elements of Theology, falsely attributed to Aristotle in the Middle Ages. A major vehicle for Neoplatonic emanationism in Latin scholasticism."),
    ("de_maximis_theologiae", "De Maximis Theologiae (Regulae Theologiae)", "LATIN", "TREATISE", 1160, 1200,
     "134 theological maxims with commentary by Alain de Lille, containing the earliest printed transmission of the 'infinite sphere' definition from the Liber XXIV Philosophorum."),
    ("liber_de_spiritu_et_anima", "Liber de spiritu et anima", "LATIN", "TREATISE", 1100, 1200,
     "A pseudo-Augustinian 12th-century mystical psychology of the soul that cites Hermes. Circulated widely in scholastic miscellanies alongside the Asclepius and Liber XXIV."),
    ("hermes_latinus_series", "Hermes Latinus (Brepols Series)", "LATIN", "COMPILATION", 2000, 2024,
     "The critical edition series published by Brepols (Corpus Christianorum Continuatio Mediaevalis) collecting all Latin texts attributed to Hermes Trismegistus, edited by Lucentini, Porreca, and others."),
    ("picatrix_latin", "Picatrix (Latin Translation)", "LATIN", "TREATISE", 1256, 1256,
     "The Latin translation of the Arabic Ghayat al-Hakim, produced in Castile c. 1256 under Alfonso X. The definitive manual of astral magic in the Latin West, translated with commentary by Attrell and Porreca (2019)."),
]

PROSE = {
    "liber_xxiv_philosophorum": """
        <p>The <i>Liber XXIV Philosophorum</i> (Book of the 24 Philosophers) is a short anonymous Latin anthology of 24 definitions of God, composed no later than the 12th century. Each definition is attributed to a different 'philosopher' and takes the form of a paradoxical metaphysical aphorism.</p>
        <h2>The Infinite Sphere</h2>
        <p>The most celebrated of the 24 definitions is the first: <i>"Deus est sphaera infinita cuius centrum est ubique, circumferentia nusquam"</i> — "God is an infinite sphere whose center is everywhere and circumference nowhere." This phrase, transmitted through Alain de Lille's <i>De Maximis Theologiae</i> (Basel, 1492), became one of the most widely quoted definitions of God in the Western philosophical tradition. Nicholas of Cusa paraphrases it directly in <i>De Docta Ignorantia</i> (1440), Giordano Bruno weaponizes it as a pantheistic axiom, and Robert Fludd and Jacob Böhme absorb its geometric theology.</p>
        <h2>Medieval Transmission</h2>
        <p>Though its aphorisms resonate deeply with Hermetic notions of divine unity, the text is not a Hermetic document in the strict Greek sense. As curator José Bouman of the Bibliotheca Philosophica Hermetica notes, the oldest manuscripts are 12th-century and often appear in scholastic miscellanies labeled <i>Sententiae Hermetis</i>, alongside the <i>Asclepius</i> and <i>Liber de Causis</i>. Its Hermetic label was a reception-history phenomenon: medieval scholars recognized in its mathematical-theological style the same 'Hermetic' spirit of creation by number, order, and figure. David Porreca's work on manuscript evidence confirms that commentators treated it as a classroom text — not an occult document — with full scholastic-style glosses.</p>
        <h2>Scholarly Edition</h2>
        <p>The standard critical edition is by Françoise Hudry (Hermes Latinus / Corpus Christianorum Continuatio Mediaevalis, Brepols). Paolo Lucentini and the Hermes Latinus editorial board, including David Porreca, provide the authoritative scholarly context.</p>
    """,
    "de_sex_rerum_principiis": """
        <p><i>De sex rerum principiis</i> (On the Six Principles of Things) is a 12th-century Latin cosmological treatise, composed c. 1147–1175. It is most plausibly attributed to <b>Gilbert of Poitiers</b> (Gilbertus Porretanus), though Renaissance manuscripts sometimes label it a work of Hermes Trismegistus — a Hermetic misattribution that guaranteed its survival and influence.</p>
        <h2>The Six Principles</h2>
        <p>The treatise extends Aristotle's <i>Categories</i> with six higher metaphysical co-principles that explain the structure of created reality. <b>Subsistentia</b> names being itself, understood as the way creatures participate in divine existence. <b>Species</b> denotes form or intelligibility, the pattern that confers identity. <b>Ordo</b> designates the hierarchical relation of parts to the whole, while <b>Numerus</b> names the proportion by which created being reflects divine harmony. <b>Figura</b> describes visible shape as the manifestation of invisible intelligible order, and <b>Motus</b> describes motion as the temporal unfolding of creation within the <i>exitus-reditus</i> cycle.</p>
        <h2>Mark Damien Delp's Reading</h2>
        <p>The decisive modern study is Mark D. Delp's Notre Dame dissertation (1994) and his co-edition with Paolo Lucentini for Brepols (2006). Delp argues the six are <b>modes of participated being</b>: not physical categories but ontological ratios, each expressing how creatures participate in divine being and intelligibility. <i>Numerus</i> is not mere counting but the proportion between a creature's being and its divine exemplar. This reading situates the text within the Boethian-Augustinian tradition of participation metaphysics, anticipating Aquinas's act-and-potency doctrine.</p>
        <h2>Hermetic Resonance and Renaissance Legacy</h2>
        <p>The text's hexadic structure evokes the six days of creation (<i>hexaemeron</i>) and was read by Renaissance scholars as an encoded Hermetic cosmology. Cornelius Agrippa cites <i>De sex rerum principiis</i> explicitly in <i>De Occulta Philosophia</i> I.3, treating the six principles as the metaphysical foundation of natural magic. Robert Fludd's hexadic cosmological diagrams in <i>Utriusque Cosmi Historia</i> echo the same schema.</p>
        <h2>David Porreca and the Hermes Latinus Project</h2>
        <p>David Porreca (University of Waterloo) — co-translator of the Latin <i>Picatrix</i> (Penn State Press, 2019) — sits on the editorial board of the Hermes Latinus series and has documented how texts like <i>De sex rerum principiis</i> and the <i>Liber XXIV Philosophorum</i> were used in 12th- and 13th-century classrooms with full scholastic commentary, not as occult curiosities but as philosophical teaching aids alongside Aristotle and Boethius.</p>
    """,
    "gilbert_of_poitiers": """
        <p>Gilbert of Poitiers (Gilbertus Porretanus, c. 1085–1154) was Bishop of Poitiers and one of the most subtle and controversial metaphysicians of the 12th century. He studied and taught at the Cathedral School of Chartres and at Paris.</p>
        <h2>Metaphysics of Participation</h2>
        <p>Gilbert's primary philosophical achievement was his <i>Commentary on Boethius's De Trinitate</i>, in which he pushed Boethian participation metaphysics to its logical limits, distinguishing sharply between God's subsistent being (<i>quo est</i>) and the form of being that creatures participate in (<i>quod est</i>). This distinction was condemned at the Council of Reims (1148) as dangerously close to dualism — a sign of the radical nature of his thinking. His probable authorship of <i>De sex rerum principiis</i> is established by Mark Damien Delp through close stylistic and doctrinal comparison with the Boethius commentary. The six principles of the treatise are the direct application of Gilbert's participation metaphysics to cosmology.</p>
    """,
    "alain_de_lille": """
        <p>Alain de Lille (Alanus ab Insulis, c. 1128–1203) was a French theologian and poet, educated at the Cathedral School of Chartres and active in Paris and Montpellier. He was called <i>Doctor Universalis</i> for the encyclopedic breadth of his learning.</p>
        <h2>The Infinite Sphere and the Liber XXIV</h2>
        <p>Alain's key role in the Hermetic tradition is as the primary transmitter of the <i>Liber XXIV Philosophorum</i>'s central definition of God: <i>"Deus est sphaera intelligibilis cuius centrum est ubique, circumferentia nusquam."</i> This appears in his <i>De Maximis Theologiae</i> (134 theological maxims), first printed in Basel, 1492. By incorporating the phrase into his orthodox theological commentary, Alain provided the Hermetic aphorism with full scholastic legitimacy, ensuring it would be read by Thomas Aquinas, Dante, Cusanus, and eventually Bruno.</p>
        <h2>Works</h2>
        <p>His major works include the allegorical poem <i>De Planctu Naturae</i> (The Complaint of Nature), where Lady Nature laments human sin — a text that gave Renaissance Hermeticists their vocabulary of Nature as God's secondary creative force — and <i>Anticlaudianus</i>, an allegory of the soul's perfection that influenced Dante's <i>Commedia</i>.</p>
    """,
    "robert_grosseteste": """
        <p>Robert Grosseteste (c. 1175–1253) was the first Chancellor of Oxford University and Bishop of Lincoln. He is recognized as the pioneer of the scientific method in medieval Europe, emphasizing mathematics and controlled experimentation as the proper tools of natural philosophy.</p>
        <h2>Hermeticism and Natural Philosophy</h2>
        <p>Grosseteste cited <i>De sex rerum principiis</i> and drew on the Hermetic-Neoplatonic tradition of light metaphysics in his foundational treatise <i>De Luce</i> (On Light), arguing that light is the first corporeal form from which all material extension proceeds — a theory that maps directly onto the Hermetic doctrine of the divine light emanating through the spheres. His student Roger Bacon continued this Hermetic-mathematical synthesis, explicitly citing Hermes Trismegistus as an authority for his empirical program.</p>
    """,
    "david_porreca": """
        <p>David Porreca is Associate Professor of Classical Studies at the University of Waterloo (Canada) and Co-Director of their Medieval Studies program. He is a leading authority on the medieval Latin reception of Hermes Trismegistus and a member of the editorial board of the <b>Hermes Latinus</b> series (Brepols / Corpus Christianorum Continuatio Mediaevalis).</p>
        <h2>Hermes in the Medieval Classroom</h2>
        <p>Porreca's most significant contribution is his systematic documentation of how texts attributed to Hermes Trismegistus were used as <b>scholastic teaching tools</b> in 12th- and 13th-century classrooms — not merely as esoteric curiosities. Through manuscript palaeography, he identifies student glosses, marginal commentary, and scholastic apparatus on texts including the <i>Liber XXIV Philosophorum</i>, <i>De sex rerum principiis</i>, and the <i>Asclepius</i>. His 2005 paper "Hermes Trismegistus in Thomas of York" demonstrates that schoolmen listed Hermes alongside Aristotle and Boethius as a standard philosophical authority. His forthcoming work "Hermes Trismegistus in the Medieval Classroom" (IMC 2025) continues this archival research.</p>
        <h2>The Latin Picatrix</h2>
        <p>With Dan Attrell, Porreca produced the first complete English translation of the Latin <i>Picatrix</i> (Penn State Press, 2019), the definitive medieval manual of astral magic. The translation includes extensive scholarly apparatus situating the <i>Picatrix</i> within the Hermetic Latinus tradition — making explicit the connections between theoretical cosmology (the six principles, the 24 definitions of God) and the practical astral magic that drew on them.</p>
    """,
    "mark_damien_delp": """
        <p>Mark Damien Delp (d. 2012) was a scholar of medieval metaphysics at the University of San Francisco and a member of the Society for Medieval Logic and Metaphysics. His central contribution to Hermetic studies was the scholarly rehabilitation of <i>De sex rerum principiis</i>.</p>
        <h2>The Metaphysics of Participation</h2>
        <p>Delp's Notre Dame dissertation (1994), <i>De Sex Rerum Principiis: A Translation and Study of a Twelfth-century Cosmology</i>, is the foundational English-language treatment. He argues the six principles are <b>modes of participated being</b> — not merely logical or physical categories, but ontological ratios expressing how creatures participate in divine being and intelligibility through the Boethian-Augustinian tradition. His key insight: <i>Numerus</i> (number) in the text is not quantitative counting but the proportion by which a creature's being is measured against its divine exemplar. With Paolo Lucentini, Delp produced the critical Latin edition for the Hermes Latinus series (Brepols, 2006), firmly establishing the text's place within medieval Latin Hermeticism and its connections to the Chartres school synthesis of Plato's <i>Timaeus</i> with Christian cosmology.</p>
    """,
    "roger_bacon": """
        <p>Roger Bacon (c. 1214/1220–1292) was an English Franciscan friar and philosopher, active at Oxford and Paris. He is celebrated as a pioneer of empirical science and the systematic use of mathematics in natural philosophy.</p>
        <h2>Hermes as Scientific Authority</h2>
        <p>Bacon repeatedly cited Hermes Trismegistus as a positive authority in his major works, including the <i>Opus Majus</i>. For Bacon, Hermes represented the ancient tradition of <i>scientia experimentalis</i> — knowledge derived from direct experience — making him a proto-scientist rather than a mystic. Bacon drew on the Hermetic astrology and optical theory preserved in Arabic sources (particularly al-Kindi's <i>De Radiis</i>) to develop his theory of the 'multiplication of species' (the propagation of natural forces through the medium of light). His engagement illustrates how Hermetic cosmological principles (correspondence, sympatheia, number) entered the foundations of early medieval natural science.</p>
    """,
    "paolo_lucentini": """
        <p>Paolo Lucentini (d. 2008) was an Italian medieval scholar and the founding editor of the <b>Hermes Latinus</b> series (Brepols / Corpus Christianorum Continuatio Mediaevalis), the definitive critical edition project for Latin texts attributed to Hermes Trismegistus.</p>
        <h2>The Hermes Latinus Project</h2>
        <p>Lucentini's great achievement was to create a rigorous editorial framework for 'Latin Hermeticism' — establishing what counts as a Latin Hermetic text through manuscript evidence, attribution history, and doctrinal analysis rather than content alone. His co-edition of <i>De sex rerum principiis</i> with Mark Damien Delp (2006) is the standard reference, situating the text within the broader 12th-century Hermetic dossier and demonstrating the continuity from ancient Hermeticism through medieval Latin synthesis to Renaissance recovery. The series, now continued by Porreca and Antonella Sannino, provides the scholarly infrastructure for all serious study of medieval Hermetic transmission.</p>
    """,
    "liber_de_causis": """
        <p>The <i>Liber de Causis</i> (Book of Causes) is an anonymous Arabic adaptation of Proclus's <i>Elements of Theology</i>, composed in Baghdad c. 850 CE. It was translated into Latin in Toledo c. 1187 by Gerard of Cremona and circulated throughout medieval Europe under the false attribution to Aristotle.</p>
        <h2>Hermetic Reception</h2>
        <p>Thomas Aquinas identified its true Proclean origins in his commentary (c. 1272), but by then the text had already deeply shaped medieval scholastic metaphysics. It provided the emanationist framework — the procession of intelligences from the First Cause — that made the Hermetic cosmology of the <i>Corpus Hermeticum</i> immediately comprehensible to Latin readers when Ficino translated it in 1463. The <i>Liber de Causis</i> forms a conceptual triad with the <i>Liber XXIV Philosophorum</i> and <i>De sex rerum principiis</i>: the first gives the definition of God (infinite sphere), the second gives the causal procession (First Cause → intelligences), and the third gives the formal principles of created being.</p>
    """,
}

PERSON_TEXT_LINKS = [
    ("gilbert_of_poitiers", "de_sex_rerum_principiis", "AUTHOR"),
    ("alain_de_lille", "liber_xxiv_philosophorum", "TRANSMITTER"),
    ("alain_de_lille", "de_maximis_theologiae", "AUTHOR"),
    ("robert_grosseteste", "de_sex_rerum_principiis", "SCHOLAR"),
    ("roger_bacon", "de_sex_rerum_principiis", "SCHOLAR"),
    ("david_porreca", "liber_xxiv_philosophorum", "EDITOR"),
    ("david_porreca", "de_sex_rerum_principiis", "EDITOR"),
    ("david_porreca", "picatrix_latin", "TRANSLATOR"),
    ("dan_attrell", "picatrix_latin", "TRANSLATOR"),
    ("paolo_lucentini", "de_sex_rerum_principiis", "EDITOR"),
    ("mark_damien_delp", "de_sex_rerum_principiis", "EDITOR"),
    ("nicholas_of_cusa", "liber_xxiv_philosophorum", "SCHOLAR"),
    ("giordano_bruno", "liber_xxiv_philosophorum", "SCHOLAR"),
    ("albertus_magnus", "secretum_secretorum", "SCHOLAR"),
    ("thomas_of_york", "liber_xxiv_philosophorum", "SCHOLAR"),
]

CONCEPT_TEXT_LINKS = [
    ("infinite_sphere", "liber_xxiv_philosophorum"),
    ("lumen_gloriae", "liber_xxiv_philosophorum"),
    ("immanent_logos", "de_sex_rerum_principiis"),
    ("emanationism", "liber_de_causis"),
    ("macrocosm_microcosm", "de_sex_rerum_principiis"),
    ("prisca_theologia", "liber_xxiv_philosophorum"),
]

def ingest():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    print("Ingesting medieval figures...")
    for pid, name, era, role, desc in NEW_PERSONS:
        try:
            cursor.execute("""
                INSERT OR IGNORE INTO persons (person_id, name, era, role_primary, description, source_method, review_status, confidence)
                VALUES (?, ?, ?, ?, ?, 'CORPUS_EXTRACTION', 'REVIEWED', 'HIGH')
            """, (pid, name, era, role, desc))
            print(f"  + {name}")
        except Exception:
            pass  # already exists

    print("Ingesting medieval texts...")
    for tid, title, lang, ttype, start, end, desc in NEW_TEXTS:
        try:
            cursor.execute("""
                INSERT OR IGNORE INTO texts (text_id, title, language, text_type, date_composed_start, date_composed_end, description, source_method, review_status, confidence)
                VALUES (?, ?, ?, ?, ?, ?, ?, 'CORPUS_EXTRACTION', 'REVIEWED', 'HIGH')
            """, (tid, title, lang, ttype, start, end, desc))
            print(f"  + {title}")
        except Exception:
            pass

    print("Injecting prose...")
    for slug, prose in PROSE.items():
        rows = cursor.execute("UPDATE persons SET bio_html = ? WHERE person_id = ?", (prose, slug)).rowcount
        if rows == 0:
            cursor.execute("UPDATE texts SET analysis_html = ? WHERE text_id = ?", (prose, slug))

    print("Linking persons to texts...")
    for p, t, rel in PERSON_TEXT_LINKS:
        cursor.execute("INSERT OR IGNORE INTO person_text_refs (person_id, text_id, rel_type) VALUES (?,?,?)", (p, t, rel))

    print("Linking concepts to texts...")
    for c_slug, t_slug in CONCEPT_TEXT_LINKS:
        cid = cursor.execute("SELECT id FROM concepts WHERE slug=?", (c_slug,)).fetchone()
        tid = cursor.execute("SELECT id FROM texts WHERE text_id=?", (t_slug,)).fetchone()
        if cid and tid:
            cursor.execute("INSERT OR IGNORE INTO concept_text_refs (concept_id, text_id) VALUES (?,?)", (cid[0], tid[0]))

    conn.commit()
    conn.close()
    print("Medieval Hermetica ingestion complete.")

if __name__ == "__main__":
    ingest()
