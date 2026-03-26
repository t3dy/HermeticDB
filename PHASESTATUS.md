# Phase Status — EmeraldTablet

**Updated:** 2026-03-25
**Current Phase:** INFRASTRUCTURE HARDENING / CORPUS STRUCTURING

## What Is BUILT

| Component | Status | Details |
|-----------|--------|---------|
| `scripts/init_db.py` | BUILT | 14 tables with CHECK constraints, schema_version tracking |
| `scripts/seed_from_json.py` | BUILT | Populates all core tables from JSON with FK resolution |
| `scripts/convert_pdfs_to_md.py` | BUILT | Batch PDF-to-markdown converter (PyMuPDF + EasyOCR fallback) |
| `data/emerald_tablet_seed.json` | BUILT | 12 texts, 22 persons, 15 translations, 8 concepts, 15 bibliography, 4 manuscripts, 19 timeline events |
| `db/emerald_tablet.db` | BUILT | 14 tables populated, schema v1 |
| Corpus conversion | BUILT | ~60 markdown files from PDFs + 8 curated KeyHermeticChats |
| `docs/SYSTEM.md` | BUILT | Architecture documentation |
| `docs/ONTOLOGY.md` | BUILT | Schema documentation |
| `docs/PIPELINE.md` | BUILT | Pipeline execution order |
| `TAKEAWAYS1.md` | BUILT | Lessons from prior projects |
| `HERMETICSEARCH.md` | BUILT | Corpus and chat search report |
| `docs/DECKARD_SECTION_MARKING.md` | BUILT | Deterministic vs LLM boundary for section marking |
| `docs/ONTOLOGY_REPORT.md` | BUILT | Expanded ontology analysis from research inventory |
| `staging/research_inventory.md` | BUILT | 84K structured inventory from KeyHermeticChats |

## Database Row Counts (actual, as of 2026-03-25)

| Table | Rows |
|-------|------|
| texts | 12 |
| persons | 22 |
| translations | 15 |
| concepts | 8 |
| bibliography | 15 |
| manuscripts | 4 |
| timeline_events | 19 |
| text_relationships | 8 |
| concept_text_refs | 15 |
| concept_links | 6 |
| person_text_roles | 0 |
| commentaries | 0 |
| translation_verses | 0 |
| schema_version | 1 |

## What Is PARTIAL

| Component | Status | What Remains |
|-----------|--------|-------------|
| Corpus conversion | 3 OCR jobs running | Merkel/Debus (221pp), Ibn Umail (228pp), Lazzarelli (376pp) |
| Corpus conversion | 4 PDFs >100MB skipped | Weisser (731pp scanned Arabic), Khunrath Vol 1 (done), Zosimos (done) |

## What Is NEXT (Immediate Build Sequence)

The missing middle layer is the priority:

- [ ] 1. Create `scripts/index_corpus.py` [REQUIRED NEXT]
  - Scans all .md/.txt files, populates `corpus_documents` table
  - Records: path, title, doc_family, language, quality, page_count, source_type
- [ ] 2. Create `scripts/segment_texts.py` [REQUIRED NEXT]
  - Splits indexed documents into page-level or section-level segments
  - Populates `corpus_segments` table with text content + metadata
- [ ] 3. Create `scripts/mark_target_sections.py` [REQUIRED NEXT]
  - Keyword density scoring, section-type detection, language detection
  - Updates segments with relevance scores and flags
- [ ] 4. Create `scripts/validate.py` [REQUIRED NEXT]
  - FK integrity, enum validation, orphan detection, row count report
  - Post-build: link checking on generated HTML
- [ ] 5. Run `extract_translations.py` — parse verse-level translations from History markdown
- [ ] 6. Run `link_persons_texts.py` — populate person_text_roles from seed data relationships
- [ ] 7. Run `build_site.py` — scaffold with proven patterns (depth-aware nav, stale cleanup)

## Blockers / Risks

- **No blockers.** All tools available (PyMuPDF, EasyOCR, Python stdlib).
- **Risk:** Scope expansion. The corpus is large enough. The bottleneck is structure, not collection.
- **Risk:** Premature site/UI work. The site is downstream of stable corpus plumbing.
- **Risk:** Ad-hoc data entry outside the pipeline. Any data not produced by a listed script is fragile.

## Do Not Drift

- Do NOT add more PDFs or corpus files unless specifically requested
- Do NOT build site pages before indexing and segmentation are complete
- Do NOT use LLM for tasks that can be done with regex/Python
- Do NOT hardcode database row IDs
- Do NOT add tables or columns without updating ONTOLOGY.md and creating a migration script
- Do NOT skip validation steps
- The missing middle layer (INDEX → SEGMENTS → MARKS) is the immediate priority
