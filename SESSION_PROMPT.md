# Session 7 Prompt — Complete Remaining 26 Text Analyses

**Goal:** Close the final content gap. Finish all 26 remaining text entries (73/99 → 100/99 equivalent).

**Context:** HermeticDB is a scholarly reference portal on the history of Hermeticism. It's in Phase 4 (content depth). Session 5 brought text analyses from 33% → 73%. Session 6 ingested Liana Saif papers on Arabic Hermetica (added 4 texts, 2 scholars, deployed successfully).

**Current state:**
- **73/99 texts** (73.7%) have full analysis_html (1,000–1,800 words, DGWE standard, 5–12 bibliography items)
- **26 texts remain** with zero or <1,000 chars of analysis_html — mostly lower-priority (scholarly commentaries, fragments, specialized texts)
- **Live site:** https://t3dy.github.io/HermeticDB

**What you'll do:**

1. **Read HANDOVER.md** (2 min) — Current state, gap audit, remaining 26 texts
2. **Read STYLEGUIDE.md** (5 min) — Text analysis template and word-count minimums (1,000 words minimum, required section structure)
3. **Pick a batch of 4–5 texts** from the remaining 26 (start with HIGH-priority: pgm_vii, iamblichus_mysteriis, sh_fragments)
4. **Write full analysis_html for each** using the template:
   - Opening paragraph (200–300 words): full title in `<i>tags</i>`, date, language, place in canon
   - `<h2>Content and Doctrine</h2>` (300–500 words): specific tractates, arguments, key passages
   - `<h2>Transmission and Manuscript Tradition</h2>` (200–400 words): survival, translations, key transmitters, editions
   - `<h2>Modern Scholarship</h2>` (150–300 words): authoritative editions, current scholarly debates
   - `<h2>Literature</h2>` (5–12 bibliography items in DGWE format)
5. **Create an idempotent UPDATE script** in `scripts/` (e.g., `expand_final_texts_batch_1.py`)
6. **Run the ingestion script** to update the database
7. **Deploy:** `python HERMETICDB/scripts/DEPLOY_PORTAL.py`
8. **Commit:** `git add -A && git commit -m "Session 7: Expand [N] text analyses (→ [X]/99)"`
9. **Update HANDOVER.md** when done with new session summary

**Remaining 26 texts (priority order):**

**HIGH-priority (start here — 3–4 texts):**
- `pgm_vii` (0 chars) — Greek Magical Papyri, fragment collection
- `iamblichus_mysteriis` (194 chars) — De Mysteriis, key theurgy text
- `sh_fragments` (835 chars) — Stobaean Hermes fragments
- `hermetic_spirituality_hanegraaff` (745 chars) — Modern Hanegraaff study

**MEDIUM-priority (12–15 texts):**
- theatrum_chemicum_britannicum, psychology_and_alchemy, liber_beibeniis, manetho_aegyptiaca, armenian_definitions, etc.

**LOWER-priority (8–10 texts):**
- esotericism_and_the_academy, specialized regional variants, ancillary texts

**Key authorities for these texts:**
- Fowden, Copenhaver, Hanegraaff, Mahé, Lucentini, Saif, van Bladel, Principe, Ebeling
- (See HANDOVER.md for full reference list and STYLEGUIDE.md for citation format)

**Estimate:** 2–3 hours to complete all 26, finishing in 2–3 focused batches.

**Quick check:**
```bash
# See remaining 26
python -c "import sqlite3; c=sqlite3.connect(r'c:\Dev\EmeraldTablet\db\emerald_tablet.db').cursor(); c.execute(\"SELECT text_id, length(coalesce(analysis_html,'')) FROM texts WHERE length(coalesce(analysis_html,'')) < 1000 ORDER BY 2 DESC\"); [print(r) for r in c.fetchall()[:30]]"

# Deploy
python C:\Dev\EmeraldTablet\HERMETICDB\scripts\DEPLOY_PORTAL.py

# Commit
git -C C:\Dev\EmeraldTablet add -A; git -C C:\Dev\EmeraldTablet commit -m "message"
```

**Files you'll need:**
- `PROMPTS.md` — Canonical vision + agent rules
- `STYLEGUIDE.md` — Word counts + required HTML structure
- `HANDOVER.md` — Current state + all remaining gaps
- `db/emerald_tablet.db` — SQLite database
- `HERMETICDB/scripts/DEPLOY_PORTAL.py` — Deployment script

**When done:** Update HANDOVER.md with final count (should be 99/99 = 100%), commit, and you're ready to move to remaining biographies in Session 8.
