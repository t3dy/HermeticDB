import sqlite3
from pathlib import Path

DB_PATH = Path(r"c:\Dev\EmeraldTablet\db\emerald_tablet.db")

def consolidate_and_expand():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    print("Cleaning up persons...")
    # Deduplicate persons
    # Nicholas Goodrick-Clarke
    cursor.execute("SELECT id FROM persons WHERE person_id = 'nicholas_goodrick-clarke'")
    bad_p = cursor.fetchone()
    if bad_p:
        cursor.execute("SELECT id FROM persons WHERE person_id = 'nicholas_goodrick_clarke'")
        good_p = cursor.fetchone()
        if good_p:
            # Update references if any (none in this table but maybe in refs)
            cursor.execute("UPDATE person_text_refs SET person_id = 'nicholas_goodrick_clarke' WHERE person_id = 'nicholas_goodrick-clarke'")
            cursor.execute("DELETE FROM persons WHERE person_id = 'nicholas_goodrick-clarke'")

    # Heinrich Cornelius Agrippa
    cursor.execute("SELECT id FROM persons WHERE person_id = 'heinrich_cornelius_agrippa'")
    bad_p = cursor.fetchone()
    if bad_p:
        cursor.execute("SELECT id FROM persons WHERE person_id = 'cornelius_agrippa'")
        good_p = cursor.fetchone()
        if good_p:
            cursor.execute("UPDATE person_text_refs SET person_id = 'cornelius_agrippa' WHERE person_id = 'heinrich_cornelius_agrippa'")
            cursor.execute("DELETE FROM persons WHERE person_id = 'heinrich_cornelius_agrippa'")

    # Move misclassified concepts
    for slug in ['ochema', 'phantasmata', 'virtus_loci']:
        cursor.execute("SELECT * FROM persons WHERE person_id = ?", (slug,))
        row = cursor.fetchone()
        if row:
            cursor.execute("""
                INSERT OR IGNORE INTO concepts (slug, label, definition_short, category, source_method)
                VALUES (?, ?, ?, 'PHILOSOPHICAL', 'CLEANUP')
            """, (row['person_id'], row['name'], row['description']))
            cursor.execute("DELETE FROM persons WHERE person_id = ?", (slug,))

    # Move misclassified text
    cursor.execute("SELECT * FROM persons WHERE person_id = 'atalanta_fugiens'")
    row = cursor.fetchone()
    if row:
        cursor.execute("""
            INSERT OR IGNORE INTO texts (text_id, title, description, text_type, source_method)
            VALUES (?, ?, ?, 'TREATISE', 'CLEANUP')
        """, (row['person_id'], row['name'], row['description']))
        cursor.execute("DELETE FROM persons WHERE person_id = 'atalanta_fugiens'")

    print("Cleaning up texts...")
    # Deduplicate texts
    text_consolidations = [
        ('yates_bruno_hermetic', 'yates_bruno'),
        ('giordano_bruno_yates', 'yates_bruno'),
        ('ch_i_poimandres', 'ch_i'),
        ('ch_iv_krater', 'ch_iv'),
        ('ch_xiii_secret_discourse', 'ch_xiii'),
        ('ch_xiii_on_rebirth_and_silence', 'ch_xiii'),
        ('theatrum_chem_britannicum', 'theatrum_chemicum_britannicum'),
        ('liber_24_philosophorum', 'liber_xxiv_philosophorum'),
        ('de_occulta_philosophia_libri_tres', 'de_occulta_philosophia'),
        ('ch_ii_to_asclepius', 'ch_ii')
    ]
    for bad, good in text_consolidations:
        cursor.execute("SELECT id FROM texts WHERE text_id = ?", (bad,))
        bad_t = cursor.fetchone()
        if bad_t:
            cursor.execute("SELECT id FROM texts WHERE text_id = ?", (good,))
            good_t = cursor.fetchone()
            if good_t:
                # Update references
            cursor.execute("UPDATE person_text_refs SET text_id = ? WHERE text_id = ?", (good, bad))
            cursor.execute("UPDATE concept_text_refs SET text_id = ? WHERE text_id = ?", (good_t['id'], bad_t['id']))
                cursor.execute("DELETE FROM texts WHERE text_id = ?", (bad,))

    print("Expanding dictionary...")
    NEW_CONCEPTS = [
        ('perfect_nature', 'Perfect Nature (Al-Tabi\'a al-Tamma)', 'The celestial twin or higher self of the practitioner in the Picatrix tradition.', 'THEOLOGICAL', 'ACTOR_TERM'),
        ('planetary_mansions', 'Planetary Mansions', 'The 28 lunar mansions and planetary hours used for talismanic construction in the Picatrix.', 'COSMOLOGICAL', 'ACTOR_TERM'),
        ('suffumigation', 'Suffumigation', 'The ritual use of incense to attract planetary spirits and establish sympathetic links.', 'SCIENTIFIC', 'ACTOR_TERM'),
        ('lumen_gloriae', 'Lumen Gloriae (Light of Glory)', 'The divine illumination through which God is known, as described in the Liber XXIV philosophorum.', 'THEOLOGICAL', 'ACTOR_TERM'),
        ('infinite_sphere', 'Infinite Sphere', 'The definition of God as an infinite sphere whose center is everywhere and circumference is nowhere.', 'COSMOLOGICAL', 'ACTOR_TERM'),
        ('immanent_logos', 'Immanent Logos', 'The divine principle of reason as an internal structure within the human mind.', 'PHILOSOPHICAL', 'HYBRID'),
        ('theurgical_statues', 'Theurgical Statues', 'The ritual animation of idols by drawing down celestial spirits, as described in the Asclepius.', 'THEOLOGICAL', 'ACTOR_TERM')
    ]
    for slug, label, desc, cat, ctype in NEW_CONCEPTS:
        cursor.execute("""
            INSERT OR IGNORE INTO concepts (slug, label, definition_short, category, category_type, source_method)
            VALUES (?, ?, ?, ?, ?, 'SEED_DATA')
        """, (slug, label, desc, cat, ctype))

    print("Strengthening relationships...")
    # Add key relationships
    relationships = [
        ('marsilio_ficino', 'corpus_hermeticum', 'TRANSLATOR'),
        ('cornelius_agrippa', 'de_occulta_philosophia', 'AUTHOR'),
        ('john_dee', 'monas_hieroglyphica', 'AUTHOR'),
        ('isaac_newton', 'emerald_tablet', 'TRANSLATOR'),
        ('garth_fowden', 'fowden_1990', 'AUTHOR'),
        ('wouter_hanegraaff', 'hanegraaff_dgwe', 'AUTHOR'),
        ('frances_yates', 'yates_bruno', 'AUTHOR'),
        ('lodovico_lazzarelli', 'crater_hermetis', 'AUTHOR'),
        ('tommaso_campanella', 'city_of_the_sun', 'AUTHOR'),
        ('michael_maier', 'atalanta_fugiens', 'AUTHOR')
    ]
    for p_slug, t_slug, rel in relationships:
        cursor.execute("SELECT id FROM persons WHERE person_id = ?", (p_slug,))
        p = cursor.fetchone()
        cursor.execute("SELECT id FROM texts WHERE text_id = ?", (t_slug,))
        t = cursor.fetchone()
        if p and t:
            cursor.execute("""
                INSERT OR IGNORE INTO person_text_refs (person_id, text_id, rel_type)
                VALUES (?, ?, ?)
            """, (p_slug, t_slug, rel))

    conn.commit()
    conn.close()
    print("Consolidation and expansion complete.")

if __name__ == "__main__":
    consolidate_and_expand()
