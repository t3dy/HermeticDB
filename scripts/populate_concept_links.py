"""
Populate concept_links table with relationships between concepts.
Target: 150-200 links across 77 concepts (2-3 outgoing per concept).

Relationships:
- RELATED: shares conceptual domain
- SUBSET_OF: narrower instance or aspect of broader concept
- OPPOSED_TO: explicitly opposed or debated
- DERIVED_FROM: develops from or depends on
- EXPLAINS: provides explanation or mechanism for
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "db" / "emerald_tablet.db"

# Define concept relationships (from_slug -> to_slug, relationship_type)
LINKS = [
    # Gnosis relationships
    ("gnosis", "nous", "DERIVED_FROM"),
    ("gnosis", "palingenesia", "RELATED"),
    ("gnosis", "lumen_gloriae", "RELATED"),

    # Nous relationships
    ("nous", "logos", "RELATED"),
    ("nous", "pneuma", "RELATED"),
    ("nous", "demiurge", "EXPLAINS"),

    # Logos relationships
    ("logos", "pneuma", "RELATED"),
    ("logos", "correspondence", "EXPLAINS"),

    # Pneuma relationships
    ("pneuma", "spiritus_mundi", "RELATED"),
    ("pneuma", "sympatheia", "RELATED"),

    # Theurgy relationships
    ("theurgy", "gnosis", "RELATED"),
    ("theurgy", "planetary_spirits", "EXPLAINS"),
    ("theurgy", "palingenesia", "RELATED"),
    ("theurgy", "sympatheia", "EXPLAINS"),

    # Sympatheia relationships
    ("sympatheia", "correspondence", "RELATED"),
    ("sympatheia", "macrocosm_microcosm", "EXPLAINS"),

    # Correspondence relationships
    ("correspondence", "macrocosm_microcosm", "RELATED"),
    ("correspondence", "planetary_mansions", "EXPLAINS"),
    ("correspondence", "decans", "EXPLAINS"),

    # Alchemy relationships
    ("alchemy", "tria_prima", "EXPLAINS"),
    ("alchemy", "prima_materia", "RELATED"),
    ("alchemy", "lapis_philosophorum", "RELATED"),
    ("alchemy", "solve_et_coagula", "EXPLAINS"),
    ("alchemy", "spagyrics", "DERIVED_FROM"),

    # Tria Prima relationships
    ("tria_prima", "prima_materia", "RELATED"),
    ("tria_prima", "quintessence", "EXPLAINS"),

    # Spagyrics relationships
    ("spagyrics", "quintessence", "EXPLAINS"),
    ("spagyrics", "alchemy", "DERIVED_FROM"),

    # Palingenesia relationships
    ("palingenesia", "way_of_hermes", "RELATED"),
    ("palingenesia", "unio_mystica", "RELATED"),

    # Way of Hermes relationships
    ("way_of_hermes", "prisca_theologia", "RELATED"),
    ("way_of_hermes", "gnosis", "EXPLAINS"),

    # Prisca Theologia relationships
    ("prisca_theologia", "philosophia_perennis", "RELATED"),
    ("prisca_theologia", "magia_naturalis", "RELATED"),

    # Magia Naturalis relationships
    ("magia_naturalis", "sympatheia", "EXPLAINS"),
    ("magia_naturalis", "correspondence", "EXPLAINS"),
    ("magia_naturalis", "astral_magic", "DERIVED_FROM"),

    # Astral Magic relationships
    ("astral_magic", "planetary_spirits", "EXPLAINS"),
    ("astral_magic", "decans", "EXPLAINS"),
    ("astral_magic", "talismans", "EXPLAINS"),

    # Planetary Spirits relationships
    ("planetary_spirits", "planetary_mansions", "RELATED"),
    ("planetary_spirits", "correspondence", "EXPLAINS"),

    # Monad relationships
    ("monad", "nous", "DERIVED_FROM"),
    ("monad", "ogdoad", "RELATED"),
    ("monad", "ennead", "RELATED"),

    # Hermetic Circle relationships
    ("hermetic_circles", "way_of_hermes", "RELATED"),
    ("hermetic_circles", "theurgy", "RELATED"),

    # Lumen Gloriae relationships
    ("lumen_gloriae", "nous", "RELATED"),
    ("lumen_gloriae", "logos", "RELATED"),

    # Philosophia Perennis relationships
    ("philosophia_perennis", "prisca_theologia", "RELATED"),
    ("philosophia_perennis", "hermeticism", "RELATED"),

    # Hermeticism relationships (Analyst Term)
    ("philosophical_hermetica", "technical_hermetica", "RELATED"),
    ("philosophical_hermetica", "gnosis", "EXPLAINS"),
    ("technical_hermetica", "alchemy", "EXPLAINS"),
    ("technical_hermetica", "astral_magic", "EXPLAINS"),

    # Macrocosm/Microcosm relationships
    ("macrocosm_microcosm", "correspondence", "RELATED"),
    ("macrocosm_microcosm", "sympatheia", "EXPLAINS"),

    # Deification/theosis relationships
    ("deification", "palingenesia", "RELATED"),
    ("deification", "gnosis", "EXPLAINS"),

    # Ochema relationships
    ("ochema", "pneuma", "RELATED"),
    ("ochema", "astral_body", "RELATED"),

    # Okhema relationships (variant of ochema)
    ("okhema", "pneuma", "RELATED"),

    # Archeus relationships
    ("archeus", "anima_mundi", "RELATED"),
    ("archeus", "spiritus_mundi", "RELATED"),

    # Anima Mundi relationships
    ("anima_mundi", "sympatheia", "EXPLAINS"),
    ("anima_mundi", "world_soul", "RELATED"),

    # Prima Materia relationships
    ("prima_materia", "lapis_philosophorum", "RELATED"),
    ("prima_materia", "solve_et_coagula", "EXPLAINS"),

    # Solve et Coagula relationships
    ("solve_et_coagula", "palingenesia", "RELATED"),
    ("solve_et_coagula", "alchemy", "EXPLAINS"),

    # Lapis Philosophorum relationships
    ("lapis_philosophorum", "quintessence", "RELATED"),
    ("lapis_philosophorum", "chrysopoeia", "EXPLAINS"),

    # Phantasmata relationships
    ("phantasmata", "imagination_magical", "EXPLAINS"),
    ("phantasmata", "nous", "RELATED"),

    # Imagination Magical relationships
    ("imagination_magical", "theurgy", "RELATED"),

    # Hermes Trismegistus relationships (if exists as concept)
    ("hermes_persona", "way_of_hermes", "EXPLAINS"),
    ("hermes_persona", "prisca_theologia", "EXPLAINS"),

    # Christran Kabbalah relationships
    ("christian_kabbalah", "prisca_theologia", "RELATED"),
    ("christian_kabbalah", "correspondance", "RELATED"),

    # Emanations relationships
    ("emanations", "logos", "EXPLAINS"),
    ("emanations", "monad", "DERIVED_FROM"),

    # Pronoia relationships
    ("pronoia", "sympatheia", "RELATED"),
    ("pronoia", "correspondence", "RELATED"),
]

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# Get all concepts to map slugs to IDs
cur.execute("SELECT id, slug FROM concepts")
slug_map = {slug: id for id, slug in cur.fetchall()}

inserted = 0
skipped = 0

for from_slug, to_slug, rel_type in LINKS:
    if from_slug not in slug_map or to_slug not in slug_map:
        skipped += 1
        continue

    from_id = slug_map[from_slug]
    to_id = slug_map[to_slug]

    try:
        cur.execute(
            "INSERT OR IGNORE INTO concept_links (from_concept_id, to_concept_id, relationship) VALUES (?, ?, ?)",
            (from_id, to_id, rel_type)
        )
        if cur.rowcount > 0:
            inserted += 1
    except Exception as e:
        skipped += 1

conn.commit()
conn.close()

print(f"[CONCEPT LINKS] Inserted: {inserted} | Skipped: {skipped} (not found)")
print(f"Total links target: 150-200 (achieved: {inserted})")
