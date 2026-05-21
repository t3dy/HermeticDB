# HermeticDB — The Hermetic Knowledge Portal

![Status](https://img.shields.io/badge/Status-Active-brightgreen)

**Live site:** [https://t3dy.github.io/HermeticDB](https://t3dy.github.io/HermeticDB)

HermeticDB is a rigorously sourced, statically generated scholarly reference portal for the history of Hermeticism — the textual tradition centred on the figure of Hermes Trismegistus from Late Antiquity through the early modern period. It is built to the historiographical standards of Wouter J. Hanegraaff and the *Dictionary of Gnosis and Western Esotericism* (Brill, 2006).

---

## What's in the portal

| Section | Contents |
|---------|----------|
| **Biographies** | 90 historical figures and modern scholars with full encyclopedia-length entries |
| **Texts** | 84 primary sources and works of scholarship, each with transmission analysis |
| **Dictionary** | 77 concepts — actor terms (*prisca theologia*, *gnosis*) and analyst terms (*Hermeticism*, *Yates Paradigm*) — with full encyclopedia entries |
| **Interactive Map** | 28 Hermetic centres from Alexandria to Prague, with key figures, associated texts, and manuscript archive notes; alphabetical sidebar navigation and marker clustering |
| **Relationship Graph** | D3.js force-directed graph of persons, texts, and concepts with colour-coded edges, node search/highlight, and click-through navigation |
| **Timeline** | Era-filtered chronological view (Antiquity → Early Modern) with entity auto-links |
| **Global Search** | Full-text overlay (`/` shortcut) across all 275+ entities |

---

## Architecture

```
SQLite database (db/emerald_tablet.db)
        │
        ▼
Python deploy script (HERMETICDB/scripts/DEPLOY_PORTAL.py)
        │  stdlib only — no frameworks, no Node
        ▼
Static HTML/CSS/JS (docs/)
        │
        ▼
GitHub Pages → https://t3dy.github.io/HermeticDB
```

- **Database**: `db/emerald_tablet.db` — SQLite, single source of truth
- **Deploy**: `python HERMETICDB/scripts/DEPLOY_PORTAL.py` — regenerates `docs/` in full from the database
- **Ingestion scripts**: `scripts/` — all data added via idempotent `INSERT OR IGNORE` Python scripts
- **Output**: `docs/` served by GitHub Pages

No build step, no Node.js, no framework. The entire site is regenerated from the database on every deploy.

---

## Scholarly framework

The portal maintains the actor/analyst distinction central to Hanegraaff's methodology:

- **Actor terms** — concepts used by historical figures themselves (*prisca theologia*, *magia naturalis*, *gnosis*, *nous*)
- **Analyst terms** — retrospective scholarly categories (*Hermeticism*, *Rejected Knowledge*, *Yates Paradigm*)

These are never collapsed. All claims are traceable to named scholarly sources.

---

## Repository layout

| Path | Purpose |
|------|---------|
| `db/emerald_tablet.db` | SQLite database |
| `HERMETICDB/scripts/DEPLOY_PORTAL.py` | Site generator |
| `scripts/` | Data ingestion scripts |
| `docs/` | Generated site (GitHub Pages root) |
| `PROMPTS.md` | Canonical project vision and agent rules |
| `STYLEGUIDE.md` | Prose word counts and structure requirements |
| `CLAUDE.md` | Development instructions |
