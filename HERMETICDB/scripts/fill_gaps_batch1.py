import sqlite3
from pathlib import Path

DB_PATH = Path(r"c:\Dev\EmeraldTablet\db\emerald_tablet.db")

TEXT_SUMMARIES = {
    "ch_ii": "In this discourse, Hermes explains to Tat that everything that is moved is moved in something and by something. He identifies the 'place' in which the cosmos is moved as the incorporeal Mind of God.",
    "ch_iii": "A dense 'Sacred Discourse' describing the emergence of the seven governors (planets) and the creation of living beings from the elements under the direction of the Word (Logos).",
    "ch_v": "Hermes argues that God is non-manifest only to the ignorant. To the wise, God is manifest in every part of the cosmos, as the artisan is known through his work.",
    "ch_vi": "A philosophical investigation into the nature of 'The Good,' concluding that God and the Good are one and the same, and that nothing in the material world is truly good.",
    "ch_xi": "Mind (Nous) appears to Hermes to reveal that God is the author of all life and that the human soul can become 'all things' by expanding to encompass the entire cosmos.",
    "kyranides": "The Cyranides is a massive compendium of Hermetic natural magic, detailing the occult properties of plants, stones, and animals, based on the principle of universal sympathy.",
    "sh_fragments": "The Stobaean Fragments preserve essential pieces of lost Hermetic dialogues, including profound teachings on the nature of the soul, fate, and the afterlife.",
    "armenian_definitions": "This collection of 'Definitions' preserves a very early layer of Hermetic thought, often phrased as short, aphoristic answers to cosmological questions.",
    "iamblichus_mysteriis": "The definitive Neoplatonic defense of ritual magic (theurgy) against the rationalist critiques of Porphyry. Iamblichus argues that God is reached through ritual acts, not just philosophy.",
    "manetho_aegyptiaca": "The priest Manetho's history of Egypt, while primarily historical, was cited by later Hermeticists as the authority for the antiquity and authenticity of the Hermes tradition."
}

def fill():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 1. Delete the duplicate Modern Hermes
    cursor.execute("DELETE FROM persons WHERE person_id = 'hermes_trismegistos'")

    # 2. Fill Text Summaries
    for slug, summary in TEXT_SUMMARIES.items():
        cursor.execute("UPDATE texts SET analysis_html = ? WHERE text_id = ?", (f"<p>{summary}</p>", slug))

    # 3. Add connections for orphaned texts (Quick links to Hermes/Fowden)
    cursor.execute("SELECT id FROM persons WHERE person_id = 'hermes_trismegistus'")
    hermes_id = cursor.fetchone()[0]
    
    cursor.execute("SELECT id, text_id FROM texts WHERE text_id LIKE 'ch_%'")
    for tid, tslug in cursor.fetchall():
        cursor.execute("INSERT OR IGNORE INTO person_text_refs (person_id, text_id, rel_type) VALUES ('hermes_trismegistus', ?, 'AUTHOR')", (tslug,))

    conn.commit()
    conn.close()
    print("Logical gaps partially filled.")

if __name__ == "__main__":
    fill()
