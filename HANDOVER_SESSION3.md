# Phase 4C Handover: Dictionary Architecture — Session 3

**Prepared by**: Session 2  
**Date**: 2026-05-21  
**Status**: Phase 4B Complete; Phase 4C Ready to Begin

---

## What You're Walking Into

**The Good News:**
- ✅ All 287 entries (81 concepts + 105 persons + 101 texts) are at scholarly standard
- ✅ Every entry has full prose content, proper structure, and bibliography
- ✅ Database is complete and validated
- ✅ Portal is deploying correctly

**The Phase 4C Task:**
Modify the deploy script to build a **two-level dictionary architecture** that surfaces concepts at two different entry points:
1. **`/dictionary/[slug].html`** — Full encyclopedia pages (1,500–2,500 words)
2. **`/dictionary/index.html`** — Browsable index with index cards (60–120 words each)

**Current State:**
- `/concepts/[slug].html` pages exist and render relational browsing (who cited this? what texts mention it?)
- `/dictionary/` pages do NOT exist yet — the deploy script doesn't generate them
- `concept_links` table is populated in the database but NOT rendered anywhere
- No cross-links between `/concepts/` and `/dictionary/` yet

---

## The Three Sub-tasks of Phase 4C

### Task 1: Build `/dictionary/[slug].html` Pages

**What to do:**
Modify `HERMETICDB/scripts/DEPLOY_PORTAL.py` to generate a page for each concept using its `definition_long` field.

**Structure required (from STYLEGUIDE.md):**
```html
<p>[Opening: 150–250 words. State term in original language. 
Declare if Actor/Analyst Term. Give earliest attestation. 
Establish significance.]</p>

<h2>Historical Usage</h2>
<p>[400–600 words. Trace usage across time—Late Antiquity through early modernity.
Name texts, authors, dates. Show evolution of meaning.]</p>

<h2>Scholarly Significance</h2>
<p>[400–600 words. How have modern scholars analyzed/debated the term?
Name scholars by name. State specific arguments explicitly.]</p>

<h2>Transmission and Variant Forms</h2>
<p>[200–400 words. OPTIONAL—include for terms with variants (Greek/Latin/Arabic).
Skip for purely modern Analyst Terms.]</p>

<h2>Related Concepts</h2>
<p>[100–200 words prose (NOT lists). Link to 3–5 related entries using <a> tags.
"The concept of <a href="../concepts/nous.html"><i>Nous</i></a> is inseparable from..."]</p>

<h2>Literature</h2>
<p>[8–15 entries. Format: Author Last, First. <i>Title</i>. Place: Publisher, Year.]</p>
```

**Current Data:**
- `concepts` table has `definition_long` field fully populated (1,500–2,500 words each)
- All concepts already have proper opening paragraphs, sections, Literature

**Implementation notes:**
- Use same template engine as current concept pages
- Output: `docs/dictionary/[slug].html` and `site/dictionary/[slug].html`
- Preserve all `<h2>` sections and bibliography from database
- Ensure proper `<a href>` links within Related Concepts section point to `/concepts/[slug].html`

**Estimated effort:** 2–3 hours

---

### Task 2: Build `/dictionary/index.html`

**What to do:**
Create an alphabetical index page showing all concepts with their Level 1 index cards.

**Structure required:**
```html
<h1>Dictionary Index</h1>

<div class="filter-controls">
  <label>Filter by category:
    <select>
      <option value="">All concepts</option>
      <option value="ACTOR_TERM">Actor Terms (historical)</option>
      <option value="ANALYST_TERM">Analyst Terms (scholarly)</option>
    </select>
  </label>
</div>

<div class="concept-grid">
  <div class="concept-card" id="gnosis">
    <h3><a href="/dictionary/gnosis.html"><i>Gnosis</i></a></h3>
    <p class="index-card">
      [60–120 word index card from definition_short field]
    </p>
    <a href="/concepts/gnosis.html" class="link-concepts">View relational page →</a>
  </div>
  [... repeat for all 81 concepts ...]
</div>
```

**Current Data:**
- `concepts` table has `definition_short` field fully populated (60–120 words each)
- `category_type` field indicates ACTOR_TERM vs ANALYST_TERM
- `label` field provides the term for sorting

**Implementation notes:**
- Generate alphabetical grid of all 81 concepts
- Filterable by `category_type` (client-side JavaScript OK, server-side also fine)
- Each card shows: concept name, index card excerpt, two links:
  - Link to `/dictionary/[slug].html` (full encyclopedia)
  - Link to `/concepts/[slug].html` (relational browsing)
- Optional: Add category badges (ACTOR_TERM / ANALYST_TERM) for visual clarity

**Estimated effort:** 1–2 hours

---

### Task 3: Render `concept_links` Table

**What to do:**
Add rendering of the `concept_links` table on both `/concepts/` and `/dictionary/` pages.

**Current state:**
- `concept_links` table is populated (from Session 1)
- Shows relationships between concepts (e.g., "gnosis" relates to "nous", "spirit", "salvation")
- **Currently zero links rendered on any page** — this is the "critical gap" from Session 1 notes

**Required rendering:**
On each concept page (both `/concepts/[slug].html` and `/dictionary/[slug].html`), add a section:

```html
<h2>Related Concepts</h2>
<p>
The concept of <a href="/concepts/nous.html"><i>Nous</i></a> is inseparable from 
<i>gnosis</i> in the philosophical Hermetica, where knowledge of God is always 
mediated through the divine intellect. The pursuit of <a href="/concepts/salvation.html">
salvation</a> in Hermetic thought depends fundamentally on <i>gnosis</i>. 
[... continue with full prose prose, not bullet lists ...]
</p>
```

**Query required:**
```sql
SELECT target_concept_id, relationship_type 
FROM concept_links 
WHERE source_concept_id = [current_concept_id]
```

Then convert each link to prose using the target concept's label and slug.

**Data availability:**
- `concept_links` table fully populated with source_id, target_id, relationship_type
- Each concept's `definition_long` field already includes a "Related Concepts" section with 100–200 words of prose AND embedded `<a>` tags
- **Just need to render the existing links via deploy script**

**Implementation notes:**
- This is NOT about adding new prose; the prose is already in the database
- This IS about making the `<a href>` links in the "Related Concepts" section actually visible and functional
- Bidirectional: if A links to B, B should link back to A

**Estimated effort:** 1–2 hours

---

## Summary: What Changes in `DEPLOY_PORTAL.py`

The deploy script currently:
1. ✅ Generates `/concepts/[slug].html` pages from concepts table
2. ✅ Generates era pages, map, graph
3. ❌ Does NOT generate `/dictionary/[slug].html` pages
4. ❌ Does NOT generate `/dictionary/index.html`
5. ❌ Does NOT render `concept_links` on concept pages

You need to add:
1. Dictionary page generation loop (1 page per concept)
2. Dictionary index page generation
3. `concept_links` table lookup and rendering logic

**Total estimated effort:** 4–6 hours  
**Complexity level:** Medium (straightforward templating, mostly copy-paste patterns)

---

## Files You'll Modify

**Primary:**
- `HERMETICDB/scripts/DEPLOY_PORTAL.py` — add dictionary page generation

**Reference (do NOT modify, just read):**
- `STYLEGUIDE.md` — dictionary page specification (lines 156–240)
- `db/emerald_tablet.db` — query structure to understand
- Existing concept page template in deploy script — use as model

**Output directories (created automatically by deploy script):**
- `docs/dictionary/[slug].html`
- `docs/dictionary/index.html`
- `site/dictionary/[slug].html`
- `site/dictionary/index.html`

---

## Testing Checklist for Phase 4C

After implementing the three tasks:

- [ ] `/dictionary/` directory exists with 81 `.html` files
- [ ] `/dictionary/index.html` exists and is browsable
- [ ] `/dictionary/gnosis.html` (pick any concept) loads correctly
- [ ] Dictionary page includes all `<h2>` sections from database
- [ ] Dictionary page includes proper Literature section
- [ ] Index page shows all 81 concepts in alphabetical order
- [ ] Index page filtering by category works
- [ ] Clicking "View relational page" on index card navigates to `/concepts/[slug].html`
- [ ] On both concept and dictionary pages, "Related Concepts" section shows embedded links
- [ ] Links in Related Concepts section navigate correctly
- [ ] Cross-links between `/concepts/` and `/dictionary/` work both directions
- [ ] Deploy script runs without errors
- [ ] No orphaned or broken links

---

## Quick Command Reference

```bash
# From C:\Dev\EmeraldTablet

# Deploy to test
python HERMETICDB/scripts/DEPLOY_PORTAL.py

# Verify a generated page exists
ls docs/dictionary/gnosis.html

# Check for broken links (manual)
grep -r "href=" docs/dictionary/ | head -20

# Commit when complete
git add -A && git commit -m "Phase 4C: Build two-level dictionary architecture"
```

---

## Notes for Success

1. **The prose is already written.** This is pure templating work. No content creation needed.

2. **Copy existing patterns.** The concept page generation logic is already in the deploy script. Duplicate that pattern for dictionary pages.

3. **Test incrementally.** After adding dictionary page generation, test one page before moving to the index. After the index, test linking.

4. **Git commit frequently.** Commit after each of the three sub-tasks completes.

5. **Reference STYLEGUIDE.md line 156+** for exact dictionary page structure. The prose is already in `definition_long` and properly formatted—just need to template it.

---

## When You're Done

- [ ] Commit: "Phase 4C: Build /dictionary/ encyclopedia pages"
- [ ] Commit: "Phase 4C: Build /dictionary/index.html alphabetical index"
- [ ] Commit: "Phase 4C: Render concept_links on concept and dictionary pages"
- [ ] Create SESSION3_SUMMARY.md with metrics
- [ ] Update PHASESTATUS.md to mark Phase 4C complete
- [ ] Portal is now a complete two-level reference system with full relational browsing

**After 4C completes, Phase 5 is: LAUNCH.**

---

**Good luck!** You're taking the portal from content-complete to architecture-complete.
