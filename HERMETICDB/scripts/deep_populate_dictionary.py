import sqlite3
from pathlib import Path

DB_PATH = Path(r"c:\Dev\EmeraldTablet\db\emerald_tablet.db")

DICTIONARY_EXPANSION = [
    # THEOLOGICAL / PHILOSOPHICAL
    ("heimarmene", "Heimarmene (Fate)", "The concept of destiny or astronomical fate in Hermeticism. In many treatises, the goal of the practitioner is to rise above the Heimarmene through Gnosis.", "ACTOR_TERM", "COSMOLOGICAL"),
    ("demiurge", "Demiurge", "The 'Craftsman' or creator god in Hermetic and Platonic thought. In the Poimandres, the Demiurge is the second Mind (Nous) who fashions the seven governors (planets).", "ACTOR_TERM", "COSMOLOGICAL"),
    ("anthropos", "Anthropos (Essential Man)", "The primordial, divine Human who falls into nature in the Poimandres myth. The return to the Anthropos is the goal of the Hermetic path.", "ACTOR_TERM", "THEOLOGICAL"),
    ("ogdoad", "Ogdoad (The Eighth)", "The eighth sphere, above the seven planetary spheres, where the soul begins its final union with the divine after death or during initiation.", "ACTOR_TERM", "THEOLOGICAL"),
    ("ennead", "Ennead (The Ninth)", "The ninth sphere, identified with the realm of God or the highest Mind, beyond the Ogdoad.", "ACTOR_TERM", "THEOLOGICAL"),
    ("pronoia", "Pronoia (Providence)", "The divine care or foresight that governs the cosmos, often contrasted with Heimarmene.", "ACTOR_TERM", "THEOLOGICAL"),
    ("ennoia", "Ennoia (Thought)", "The divine thought or conception from which the cosmos emerges.", "ACTOR_TERM", "PHILOSOPHICAL"),
    ("phronesis", "Phronesis (Practical Wisdom)", "A type of wisdom or mindfulness that allows the practitioner to navigate the material world without losing sight of the divine.", "ACTOR_TERM", "PHILOSOPHICAL"),
    ("unio_mystica", "Unio Mystica", "The mystical union between the practitioner and the divine Mind, the culmination of the 'Way of Hermes'.", "ANALYST_TERM", "THEOLOGICAL"),

    # HISTORIOGRAPHICAL / SCHOLARLY
    ("actor_category", "Actor Category", "A term or concept as understood by the historical practitioners (the 'actors') themselves, rather than as defined by modern scholars.", "ANALYST_TERM", "HISTORIOGRAPHICAL"),
    ("analyst_category", "Analyst Category", "A term or framework developed by modern scholars (the 'analysts') to study and categorize historical phenomena.", "ANALYST_TERM", "HISTORIOGRAPHICAL"),
    ("hermetism_vs_hermeticism", "Hermetism vs. Hermeticism", "A scholarly distinction often made between 'Hermetism' (the ancient Greek texts) and 'Hermeticism' (the broader Western esoteric tradition).", "ANALYST_TERM", "HISTORIOGRAPHICAL"),
    ("rejected_knowledge", "Rejected Knowledge", "Wouter Hanegraaff's term for the various traditions (including Hermeticism) that were excluded from mainstream Western academia during the Enlightenment.", "ANALYST_TERM", "HISTORIOGRAPHICAL"),
    ("prisca_theologia", "Prisca Theologia", "The 'Ancient Theology.' The Renaissance idea (championed by Ficino) that a single, true theology exists which was revealed to Hermes and other ancient sages.", "ACTOR_TERM", "HISTORIOGRAPHICAL"),
    ("perennialism", "Perennialism", "The belief that all the world's religious traditions share a single, universal truth or 'perennial philosophy'.", "ANALYST_TERM", "HISTORIOGRAPHICAL"),
    ("yates_paradigm", "The Yates Paradigm", "The influential (and now heavily debated) thesis by Frances Yates that Hermeticism was the primary catalyst for the Scientific Revolution.", "ANALYST_TERM", "HISTORIOGRAPHICAL"),

    # MAGICAL / TECHNICAL
    ("sympatheia", "Sympatheia (Universal Sympathy)", "The principle of 'as above, so below.' The idea that all parts of the cosmos are interconnected and can influence one another through occult links.", "ACTOR_TERM", "COSMOLOGICAL"),
    ("theurgy", "Theurgy (God-Working)", "Ritual practices intended to facilitate union with the divine or to 'animate' statues, as described in the Asclepius.", "ACTOR_TERM", "RITUAL"),
    ("decans", "Decans", "The 36 Egyptian star-gods that govern the degrees of the zodiac, central to the technical/astrological Hermetica.", "ACTOR_TERM", "ASTROLOGICAL"),
    ("iatromathematica", "Iatromathematica", "The application of astrology (mathematica) to medicine (iatreia), a core branch of the technical Hermetica.", "ACTOR_TERM", "TECHNICAL"),
    ("prima_materia", "Prima Materia", "The 'First Matter.' The formless substance that is the starting point of the alchemical Great Work.", "ACTOR_TERM", "ALCHEMICAL")
]

def populate():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for slug, label, desc, ctype, cat in DICTIONARY_EXPANSION:
        cursor.execute("""
            INSERT OR IGNORE INTO concepts (slug, label, definition_short, category_type, category, source_method)
            VALUES (?, ?, ?, ?, ?, 'DEEP_POPULATION')
        """, (slug, label, desc, ctype, cat))

    conn.commit()
    conn.close()
    print("Dictionary massively expanded.")

if __name__ == "__main__":
    populate()
