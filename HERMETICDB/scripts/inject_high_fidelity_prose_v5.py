import sqlite3
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR.parent / "db" / "emerald_tablet.db"

SCHOLARLY_PROSE_V5 = {
    "theurgy": """
        <p>Theurgy (from the Greek <i>theourgia</i>, "divine work") represents the ritual culmination of Neoplatonic and Hermetic philosophy. Unlike pure theology, which seeks to understand the divine through reason, theurgy uses sacred ritual, symbols (<i>synthemata</i>), and divine names to enact a direct experiential union with higher powers.</p>
        <h2>Historical Context</h2>
        <p>Principally developed by Iamblichus in his <i>De Mysteriis</i>, theurgy was a response to the "descended soul" problem. It argued that because humans are profoundly embedded in matter, they need material, divinely-instituted rituals to serve as a ladder back to the One. The practice involved the "animation" of statues, the invocation of planetary spirits, and the purifying of the subtle body (<i>okhema</i>).</p>
        <h2>Scholarly Significance</h2>
        <p>Contemporary scholars like Gregory Shaw have rehabilitated theurgy as a "sacramental philosophy" rather than a primitive magic. It is now understood as an essential bridge between a theoretical cosmology and a lived mystical experience, providing the blueprints for much of the later Western ritual magic tradition.</p>
    """,
    "gnosis": """
        <p>Gnosis (Greek for "knowledge") in the Hermetic tradition signifies a transformative, direct, and non-discursive insight into the nature of the divine and the true origin of the self. It is not merely a collection of facts (<i>episteme</i>) but a participatory awareness that results in the salvation and "re-birth" of the soul.</p>
        <h2>Historical Context</h2>
        <p>In the <i>Corpus Hermeticum</i>, Gnosis is the goal of the philosophical path. It involves the recognition that the human mind (<i>Nous</i>) is of the same essence as the divine Mind. Achieving Gnosis allows the practitioner to transcend the planetary spheres, cast off the garments of matter, and return to the "Ogdoad," the eighth sphere of the fixed stars, and beyond to the source of Light.</p>
        <h2>Scholarly Significance</h2>
        <p>Wouter Hanegraaff and others distinguish "Hermetic Gnosis" from the more pessimistic Gnosticism of the dualistic sects. Hermeticism generally views the cosmos as a beautiful, if distracting, mirror of the divine, and Gnosis as the key to harmonizing with that divine order while ultimately transcending it.</p>
    """,
    "nous": """
        <p>Nous, often translated as "Mind" or "Intellect," is the supreme ontological principle in Hermetic and Neoplatonic thought. It is the divine consciousness that structures and sustans the universe, often identified with the first emanation of the One or the supreme Godhead himself.</p>
        <h2>Historical Context</h2>
        <p>In the <i>Poimandres</i>, the first treatise of the <i>Corpus Hermeticum</i>, Nous appears as a majestic figure of light who reveals the secrets of creation to Hermes. The text teaches that every human being possesses a fragment of this universal Nous, which serves as the immortal spark and the organ of divine perception. To "live according to Nous" is to achieve the highest state of human existence.</p>
        <h2>Scholarly Significance</h2>
        <p>Scholars analyze the concept of Nous as the pivot point between the transcendent and the immanent. It is both the "Creator-Mind" (the Demiurge) and the "Saving-Mind" that calls the soul back to its origin, representing the intellectualized vitalism that defines the Hermetic worldview.</p>
    """,
    "prima_materia": """
        <p>The <i>Prima Materia</i> (First Matter) is the foundational concept of alchemical practice. It is the original, undifferentiated substance that exists at the beginning of the Great Work—a substance that is theoretically "everywhere and in everything" but remains hidden and "base" until purified.</p>
        <h2>Historical Context</h2>
        <p>Alchemists used hundreds of cryptic names for the Prima Materia: "Our Mercury," "The Virgin's Milk," "The Chaos," or "The Dragon." The goal of the first stage of alchemy (the <i>Nigredo</i> or Blackening) was to reduce matter back to this primal state, stripping away its specific forms so that a new, divine form could be imprinted upon it. In Hermetic terms, it represents the potentiality of the "One Thing" mentioned in the <i>Emerald Tablet</i>.</p>
        <h2>Scholarly Significance</h2>
        <p>Psychological interpretations by C.G. Jung viewed the Prima Materia as a symbol for the unconscious—the raw, chaotic material of the psyche that must be integrated to achieve wholeness (Individuation). Historiographical research emphasizes it as the alchemist's way of engaging with the "pre-cosmic" state of reality, a chemical re-enactment of Genesis.</p>
    """,
    "decans": """
        <p>The Decans are thirty-six 10-degree segments of the zodiac, each ruled by a specific spirit or deity. Emerging from ancient Egyptian astronomical practice, they became a central component of Hermetic "astrological magic" in late antiquity.</p>
        <h2>Historical Context</h2>
        <p>In the Hermetic <i>Sacred Book of Hermes to Asclepius</i>, the Decans are described as "forces" that govern the human body and the material world. Each Decan has a specific image (a <i>kharakter</i>) and associated talismans. By understanding the Decans, the Hermetic practitioner could mitigate the "Fate" (<i>Heimarmene</i>) of the planets, utilizing the Decanic spirits as intermediaries to the divine.</p>
        <h2>Scholarly Significance</h2>
        <p>Recent research by David Pingree and others has highlighted the Decans as the "secret heart" of the transmission of Egyptian influence into the Greek Hermetica. They represent the "technical" side of the tradition, where the celestial spheres are mapped with precision to enable the magus to navigate the powers of the heavens.</p>
    """
}

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for eid, prose in SCHOLARLY_PROSE_V5.items():
        # Update concept definition_long (where we store high fidelity prose for concepts)
        cursor.execute("UPDATE concepts SET definition_long = ? WHERE slug = ?", (prose, eid))
    
    conn.commit()
    conn.close()
    print("Payload injection Volume 5 complete (Concepts).")

if __name__ == "__main__":
    main()
