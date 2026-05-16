import sqlite3
from pathlib import Path

DB_PATH = Path(r"c:\Dev\EmeraldTablet\db\emerald_tablet.db")

DICTIONARY_EXTENSIONS = {
    "gnosis": """
        <p>Gnosis is the central goal of the Hermetic tradition. It is not mere intellectual knowledge (<i>episteme</i>), but a direct, experiential realization of the divine nature of the self and the cosmos. In the <i>Corpus Hermeticum</i>, Gnosis is described as a 'rebirth' (<i>palingenesia</i>) that transforms the practitioner into a 'child of the Mind'.</p>
        <p><b>Analytical Context:</b> Scholars distinguish between 'Hermetic Gnosis' and 'Gnostic Gnosis' (dualistic); the former tends to be more 'cosmic-optimistic,' viewing the world as a beautiful, if distracting, mirror of God.</p>
    """,
    "logos": """
        <p>The <i>Logos</i> (Word or Reason) is the creative instrument of the divine Mind. In the <i>Poimandres</i>, the Logos is a 'holy Word' that descends into the material elements to organize them into the cosmos. It serves as the mediator between the unknowable God and the manifest world.</p>
        <p><b>Philosophical Nuance:</b> The Hermetic Logos draws from both Stoic (the rational principle of the world) and Philonic (the divine mediator) traditions, representing the bridge between contemplation and creation.</p>
    """,
    "theurgy": """
        <p>Theurgy ('God-working') refers to ritual practices intended to invoke the presence of the gods or to achieve union with the divine. While the <i>Corpus Hermeticum</i> focuses on contemplative Gnosis, the <i>Asclepius</i> and technical Hermetica describe practical theurgic operations, such as the 'animation' of statues.</p>
        <p><b>Scholarly Distinction:</b> Theurgy is often distinguished from 'Goetia' (common magic) by its higher spiritual aims and its reliance on the principle of <i>Sympatheia</i> rather than the coercion of spirits.</p>
    """,
    "prisca_theologia": """
        <p>The <i>Prisca Theologia</i> (Ancient Theology) is a historiographical concept developed during the Renaissance, most notably by Marsilio Ficino. It holds that a single, primordial wisdom was revealed by God to ancient sages like Hermes Trismegistus, Zoroaster, and Orpheus, which eventually flowed into the works of Plato.</p>
        <p><b>Historical Impact:</b> This concept allowed Renaissance thinkers to harmonize Hermeticism and Neoplatonism with Christianity, viewing Hermes as an 'Ancient Prophet' who anticipated the mysteries of the Trinity.</p>
    """
}

def populate():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for slug, html in DICTIONARY_EXTENSIONS.items():
        cursor.execute("UPDATE concepts SET definition_long = ? WHERE slug = ?", (html, slug))

    conn.commit()
    conn.close()
    print("Dictionary extensive expansion complete.")

if __name__ == "__main__":
    populate()
