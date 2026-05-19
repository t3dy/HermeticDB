"""Final clean run: insert remaining Compagni texts and all links."""
import sqlite3

DB = r"C:\Dev\EmeraldTablet\db\emerald_tablet.db"
conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

# ── update existing De occulta text to full title ──────────────────────────────
cur.execute("""UPDATE texts SET
    title='De occulta philosophia libri tres (Compagni critical edition)',
    title_original='De occulta philosophia libri tres',
    description=?
WHERE text_id='agrippa_de_occulta_compagni_ed'""", (
    "The authoritative critical edition of Agrippa's De occulta philosophia libri tres, "
    "edited with apparatus criticus and scholarly introduction by Vittoria Perrone Compagni. "
    "Published by Brill (Leiden, 1992) in the series Studien und Texte zur Geistesgeschichte "
    "des Mittelalters. This edition established the definitive Latin text based on collation "
    "of manuscript and early printed witnesses, supplanting all prior editions for scholarly "
    "purposes. Compagni's introduction provides a rigorous analysis of the work's sources, "
    "composition history, and place in Renaissance philosophical and magical thought.",
))
print("De occulta updated:", cur.rowcount, "row(s)")

# ── insert two Compagni articles ───────────────────────────────────────────────
articles = [
    ("compagni_circe_virtus_loci_2007",
     "Circe, la virtus loci, il determinismo nel De incantationibus di Pomponazzi",
     "Circe, la virtus loci, il determinismo nel De incantationibus di Pomponazzi",
     None, "SCHOLARSHIP", 2007, 2007,
     ("A scholarly article examining Pietro Pomponazzi's De incantationibus (written c.1520, "
      "published posthumously 1556) through the philosophical problem of the virtus loci -- "
      "the inherent power of place -- and its relationship to astrological determinism and the "
      "myth of Circe. Compagni analyzes how Pomponazzi mobilizes the concept of local virtue "
      "to provide a naturalistic, Aristotelian explanation for apparent magical effects, "
      "rejecting supernatural causation while accounting for the evident efficacy of certain "
      "locations, substances, and practices within a framework of celestial causality.")),
    ("compagni_picatrix_review_1988",
     "Review: Picatrix -- The Latin Version of the Ghayat al-Hakim (Pingree ed.)",
     "Picatrix. The latin version of the Gayat Al-akim [review, Nuncius 1988]",
     None, "SCHOLARSHIP", 1988, 1988,
     ("A scholarly review, published in Nuncius: Annali di Storia della Scienza, of David Pingree's "
      "critical edition of the Latin Picatrix (The Warburg Institute, 1986). Compagni's review "
      "evaluates Pingree's editorial methodology, his reconstruction of the Latin text from "
      "manuscript witnesses, and the editorial apparatus. The review reflects Compagni's expertise "
      "in the Latin magical tradition and its relationship to Arabic sources.")),
]

for tid, title, title_orig, lang, ttype, ds, de, desc in articles:
    cur.execute("""INSERT OR IGNORE INTO texts
        (text_id, title, title_original, language, text_type,
         date_composed_start, date_composed_end, description, analysis_html,
         source_method, review_status, confidence)
        VALUES (?,?,?,?,?,?,?,?,'','SEED_DATA','DRAFT','HIGH')""",
        (tid, title, title_orig, lang, ttype, ds, de, desc))
    print(f"{tid}: {'inserted' if cur.rowcount else 'already exists'}")

conn.commit()

# ── verify ─────────────────────────────────────────────────────────────────────
text_ids = ["agrippa_de_occulta_compagni_ed", "compagni_circe_virtus_loci_2007",
            "compagni_picatrix_review_1988"]
text_map = {}
for tid in text_ids:
    cur.execute("SELECT id FROM texts WHERE text_id=?", (tid,))
    r = cur.fetchone()
    if r:
        text_map[tid] = r["id"]
        print(f"  text {tid} -> id {r['id']}")
    else:
        print(f"  MISSING: {tid}")

# ── person -> text refs ────────────────────────────────────────────────────────
ptr = [
    ("vittoria_perrone_compagni", "agrippa_de_occulta_compagni_ed",  "EDITOR"),
    ("vittoria_perrone_compagni", "compagni_circe_virtus_loci_2007", "AUTHOR"),
    ("vittoria_perrone_compagni", "compagni_picatrix_review_1988",   "AUTHOR"),
    ("cornelius_agrippa",         "agrippa_de_occulta_compagni_ed",  "AUTHOR"),
]
for pid, tid, role in ptr:
    if tid not in text_map:
        print(f"  skip {pid}->{tid}: text not found")
        continue
    cur.execute("INSERT OR IGNORE INTO person_text_refs (person_id, text_id, rel_type) VALUES (?,?,?)",
                (pid, tid, role))
    print(f"  person_text {pid}->{tid} ({role}): {'ok' if cur.rowcount else 'dup'}")

# ── concept -> text refs ───────────────────────────────────────────────────────
ctlinks = [
    ("magia_naturalis",     "agrippa_de_occulta_compagni_ed"),
    ("astral_magic",        "agrippa_de_occulta_compagni_ed"),
    ("sympatheia",          "agrippa_de_occulta_compagni_ed"),
    ("planetary_spirits",   "agrippa_de_occulta_compagni_ed"),
    ("suffumigation",       "agrippa_de_occulta_compagni_ed"),
    ("talismans",           "agrippa_de_occulta_compagni_ed"),
    ("macrocosm_microcosm", "agrippa_de_occulta_compagni_ed"),
    ("correspondence",      "agrippa_de_occulta_compagni_ed"),
    ("virtus_loci",         "compagni_circe_virtus_loci_2007"),
    ("magia_naturalis",     "compagni_circe_virtus_loci_2007"),
    ("astral_magic",        "compagni_circe_virtus_loci_2007"),
    ("astral_magic",        "compagni_picatrix_review_1988"),
    ("talismans",           "compagni_picatrix_review_1988"),
    ("planetary_mansions",  "compagni_picatrix_review_1988"),
    ("suffumigation",       "compagni_picatrix_review_1988"),
]
for cslug, tid in ctlinks:
    if tid not in text_map:
        print(f"  skip {cslug}->{tid}: text not found")
        continue
    cur.execute("SELECT id FROM concepts WHERE slug=?", (cslug,))
    c = cur.fetchone()
    if not c:
        print(f"  skip concept {cslug}: not found")
        continue
    cur.execute("INSERT OR IGNORE INTO concept_text_refs (concept_id, text_id) VALUES (?,?)",
                (c["id"], text_map[tid]))
    print(f"  concept {cslug}->{tid}: {'ok' if cur.rowcount else 'dup'}")

conn.commit()
conn.close()
print("Done.")
