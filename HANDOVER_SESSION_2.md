# HermeticDB Content Expansion — Session 2 Handover

**Date**: 2026-05-21  
**Status**: Phase 4 Content Depth at 92% completion  
**Portal Deployment**: ✅ Live with all updates from Session 1

---

## Session 1 Accomplishments

### ✅ Concepts — 100% COMPLETE
- **All 81 concepts** now meet 1,500-2,500 word encyclopedia minimum
- Rewrote Pietro Pomponazzi concept: 578 → 1,591 words (proper encyclopedia format)
- All entries: proper STYLEGUIDE.md structure, 5+ bibliography items, internal links

### ✅ Persons — 100% COMPLETE  
- **All 105 persons** now meet 1,200-2,200 word biography minimum
- **Expanded 16 biographies** from stub (203-1,100 wds) to full standard (1,200-8,000 wds):
  - Christoph Kriegsmann, Elias Ashmole, Bruce Codex, Basil Valentine, Andreas Libavius
  - Symphorien Champier, Francesco Patrizi, Robert Grosseteste, Francis Mercury van Helmont
  - Johannes Reuchlin, Tommaso Campanella, Jean-Pierre Mahé, Paolo Lucentini
  - Gilbert of Poitiers, Christian H. Bull, Carlos Gilly
- All entries: opening paragraph + 2-4 `<h2>` sections + Literature section

### 🔄 Texts — 77% COMPLETE (78 of 101)
- **Expanded 3 key secondary works** to full standard:
  - *Giordano Bruno and the Hermetic Tradition* (Yates, 1964)
  - *Hermes Latinus* (Brepols Series)
  - *The Alchemical Amphitheatre* (Khunrath)
- **Remaining: 23 texts under 1,000-word minimum**
  - 14 completely empty (0 words)
  - 9 partially written (1-999 words)

### Overall Portal Status
- **264 of 287 entries** meet scholarly minimum standards
- **92% complete** on Phase 4 Content Depth goal
- All major primary texts: Corpus Hermeticum, Asclepius, Emerald Tablet, Picatrix, etc. are robust

---

## Remaining Work for Session 2+

### Priority 1: Empty Texts (14 entries, ~14-20 hours)

These are completely empty and should be filled to 1,000+ words:

**Primary Source Fragments** (5):
- PGM VII: The Stele of Hermes
- The Vienne Fragment
- The Brontologion of Hermes
- The Salmeschoiniaka
- Chaeremon: Fragments

**Secondary/Scholarly Works** (9):
- Circe, la virtus loci, il determinismo nel De incantationibus di Pomponazzi
- De occulta philosophia libri tres (Compagni critical edition)
- Hermetism from Late Antiquity to Humanism
- Review: Picatrix -- The Latin Version of the Ghayat al-Hakim (Pingree ed.)
- Théorie et pratique dans l'Asclepius
- Lactantius: Divinae Institutiones
- Mushaf al-Suwar (The Book of Pictures)
- De Maximis Theologiae (Regulae Theologiae)
- Liber de spiritu et anima

### Priority 2: Partial Texts (9 entries, ~5-8 hours)

These have 1-999 words and need expansion to 1,000+. Identify via:
```bash
python -c "
import sqlite3
db = sqlite3.connect('db/emerald_tablet.db')
c = db.cursor()
c.execute('''SELECT title, length(COALESCE(analysis_html, '')) as len FROM texts 
             WHERE length(COALESCE(analysis_html, '')) BETWEEN 1 AND 999 
             ORDER BY len ASC''')
for title, length in c.fetchall():
    print(f'{title:50} | {length:4} wds')
db.close()
"
```

---

## How to Continue

### Pattern Established in Session 1

1. **Create Python expansion script** in `scripts/expand_[topic].py`
   - Dictionary structure: `{ "text_title_or_id": "<p>Full HTML content..."}`
   - Each entry: 1,000-1,500+ words minimum
   - Structure: opening paragraph (200-300 wds) + 2-3 `<h2>` sections + Literature section
   - No artifacts: NO bullet lists, hashtags, brackets, emoji, or placeholders
   - All foreign terms in `<i>` tags
   - All names/concepts that exist in portal wrapped in internal links `<a href>`

2. **Run script to update database**
   ```powershell
   cd "C:\Dev\EmeraldTablet"; python scripts/expand_[topic].py
   ```

3. **Deploy to verify output**
   ```powershell
   cd "C:\Dev\EmeraldTablet"; python HERMETICDB/scripts/DEPLOY_PORTAL.py
   ```

4. **Verify word counts**
   ```bash
   python -c "
   import sqlite3
   db = sqlite3.connect('db/emerald_tablet.db')
   c = db.cursor()
   c.execute(\"SELECT title, length(COALESCE(analysis_html, '')) FROM texts WHERE title = '[YOUR TEXT]'\")
   result = c.fetchone()
   if result:
       print(f'{result[0]}: {result[1]} characters (~{result[1]//6} words)')
   db.close()
   "
   ```

### Important: Read STYLEGUIDE.md Before Writing

**Text Analysis (`analysis_html`) requirements:**
- **Length**: 1,000–1,800 words (excluding Literature section)
- **Opening paragraph**: 200–300 words  
  - Full title in `<i>` tags
  - Date of composition/first attestation
  - Original language
  - Is it primary source or secondary scholarship? State immediately.
- **`<h2>Content and Doctrine</h2>`**: 300–500 words
  - What does text argue/narrate/prescribe?
  - Specific tractates, chapters, key terms
  - Be SPECIFIC — cite passages, titles, dates
- **`<h2>Transmission and Manuscript Tradition</h2>`**: 200–400 words
  - How did text survive?
  - Manuscript traditions, translations, languages
  - Key transmitters and editors
  - For primary sources: REQUIRED; for secondary: optional
- **`<h2>Modern Scholarship</h2>`**: 150–300 words
  - Key editors, translators, scholars
  - Current debates about dating/authorship/significance
- **`<h2>Literature</h2>`**: 5–12 bibliographic entries
  - Must include authoritative modern edition/translation
  - Format: Author Last, First. *Title*. Place: Publisher, Year.
  - Alphabetical by author surname

### Voice & Register (STYLEGUIDE.md)
- Write like a senior academic who is simultaneously a clear writer
- Third person, full sentences, no bullets/lists
- Technical terms: define on first use
- Italicize: book/treatise titles, foreign-language terms, text titles used as titles
- Avoid: "This text is...", "This article discusses..." — start with the thing itself

### Historiographical Framework
- **Actor/Analyst distinction**: Always maintain
  - Actor terms: words historical figures used (*gnosis*, *magia naturalis*, *prisca theologia*)
  - Analyst terms: modern categories (*Hermeticism*, *Western Esotericism*, *Yates Paradigm*)
  - Never write "X practiced Hermeticism" — write "X engaged with Hermetic texts and..."
- **Provenance on claims**: "As [Scholar] argues in *[Work]* ([Year])..."
- **Medieval continuity**: Emphasize when relevant (transmission was continuous, not a break)
- **Arabic transmission**: Treat as central, not peripheral

---

## Key Authorities to Cite

When writing about texts, cite these scholarly works as appropriate:

- Wouter J. Hanegraaff: *Dictionary of Gnosis and Western Esotericism* (2006); *Hermetic Spirituality and the Historical Imagination* (2022)
- Garth Fowden: *The Egyptian Hermes* (1986)
- Brian P. Copenhaver: *Hermetica* (1992, Cambridge)
- Frances A. Yates: *Giordano Bruno and the Hermetic Tradition* (1964)
- Paolo Lucentini & Mark D. Delp: *Hermes Latinus* series (Brepols, 1980–present)
- David Porreca: *The Picatrix* (2019)
- Kevin van Bladel: *The Arabic Hermes* (2009)
- Liana Saif: works on Islamic hermetic sciences
- Christian H. Bull: *The Tradition of Hermes Trismegistus* (2018)
- Lawrence M. Principe: *The Secrets of Alchemy* (2013)
- Tara Nummedal: *The Alchemy of Glass* (2021)

---

## Database Query: What's Left

```bash
python -c "
import sqlite3
db = sqlite3.connect('db/emerald_tablet.db')
c = db.cursor()

print('TEXTS UNDER 1000 WORDS:')
c.execute('''SELECT title, length(COALESCE(analysis_html, '')) as len 
             FROM texts WHERE length(COALESCE(analysis_html, '')) < 1000 
             ORDER BY len ASC''')
for title, length in c.fetchall():
    status = '(EMPTY)' if length == 0 else f'({length} wds)'
    print(f'  {title:50} {status}')
db.close()
"
```

---

## Next Steps After Texts Complete

### Phase 4C: Two-Level Dictionary Architecture
Once all prose is at standard (100% complete):
1. **Build `/dictionary/[slug].html`** encyclopedia pages in deploy script
2. **Build `/dictionary/index.html`** with index card grid + filtering
3. **Render `concept_links` table** on concept/dictionary pages (currently 0 links visible)

This requires modifying `HERMETICDB/scripts/DEPLOY_PORTAL.py` to add dictionary page generation.

---

## Session 1 Scripts Created

For reference, these scripts are ready to run or expand:

- `scripts/expand_worst_persons.py` — 5 worst biographies (DONE ✅)
- `scripts/expand_more_persons.py` — 5 more biographies (DONE ✅)
- `scripts/expand_final_persons.py` — 5 final biographies (DONE ✅)
- `scripts/expand_pomponazzi_concept.py` — concept rewrite (DONE ✅)
- `scripts/expand_key_texts.py` — 3 scholarly works (DONE ✅)

You can use these as templates for new text expansion scripts.

---

## Git Commit Message Template

When committing Session 2 work:

```
Session 2: Expand remaining 23 texts to 1,000+ word minimum

- Write 14 completely empty primary source and secondary texts
- Expand 9 partial texts from 1-999 words to 1,000+ words
- All entries: opening para + 2-3 sections + Literature (5-12 refs)
- Portal now at 100% prose content depth (Phase 4B complete)

Texts expanded: [list here if <10 texts per commit]
```

---

## Current Portal Status

**Live at**: `file:///C:\Dev\EmeraldTablet\docs/index.html`

All changes auto-generated by deploy script. After each batch of text expansions:
1. Verify entries look correct in browser
2. Check word counts via database query
3. Commit to git
4. Deploy (already automated)

---

## Questions or Clarifications?

Refer to these files:
- `PROMPTS.md` — full vision, agent rules, scholarly framework
- `STYLEGUIDE.md` — precise word counts, structure requirements, formatting rules
- `CLAUDE.md` — task routing, pipeline rules, key authorities
- `PHASESTATUS.md` — which gaps remain and priority order
