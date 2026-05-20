# HermeticDB Handover — 2026-05-20

## State of the project

Latest commits: `3d082b8`, `271157c`  
Branch: `main`  
Deploy: `python C:\Dev\EmeraldTablet\HERMETICDB\scripts\DEPLOY_PORTAL.py`

---

## What was done in the last two sessions

### Session A (commit 56ced4f)
- Linted all prose fields — 0 style violations
- Wrote full encyclopedia entries (1,300–2,500 words) for all 12 remaining concept stubs
- Wrote 5 full biographies for zero-bio persons (Olympiodorus, Suhrawardi, Thomas of York, Thierry of Chartres, William of Conches)
- Created `person_locations` join table with 45 associations
- Extended deploy script: Key Locations on every biography page, enriched map popups

### Session B (commits 3d082b8 + 271157c)
Implemented 18 of 20 frontend improvements from `20frontendQs.md`:

| Q# | Feature | Status |
|----|---------|--------|
| Q1 | Hover preview cards on all internal links | done |
| Q2 | Map popup person names are hyperlinks | done |
| Q3 | Key Figures section on concept/dictionary pages | done |
| Q4 | Graph nodes navigate on click | done |
| Q5 | Graph edge hover tooltip (type + labels) | done |
| Q6 | Timeline era filter buttons (5 eras) | done |
| Q7 | Timeline entity auto-linking at deploy time | done |
| Q8 | Global search overlay (/ shortcut, ⌕ nav button) | done |
| Q9 | Key Concepts on biography/scholar pages | done |
| Q10 | Actor/Analyst/Hybrid badge on dictionary index cards | done |
| Q12 | Cross-link /concepts/ and /dictionary/ (gold banner) | done |
| Q13 | Back-to-top button | done |
| Q14 | Era colour stripe on biography page headers | done |
| Q17 | Primary Source / Scholarship badge on text cards | done |
| Q18 | Era nav links (pages were already being generated) | verified |
| Q20 | Graph edges colour-coded by relationship type | done |

**Not yet done:**
- Q11: Map sidebar (click location name → pan + open marker)
- Q15: Graph text search / node highlight input
- Q16: Map marker clustering (Leaflet.markercluster plugin)
- Q19: CSS line-clamp on card descriptions (cosmetic)

---

## Current database state

| Entity | Count | Notes |
|--------|-------|-------|
| concepts | 77 | All have full definition_long (1,300–2,500 words) |
| persons | 90 | 47 still have bio_html < 1,000 chars — needs expansion |
| texts | 84 | 64 still have analysis_html < 500 chars — needs expansion |
| concept_links | 421+ | Rendered on dictionary pages |
| person_locations | 45 | Powers map popup hyperlinks + biography Key Locations |
| search_index.json | 275 entries | Generated at deploy time; powers Q1 + Q8 |

---

## Biggest remaining gaps (priority order)

### 1. Expand short biographies (highest ROI for scholarly quality)
47 persons still have bio_html under 1,000 chars. The STYLEGUIDE.md minimum is 1,200 words.

Run to find them:
```sql
SELECT person_id, name, era, role_primary, length(bio_html) as len
FROM persons WHERE length(bio_html) < 1000 ORDER BY era, name;
```

Each bio needs: opening paragraph + Life and Career + Works section + Scholarly reception + Literature (5+ bibliography items). Use `scripts/write_bios_batch1.py` as a template.

### 2. Expand text analysis_html entries
64 texts have nearly empty analysis_html. Minimum: 1,000 words per STYLEGUIDE.md Texts section.

### 3. Enrich concept_text_refs (improves Q3 Key Figures display)
Only 55 rows exist linking concepts to texts. Most concepts show no Key Figures because the join chain `concept → text → person` returns empty. To fix: run INSERT scripts that add rows to `concept_text_refs`. The table schema is `(concept_id INT FK concepts.id, text_id INT FK texts.id, notes TEXT)`. The `texts.id` is the integer primary key, NOT the text_id slug.

### 4. Q11: Map sidebar
On `map.html`, add a fixed sidebar listing all 28 location names. Clicking a name fires the marker's click event and pans the map. All location data is already in `LOCATION_EXTRAS` dict in `DEPLOY_PORTAL.py` (around line 1050+). This is a pure HTML/JS addition to the `map_content` f-string in section 6.8.

### 5. Q15: Graph node search/highlight
Add an `<input>` above the D3 graph. On keyup: scale matching nodes to 2x, fade unmatched to 0.1 opacity. On clear: restore. Pure JS addition to the graph `<script>` block in `DEPLOY_PORTAL.py` (around line 1500+).

---

## Known schema quirk

`person_text_refs.text_id` stores **text slugs** (e.g. `ch_i`, `asclepius`).  
`concept_text_refs.text_id` stores **integer `texts.id`** values.  
This asymmetry is baked in. Any join between the two tables must use `texts.text_id = ptr.text_id` and `texts.id = ctr.text_id` respectively.

---

## Key files

| Purpose | File |
|---------|------|
| Canonical vision + agent rules | `PROMPTS.md` |
| Style mandate (read before any prose) | `STYLEGUIDE.md` |
| Phase completion status | `PHASESTATUS.md` |
| Full pipeline (read all of it) | `HERMETICDB/scripts/DEPLOY_PORTAL.py` |
| Database | `db/emerald_tablet.db` |
| Search index (generated) | `docs/search_index.json` |
