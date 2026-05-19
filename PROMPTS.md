# HermeticDB: Canonical Vision and Prompts

**This file is the single document AI agents read before beginning any content or architecture work on HermeticDB. It compiles the user's expressed vision across all sessions, system files, and iteration history. It supersedes no other file — it synthesizes them.**

---

## Part I: Project Vision

HermeticDB is an authoritative scholarly reference portal for the history of Hermeticism — the textual tradition centered on the figure of Hermes Trismegistus from Late Antiquity through the modern period. It is not an esoteric or promotional site. It is a rigorous, provenance-aware digital edition structured for academic browsing, built to the historiographical standards of Wouter J. Hanegraaff and the *Dictionary of Gnosis and Western Esotericism* (Brill, 2006).

**The model for every entry in this portal is the DGWE itself:** the Brill *Dictionary of Gnosis and Western Esotericism*, edited by Wouter J. Hanegraaff (2006). Every dictionary entry should aspire to that standard — an opening paragraph that defines the term with precision, chronologically organized sections, a closing Literature section with full bibliographic references, and internal cross-references linking to related entries.

**What this portal is NOT:**
- A theosophical or New Age resource
- A promotional site for esoteric practice
- A Wikipedia mirror
- A collection of AI-generated summaries without scholarly grounding

**The tone is always:** critical, reportorial, provenance-aware. Disagreements between scholars are named explicitly. No bland syntheses.

---

## Part II: Three Constituencies

Every page must serve all three simultaneously:

1. **Scholars**: Need precision, historiographical nuance, named sources, bibliography, relational links to primary texts and secondary literature. They will tolerate no vagueness.

2. **Students**: Need accessible prose, definitions on first use of technical terms, clear chronological frameworks, and connections between concepts. They will be lost without scaffolding.

3. **Serious independent researchers**: Need depth, rabbit holes, relational browsing, and the ability to follow a thread from one concept to a text to a person to a related concept. They want the "delightful rabbit hole" experience — the sense that pulling one thread reveals a whole web.

**Design principle for constituency 3:** Every card must link outward. Every entity page must be a crossroads, not a dead end. The user should be able to start at *gnosis*, follow a link to the *Corpus Hermeticum*, from there to Marsilio Ficino, from Ficino to *prisca theologia*, from *prisca theologia* to Pico della Mirandola, and so on indefinitely. This is the site's primary value proposition for the interested layperson.

---

## Part III: Scholarly Framework (Hanegraaffian Principles)

The following principles are not stylistic preferences — they are the intellectual framework of the entire portal. Every agent working on this project must internalize them:

### 3.1 The Actor/Analyst Distinction (NEVER collapse this)

- **Actor Terms**: Words and concepts used by historical figures themselves. *Prisca theologia*, *magia naturalis*, *gnosis*, *nous*, *spiritus*, *theurgía*. When defining these, explain what the historical actors meant by the term, in their own context.
- **Analyst Terms**: Retrospective scholarly categories imposed by modern historians. *Hermeticism*, *Western Esotericism*, *the Yates Paradigm*, *Rejected Knowledge*, *Correspondences*. When using these, signal clearly that they are scholarly constructions, not historical self-descriptions.

**Forbidden formulation**: "Ficino practiced Hermeticism."
**Correct formulation**: "Ficino engaged with the Hermetic texts and integrated their Neoplatonic cosmology with his Christian philosophy."

### 3.2 No Reification

Do not treat "Hermeticism" as a bounded, coherent tradition with fixed membership. Historical actors were embedded in complex, overlapping contexts. The boundaries of "Hermeticism" are a scholarly construction and are actively debated. Present them as such.

### 3.3 Medieval Continuity

The Renaissance "rediscovery" of Hermeticism in 1463 (Ficino's translation of the *Corpus Hermeticum*) was NOT a break from the preceding period. It built on a continuous 12th–13th century Latin Hermetic tradition (*Hermes Latinus*) centered on texts like *De sex rerum principiis*, *Liber XXIV Philosophorum*, and the Latin *Asclepius*. This continuity must be articulated clearly in the relevant entries and never silently elided.

### 3.4 Arabic Transmission Is Central, Not Peripheral

The Islamic world was the primary vehicle of Hermetic survival from Late Antiquity. Abu Ma'shar, Jabir ibn Hayyan, al-Kindi, the Sabian community at Harran, and the *Picatrix* tradition are not footnotes or exotic additions — they are essential chapters in the Hermetic story. Entries on transmission must give them equal weight to the Latin and Greek traditions.

### 3.5 The Yates Paradigm Is Contested

Frances Yates's thesis — that Renaissance Hermeticism was a catalyst for the Scientific Revolution — was enormously influential (1964) but has been substantially revised. Hanegraaff, Copenhaver, and others have demonstrated that Yates overstated the causal link and misread the nature of Renaissance Hermeticism. Present the Yates Paradigm as contested. Name the critics.

### 3.6 Provenance on Every Claim

Every substantive assertion must be traceable to a named source. Integrate citations organically: "As Garth Fowden argues in *The Egyptian Hermes* (1986)..." Do not use footnote brackets — write citations into the prose. Every entry must end with a Literature section.

---

## Part IV: Content Standards (by Type)

The following are the **minimum** requirements for each content type. Read `STYLEGUIDE.md` for full specifications. Never write entries shorter than these targets.

### Dictionary Entry
**Two mandatory levels:**

**Level 1 — Index Card** (`definition_short` field):
- 60–120 words, 2–4 sentences
- Plain text only, no HTML
- Must state: term category (Actor Term or Analyst Term), earliest attestation or origin, one-line significance

**Level 2 — Encyclopedia Page** (`definition_long` field):
- 1,500–2,500 words of HTML prose
- Required sections: opening paragraph → Historical Usage → Scholarly Significance → (optional) Transmission and Variant Forms → Related Concepts → Literature
- Literature section: 8–15 bibliographic references, full author-date format
- At least 3 hyperlinks to related entities (persons, texts, or other concepts) via `<a href>` tags

### Person Biography (`bio_html` field)
- 1,200–2,200 words total
- Opening paragraph: 200–350 words
- 2–4 `<h2>` sections: 250–400 words each
- Literature section: 5–12 references

### Text Analysis (`analysis_html` field)
- 1,000–1,800 words total
- Opening paragraph: 200–300 words
- Sections: Content and Doctrine / Transmission and Manuscript Tradition / Modern Scholarship
- Literature section: 5–12 references

### Timeline Event (`description` field)
- 100–250 words, plain text
- Must specify: exact date or date range, named actors, geographic location, and one sentence of historiographical significance

---

## Part V: Architecture Principles

### 5.1 Two-Level Dictionary Architecture

The dictionary section has two levels that must both exist and cross-link:

**`/dictionary/` section** — The scholarly reference section:
- `/dictionary/index.html`: Alphabetical + category-filtered index of all concepts, showing Level 1 index cards
- `/dictionary/[slug].html`: Full encyclopedia pages with Level 2 content, bibliography, and relational links

**`/concepts/` section** — The relational browsing section:
- `/concepts/[slug].html`: Relational detail pages showing what texts mention this concept, what persons worked with it, and what related concepts connect to it
- Cross-links to the `/dictionary/[slug].html` page: "Read the full scholarly entry →"

### 5.2 Relational Browsing (No Dead Ends)

Every entity page — person, text, concept — must link to at least three other entities. The `concept_links` table is already populated but not currently rendered. This is the single most impactful gap to fix. Implement it.

**Relational links appear as:**
- Inline links within prose (wrap entity names in `<a href>` when first mentioned)
- A "Related Concepts" or "Related Figures" section at the bottom of each page
- Category-browsable lists (e.g., "More ACTOR_TERMs in the THEOLOGICAL category")

### 5.3 Pipeline Rules (From TAKEAWAYS1.md)
- All data enters via idempotent Python scripts in `scripts/`
- No hardcoded database row IDs — use slugs
- All agent output goes to `staging/` first, validated before DB insertion
- Background agents cannot run Bash — use the staging file pattern
- Clear stale HTML before regenerating pages
- Export `data.json` for JavaScript consumers (filtering, graph, timeline)

---

## Part VI: Agent Operating Rules

### 6.1 What Agents Can and Cannot Do

**Can do (no Bash needed):**
- Read existing markdown files provided by the main session
- Write JSON output to `staging/` directories
- Produce HTML content for database fields
- Audit and cross-reference provided entity lists

**Cannot do (require main session):**
- Run Python scripts (database writes)
- Run the deploy command
- Read files not explicitly handed to them

### 6.2 Three Standard Agent Types

**Agent Type A — Dictionary Encyclopedia Writer**
- Given: concept slug, label, category_type, existing definition_long, all concept_text_refs (pre-queried)
- Produces: `staging/dictionary/[slug].json` with `definition_short` + `definition_long`
- Constraints: must reach 1,500–2,500 words; must declare Actor/Analyst category explicitly; must cite ≥3 named scholars; must include a Literature section with ≥8 references; all entity names that exist in the portal must be wrapped in placeholder `[LINK:slug]` markup for the main session to convert to `<a href>` tags

**Agent Type B — Biography Enricher**
- Given: person slug, role, era, existing bio_html, all their text_refs (pre-queried), list of their relationships
- Produces: `staging/persons/[slug].json` with expanded `bio_html`
- Constraints: must reach 1,200–2,200 words; must name all significant works; must include a Literature section; must not conflate Actor and Analyst registers

**Agent Type C — Relational Auditor**
- Given: full entity list (persons, texts, concepts) as JSON — NO database access needed
- Produces: `staging/concept_links.json` with proposed cross-links between concepts
- Constraints: may only reference slugs that appear in the provided entity list; must explain the relationship type (RELATED, CONTRASTED, PART_OF, BROADER, NARROWER)

### 6.3 Vocabulary Lock

Agents must use only these enum values and no others:

```
era:           ANTIQUITY | MEDIEVAL | RENAISSANCE | EARLY_MODERN | MODERN
text_type:     PRIMARY_SOURCE | TREATISE | SCHOLARSHIP | MANIFESTO | COMPILATION | COMMENTARY
role_primary:  SCHOLAR | PHILOSOPHER | ALCHEMIST | SAGE | TRANSLATOR | PRIEST | DEITY | PHYSICIAN | MATHEMATICIAN | POET
category_type: ACTOR_TERM | ANALYST_TERM | HYBRID
review_status: DRAFT | REVIEWED | VERIFIED
confidence:    HIGH | MEDIUM | LOW
```

Any value not in these lists must be flagged for human review, not silently inserted.

---

## Part VII: Iteration History

The following is a compressed log of the project's development arc, derived from git commit history and session notes. It documents the scope of what has been built and the direction of travel.

**Founding phase** (commits: `f525980`, `aced357`):
- Initial deploy with 49 persons, 27 texts, 19 concepts, 69 timeline events
- Parallel translation viewer for the Emerald Tablet itself
- Core site structure (era pages, timeline, card layout)

**Expansion waves 1–4** (commits: `a70c26a` through `5ebd777`):
- Full *Corpus Hermeticum* tractates populated
- Late Antique figures: Zosimos, Iamblichus, Proclus, Pseudo-Dionysius, etc.
- Stobaean Fragments, Nag Hammadi Hermetica, Thoth
- Technical Hermetica: astrology, medicine, natural magic (*Liber Hermetis*, *Kyranides*)

**Medieval and Arabic expansion** (commits: `6c2204e` through `326e0b8`):
- Jabir ibn Hayyan, Ibn Umayl, *Picatrix*, *Secretum Secretorum*
- *Liber XXIV Philosophorum*, *De sex rerum principiis*
- Scholars: Lucentini, Porreca, Delp (medieval transmission)
- Abu Ma'shar, al-Kindi, Sabian tradition

**Renaissance and Early Modern** (commits: `5d82302`):
- Ficino, Pico, Agrippa, Bruno, Dee, Maier, Casaubon
- Rosicrucian materials, *Chymische Hochzeit*
- Modern scholars: Mead, G.R.S. Mead era

**Dictionary expansion** (commit: `f055324`):
- 50+ dictionary terms added
- Primary/secondary source separation implemented
- Prose sanitization pass

**Interactive features** (commits: `e7e608c`, `ab6f141`):
- D3.js relationship graph
- Leaflet.js geography map

**Ongoing enrichment** (commits: `7dd766f` through `430211e`):
- Lazzarelli, Pomponazzi profiles
- Hanegraaff 2022 ingestion
- Delp/Porreca medieval scholarship
- Portal deployment fixes

**Current state (as of 2026-05-17)**:
- 84 texts, 90 persons, 74 concepts, 34 timeline events in DB
- Key gap: encyclopedia-length entries missing; concept_links not rendered; definition_short mostly empty; no bibliography sections anywhere

**Next phase**: Dictionary Architecture (two-level), content depth (DGWE-standard entries), relational browsing implementation.

---

## Part VIII: Key Sources on This Computer

The following scholarly works are available as files and should be consulted when writing entries:

| File | Relevance |
|------|-----------|
| `C:\Users\PC\Downloads\Wouter J. Hanegraaff (editor) - Dictionary of Gnosis & Western Esotericism (2006, Brill Academic Publishers) - libgen.li.pdf` | **Primary model** for all entry format and scholarly standards |
| `C:\Users\PC\Downloads\Wouter J. Hanegraaff - Hermetic Spirituality and the Historical Imagination (2022).pdf` | Methodological framework; updated historiography |
| `C:\Users\PC\Downloads\[Mythos] Garth Fowden - The Egyptian Hermes (1993).pdf` | Late Antique Hermetic milieu |
| `C:\Dev\EmeraldTablet\artifacts\Hanegraaff_Hermetic_Spirituality.md` | Pre-ingested Hanegraaff 2022 content |
| `C:\Dev\EmeraldTablet\hermetic\Scholarship_Maier_Report.md` | Maier scholarship |
