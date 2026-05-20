"""
add_person_locations.py — Create person_locations table and populate
Idempotent: safe to re-run.
"""
import sqlite3

DB_PATH = r"C:\Dev\EmeraldTablet\db\emerald_tablet.db"

# Known person-location associations with scholarly basis
# Format: (person_id, location_slug, role, note)
# role: BORN, WORKED, DIED, FOUNDED, STUDIED, EXILED, ACTIVE
ASSOCIATIONS = [
    # ANTIQUITY — Egypt / Alexandrian tradition
    ("hermes_trismegistus",     "hermopolis",     "ACTIVE",  "Hermopolis Magna was the cult center of Thoth, identified with Hermes Trismegistus"),
    ("hermes_trismegistus",     "memphis",        "ACTIVE",  "Memphis was a major Egyptian priestly center associated with Ptah-Thoth syncretism"),
    ("zosimos_of_panopolis",    "akhmim",         "BORN",    "Zosimos was born and worked in Panopolis (Akhmim), modern Asyut governorate"),
    ("zosimos_of_panopolis",    "panopolis",      "ACTIVE",  "Panopolis (Akhmim) was Zosimos's primary base of alchemical and Hermetic activity"),
    ("zosimos_of_panopolis",    "alexandria",     "ACTIVE",  "Zosimos corresponded with Theosebeia in Alexandria and likely visited the city"),
    ("chaeremon",               "alexandria",     "ACTIVE",  "Chaeremon of Alexandria was a Stoic philosopher and Egyptian priest in Alexandria"),
    ("olympiodorus",            "alexandria",     "ACTIVE",  "Olympiodorus the Younger headed the Neoplatonic school in Alexandria c. 540-570 CE"),
    ("stephen_of_alexandria",   "alexandria",     "ACTIVE",  "Stephen of Alexandria taught at the philosophical school in Alexandria before 610 CE"),
    ("stephen_of_alexandria",   "constantinople", "ACTIVE",  "Stephen was summoned to Constantinople by Emperor Heraclius c. 610 CE"),
    ("plotinus",                "rome",           "ACTIVE",  "Plotinus taught philosophy in Rome from c. 244 CE until his death c. 270 CE"),
    ("iamblichus",              "antioch",        "ACTIVE",  "Iamblichus founded his Neoplatonic school in or near Apamea in Syria, close to Antioch"),
    ("proclus",                 "constantinople", "ACTIVE",  "Proclus is associated with Constantinople though his school was in Athens"),
    ("lactantius",              "rome",           "ACTIVE",  "Lactantius served at the imperial court in Rome and Nicomedia; key Latin transmitter of the Hermetica"),
    # MEDIEVAL — Islamic world
    ("jabir_ibn_hayyan",        "basra",          "ACTIVE",  "Jabir's works are associated with the Basran Ismaili tradition"),
    ("jabir_ibn_hayyan",        "baghdad",        "ACTIVE",  "Jabir worked under the Abbasid caliphate, centered on Baghdad"),
    ("al_kindi",                "baghdad",        "ACTIVE",  "Al-Kindi was the leading philosopher at the Abbasid court in Baghdad"),
    ("abu_mashar",              "baghdad",        "ACTIVE",  "Abu Ma'shar worked in Baghdad at the House of Wisdom under al-Mutawakkil"),
    ("al_razi",                 "baghdad",        "ACTIVE",  "Al-Razi (Rhazes) practiced medicine in Baghdad and served at the Abbasid court"),
    ("ibn_umayl",               "cairo",          "ACTIVE",  "Ibn Umayl (Senior Zadith) worked in Egypt; his Tabula Chemica uses Egyptian imagery"),
    ("khalid_ibn_yazid",        "cairo",          "ACTIVE",  "Khalid ibn Yazid (Calid) was an Umayyad prince based in Damascus and Egypt"),
    ("suhrawardi",              "antioch",        "DIED",    "Suhrawardi was executed in Aleppo (near Antioch) in 1191 CE under Saladin"),
    # MEDIEVAL — Latin West
    ("gerard_of_cremona",       "toledo",         "ACTIVE",  "Gerard of Cremona translated over 80 Arabic works to Latin in Toledo"),
    ("robert_of_chester",       "toledo",         "ACTIVE",  "Robert of Chester made the first Latin translation of an alchemical work in Toledo, 1144"),
    ("hugo_of_santalla",        "toledo",         "ACTIVE",  "Hugo of Santalla worked in Toledo and the Ebro valley translating Arabic astrological texts"),
    ("robert_grosseteste",      "oxford",         "ACTIVE",  "Grosseteste was Chancellor of Oxford University and first Bishop of Lincoln"),
    ("roger_bacon",             "oxford",         "ACTIVE",  "Roger Bacon spent much of his career at Oxford and the Franciscan house there"),
    ("roger_bacon",             "paris",          "STUDIED", "Roger Bacon studied at Paris before returning to Oxford"),
    ("thomas_of_york",          "oxford",         "ACTIVE",  "Thomas of York was a member of the Oxford Franciscan school"),
    ("thierry_of_chartres",     "paris",          "ACTIVE",  "Thierry taught in Paris and Chartres; Chartres was a dependency of the Paris cathedral school tradition"),
    ("william_of_conches",      "paris",          "ACTIVE",  "William of Conches taught at Chartres and Paris in the first half of the 12th century"),
    ("albertus_magnus",         "paris",          "STUDIED", "Albertus Magnus studied and taught theology at the University of Paris"),
    ("thomas_aquinas",          "paris",          "STUDIED", "Thomas Aquinas studied under Albertus Magnus and taught at the University of Paris"),
    ("thomas_aquinas",          "rome",           "ACTIVE",  "Thomas taught at various Dominican houses in Italy; died at Fossanova near Rome"),
    ("nicolas_flamel",          "paris",          "ACTIVE",  "Nicolas Flamel worked as a scribe and notary in Paris; his house survives on the rue de Montmorency"),
    ("ramon_llull",             "paris",          "ACTIVE",  "Ramon Lull lectured in Paris on multiple occasions and sought papal support there"),
    # RENAISSANCE
    ("marsilio_ficino",         "florence",       "ACTIVE",  "Ficino worked his entire career in Florence under Medici patronage at the Platonic Academy"),
    ("giovanni_pico_della_mirandola", "florence", "ACTIVE",  "Pico was closely associated with the Florentine Neoplatonic circle and died in Florence"),
    ("giovanni_pico_della_mirandola", "venice",   "ACTIVE",  "Pico's Conclusiones were printed in Rome but he had significant connections in the Veneto"),
    # EARLY MODERN
    ("athanasius_kircher",      "rome",           "ACTIVE",  "Kircher spent most of his career at the Collegio Romano in Rome"),
    ("isaac_newton",            "london",         "ACTIVE",  "Newton served as Master of the Royal Mint in London and was President of the Royal Society"),
    ("isaac_newton",            "oxford",         "ACTIVE",  "Newton studied mathematics at Cambridge but Oxford was the other key English center"),
    ("robert_boyle",            "london",         "ACTIVE",  "Boyle was a founder of the Royal Society in London and worked at his sister's house there"),
    ("robert_boyle",            "oxford",         "ACTIVE",  "Boyle conducted his pneumatic experiments in Oxford with Robert Hooke"),
    ("elias_ashmole",           "london",         "ACTIVE",  "Ashmole founded the Ashmolean Museum at Oxford but worked primarily in London"),
    ("thomas_vaughan",          "london",         "ACTIVE",  "Thomas Vaughan published his alchemical works in London"),
    ("isaac_casaubon",          "london",         "ACTIVE",  "Casaubon moved to London in 1610 where he completed his philological critique of the Hermetica"),
    ("jacob_boehme",            "strasbourg",     "ACTIVE",  "Böhme's works circulated in Strasbourg and through the Alsatian printing network"),
]


def main():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Create table if not exists
    cur.execute("""
        CREATE TABLE IF NOT EXISTS person_locations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            person_id TEXT NOT NULL,
            location_slug TEXT NOT NULL,
            role TEXT DEFAULT 'ACTIVE',
            note TEXT,
            UNIQUE(person_id, location_slug)
        )
    """)

    # Verify person_ids and location_slugs exist
    cur.execute("SELECT person_id FROM persons")
    valid_persons = {r[0] for r in cur.fetchall()}
    cur.execute("SELECT slug FROM locations")
    valid_locations = {r[0] for r in cur.fetchall()}

    inserted = 0
    skipped = 0
    for person_id, location_slug, role, note in ASSOCIATIONS:
        if person_id not in valid_persons:
            print(f"  SKIP (no person): {person_id}")
            skipped += 1
            continue
        if location_slug not in valid_locations:
            print(f"  SKIP (no location): {location_slug} for {person_id}")
            skipped += 1
            continue
        cur.execute(
            "INSERT OR IGNORE INTO person_locations (person_id, location_slug, role, note) VALUES (?, ?, ?, ?)",
            (person_id, location_slug, role, note)
        )
        if cur.rowcount:
            inserted += 1

    conn.commit()

    # Report totals
    cur.execute("SELECT count(*) FROM person_locations")
    total = cur.fetchone()[0]
    print(f"Inserted: {inserted}, Skipped: {skipped}")
    print(f"Total person_locations rows: {total}")

    # Show sample
    cur.execute("""
        SELECT pl.person_id, pl.location_slug, pl.role, p.name, l.label
        FROM person_locations pl
        JOIN persons p ON pl.person_id = p.person_id
        JOIN locations l ON pl.location_slug = l.slug
        ORDER BY l.label, p.name
        LIMIT 20
    """)
    print("\nSample associations:")
    for row in cur.fetchall():
        print(f"  {row[3]:35} → {row[4]:25} [{row[2]}]")

    conn.close()


if __name__ == "__main__":
    main()
