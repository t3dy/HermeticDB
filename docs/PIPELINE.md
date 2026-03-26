# Pipeline — EmeraldTablet

## Architecture

```
CORPUS → INDEX → SEGMENTS → TARGET MARKS → VALIDATE → ENTITIES → LINK → ASSEMBLE → BUILD → VALIDATE
```

## Execution Order

### Stage 1: Scaffold [BUILT]
```bash
python scripts/init_db.py              # Create all tables
python scripts/seed_from_json.py       # Ingest data/emerald_tablet_seed.json
```
**Status:** BUILT. 14 tables, seed data populated.
**Data allowed:** Curated seed data only. source_method = SEED_DATA.

### Stage 2: Index [REQUIRED NEXT]
```bash
python scripts/index_corpus.py         # Scan .md/.txt → corpus_documents table
```
**Status:** PLANNED. Script does not yet exist.
**Responsibility:** Register every corpus file in the database. Record path, title, doc_family, language, quality, page_count, source_type.
**Data allowed:** Deterministic metadata from filesystem + file content analysis. source_method = DETERMINISTIC.
**Table:** `corpus_documents` [PLANNED]

### Stage 3: Segment [REQUIRED NEXT]
```bash
python scripts/segment_texts.py        # Split documents → corpus_segments table
```
**Status:** PLANNED. Script does not yet exist.
**Responsibility:** Split each indexed document into page-level or section-level segments. Store text content + structural metadata (section_type, page_number).
**Data allowed:** Deterministic parsing of markdown structure (## Page N headers, section boundaries). source_method = DETERMINISTIC.
**Table:** `corpus_segments` [PLANNED]

### Stage 4: Mark [REQUIRED NEXT]
```bash
python scripts/mark_target_sections.py # Score segments → relevance flags
```
**Status:** PLANNED. Script does not yet exist.
**Responsibility:** Score each segment by keyword density, detect section types (FRONT_MATTER, CHAPTER, BIBLIOGRAPHY, INDEX, APPARATUS), detect language, flag high-relevance segments for targeted reading.
**Data allowed:** Deterministic keyword matching + regex pattern detection. source_method = DETERMINISTIC.
**Updates:** `corpus_segments.relevance_score`, `corpus_segments.section_type`, `corpus_segments.language`

### Stage 5: Validate (structural) [REQUIRED NEXT]
```bash
python scripts/validate.py --structural  # FK integrity, enum checks, orphan detection
```
**Status:** PLANNED. Script does not yet exist.
**Responsibility:** Check all FK references resolve, all enum values match CHECK constraints, no orphaned rows, report row counts per table.

### Stage 6: Extract [PLANNED]
```bash
python scripts/extract_translations.py      # Parse History_and_Translations markdown → translation_verses
python scripts/extract_research_notes.py     # Parse GPT/Gemini research text → supplementary data
python scripts/extract_weisser.py            # Parse Weisser edition markdown (limited)
```
**Status:** PLANNED. Scripts do not yet exist.
**Responsibility:** Parse specific source documents into entity tables (translation_verses, supplementary persons/bibliography/timeline).
**Data allowed:** Deterministic regex extraction from corpus segments. source_method = CORPUS_EXTRACTION.
**Prerequisite:** Stages 2-5 must be complete. Extraction scripts should reference corpus_segments, not raw files.

### Stage 7: Link [PLANNED]
```bash
python scripts/link_persons_texts.py               # Populate person_text_roles
python scripts/link_concepts.py                     # Populate concept cross-references
```
**Status:** PLANNED. Scripts do not yet exist.
**Responsibility:** Build join-table relationships from seed data and extracted entities.
**Data allowed:** Deterministic FK resolution from existing entity rows.

### Stage 8: Assemble [PLANNED]
```bash
python scripts/assemble_text_analyses.py            # Template analysis_html from DB fields
python scripts/assemble_translation_apparatus.py    # Generate parallel-text alignment data
```
**Status:** PLANNED. Scripts do not yet exist.
**Responsibility:** Template-assemble rich HTML content from database fields. No LLM. Pure string formatting.
**Data allowed:** Deterministic templating from existing DB rows.

### Stage 9: Build [PLANNED]
```bash
python scripts/build_site.py           # Generate all static HTML in site/
```
**Status:** PLANNED. Script does not yet exist.
**Responsibility:** Generate static HTML from database. Depth-aware navigation, stale file cleanup, data.json export.
**Prerequisite:** Stages 6-8 must be complete.

### Stage 10: Validate (site) [PLANNED]
```bash
python scripts/validate.py --site      # Check links, missing pages, broken references
```
**Status:** PLANNED.
**Responsibility:** Check all internal links resolve to existing files. Verify all images referenced exist.

## Full Rebuild

```bash
rm -f db/emerald_tablet.db && \
python scripts/init_db.py && \
python scripts/seed_from_json.py && \
python scripts/index_corpus.py && \
python scripts/segment_texts.py && \
python scripts/mark_target_sections.py && \
python scripts/validate.py --structural && \
python scripts/extract_translations.py && \
python scripts/extract_research_notes.py && \
python scripts/extract_weisser.py && \
python scripts/link_persons_texts.py && \
python scripts/link_concepts.py && \
python scripts/assemble_text_analyses.py && \
python scripts/assemble_translation_apparatus.py && \
python scripts/build_site.py && \
python scripts/validate.py --site
```

## Script Status Summary

| Script | Stage | Status |
|--------|-------|--------|
| `init_db.py` | 1 | BUILT |
| `seed_from_json.py` | 1 | BUILT |
| `convert_pdfs_to_md.py` | pre-pipeline | BUILT |
| `index_corpus.py` | 2 | REQUIRED NEXT |
| `segment_texts.py` | 3 | REQUIRED NEXT |
| `mark_target_sections.py` | 4 | REQUIRED NEXT |
| `validate.py` | 5/10 | REQUIRED NEXT |
| `extract_translations.py` | 6 | PLANNED |
| `extract_research_notes.py` | 6 | PLANNED |
| `extract_weisser.py` | 6 | PLANNED |
| `link_persons_texts.py` | 7 | PLANNED |
| `link_concepts.py` | 7 | PLANNED |
| `assemble_text_analyses.py` | 8 | PLANNED |
| `assemble_translation_apparatus.py` | 8 | PLANNED |
| `build_site.py` | 9 | PLANNED |

## Rules

- Each script assumes all prior stages have run
- All scripts are idempotent (safe to re-run)
- No script may write data outside its designated tables
- No script may skip validation
- Extraction scripts read from corpus_segments, not raw files
- LLM-assisted extraction (if any) writes to staging/ first, then validated and loaded by a separate script
