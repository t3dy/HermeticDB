import sqlite3
import re

DB_PATH = r"c:\Dev\EmeraldTablet\db\emerald_tablet.db"

def slugify(text):
    return re.sub(r'\W+', '_', text).lower().strip('_')

texts_data = [
    {
        "title": "Liber XXIV philosophorum",
        "era": "Medieval",
        "type": "PRIMARY_SOURCE",
        "description": "A 12th-century Latin collection of 24 ontological definitions of God attributed to various ancient philosophers.",
        "analysis_html": "<p>A central text of medieval apophatic theology, frequently cited by scholastics like Thomas Aquinas and Meister Eckhart. The text explores the nature of divine unity through paradoxical and abstract definitions, such as 'God is an infinite sphere whose center is everywhere and circumference nowhere.' It represents the intersection of Neoplatonic metaphysics and Hermetic authority in the Latin West.</p>"
    },
    {
        "title": "De sex rerum principiis",
        "era": "Medieval",
        "type": "PRIMARY_SOURCE",
        "description": "A 12th-century cosmological treatise, often associated with the School of Chartres.",
        "analysis_html": "<p>Outlines six fundamental principles of reality: causa efficiens, causa formalis, causa finalis, materia, motus, and tempus. Mark Damien Delp identifies in this text a specific 'immanence of ratio,' where Hermetic cosmology is integrated into natural philosophy to explain the rational structure of the created world. It serves as a bridge between late antique Hermetism and medieval scholastic naturalism.</p>"
    },
    {
        "title": "Picatrix",
        "era": "Medieval",
        "type": "PRIMARY_SOURCE",
        "description": "The Latin translation of the Arabic 'Ghāyat al-Ḥakīm' (The Goal of the Wise).",
        "analysis_html": "<p>A massive compendium of astral magic and talismanic lore. It attributes many of its operations to Hermes Trismegistus and describes the 'perfect nature' as a source of secret knowledge. The text provides detailed instructions on planetary correspondences, image magic, and the invocation of celestial spirits, forming the cornerstone of the operative Hermetic tradition in the Middle Ages and Renaissance.</p>"
    },
    {
        "title": "Crater Hermetis",
        "era": "Renaissance",
        "type": "PRIMARY_SOURCE",
        "description": "A 15th-century dialogue by Lodovico Lazzarelli that synthesizes Hermetic regeneration with Christian theology.",
        "analysis_html": "<p>Lazzarelli identifies the Hermetic 'krater' or mixing bowl of Nous with the Christian experience of spiritual rebirth. The text is a significant witness to the 'lived' Hermetism of the Renaissance, where the author adopts the persona of Enoch and views his mentor, Giovanni da Correggio, as a living manifestation of Hermes.</p>"
    },
    {
        "title": "De occulta philosophia",
        "era": "Renaissance",
        "type": "PRIMARY_SOURCE",
        "description": "Heinrich Cornelius Agrippa's monumental three-book synthesis of occult knowledge (1533).",
        "analysis_html": "<p>Organizes magic into three realms: Natural, Celestial, and Ceremonial. Agrippa integrates Hermetic cosmology with Kabbalah and Neoplatonism to provide a systematic framework for the magus's interaction with the universe. It is the most influential textbook of Western occultism.</p>"
    }
]

ch_tractates = [
    ("CH I – Poimandres", "Antiquity", "PRIMARY_SOURCE", "The foundational revelation of the Hermetic corpus.", "Detailed creation vision involving Nous and the Anthropos."),
    ("CH II – To Asclepius", "Antiquity", "PRIMARY_SOURCE", "A metaphysical dialogue on the nature of God.", "Defines God as an infinite circle."),
    ("CH XIII – On Rebirth and Silence", "Antiquity", "PRIMARY_SOURCE", "Initiatory dialogue on spiritual regeneration.", "Guides Tat through the experience of palingenesis.")
    # ... simplified for script brevity, can add more later
]

scholars_data = [
    {
        "name": "Mark Damien Delp",
        "era": "Modern",
        "role": "SCHOLAR",
        "description": "Specialist in medieval cosmology and Hermetic reception.",
        "bio_html": "<p>Identified the 'immanence of ratio' in medieval Hermetic texts like 'De sex rerum principiis.' Argued Hermes was a primary authority on the rational structure of the physical universe.</p>"
    },
    {
        "name": "David Porreca",
        "era": "Modern",
        "role": "SCHOLAR",
        "description": "Scholar of medieval intellectual history and Hermetic transmission.",
        "bio_html": "<p>Specializes in the reception of the 'Liber viginti quattuor philosophorum' and the 'Asclepius' in scholastic circles. Challenged the narrative of universal scholastic hostility toward Hermetism.</p>"
    }
]

concepts_data = [
    {
        "label": "Immanence of Ratio",
        "category": "PHILOSOPHICAL",
        "definition_short": "Historiographical term for the 12th-century view of cosmic rationality.",
        "definition_long": "Introduced by Mark Damien Delp to describe how medieval thinkers used Hermetic cosmology to justify rational investigation of nature."
    },
    {
        "label": "Theurgy",
        "category": "THEOLOGICAL",
        "definition_short": "Ritual practices intended to invoke divine presence.",
        "definition_long": "In Hermetism, manifested as the 'animation of statues.' Viewed by scholars like Mahé as a necessary mechanism for spiritual union."
    }
]

def populate():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    for t in texts_data:
        t_id = slugify(t["title"])
        cursor.execute("""
            INSERT INTO texts (text_id, title, text_type, description, analysis_html, source_method)
            VALUES (?, ?, ?, ?, ?, 'SCHOLARSHIP_INGESTION')
            ON CONFLICT(text_id) DO UPDATE SET
                description=excluded.description,
                analysis_html=excluded.analysis_html
        """, (t_id, t["title"], t["type"], t["description"], t["analysis_html"]))

    for label, era, t_type, desc, analysis in ch_tractates:
        t_id = slugify(label)
        cursor.execute("""
            INSERT INTO texts (text_id, title, text_type, description, analysis_html, source_method)
            VALUES (?, ?, ?, ?, ?, 'SCHOLARSHIP_INGESTION')
            ON CONFLICT(text_id) DO UPDATE SET
                description=excluded.description,
                analysis_html=excluded.analysis_html
        """, (t_id, label, t_type, desc, analysis))

    for s in scholars_data:
        p_id = slugify(s["name"])
        cursor.execute("""
            INSERT INTO persons (person_id, name, era, role_primary, description, bio_html, source_method)
            VALUES (?, ?, ?, ?, ?, ?, 'SCHOLARSHIP_INGESTION')
            ON CONFLICT(person_id) DO UPDATE SET
                description=excluded.description,
                bio_html=excluded.bio_html
        """, (p_id, s["name"], s["era"], s["role"], s["description"], s["bio_html"]))

    for c in concepts_data:
        c_id = slugify(c["label"])
        cursor.execute("""
            INSERT INTO concepts (slug, label, category, definition_short, definition_long, source_method)
            VALUES (?, ?, ?, ?, ?, 'SCHOLARSHIP_INGESTION')
            ON CONFLICT(slug) DO UPDATE SET
                definition_short=excluded.definition_short,
                definition_long=excluded.definition_long
        """, (c_id, c["label"], c["category"], c["definition_short"], c["definition_long"]))
        
    conn.commit()
    conn.close()

if __name__ == "__main__":
    populate()
    print("Database updated successfully.")
