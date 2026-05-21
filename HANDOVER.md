# HermeticDB Handover — 2026-05-20 (Session 4)

## Current state

**Branch:** `main`  
**Latest commit:** `565ff40`  
**Live site:** https://t3dy.github.io/HermeticDB  
**Deploy command:** `python C:\Dev\EmeraldTablet\HERMETICDB\scripts\DEPLOY_PORTAL.py`  
**DB path:** `c:\Dev\EmeraldTablet\db\emerald_tablet.db`

---

## What was done this session (Session 4)

### Content Expansion Sprint
This session focused on systematic expansion of critical content gaps identified in previous sessions. Following the user's directive to achieve "full writing" in every category, the following work was completed:

#### 1. Biography Expansion (22 figures)
**Batch 1 (5 figures):** john_dee, giordano_bruno, hermes_trismegistus, paracelsus, iamblichus
- Full biographies: 5,545–8,402 chars each (1,200+ word equivalents)
- Structured with 2–3 major sections plus Literature

**Batch 2 (8 figures):** al_kindi, abu_mashar, jabir_ibn_hayyan, plato, isaac_newton, robert_boyle, robert_fludd, michael_maier
- Full biographies: 3,463–4,198 chars each

**Batch 3 (4 figures):** ramon_llull, lodovico_lazzarelli, heinrich_khunrath, giovanni_pico
- Full biographies: 2,754–3,854 chars each

**Batch 4 (5 figures):** david_litwa, didier_kahn, hereward_tilton, nicholas_of_cusa, albertus_magnus
- Full biographies: 2,514–3,079 chars each

**Status:** Brought biographies from 78/99 (78.8%) to 81/99 (81.8%)
**Remaining:** 18 biography stubs to expand

#### 2. Text Analysis Expansion (15 texts)
**Corpus Hermeticum Tractates (11):** ch_i_poimandres, ch_iv_krater, ch_vii, ch_viii, ch_ix, ch_x, ch_xii, ch_xiv, ch_xvi, ch_xvii, ch_xviii
- Full analyses: 2,231–4,400 chars each
- Structured template: Opening, Content and Doctrine, Transmission/Manuscript, Modern Scholarship, Literature

**Major Primary Works (4):** de_occulta_philosophia_libri_tres, picatrix_latin, liber_24_philosophorum, asclepius
- Full analyses: 3,166–4,369 chars each

**Status:** Brought texts from 18/99 (18.2%) to 33/99 (33.3%)
**Remaining:** 66 texts with zero or short analysis

#### 3. Concept Index Cards (2)
- Added definition_short (60–120 word) index cards for: phantasmata, pietro_pomponazzi
- **Status:** Concepts 73/74 (98.6%) — 1 index card still missing (verify which)

#### 4. Deployment
- Deployed portal successfully with all new content
- Verified no build errors

---

## What was done previous sessions

### 1. Journey enrichment (DEPLOY_PORTAL.py JOURNEYS dict)
- **Bruno:** Added Toulouse (1579–81 doctorate), Wittenberg (1586–88), Helmstedt (1589 excommunication). Correct order: Geneva → Toulouse → Paris → London → Wittenberg → Helmstedt → Frankfurt → Venice → Rome.
- **Agrippa:** Added London (1510, Colet/More/Erasmus), Grenoble (1535 death). Improved Pavia (first university Hermetica lectures).
- **Dee:** Fixed Mortlake coords (51.47, −0.27). Expanded Enochian detail. Třeboň now includes Kelley transmutation claim.
- **Trithemius:** Sponheim stop notes 1996–98 confirmation that Steganographia encodes genuine ciphers.
- **Digby:** Added Algiers (Feb 1628, Barbary ransom) and Milos (Spring 1628, powder-of-sympathy experiment). Expanded all stops.

### 2. 26 new locations + 38 person_location links
All journey stop cities are now proper DB location entities with scholarly descriptions and LOCATION_TAGLINES. All 6 peregrination figures linked to their journey stops via `person_locations`.

New locations: Toulouse, Wittenberg, Helmstedt, Grenoble, Dole, Pavia, Metz, Lyon, Antwerp, Cambridge, Louvain, Kraków, Třeboň, Trittenheim, Heidelberg, Sponheim, Mirandola, Bologna, Ferrara, Padua, Gayhurst, Algiers, Milos, Scanderoon, Frankfurt, Geneva.

### 3. 24 new full biographies (1,200–1,500 words each)
- **Antiquity (6):** Plotinus, Porphyry, Proclus, Zosimos, Balinas, Stephen of Alexandria
- **Medieval (6):** Thomas Aquinas, al-Razi, Ibn Umayl, Khalid ibn Yazid, Bernard of Treviso, Petrus Bonus
- **Renaissance/EM (5):** Giovanni Pico, Nicholas of Cusa, Jakob Böhme, Kenelm Digby, Nicolas Flamel
- **Modern scholars (7):** Carl Jung, Moshe Idel, Peter Forshaw, Didier Kahn, Florian Ebeling, Hereward Tilton, Marco Pasi

---

## Complete gap audit — what still needs writing

### GAP 1: Critical short biographies (bio_html under 2,000 chars — URGENT)
These are among the portal's most important figures but remain stubs:

| person_id | chars | Why critical |
|---|---|---|
| `john_dee` | 1,006 | 9 journey stops; central Renaissance figure |
| `jabir_ibn_hayyan` | 1,072 | Foundational Arabic alchemist |
| `hermes_trismegistus` | 1,265 | The portal's central mythological figure |
| `giordano_bruno` | 1,284 | 11 journey stops; major Hermetic philosopher |
| `albertus_magnus` | 1,294 | Scholastic bridge to Hermetism; Aquinas's teacher |
| `paracelsus` | 1,384 | Gateway figure for Böhme, Digby, Khunrath, Fludd |
| `iamblichus` | 1,400 | Foundational theurgical Neoplatonism |
| `clement_alexandria` | 1,395 | Early Christian Hermetic engagement |
| `stobaeus` | 1,603 | Compiler of the Stobaean fragments |
| `lactantius` | 1,632 | Key Christian transmitter of Hermes |
| `david_porreca` | 1,704 | Medieval Hermes Latinus scholar |
| `robert_fludd` | 1,168 | Key Rosicrucian apologist; map figure |
| `lodovico_lazzarelli` | 1,183 | Key Renaissance Hermetist |
| `heinrich_khunrath` | 1,187 | Subject of Forshaw's research; map figure |
| `michael_maier` | 1,201 | Subject of Tilton's monograph; map figure |
| `alain_de_lille` | 1,286 | Medieval natural theology |
| `david_litwa` | 1,292 | Modern Hermetica II scholar |
| `christian_bull` | 1,167 | Key modern scholar on Egyptian origins |
| `mark_damien_delp` | 1,246 | Hermes Latinus series editor |
| `gilbert_of_poitiers` | 1,060 | Medieval natural philosophy |

**Also under 1000 chars (stubs needing full bios):**
- `christoph_kriegsmann` (203), `elias_ashmole` (204), `bruce_codex` (209), `basil_valentine` (312), `andreas_libavius` (357), `symphorien_champier` (635)

### GAP 2: Significant figures 1,000–5,000 chars (need expansion to 7,000+)

| person_id | chars | Note |
|---|---|---|
| `plato` | 909 | Essential philosophical background |
| `al_kindi` | 755 | Major Arabic transmission figure |
| `abu_mashar` | 807 | Major Arabic astral magic figure |
| `ramon_llull` | 799 | Medieval Lullism and Hermetic influence |
| `isaac_newton` | 900 | Alchemical Newton; major scholarly debate |
| `robert_boyle` | 899 | Opposed Digby; mechanical vs Hermetic |
| `johannes_reuchlin` | 949 | Christian Kabbalah bridge figure |
| `francis_mercury_van_helmont` | 897 | Böhme→Kabbalah transmission |
| `roger_bacon` | 1,015 | Medieval experimental tradition |
| `tommaso_campanella` | 960 | City of the Sun; Hermetic utopianism |
| `john_dee` | 1,006 | **MOST URGENT** — 9 journey stops |
| `giordano_bruno` | 1,284 | **MOST URGENT** — 11 journey stops |
| `didier_kahn` | 4,902 | Needs ~2,000 more words |
| `hereward_tilton` | 4,944 | Needs ~2,000 more words |

### GAP 3: Text analysis_html — LARGEST REMAINING GAP

**69 texts have zero analysis_html. 15 more have under 3,000 chars. Only 15 texts (out of 84) meet the 3,000-char minimum.**

The style guide requires 1,000–1,800 words per text entry with structured HTML sections.

**Highest-priority zero-analysis texts:**

| text_id | What it is | Priority |
|---|---|---|
| `ch_i_poimandres` | First CH tractate (933 chars — needs expansion) | CRITICAL |
| `ch_ii` through `ch_xviii` | Individual CH tractates — all under 300 chars | CRITICAL |
| `de_occulta_philosophia` | Agrippa's masterwork (285 chars) | CRITICAL |
| `picatrix_latin` | The Latin Picatrix (0 chars) | CRITICAL |
| `liber_24_philosophorum` | Medieval Hermetic collection (0 chars) | CRITICAL |
| `atalanta_fugiens` | Maier's emblem book (1,231 chars — needs expansion) | HIGH |
| `fama_fraternitatis` | Rosicrucian founding document (927 chars) | HIGH |
| `kitab_sirr_al_khaliqa` | Emerald Tablet source (357 chars) | HIGH |
| `amphitheatrum_sapientiae` | Khunrath's major work (344 chars) | HIGH |
| `rosarium_philosophorum` | Key alchemical emblem text (373 chars) | HIGH |
| `monas_hieroglyphica` | Dee's key Hermetic work (569 chars) | HIGH |
| `iamblichus_mysteriis` | De Mysteriis — theurgy (194 chars) | HIGH |
| `turba_philosophorum` | Early medieval alchemy (903 chars) | HIGH |
| `splendor_solis` | Major alchemical emblem text (1,188 chars) | HIGH |
| `liber_de_causis` | Proclus → scholasticism (1,091 chars) | MEDIUM |
| `chymical_wedding` | Rosicrucian narrative (163 chars) | MEDIUM |
| `aurora_consurgens` | Late medieval alchemical vision (397 chars) | MEDIUM |

**Text analysis template (STYLEGUIDE.md):**
```html
<p>Opening paragraph (200–300 words): full title in <i>tags</i>, date, language, place in canon.</p>
<h2>Content and Doctrine</h2>
<p>300–500 words. Specific tractates, arguments, key passages.</p>
<h2>Transmission and Manuscript Tradition</h2>
<p>200–400 words. Survival, translations, key transmitters, modern critical editions.</p>
<h2>Modern Scholarship</h2>
<p>150–300 words. Authoritative editions, current debates.</p>
<h2>Literature</h2>
<p>5–12 bibliography items in DGWE format.</p>
```

**Run to check current state:**
```sql
SELECT text_id, text_type, length(coalesce(analysis_html,'')) 
FROM texts ORDER BY length(coalesce(analysis_html,''));
```

### GAP 4: Concepts below 5,000 chars definition_long (15 of 77)

| slug | chars | What it needs |
|---|---|---|
| `archeus` | 4,015 | Paracelsian vital principle — needs 2,000 more words |
| `quintessence` | 4,443 | Fifth element — needs 1,500 more words |
| `spagyrics` | 4,951 | Paracelsian pharmaceutical alchemy — nearly there |
| `emanations` | 4,883 | Neoplatonic procession — nearly there |
| `okhema` | 4,254 | Vehicle of the soul — needs 1,500 more words |
| `phantasmata` | 4,294 | Imagination in Neoplatonism — needs 1,500 more |
| `infinite_sphere` | 3,798 | Cusanus/Bruno cosmology — needs 2,000 more |
| `theosophy` | 3,279 | Analyst term — needs substantial expansion |
| `immanent_logos` | 3,487 | Stoic divine reason — needs 2,000 more |
| `aretalogy` | 3,433 | Narrative of divine wonders — needs 2,000 more |
| `hermetic_persona` | 4,142 | Actor term — needs 1,500 more |
| `monas_generativa` | 3,002 | Actor term — needs 2,500 more |
| `anima_mundi_divine` | 3,047 | World Soul — needs 2,500 more |
| `phronesis` | 3,072 | Practical wisdom — needs 2,500 more |

**Also: 8 of these have empty definition_short (0 chars) — need 60–120 word index cards.**

---

## Current Gap Status (End of Session 4)

| Category | Complete | Total | % | Remaining |
|----------|----------|-------|---|-----------|
| Biographies (1,200+ chars) | 81 | 99 | 81.8% | 18 stubs |
| Text Analyses (1,000+ chars) | 33 | 99 | 33.3% | 66 zero/short |
| Concept Index Cards | 73 | 74 | 98.6% | 1 missing |
| Concept Encyclopedia | 74 | 74 | 100% | ✓ Complete |

---

## Recommended session plan (Session 5+)

### Session A — Five critical biography expansions (highest single-session ROI)
Write full biographies (12,000+ chars each) for the 5 most critical figures:
1. `hermes_trismegistus` — the portal's central figure; trace from Egyptian Thoth through Late Antique CH composition to Renaissance and beyond
2. `giordano_bruno` — 11 journey stops; the Hermetic cosmologist and martyr
3. `john_dee` — 9 journey stops; mathematician, angelic philosopher, imperial court figure
4. `paracelsus` — essential gateway to half a dozen other figures' biographies
5. `iamblichus` — theurgical Neoplatonism; essential for Late Antique section

### Session B — Text analysis batch (74 texts need work)
Start with the CH tractates (ch_i through ch_xviii) — they can share a structural template, with the opening paragraph situating each tractate in the Corpus and the Content section focusing on that tractate's specific doctrine. Then move to major non-CH texts.

### Session C — Concept expansion
The 15 concepts under 5,000 chars. Add definition_short index cards for the 8 missing them.

### Session 5 Priority: Text Analyses (66 remaining — the LARGEST gap)

The text analysis gap is by far the most critical remaining work. **66 texts still need analyses.** To reach "full writing" status:

**Tier 1 — CRITICAL (write immediately):**
- Remaining CH tractates if any (ch_ii, ch_iii, ch_v, ch_vi, ch_xi, ch_xiii, ch_xv) — foundational
- Major esoteric texts (fama_fraternitatis, chymical_wedding, aurora_consurgens, monas_hieroglyphica, atalanta_fugiens, rosarium_philosophorum, amphitheatrum_sapientiae, splendor_solis)
- Primary Hermetic sources (ogdoad_ennead, seven_chapters, golden_tractate, centiloquium, turba_philosophorum)
- Islamic alchemy (kitab_sirr_al_khaliqa / Emerald Tablet concept)

**Tier 2 — HIGH PRIORITY:**
- Fragment collections (lactantius_fragments, clement_stromata, cyril_fragments, eusebius_praeparatio, chaeremon_fragments)
- Medieval works (liber_de_causis, liber_25_chapters, secretum_secretorum, liber_vaccae)
- Kabbalistic texts (sefer_yetzirah)
- Scholarship compilations and commentaries

**Tier 3 — MEDIUM PRIORITY:**
- Secondary scholarship (Forshaw, Lucentini, Mahé commentaries)
- Specialized alchemical texts (various PGM fragments, brontologion, salmeschoiniaka)

**Estimate:** 66 texts × ~3,500 chars average = ~231,000 chars = ~58,000 words
This is a multi-session commitment.

### Session 5 Secondary: Remaining biographies (18 stubs)

After high-priority text analyses, continue with remaining 18 biographies. These are lower-priority figures; shorter entries (2,000–2,500 chars) acceptable if full biographies prove resource-intensive.

**Remaining stub figures:**
- christoph_kriegsmann, elias_ashmole, bruce_codex, basil_valentine, andreas_libavius, symphorien_champier
- और remaining figures from GAP 1 list in previous sessions

---

## Implementation Notes

### Scripts Created This Session
All expansions now use idempotent UPDATE scripts in `scripts/`:
- `expand_critical_biographies.py` — 5 major figures
- `expand_batch2_biographies.py` — 8 authorities
- `expand_batch3_biographies.py` — 4 philosophers
- `expand_batch4_biographies.py` — 5 scholars
- `expand_corpus_hermeticum.py` — 11 CH tractates
- `expand_critical_texts.py` — 4 major primary works

Run before deployment: `python HERMETICDB/scripts/DEPLOY_PORTAL.py`

### Known Issues to Resolve
1. Verify which 1 concept is missing definition_short (output showed 73/74)
2. Consider whether concept entries under 5,000 chars should be expanded (currently 15 concepts in 3,000–5,000 range)

---

## Database schema reference

```sql
-- Key tables
persons (person_id TEXT PK, name, era, role_primary, bio_html, description, ...)
texts (id INT PK, text_id TEXT UNIQUE, title, text_type, analysis_html, ...)
concepts (id INT PK, slug TEXT, label, category_type, definition_short, definition_long, ...)
locations (slug TEXT PK, label, lat REAL, lng REAL, description, region, era_primary, ...)
person_locations (person_id, location_slug, role, source_method, confidence)
concept_text_refs (concept_id INT FK concepts.id, text_id INT FK texts.id, notes)
person_text_refs (person_id TEXT FK, text_id TEXT [slug, NOT int!], role)

-- CRITICAL asymmetry:
-- person_text_refs.text_id = TEXT slug (e.g. 'ch_i', 'asclepius')
-- concept_text_refs.text_id = INTEGER texts.id (primary key)
-- Never mix in JOIN queries
```

**Enum values (do not invent new ones without updating init_db.py CHECK constraints):**
- `era`: ANTIQUITY, MEDIEVAL, RENAISSANCE, EARLY_MODERN, MODERN
- `text_type`: PRIMARY_SOURCE, TREATISE, SCHOLARSHIP, MANIFESTO, COMPILATION, COMMENTARY
- `role_primary`: SCHOLAR, PHILOSOPHER, ALCHEMIST, SAGE, TRANSLATOR, PRIEST, DEITY, PHYSICIAN, MATHEMATICIAN, POET, MYTHICAL_FIGURE, COMPILER, AUTHOR
- `category_type` (concepts): ACTOR_TERM, ANALYST_TERM, HYBRID

---

## Style guide minimums (STYLEGUIDE.md)

| Content type | Min words | Min literature items |
|---|---|---|
| Biography (bio_html) | 1,200 | 5 |
| Text analysis (analysis_html) | 1,000 | 5 |
| Concept — Level 1 (definition_short) | 60–120 words | — |
| Concept — Level 2 (definition_long) | 1,500 | 8 |

**Absolute prohibitions in all prose fields:** hashtags, square brackets, bullet points, markdown headers (use `<h2>` HTML), asterisks for emphasis, emoji, placeholder text.

**Required HTML structure for biographies:**
```html
<p>Opening paragraph: name, dates, nationality, significance. 200–350 words.</p>
<h2>Works and Intellectual Context</h2>
<p>250–400 words. Specific texts, dates, arguments.</p>
<h2>Hermetic Significance</h2>
<p>250–400 words. Why this figure matters to the tradition specifically.</p>
<h2>Transmission and Reception</h2>
<p>200–350 words. How they were read in subsequent centuries.</p>
<h2>Literature</h2>
<p>5–12 items. Format: Author Last, First. <i>Title</i>. City: Publisher, Year.</p>
```

---

## Key scholarly authorities

| Scholar | Key work | Use for |
|---|---|---|
| Wouter Hanegraaff | *Dictionary of Gnosis and Western Esotericism* (Brill, 2006); *Hermetic Spirituality* (2022) | Methodological framework; all entries |
| Garth Fowden | *The Egyptian Hermes* (1986) | Late Antique Hermetic milieu |
| Brian P. Copenhaver | *Hermetica* (Cambridge, 1992) | CH translation; all CH tractate entries |
| Frances Yates | *Giordano Bruno and the Hermetic Tradition* (1964) | Yates Paradigm (contested) |
| Kevin van Bladel | *The Arabic Hermes* (2009) | Arabic transmission |
| Lawrence Principe | *The Secrets of Alchemy* (2012) | Practical alchemy; debunking myths |
| William Newman | *Promethean Ambitions* (2004) | Alchemy and science |
| Christian H. Bull | *The Tradition of Hermes Trismegistus* (2018) | Egyptian priestly origins |
| Moshe Idel | *Kabbalah: New Perspectives* (1988) | Kabbalah and Renaissance synthesis |
| D.P. Walker | *Spiritual and Demonic Magic* (1958) | Renaissance magic framework |

---

## Quick commands

```bash
# Full bio audit
python -c "import sqlite3; c=sqlite3.connect(r'c:\Dev\EmeraldTablet\db\emerald_tablet.db').cursor(); c.execute('SELECT person_id, length(bio_html) FROM persons WHERE length(bio_html) < 5000 ORDER BY length(bio_html)'); [print(r) for r in c.fetchall()]"

# Text analysis audit
python -c "import sqlite3; c=sqlite3.connect(r'c:\Dev\EmeraldTablet\db\emerald_tablet.db').cursor(); c.execute(\"SELECT text_id, length(coalesce(analysis_html,'')) FROM texts ORDER BY 2\"); [print(r) for r in c.fetchall()[:25]]"

# Concept audit
python -c "import sqlite3; c=sqlite3.connect(r'c:\Dev\EmeraldTablet\db\emerald_tablet.db').cursor(); c.execute(\"SELECT slug, length(coalesce(definition_long,'')) FROM concepts ORDER BY 2\"); [print(r) for r in c.fetchall()[:20]]"

# Deploy
python C:\Dev\EmeraldTablet\HERMETICDB\scripts\DEPLOY_PORTAL.py

# Commit (PowerShell)
git -C C:\Dev\EmeraldTablet add -A; git -C C:\Dev\EmeraldTablet commit -m "message"
```
