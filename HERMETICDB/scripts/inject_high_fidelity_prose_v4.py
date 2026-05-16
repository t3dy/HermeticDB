import sqlite3
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR.parent / "db" / "emerald_tablet.db"

SCHOLARLY_PROSE_V4 = {
    "albertus_magnus": """
        <p>Albertus Magnus (c. 1200–1280), the <i>Doctor Universalis</i>, was a German Dominican friar and bishop who became one of the most influential scholars of the Middle Ages. He is celebrated for his vast efforts to integrate Aristotelian philosophy with Christian theology and for his extensive empirical observations in the natural sciences.</p>
        <h2>Historical Context</h2>
        <p>Albertus was the teacher of Thomas Aquinas and a pivotal figure in the University of Paris. His interest in alchemy was both theoretical and practical; while he was cautious of the occult, he viewed the study of metals as a legitimate branch of natural philosophy. Legendary accounts attribute to him the creation of a "brazen head" and the discovery of the Philosopher's Stone, reflecting his reputation as a master of both divine and material secrets.</p>
        <h2>Scholarly Significance</h2>
        <p>Modern research, such as that by Pearl Kibre, has identified a significant corpus of alchemical texts (the <i>Semita Recta</i>) attributed to Albertus, though their authenticity is debated. Regardless of authorship, his endorsement of the "chemical path" provided the necessary ecclesiastical cover for the development of medieval alchemy as a serious intellectual pursuit.</p>
    """,
    "roger_bacon": """
        <p>Roger Bacon (c. 1214–1292), known as the <i>Doctor Mirabilis</i>, was an English Franciscan friar and polymath. He is often cited as an early advocate of the experimental method (<i>scientia experimentalis</i>), arguing that reasoning alone could never provide certainty without the confirmation of experience.</p>
        <h2>Historical Context</h2>
        <p>Bacon’s <i>Opus Maius</i>, sent to Pope Clement IV, envisioned a total reform of the sciences, including alchemy, which he divided into "speculative" and "operative" branches. He believed that alchemy could not only transform metals but also prolong human life (the Elixir of Life). His cryptic writings and interest in "miracles of art and nature" led to his later reputation as a sorcerer and the legendary inventor of gunpowder.</p>
        <h2>Scholarly Significance</h2>
        <p>Contemporary analysis by William Newman has highlighted Bacon's sophisticated understanding of the "art-nature" relationship. He saw alchemy as the highest form of natural philosophy, because it did not merely observe nature but perfected it through human intervention, a core Hermetic theme.</p>
    """,
    "giordano_bruno": """
        <p>Giordano Bruno (1548–1600) was an Italian Dominican friar, philosopher, and mathematical theorist who remains one of the most tragic and heroic figures of the Hermetic tradition. He is best known for his cosmological theories, which proposed an infinite universe with an infinite number of inhabited worlds, a vision that ultimately led to his execution by the Roman Inquisition.</p>
        <h2>Historical Context</h2>
        <p>Bruno was deeply immersed in the "Art of Memory" (<i>Mnemotechnics</i>) and the magical philosophy of the <i>Corpus Hermeticum</i>. He viewed himself as a Hermetic reformer whose mission was to restore the "ancient Egyptian religion" of the cosmos. For Bruno, the universe was a living, sentient organism (<i>Anima Mundi</i>), and the human mind could achieve divinity through the internalizing of cosmic images.</p>
        <h2>Scholarly Significance</h2>
        <p>The "Yates Thesis" (Frances Yates, 1964) revolutionized Bruno studies by identifying him not primarily as a modern scientist, but as a "Hermetic Magus." While later scholars like Hillary Gatti have emphasized his mathematical and logical rigour, his synthesis of infinite cosmology and Hermetic gnosis remains a defining moment in the transition to the modern era.</p>
    """,
    "cornelius_agrippa": """
        <p>Heinrich Cornelius Agrippa von Nettesheim (1486–1535) was the most famous occult scholar of the Renaissance. His encyclopedic work, <i>De Occulta Philosophia Libri Tres</i> (Three Books of Occult Philosophy), provided the definitive systematic defense of magic as a noble and pious discipline, integrating the Hermetic, Neoplatonic, and Cabalistic traditions.</p>
        <h2>Historical Context</h2>
        <p>Agrippa’s career was marked by controversy and intellectual doubt. While his early work defended magic, his later <i>De Vanitate Scientiarum</i> seemed to reject all human knowledge, including the occult. This tension reflects the profound epistemological crisis of the early 16th century. His work became the "handbook" for the Renaissance magus, providing the theoretical blueprints for talismans, planetary magic, and the hierarchy of angels.</p>
        <h2>Scholarly Significance</h2>
        <p>Modern studies by Michael Keefer and others have analyzed Agrippa as a "Christian Hermeticist" attempting to find a unified science of the divine. His work serves as the crucial link between the high scholarship of Ficino and the practical grimoires of the later esoteric tradition.</p>
    """,
    "atalanta_fugiens": """
        <p>The <i>Atalanta Fugiens</i> (1617), authored by Michael Maier and illustrated with engravings by Matthäus Merian, is the most celebrated "emblem book" in the history of alchemy. It utilizes the myth of Atalanta’s race as a multi-layered allegory for the fugitive nature of the Philosopher's Stone and the necessity of persistence in the alchemical quest.</p>
        <h2>Historical Context</h2>
        <p>The work is unique for its inclusion of 50 musical fugues (musical "canons" for three voices) that accompany 50 emblems and 50 discourses. This was intended as a total "Hermetic experience," engaging the eyes, the ears, and the intellect simultaneously. Maier believed that musical harmony reflected the mathematical ordering of the cosmos, and that "hearing" the alchemical process was as important as "seeing" it.</p>
        <h2>Scholarly Significance</h2>
        <p>Scholars such as Joscelyn Godwin have decoded the musical and symbolic structures of the <i>Atalanta</i>, showing how it encodes the "Chemical Wedding" and the perfection of the <i>materia</i>. It remains a primary example of how the Hermetic tradition utilized fine art and music as tools for spiritual and cognitive transformation.</p>
    """
}

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for eid, prose in SCHOLARLY_PROSE_V4.items():
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
    print("Payload injection Volume 4 complete.")

if __name__ == "__main__":
    main()
