import sqlite3
from pathlib import Path

DB_PATH = Path(r"c:\Dev\EmeraldTablet\db\emerald_tablet.db")

PERSON_ERAS = [
    ('ANTIQUITY', ['hermes_trismegistus', 'zosimos_of_panopolis', 'iamblichus', 'porphyry', 'plotinus', 'proclus', 'balinas', 'stephen_of_alexandria', 'julian_the_apostate', 'stobaeus', 'cyril_alexandria', 'clement_alexandria', 'chaeremon', 'olympiodorus']),
    ('MEDIEVAL', ['jabir_ibn_hayyan', 'al_razi', 'ibn_umayl', 'khalid_ibn_yazid', 'albertus_magnus', 'thomas_aquinas', 'roger_bacon', 'petrus_bonus', 'nicolas_flamel', 'bernard_of_trevisan', 'suhrawardi', 'abu_mashar', 'al_kindi', 'hugo_of_santalla', 'robert_of_chester', 'gerard_of_cremona', 'ramon_llull']),
    ('RENAISSANCE', ['marsilio_ficino', 'giovanni_pico', 'lodovico_lazzarelli', 'cornelius_agrippa', 'paracelsus', 'john_dee', 'giordano_bruno', 'robert_fludd', 'michael_maier', 'basil_valentine', 'heinrich_khunrath', 'andreas_libavius', 'johannes_reuchlin', 'johannes_trithemius', 'tommaso_campanella', 'guillaume_postel', 'francesco_patrizi', 'johann_valentin_andreae', 'nicholas_of_cusa', 'pietro_pomponazzi', 'symphorien_champier']),
    ('EARLY_MODERN', ['kenelm_digby', 'elias_ashmole', 'athanasius_kircher', 'isaac_newton', 'robert_boyle', 'thomas_vaughan', 'francis_mercury_van_helmont', 'jacob_boehme', 'christoph_kriegsmann', 'isaac_casaubon']),
    ('MODERN', ['brian_copenhaver', 'wouter_hanegraaff', 'garth_fowden', 'florian_ebeling', 'peter_forshaw', 'didier_kahn', 'hereward_tilton', 'marco_pasi', 'christian_bull', 'david_litwa', 'frances_yates', 'carl_jung', 'antoine_faivre', 'dp_walker', 'carlos_gilly', 'kocku_von_stuckrad', 'arthur_versluis', 'nicholas_goodrick_clarke', 'moshe_idel', 'liana_saif', 'paola_zambelli', 'jean_pierre_mahe', 'bruce_codex', 'mark_damien_delp', 'david_porreca'])
]

TEXT_DATES = [
    ('corpus_hermeticum', 100),
    ('asclepius', 100),
    ('ch_i', 100),
    ('ch_iv', 100),
    ('ch_x', 100),
    ('ch_xiii', 100),
    ('picatrix', 950),
    ('emerald_tablet', 800),
    ('sirr_al_khaliqa', 800),
    ('kitab_sirr_al_khaliqa', 800),
    ('aurora_consurgens', 1420),
    ('rosarium_philosophorum', 1550),
    ('monas_hieroglyphica', 1564),
    ('de_occulta_philosophia', 1531),
    ('atalanta_fugiens', 1617),
    ('splendor_solis', 1532),
    ('amphitheatrum_sapientiae', 1595),
    ('theatrum_chemicum_britannicum', 1652),
    ('crater_hermetis', 1494),
    ('city_of_the_sun', 1602),
    ('kyranides', 300),
    ('liber_hermetis', 400),
    ('sh_fragments', 450),
    ('nag_hammadi_hermetica', 300),
    ('liber_xxiv_philosophorum', 1200),
    ('de_sex_rerum_principiis', 1150)
]

def refine():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    print("Refining person eras...")
    for era, slugs in PERSON_ERAS:
        for slug in slugs:
            cursor.execute("UPDATE persons SET era = ? WHERE person_id = ?", (era, slug))

    print("Refining text dates...")
    for slug, year in TEXT_DATES:
        cursor.execute("UPDATE texts SET date_composed_start = ? WHERE text_id = ?", (year, slug))

    conn.commit()
    conn.close()
    print("Historical metadata refinement complete.")

if __name__ == "__main__":
    refine()
