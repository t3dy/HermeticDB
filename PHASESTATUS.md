# Phase Status — EmeraldTablet

**Updated:** 2026-05-17
**Current Phase:** PHASE 4 — DICTIONARY ARCHITECTURE + CONTENT DEPTH (IN PROGRESS)

---

## What Is BUILT

| Component | Status | Details |
|-----------|--------|---------|
| `scripts/init_db.py` | BUILT | 14 tables with CHECK constraints, schema_version tracking |
| `HERMETICDB/scripts/DEPLOY_PORTAL.py` | BUILT | Static site generator with relational browsing, era pages, map, and graph |
| `db/emerald_tablet.db` | BUILT | High-fidelity relational database with scholarly provenance |
| Corpus Ingestion | BUILT | Garth Fowden, Lucentini conference, Picatrix, Liber XXIV, and full CH |
| `scripts/consolidate_and_expand.py` | BUILT | Database cleanup, deduplication, and misclassification fixes |
| `scripts/mass_link_scholarship.py` | BUILT | Relational mapping between authors, texts, and themes |
| `scripts/refine_historical_data.py` | BUILT | Standardization of eras and text composition dates |
| Interactive Features | BUILT | Leaflet.js Map and D3.js Relationship Graph integrated |
| System Files | BUILT | PROMPTS.md, STYLEGUIDE.md, CLAUDE.md, AGENTS.md — overhauled 2026-05-17 |

---

## Database Row Counts (as of 2026-05-17)

| Table | Rows | Content Status |
|-------|------|----------------|
| texts | 84 | Most analysis_html under 300 words — needs expansion |
| persons | 90 | Most bio_html under 300 words — needs expansion |
| concepts | 74 (DB shows 77) | definition_short mostly empty; definition_long stubs — needs major expansion |
| timeline_events | 34 | Many under 100 words — needs expansion |
| person_text_refs | 65 | Adequate |
| concept_text_refs | 40 | Adequate |
| concept_links | populated | **NOT RENDERED in deploy script — critical gap** |
| corpus_segments | ~200+ | Adequate |

---

## Phase 4 Goals (Priority Order)

### 4A — Content Depth: Dictionary (ACTIVE)
For all 74+ concepts:
- [ ] Expand `definition_short` to 60–120 words (index card standard) — currently mostly empty
- [ ] Expand `definition_long` to 1,500–2,500 words (encyclopedia standard) — currently stubs
- [ ] Add `<h2>Literature</h2>` section with 8–15 bibliography items to each concept

Priority concepts for first pass (ACTOR_TERMs at the core of the tradition):
1. *Gnosis* | 2. *Nous* | 3. *Prisca theologia* | 4. *Magia naturalis* | 5. *Theurgy* | 6. *Spiritus* | 7. *Logos* | 8. *Sympatheia* | 9. *Pneuma* | 10. *Lumen Gloriae*

Priority ANALYST_TERMs:
1. *Hermeticism* | 2. *Western Esotericism* | 3. Yates Paradigm | 4. *Rejected Knowledge* | 5. *Philosophia Perennis*

### 4B — Content Depth: Persons and Texts (ACTIVE)
- [ ] Expand all `bio_html` to 1,200–2,200 words
- [ ] Expand all `analysis_html` to 1,000–1,800 words
- [ ] Add `<h2>Literature</h2>` sections to all person and text entries

Priority persons:
- Hermes Trismegistus, Marsilio Ficino, Cornelius Agrippa, Giordano Bruno, Jabir ibn Hayyan, Zosimos of Panopolis, Iamblichus, Wouter Hanegraaff, Garth Fowden, Frances Yates

Priority texts:
- Corpus Hermeticum, Asclepius, Emerald Tablet, Picatrix, Liber XXIV Philosophorum, De sex rerum principiis

### 4C — Site Architecture: Two-Level Dictionary (PLANNED)
- [ ] Build `/dictionary/[slug].html` encyclopedia pages in DEPLOY_PORTAL.py
- [ ] Build `/dictionary/index.html` with index card grid + filtering
- [ ] Render `concept_links` table on concept and dictionary pages
- [ ] Add "Read the full dictionary entry →" cross-links from `/concepts/` to `/dictionary/`
- [ ] Add category-browsing within dictionary section

### 4D — Relational Browsing Enhancement (PLANNED)
- [ ] Render `concept_links` table on `/concepts/[slug].html` pages (currently zero links rendered)
- [ ] Add person-to-concept links on biography pages
- [ ] Add text-to-concept links on text analysis pages
- [ ] Ensure every entity page links to at least 3 other entities

---

## Known Gaps (Discovered 2026-05-17)

| Gap | Impact | Fix |
|-----|--------|-----|
| `concept_links` table not rendered | Zero relational browsing between concepts | Add to DEPLOY_PORTAL.py |
| `definition_short` mostly empty | Dictionary index shows "No short definition available..." | Agent Type A pass |
| All prose under target word counts | Portal fails to serve scholarly constituency | Agent Type A, B passes |
| No `Literature` sections anywhere | Cannot verify claims; fails bibliography standard | Add to all encyclopedia entries |
| `significance` column unused | Data present but not displayed | Add to concept page rendering |

---

## Agent Swarm Queue

Use the staging file pattern (agents write JSON to `staging/`, main session validates and loads). See `PROMPTS.md` Part VI for full agent specs.

**Next swarm task**: Agent Type A pass on the 15 priority concepts listed in 4A above.
Main session must pre-query: slug, label, category_type, all concept_text_refs, all concept_links.

---

## Repository Reference
- **Repo**: `t3dy/HermeticDB`
- **Path**: `c:\Dev\EmeraldTablet`
- **GitHub Pages**: serves from `docs/`
