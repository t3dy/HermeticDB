import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR.parent / "db" / "emerald_tablet.db"

CLEAN_PROSE = {
    "hermes_trismegistus": {
        "title": "Hermes Trismegistus",
        "bio": """
<p>
Hermes Trismegistus (the "Thrice-Great Hermes") is the legendary Hellenistic figure at the heart of the Hermetic tradition. Often identified as a syncretic blend of the Greek god Hermes and the Egyptian god Thoth, he is credited as the progenitor of alchemy, astrology, and magic. In the <i>Tabula Smaragdina</i> (Emerald Tablet), Hermes is positioned as the authoritative speaker who reveals the fundamental principles of the cosmos.
</p>

<h2>Historical Context</h2>
<p>
The mythos of Hermes Trismegistus emerged in the cultural crucible of Hellenistic Egypt, where Ptolemaic-era scholars sought to reconcile Egyptian temple wisdom with Greek philosophical rigor. He was traditionally assigned a vast corpus of writings (the <i>Hermetica</i>), which were later categorized during the Renaissance into philosophical and technical (alchemical/magical) branches [emeraldtablet:page_1].
</p>

<h2>Academic Analysis</h2>
<p>
Renaissance Neoplatonists like Marsilio Ficino viewed Hermes as a <i>Prisca Theologia</i> figure—a contemporary of Moses who provided a pagan confirmation of Christian truths. However, seventeenth-century critical scholarship, led by Isaac Casaubon, correctly repositioned the Hermetic texts as products of late antiquity rather than ancient Egyptian antiquity [emeraldtablet:page_1]. Despite this 'demystification,' the figure of Hermes remained a potent symbol for the unity of the macrocosm and microcosm.
</p>
"""
    },
    "iamblichus": {
        "title": "Iamblichus of Chalcis",
        "bio": """
<p>
Iamblichus (c. 245–325 AD) was the Syrian Neoplatonist philosopher who decisively shifted the Platonic tradition toward theurgical practice. His magnum opus, <i>De Mysteriis Aegyptiorum</i> (On the Mysteries of the Egyptians), serves as the definitive defense of ritual magic as a necessary supplement to intellectual dialectic.
</p>

<h2>Academic Analysis</h2>
<p>
Iamblichus argued that human reason alone was insufficient for the soul's ascent to the One; instead, the soul required the 'ineffable' power of theurgy (divine work) mediated through material tokens or <i>synthemata</i>. Scholarly analysis by researchers such as Gregory Shaw has highlighted Iamblichus's role in creating a 'sacramental Neoplatonism' that deeply influenced later alchemical concepts of spirit inhabitating matter [emeraldtablet:page_1].
</p>
"""
    },
    "emerald_tablet": {
        "title": "The Emerald Tablet (Tabula Smaragdina)",
        "bio": """
<p>
The <i>Tabula Smaragdina</i> is arguably the most famous alchemical text in the Western world. Although brief—consisting of only about a dozen cryptic verses—it provides the foundation for the alchemical doctrine of correspondence: "That which is below is as that which is above."
</p>

<h2>Historical Context</h2>
<p>
The text's earliest known appearance is in Arabic works of the eighth or ninth century, specifically the <i>Kitab Sirr al-Khaliqa</i> (Book of the Secret of Creation), attributed to Apollonius of Tyana (Balinus). It was later translated into Latin in the twelfth century, where it became a foundational document for European alchemy [emeraldtablet:page_1].
</p>

<h2>Legacy and Scholarship</h2>
<p>
The Tablet has were interpreted through numerous lenses: Isaac Newton composed a famous translation and commentary, focusing on its cosmological implications, while the twentieth-century alchemist Fulcanelli saw in it a chemical recipe for the Philosopher's Stone. The 0-14 verse numbering scheme used in modern scholarship is an editorial imposition intended to facilitate cross-translation comparison [emeraldtablet:page_1].
</p>
"""
    }
}

def main():
    if not DB_PATH.exists():
        print("DB not found.")
        return

    conn = sqlite3.connect(DB_PATH)
    
    for eid, data in CLEAN_PROSE.items():
        print(f"Applying clean prose for: {data['title']}")
        
        # Ensure entity exists in persons or texts or concepts
        # For simplicity, we'll check where it fits best or just insert into persons/texts
        if eid == 'emerald_tablet':
            conn.execute("INSERT OR IGNORE INTO texts (text_id, title) VALUES (?, ?)", (eid, data['title']))
            conn.execute("UPDATE texts SET analysis_html = ? WHERE text_id = ?", (data['bio'], eid))
        else:
            conn.execute("INSERT OR IGNORE INTO persons (person_id, name) VALUES (?, ?)", (eid, data['title']))
            conn.execute("UPDATE persons SET bio_html = ? WHERE person_id = ?", (data['bio'], eid))
            
    conn.commit()
    conn.close()
    print("Clean prose update complete.")

if __name__ == "__main__":
    main()
