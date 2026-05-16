import sqlite3
import os

DB_PATH = r"c:\Dev\EmeraldTablet\db\emerald_tablet.db"

texts_data = [
    {
        "label": "Liber XXIV philosophorum",
        "era": "Medieval",
        "type": "Primary",
        "summary": "A 12th-century Latin collection of 24 ontological definitions of God attributed to various ancient philosophers. It is a central text of medieval apophatic theology, frequently cited by scholastics like Thomas Aquinas and Meister Eckhart. The text explores the nature of divine unity through paradoxical and abstract definitions, such as 'God is an infinite sphere whose center is everywhere and circumference nowhere.' It represents the intersection of Neoplatonic metaphysics and Hermetic authority in the Latin West.",
        "bibliography": "Lucentini, P. (Ed.). (1997). Liber viginti quattuor philosophorum. CCCM 143."
    },
    {
        "label": "De sex rerum principiis",
        "era": "Medieval",
        "type": "Primary",
        "summary": "A 12th-century cosmological treatise, often associated with the School of Chartres, which outlines six fundamental principles of reality: causa efficiens, causa formalis, causa finalis, materia, motus, and tempus. Mark Damien Delp identifies in this text a specific 'immanence of ratio,' where Hermetic cosmology is integrated into natural philosophy to explain the rational structure of the created world. It serves as a bridge between late antique Hermetism and medieval scholastic naturalism.",
        "bibliography": "Delp, M. D. (2003). The Immanence of Ratio in the De Sex Rerum Principiis."
    },
    {
        "label": "Picatrix",
        "era": "Medieval",
        "type": "Primary",
        "summary": "The Latin translation of the Arabic 'Ghāyat al-Ḥakīm' (The Goal of the Wise), a massive compendium of astral magic and talismanic lore. It attributes many of its operations to Hermes Trismegistus and describes the 'perfect nature' as a source of secret knowledge. The text provides detailed instructions on planetary correspondences, image magic, and the invocation of celestial spirits, forming the cornerstone of the operative Hermetic tradition in the Middle Ages and Renaissance.",
        "bibliography": "Pingree, D. (Ed.). (1986). Picatrix: The Latin Version."
    },
    {
        "label": "Crater Hermetis",
        "era": "Renaissance",
        "type": "Primary",
        "summary": "A 15th-century dialogue by Lodovico Lazzarelli that synthesizes Hermetic regeneration with Christian theology. Lazzarelli identifies the Hermetic 'krater' or mixing bowl of Nous with the Christian experience of spiritual rebirth. The text is a significant witness to the 'lived' Hermetism of the Renaissance, where the author adopts the persona of Enoch and views his mentor, Giovanni da Correggio, as a living manifestation of Hermes.",
        "bibliography": "Lazzarelli, L. (15th c.). Crater Hermetis."
    },
    {
        "label": "De occulta philosophia",
        "era": "Renaissance",
        "type": "Primary",
        "summary": "Heinrich Cornelius Agrippa's monumental three-book synthesis of occult knowledge, first published in 1533. It organizes magic into three realms: Natural (elemental), Celestial (astrological), and Ceremonial (theological/angelic). Agrippa integrates Hermetic cosmology with Kabbalah and Neoplatonism to provide a systematic framework for the magus's interaction with the universe. It is the most influential textbook of Western occultism and a primary source for Renaissance Hermetic philosophy.",
        "bibliography": "Agrippa, H. C. (1533). De occulta philosophia libri tres."
    }
]

# Adding CH I-XVIII
ch_tractates = [
    ("CH I – Poimandres", "Antiquity", "Primary", "The foundational revelation of the Hermetic corpus, where the Mind (Nous) reveals the creation of the world and the origin of humanity to Hermes. It details the descent of the 'Essential Man' through the planetary spheres and his subsequent entrapment in matter, followed by the path of spiritual ascent and return to the divine realm."),
    ("CH II – To Asclepius", "Antiquity", "Primary", "A metaphysical dialogue on the nature of God, defining the divine as a 'circle' and exploring the concept of transcendence through contemplation."),
    ("CH III – The Sacred Discourse", "Antiquity", "Primary", "A brief cosmological summary detailing the creation of the universe, the role of the Logos, and the maintenance of cosmic order."),
    ("CH IV – The Mixing Bowl (Krater)", "Antiquity", "Primary", "Describes a symbolic mixing bowl filled with Intellect (Nous) sent by God to humanity. Those who 'dip themselves' in the krater receive true gnosis and are set apart from those who possess only reason."),
    ("CH V – God is Invisible and Most Manifest", "Antiquity", "Primary", "A theological reflection on the paradox of divine omnipresence: God is hidden because He is all things, yet visible through His works in the cosmos."),
    ("CH VI – In God Alone is Good", "Antiquity", "Primary", "An ontological argument identifying the essence of 'the Good' exclusively with God, contrasting it with the transitory nature of material existence."),
    ("CH VII – The Greatest Evil is Ignorance of God", "Antiquity", "Primary", "A didactic exhortation to overcome the 'drunkenness' of ignorance and seek the light of gnosis for salvation."),
    ("CH VIII – That None of the Things that Are Perishes", "Antiquity", "Primary", "Rejects the notion of annihilation, arguing that what we perceive as death is merely a transformation or 'metamorphosis' within the eternal continuity of being."),
    ("CH IX – On Thought and Sense", "Antiquity", "Primary", "Distinguishes between intellectual thought (noesis) and sensory perception (aisthesis), prioritizing the former as the means to divine knowledge."),
    ("CH X – The Key", "Antiquity", "Primary", "A systematic condensation of Hermetic doctrine, covering the hierarchy of being, the nature of the soul, and the relationship between the One and the Many."),
    ("CH XI – Mind to Hermes", "Antiquity", "Primary", "A direct instruction from the Divine Mind (Nous) to Hermes, emphasizing the ability of the human intellect to expand and encompass the entire universe in contemplation."),
    ("CH XII – On the Common Mind", "Antiquity", "Primary", "Explores the 'Common Mind' that permeates all living things and the specific role of human reason in participating in divine rationality."),
    ("CH XIII – On Rebirth and Silence", "Antiquity", "Primary", "A pivotal initiatory dialogue where Hermes guides Tat through the experience of spiritual regeneration (palingenesis) and the silencing of the senses to receive divine light."),
    ("CH XIV – Letter of Hermes to Asclepius", "Antiquity", "Primary", "An epistolary exposition of the unity of the divine essence and the relationship between the Creator and the created."),
    ("CH XV – Fragment on Cosmic Unity", "Antiquity", "Primary", "A short fragment affirming the interconnectedness of all things within the divine totality."),
    ("CH XVI – Definitions to Asclepius", "Antiquity", "Primary", "A discourse clarifying Hermetic theology and cosmology, with a specific focus on the divine presence within the elements and a defense against the misunderstanding of idolatry."),
    ("CH XVII – To Asclepius", "Antiquity", "Primary", "A brief text discussing the presence of divine power within animated statues and the role of sacred art in manifesting the intelligible world."),
    ("CH XVIII – Letter to Ammon", "Antiquity", "Primary", "A royal instruction text focusing on the praise of kingship as a reflection of divine sovereignty and the maintenance of justice.")
]

scholars_data = [
    {
        "name": "Mark Damien Delp",
        "era": "Modern",
        "bio": "A specialist in the history of medieval cosmology and the reception of Hermetic thought in the Latin West. Delp's research focuses on the 12th-century transition from purely theological cosmology to natural philosophy. He is best known for identifying the 'immanence of ratio' in medieval Hermetic texts like the 'De sex rerum principiis,' arguing that Hermes was viewed not just as a prophet but as a primary authority on the rational structure of the physical universe.",
        "works": "The Immanence of Ratio in the De Sex Rerum Principiis (2003)"
    },
    {
        "name": "David Porreca",
        "era": "Modern",
        "bio": "A scholar of medieval intellectual history specializing in the transmission of Hermetic and magical texts. Porreca's work involves the philological analysis of philosophical Hermetism in the Middle Ages, particularly the reception of the 'Liber viginti quattuor philosophorum' and the 'Asclepius' in scholastic circles. He has challenged the narrative of universal scholastic hostility toward Hermetism, demonstrating instead a nuanced integration of Hermes as a 'proto-Christian' philosopher.",
        "works": "The Reception of Hermes in Medieval Scholasticism; Alain de Lille and the Hermetic Tradition."
    },
    {
        "name": "Paolo Lucentini",
        "era": "Modern",
        "bio": "A preeminent historian of medieval philosophy and the founder of the 'Hermes Latinus' research group. Lucentini dedicated his career to the census and critical edition of Latin Hermetic manuscripts. His research established the philosophical rigor and structural coherence of the 'Asclepius' and the 'Liber viginti quattuor philosophorum,' effectively mapping the cartography of Hermetic transmission from Late Antiquity to the Renaissance.",
        "works": "Hermetica Mediaevalia; Il problema del male nell’Asclepius."
    },
    {
        "name": "Jean-Pierre Mahé",
        "era": "Modern",
        "bio": "A world-renowned specialist in Late Antique philosophy and Coptic Hermetism. Mahé's groundbreaking work on the Nag Hammadi Coptic Hermetica provided the first clear evidence that Hermetic texts were not merely literary fictions but reflected the ritual and philosophical practices of real communities in Roman Egypt. He developed the theory of the 'Hermetic Way' (the path of immortality) involving gnose, discourse, and intellect.",
        "works": "Hermès en Haute-Égypte (1978, 1982)."
    }
]

concepts_data = [
    {
        "label": "Immanence of Ratio",
        "definition": "A historiographical term introduced by Mark Damien Delp to describe the 12th-century medieval view that the rational structure of the universe (Ratio) is immanent within the physical cosmos. This concept allowed medieval thinkers to use Hermetic cosmological texts to justify a rational, proto-scientific investigation of nature without abandoning divine causality.",
        "era": "Medieval"
    },
    {
        "label": "Theurgy",
        "definition": "Derived from the Greek 'theourgia' (divine work), it refers to ritual practices intended to invoke the presence of the divine or to purify the soul for ascent. In the Hermetic tradition, specifically the 'Asclepius,' theurgy is manifested in the 'animation of statues,' where divine powers are drawn into terrestrial forms through sacred rites, herbs, and stones. Modern scholars like Iamblichus and Jean-Pierre Mahé emphasize that theurgy was viewed as a necessary mechanism for spiritual union, bridging the gap between human reason and divine intellect.",
        "era": "Antiquity"
    }
]

def populate_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Insert Reception Texts
    for text in texts_data:
        cursor.execute("""
            INSERT OR REPLACE INTO texts (label, era, type, summary, writing)
            VALUES (?, ?, ?, ?, ?)
        """, (text["label"], text["era"], text["type"], text["summary"], text["summary"]))
    
    # Insert CH Tractates
    for label, era, t_type, summary in ch_tractates:
        cursor.execute("""
            INSERT OR REPLACE INTO texts (label, era, type, summary, writing)
            VALUES (?, ?, ?, ?, ?)
        """, (label, era, t_type, summary, summary))

    # Insert Scholars
    for scholar in scholars_data:
        cursor.execute("""
            INSERT OR REPLACE INTO figures (name, era, bio, works)
            VALUES (?, ?, ?, ?)
        """, (scholar["name"], scholar["era"], scholar["bio"], scholar["works"]))

    # Insert Concepts
    for concept in concepts_data:
        cursor.execute("""
            INSERT OR REPLACE INTO concepts (label, definition, era)
            VALUES (?, ?, ?)
        """, (concept["label"], concept["definition"], concept["era"]))
        
    conn.commit()
    conn.close()

if __name__ == "__main__":
    populate_database()
    print("Database updated with scholarship, scholars, and key concepts.")
