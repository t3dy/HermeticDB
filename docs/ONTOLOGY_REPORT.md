# ONTOLOGY REPORT: What We Learn from the Corpus for the Hermeticism Knowledge Portal

## Executive Summary

The research inventory (84K chars from 8 KeyHermeticChats + 2 research texts) reveals that our current 14-table schema, designed for the Emerald Tablet, needs significant expansion to serve as a full Hermeticism Knowledge Portal. The corpus identifies **50+ persons**, **40+ texts**, **30+ concepts**, **7 chronological periods**, and **10 open scholarly questions** spanning late antiquity to modernity.

This report recommends schema changes, new tables, and pipeline additions based on what we've learned.

---

## 1. WHAT THE CURRENT SCHEMA GETS RIGHT

### Already adequate:
- **texts** table with `text_type` enum — covers PRIMARY_SOURCE, COMMENTARY, COMPILATION, etc.
- **persons** table with `role_primary` — covers AUTHOR, TRANSLATOR, COMMENTATOR, MYTHICAL_FIGURE, etc.
- **text_relationships** — CONTAINS, DERIVES_FROM, TRANSLATION_OF, RECENSION_OF all needed
- **translations** + **translation_verses** — parallel translation viewer works for Emerald Tablet
- **concepts** with categories — COSMOLOGICAL, ALCHEMICAL, PHILOSOPHICAL, LINGUISTIC, THEOLOGICAL all needed
- **bibliography** — adequate for scholarly references
- **manuscripts** — adequate for physical witnesses
- **timeline_events** — adequate for dated events
- **Provenance model** — source_method, review_status, confidence all essential

### The HPMarginalia pattern holds: SQLite → Python → static HTML → GitHub Pages.

---

## 2. WHAT NEEDS TO CHANGE

### 2.1 New Table: `reception_periods` [PROPOSED]

The research identifies **7 distinct periods** of Hermetic reception, each with its own institutional context, key figures, and interpretive framework. This is a first-class entity, not just a tag.

```sql
CREATE TABLE IF NOT EXISTS reception_periods (
    id              INTEGER PRIMARY KEY,
    period_id       TEXT UNIQUE NOT NULL,  -- 'late_antique', 'medieval_islamic', etc.
    name            TEXT NOT NULL,
    start_year      INTEGER NOT NULL,
    end_year        INTEGER,
    description     TEXT,
    key_innovation  TEXT,  -- one-line: what this period added to Hermeticism
    intellectual_context TEXT,
    source_method   TEXT DEFAULT 'SEED_DATA',
    confidence      TEXT DEFAULT 'HIGH'
);
```

**Seed data:** 7 rows (Late Antique Formation, Medieval Islamic Reception, Medieval European Reception, Renaissance Revival, Early Modern Esotericism, Modern Occultism & Academic Study, Contemporary Scholarship).

**Relationships:** Persons, texts, and events can be linked to periods via FK.

### 2.2 New Table: `receptions` [PROPOSED]

The research reveals that **reception** — how one author/period received and reinterpreted a Hermetic text — is a core scholarly concern. This is different from `text_relationships` (which models textual containment/derivation) and from `scholarly_refs` (which models modern scholars' interpretations).

```sql
CREATE TABLE IF NOT EXISTS receptions (
    id              INTEGER PRIMARY KEY,
    source_text_id  INTEGER REFERENCES texts(id),      -- what was received
    receiver_id     INTEGER REFERENCES persons(id),     -- who received it
    receiving_text_id INTEGER REFERENCES texts(id),     -- where they discussed it
    period_id       INTEGER REFERENCES reception_periods(id),
    reception_type  TEXT CHECK(reception_type IN (
        'TRANSLATION','CITATION','PARAPHRASE','CRITIQUE','SYNTHESIS',
        'DISTORTION','COMMENTARY','APPROPRIATION','REJECTION'
    )),
    interpretation  TEXT,  -- how they interpreted it
    notes           TEXT,
    source_method   TEXT DEFAULT 'SEED_DATA',
    confidence      TEXT DEFAULT 'MEDIUM'
);
```

**Examples:**
- Ficino TRANSLATION of Corpus Hermeticum (Renaissance period)
- Augustine CRITIQUE of Asclepius (Late Antique period)
- Hortulanus COMMENTARY on Emerald Tablet (Medieval European period)
- Bruno APPROPRIATION of Hermetic naturalism (Renaissance period)

### 2.3 New Table: `scholarly_debates` [PROPOSED]

The research identifies **10 open scholarly questions**. These are first-class entities that can be linked to persons, texts, and concepts.

```sql
CREATE TABLE IF NOT EXISTS scholarly_debates (
    id              INTEGER PRIMARY KEY,
    debate_id       TEXT UNIQUE NOT NULL,
    question_title  TEXT NOT NULL,
    description     TEXT,
    positions       TEXT,  -- JSON array of named positions
    unresolved      TEXT,  -- what remains disputed
    computational_test TEXT,  -- proposed computational approach
    source_method   TEXT DEFAULT 'SEED_DATA',
    confidence      TEXT DEFAULT 'HIGH'
);
```

**Seed data:** 10 rows (Egyptian authenticity, philosophical vs. technical unity, Gnosticism distinction, translation-as-dilution, alchemy's Hermetic basis, Iamblichus as innovator, periodization coherence, gender, efficacy, computational methods).

### 2.4 Expanded `concepts` Table: Add `registers` Column

The research reveals that many Hermetic concepts operate across multiple **registers** — metaphysical, alchemical, ritual, psychological, cosmological. Following the AtalantaClaudiens pattern:

```sql
ALTER TABLE concepts ADD COLUMN registers TEXT;
-- JSON: {"metaphysical": "...", "alchemical": "...", "ritual": "...", "psychological": "..."}
```

**Example for "Nous":**
```json
{
    "metaphysical": "Supreme intellect; first principle of being below the One",
    "alchemical": "Active principle in transmutation; the 'fire of the mind'",
    "ritual": "Object of contemplative ascent; goal of theurgic practice",
    "psychological": "Higher consciousness; capacity for divine knowledge"
}
```

### 2.5 Expanded `concepts` Table: Add `greek_term` and `arabic_term` Columns

Many concepts have technical terms in Greek and Arabic that are essential for cross-referencing:

```sql
ALTER TABLE concepts ADD COLUMN greek_term TEXT;
ALTER TABLE concepts ADD COLUMN arabic_term TEXT;
```

**Examples:**
- Nous: greek_term = "νοῦς"
- Logos: greek_term = "λόγος"
- Emanation: greek_term = "πρόοδος"
- Telesmi: arabic_term = "طلسم"

### 2.6 Expanded `persons` Table: Add `period_id` Column

```sql
ALTER TABLE persons ADD COLUMN period_id INTEGER REFERENCES reception_periods(id);
```

### 2.7 Expanded `texts` Table: Add `period_id` and `genre` Columns

```sql
ALTER TABLE texts ADD COLUMN period_id INTEGER REFERENCES reception_periods(id);
ALTER TABLE texts ADD COLUMN genre TEXT;
-- Genre values: PHILOSOPHICAL_DIALOGUE, COSMOLOGICAL_TREATISE, ALCHEMICAL_MANUAL,
-- VISIONARY_ALLEGORY, COMMENTARY, MAGICAL_TREATISE, CRITICAL_EDITION, ENCYCLOPEDIC
```

### 2.8 New Table: `treatise_sections` [PROPOSED]

For the Corpus Hermeticum and other multi-section works, we need section-level granularity:

```sql
CREATE TABLE IF NOT EXISTS treatise_sections (
    id              INTEGER PRIMARY KEY,
    text_id         INTEGER NOT NULL REFERENCES texts(id),
    section_id      TEXT NOT NULL,  -- 'CH_I', 'CH_XIII', 'Asclepius_24-26'
    title           TEXT,
    section_number  INTEGER,
    summary         TEXT,
    key_concepts    TEXT,  -- JSON array of concept slugs
    narrative_type  TEXT CHECK(narrative_type IN (
        'DIALOGUE','MONOLOGUE','VISION','HYMN','PRAYER',
        'INSTRUCTION','APOCALYPTIC','COSMOGONY'
    )),
    source_method   TEXT DEFAULT 'SEED_DATA',
    confidence      TEXT DEFAULT 'MEDIUM',
    UNIQUE(text_id, section_id)
);
```

**Seed data:** CH I (Poimandres), CH II (God and cosmos), CH VIII (Divine thought), CH XIII (On Rebirth), CH XVI (Fading of divine speech), Asclepius 24-26 (apocalyptic prophecy), Asclepius 38-41 (statue consecration), etc.

---

## 3. NEW CONCEPTS TO ADD TO SEED DATA

The research inventory reveals concepts not yet in our `emerald_tablet_seed.json`:

| Concept | Category | Why It Matters |
|---------|----------|----------------|
| **nous** (Divine Mind) | PHILOSOPHICAL | Core Hermetic principle; appears in every treatise |
| **logos** (Divine Word) | PHILOSOPHICAL | Creative principle; mediates between One and matter |
| **anthropos** (Primal Human) | PHILOSOPHICAL | Basis for human capacity for deification |
| **gnosis** (Saving Knowledge) | THEOLOGICAL | Central salvific mechanism; distinguishes Hermeticism from Gnosticism |
| **theurgy** (Divine Work) | THEOLOGICAL | Iamblichean ritual technology; bridge to operative Hermeticism |
| **palingenesia** (Regeneration) | THEOLOGICAL | Spiritual rebirth; central to CH XIII |
| **sympatheia** (Universal Correspondence) | COSMOLOGICAL | Basis of astrology, talismanic magic, theurgy |
| **pneuma** (Spirit/Breath) | PHILOSOPHICAL | Animating substance; carrier of divine intelligence |
| **barbarous_names** (Sacred Language) | LINGUISTIC | Ritual language theory; names carry inherent divine energy |
| **exitalos** (Fading through Translation) | LINGUISTIC | Translation weakens ritual efficacy; key to Iamblichus-Hermes connection |
| **tria_prima** (Salt/Sulphur/Mercury) | ALCHEMICAL | Three fundamental substances; Paracelsian development |
| **magnum_opus_stages** (Alchemical Operations) | ALCHEMICAL | Nigredo/albedo/citrinitas/rubedo sequence |
| **philosophical_vs_technical** | PHILOSOPHICAL | Division within Hermetic corpus; open scholarly debate |
| **demiurge** | COSMOLOGICAL | Craftsman god; positive in Hermeticism vs. negative in Gnosticism |

---

## 4. NEW PERSONS TO ADD

The research identifies persons not yet in our seed data:

| Person | Era | Role | Significance |
|--------|-----|------|-------------|
| Zosimos of Panopolis | 3rd c. CE | Alchemist | Bridge between Hermetic philosophy and practical alchemy |
| Iamblichus | 245-325 CE | Philosopher | Synthesizer of Hermetic ritual with Neoplatonic philosophy |
| Porphyry | 234-305 CE | Philosopher | Critic of theurgy; Iamblichus's interlocutor |
| Plotinus | 204-270 CE | Philosopher | Founder of Neoplatonism; backdrop for Hermetic philosophy |
| Augustine | 354-430 CE | Church Father | Critic of Hermetic pagan theology |
| Marsilio Ficino | 1433-1499 | Translator | Renaissance revival of Hermetica |
| Giovanni Pico della Mirandola | 1463-1494 | Philosopher | Hermetic-Kabbalistic synthesis |
| Giordano Bruno | 1548-1600 | Philosopher | Radicalization of Hermetic naturalism |
| Cornelius Agrippa | 1486-1535 | Magus | Systematizer of Hermetic magic |
| Lodovico Lazzarelli | 1447-1500 | Philosopher | Medieval-to-Renaissance bridge |
| Al-Razi (Rhazes) | 9th-10th c. | Alchemist | Major Islamic alchemy figure |
| Brian Copenhaver | contemporary | Scholar | Standard Hermetica translation |
| Christian H. Bull | contemporary | Scholar | Egyptian priestly authorship argument |
| Wouter Hanegraaff | contemporary | Scholar | Western esotericism framework |
| David Litwa | contemporary | Scholar | Fragmentary Hermetica |
| Garth Fowden | contemporary | Scholar | Egyptian Hermes (1986) |
| Kyle Fraser | contemporary | Scholar | Iamblichus-Hermes connection |

---

## 5. NEW TEXTS TO ADD

| Text | Language | Date | Type |
|------|----------|------|------|
| Corpus Hermeticum (18 treatises) | Greek | 1st-3rd c. CE | PRIMARY_SOURCE |
| Asclepius | Latin | 2nd-4th c. CE | PRIMARY_SOURCE |
| Discourse on the Eighth and Ninth | Coptic | 3rd-4th c. CE | PRIMARY_SOURCE |
| Visions of Zosimos | Greek | 3rd c. CE | PRIMARY_SOURCE |
| De mysteriis (Iamblichus) | Greek | early 4th c. CE | TREATISE |
| Picatrix (Ghayat al-Hakim) | Arabic | 10th c. CE | COMPILATION |
| Book of 24 Philosophers | Latin | 12th c. CE | TREATISE |
| De sex rerum principiis | Latin | Medieval | PSEUDO_EPIGRAPHA |
| Three Books of Occult Philosophy (Agrippa) | Latin | 1531 | TREATISE |
| 900 Theses (Pico) | Latin | 1486 | TREATISE |
| De magia (Bruno) | Italian | late 16th c. | TREATISE |
| Rosicrucian manifestos | German/Latin | 1614-1615 | TREATISE |

---

## 6. IMPLICATIONS FOR THE DATA PIPELINE

### 6.1 `mark_sections.py` (NEW — see DECKARD_SECTION_MARKING.md)
Deterministic script to score pages by keyword density, detect section boundaries, and identify high-relevance pages for targeted LLM reading.

### 6.2 `extract_corpus_hermeticum.py` (NEW)
Parse Copenhaver's Hermetica (397 text pages converted) to extract:
- Treatise boundaries (CH I through CH XVIII)
- Section-level summaries
- Key concept mentions per section
- Cross-references between treatises

### 6.3 `extract_persons_from_scholarship.py` (NEW)
Use keyword co-occurrence (person name + verb pattern) to deterministically extract person-text relationships from converted scholarship markdown.

### 6.4 Seed data expansion
`emerald_tablet_seed.json` needs to grow significantly. Following the AtalantaClaudiens lesson, consider splitting:
- `data/emerald_tablet_seed.json` — Emerald Tablet-specific data (keep existing)
- `data/hermetica_persons.json` — expanded persons
- `data/hermetica_texts.json` — expanded texts
- `data/hermetica_concepts.json` — expanded concepts with registers
- `data/reception_periods.json` — 7 periods
- `data/scholarly_debates.json` — 10 debates

### 6.5 `seed_from_json.py` Update
Modify to load from multiple JSON files. Pattern: iterate `data/*.json`, load each.

---

## 7. IMPLICATIONS FOR THE WEBSITE

### 7.1 New Sections Needed

The 9-tab site plan should expand to accommodate:

| Section | Content | Priority |
|---------|---------|----------|
| **Periods** (NEW) | 7 reception periods with context, key figures, key texts | HIGH |
| **Debates** (NEW) | 10 scholarly questions with positions and evidence | MEDIUM |
| **Treatises** (NEW) | Section-level navigation of Corpus Hermeticum | HIGH |
| **Reception Pathways** (NEW) | How texts were received across periods | MEDIUM |

### 7.2 Enhanced Existing Sections

- **Concepts**: Add multi-register view (metaphysical / alchemical / ritual tabs)
- **Persons**: Group by period; show reception relationships
- **Texts**: Add genre badges; link to reception periods
- **Timeline**: Color-code by period; add period headers

### 7.3 The Centerpiece: Parallel Translation Viewer

Still the anchor feature, but now within a richer context:
- Emerald Tablet parallel translations (already planned)
- Corpus Hermeticum treatise viewer (new)
- Links to reception history per verse/passage

---

## 8. REVISED SCHEMA SUMMARY

### Current Tables [BUILT] — 14
All existing tables remain. No changes to core schema.

### New Tables [PROPOSED] — 4
- `reception_periods` — 7 rows of periodization
- `receptions` — how texts were received across periods
- `scholarly_debates` — 10 open questions
- `treatise_sections` — section-level granularity for multi-treatise works

### Column Additions [PROPOSED] — 5
- `concepts.registers` (TEXT/JSON)
- `concepts.greek_term` (TEXT)
- `concepts.arabic_term` (TEXT)
- `persons.period_id` (FK → reception_periods)
- `texts.period_id` (FK → reception_periods)
- `texts.genre` (TEXT)

### Estimated Final Schema: 18 tables

---

## 9. WHAT NOT TO DO YET

Following the deferred schema pattern from TAKEAWAYS1.md:

1. **Don't build a RAG pipeline.** The corpus fits in context. SQL queries + targeted reads are more accurate than vector search.
2. **Don't build TEI/XML encoding.** The research notes discuss it, but SQLite-to-HTML is proven and simpler. TEI could layer on later.
3. **Don't build computational analysis tools** (topic modeling, network analysis). These are Phase 5+ features. Build the data layer first.
4. **Don't add all 50+ persons at once.** Seed the core 30 (already in seed + the 17 above). Add others as extraction scripts find them.
5. **Don't add concept cartography or 3D visualizations.** Static HTML knowledge portal first. Interactive features later.

---

## 10. RECOMMENDED NEXT STEPS

1. **Create `migrate_v2.py`** adding 4 new tables + 5 new columns
2. **Expand seed data** with new persons, texts, concepts, periods, debates
3. **Write `mark_sections.py`** for deterministic section marking
4. **Write `extract_corpus_hermeticum.py`** to parse Copenhaver
5. **Build site** with expanded sections (Periods, Debates)
6. **Targeted LLM reading** of ~370 high-relevance pages identified by marking script
