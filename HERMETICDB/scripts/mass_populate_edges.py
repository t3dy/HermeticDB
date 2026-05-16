import sqlite3
from pathlib import Path

DB_PATH = Path(r"c:\Dev\EmeraldTablet\db\emerald_tablet.db")

MASS_EDGES = [
    # ANTIQUITY LINKS
    ("ammon", "ch_xvi", "AUTHOR"),
    ("asclepius_sage", "asclepius", "AUTHOR"),
    ("isis", "kore_kosmou", "AUTHOR"),
    ("chaeremon", "manetho", "CONTEMPORARY"),
    ("zosimos_of_panopolis", "theosebeia", "TEACHER_OF"),
    ("bolus_of_mendes", "maria_the_jewess", "INFLUENCED"),
    ("iamblichus", "theurgy", "THEORIZED"),
    
    # MEDIEVAL LINKS
    ("abu_mashar", "jabir_ibn_hayyan", "INFLUENCED"),
    ("maslama_al_majriti", "picatrix", "AUTHOR"),
    ("hugo_of_santalla", "sirr_al_khaliqa", "TRANSLATOR"),
    ("albertus_magnus", "secretum_secretorum", "SCHOLAR"),
    ("roger_bacon", "secretum_secretorum", "SCHOLAR"),
    
    # RENAISSANCE LINKS
    ("paracelsus", "sympatheia", "PRACTITIONER"),
    ("paracelsus", "prima_materia", "PRACTITIONER"),
    ("john_dee", "monas_hieroglyphica", "AUTHOR"),
    ("michael_maier", "atalanta_fugiens", "AUTHOR"),
    ("giordano_bruno", "monas_hieroglyphica", "INFLUENCED_BY"),
    ("heinrich_khunrath", "yates_bruno", "SUBJECT"),
    
    # CONCEPT LINKS
    ("alchemy", "emerald_tablet", "THEME"),
    ("alchemy", "seven_chapters", "THEME"),
    ("alchemy", "golden_tractate", "THEME"),
    ("astrology", "liber_beibeniis", "THEME"),
    ("astrology", "liber_25_chapters", "THEME"),
    ("theurgy", "ch_xiii", "THEME"),
    ("theurgy", "iamblichus_mysteriis", "THEME"),
    ("pneuma", "asclepius", "THEME"),
    ("nous", "ch_i", "THEME"),
    ("nous", "ch_xi", "THEME")
]

def populate():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for src, tgt, rel in MASS_EDGES:
        # Check if source is a person or text or concept
        # We'll use a helper to find which table to link
        cursor.execute("SELECT 1 FROM persons WHERE person_id = ?", (src,))
        is_person_src = cursor.fetchone()
        cursor.execute("SELECT 1 FROM texts WHERE text_id = ?", (tgt,))
        is_text_tgt = cursor.fetchone()

        if is_person_src and is_text_tgt:
            cursor.execute("INSERT OR IGNORE INTO person_text_refs (person_id, text_id, rel_type) VALUES (?, ?, ?)", (src, tgt, rel))
        
        # Check for person-person
        cursor.execute("SELECT 1 FROM persons WHERE person_id = ?", (tgt,))
        is_person_tgt = cursor.fetchone()
        if is_person_src and is_person_tgt:
            cursor.execute("INSERT OR IGNORE INTO person_person_refs (person_a, person_b, rel_type) VALUES (?, ?, ?)", (src, tgt, rel))

        # Check for text-text
        cursor.execute("SELECT 1 FROM texts WHERE text_id = ?", (src,))
        is_text_src = cursor.fetchone()
        if is_text_src and is_text_tgt:
            cursor.execute("INSERT OR IGNORE INTO text_text_refs (text_a, text_b, rel_type) VALUES (?, ?, ?)", (src, tgt, rel))

        # Check for concept-text
        cursor.execute("SELECT 1 FROM concepts WHERE slug = ?", (src,))
        is_concept_src = cursor.fetchone()
        if is_concept_src and is_text_tgt:
            # Need integer IDs for concept_text_refs
            cid = cursor.execute("SELECT id FROM concepts WHERE slug = ?", (src,)).fetchone()[0]
            tid = cursor.execute("SELECT id FROM texts WHERE text_id = ?", (tgt,)).fetchone()[0]
            cursor.execute("INSERT OR IGNORE INTO concept_text_refs (concept_id, text_id) VALUES (?, ?)", (cid, tid))

    conn.commit()
    conn.close()
    print("Mass edge population complete.")

if __name__ == "__main__":
    populate()
