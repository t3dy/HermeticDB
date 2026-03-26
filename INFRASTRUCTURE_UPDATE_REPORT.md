# Infrastructure Update Report

**Date:** 2026-03-25
**Phase:** Infrastructure Hardening

## Files Changed

| File | Action | What Changed |
|------|--------|-------------|
| `CLAUDE.md` | **REWRITTEN** | Added: Current Phase declaration, Deckard boundary table, pipeline rules (no ad-hoc data, provenance mandatory, BUILT vs PLANNED), swarm rules, vocabulary lock reference. Removed: aspirational site sections list (downstream of plumbing). |
| `PHASESTATUS.md` | **CREATED** | Concrete phase status: what's BUILT, what's PARTIAL, what's NEXT. Actual DB row counts. Immediate build checklist. "Do not drift" section. |
| `docs/PIPELINE.md` | **REWRITTEN** | 10-stage pipeline replacing 5-stage. Added: INDEX, SEGMENT, MARK stages as REQUIRED NEXT. Every stage has: status (BUILT/PLANNED), responsibility, data allowed, prerequisite. Script status summary table. |
| `docs/SYSTEM.md` | **REWRITTEN** | Added: "The Required Middle Layer" section with full data flow diagram. System boundary table (Corpus → Index → Segments → Entities → Site). Deterministic/LLM boundary. Updated directory structure. |
| `docs/ONTOLOGY.md` | **REWRITTEN** | Added [BUILT] tags to all 14 existing tables. Added corpus_documents and corpus_segments as [PLANNED — REQUIRED NEXT] with full column specs. Moved future tables (reception_periods, receptions, scholarly_debates, treatise_sections) to "PLANNED — NOT REQUIRED YET" section. Added design note on Work vs Text vs Version vs Segment distinction. |
| `INFRASTRUCTURE_NEXT.md` | **CREATED** | Routing guide: task → document mapping. Immediate build sequence. Rules. Common mistakes to avoid (from TAKEAWAYS1.md). |
| `.gitignore` | **CREATED** | Excludes db/, staging/, __pycache__, *.pdf, *.png, .claude/ |
| `docs/DECKARD_SECTION_MARKING.md` | **CREATED** (earlier in session) | Deterministic vs LLM boundary for section marking. Regex patterns for headers, keywords, language detection. Token budget estimates. |
| `docs/ONTOLOGY_REPORT.md` | **CREATED** (earlier in session) | Expanded ontology analysis from research inventory. New tables, persons, texts, concepts proposed. Clearly marked as aspirational analysis, not implemented schema. |

## Architectural Corrections Made

1. **Formalized the missing middle layer.** The pipeline now requires: CORPUS → INDEX → SEGMENTS → MARKS → VALIDATE before any entity extraction can begin. This is enforced in CLAUDE.md, PIPELINE.md, SYSTEM.md, and INFRASTRUCTURE_NEXT.md.

2. **Separated BUILT from PLANNED.** All 14 existing tables tagged [BUILT]. Two new corpus-layer tables (corpus_documents, corpus_segments) tagged [PLANNED — REQUIRED NEXT]. Four future tables tagged [PLANNED — NOT REQUIRED YET].

3. **Made the Deckard boundary explicit.** CLAUDE.md now has a table classifying every task type as DETERMINISTIC, JUDGMENT, WASTE, or DANGER.

4. **Enforced the no-ad-hoc-data rule.** CLAUDE.md states: "If data is not seeded, indexed, or produced by a listed pipeline script, it is fragile and out of contract."

5. **Made the site downstream.** CLAUDE.md, SYSTEM.md, and PIPELINE.md all state that site build is Stage 9, dependent on Stages 2-8.

6. **Added validation gates.** Pipeline now has two validation points: structural (Stage 5, after marking) and site (Stage 10, after build).

## Contradictions Found and Resolved

| Contradiction | Resolution |
|--------------|-----------|
| Old CLAUDE.md listed site sections as if they were the project's primary output | Rewritten to focus on infrastructure; site sections moved to downstream position |
| Old PIPELINE.md jumped from seed → extract → link → build with no intermediate layer | Added INDEX, SEGMENT, MARK stages as required intermediate steps |
| Old ONTOLOGY.md had no BUILT/PLANNED distinction | All tables now tagged |
| No PHASESTATUS.md existed | Created with actual row counts and honest status |
| docs/ONTOLOGY_REPORT.md proposed 4 new tables as if they should be built now | Explicitly marked as "PLANNED — NOT REQUIRED YET" in ONTOLOGY.md |

## What Remains Unbuilt

### REQUIRED NEXT (immediate priority)
- `scripts/index_corpus.py` — creates corpus_documents table, scans all .md/.txt files
- `scripts/segment_texts.py` — creates corpus_segments table, splits documents into segments
- `scripts/mark_target_sections.py` — scores segments by keyword density
- `scripts/validate.py` — FK integrity, enum validation, orphan detection
- `scripts/migrate_v2.py` — adds corpus_documents and corpus_segments tables to schema

### PLANNED (after middle layer is complete)
- `scripts/extract_translations.py` — parse verse-level translations
- `scripts/extract_research_notes.py` — parse GPT/Gemini research text
- `scripts/link_persons_texts.py` — populate person_text_roles
- `scripts/build_site.py` — static site generation
- All other Stage 6-10 scripts

### BACKGROUND (still running)
- OCR: Merkel/Debus (221pp), Ibn Umail (228pp), Lazzarelli (376pp)

## Next Deterministic Implementation Tasks

1. Write `scripts/migrate_v2.py` — add `corpus_documents` and `corpus_segments` tables
2. Write `scripts/index_corpus.py` — scan filesystem, populate `corpus_documents`
3. Write `scripts/segment_texts.py` — split each document into page-level segments
4. Write `scripts/mark_target_sections.py` — keyword scoring, section-type detection
5. Write `scripts/validate.py` — structural integrity checks
6. Run full rebuild: `init_db → seed → migrate_v2 → index → segment → mark → validate`
7. Review validation output. Fix any issues.
8. Only then proceed to entity extraction (Stage 6).
