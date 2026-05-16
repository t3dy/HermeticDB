import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR.parent / "db" / "emerald_tablet.db"

NEW_PERSONS = [
    ("lactantius", "Lactantius", "LATE_ANTIQUITY", "SCHOLAR", "Early Christian apologist who heavily utilized Hermetic texts."),
    ("stobaeus", "John of Stobi (Stobaeus)", "LATE_ANTIQUITY", "COMPILER", "5th-century compiler who preserved the Hermetic Excerpts."),
    ("cyril_alexandria", "Cyril of Alexandria", "LATE_ANTIQUITY", "SCHOLAR", "Patriarch of Alexandria who quoted the Hermetica against Julian the Apostate."),
    ("clement_alexandria", "Clement of Alexandria", "LATE_ANTIQUITY", "SCHOLAR", "Christian theologian who described the 42 Books of Hermes.")
]

RICH_PROSE = {
    # Litwa Anthology Figures
    "lactantius": """
        <p>Lucius Caecilius Firmianus Lactantius (c. 250–c. 325 AD) was an early Christian apologist and advisor to Constantine I. Within the study of Hermeticism, his <i>Divinae Institutiones</i> (Divine Institutes) serves as a paramount testimonium to the late antique reception of Hermes Trismegistus.</p>
        <h2>Fragments and Testimonies in <i>Hermetica II</i></h2>
        <p>As documented in M. David Litwa's <i>Hermetica II</i>, Lactantius enthusiastically appropriated Hermes as a Gentile prophet who anticipated Christianity. Lactantius quotes the Hermetica extensively to prove to pagan intellectuals that their own most ancient sage recognized a single, supreme God. Specifically, he cites fragments describing God as 'without a name' (<i>anōnymos</i>), unbegotten, and the creator of the divine Son (which Lactantius maps directly onto Christ). Litwa's analysis highlights how Lactantius carefully curated his Hermetic quotations, ignoring the more pantheistic or polytheistic elements of the Corpus Hermeticum to construct a monotheistic 'Hermes Christianus.'</p>
        <h2>Scholarly Significance</h2>
        <p>Scholars like Garth Fowden and Christian Bull point to Lactantius as evidence of the high prestige Hermes held in the 3rd and 4th centuries. By elevating Hermes to a status equivalent or superior to Plato and Pythagoras, Lactantius inadvertently secured the survival of the Hermetic tradition into the Renaissance; when Marsilio Ficino translated the <i>Corpus Hermeticum</i> in 1471, he relied on Lactantius's endorsement to guarantee the text's theological safety and profound antiquity.</p>
    """,
    "stobaeus": """
        <p>John of Stobi, commonly known as Stobaeus (fl. 5th century AD), was a Macedonian compiler who constructed a massive anthology (<i>Anthologion</i>) of Greek literature, philosophy, and wisdom literature for the education of his son, Septimius.</p>
        <h2>The Stobaean Hermetica</h2>
        <p>Stobaeus is the sole surviving source for a vast swathe of Hermetic literature, encompassing forty excerpts collectively known as the <i>Stobaean Hermetica</i> (included in Litwa's <i>Hermetica II</i>). The most famous of these is the <i>Kore Kosmou</i> (Virgin of the World), an elaborate cosmological narrative in which Isis imparts secret Hermetic wisdom to her son Horus. The Stobaean fragments cover themes not fully explored in the standard 14 treatises of the Corpus Hermeticum, including the mechanics of reincarnation, the animation of statues, the nature of decanic spirits, and the divine geography of Egypt.</p>
        <h2>Scholarly Context (Bull and Fowden)</h2>
        <p>Garth Fowden uses the Stobaean excerpts to argue for a highly developed, ritualistic Hermetic milieu in Upper Egypt, contrasting the philosophical bent of the <i>Corpus Hermeticum</i> with the more mythological and ritualistic tone of the <i>Kore Kosmou</i>. Christian H. Bull notes that the Stobaean fragments heavily emphasize the Egyptian identity of the Hermetic teachings, reinforcing the thesis that Hermeticism was not merely "Greek philosophy in Egyptian dress" but an authentic translation of native Egyptian priestly lore (specifically from the temples of Thoth) into Hellenistic Greek.</p>
    """,
    "cyril_alexandria": """
        <p>Cyril of Alexandria (c. 376–444 AD) was the powerful and controversial Patriarch of Alexandria. In Hermetic studies, his significance lies in his massive polemical work, <i>Contra Julianum</i> (Against Julian), written to refute the anti-Christian treatises of the Emperor Julian.</p>
        <h2>Hermetic Testimonies in <i>Hermetica II</i></h2>
        <p>As Litwa details in <i>Hermetica II</i>, Cyril uses Hermes Trismegistus as a rhetorical weapon against Julian. Since Julian respected the ancient Hellenic and Egyptian sages, Cyril quotes extensively from lost Hermetic texts (many of which only survive in Cyril's quotes) to prove that Hermes actually taught the Trinity and the Incarnation. Cyril cites the <i>Hermetica</i> to show that the Egyptian sage acknowledged a "Word" (<i>Logos</i>) of God that organized the cosmos.</p>
        <h2>Scholarly Perspectives</h2>
        <p>Fowden and Bull highlight Cyril's testimonies as a window into the late antique "battle for Hermes." Both pagans (like Iamblichus and Julian) and Christians (like Cyril) claimed ownership of the Hermetic revelation. Cyril's fragments are particularly valuable because they show traces of authentic Egyptian theology (such as the theology of Memphis regarding Ptah/Logos) that had been absorbed into the Hermetic discourse, supporting Bull's thesis of the indigenous Egyptian roots of the tradition.</p>
    """,
    "clement_alexandria": """
        <p>Clement of Alexandria (c. 150–c. 215 AD) was a Christian theologian and head of the Catechetical School of Alexandria. He is crucial to the study of Hermeticism for his detailed ethnographic description of Egyptian priestly processions.</p>
        <h2>The 42 Books of Hermes</h2>
        <p>In his <i>Stromata</i> (Miscellanies), Clement describes a sacred procession of Egyptian priests carrying the "forty-two indispensable books of Hermes." These books contained hymns, astrological charts, cosmography, temple construction rules, and medical texts. As M. David Litwa and Christian Bull emphasize, Clement's account proves that in the 2nd century AD, "Hermes" was explicitly identified with the Egyptian god Thoth, the author of the sacred temple archives.</p>
        <h2>The "Egyptian Hermes"</h2>
        <p>Garth Fowden uses Clement's testimony as the cornerstone of <i>The Egyptian Hermes</i>. Clement's 42 books do not directly match the philosophical <i>Corpus Hermeticum</i>; rather, they represent the "technical" Hermetica (astrology, magic, medicine) that formed the daily lived reality of the Egyptian priesthood. Bull argues that the authors of the philosophical Hermetica were likely native Egyptian priests, like those described by Clement, who were Hellenized and translating their temple wisdom into the idiom of Greek philosophy for a broader audience.</p>
    """,

    # Major Expansions (Zosimos, Iamblichus, Julian)
    "zosimos_of_panopolis": """
        <p>Zosimos of Panopolis (fl. c. 300 AD) is the most important alchemical author of Greco-Roman antiquity. Born in the Upper Egyptian city of Panopolis (Akhmim), Zosimos synthesized practical metallurgy with Gnostic theology, Neoplatonism, and Hermetic philosophy.</p>
        <h2>Zosimos as Hermetic Priest</h2>
        <p>Recent scholarship, particularly expanding on the fragments highlighted in Litwa's <i>Hermetica II</i> and the work of Christian Bull, has repositioned Zosimos not merely as a proto-chemist, but as a practicing Hermetic priest. Zosimos frequently cites Hermes Trismegistus as the ultimate authority on both physical transmutation and the salvation of the soul. In his treatise <i>On the Letter Omega</i>, Zosimos fiercely critiques "demonic" magic and the binding of planetary fates, advocating instead for the Hermetic path of relying purely on the divine Nous (Mind) to achieve salvation.</p>
        <h2>The Visions of Zosimos</h2>
        <p>Zosimos is most famous for his "Visions," a series of dream narratives where he witnesses a priest named Ion undergoing horrific dismemberment, boiling, and transmutation on a bowl-shaped altar. Jung famously interpreted these visions psychologically, but modern historians like Fowden and Litwa view them within the context of late antique ritual. The dismemberment reflects the Egyptian myth of Osiris, and the alchemy of Zosimos is essentially an internalization of the mummification and resurrection rituals of the Egyptian temples, translated into chemical operations on metals.</p>
    """,
    "iamblichus": """
        <p>Iamblichus of Chalcis (c. 245–c. 325 AD) was the architect of Syrian Neoplatonism and the primary philosophical defender of theurgy (divine ritual work). He is central to the late antique Hermetic milieu.</p>
        <h2>The <i>De Mysteriis</i> and the Way of Hermes</h2>
        <p>In his masterwork, the <i>De Mysteriis Aegyptiorum</i> (On the Mysteries of the Egyptians), written under the pseudonym of an Egyptian priest named Abammon, Iamblichus explicitly aligns his theurgical system with the teachings of Hermes Trismegistus. He claims that all true theological knowledge comes from the "pillars of Hermes," which Pythagoras and Plato merely translated into Greek.</p>
        <h2>Theurgy vs. Theology</h2>
        <p>Iamblichus argued against his teacher Porphyry's purely intellectual approach. Iamblichus posited that the human soul is fully descended into matter and cannot achieve union with the One through thought alone. It requires <i>synthemata</i> (divine symbols, stones, herbs, incantations) embedded in the material world by the Demiurge. As Christian Bull and Garth Fowden demonstrate, Iamblichus's "Egyptian" theology in the <i>De Mysteriis</i> closely parallels the cosmology and ritual mechanics found in the Hermetic <i>Asclepius</i> and the Stobaean fragments, proving that Hermetic texts were actively used as liturgical manuals in theurgical circles.</p>
    """,
    "julian_the_apostate": """
        <p>Flavius Claudius Julianus (331–363 AD), known as Julian the Apostate, was the last non-Christian Roman Emperor. A dedicated Neoplatonist and initiate into several mystery cults, he attempted to revitalize paganism against the rising tide of Christianity.</p>
        <h2>Julian and the Hermetic Tradition</h2>
        <p>As documented in <i>Hermetica II</i>, Julian held Hermes Trismegistus in the highest esteem. In his <i>Hymn to King Helios</i> and his polemic <i>Against the Galileans</i>, Julian references the teachings of Hermes regarding the structure of the cosmos and the emanation of the gods. Julian utilized the Hermetic and Iamblichan framework of theurgy to construct his "pagan church," arguing that the ancient revelations of Thoth-Hermes were vastly superior to the relatively recent scriptures of the Christians.</p>
        <h2>Scholarly Interpretation</h2>
        <p>Garth Fowden views Julian as the culmination of the philosophical-magical synthesis of Late Antiquity. Julian's reliance on Hermetic authority (alongside the Chaldean Oracles) demonstrates how the <i>Corpus Hermeticum</i> had been elevated from obscure Egyptian temple wisdom into the canonical scripture of the imperial Neoplatonic resistance. Cyril of Alexandria's massive refutation of Julian (which preserves so many Hermetic fragments) was a direct response to Julian's successful weaponization of the Hermetic tradition.</p>
    """,
    
    # Modern Scholars
    "garth_fowden": """
        <p>Garth Fowden is a preeminent historian of Late Antiquity. His 1986 masterwork, <i>The Egyptian Hermes: A Historical Approach to the Late Pagan Mind</i>, fundamentally revolutionized Hermetic studies.</p>
        <h2>The Egyptian Context of Hermeticism</h2>
        <p>Prior to Fowden, scholars (like Festugière) viewed the <i>Corpus Hermeticum</i> as Greek philosophy written by Greeks who merely slapped an "Egyptian" label on the text for exotic flavor. Fowden systematically dismantled this view. He argued that the "technical" Hermetica (astrology, alchemy, magic) and the "philosophical" Hermetica (theology, soteriology) were not separate traditions, but two sides of the same coin, reflecting the lived reality of Egyptian priests who were grappling with Hellenization.</p>
        <h2>The Hermetic Milieu</h2>
        <p>Fowden introduced the concept of the "Hermetic milieu"—small, intimate circles of spiritual seekers in Roman Egypt engaging in ritualized study, prayer, and ecstatic vision under the guidance of a master. His work paved the way for all modern understandings of the texts as active ritual documents rather than dry philosophical treatises.</p>
    """,
    "christian_bull": """
        <p>Christian H. Bull is a leading contemporary scholar of ancient religion and Western Esotericism. His 2018 book, <i>The Tradition of Hermes Trismegistus: The Egyptian Priestly Figure as a Teacher of Hellenized Wisdom</i>, serves as the definitive modern update to Fowden's thesis.</p>
        <h2>The Priestly Authorship Thesis</h2>
        <p>Bull forcefully argues that the authors of the Hermetica were actual, ethnically Egyptian priests of Thoth (acting in temples at places like Hermopolis). Confronted by the cultural dominance of the Greeks and later the Romans, these priests translated their indigenous theology—specifically the Memphite theology of creation via the heart and tongue (Nous and Logos)—into the language of Middle Platonism.</p>
        <h2>The "Way of Hermes"</h2>
        <p>Bull reconstructs the "Way of Hermes" as a graduated initiatory path. Neophytes began with the "General Discourses" to purify the mind, advanced to the "Detailed Discourses" mapping the cosmos, and culminated in the ecstatic, silent union with the divine mind (the Ogdoadic revelation), often facilitated by temple rituals like statue animation.</p>
    """,
    "david_litwa": """
        <p>M. David Litwa is a prominent scholar of ancient Mediterranean religions, early Christianity, and late antique philosophy. In the context of Hermetic studies, his magnum opus is <i>Hermetica II: The Excerpts of Stobaeus, Papyrus Fragments, and Ancient Testimonies</i> (2018).</p>
        <h2>Completing the Hermetic Corpus</h2>
        <p>For centuries, the English-speaking world relied almost entirely on the 17 treatises of the <i>Corpus Hermeticum</i> and the Latin <i>Asclepius</i> (most recently translated by Brian Copenhaver). Litwa's <i>Hermetica II</i> gathered, translated, and provided extensive commentary on the rest of the surviving tradition. This includes the massive Stobaean anthology, the Oxford and Vienna papyri, and the myriad quotations embedded in the works of church fathers like Lactantius, Cyril, and Augustine, as well as alchemists like Zosimos.</p>
        <h2>Scholarly Impact</h2>
        <p>Litwa's comprehensive anthology allowed scholars to see the full breadth of the "Hermetic discourse." It revealed that in Late Antiquity, the Hermetic writings were vastly more extensive and diverse than the canonical 17 texts suggest, heavily involved in practical ritual, Egyptian temple myth, and fierce polemics between pagans and Christians.</p>
    """,
    "hermes_trismegistus": """
        <p>Hermes Trismegistus ("Thrice-Greatest Hermes") is the legendary Hellenistic amalgamation of the Greek god Hermes and the Egyptian god of wisdom and writing, Thoth.</p>
        <h2>The Late Antique Figure</h2>
        <p>In the context of the Egyptian priesthood (as analyzed by Fowden and Bull), Hermes Trismegistus was not viewed as a god, but as an ancient, incredibly powerful human sage or prophet who achieved deification. He was the author of the sacred temple libraries (the 42 books mentioned by Clement of Alexandria) and the revealer of all arts, sciences, alchemy, astrology, and theology.</p>
        <h2>The Evolution of the Myth</h2>
        <p>During the Middle Ages, Hermes was received in the Arabic world as Idris or Enoch, the prophet before the flood who preserved celestial mechanics and alchemy. In the Latin Renaissance, heavily influenced by Lactantius and translated by Ficino, Hermes became the cornerstone of the <i>Prisca Theologia</i> (Ancient Theology)—a contemporary of Moses who foresaw the coming of Christ. The modern historiography of Litwa and Hanegraaff traces how this mythical figure served as a crucial blank canvas upon which successive eras projected their highest spiritual and scientific aspirations.</p>
    """
}

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 1. Insert any new persons if they don't exist
    for pid, name, era, role, desc in NEW_PERSONS:
        try:
            cursor.execute("""
                INSERT INTO persons (person_id, name, era, role_primary, description, source_method, review_status, confidence)
                VALUES (?, ?, ?, ?, ?, 'SEED_DATA', 'REVIEWED', 'HIGH')
            """, (pid, name, era, role, desc))
            print(f"Added new figure: {name}")
        except sqlite3.IntegrityError:
            pass # Already exists

    # 2. Update with the massively rich prose
    print("Injecting rich Litwa/Bull/Fowden/Zosimos prose...")
    for slug, prose in RICH_PROSE.items():
        cursor.execute("UPDATE persons SET bio_html = ? WHERE person_id = ?", (prose, slug))
        if cursor.rowcount == 0:
            cursor.execute("UPDATE texts SET analysis_html = ? WHERE text_id = ?", (prose, slug))
            if cursor.rowcount == 0:
                cursor.execute("UPDATE concepts SET definition_long = ? WHERE slug = ?", (prose, slug))

    conn.commit()
    conn.close()
    print("Litwa Anthology & Late Antique Rich Prose Expansion complete.")

if __name__ == "__main__":
    main()
