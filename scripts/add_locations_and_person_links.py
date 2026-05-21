"""
Add new geographic locations and person-location associations for key Hermetic figures.
Idempotent: safe to re-run.
"""
import sqlite3
from pathlib import Path

DB = Path(r"c:\Dev\EmeraldTablet\db\emerald_tablet.db")
conn = sqlite3.connect(DB)
c = conn.cursor()

# ── 1. NEW LOCATIONS ──────────────────────────────────────────────────────────

new_locations = [
    {
        "slug": "cologne",
        "label": "Cologne, Germany",
        "lat": 50.938,
        "lng": 6.960,
        "description": (
            "Cologne was the birthplace and publishing centre of Heinrich Cornelius Agrippa, "
            "the most ambitious synthesiser of Renaissance Hermetic and occult philosophy. "
            "Albertus Magnus, whose encyclopedic natural philosophy shaped the scholastic "
            "reception of Arabic Hermetica, led the Dominican studium here. "
            "The final edition of Agrippa's De Occulta Philosophia (1531) was printed in Cologne."
        ),
        "region": "EUROPE",
        "era_primary": "RENAISSANCE",
        "source_method": "MANUAL",
        "confidence": "HIGH",
        "review_status": "REVIEWED",
    },
    {
        "slug": "wurzburg",
        "label": "Würzburg, Germany",
        "lat": 49.800,
        "lng": 9.936,
        "description": (
            "Würzburg was the base of Johannes Trithemius as Abbot of St James (1506–16), "
            "the foremost late-medieval encyclopedist of Hermetic and magical lore. "
            "Agrippa visited Trithemius here in 1510 and completed the first draft of "
            "De Occulta Philosophia, which he dedicated to the abbot — making Würzburg "
            "the site of one of the most consequential collaborations in Hermetic history."
        ),
        "region": "EUROPE",
        "era_primary": "RENAISSANCE",
        "source_method": "MANUAL",
        "confidence": "HIGH",
        "review_status": "REVIEWED",
    },
]

c.execute("PRAGMA table_info(locations)")
cols = {row[1] for row in c.fetchall()}

for loc in new_locations:
    row = {k: v for k, v in loc.items() if k in cols}
    placeholders = ", ".join(["?"] * len(row))
    col_names = ", ".join(row.keys())
    c.execute(
        f"INSERT OR IGNORE INTO locations ({col_names}) VALUES ({placeholders})",
        list(row.values()),
    )
    print(f"  location: {loc['slug']} -- {c.rowcount} row(s) inserted")

conn.commit()

# ── 2. PERSON-LOCATION ASSOCIATIONS ──────────────────────────────────────────

# (person_id, location_slug, role, source_method, confidence)
associations = [
    # Pico della Mirandola — central figure of Florentine Neoplatonism
    ("giovanni_pico",       "florence",        "ACTIVE",  "MANUAL", "HIGH"),

    # Agrippa — born Cologne, key Würzburg visit with Trithemius
    ("cornelius_agrippa",   "cologne",         "BORN",    "MANUAL", "HIGH"),
    ("cornelius_agrippa",   "wurzburg",        "VISITED", "MANUAL", "HIGH"),

    # Trithemius — Abbot of St James, Würzburg
    ("johannes_trithemius", "wurzburg",        "ACTIVE",  "MANUAL", "HIGH"),

    # Giordano Bruno — Venice (arrested 1592), Rome (executed 1600)
    ("giordano_bruno",      "venice",          "ACTIVE",  "MANUAL", "HIGH"),
    ("giordano_bruno",      "rome",            "DIED",    "MANUAL", "HIGH"),

    # Paracelsus — city physician of Basel; Strasbourg stay
    ("paracelsus",          "strasbourg",      "ACTIVE",  "MANUAL", "HIGH"),

    # John Dee — Mortlake/London practice; Prague court of Rudolf II
    ("john_dee",            "london",          "ACTIVE",  "MANUAL", "HIGH"),
    ("john_dee",            "prague_hermetic", "VISITED", "MANUAL", "HIGH"),

    # Robert Fludd — London physician and Rosicrucian apologist
    ("robert_fludd",        "london",          "ACTIVE",  "MANUAL", "HIGH"),

    # Michael Maier — Prague court, Frankfurt publishing
    ("michael_maier",       "prague_hermetic", "ACTIVE",  "MANUAL", "HIGH"),

    # Porphyry — studied and taught in Rome under Plotinus
    ("porphyry",            "rome",            "ACTIVE",  "MANUAL", "HIGH"),

    # Lazzarelli — Rome, received initiation from da Correggio
    ("lodovico_lazzarelli", "rome",            "ACTIVE",  "MANUAL", "HIGH"),
    ("lodovico_lazzarelli", "venice",          "ACTIVE",  "MANUAL", "MEDIUM"),

    # Khunrath — Hamburg/Prague alchemist; visited Rudolf's court
    ("heinrich_khunrath",   "prague_hermetic", "VISITED", "MANUAL", "MEDIUM"),

    # Andreae — Strasbourg centre of early Rosicrucian movement
    ("johann_valentin_andreae", "strasbourg",  "ACTIVE",  "MANUAL", "HIGH"),

    # Reuchlin — visited Florence 1490, met Ficino and Pico
    ("johannes_reuchlin",   "florence",        "VISITED", "MANUAL", "HIGH"),

    # Francesco Patrizi — Venice, published Hermetic works
    ("francesco_patrizi",   "venice",          "ACTIVE",  "MANUAL", "HIGH"),
]

c.execute("PRAGMA table_info(person_locations)")
pl_cols = {row[1] for row in c.fetchall()}

for person_id, loc_slug, role, src, conf in associations:
    # Verify person exists
    c.execute("SELECT 1 FROM persons WHERE person_id=?", (person_id,))
    if not c.fetchone():
        print(f"  SKIP (person not found): {person_id}")
        continue
    # Verify location exists
    c.execute("SELECT 1 FROM locations WHERE slug=?", (loc_slug,))
    if not c.fetchone():
        print(f"  SKIP (location not found): {loc_slug}")
        continue

    row_data = {"person_id": person_id, "location_slug": loc_slug, "role": role}
    if "source_method" in pl_cols:
        row_data["source_method"] = src
    if "confidence" in pl_cols:
        row_data["confidence"] = conf

    placeholders = ", ".join(["?"] * len(row_data))
    col_names = ", ".join(row_data.keys())
    c.execute(
        f"INSERT OR IGNORE INTO person_locations ({col_names}) VALUES ({placeholders})",
        list(row_data.values()),
    )
    print(f"  person_location: {person_id} -> {loc_slug} ({role}) -- {c.rowcount} inserted")

conn.commit()
conn.close()
print("\nDone.")
