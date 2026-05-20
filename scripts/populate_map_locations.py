"""
Populate map locations with comprehensive Hermetic centers.
Focuses on Christian Bull's priestly tradition thesis and Zosimos as a case study.
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "db" / "emerald_tablet.db"

LOCATIONS = [
    # EGYPTIAN PRIESTLY CENTERS (Christian Bull's thesis emphasis)
    ("memphis", "Memphis, Egypt", 29.8432, 31.2495,
     "The ancient capital of Egypt and center of the Memphite theology. According to Christian Bull, the Hermetic priesthood rooted themselves in the theological traditions of Memphis, translating the Memphite cosmology (creation via Ptah's heart and tongue/nous and logos) into Greek philosophical language. Memphis was home to major temple complexes and remained a significant religious center through the Greco-Roman period."),

    ("thebes", "Thebes (Luxor), Egypt", 25.6872, 32.6396,
     "The great religious capital of Upper Egypt and home to the Temple of Amun, the largest temple complex in the ancient world. Thebes was the primary center of Egyptian priesthood and theological learning. As Bull argues, the Hermetic authors drew on the priestly theological traditions preserved at Thebes, adapting them to Greek philosophy. Multiple Hermetic sites of composition may have connections to Theban priestly circles."),

    ("coptos", "Coptos (Qift), Egypt", 26.1061, 32.8167,
     "A crucial trading hub on the Red Sea route, where commerce, religious practice, and philosophical transmission intersected. Coptos was a major center for Mediterranean-Indian trade and a site where Hermetic ideas may have been transmitted through merchant networks. The city served as a gateway between the Nile Valley and international trade routes."),

    ("assuan", "Assuan (Syene), Egypt", 24.0883, 32.8873,
     "The southern border city of Egypt, home to significant temple traditions and priestly centers. Assuan was a major site for the preservation of Egyptian religious knowledge and served as a transmission point for Hermetic ideas southward into Nubia and northward along the Nile."),

    # ZOSIMOS FOCUS
    ("akhmim_expanded", "Akhmim (Panopolis), Egypt - Zosimos Center", 26.5667, 31.7333,
     "Home of Zosimos of Panopolis (fl. 300 CE), the most important surviving alchemical author of Late Antiquity. Zosimos represents the synthesis of Hermetic philosophy with technical alchemy. His vision-narratives (Visiones Zosimi) present alchemical transmutation as both chemical process and spiritual transformation. Zosimos's work integrates the Hermetic principle of correspondence (macrocosm-microcosm) with practical laboratory operations. His texts cite the Hermetica explicitly and synthesize Egyptian priestly knowledge, Greek philosophy, and technical chemical practice. Zosimos wrote for a community of alchemists in Upper Egypt and his surviving corpus is preserved through Byzantine Greek manuscripts and Arabic recensions."),

    # LATE ANTIQUE TRANSMISSION CENTERS
    ("antioch", "Antioch, Syria", 36.2021, 36.1627,
     "A major center of late antique Christianity, Neoplatonism, and Hermetic philosophy. Antioch was the site of significant synthesis between Christian theology, Neoplatonic metaphysics, and Hermetic cosmology. The city hosted important theological schools and was a crucial transmission point for Greek learning into the Syriac world."),

    ("constantinople", "Constantinople (Istanbul), Turkey", 41.0082, 28.9784,
     "The Byzantine capital and primary custodian of Greek learning in the medieval period. Constantinople preserved Hermetic texts and Byzantine scholars engaged in detailed study and commentary on the Corpus Hermeticum and related texts. The city served as the crucial transmission bridge between Late Antique and medieval Mediterranean Hermeticism."),

    ("rome", "Rome, Italy", 41.9028, 12.4964,
     "The center of the Roman Empire and home to significant Neoplatonic circles in the 3rd-4th centuries. Rome hosted philosophers including Plotinus and his student Porphyry, who engaged with Hermetic philosophy within the broader Neoplatonic synthesis. Roman intellectual circles preserved and transmitted Hermetic ideas throughout the empire."),

    # ISLAMIC WORLD CENTERS
    ("damascus", "Damascus, Syria", 33.5138, 36.2765,
     "A major Islamic intellectual center where Hermetic texts were preserved and studied. Damascus hosted significant scholars of natural philosophy and occult sciences who engaged with Hermetic and Neoplatonic doctrines translated from Greek."),

    ("cairo", "Cairo (Fustat), Egypt", 30.0444, 31.2357,
     "The great Islamic capital of Egypt and site of significant Hermetic and alchemical transmission. Cairo served as a center for the preservation and study of Hermetic texts and was home to major alchemists and natural philosophers. The city maintained continuity with the ancient Egyptian Hermetic tradition."),

    ("cordoba", "Cordoba, Spain", 37.8882, -4.7794,
     "A major center of Islamic-Andalusian learning where Greek philosophical and Hermetic texts were preserved, studied, and translated. Cordoba was crucial for transmitting Hermetic, Neoplatonic, and alchemical knowledge from the Islamic world into Christian Europe via Latin translation."),

    ("toledo", "Toledo, Spain", 39.8581, -4.0201,
     "The primary site of the Iberian translation movement where Arabic, Hebrew, and Greek texts were translated into Latin. Toledo was the gateway through which Hermetic texts, alchemical treatises, and philosophical works entered medieval Christian Europe. Many key Hermetic texts (including the Emerald Tablet) entered the Latin West through Toledo translations."),

    # RENAISSANCE CENTERS
    ("venice", "Venice, Italy", 45.4408, 12.3155,
     "A major trading and intellectual hub with connections to the Byzantine and Islamic worlds. Venice served as a crucial source of Greek manuscripts during the Renaissance and was a center for the collection and study of Hermetic texts. The city was home to significant Renaissance Hermetic scholars and alchemists."),

    ("mantua", "Mantua, Italy", 45.1564, 10.7967,
     "The court of the Gonzaga family, a major center of Renaissance humanism and Hermetic scholarship. Mantua hosted significant Hermetic philosophers and was a site of alchemical and magical experimentation under ducal patronage."),

    # NORTHERN EUROPEAN CENTERS
    ("prague_hermetic", "Prague, Bohemia", 50.0755, 14.4378,
     "The alchemical capital of 16th-17th century Europe under the patronage of Emperor Rudolf II. Prague became a haven for alchemists, astrologers, and Hermetic practitioners who were attracted by imperial collecting and patronage. The city hosted some of Europe's most significant alchemical laboratories and the most extensive collections of alchemical manuscripts. Rudolf's Kunstkammer assembled occult and alchemical texts and objects."),

    ("strasbourg", "Strasbourg, France", 48.5734, 7.7521,
     "A major center of Renaissance alchemy and Hermetic studies in the 16th century. Strasbourg hosted important alchemists and was a center for the publication of alchemical and Hermetic texts during the early modern period."),

    # MEDIEVAL CENTERS
    ("paris", "Paris, France", 48.8566, 2.3522,
     "A major center of medieval learning where Hermetic and alchemical texts circulated among scholars and natural philosophers. Paris hosted significant translators and commentators on Hermetic and Arabic philosophical texts."),

    ("oxford", "Oxford, England", 51.7548, -1.2545,
     "A center of medieval and early modern Hermetic learning where scholars including Roger Bacon engaged with alchemical and Hermetic ideas. Oxford hosted important natural philosophers who integrated Hermetic philosophy with their investigations of nature."),

    # ISLAMIC TRANSMISSION HUB
    ("basra", "Basra, Iraq", 30.5433, 47.8027,
     "A major center of early Islamic philosophy and natural science. Basra hosted the Ikhwan al-Safa (Brethren of Purity), whose Epistles synthesized Neoplatonic, Hermetic, and Islamic theological doctrines into a comprehensive philosophical encyclopedia."),
]

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# Clear existing non-primary locations (keep the core 9)
core_slugs = ('akhmim', 'hermopolis', 'alexandria', 'panopolis', 'harran', 'baghdad', 'florence', 'prague', 'london')
cur.execute("SELECT COUNT(*) FROM locations")
initial_count = cur.fetchone()[0]

inserted = 0
updated = 0
skipped = 0

for slug, label, lat, lng, description in LOCATIONS:
    try:
        # Check if location exists
        cur.execute("SELECT id FROM locations WHERE slug = ?", (slug,))
        exists = cur.fetchone()

        if exists:
            # Update if it's an expanded version
            if '_expanded' in slug or slug not in core_slugs:
                cur.execute(
                    "UPDATE locations SET label = ?, lat = ?, lng = ?, description = ? WHERE slug = ?",
                    (label, lat, lng, description, slug)
                )
                updated += 1
            else:
                skipped += 1
        else:
            # Insert new location
            cur.execute(
                "INSERT INTO locations (slug, label, lat, lng, description) VALUES (?, ?, ?, ?, ?)",
                (slug, label, lat, lng, description)
            )
            inserted += 1
    except Exception as e:
        print(f"ERROR with {slug}: {e}")

conn.commit()
conn.close()

print(f"[MAP LOCATIONS] Inserted: {inserted} new locations | Updated: {updated} | Skipped: {skipped}")
print(f"Total locations now: {initial_count + inserted}")
