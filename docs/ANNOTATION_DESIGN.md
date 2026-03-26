# Annotation Design — Emerald Tablet Digital Edition

## Four Annotation Layers

### Layer 1: Terminological Divergence
**Purpose:** Show WHY translations differ, not just THAT they differ.
**Method:** Color-coded divergence markers (green=close, amber=shifted, red=transformed) on each verse cell. Inline annotations on key terms showing Arabic → Latin → English semantic drift.
**Key examples:**
- "from" (Arabic min) → "like" (vulgate sicut): causation → correspondence
- tilasm (talisman) → telesmi (transliteration) → perfection (Newton's substitution)
- tadbir (planning) → meditatio (meditation): management → contemplation

### Layer 2: Period Context
**Purpose:** Same text meant different things in different centuries.
**Method:** Expandable context panels per verse showing the dominant interpretive framework of each era (8th c. Arabic cosmology, 12th c. Latin translation, 14th c. Hortulanus laboratory, 17th c. Newton gravitational alchemy).
**Key insight:** The Latin reader gets aphorisms detached from the 6-book Sirr al-Khaliqa framework. Obscurity is created by decontextualization.

### Layer 3: Linguistic Registers
**Purpose:** Arabic, Latin, and English encode reality differently.
**Method:** Hoverable term annotations showing semantic fields. Word-level comparison across columns.
**Key terms:** al-aʿlā/inferius/above, ṭilasm/telesmi/perfection, tadbīr/meditatio/mediation, al-laṭīf/subtile/subtle.

### Layer 4: Alchemical Decoding (Multi-Register)
**Purpose:** Each verse operates simultaneously as cosmology, laboratory instruction, and spiritual allegory.
**Method:** Register toggle tabs (Cosmological/Laboratory/Spiritual/Philological) with color-coded annotations.
**Register colors:** Cosmological=#1a5276, Laboratory=#8b4513, Spiritual=#6c3483, Philological=#2c3e50.

## Verse Annotation Examples

### Verse 2: "As above, so below"
| Register | Annotation |
|----------|-----------|
| Cosmological | Celestial spheres generate terrestrial forms. Upper and lower realms are causally linked through emanation. |
| Laboratory | Volatile substances (above) and fixed substances (below) must be reunited through distillation and fixation. |
| Spiritual | The divine mind (above) and material existence (below) are reconciled through gnosis. |
| Philological | Arabic uses "from" (min = causal/generative). Hugo preserves this (de). Vulgate changes to "like" (sicut = correspondence). The most famous Hermetic axiom is a Latin creative reading. |

### Verse 8: "Father of telesmi / perfection"
| Register | Annotation |
|----------|-----------|
| Cosmological | The One Thing is the source of all talismanic power in the cosmos — celestial forces channeled through material forms. |
| Laboratory | The Philosopher's Stone is the master talisman enabling all transmutations. |
| Spiritual | The perfected adept becomes the source of transformative power. |
| Philological | Arabic abu al-tilasmat = "father of talismans" (linked to astral magic). Latin telesmi = transliteration (ghost word, no Latin meaning). Newton's "perfection" = interpretive substitution reflecting his own alchemical theology. Three-layer information loss. |

## Data Model [PLANNED]

```sql
CREATE TABLE verse_annotations (
    id              INTEGER PRIMARY KEY,
    translation_id  INTEGER REFERENCES translations(id),
    verse_number    TEXT NOT NULL,
    register        TEXT CHECK(register IN ('COSMOLOGICAL','LABORATORY','SPIRITUAL','PHILOLOGICAL')),
    annotation_text TEXT NOT NULL,
    term_highlighted TEXT,
    cross_ref_verse TEXT,
    source_citation TEXT,
    source_method   TEXT DEFAULT 'SEED_DATA',
    confidence      TEXT DEFAULT 'HIGH'
);
```

## Implementation Priority

1. Extract verse-level translations (deterministic, Stage 6)
2. Seed key divergence annotations (5-6 per verse, ~80 total) — v1
3. Seed period context panels (4 per verse, ~56 total) — v1
4. Register toggles (cosmological/laboratory/spiritual) — v2
5. Word-level linguistic annotations — v2

## Anti-Patterns to Prevent

- **"All translations say the same thing"** — they encode different cosmologies
- **Presentism** — reading modern meanings back into ancient texts
- **Monolithic reading** — the text is not EITHER cosmology OR lab manual; it's both simultaneously
- **Transparent translation** — every translation is an interpretation
