import sqlite3
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR.parent / "db" / "emerald_tablet.db"

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Expand Concepts
    concepts = [
        ("tria_prima", "Tria Prima", "Salt, Sulfur, Mercury", "ALCHEMICAL", "The three primes introduced by Paracelsus: salt (body/solid), sulfur (soul/combustible), and mercury (spirit/fluid).", "The foundational theory of Paracelsian iatrochemistry.", "SEED_DATA", "REVIEWED", "HIGH"),
        ("archeus", "Archeus", "Inner Alchemist", "PHILOSOPHICAL", "The vital, animating force within living beings.", "Paracelsian concept that guides the body's internal functions and separates the pure from the impure.", "SEED_DATA", "REVIEWED", "HIGH"),
        ("lapis_philosophorum", "Lapis Philosophorum", "Philosopher's Stone", "ALCHEMICAL", "The ultimate goal of alchemy, capable of transmuting base metals into gold or granting immortality.", "Central mythos of Western alchemy, later interpreted spiritually as enlightenment or integration.", "SEED_DATA", "REVIEWED", "HIGH"),
        ("anima_mundi", "Anima Mundi", "World Soul", "COSMOLOGICAL", "The universal essence that connects all living things.", "A foundational Hermetic and Neoplatonic concept explaining sympathies between disparate phenomena.", "SEED_DATA", "REVIEWED", "HIGH"),
        ("solve_et_coagula", "Solve et Coagula", "Dissolve and Coagulate", "ALCHEMICAL", "The fundamental alchemical operation of breaking down a substance and recombining it into a higher form.", "Serves as both a practical laboratory instruction and a metaphor for spiritual transformation.", "SEED_DATA", "REVIEWED", "HIGH"),
        ("chrysopoeia", "Chrysopoeia", "Transmutation", "ALCHEMICAL", "The specific alchemical process of making gold from base metals.", "Often contrasted with iatrochemistry, it was the classical pursuit of medieval alchemists.", "SEED_DATA", "REVIEWED", "HIGH"),
        ("prima_materia", "Prima Materia", "First Matter", "COSMOLOGICAL", "The original, formless substance from which all things in the universe were created.", "The starting point of the Great Work in alchemy, requiring the alchemist to reduce their subject to this state.", "SEED_DATA", "REVIEWED", "HIGH")
    ]

    for c in concepts:
        try:
            cursor.execute("""
                INSERT INTO concepts (slug, label, label_alt, category, definition_short, definition_long, source_method, review_status, confidence)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, c)
        except sqlite3.IntegrityError:
            pass

    # Expand Persons (Key figures and scholars)
    persons = [
        ("john_dee", "John Dee", "Dr. John Dee", 1527, 1608, "Renaissance", "SCHOLAR", "English mathematician, astronomer, astrologer, occult philosopher, and advisor to Queen Elizabeth I.", "<p>John Dee was a pivotal figure in Renaissance thought, bridging the worlds of science and magic. He amassed one of the largest libraries in England and sought contact with angels to uncover the universal language of creation, leading to the Enochian system.</p>", "SEED_DATA", "REVIEWED", "HIGH"),
        ("kenelm_digby", "Sir Kenelm Digby", "Kenelm Digby", 1603, 1665, "Early Modern", "SCHOLAR", "English courtier, natural philosopher, and alchemist, famously associated with the Powder of Sympathy.", "<p>Sir Kenelm Digby was a prominent English Catholic and polymath. His most famous contribution to the history of science and magic was the 'Powder of Sympathy', a form of sympathetic magic that supposedly healed wounds at a distance by applying a powder to the weapon that caused the injury.</p>", "SEED_DATA", "REVIEWED", "HIGH"),
        ("elias_ashmole", "Elias Ashmole", None, 1617, 1692, "Early Modern", "SCHOLAR", "English antiquary, politician, and student of astrology and alchemy.", "<p>Ashmole preserved much of the English alchemical heritage in his massive compilation <i>Theatrum Chemicum Britannicum</i>. He was also an early Freemason and a founding fellow of the Royal Society.</p>", "SEED_DATA", "REVIEWED", "HIGH"),
        ("frances_yates", "Frances Yates", "Dame Frances Amelia Yates", 1899, 1981, "Modern", "SCHOLAR", "British historian focused on the study of the Renaissance and Western esotericism.", "<p>Yates revolutionized the academic study of Hermeticism with her 1964 book <i>Giordano Bruno and the Hermetic Tradition</i>, arguing that the Hermetic tradition was a key catalyst for the Scientific Revolution.</p>", "SEED_DATA", "REVIEWED", "HIGH"),
        ("carl_jung", "Carl Jung", "Carl Gustav Jung", 1875, 1961, "Modern", "SCHOLAR", "Swiss psychiatrist and psychoanalyst who founded analytical psychology.", "<p>Jung recognized deep psychological meaning in alchemical symbolism. In works like <i>Psychology and Alchemy</i>, he posited that alchemical texts were projections of unconscious processes, primarily the process of individuation.</p>", "SEED_DATA", "REVIEWED", "HIGH"),
        ("antoine_faivre", "Antoine Faivre", None, 1934, 2021, "Modern", "SCHOLAR", "French scholar of Western esotericism.", "<p>Faivre provided the first rigorous academic framework for defining Western esotericism as a field of study, identifying four fundamental characteristics: correspondences, living nature, imagination/mediations, and experience of transmutation.</p>", "SEED_DATA", "REVIEWED", "HIGH"),
        ("wouter_hanegraaff", "Wouter Hanegraaff", "Wouter J. Hanegraaff", 1961, None, "Modern", "SCHOLAR", "Dutch historian of religion and leading academic in the study of Western esotericism.", "<p>Hanegraaff's work, particularly <i>Esotericism and the Academy</i>, explores how the concept of 'esotericism' was constructed as a category of rejected knowledge during the Enlightenment.</p>", "SEED_DATA", "REVIEWED", "HIGH")
    ]

    for p in persons:
        try:
            cursor.execute("""
                INSERT INTO persons (person_id, name, name_alt, birth_year, death_year, era, role_primary, description, bio_html, source_method, review_status, confidence)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, p)
        except sqlite3.IntegrityError:
            pass

    # Expand Texts
    texts = [
        ("yates_bruno_hermetic", "Giordano Bruno and the Hermetic Tradition", "Giordano Bruno and the Hermetic Tradition", "ENGLISH", "COMPILATION", 1964, 1964, "Groundbreaking scholarly work by Frances Yates.", "<p>Yates argued that Giordano Bruno was not primarily a martyr for modern science but rather a Hermetic magus whose heliocentric views were rooted in an Egyptian revivalist cosmology based on the Corpus Hermeticum.</p>", "Groundbreaking for academic study of esoteric currents.", "SEED_DATA", "REVIEWED", "HIGH"),
        ("theatrum_chemicum_britannicum", "Theatrum Chemicum Britannicum", "Theatrum Chemicum Britannicum", "ENGLISH", "COMPILATION", 1652, 1652, "Extensive collection of English alchemical poetry compiled by Elias Ashmole.", "<p>This work preserved many important alchemical poems, including those by Thomas Norton, George Ripley, and Geoffrey Chaucer, accompanied by Ashmole's extensive annotations and engravings by Robert Vaughan.</p>", "Preserved a distinctively English alchemical tradition.", "SEED_DATA", "REVIEWED", "HIGH"),
        ("psychology_and_alchemy", "Psychology and Alchemy", "Psychologie und Alchemie", "GERMAN", "TREATISE", 1944, 1944, "A major work by Carl Jung connecting alchemical symbolism to psychoanalysis.", "<p>Jung demonstrated that the symbols found in alchemical texts were analogous to those emerging in the dreams of his patients, viewing the alchemical <i>opus</i> as a metaphor for psychological integration.</p>", "Influential in shaping 20th-century psychological approaches to esotericism.", "SEED_DATA", "REVIEWED", "HIGH"),
        ("esotericism_and_the_academy", "Esotericism and the Academy", "Esotericism and the Academy: Rejected Knowledge in Western Culture", "ENGLISH", "TREATISE", 2012, 2012, "Key historiographical work by Wouter Hanegraaff.", "<p>Traces the intellectual history of how 'magic', 'alchemy', and 'occultism' were excluded from academic discourse to define the boundaries of rationalism and Protestant orthodoxy.</p>", "Definitive work on the historiography of the field.", "SEED_DATA", "REVIEWED", "HIGH"),
        ("fama_fraternitatis", "Fama Fraternitatis", "Fama Fraternitatis Roseae Crucis", "GERMAN", "PRIMARY_SOURCE", 1614, 1614, "The first Rosicrucian manifesto.", "<p>An anonymous text announcing the existence of a secret brotherhood founded by Christian Rosenkreutz, calling for a universal reformation of mankind through the integration of alchemical and Paracelsian thought.</p>", "Sparked the 'Rosicrucian furor' across Europe.", "SEED_DATA", "REVIEWED", "HIGH"),
        ("chymical_wedding", "Chymical Wedding of Christian Rosenkreutz", "Chymische Hochzeit Christiani Rosencreutz anno 1459", "GERMAN", "PRIMARY_SOURCE", 1616, 1616, "The third Rosicrucian manifesto, an allegorical romance.", "<p>A highly symbolic narrative describing the journey of Christian Rosenkreutz to a royal wedding, representing the alchemical marriage of the soul and spirit.</p>", "Deeply influential on later esoteric orders like the Golden Dawn.", "SEED_DATA", "REVIEWED", "HIGH"),
        ("monas_hieroglyphica", "Monas Hieroglyphica", "Monas Hieroglyphica", "LATIN", "TREATISE", 1564, 1564, "An esoteric treatise by John Dee explaining his symbol, the Hieroglyphic Monad.", "<p>Dee's Monas was presented as a unified cosmic symbol combining the planetary, zodiacal, and alchemical signs, offering a profound mathematical and kabbalistic exegesis of creation.</p>", "A foundational text for later Rosicrucian currents.", "SEED_DATA", "REVIEWED", "HIGH")
    ]

    for t in texts:
        try:
            cursor.execute("""
                INSERT INTO texts (text_id, title, title_original, language, text_type, date_composed_start, date_composed_end, description, analysis_html, transmission_notes, source_method, review_status, confidence)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, t)
        except sqlite3.IntegrityError:
            pass

    # Expand Timeline Events
    timeline_events = [
        (1471, None, "TRANSLATION", "Ficino translates Corpus Hermeticum", "Marsilio Ficino completes the Latin translation of the Corpus Hermeticum.", "<p>Commissioned by Cosimo de' Medici, Marsilio Ficino translated the Greek manuscript of the Corpus Hermeticum (Pimander) into Latin, sparking the Renaissance revival of Hermetic philosophy.</p>", None, None, None, "HIGH"),
        (1564, None, "PUBLICATION", "Publication of Monas Hieroglyphica", "John Dee publishes his mathematical-magical treatise.", "<p>John Dee publishes the <i>Monas Hieroglyphica</i> in Antwerp, a complex mystical treatise explaining his unified symbol of the cosmos.</p>", None, None, None, "HIGH"),
        (1614, None, "PUBLICATION", "Publication of Fama Fraternitatis", "The first Rosicrucian manifesto is published anonymously in Kassel.", "<p>The publication of the <i>Fama Fraternitatis</i> catalyzed the Rosicrucian movement, proclaiming a general reformation of divine and human understanding.</p>", None, None, None, "HIGH"),
        (1616, None, "PUBLICATION", "Publication of Chymical Wedding", "The Chymical Wedding of Christian Rosenkreutz is published in Strasbourg.", "<p>Johann Valentin Andreae is believed to have authored this allegorical alchemical romance, serving as the third and final foundational Rosicrucian text.</p>", None, None, None, "HIGH"),
        (1652, None, "PUBLICATION", "Publication of Theatrum Chemicum Britannicum", "Elias Ashmole publishes a compilation of English alchemical poetry.", "<p>Ashmole's work systematically gathered the scattered manuscript traditions of English alchemy, ensuring their survival for later generations.</p>", None, None, None, "HIGH"),
        (1658, None, "PUBLICATION", "Digby's Discourse on the Powder of Sympathy", "Sir Kenelm Digby delivers his famous discourse at Montpellier.", "<p>Digby argued for the efficacy of weapon-salve and sympathetic magic based on a naturalistic philosophy of effluvia and atomic action, blending hermetic ideas with the new mechanical philosophy.</p>", None, None, None, "HIGH"),
        (1944, None, "SCHOLARSHIP", "Jung publishes Psychology and Alchemy", "Carl Jung introduces his psychological interpretation of alchemy.", "<p>Jung argued that the alchemical process of transmuting base matter into gold was an allegory for the psychological process of individuation.</p>", None, None, None, "HIGH"),
        (1964, None, "SCHOLARSHIP", "Yates publishes Giordano Bruno and the Hermetic Tradition", "Frances Yates shifts the paradigm of Renaissance history.", "<p>Yates's book firmly established the importance of the 'Hermetic tradition' as a major intellectual force in the early modern period, profoundly influencing subsequent scholarship.</p>", None, None, None, "HIGH"),
        (2012, None, "SCHOLARSHIP", "Hanegraaff publishes Esotericism and the Academy", "Wouter Hanegraaff explores the historiography of Western esotericism.", "<p>Hanegraaff traces the invention of 'esotericism' as a polemical category, showing how it was excluded from standard academic disciplines during the Enlightenment.</p>", None, None, None, "HIGH")
    ]

    # Resolve IDs for timeline events where possible
    for te in timeline_events:
        cursor.execute("SELECT id FROM persons WHERE person_id = ?", ("john_dee",))
        dee_id = cursor.fetchone()
        
        # We will just insert them directly without full foreign key resolution for now to simplify
        try:
            cursor.execute("""
                INSERT INTO timeline_events (year, year_end, event_type, title, description, description_long, person_id, text_id, bib_id, confidence)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, te)
        except sqlite3.IntegrityError:
            pass

    conn.commit()
    conn.close()
    print("Database expanded successfully.")

if __name__ == "__main__":
    main()
