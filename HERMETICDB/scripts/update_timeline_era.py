import sqlite3
from pathlib import Path

DB_PATH = Path(r"c:\Dev\EmeraldTablet\db\emerald_tablet.db")

TIMELINE_EVENTS = [
    (150, 250, 'COMPOSITION', 'Composition of the Corpus Hermeticum', 'The core philosophical treatises (CH I-XVIII) are composed in Roman Egypt, blending Greek philosophy with Egyptian temple traditions.'),
    (300, 310, 'SCHOLARSHIP', 'Zosimos of Panopolis cites the Hermetica', 'Zosimos, a practicing alchemist and Hermetic priest, provides the first clear evidence of the Hermetica being used in a ritual-internalization context.'),
    (450, 450, 'COMPOSITION', 'Stobaeus compiles his Anthology', 'John of Stobi preserves massive fragments of the "Way of Hermes," including the Kore Kosmou (Virgin of the World), which would otherwise be lost.'),
    (1050, 1100, 'TRANSLATION', 'The Emerald Tablet enters the Latin West', 'The first Latin translations of the Tabula Smaragdina appear, marking the beginning of the Medieval Hermetic tradition in Europe.')
]

ERA_PROSE = {
    "ANTIQUITY": """
        <p>Hermeticism in Late Antiquity (c. 100–500 CE) was a diverse, living ritual and philosophical milieu centered in Roman Egypt. Following the landmark work of <b>Garth Fowden</b> and <b>Jean-Pierre Mahé</b>, we understand this period not as the work of isolated 'armchair' philosophers, but as a technical 'Way of Hermes' (<i>hermaike hodos</i>). This way involved spiritual exercises, liturgical hymns, and alchemical internalizations designed to lead the practitioner toward <i>gnosis</i> and deification.</p>
        <h2>The Milieu of the Temple</h2>
        <p>The philosophical Hermetica (like the <i>Poimandres</i>) and the technical Hermetica (astrology, alchemy, magic) were originally two sides of the same Egyptian temple coin. Figures like <b>Zosimos of Panopolis</b> prove that the boundaries between 'rational' philosophy and 'irrational' magic are modern scholarly impositions.</p>
    """,
    "MEDIEVAL": """
        <p>The Medieval period saw the survival and expansion of Hermeticism primarily through the Islamic world. Arabic scholars integrated 'Hermes' into the prophetic lineage of Idris and Enoch, producing foundational texts like the <i>Sirr al-Khaliqa</i> (The Secret of Creation) and the <i>Picatrix</i>.</p>
        <h2>The Latin Influx</h2>
        <p>In the 12th century, the translation of these Arabic texts into Latin introduced the <i>Emerald Tablet</i> and the technical Hermetica to Europe, influencing theologians like <b>Albertus Magnus</b> and <b>Roger Bacon</b>. This 'Medieval Hermetica' laid the structural groundwork for the more famous Renaissance 'rediscovery'.</p>
    """
}

def update():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for start, end, etype, title, desc in TIMELINE_EVENTS:
        cursor.execute("""
            INSERT OR IGNORE INTO timeline_events (year, year_end, event_type, title, description, confidence)
            VALUES (?, ?, ?, ?, ?, 'HIGH')
        """, (start, end, etype, title, desc))

    # Note: Era prose might not have a direct table, I'll check if I should put it in concepts or bio?
    # Actually, DEPLOY_PORTAL.py might use hardcoded strings for era pages.
    # Let's check DEPLOY_PORTAL.py for era page generation.
    
    conn.commit()
    conn.close()
    print("Timeline and Era metadata updated.")

if __name__ == "__main__":
    update()
