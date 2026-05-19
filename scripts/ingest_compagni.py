"""
Ingest Vittoria Perrone Compagni as a scholar and her key works as texts.
Links her to concepts: magia_naturalis, virtus_loci, astral_magic, cornelius_agrippa.
Idempotent — safe to re-run.
"""
import sqlite3

DB_PATH = r"C:\Dev\EmeraldTablet\db\emerald_tablet.db"

conn = sqlite3.connect(DB_PATH)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

# ─── PERSON ───────────────────────────────────────────────────────────────────

cur.execute("""
    INSERT OR IGNORE INTO persons (
        person_id, name, name_alt, birth_year, death_year,
        role_primary, era, description, bio_html,
        source_method, review_status, confidence, scholar_group
    ) VALUES (
        'vittoria_perrone_compagni',
        'Vittoria Perrone Compagni',
        'Perrone Compagni',
        1946, NULL,
        'SCHOLAR',
        'MODERN',
        'Italian historian of Renaissance philosophy and editor of the critical edition of Cornelius Agrippa''s De occulta philosophia (Brill, 1992). A leading expert on Renaissance natural magic, Pomponazzi''s naturalistic philosophy, and the Picatrix tradition.',
        '',
        'SEED_DATA', 'DRAFT', 'HIGH',
        'Renaissance and Early Modern Studies'
    )
""")
print("Person:", "inserted" if cur.rowcount else "already exists")

# ─── TEXTS ────────────────────────────────────────────────────────────────────

texts = [
    {
        "text_id": "agrippa_de_occulta_compagni_ed",
        "title": "De occulta philosophia libri tres (Compagni critical edition)",
        "title_original": "De occulta philosophia libri tres",
        "language": "Latin",
        "text_type": "SCHOLARSHIP",
        "date_composed_start": 1992,
        "date_composed_end": 1992,
        "description": (
            "The authoritative critical edition of Agrippa's De occulta philosophia libri tres, "
            "edited with apparatus criticus and scholarly introduction by Vittoria Perrone Compagni. "
            "Published by Brill (Leiden, 1992) in the series Studien und Texte zur Geistesgeschichte "
            "des Mittelalters. This edition established the definitive Latin text based on collation "
            "of manuscript and early printed witnesses, supplanting all prior editions for scholarly "
            "purposes. Compagni's introduction provides a rigorous analysis of the work's sources, "
            "composition history, and place in Renaissance philosophical and magical thought."
        ),
        "analysis_html": "",
        "source_method": "SEED_DATA",
    },
    {
        "text_id": "compagni_circe_virtus_loci_2007",
        "title": "Circe, la «virtus loci», il determinismo nel De incantationibus di Pomponazzi",
        "title_original": "Circe, la «virtus loci», il determinismo nel De incantationibus di Pomponazzi",
        "language": None,  # Italian — not in schema enum
        "text_type": "SCHOLARSHIP",
        "date_composed_start": 2007,
        "date_composed_end": 2007,
        "description": (
            "A scholarly article examining Pietro Pomponazzi's De incantationibus (written c.1520, "
            "published posthumously 1556) through the philosophical problem of the virtus loci — "
            "the inherent power of place — and its relationship to astrological determinism and the "
            "myth of Circe. Compagni analyzes how Pomponazzi mobilizes the concept of local virtue "
            "to provide a naturalistic, Aristotelian explanation for apparent magical effects, "
            "rejecting supernatural causation while accounting for the evident efficacy of certain "
            "locations, substances, and practices within a framework of celestial causality."
        ),
        "analysis_html": "",
        "source_method": "SEED_DATA",
    },
    {
        "text_id": "compagni_picatrix_review_1988",
        "title": "Review: Picatrix — The Latin Version of the Ghāyat al-Ḥakīm (Pingree ed.)",
        "title_original": "Picatrix. The latin version of the Gāyat Al-akīm [review]",
        "language": None,  # Italian — not in schema enum
        "text_type": "SCHOLARSHIP",
        "date_composed_start": 1988,
        "date_composed_end": 1988,
        "description": (
            "A scholarly review, published in Nuncius: Annali di Storia della Scienza, of David Pingree's "
            "critical edition of the Latin Picatrix (The Warburg Institute, 1986), the definitive edition "
            "of the Latin translation of the Arabic Ghāyat al-Ḥakīm. Compagni's review evaluates Pingree's "
            "editorial methodology, his reconstruction of the Latin text from manuscript witnesses, and "
            "the editorial apparatus. The review reflects Compagni's expertise in the Latin magical "
            "tradition and its relationship to Arabic sources."
        ),
        "analysis_html": "",
        "source_method": "SEED_DATA",
    },
]

for t in texts:
    cur.execute("""
        INSERT OR IGNORE INTO texts (
            text_id, title, title_original, language, text_type,
            date_composed_start, date_composed_end,
            description, analysis_html, source_method, review_status, confidence
        ) VALUES (
            :text_id, :title, :title_original, :language, :text_type,
            :date_composed_start, :date_composed_end,
            :description, :analysis_html, :source_method, 'DRAFT', 'HIGH'
        )
    """, t)
    print(f"Text '{t['text_id']}': {'inserted' if cur.rowcount else 'already exists'}")

# ─── PERSON → TEXT REFS ───────────────────────────────────────────────────────

person_text_links = [
    ("vittoria_perrone_compagni", "agrippa_de_occulta_compagni_ed",    "EDITOR"),
    ("vittoria_perrone_compagni", "compagni_circe_virtus_loci_2007",   "AUTHOR"),
    ("vittoria_perrone_compagni", "compagni_picatrix_review_1988",     "AUTHOR"),
    # Link Agrippa as subject-author of the critical edition
    ("cornelius_agrippa",         "agrippa_de_occulta_compagni_ed",   "AUTHOR"),
]

for pid, tid, role in person_text_links:
    cur.execute("SELECT id FROM persons WHERE person_id=?", (pid,))
    p = cur.fetchone()
    if not p:
        print(f"  WARN: person '{pid}' not found — skipping link")
        continue
    cur.execute("SELECT id FROM texts WHERE text_id=?", (tid,))
    t = cur.fetchone()
    if not t:
        print(f"  WARN: text '{tid}' not found — skipping link")
        continue
    cur.execute(
        "INSERT OR IGNORE INTO person_text_refs (person_id, text_id, rel_type) VALUES (?,?,?)",
        (pid, tid, role)
    )
    status = "linked" if cur.rowcount else "already linked"
    print(f"  {pid} → {tid} ({role}): {status}")

# ─── CONCEPT → TEXT REFS ──────────────────────────────────────────────────────

concept_text_links = [
    # De occulta philosophia covers all these
    ("magia_naturalis",    "agrippa_de_occulta_compagni_ed"),
    ("astral_magic",       "agrippa_de_occulta_compagni_ed"),
    ("sympatheia",         "agrippa_de_occulta_compagni_ed"),
    ("planetary_spirits",  "agrippa_de_occulta_compagni_ed"),
    ("suffumigation",      "agrippa_de_occulta_compagni_ed"),
    ("talismans",          "agrippa_de_occulta_compagni_ed"),
    ("macrocosm_microcosm","agrippa_de_occulta_compagni_ed"),
    ("correspondence",     "agrippa_de_occulta_compagni_ed"),
    # Circe article — virtus loci + determinism in Pomponazzi
    ("virtus_loci",        "compagni_circe_virtus_loci_2007"),
    ("magia_naturalis",    "compagni_circe_virtus_loci_2007"),
    ("astral_magic",       "compagni_circe_virtus_loci_2007"),
    # Picatrix review
    ("astral_magic",       "compagni_picatrix_review_1988"),
    ("talismans",          "compagni_picatrix_review_1988"),
    ("planetary_mansions", "compagni_picatrix_review_1988"),
    ("suffumigation",      "compagni_picatrix_review_1988"),
]

for cslug, tid in concept_text_links:
    cur.execute("SELECT id FROM concepts WHERE slug=?", (cslug,))
    c = cur.fetchone()
    cur.execute("SELECT id FROM texts WHERE text_id=?", (tid,))
    t = cur.fetchone()
    if not c:
        print(f"  WARN: concept '{cslug}' not found")
        continue
    if not t:
        print(f"  WARN: text '{tid}' not found")
        continue
    cur.execute(
        "INSERT OR IGNORE INTO concept_text_refs (concept_id, text_id) VALUES (?,?)",
        (c["id"], t["id"])
    )
    # concept_text_refs uses INTEGER ids, not text slugs
    print(f"  concept {cslug} → {tid}: {'linked' if cur.rowcount else 'already linked'}")

conn.commit()
conn.close()
print("\nDone. Run DEPLOY_PORTAL.py to rebuild the site.")
