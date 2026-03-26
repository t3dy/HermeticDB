# Database Ontology — EmeraldTablet

## Entity Model

The schema distinguishes five layers:

| Layer | Tables | Purpose |
|-------|--------|---------|
| **Corpus** | corpus_documents, corpus_segments | Raw text anchoring |
| **Entity** | texts, persons, translations, concepts, commentaries, bibliography, manuscripts | Knowledge objects |
| **Relationship** | text_relationships, person_text_roles, concept_text_refs, concept_links | Links between entities |
| **Timeline** | timeline_events | Dated events |
| **Infrastructure** | schema_version | Migration tracking |

## Schema v1: 14 Tables [BUILT]

### Entity Tables (8) [BUILT]

**texts** — Primary sources, treatises, compilations, encyclopedias
- `text_id` TEXT UNIQUE — slug identifier
- `title`, `title_original` — English and original language titles
- `language` — ARABIC/LATIN/GREEK/SYRIAC/GERMAN/ENGLISH/PERSIAN/HEBREW
- `text_type` — PRIMARY_SOURCE/COMMENTARY/COMPILATION/TREATISE/ENCYCLOPEDIA/TRANSLATION/PSEUDO_EPIGRAPHA
- `date_composed_start`, `date_composed_end` — year range
- `description`, `analysis_html`, `transmission_notes`
- Provenance: `source_method`, `review_status`, `confidence`

**persons** [BUILT] — Historical, mythical, and modern scholarly figures
- `person_id` TEXT UNIQUE — slug identifier
- `name`, `name_alt` (JSON array of alternative names)
- `birth_year`, `death_year`, `era`
- `role_primary` — AUTHOR/TRANSLATOR/COMMENTATOR/SCHOLAR/MYTHICAL_FIGURE/COMPILER/EDITOR/PHILOSOPHER

**translations** [BUILT] — Named translations of texts (especially the Emerald Tablet)
- `translation_id` TEXT UNIQUE
- `source_text_id` FK → texts, `translator_id` FK → persons
- `language`, `date_approximate`, `date_year`
- `tradition` — SIRR_AL_KHALIQA/SECRETUM_SECRETORUM/JABIRIAN/IBN_UMAYL/VULGATE/HUGO_OF_SANTALLA/INDEPENDENT/MODERN

**translation_verses** [BUILT] — Verse-level text for parallel display
- `translation_id` FK → translations
- `verse_number` TEXT — "0" through "14" (text, not integer)
- `verse_sub` TEXT — sub-verse identifier ("a", "b")
- `verse_text` TEXT

**concepts** [BUILT] — Alchemical, philosophical, cosmological concepts
- `slug` TEXT UNIQUE, `label`, `label_alt` (JSON), `category`
- `definition_short`, `definition_long`, `significance`
- Category: COSMOLOGICAL/ALCHEMICAL/PHILOSOPHICAL/LINGUISTIC/THEOLOGICAL/SCIENTIFIC

**commentaries** [BUILT] — Named commentaries on texts
- `commentary_id` TEXT UNIQUE
- `author_id` FK → persons, `target_text_id` FK → texts

**bibliography** [BUILT] — Scholarly works and references
- `source_id` TEXT UNIQUE
- `pub_type` — MONOGRAPH/ARTICLE/EDITION/REVIEW/PRIMARY_SOURCE/COLLECTION/DISSERTATION/CHAPTER
- `relevance` — PRIMARY/DIRECT/CONTEXTUAL

**manuscripts** [BUILT] — Physical manuscript witnesses
- `manuscript_id` TEXT UNIQUE, `shelfmark`, `repository`, `city`
- `image_folder` — path to page scans if available

### Relationship Tables (4) [BUILT]

**text_relationships** [BUILT] — CONTAINS/DERIVES_FROM/COMMENTARY_ON/TRANSLATION_OF/RECENSION_OF/RELATED_TO

**person_text_roles** [BUILT] — AUTHOR/ATTRIBUTED_AUTHOR/TRANSLATOR/COMMENTATOR/EDITOR/DISCOVERER/COMPILER

**concept_text_refs** [BUILT] — concept_id FK × text_id FK

**concept_links** [BUILT] — RELATED/SUBSET_OF/OPPOSED_TO/DERIVED_FROM/EXPLAINS

### Timeline [BUILT]

**timeline_events** [BUILT] — year, event_type, title, description, person/text/bib FKs

### Infrastructure [BUILT]

**schema_version** [BUILT] — version, applied_at, description

---

## Corpus Layer Tables [PLANNED — REQUIRED NEXT]

These tables implement the missing middle layer between raw files and entity extraction.

**corpus_documents** [PLANNED]
```
id              INTEGER PRIMARY KEY
doc_id          TEXT UNIQUE NOT NULL     -- slugified filename
file_path       TEXT NOT NULL            -- relative path from project root
title           TEXT                     -- cleaned human-readable title
doc_family      TEXT CHECK(doc_family IN (
    'HERMETIC_CORPUS','ALCHEMICAL','SCHOLARLY_MONOGRAPH','SCHOLARLY_ARTICLE',
    'BOOK_REVIEW','RESEARCH_NOTES','CHAT_SUMMARY','CONFERENCE_PROCEEDINGS',
    'CRITICAL_EDITION','PRIMARY_SOURCE','REFERENCE_WORK','MAIER_EXTRACT'
))
language        TEXT                     -- primary language
text_quality    TEXT CHECK(text_quality IN ('HIGH','MEDIUM','LOW','EMPTY'))
source_type     TEXT CHECK(source_type IN ('PDF_EXTRACTED','OCR','CHAT_EXPORT','RESEARCH_NOTES','MAIER_EXTRACT'))
page_count      INTEGER
indexed_at      TEXT DEFAULT (datetime('now'))
source_method   TEXT DEFAULT 'DETERMINISTIC'
confidence      TEXT DEFAULT 'HIGH'
```

**corpus_segments** [PLANNED]
```
id              INTEGER PRIMARY KEY
doc_id          INTEGER NOT NULL REFERENCES corpus_documents(id)
segment_id      TEXT NOT NULL            -- 'doc_slug:page_42' or 'doc_slug:ch_3'
page_number     INTEGER
section_type    TEXT CHECK(section_type IN (
    'FRONT_MATTER','CHAPTER','SECTION','BIBLIOGRAPHY','INDEX',
    'APPENDIX','APPARATUS','NOTES','UNKNOWN'
) OR section_type IS NULL)
section_title   TEXT
text_content    TEXT NOT NULL
language        TEXT                     -- detected language for this segment
relevance_score INTEGER DEFAULT 0       -- keyword density score
has_emerald_tablet INTEGER DEFAULT 0    -- 1 if Emerald Tablet text detected
persons_mentioned TEXT                   -- JSON array of person slugs found
concepts_mentioned TEXT                  -- JSON array of concept slugs found
source_method   TEXT DEFAULT 'DETERMINISTIC'
confidence      TEXT DEFAULT 'HIGH'
UNIQUE(doc_id, segment_id)
```

---

## Proposed Future Tables [PLANNED — NOT REQUIRED YET]

These tables are documented for planning but should NOT be created until their phase begins. See `docs/ONTOLOGY_REPORT.md` for rationale.

- **reception_periods** — 7 chronological periods of Hermetic reception [PLANNED]
- **receptions** — how texts were received across periods [PLANNED]
- **scholarly_debates** — 10 open scholarly questions [PLANNED]
- **treatise_sections** — section-level granularity for multi-treatise works [PLANNED]

## Column Additions [PLANNED — NOT REQUIRED YET]

- `concepts.registers` (TEXT/JSON) — multi-register definitions [PLANNED]
- `concepts.greek_term`, `concepts.arabic_term` (TEXT) — original language terms [PLANNED]
- `persons.period_id`, `texts.period_id` (FK → reception_periods) — period linking [PLANNED]
- `texts.genre` (TEXT) — genre classification [PLANNED]

---

## Key Design Notes

1. **Work vs. Text vs. Version vs. Segment:** The `texts` table holds abstract works (Emerald Tablet, Sirr al-Khaliqa). The `translations` table holds specific versions. The `corpus_segments` table holds physical text anchored to specific pages in specific documents. These are distinct layers.
2. **Scholarly works vs. primary sources:** Both live in `bibliography` (pub_type distinguishes). The `texts` table is for historical Hermetic texts, not modern scholarship about them.
3. **Chat/LLM interpretation:** Research chats live in `corpus_documents` with `doc_family = 'CHAT_SUMMARY'` or `'RESEARCH_NOTES'`. They are not collapsed into the same layer as primary sources.
