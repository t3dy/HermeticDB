# TAKEAWAYS1.md — Lessons from Prior Knowledge Portal Projects

**Compiled for:** EmeraldTablet Knowledge Portal
**Sources analyzed:** AtalantaClaudiens, HPMarginalia (Hypnerotomachia Poliphili), Shakespeare Sonnets, DreamBase/MegaBase, PKD Festival Site, Alchemy Scryfall
**Date:** 2026-03-25

---

## 1. ARCHITECTURE: WHAT WORKS

### 1.1 The HPMarginalia Pattern Is Proven

All successful knowledge portals follow the same data flow:

```
Curated Seed JSON → Python Scripts (deterministic) → SQLite (source of truth)
    → build_site.py (static HTML generator) → site/ → GitHub Pages
```

**Evidence across projects:**
| Project | Tables | Rows | Pages | Status |
|---------|--------|------|-------|--------|
| HPMarginalia | 27 | ~3,500 | 535+ | Live, production-ready |
| AtalantaClaudiens | 14 | ~600 | 60+ | Live, phases 3B/4 ready |
| Shakespeare | 21 | ~5,000 | planned | Phase 2 enrichment |

**Why it wins:** Zero dependencies beyond Python stdlib. Static sites survive decades (MIT's Renaissance marginalia site: 29 years unchanged). Trivial to rebuild, audit, debug. No server to maintain.

**Takeaway for EmeraldTablet:** We're already on this pattern. Don't deviate.

### 1.2 SQLite-Not-ORM Is Non-Negotiable

All projects use raw `sqlite3` from Python stdlib. No ORMs, no query builders.

**Why:** SQL is easier to audit than ORM abstraction layers. No N+1 queries. Raw SQL can be pasted directly into sqlite3 CLI for debugging. No migration drift ("docs say column X exists but ORM never created it").

**Takeaway:** Already implemented in `init_db.py`. Keep it.

### 1.3 Deterministic Before LLM (Deckard Boundary)

Shakespeare project made this explicit:
- **DETERMINISTIC (Python):** Parsing, schema, validation, template assembly
- **JUDGMENT (LLM):** Literary interpretation, device identification, analysis
- **WASTE:** Don't use LLM for structure extraction, syllable counts, HTML generation
- **DANGER:** Never allow LLM output directly into DB without validation gate

AtalantaClaudiens achieved **50/50 mottos and 47/50 discourses via regex** before touching LLM. The 3 remaining cases are bounded, documented, and cheap to solve with targeted LLM pass.

**Takeaway for EmeraldTablet:** Extract verse-level translations via deterministic regex first. Use LLM only for bounded enrichment (analysis assembly, concept elaboration). Our `extract_translations.py` should be pure regex; `assemble_text_analyses.py` can use templates but not LLM.

---

## 2. SCHEMA: PATTERNS AND ANTI-PATTERNS

### 2.1 Provenance on Every Row (Three-Axis Model)

Every datum carries three fields:
```
source_method  ∈ {SEED_DATA, CORPUS_EXTRACTION, LLM_ASSISTED, HUMAN_VERIFIED, DETERMINISTIC}
review_status  ∈ {DRAFT, REVIEWED, VERIFIED}  -- forward-only promotion
confidence     ∈ {HIGH, MEDIUM, LOW}
```

**Already implemented** in our `init_db.py`. This is the single most important pattern across all projects.

**Key lesson from AtalantaClaudiens:** LLM-extracted data starts as DRAFT/MEDIUM. Deterministic data starts as DRAFT/HIGH. Only VERIFIED data is protected from overwrite.

**Key lesson from HPMarginalia:** Tag provenance at creation, not after the fact. Retroactively tagging 282 records as LLM_ASSISTED was painful. Adding `needs_review` and `source_method` columns via migration was necessary but would have been free if done in v1 schema.

**Takeaway:** We have this right. Don't skip it on any new table.

### 2.2 Deferred Schema: Build Only What You Need Now

AtalantaClaudiens documented 18 tables but only built 13. The 7 planned tables were tagged `[PLANNED]` in ONTOLOGY.md. Migrations created only when phases unlocked.

**The anti-pattern** (from BLUNDERS321.md): Documenting planned tables without `[PLANNED]` tags confused agents into trying to query non-existent tables, causing crashes.

**Takeaway for EmeraldTablet:** Our 14-table schema is complete for Phase 1. If we add tables later (e.g., `alchemical_processes`, `recension_variants`), they must be explicitly tagged `[PLANNED]` in ONTOLOGY.md until the migration script exists.

### 2.3 CHECK Constraints Prevent Silent Corruption

**Problem from Shakespeare:** No CHECK constraints on enum fields. Invalid values inserted silently. Swarm agents invented `device_id` values not in the schema (`POLYPTOTON`, `RHETORICAL_QUESTION`). Ontology drifted under LLM pressure.

**Solution:** Added CHECK constraints to init_db.py; added `validate_enrichment.py --fix` as pre-load gate.

**Takeaway:** Our `init_db.py` already has CHECK constraints on `language`, `text_type`, `role_primary`, `relationship_type`, etc. This is correct and must be maintained. Any future swarm/LLM output must be validated against these constraints before loading.

### 2.4 Multi-Register Terms (Polysemy Model)

AtalantaClaudiens stores dictionary terms with a `registers` JSON column:
```json
{
  "alchemical": "The red stone produced at the final stage...",
  "medical": "In Paracelsianism, the universal cure...",
  "spiritual": "The perfected self achieved through inner transformation...",
  "cosmological": "The universal principle governing planetary harmony..."
}
```

**Why it works:** Alchemical terms are polymorphic. The same word (coniunctio, lapis, Sol) has different meanings in material, medical, spiritual, and cosmic registers.

**Takeaway for EmeraldTablet:** Our `concepts` table uses `definition_short` + `definition_long` + `significance`. This is adequate for now, but if the concept definitions grow to need multi-register breakdown (alchemical vs. cosmological vs. linguistic meanings of "telesmi"), we should add a `registers` JSON column.

### 2.5 Concordance Tables Must Come First

**Hard lesson from HPMarginalia:** The Hypnerotomachia Poliphili has 6 numbering systems (sequential page, signature, folio, photo number, Internet Archive index, woodcut catalog number). Off-by-one errors plagued the project until `page_concordance` (448 rows mapping all systems) was built.

**Specific failure:** Woodcut entries placed at systematically wrong pages (241 instead of 242, 243 instead of 244) because LLM-assisted seeding used different numbering systems. Fixing required `fix_woodcut_pages.py` to correct 10 off-by-one errors, delete 5 duplicates, merge 13 entries.

**Takeaway for EmeraldTablet:** The Emerald Tablet has multiple verse-numbering systems (Arabic verses, Latin verses, Holmyard numbering, Ruska numbering, the "0-14" scheme from Bauer & Lindemann). We chose the 0-14 scheme as canonical in `translation_verses`. This is our concordance. If we later ingest verse numberings from other sources, we need a mapping table.

### 2.6 Text Relationships Over Flat Categories

**Pattern (EmeraldTablet, already implemented):** Instead of a `recension` column on `texts`, the `text_relationships` table models containment, derivation, and translation chains:
- Sirr al-Khaliqa CONTAINS Emerald Tablet
- De secretis naturae TRANSLATION_OF Sirr al-Khaliqa
- Vulgate RECENSION_OF Emerald Tablet

**Why this is better than flat categories:** The Emerald Tablet's transmission is a directed graph, not a flat taxonomy. A text can simultaneously be contained in one work and derived from another.

**Validation:** This pattern aligns with HPMarginalia's approach to copy-annotation relationships (annotations → copies → hands) and AtalantaClaudiens' emblem-source matrix.

---

## 3. PIPELINE: CRITICAL LESSONS

### 3.1 Any Data Set Outside the Standard Pipeline Is Fragile

**Disaster from AtalantaClaudiens (BLUNDERS321.md):** A background agent ran `rm -f db/atalanta.db && [full pipeline]`, wiping 31/50 alchemical stage classifications. Those classifications were set by `classify_stages.py`, which was session-specific and not in the standard rebuild sequence.

**Fix:** Moved alchemical stage data into `atalanta_fugiens_seed.json` so it survives rebuilds.

**Takeaway for EmeraldTablet:** Every piece of data must either be:
1. In `emerald_tablet_seed.json` (survives rebuild)
2. In an extraction script listed in PIPELINE.md (runs during rebuild)
3. Or explicitly documented as session-only data that will be lost on rebuild

Our pipeline rebuild command (`rm -f db/emerald_tablet.db && python scripts/init_db.py && ...`) must reproduce the complete database. If we add data via ad-hoc scripts, those scripts must be added to PIPELINE.md.

### 3.2 Extraction Is a Multi-Pass Problem

AtalantaClaudiens needed three passes:
1. **Deterministic regex** → 50/50 mottos, 47/50 discourses
2. **Pass 2 recovery** (position interpolation) → filled 2 remaining
3. **LLM-assisted** (proposed, bounded) → 3 hard OCR cases

HPMarginalia similarly needed 4 phases of image reading, each building on the previous.

**Takeaway for EmeraldTablet:** `extract_translations.py` will be our primary extraction pass. We may need a `extract_translations_pass2.py` for edge cases in the History & Translations markdown (some translations have irregular verse numbering, embedded commentary, or missing verse numbers). Plan for it; don't force everything into one script.

### 3.3 Idempotent Scripts Are Non-Negotiable

Every project uses `CREATE TABLE IF NOT EXISTS` and `INSERT OR IGNORE`. Every script is safe to re-run.

**Why:** Agents may re-run scripts. Builds may be interrupted. Partial state must not corrupt the database.

**Already implemented** in our scripts. Keep it.

### 3.4 Schema Migration as First-Class Artifact

AtalantaClaudiens has 5 migration scripts (`migrate_v2.py` through `migrate_v4_enrichment.py`). Each:
- Checks `PRAGMA table_info` before `ALTER TABLE`
- Updates `schema_version` table
- Is idempotent

**Key lesson from HPMarginalia:** Scripts crashed trying to reference `ia_page` column (actually named `page_1499_ia`). CHECK constraint rejected `source_method = 'IA_SCAN_VERIFIED'` (not in allowed list).

**Fix:** Always read `PRAGMA table_info(tablename)` before writing any script that touches the schema.

**Takeaway:** When we need to add columns or tables later, create `scripts/migrate_v2.py`, not ad-hoc ALTER TABLE commands.

### 3.5 Pre-Load Validation Gate

**Critical lesson from Shakespeare:** Without `validate_enrichment.py --fix`, swarm agent output violated FK constraints and was discovered reactively at INSERT time.

**Pattern:**
1. LLM/swarm produces JSON output
2. `validate_enrichment.py` checks: valid FKs, valid enum values, no duplicates, required fields present
3. `--fix` mode maps invalid values to valid ones (e.g., `POLYPTOTON` → added to schema after editorial review)
4. Only validated output enters the database

**Takeaway for EmeraldTablet:** If we ever use LLM/swarm for enrichment (e.g., generating concept elaborations, analysis HTML), we need a validation gate between LLM output and database insertion. Our `validate.py` script should check FK integrity, enum values, and required fields.

---

## 4. SITE GENERATION: PATTERNS

### 4.1 Two-Phase Rendering

AtalantaClaudiens uses two-phase rendering:
1. **Data assembly** (`seed_emblem_analyses.py`): Assembles `analysis_html` from DB fields using templates, no LLM
2. **HTML generation** (`build_site.py`): Reads assembled HTML and renders pages

**Why:** Decoupling data assembly from HTML generation makes each phase testable independently. You can verify `analysis_html` in the DB without rendering. Same analysis can appear in multiple page formats.

**Takeaway:** Our planned `assemble_text_analyses.py` and `assemble_translation_apparatus.py` follow this pattern. They produce structured data; `build_site.py` renders it.

### 4.2 Navigation Depth for Multi-Level Sites

**Bug from AtalantaClaudiens (BLUNDERS321.md):** Dictionary index page at `site/dictionary/index.html` had broken CSS and navigation. Root cause: `page_shell()` call was missing `depth=1` parameter.

**Pattern:**
```python
def page_shell(..., depth=0):
    prefix = '../' * depth  # depth=0 for root, depth=1 for /texts/, depth=2 for /texts/detail/
    nav_html(prefix=prefix)
```

**Same bug in HPMarginalia:** Concordance page built with `depth=0` instead of `depth=1` — all CSS/nav links wrong.

**Takeaway:** Our `build_site.py` must implement depth-aware relative paths from day one. Every page in a subdirectory (`texts/`, `persons/`, `translations/`, `concepts/`, `manuscripts/`) needs `depth=1`.

### 4.3 Build Scripts Must Clean Stale Output

**Bug from HPMarginalia (CORPUSEXTRACTIONSILLINESS.md):** When 18 woodcuts moved from one gallery to another, the build script never deleted the old HTML files. 47 stale pages persisted, creating 113 broken links.

**Fix:** Added stale page cleanup to the build script. Added `check_links.py` validator.

**Takeaway:** Our `build_site.py` should clear `site/texts/`, `site/persons/`, etc. before generating new pages. Otherwise, deleted entities leave ghost HTML files.

### 4.4 Link Validation After Every Build

HPMarginalia built `check_links.py` that checks ALL `href` and `src` attributes in generated HTML. Found 113 broken links.

**Takeaway:** Our `validate.py` should include a link-checking pass after `build_site.py` runs. Check every internal link resolves to an existing file.

### 4.5 Export data.json for JavaScript Consumers

Both AtalantaClaudiens and HPMarginalia export a `site/data.json` with all entity data for JavaScript filtering, searching, and dynamic views (timeline, gallery).

**Takeaway:** Our `build_site.py` should export `data.json` containing texts, persons, translations, concepts, timeline events — enabling client-side filtering without server infrastructure.

---

## 5. DOCUMENTATION: HARD-WON RULES

### 5.1 Document Reality, Not Aspiration

**Anti-pattern (BLUNDERS321.md):** ONTOLOGY.md documented 18 tables including columns that didn't exist in the DB. Scripts crashed.

**Fix:** Tag all tables/columns as `[BUILT]` or `[PLANNED]`.

**Anti-pattern (Shakespeare):** PHASESTATUS.md claimed 17 sonnets enriched; actual state was 71. Session logging lapsed.

**Rule:** Update PHASESTATUS.md at end of every session with actual database row counts.

**Takeaway:** Our ONTOLOGY.md currently documents only built tables (all 14). If we add planned tables, tag them explicitly. Keep a PHASESTATUS.md updated with actual counts.

### 5.2 DOCUMENTAIRTRAFFICCONTROL.md (Routing Guide)

AtalantaClaudiens created a routing guide that maps tasks to documents:
- "I need to add a scholar" → Read `docs/ONTOLOGY.md` (scholars table), then `EMBLEMGUIDE.md`
- "I need to fix an image" → Read `data/emblem_manifest.json`
- "I need to understand a past mistake" → Read `docs/reports/IMAGEFOLLIES.md`

**Why it works:** Prevents agents from reading 30 docs to figure out which is current.

**Takeaway:** Create a similar routing guide for EmeraldTablet once we have more docs. For now, CLAUDE.md is sufficient as the single entry point.

### 5.3 Lessons-Learned Reports Prevent Repeat Mistakes

AtalantaClaudiens has 20+ reports in `docs/reports/`:
- TRIALANDERROR.md (extraction bugs)
- IMAGEFOLLIES.md (9 failed approaches)
- BLUNDERS321.md (10 session mistakes)
- DOWEREALLYNEEDARAG.md (why RAG isn't needed)

HPMarginalia has similar:
- TRIALSANDERRORS.md (8 lessons)
- CORPUSEXTRACTIONSILLINESS.md (ghost pages)
- MISTAKESTOAVOID.md (12 hard-won mistakes)

**Takeaway:** When we encounter problems in EmeraldTablet, document them. This file (TAKEAWAYS1.md) is the first such report.

---

## 6. MULTI-AGENT OPERATIONS: WHAT WORKS AND WHAT DOESN'T

### 6.1 Staging File Pattern (Proven)

```
AGENT A → staging/scholars.json
AGENT B → staging/bibliography.json
AGENT C → staging/timeline.json
    ↓
MAIN SESSION: Validate → Merge → Rebuild
```

**Why:** Agents can't run Bash (permission system blocks shell access for background agents). Staging files avoid this entirely.

### 6.2 Vocabulary Lock Is Essential for Swarm Output

**Disaster from Shakespeare:** Without locked `device_id` lists in agent prompts, swarm output invented new IDs (`POLYPTOTON`, `RHETORICAL_QUESTION`, `ALLUSION`). Ontology drifted under LLM pressure.

**Fix:** `prep_batch.py` generates prompts with explicit enum lists and instructions to reject unmapped values.

**Takeaway:** If we use LLM agents for EmeraldTablet enrichment, lock the vocabulary:
- Valid `text_type` values: PRIMARY_SOURCE, COMMENTARY, COMPILATION, TREATISE, ENCYCLOPEDIA, TRANSLATION, PSEUDO_EPIGRAPHA
- Valid `role` values: AUTHOR, ATTRIBUTED_AUTHOR, TRANSLATOR, COMMENTATOR, EDITOR, DISCOVERER, COMPILER
- Agents must use these exact values or flag for human review.

### 6.3 Hard Rule: Background Agents Can't Run Bash

Documented in AtalantaClaudiens SWARMGUIDELINES.md. Background agents stall asking for Bash permission because they can't prompt the user.

**Working patterns:**
1. Staging files (agents write JSON, main session merges)
2. Pre-queried data (main exports DB to JSON, agents read it)
3. Report-only audits (agents write Markdown analysis, main acts on it)

---

## 7. ANTI-PATTERNS: WHAT TO AVOID

### 7.1 Analysis Without Fixing Is Just Anxiety

**DreamBase lesson (COST_AND_MISTAKES_ANALYSIS.md):** Session generated 7 analysis documents identifying bugs. None were fixed. The sidecar JSON crash bug was identified early and remained unfixed after 14 prompts.

**Rule:** Don't write analysis reports unless you're going to fix what they find. Visibility without action doesn't move projects forward.

### 7.2 Hardcoded IDs + Dynamic DB = Fragility

**DreamBase:** 30 scholar pages store hardcoded `conversation_ids` in Python dicts. If DB is rebuilt, IDs change. Every page silently links to wrong conversations.

**Takeaway:** Never hardcode database row IDs in application code. Use slugs (`text_id`, `person_id`, `translation_id`) that survive rebuilds. Our schema already uses TEXT UNIQUE slugs for all entities.

### 7.3 Don't Build Meta-Tools for Your Todo List

**DreamBase:** Session built `action_map.html` (15 minutes) as a development planning tool embedded in the public app. Conceptually misplaced, accessible only by direct URL, never used again.

**Rule:** Use existing tools (TodoWrite, PHASESTATUS.md, GitHub Issues) for project management. Don't build custom planning infrastructure.

### 7.4 Big Numbers Feel Productive But Aren't

**DreamBase:** 50 takeaways (AI-generated, not evidence-linked) vs. 10 verified takeaways. 20 audit dimensions vs. 3 actual fixes.

**Rule:** 5 completed takeaways > 50 abandoned ones. Default to small, actionable numbers.

### 7.5 Scope Explosion During Sessions

**DreamBase:** Session started with "audit" → "build showcase" → "plan swarm for ALL" → "build another showcase" → "cross-pollinate ALL pages" → "build ACTION MAP WEBSITE."

**Rule:** This is what `/plan-abendsen-parking` is for. When new ideas emerge during building, park them instead of expanding scope.

### 7.6 Don't Trust Two Scholarly Sources to Agree on Page Numbers

**HPMarginalia:** Temple of Venus scenes represented 4 times at wrong pages because multiple scholarly sources described the same scene differently. LLM generated separate entries for each description.

**Rule:** Cross-reference against the physical artifact. For EmeraldTablet: when ingesting verse numbers from different sources, verify against the actual text, not other scholars' numbering.

### 7.7 Test on 10 Before Building for 300

**HPMarginalia:** File-size analysis for woodcut detection would have failed in 5 minutes with 10 calibration samples. Instead, a full pipeline was built, 51 pages downloaded, and the method was useless (at 600 DPI, text pages compress nearly as large as woodcut pages).

**Rule:** Always calibrate with a small sample before scaling a pipeline.

---

## 8. SPECIFIC RECOMMENDATIONS FOR EMERALDTABLET

Based on all lessons above, here are actionable recommendations:

### 8.1 Schema (Already Good, Minor Additions)
- [x] Provenance on every row — implemented
- [x] CHECK constraints on enums — implemented
- [x] TEXT slugs for all entities — implemented
- [ ] Consider adding `registers` JSON column to `concepts` table if definitions grow to need multi-register breakdown
- [ ] Tag any future planned tables as `[PLANNED]` in ONTOLOGY.md

### 8.2 Pipeline (Needs Attention)
- [ ] Ensure rebuild command in PIPELINE.md reproduces complete database
- [ ] Plan for multi-pass extraction (`extract_translations.py` → `extract_translations_pass2.py`)
- [ ] Add `validate.py` with link-checking after `build_site.py`
- [ ] If using LLM enrichment, add validation gate between LLM output and DB

### 8.3 Site Generation (Must Implement)
- [ ] Depth-aware relative paths in `page_shell()` from day one
- [ ] Clear stale HTML before generating new pages in `build_site.py`
- [ ] Export `data.json` for client-side filtering
- [ ] Link validation pass in `validate.py`

### 8.4 Documentation (Discipline)
- [ ] Create PHASESTATUS.md with actual row counts after each session
- [ ] Keep ONTOLOGY.md in sync with actual schema (tag BUILT vs PLANNED)
- [ ] Document problems when they occur (this file is the first report)

### 8.5 Data Integrity (Critical)
- [ ] Never hardcode database row IDs — use slugs
- [ ] All ad-hoc data must enter the pipeline or be documented as ephemeral
- [ ] If swarm agents produce output, validate against schema CHECK constraints before loading
- [ ] Cross-reference verse numbering against actual text, not other scholars' numbering

---

## 9. THE ONE RULE THAT MATTERS MOST

From BLUNDERS321.md, TRIALANDERROR.md, CORPUSEXTRACTIONSILLINESS.md, IMAGEFOLLIES.md, and COST_AND_MISTAKES_ANALYSIS.md, the single most repeated lesson is:

> **The bug is in the plumbing, not the detector.**

Most debugging time is spent improving regex patterns, adding LLM passes, or building clever detection systems. But the actual bugs are in dedup logic, sort order, boundary calculations, missing `depth=1` parameters, stale HTML files, and hardcoded IDs.

The boring infrastructure — validation scripts, link checkers, concordance tables, stale file cleanup — prevents more bugs than any amount of clever extraction logic.

Build the plumbing right. The content will follow.
