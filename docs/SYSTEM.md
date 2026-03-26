# System Architecture

## Stack

| Layer | Technology |
|-------|-----------|
| Database | SQLite 3 (`db/emerald_tablet.db`) |
| Processing | Python 3.10+ (stdlib only: sqlite3, json, re, pathlib) |
| Frontend | Vanilla HTML/CSS/JS — no frameworks, no build tools |
| Deployment | GitHub Pages (static files from `site/`) |

## Data Flow: The Required Middle Layer

Corpus files are not yet the knowledge portal. Indexing and segmentation are first-class infrastructure that transforms raw text into anchored, linkable segments. The real engineering task is stable transformation, not more ingestion.

```
CORPUS FILES (.md, .txt in root, hermetic/, KeyHermeticChats/)
    ↓
STAGE 2: INDEX — scripts/index_corpus.py
    Register every document in corpus_documents table
    ↓
STAGE 3: SEGMENT — scripts/segment_texts.py
    Split documents into page/section-level corpus_segments
    ↓
STAGE 4: MARK — scripts/mark_target_sections.py
    Score segments by keyword density, detect section types
    ↓
STAGE 5: VALIDATE — scripts/validate.py
    Structural checks (FK, enums, orphans) before extraction
    ↓
STAGE 6: EXTRACT — scripts/extract_*.py
    Parse segments into entity tables (texts, persons, translations, etc.)
    ↓
STAGE 7-8: LINK + ASSEMBLE
    Build relationships, template analysis HTML
    ↓
STAGE 9: BUILD — scripts/build_site.py
    Generate static HTML from database
    ↓
STAGE 10: VALIDATE — scripts/validate.py
    Link checks, missing pages, broken references
    ↓
GitHub Pages
```

## The System Boundary

| Layer | What It Is | Source of Truth |
|-------|-----------|----------------|
| **Corpus** | Raw converted text files (.md, .txt) | Filesystem |
| **Index** | Document registry with metadata | `corpus_documents` table |
| **Segments** | Page/section-level text anchors | `corpus_segments` table |
| **Entities** | Texts, persons, concepts, translations, etc. | Entity tables (texts, persons, etc.) |
| **Site** | Static HTML pages | `site/` directory |

SQLite is the source of truth for everything below corpus files. The site is a read-only consumer of the database. LLM interpretation is downstream and bounded — it operates only on marked segments and writes only to `staging/`.

## Deterministic / LLM Boundary

- **Indexing** is deterministic (filesystem scan + file metadata)
- **Segmentation** is deterministic (markdown structure parsing)
- **Marking** is deterministic (keyword matching + regex patterns)
- **Validation** is deterministic (FK checks, enum matching)
- **Extraction** is mostly deterministic (regex parsing of known patterns)
- **LLM reading** is bounded: operates only on HIGH-relevance segments, writes to staging, validated before DB entry

## Provenance Model

Every datum carries three fields:

| Field | Values | Purpose |
|-------|--------|---------|
| `source_method` | SEED_DATA, DETERMINISTIC, CORPUS_EXTRACTION, LLM_ASSISTED, HUMAN_VERIFIED | How the data was produced |
| `review_status` | DRAFT → REVIEWED → VERIFIED | Promotion-only workflow |
| `confidence` | HIGH, MEDIUM, LOW | Certainty level |

## Directory Structure

```
EmeraldTablet/
├── CLAUDE.md              # Agent instructions (entry point)
├── PHASESTATUS.md         # Current phase + row counts
├── INFRASTRUCTURE_NEXT.md # Routing guide for next tasks
├── TAKEAWAYS1.md          # Lessons from prior projects
├── HERMETICSEARCH.md      # Corpus search report
├── data/                  # Curated JSON seed files
├── db/                    # SQLite database (gitignored)
├── docs/                  # System documentation
│   ├── SYSTEM.md          # This file
│   ├── ONTOLOGY.md        # Schema documentation
│   ├── PIPELINE.md        # Script execution order
│   ├── DECKARD_SECTION_MARKING.md  # Section marking heuristics
│   └── ONTOLOGY_REPORT.md # Expanded ontology analysis
├── scripts/               # Pipeline scripts
├── staging/               # Swarm/LLM output (validated before DB)
├── site/                  # Static output (deployed)
├── hermetic/              # Scholarly PDFs + converted markdown
├── KeyHermeticChats/      # Curated research chats (8 files)
└── HermeticChats/         # Full chat archive (~980 files)
```

## Design Principles

1. **Database is source of truth** — all site content generated from SQLite
2. **Scripts are idempotent** — safe to re-run at any time
3. **No external dependencies** — Python stdlib only
4. **Provenance on every row** — track how data was produced
5. **Infrastructure before enrichment** — index and segment before extracting
6. **Enrichment before UI** — populate entities before building pages
7. **No ad-hoc data** — everything enters through the pipeline or is fragile
8. **BUILT vs PLANNED** — all docs distinguish implemented from aspirational
9. **Validate twice** — structural checks after extraction, link checks after build
