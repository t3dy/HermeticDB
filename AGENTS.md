# Codex Instructions — EmeraldTablet / HermeticDB

## MANDATORY FIRST STEPS (in order)

1. **Read `PROMPTS.md` in full.** This is the canonical record of the project vision, scholarly framework, agent operating rules, and vocabulary lock. Non-negotiable — it prevents redoing work and eliminates direction errors.

2. **Read `STYLEGUIDE.md` in full.** It governs all `bio_html`, `analysis_html`, `definition_long`, and `description` fields with precise word counts and required section structures. The minimum for dictionary encyclopedia pages is 1,500 words; for biographies, 1,200 words; for text analyses, 1,000 words. Stubs, bullets, hashtags, or placeholder text will corrupt the portal. The model is the *Dictionary of Gnosis and Western Esotericism*.

3. **You cannot run Bash.** All output must go to `staging/` as JSON files. The main session will validate and load into the database. See `PROMPTS.md` Part VI for the three agent types (Dictionary Encyclopedia Writer, Biography Enricher, Relational Auditor) and their exact input/output contracts.

---

## Project Mission

The HermeticDB is an authoritative scholarly reference portal for the history of Hermeticism — the textual tradition centered on the figure of Hermes Trismegistus from Late Antiquity through the modern period. It is not an esoteric or promotional site. It is a rigorous, provenance-aware digital edition structured for academic browsing, built to the historiographical standards of Wouter J. Hanegraaff and the *Dictionary of Gnosis and Western Esotericism* (Brill, 2006).

The portal has three constituencies: (1) scholars researching the Hermetic tradition, (2) students approaching the field for the first time, (3) serious independent researchers. All three deserve the same standard of accuracy and readability.

---

## Current Phase

**SCHOLARLY SYNTHESIS / ONGOING ENRICHMENT**

The infrastructure is built. The database is relational and populated. The static site deploys correctly. The current priority is:

1. Ensuring all significant scholars, figures, and texts are in the database with full encyclopedia-quality prose
2. Fixing any entries with style violations (artifacts, hashtags, stubs)
3. Strengthening the relational graph (person → text → concept links)
4. Expanding the timeline with granular event data

---

## Architecture

SQLite → Python pipeline → static HTML/CSS/JS → GitHub Pages. No frameworks, stdlib only.

- **Database**: `db/emerald_tablet.db`
- **Deploy script**: `HERMETICDB/scripts/DEPLOY_PORTAL.py` — single source of truth for site generation
- **Ingestion scripts**: `scripts/` — all data modifications go through idempotent Python scripts
- **Output**: `docs/` and `site/` (GitHub Pages serves `docs/`)

---

## Key Files

| Purpose | File |
|---------|------|
| **Style mandate** | `STYLEGUIDE.md` ← READ FIRST |
| Entry point | This file (`AGENTS.md`) |
| Phase status | `PHASESTATUS.md` |
| Data ontology | `docs/ONTOLOGY.md` |
| Architecture | `docs/SYSTEM.md` |
| Database | `db/emerald_tablet.db` |
| Deploy | `HERMETICDB/scripts/DEPLOY_PORTAL.py` |

---

## Data Ontology Summary

### Persons Table
All entries in `persons` cover either (a) historical/mythical figures who appear in the Hermetic tradition as actors, or (b) modern scholars who study that tradition. The `role_primary` field distinguishes them:

- **SCHOLAR** — modern academic historians and translators (Hanegraaff, Fowden, Copenhaver, Porreca, etc.)
- **PHILOSOPHER, ALCHEMIST, SAGE, TRANSLATOR, PRIEST, DEITY, PHYSICIAN, MATHEMATICIAN, POET** — historical figures

The `era` field uses: `ANTIQUITY`, `MEDIEVAL`, `RENAISSANCE`, `EARLY_MODERN`, `MODERN`.

Scholars are grouped on the website by their area of specialization, not merely by era:
- Antiquity and Late Antique Studies
- Medieval and Arabic Hermetica
- Renaissance and Early Modern Studies
- Modern Esotericism and Historiography
- Kabbalistic and Related Studies

### Texts Table
Primary texts (`text_type = PRIMARY_SOURCE`) vs. secondary scholarship (`text_type = SCHOLARSHIP`, `COMMENTARY`, `COMPILATION`) must be clearly separated throughout the site. The key types are:

- **PRIMARY_SOURCE** — original Hermetic texts (CH, Asclepius, Emerald Tablet, Picatrix, Liber XXIV)
- **TREATISE** — Renaissance and early modern philosophical works with Hermetic content
- **SCHOLARSHIP** — modern academic books and critical editions
- **MANIFESTO** — Rosicrucian and related programmatic texts
- **COMPILATION** — Anthologies, collected fragments

### Concepts Table
Two fundamental categories, maintained with `category_type`:
- **ACTOR_TERM** — used by historical figures (*prisca theologia*, *magia naturalis*, *gnosis*, *nous*)
- **ANALYST_TERM** — retrospective scholarly categories (*Hermeticism*, *Yates Paradigm*, *Rejected Knowledge*)

This distinction must NEVER be collapsed. It is central to the Hanegraaffian methodology underpinning the entire project.

---

## Historiographical Principles (Bake These In)

1. **No reification**: Do not treat "Hermeticism" as a bounded, coherent tradition with fixed members. Historical actors were embedded in complex, overlapping contexts.
2. **Actor/Analyst distinction**: Always maintained (see STYLEGUIDE.md and ONTOLOGY.md).
3. **Provenance on every claim**: All assertions traceable to a named source.
4. **Medieval continuity**: The Renaissance "rediscovery" was not a break — it built on a continuous 12th–13th century Latin Hermetic tradition (*Hermes Latinus*) centered on texts like *De sex rerum principiis*, *Liber XXIV Philosophorum*, and the Latin *Asclepius*.
5. **Arabic transmission**: The Islamic world was the primary vehicle of Hermetic survival from Late Antiquity. Abu Ma'shar, Jabir, al-Kindi, and the *Picatrix* tradition are not peripheral — they are central.
6. **The Yates Paradigm is contested**: Present Frances Yates's thesis (Hermeticism → Scientific Revolution) with appropriate historiographical context. The paradigm has been substantially revised by Hanegraaff, Copenhaver, and others.

---

## Pipeline Rules

1. **No ad-hoc data.** All data must be inserted via idempotent Python scripts in `scripts/`.
2. **Provenance on every row.** `source_method`, `review_status`, `confidence` required on all rows.
3. **Idempotent scripts.** All scripts use `INSERT OR IGNORE`. Safe to re-run.
4. **Slugs, not row IDs.** Never hardcode database row IDs.
5. **Validate after enrichment.** Run the deploy script after any ingestion to verify output.
6. **Style before deploy.** Check new prose against `STYLEGUIDE.md` before committing to DB.

---

## Key Scholarly Authorities (Reference These)

These are the primary scholarly authorities whose frameworks govern this portal:

| Scholar | Key Work | Relevance |
|---------|----------|-----------|
| Wouter J. Hanegraaff | *Dictionary of Gnosis and Western Esotericism* (2006); *Hermetic Spirituality and the Historical Imagination* (2022) | Methodological framework; Actor/Analyst distinction |
| Garth Fowden | *The Egyptian Hermes* (1986) | Late Antique Hermetic milieu; the "Way of Hermes" |
| Brian P. Copenhaver | *Hermetica* (1992, Cambridge) | Standard English translation of CH and Asclepius |
| Frances A. Yates | *Giordano Bruno and the Hermetic Tradition* (1964) | The Yates Paradigm (contested but foundational) |
| Paolo Lucentini & Mark D. Delp | *De sex rerum principiis* (Brepols, 2006) | Medieval Latin Hermetica |
| David Porreca | Hermes Latinus series; *Picatrix* translation (2019) | Medieval classroom reception of Hermes |
| Kevin van Bladel | *The Arabic Hermes* (2009) | Arabic transmission |
| Liana Saif | Arabic occult sciences | Islamic Hermetica and astral magic |
| Christian H. Bull | *The Tradition of Hermes Trismegistus* (2018) | Egyptian priestly origins |
| Anna van den Kerchove | *La voie d'Hermès* (2012) | Ritual practices in the Hermetica |
| M. David Litwa | *Hermetica II* (2018, Cambridge) | Stobaean fragments and papyri |

---

## Vocabulary Lock

All enum values are defined in `scripts/init_db.py` CHECK constraints. Do not invent new values for `era`, `text_type`, `category`, `category_type`, `role_primary`, or `source_method` without adding them to the schema first.

---

## Python Conventions

- Python stdlib only (sqlite3, json, re, pathlib)
- All scripts must be idempotent (`INSERT OR IGNORE`, `UPDATE OR IGNORE`)
- DB path: `c:\Dev\EmeraldTablet\db\emerald_tablet.db`
- Deploy command: `python c:\Dev\EmeraldTablet\HERMETICDB\scripts\DEPLOY_PORTAL.py`
