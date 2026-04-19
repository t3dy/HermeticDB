# HermeticDB: The Zero-Loss Knowledge Portal

![Status](https://img.shields.io/badge/Status-Active-brightgreen)
**Live Site:** [https://t3dy.github.io/HermeticDB](https://t3dy.github.io/HermeticDB)

HermeticDB is a structured, deterministically-grounded repository and web portal for tracking Hermetic, Alchemical, and Neoplatonic textual transmission.

---

## 🏗️ The Zero-Loss Pipeline

Our primary data ingestion involves a multi-pass autonomous structure:

1. **Pre-Processing**: Parsing 70+ academic volumes into 10,000+ atomic segments.
2. **Open Discovery**: Swarm extraction identifies historical figures, manuscripts, and concepts mentioned in the scholarship.
3. **Fact Ingestion**: 7,003 atomic claims harvested with verbatim citations and provenance tooltips.
4. **Narrative Synthesis**: Woven into Wikipedia-style scholarly articles.

---

## 🌐 The Next.js Portal

The frontend is a modern **Next.js 15** application statically generated (SSG). It features:
- **Chronological Era Navigation** (Antiquity, Medieval, Renaissance)
- **Relational Browsing**: Bidi-links between scholars, concepts, and primary source texts.
- **Provenance Tooltips**: Instant verification of every claim back to the source document.

---

## 🛠️ Repository Organization

* `docs/` — Final static site export (served via GitHub Pages).
* `scripts/` — The deterministic python pipeline.
* `db/` — Target path for the `emerald_tablet.db` SQLite truth state.
* `data/` — Curated seed data and JSON concepts.
