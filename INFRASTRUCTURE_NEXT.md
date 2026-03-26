# Infrastructure Next — Routing & Control

## Purpose

This file routes future work. Read it before starting any task.

## Where To Read For Any Task

| I need to... | Read this first |
|-------------|-----------------|
| Understand the project | `CLAUDE.md` |
| Know what's built vs planned | `PHASESTATUS.md` |
| Know the pipeline order | `docs/PIPELINE.md` |
| Know the database schema | `docs/ONTOLOGY.md` |
| Know the architecture | `docs/SYSTEM.md` |
| Know lessons from other projects | `TAKEAWAYS1.md` |
| Know what's in the corpus | `HERMETICSEARCH.md` |
| Know the section-marking heuristics | `docs/DECKARD_SECTION_MARKING.md` |
| Know the expanded ontology ideas | `docs/ONTOLOGY_REPORT.md` |
| Know the controlled vocabulary | `staging/vocab_lock.md` |
| Know the corpus inventory | `staging/research_inventory.md` |

## What NOT To Trust

- **ONTOLOGY_REPORT.md** is aspirational analysis, not current schema. Don't query tables it proposes unless they exist in `docs/ONTOLOGY.md` as `[BUILT]`.
- **Staging files** are agent output. They haven't been validated or loaded into the DB.
- **Chat exports** in `HermeticChats/` are raw working notes. Only the 8 files in `KeyHermeticChats/` have been curated.

## Immediate Build Sequence

```
1. scripts/index_corpus.py       [REQUIRED NEXT — creates corpus_documents table]
2. scripts/segment_texts.py      [REQUIRED NEXT — creates corpus_segments table]
3. scripts/mark_target_sections.py [REQUIRED NEXT — scores segments]
4. scripts/validate.py           [REQUIRED NEXT — structural checks]
5. scripts/extract_translations.py [PLANNED — first entity extraction]
```

## Rules

1. **Infrastructure comes before enrichment.** Do not extract entities until indexing + segmentation + marking are complete.
2. **Enrichment comes before UI.** Do not build site pages until entity tables are populated.
3. **New scripts go in `scripts/`.** New data goes in `data/`. Agent output goes in `staging/`.
4. **New tables require a migration script** (`scripts/migrate_v2.py`). Do not ALTER TABLE ad-hoc.
5. **If you're about to add data outside the pipeline, stop.** Put it in a seed JSON file or write a pipeline script.
6. **If you're about to query a table that doesn't exist, check ONTOLOGY.md.** If it's tagged `[PLANNED]`, create the migration first.
7. **If you're about to use LLM for something regex can do, don't.** See `docs/DECKARD_SECTION_MARKING.md`.

## Common Mistakes To Avoid

From `TAKEAWAYS1.md`:

| Mistake | Prevention |
|---------|-----------|
| Data set outside pipeline → lost on rebuild | Add to seed JSON or pipeline script |
| ONTOLOGY.md documents non-existent tables → scripts crash | Tag `[BUILT]` vs `[PLANNED]` |
| Missing `depth=1` in site generator → broken nav | Implement depth-aware `page_shell()` from day one |
| Stale HTML files after content moves → broken links | Clear output dirs before generating |
| Hardcoded DB row IDs → stale after rebuild | Use text slugs |
| LLM output loaded without validation → enum violations | Validate against CHECK constraints first |
| Scope explosion during sessions | Use `/plan-abendsen-parking` |
| Analysis without fixing → anxiety debt | Don't write reports unless you'll act on them |
