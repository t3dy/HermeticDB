import sqlite3
from pathlib import Path

DB_PATH = Path(r"c:\Dev\EmeraldTablet\db\emerald_tablet.db")

LINKS = [
    # Modern Scholarship
    ('garth_fowden', 'fowden_1990', 'AUTHOR'),
    ('jean_pierre_mahe', 'mahe_asclepius', 'AUTHOR'),
    ('brian_copenhaver', 'copenhaver_hermetica', 'AUTHOR'),
    ('wouter_hanegraaff', 'hanegraaff_dgwe', 'AUTHOR'),
    ('frances_yates', 'yates_bruno', 'AUTHOR'),
    ('paola_zambelli', 'zambelli_white_magic', 'AUTHOR'),
    ('liana_saif', 'saif_arabic_hermes', 'AUTHOR'),
    ('peter_forshaw', 'forshaw_khunrath', 'AUTHOR'),
    ('didier_kahn', 'alchemy', 'SCHOLAR'),
    ('hereward_tilton', 'michael_maier', 'SCHOLAR'),
    ('marco_pasi', 'dictionary_of_gnosis', 'SCHOLAR'),
    
    # Medieval & Renaissance Authors
    ('marsilio_ficino', 'ch_i', 'TRANSLATOR'),
    ('marsilio_ficino', 'asclepius', 'TRANSLATOR'),
    ('pico_della_mirandola', 'ch_i', 'SCHOLAR'),
    ('lodovico_lazzarelli', 'crater_hermetis', 'AUTHOR'),
    ('cornelius_agrippa', 'de_occulta_philosophia', 'AUTHOR'),
    ('john_dee', 'monas_hieroglyphica', 'AUTHOR'),
    ('giordano_bruno', 'ch_i', 'SCHOLAR'),
    ('michael_maier', 'atalanta_fugiens', 'AUTHOR'),
    ('heinrich_khunrath', 'amphitheatrum_sapientiae', 'AUTHOR'),
    ('robert_fludd', 'utriusque_cosmi_historia', 'AUTHOR'),
    ('isaac_newton', 'emerald_tablet', 'TRANSLATOR'),
    
    # Concept to Text links
    ('perfect_nature', 'picatrix', 'THEME'),
    ('planetary_mansions', 'picatrix', 'THEME'),
    ('suffumigation', 'picatrix', 'THEME'),
    ('infinite_sphere', 'liber_xxiv_philosophorum', 'THEME'),
    ('lumen_gloriae', 'liber_xxiv_philosophorum', 'THEME'),
    ('theurgical_statues', 'asclepius', 'THEME'),
    ('theurgical_statues', 'iamblichus_mysteriis', 'THEME'),
    ('ascent', 'ch_i', 'THEME'),
    ('palingenesia', 'ch_xiii', 'THEME'),
    ('correspondence', 'emerald_tablet', 'THEME'),
    ('alchemy', 'aurora_consurgens', 'THEME'),
    ('alchemy', 'rosarium_philosophorum', 'THEME')
]

def link():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for src, tgt, rel in LINKS:
        # Person-Text
        cursor.execute("SELECT 1 FROM persons WHERE person_id = ?", (src,))
        is_p = cursor.fetchone()
        cursor.execute("SELECT 1 FROM texts WHERE text_id = ?", (tgt,))
        is_t = cursor.fetchone()
        if is_p and is_t:
            cursor.execute("INSERT OR IGNORE INTO person_text_refs (person_id, text_id, rel_type) VALUES (?, ?, ?)", (src, tgt, rel))
        
        # Concept-Text
        cursor.execute("SELECT 1 FROM concepts WHERE slug = ?", (src,))
        is_c = cursor.fetchone()
        if is_c and is_t:
            # Get integer IDs
            cid = cursor.execute("SELECT id FROM concepts WHERE slug = ?", (src,)).fetchone()[0]
            tid = cursor.execute("SELECT id FROM texts WHERE text_id = ?", (tgt,)).fetchone()[0]
            cursor.execute("INSERT OR IGNORE INTO concept_text_refs (concept_id, text_id) VALUES (?, ?)", (cid, tid))

    conn.commit()
    conn.close()
    print("Scholarship linking complete.")

if __name__ == "__main__":
    link()
