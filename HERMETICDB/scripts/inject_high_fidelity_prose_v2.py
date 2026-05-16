import sqlite3
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR.parent / "db" / "emerald_tablet.db"

SCHOLARLY_PROSE_V2 = {
    "paracelsus": """
        <p>Theophrastus von Hohenheim, known as Paracelsus (1493–1541), remains one of the most radical and disruptive figures in the history of science and magic. A Swiss-German physician, alchemist, and lay theologian, he sought to overthrow the prevailing Galenic medical orthodoxy, proposing instead a system of "iatrochemistry" rooted in the <i>Tria Prima</i>: Salt, Sulfur, and Mercury.</p>
        <h2>Historical Context</h2>
        <p>Paracelsus’s career was marked by itinerant wandering across Europe, during which he gathered folk knowledge and combined it with a profound, if idiosyncratic, Hermetic worldview. He emphasized the "inner alchemist" (the <i>Archeus</i>) and the essential correspondence between the macrocosm of the heavens and the microcosm of the human body. His rejection of academic tradition and his use of the vernacular made him a hero to later Rosicrucians and medical reformers.</p>
        <h2>Scholarly Significance</h2>
        <p>In modern historiography, the work of Walter Pagel and Andrew Weeks has emphasized Paracelsus as a bridge between medieval vitalism and modern biochemistry. His alchemical theories were not merely about the transmutation of gold, but about the "transmutation" of medicine into a spiritual and chemical discipline of healing, defining the paracelsian "chemical philosophy" that dominated the 17th century.</p>
    """,
    "michael_maier": """
        <p>Michael Maier (1568–1622) was a German physician, counselor to Emperor Rudolf II, and one of the most sophisticated "emblematic" alchemists of the early modern period. He is best known for his <i>Atalanta Fugiens</i> (1617), a masterpiece that combined stunning copperplate engravings, cryptic alchemical verses, and original musical fugues.</p>
        <h2>Historical Context</h2>
        <p>Operating in the intellectual hothouse of Prague and later England, Maier was deeply involved with the incipient Rosicrucian movement. He understood alchemy as a profound psycho-spiritual and historical mystery, often interpreting Greek and Egyptian mythology as encoded alchemical instructions. His work represents the high point of the "Hermetic-Cabalistic" synthesis of the Renaissance.</p>
        <h2>Scholarly Significance</h2>
        <p>Scholarship by H.M.E. de Jong and Hereward Tilton has analyzed Maier's use of multisensory stimuli—visual, textual, and auditory—to lead the practitioner toward a total Hermetic gnosis. Maier did not merely write about alchemy; he created an "audio-visual" ritual environment intended to catalyze the transformation of the viewer's intellect.</p>
    """,
    "heinrich_khunrath": """
        <p>Heinrich Khunrath (c. 1560–1605) was a Paracelsian physician and the foremost proponent of "Amphitheatrical" or "theosophical" alchemy. His seminal work, <i>Amphitheatrum Sapientiae Aeternae</i> (Amphitheater of Eternal Wisdom), is famous for its intricate, circular engravings that depict the alchemist's laboratory as a temple of prayer and laboratory investigation (<i>Oratorium-Laboratorium</i>).</p>
        <h2>Historical Context</h2>
        <p>Khunrath's system integrated Hermeticism with Christian Cabala and Lutheran mysticism. He posited that the alchemical quest required both physical labor and divine "re-birth." His iconography serves as a roadmap for the "Theosophia," where the physical discovery of the Philosopher's Stone is identical to the spiritual discovery of Christ (the <i>Lapis-Christos</i> parallel).</p>
        <h2>Scholarly Significance</h2>
        <p>Peter Forshaw’s work has been instrumental in decrypting Khunrath’s complex visual rhetoric. Khunrath is seen as a key figure in the "Sapiential" tradition of alchemy, where the search for wisdom (<i>Sapientia</i>) is the ultimate goal of all chemical and philosophical operations.</p>
    """,
    "robert_fludd": """
        <p>Robert Fludd (1574–1637) was an English Paracelsian physician and polymath whose massive multivolume works, such as the <i>Utriusque Cosmi Historia</i>, attempted to document the entire history and structure of the two worlds: the macrocosm and the microcosm. His work is celebrated for its breathtakingly detailed and symbolic illustrations of the cosmic machine.</p>
        <h2>Historical Context</h2>
        <p>Fludd was a fierce defender of the Rosicrucian manifestos and a critic of the nascent experimental philosophy of his time (notably engaging in a famous debate with Johannes Kepler). His cosmology was rooted in the Hermetic "monochord," a musical metaphor for the harmonious ordering of the universe by the divine hand.</p>
        <h2>Scholarly Significance</h2>
        <p>Contemporary scholars like Joscelyn Godwin have highlighted Fludd's role as a preserver of the Renaissance Hermetic tradition into the 17th century. His work provides the most complete visual encyclopedia of the Hermetic worldview, mapping everything from the celestial hierarchies to the anatomy of the human soul onto a single, unified philosophical grid.</p>
    """,
    "splendor_solis": """
        <p>The <i>Splendor Solis</i> (Splendor of the Sun) is widely considered the most beautiful alchemical manuscript ever produced. Attributed to the legendary Salomon Trismosin, the teacher of Paracelsus, the manuscript is famous for its 22 extraordinary full-page miniatures, which depict the alchemical process through a series of mythological and laboratory allegories.</p>
        <h2>Historical Context</h2>
        <p>The earliest versions of the manuscript date to the 1530s, emerging from the workshop contexts of Nuremberg and southern Germany. The miniatures—such as the "Philosopher's Stone in a Flask" and the "Red Stone"—utilize vibrant colors and gold leaf to signify the internal radiance of the alchemical <i>materia</i> as it progresses toward perfection.</p>
        <h2>Scholarly Significance</h2>
        <p>The work provides a definitive visual summary of medieval alchemical theory (the Sulfur-Mercury theory) while anticipating the emblematic complexity of the Renaissance. Recent facsimiles and studies have highlighted its role in late-medieval courtly culture, where alchemy was viewed as a "regal art" deserving of the highest artistic patronage.</p>
    """
}

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for eid, prose in SCHOLARLY_PROSE_V2.items():
        # Check if it's a person
        cursor.execute("SELECT name FROM persons WHERE person_id = ?", (eid,))
        if cursor.fetchone():
            print(f"Injecting scholarly bio for {eid}...")
            cursor.execute("UPDATE persons SET bio_html = ? WHERE person_id = ?", (prose, eid))
        else:
            # Check if it's a text
            cursor.execute("SELECT title FROM texts WHERE text_id = ?", (eid,))
            if cursor.fetchone():
                print(f"Injecting scholarly analysis for {eid}...")
                cursor.execute("UPDATE texts SET analysis_html = ? WHERE text_id = ?", (prose, eid))
    
    conn.commit()
    conn.close()
    print("Payload injection Volume 2 complete.")

if __name__ == "__main__":
    main()
