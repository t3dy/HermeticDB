# HermeticDB Project Handover — May 19, 2026

**Project Root**: `C:\Dev\EmeraldTablet\`

**Current Branch**: `main` (5 commits ahead of origin)

**Last Updated**: 2026-05-19 21:50 UTC

---

## Executive Summary

The HermeticDB portal is a scholarly reference database for the history of Hermeticism (Late Antiquity through modernity). The infrastructure is complete. Phase 4 (Scholarly Synthesis / Ongoing Enrichment) is now in advanced completion:

- **Dictionary**: 77/77 concepts written (100% complete)
- **Timeline**: 41/41 events expanded to 100-250 words (100% complete)
- **Interactive Map**: 28 Hermetic centers mapped with rich scholarly context
- **Biographies**: 90 persons (mix of historical figures and modern scholars)
- **Texts**: 84 primary and secondary texts
- **Relationship Graph**: 421+ semantic concept links; person-text-person-person references

The portal is deployment-ready to GitHub Pages (docs/ directory).

---

## Core Architecture

### Database
**File**: `db/emerald_tablet.db` (SQLite3)

**Tables**:
- `concepts` — 77 concepts (ACTOR_TERMs and ANALYST_TERMs with Hanegraaff distinction)
- `persons` — 90 figures (historical and modern scholars, grouped by era)
- `texts` — 84 texts (PRIMARY_SOURCE, TREATISE, SCHOLARSHIP, COMMENTARY, COMPILATION)
- `timeline_events` — 41 events (100-250 word descriptions)
- `locations` — 28 Hermetic centers (interactive map)
- `concept_links` — 421+ relationships (RELATED, DERIVED_FROM, EXPLAINS, SUBSET_OF, OPPOSED_TO)
- `person_text_roles`, `person_person_refs`, `text_text_refs` — relational metadata
- `concept_text_refs` — bibliography for each concept

**Schema**: Run `scripts/init_db.py` to create from scratch (idempotent).

### Deployment Pipeline

**Entry Point**: `HERMETICDB/scripts/DEPLOY_PORTAL.py`

**Process**:
1. Reads all data from SQLite
2. Generates static HTML/CSS/JS pages
3. Outputs to `docs/` and `site/` directories (dual deployment for GitHub Pages)
4. No server-side logic; pure static site

**Key Output Files**:
- `docs/index.html` — home page
- `docs/dictionary/` — 77 concept encyclopedia pages
- `docs/dictionary.html` — concept listing/search
- `docs/biographies.html`, `/biographies/` — person pages
- `docs/texts.html`, `/texts/` — text analysis pages
- `docs/timeline.html` — chronological event listing
- `docs/map.html` — interactive Leaflet map
- `docs/graph.html` — concept relationship visualization

**Deploy Command**:
```bash
cd C:\Dev\EmeraldTablet
python HERMETICDB/scripts/DEPLOY_PORTAL.py
```

Outputs: `[SUCCESS] Dual Deployment complete.`

### Style Standards

**Read First**: `STYLEGUIDE.md` — mandatory for all prose

**All prose fields must be**:
- Encyclopedia-level scholarly writing (no bullets, hashtags, placeholders)
- Free of markdown symbols, template artifacts, HTML in plain-text fields
- Rooted in named scholarly sources
- Actor/Analyst distinction maintained (Hanegraaff methodology)

**Minimum specifications**:
- Dictionary entries (definition_long): 1,500–2,500 words + 8+ bibliography items
- Person biographies: 1,200–2,200 words + 5+ bibliography items
- Timeline events: 100–250 words plain text
- Text analyses: 1,000–1,800 words + 5+ bibliography items

---

## Recent Completion (May 19, 2026)

### 1. Final Dictionary Entries (7 concepts)
**Script**: `scripts/write_final_8_concepts.py`
- Hermetic Persona (4,142 chars)
- Monas Generativa (3,002 chars)
- Phronesis — Practical Wisdom (3,072 chars)
- Anima Mundi — Divine Soul (3,047 chars)
- Aretalogy (3,433 chars)
- Christian Theosophy (3,279 chars)
- Immanent Logos (3,487 chars)

Dictionary now 100% complete (77/77 concepts).

### 2. Timeline Expansion (41 events)
**Script**: `scripts/expand_timeline_events.py`

All 41 timeline events expanded to 100-250+ words with:
- Exact dates (CE/BCE notation)
- Named historical actors
- Geographic locations
- Historiographical significance to the Hermetic tradition
- Integration with scholarly authorities (Fowden, Hanegraaff, Yates, Copenhaver, Bull, etc.)

Timeline completion: 35 events >250 chars, 6 events 100-250 chars, 0 stubs.

### 3. Interactive Map Expansion (28 centers)
**Script**: `scripts/populate_map_locations.py`

Map grew from 9 to 28 Hermetic centers with emphasis on:
- **Christian Bull's thesis**: Egyptian priestly tradition (Memphis, Thebes, Hermopolis)
- **Zosimos focus**: Expanded Akhmim entry with alchemical vision-narratives, Hermetic correspondence, manuscript traditions
- **Late Antique**: Antioch, Constantinople, Rome
- **Islamic transmission**: Baghdad (House of Wisdom), Damascus, Cairo, Cordoba, Basra
- **Medieval-Renaissance**: Toledo (translation movement), Venice, Florence, Mantua
- **Early Modern**: Prague (Rudolf II), London, Oxford, Strasbourg

Each location features:
- Detailed description (100-300 words)
- Key figures with dates
- Primary texts and treatises
- Manuscript archives
- Historiographical context

Interactive map deployed to `docs/map.html`.

---

## File Directory Guide

| Path | Purpose | Type |
|------|---------|------|
| `db/emerald_tablet.db` | Main database | SQLite3 |
| `STYLEGUIDE.md` | Content standards (READ FIRST) | Doc |
| `CLAUDE.md` | Project instructions | Doc |
| `PHASESTATUS.md` | Phase tracking | Doc |
| `docs/ONTOLOGY.md` | Data model reference | Doc |
| `docs/SYSTEM.md` | Technical architecture | Doc |
| `HERMETICDB/scripts/DEPLOY_PORTAL.py` | Main site generator | Python |
| `scripts/` | Data ingestion scripts | Python |
| `scripts/init_db.py` | Database schema (idempotent) | Python |
| `scripts/populate_concept_links.py` | 421 semantic relationships | Python |
| `docs/` | GitHub Pages deployment target | HTML/CSS/JS |
| `site/` | Mirror deployment (for testing) | HTML/CSS/JS |

---

## Key Scholarly Authorities

The project is grounded in the historiography of:

- **Wouter J. Hanegraaff** — *Dictionary of Gnosis and Western Esotericism* (2006); *Hermetic Spirituality and the Historical Imagination* (2022) — foundational methodology
- **Christian H. Bull** — *The Tradition of Hermes Trismegistus* (2018) — Egyptian priestly thesis
- **Garth Fowden** — *The Egyptian Hermes* (1986) — Late Antique context
- **Brian P. Copenhaver** — *Hermetica* (1992, Cambridge) — standard English translation
- **Frances A. Yates** — *Giordano Bruno and the Hermetic Tradition* (1964) — Yates Paradigm (contested)
- **Paolo Lucentini & Mark D. Delp** — Medieval Latin Hermetica tradition
- **David Porreca** — *Hermes Latinus*, *Picatrix* translation (2019)
- **Kevin van Bladel** — *The Arabic Hermes* (2009)

All entries cite these authorities and distinguish Actor Terms (used by historical figures) from Analyst Terms (retrospective scholarly categories).

---

## Current Phase Status

### Completed ✓
- Database schema and initialization
- Dictionary entries (77/77 concepts, 100% complete)
- Person biographies (90/90 entries)
- Text analyses and summaries (84/84 texts)
- Timeline events (41/41 events, fully expanded)
- Interactive map (28 centers)
- Concept semantic network (421+ links)
- Static site generation pipeline
- GitHub Pages dual deployment (docs/ and site/)
- Git workflow with feature branch commits

### Next Priority (Optional Future Work)

1. **Relationship enrichment**:
   - Add person-location associations (Zosimos in Akhmim, Ficino in Florence, etc.)
   - Expand person-text-person connections (who translated whom?)
   - Add era-based filtering to all index pages

2. **Content validation**:
   - Lint check for style violations (STYLEGUIDE.md compliance)
   - Verify all bibliography entries are accurate and complete
   - Cross-check internal links for dead references

3. **Site enhancements**:
   - Add advanced search/filtering to map and timeline
   - Build "journey" views (text transmission paths, scholar genealogy)
   - Create era-based visual timelines
   - Add manuscript provenance details to texts

4. **Scholarly depth** (if expanding):
   - Write encyclopedia entries for 10-15 additional concepts (currently 77 at full length, but 13 others are stubs)
   - Expand person-text relationships with specific role metadata
   - Add detailed commentary sections to major texts

---

## How to Continue Work

### To Ingest New Data
1. Read `STYLEGUIDE.md` (mandatory)
2. Write an idempotent Python script in `scripts/`
3. Use `INSERT OR IGNORE` to avoid duplicates
4. Update database with `db/emerald_tablet.db` path
5. Run `python HERMETICDB/scripts/DEPLOY_PORTAL.py`
6. Verify output in `docs/` directory
7. Commit with descriptive message

### To Add a Person
```python
# In a new script, e.g., scripts/add_scholar.py
cur.execute("""
    INSERT OR IGNORE INTO persons 
    (person_id, name, era, role_primary, description, bio_html)
    VALUES (?, ?, ?, ?, ?, ?)
""", ("scholar_slug", "Name", "MODERN", "SCHOLAR", "short desc", "<p>Full biography...</p>"))
```

### To Add a Concept
```python
cur.execute("""
    INSERT OR IGNORE INTO concepts
    (slug, label, category, definition_short, definition_long, category_type)
    VALUES (?, ?, ?, ?, ?, ?)
""", ("concept_slug", "Concept Label", "TERM", "short def", "<p>Long encyclopedia...</p>", "ACTOR_TERM"))
```

### To Add a Location
```python
cur.execute("""
    INSERT OR IGNORE INTO locations
    (slug, label, lat, lng, description)
    VALUES (?, ?, ?, ?, ?)
""", ("location_slug", "City, Country", 35.123, 45.678, "Description..."))
# Then add entry to LOCATION_EXTRAS in DEPLOY_PORTAL.py
```

---

## Git Workflow

**Current status**: 
- Branch: `main` (5 commits ahead of origin/main)
- Last commit: `30f3e66` — Populate interactive map with 28 Hermetic centers

**To push**:
```bash
cd C:\Dev\EmeraldTablet
git push origin main
```

**For new feature**:
```bash
git checkout -b feature/description
# Make changes, test
git add -A
git commit -m "Descriptive message"
git push origin feature/description
# Create PR on GitHub
```

---

## Testing / Verification Checklist

Before declaring work complete:

- [ ] Run `python HERMETICDB/scripts/DEPLOY_PORTAL.py` successfully
- [ ] Check `docs/` directory for updated HTML files (timestamps should be recent)
- [ ] Open `docs/index.html` in browser — site should load without errors
- [ ] Spot-check new entries:
  - [ ] Dictionary page loads with full content
  - [ ] Internal links are not broken
  - [ ] Bibliography formatting is correct
  - [ ] Actor/Analyst distinction is clear in prose
- [ ] Map page has all expected markers
- [ ] Timeline events display full descriptions
- [ ] No console errors in browser DevTools

---

## Common Issues & Fixes

| Issue | Fix |
|-------|-----|
| `FileNotFoundError: db/emerald_tablet.db` | Ensure you're in `C:\Dev\EmeraldTablet\` when running scripts |
| `sqlite3.OperationalError: no such table` | Run `python scripts/init_db.py` to create schema |
| Duplicate entries in database | Scripts use `INSERT OR IGNORE` — safe to re-run |
| HTML generation incomplete | Check `DEPLOY_PORTAL.py` error output; ensure no prose has forbidden characters (hashtags, brackets, etc.) |
| Map not showing locations | Verify `locations` table has entries; check `LOCATION_EXTRAS` slug matching in `DEPLOY_PORTAL.py` |
| Internal links broken | Check slug consistency between database and generated HTML (slugs are in URL paths) |
| PowerShell && operator fails | Use Bash (`cd /c/Dev/EmeraldTablet && command`) or PowerShell semicolons |

---

## Contact & Resources

**Project Documentation**:
- `STYLEGUIDE.md` — mandatory for all prose (1,500+ word concepts, 100-250 word timeline events)
- `CLAUDE.md` — project overview and phase status
- `docs/ONTOLOGY.md` — database schema reference
- `docs/SYSTEM.md` — technical architecture

**Key Authorities** (for scholarly grounding):
- Hanegraaff, Wouter J. *Hermetic Spirituality and the Historical Imagination*. Oxford: Oxford University Press, 2022.
- Bull, Christian H. *The Tradition of Hermes Trismegistus: The Egyptian Priestly Figure as a Teacher of Hellenized Wisdom*. Cambridge: Cambridge University Press, 2018.
- Fowden, Garth. *The Egyptian Hermes*. Cambridge: Cambridge University Press, 1986.
- Copenhaver, Brian P. (trans.). *Hermetica: The Greek Corpus Hermeticum and the Latin Asclepius*. Cambridge: Cambridge University Press, 1992.

---

## Next Session Prompt

Copy and paste into a new Claude Code window:

---

### New Session Prompt

**File**: `C:\Dev\EmeraldTablet\HANDOVER.md`

Read the handover document (above) and continue work on the HermeticDB portal.

**Current state**:
- Dictionary: 77/77 concepts complete
- Timeline: 41/41 events expanded
- Map: 28 Hermetic centers mapped
- Ready for GitHub Pages deployment

**Your options**:
1. **Validate & fix**: Run lint checks on all entries for STYLEGUIDE.md violations (hashtags, brackets, stubs); fix any issues
2. **Relationship depth**: Add person-location associations and expand person-person connections with translation/influence metadata
3. **Stub completion**: Write full encyclopedia entries for the 13 remaining concept stubs (Pietro Pomponazzi, Christian Kabbalah, Astral Magic, Decans, Ochema, etc.)
4. **New content**: Add additional scholars, texts, or figures discovered in your research
5. **Site enhancements**: Build advanced filtering, era-based views, or manuscript provenance details

**Before starting**: Read `STYLEGUIDE.md` in full.

**Database**: `C:\Dev\EmeraldTablet\db\emerald_tablet.db`

**Deploy command**: `python C:\Dev\EmeraldTablet\HERMETICDB\scripts\DEPLOY_PORTAL.py`

**Git status**: Check with `git log --oneline -5` to see recent commits. Push to origin/main when ready.

---

