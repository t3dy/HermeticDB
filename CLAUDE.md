# Claude Code Instructions — EmeraldTablet

## Current Phase

**INFRASTRUCTURE HARDENING / CORPUS STRUCTURING**

The project has enough corpus material. Collection is no longer the bottleneck. The priority is building stable transformation infrastructure: corpus indexing → segmentation → validation → entity extraction. Do not expand scope. Do not build UI. Do not invent ontology beyond what is needed for corpus plumbing.

## Project Overview

Hermeticism Knowledge Portal anchored on the Emerald Tablet (Tabula Smaragdina). Covers late antiquity through early modern period. Database-driven static site following the AtalantaClaudiens/HPMarginalia architecture.

## Architecture

SQLite → Python pipeline → static HTML/CSS/JS → GitHub Pages. No frameworks, stdlib only.

**Required data flow (the middle layer is mandatory):**

```
CORPUS FILES (.md, .txt)
    ↓
INDEX (scripts/index_corpus.py → corpus_documents table)
    ↓
SEGMENTS (scripts/segment_texts.py → corpus_segments table)
    ↓
TARGET MARKS (scripts/mark_target_sections.py → segment scores/flags)
    ↓
VALIDATION (scripts/validate.py — structural checks)
    ↓
ENTITY EXTRACTION (scripts/extract_*.py → entity tables)
    ↓
LINKING (scripts/link_*.py → relationship tables)
    ↓
ASSEMBLY (scripts/assemble_*.py → analysis_html)
    ↓
SITE BUILD (scripts/build_site.py → site/)
    ↓
FINAL VALIDATION (scripts/validate.py — site/link checks)
```

The site is a consumer of the structured database, not the place where structure gets improvised.

## Key Files

| Purpose | File |
|---------|------|
| Entry point | This file |
| Phase status | `PHASESTATUS.md` |
| Routing guide | `INFRASTRUCTURE_NEXT.md` |
| Schema | `docs/ONTOLOGY.md` |
| Pipeline | `docs/PIPELINE.md` |
| Architecture | `docs/SYSTEM.md` |
| Lessons learned | `TAKEAWAYS1.md` |
| Corpus search report | `HERMETICSEARCH.md` |
| Database | `db/emerald_tablet.db` (gitignored, rebuilt from scripts) |
| Seed data | `data/emerald_tablet_seed.json` |
| Output | `site/` (static HTML deployed to GitHub Pages) |

## Deterministic / LLM Boundary (Deckard Rule)

| Category | Examples | Tool |
|----------|----------|------|
| **DETERMINISTIC** | Parsing, indexing, segmentation, keyword scoring, section detection, FK validation, HTML generation | Python (regex, sqlite3) |
| **JUDGMENT (LLM)** | Scholarly argument extraction, concept elaboration, translation alignment, analysis assembly | Targeted LLM reading of marked sections |
| **WASTE** | Using LLM for structure extraction, keyword counting, language detection, header parsing | — |
| **DANGER** | LLM output directly into DB without validation gate | — |

LLM usage is bounded, late-stage, and validated. It happens only AFTER indexing, segmentation, and marking are complete. All LLM output goes to `staging/` first, is validated against schema CHECK constraints, then loaded.

## Pipeline Rules

1. **No ad-hoc data.** If data is not seeded, indexed, or produced by a listed pipeline script, it is fragile and out of contract. Any data set outside the standard pipeline will be lost on rebuild.
2. **Provenance on every row.** Every database row must carry `source_method`, `review_status`, `confidence`. No exceptions.
3. **Idempotent scripts.** Every script uses `CREATE TABLE IF NOT EXISTS` and `INSERT OR IGNORE`. Safe to re-run.
4. **Rebuild reproduces everything.** The full rebuild command in `docs/PIPELINE.md` must produce the complete database from scratch.
5. **Validate before and after.** Structural validation after entity extraction. Link validation after site build.
6. **BUILT vs PLANNED.** All docs must distinguish implemented from aspirational. Tag `[BUILT]` or `[PLANNED]`.
7. **Slugs, not row IDs.** Never hardcode database row IDs. Use text slugs that survive rebuilds.
8. **Infrastructure before enrichment.** Corpus indexing and segmentation must be complete before entity extraction begins.
9. **Enrichment before UI.** Entity tables must be populated before site build is meaningful.

## Vocabulary Lock

All enum values are defined in `scripts/init_db.py` CHECK constraints. See `staging/vocab_lock.md` for the complete list. Swarm agents and LLM output must use only these values. If a new value is needed, add it to the CHECK constraint in `init_db.py` first.

## Swarm Rules

- Background agents are read-only
- Agents write only to `staging/` (JSON or Markdown)
- Main session validates and merges staging output into pipeline
- Agents cannot run Bash (permission system blocks shell access)
- Use staging-file pattern, not direct DB writes

## Key Conventions

- Python stdlib only (sqlite3, json, re, pathlib)
- Verse numbering uses TEXT (0-14 scheme with sub-verses like "6a")
- Text relationships model containment, derivation, and translation chains
- Persons table includes both historical and mythical figures
- Corpus files live in root, `hermetic/`, and `KeyHermeticChats/`
- Converted scholarship goes alongside source PDFs as `.md` files
