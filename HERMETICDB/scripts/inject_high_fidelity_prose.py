import sqlite3
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR.parent / "db" / "emerald_tablet.db"

SCHOLARLY_PROSE = {
    "hermes_trismegistus": """
        <p>Hermes Trismegistus, the "Thrice-Greatest Hermes," signifies the monumental fusion of the Egyptian god Thoth and the Greek deity Hermes. In the late antique period, he represents not merely a mythological figure but the legendary founder of alchemy, astrology, and theurgy. The <i>Corpus Hermeticum</i>, attributed to him, serves as the foundational pillar of the Western Esoteric tradition, bridging the divide between divine revelation and rigorous philosophical inquiry.</p>
        <h2>Historical Context</h2>
        <p>Emerging from the syncretism of Roman Egypt, the Hermetic figure became the "prisca theologia" for Renaissance scholars like Marsilio Ficino. He was regarded as a contemporary of Moses, a sage whose wisdom pre-dated the Greek philosophers and provided a unified theory of the cosmos, wherein the human soul (Mind or <i>Nous</i>) could achieve direct gnosis of the Divine.</p>
        <h2>Scholarly Significance</h2>
        <p>In modern scholarship, particularly the work of Garth Fowden and Wouter Hanegraaff, Hermes is understood as an "urban shaman" or a symbol of the technical and philosophical expertise found in the sacred libraries of Alexandria. His legacy defines the "Way of Hermes," a path of transformative knowledge that continues to inform modern esoteric and philosophical discourse.</p>
    """,
    "zosimos_of_panopolis": """
        <p>Zosimos of Panopolis (fl. c. 300 CE) remains the most significant historical figure in early Greco-Egyptian alchemy. His extant writings, preserved in the <i>Stobaeus</i> fragments and various Syriac translations, represent the transition from operative metallurgy to spiritualized "chymical" philosophy. Zosimos is the first to articulate the internal, psychological dimensions of the alchemical process, famously depicted in his <i>Visions</i>.</p>
        <h2>Historical Context</h2>
        <p>Operating in late antique Alexandria, Zosimos integrated Hermetic gnosis with Gnostic and Neopythagorean elements. He emphasized the "Spirit" (<i>pneuma</i>) within matter and the necessity of liberating the "inner human" from the planetary constraints of fate (<i>Heimarmene</i>).</p>
        <h2>Scholarly Significance</h2>
        <p>Scholars such as Matteo Martelli have highlighted Zosimos's role in documenting the technical apparatus of the ancient laboratory while simultaneously providing the earliest sophisticated theoretical framework for the transmutation of metals as a mirror of the soul's purification.</p>
    """,
    "iamblichus_of_chalcis": """
        <p>Iamblichus of Chalcis (c. 245–325 CE) was the Syrian Neoplatonist who revolutionized the Platonic tradition by introducing theurgy (divine work) as the essential culmination of philosophy. His masterpiece, <i>De Mysteriis Aegyptiorum</i>, provided the definitive defense of ritual practice against the rationalist critiques of his predecessor, Porphyry.</p>
        <h2>Historical Context</h2>
        <p>Iamblichus argued that the human soul, being profoundly "descended" into matter, could not achieve union with the One through dialectic alone. Instead, he posited that the gods had embedded <i>synthemata</i> (divine tokens) within the material world, which could be activated through right ritual to elevate the practitioner.</p>
        <h2>Scholarly Significance</h2>
        <p>Contemporary analysis by Gregory Shaw has rehabilitated Iamblichus as a "theurgist of the city," whose system provided a sophisticated ecological and sacramental framework for the interaction between humanity, nature, and the divine. His influence on the later Hermetic and alchemical traditions cannot be overstated.</p>
    """,
    "jabir_ibn_hayyan": """
        <p>Jābir ibn Ḥayyān, latinized as Geber, is arguably the most influential figure in the history of Islamic and Western alchemy. The "Jabirian Corpus" (<i>Kutub al-Mawazin</i>) represents a massive intellectual project to categorize all knowledge under the science of Balance (<i>‘ilm al-mīzān</i>), integrating Aristotelian physics with Pythagorean numerology.</p>
        <h2>Historical Context</h2>
        <p>Active during the 8th and early 9th centuries in Kufa and Baghdad, Jābir is credited with the development of the Sulfur-Mercury theory of metals, which dominated alchemical thought for a millennium. His work represents the first rigorous attempt to provide a mathematical and philosophical foundation for the transmutation of substances.</p>
        <h2>Scholarly Significance</h2>
        <p>Paul Kraus and later William Newman have analyzed the radical materialism and sophisticated experimentalism of the Jābirian tradition. Jābir serves as the crucial link between late antique Hermeticism and the "New Chymistry" of the Latin Middle Ages, defining the laboratory as a site of both physical transformation and cosmological revelation.</p>
    """,
    "marsilio_ficino": """
        <p>Marsilio Ficino (1433–1499) was the architect of the Renaissance revival of Platonism and Hermeticism. As the head of the Platonic Academy in Florence, under the patronage of Cosimo de' Medici, Ficino translated the <i>Corpus Hermeticum</i> into Latin (1463), an event that fundamentally altered the course of Western intellectual history.</p>
        <h2>Historical Context</h2>
        <p>Ficino's <i>Pymander</i> translation made the "Way of Hermes" accessible to the European elite, sparking a fascination with natural magic, astrology, and the concept of the <i>Anima Mundi</i> (World Soul). His work established Hermes Trismegistus as a central figure in the genealogy of wisdom (<i>prisca theologia</i>) stretching back to the dawn of humanity.</p>
        <h2>Scholarly Significance</h2>
        <p>Scholars such as Frances Yates have defined the "Ficinian moment" as the birth of the Hermetic tradition in the West. Ficino's integration of Neoplatonic philosophy with Christian theology provided the framework for the Renaissance Magus, whose role was to "harmonize" with the celestial influences for the benefit of the human condition.</p>
    """,
    "john_dee": """
        <p>John Dee (1527–1608) represents the pinnacle of the English Renaissance polymath and occultist. As the court astronomer to Queen Elizabeth I, Dee's intellectual journey spanned from maritime navigation to the most cryptic realms of angelic communication and Hermetic geometry.</p>
        <h2>Historical Context</h2>
        <p>His 1564 work <i>Monas Hieroglyphica</i> attempted to explain the fundamental unity of the cosmos through a single, mystical symbol. For Dee, the "Monad" was a mathematical and spiritual key that could unlock the secrets of both the material and celestial worlds, reflecting the Hermetic axiom "As Above, So Below."</p>
        <h2>Scholarly Significance</h2>
        <p>Nicholas Clulee and others have explored the tensions in Dee's career between rigorous science and esoteric experimentation. His work remains a primary subject for the study of the "scientific revolution" and the role of Hermeticism in the development of early modern intellectual life.</p>
    """,
    "emerald_tablet": """
        <p>The <i>Emerald Tablet</i> (Tabula Smaragdina) is arguably the most famous and enigmatic text in the Hermetic tradition. Consisting of a few cryptic verses, it articulates the foundational principles of alchemy and the essential unity of all levels of existence through the operation of the "One Thing."</p>
        <h2>Historical Context</h2>
        <p>While legendary accounts attribute the tablet to Hermes Trismegistus himself (found in a hidden chamber), historical scholarship traces its origin to the Arabic <i>Kitāb Sirr al-Khalīqa</i> (Book of the Secret of Creation), likely composed in the 8th or 9th century. Its translation into Latin in the 12th century sparked a centuries-long tradition of commentary and operative alchemical practice.</p>
        <h2>Scholarly Significance</h2>
        <p>Scholars like Julius Ruska and Eric Holmyard have mapped the complex transmission of the Tablet from the Islamic world to the Latin West. Its succinct phrases, such as "That which is below is like that which is above," have provided the central axiom for the Western Esoteric tradition, influencing everyone from medieval alchemists to Isaac Newton.</p>
    """,
    "monas_hieroglyphica": """
        <p>The <i>Monas Hieroglyphica</i> (1564) is the cryptic and profound masterpiece of John Dee. Through a single, intricate symbol composed of the cross, the crescent, and the circle, Dee attempted to demonstrate the structural unity of the universe, the metals, and the human soul.</p>
        <h2>Historical Context</h2>
        <p>Written in a state of intense inspiration in Antwerp, the work was dedicated to Emperor Maximilian II. It represents the height of Renaissance "Mathematical Magic," where geometry is understood not as an abstract abstraction but as a living bridge between the divine mind and material reality.</p>
        <h2>Scholarly Significance</h2>
        <p>Contemporary historiography, particularly the work of Håkan Håkansson, has analyzed the <i>Monas</i> as a culmination of Hermetic and Cabalistic traditions. It remains a definitive text for understanding the Renaissance effort to find a "Universal Science" that integrated all fields of knowledge into a single, divine symbol.</p>
    """
}

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for eid, prose in SCHOLARLY_PROSE.items():
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
    print("Payload injection complete.")

if __name__ == "__main__":
    main()
