# Deckard Boundary Analysis: Scripting to Find and Mark Sections for Targeted LLM Reading

## Problem

We have ~60 converted markdown files totaling thousands of pages. We need to identify sections worth targeted LLM reading (for entity extraction, concept elaboration, translation alignment, etc.) without wasting tokens reading tables of contents, bibliography pages, and front matter.

## DETERMINISTIC TASKS (Use Regex/Python, Not LLM)

### 1. Section Header Detection
**Method:** Regex on markdown `## Page N` headers + content patterns
**Patterns:**
```python
# Chapter/section headers in scholarly texts
r'(?i)^(chapter|part|section|book)\s+[IVXLCDM\d]+'
r'(?i)^(introduction|preface|foreword|conclusion|bibliography|index|appendix)'
r'(?i)^(table of contents|contents|abbreviations|acknowledgments)'
```
**Output:** `staging/section_map.json` — page ranges with section types (FRONT_MATTER, CHAPTER, BIBLIOGRAPHY, INDEX, APPENDIX)
**Confidence:** HIGH — section headers are structurally predictable

### 2. Language Detection per Page
**Method:** Character class analysis
```python
# Arabic: \u0600-\u06FF
# Greek: \u0370-\u03FF
# Latin diacritics: common in scholarly apparatus
arabic_ratio = len(re.findall(r'[\u0600-\u06FF]', text)) / max(len(text), 1)
greek_ratio = len(re.findall(r'[\u0370-\u03FF]', text)) / max(len(text), 1)
```
**Output:** Language tags per page (ENGLISH, ARABIC, GREEK, LATIN, MIXED, GERMAN, FRENCH, ITALIAN)
**Confidence:** HIGH for dominant language, MEDIUM for mixed pages

### 3. Keyword Density Scoring
**Method:** Count occurrences of domain-specific terms per page
```python
HERMETIC_KEYWORDS = {
    'primary': ['hermes', 'trismegistus', 'emerald tablet', 'tabula smaragdina',
                'corpus hermeticum', 'asclepius', 'poimandres', 'nous', 'logos'],
    'alchemical': ['transmutation', 'philosopher.s stone', 'mercury', 'sulphur',
                   'calcination', 'distillation', 'nigredo', 'albedo', 'rubedo'],
    'persons': ['ficino', 'bruno', 'agrippa', 'iamblichus', 'zosimos', 'jabir',
                'balinas', 'apollonius', 'hortulanus', 'khunrath', 'maier'],
    'concepts': ['macrocosm', 'microcosm', 'emanation', 'theurgy', 'gnosis',
                 'demiurge', 'pneuma', 'sympathy', 'talisman'],
}
score = sum(len(re.findall(kw, text, re.IGNORECASE)) for kw in all_keywords)
```
**Output:** Per-page relevance score. Pages scoring >5 are HIGH RELEVANCE; 2-5 MEDIUM; <2 LOW.
**Confidence:** HIGH — keyword matching is deterministic

### 4. Table of Contents Extraction
**Method:** Detect numbered lists with page references
```python
r'(?:chapter|part)?\s*[IVXLCDM\d]+[.\s]+[A-Z].*?\d{1,3}$'
```
**Output:** Structural outline of each book — chapter titles with page numbers
**Confidence:** MEDIUM — OCR can garble page numbers

### 5. Bibliography/Footnote Detection
**Method:** Pattern matching for citations
```python
# Footnote markers
r'^\d+\s+[A-Z]'  # numbered footnotes at page bottom
# Bibliography entries
r'^[A-Z][a-z]+,\s+[A-Z]'  # "Smith, J." style
r'\(\d{4}\)'  # year in parentheses
```
**Output:** Pages tagged as BIBLIOGRAPHY, FOOTNOTES, APPARATUS
**Confidence:** HIGH — bibliographic format is highly regular

### 6. Emerald Tablet Text Detection
**Method:** Match known phrases across all translations
```python
TABLET_PHRASES = [
    r'quod est (inferius|superius)',
    r'as above.*so below',
    r'father.*sun.*mother.*moon',
    r'wind.*womb',
    r'pater.*sol.*mater.*luna',
    r'tabula smaragdina',
    r'الأعلى.*الأسفل',  # Arabic
]
```
**Output:** Pages containing Emerald Tablet text or direct discussion
**Confidence:** HIGH — the text is distinctive and well-known

## PROBABILISTIC TASKS (LLM Appropriate — But Use Targeted Reading)

### 7. Scholarly Argument Extraction
**When:** After deterministic section marking identifies HIGH RELEVANCE pages
**Method:** Read 5-10 page chunks of high-scoring sections; extract:
- Thesis statements
- Named scholarly positions
- Evidence cited
- Counterarguments
**Why LLM:** Argument structure requires semantic understanding
**Token budget:** ~2K tokens per page × ~200 high-relevance pages = ~400K tokens (fits in session)

### 8. Concept Definition Extraction
**When:** Pages mentioning key concepts (nous, logos, emanation, theurgy, etc.)
**Method:** Read page + 1 page context; extract formal or informal definitions
**Why LLM:** Definitions are embedded in prose, not marked up
**Token budget:** ~50 concept pages × 2K = ~100K tokens

### 9. Person-Text Relationship Extraction
**When:** Pages mentioning known persons AND known texts together
**Method:** Read co-occurrence pages; extract relationship (author, translator, commentator, critic)
**Why LLM:** Relationship type requires understanding context ("Ficino translated" vs "Ficino criticized")
**Token budget:** ~100 co-occurrence pages × 1K = ~100K tokens

### 10. Translation Variant Detection
**When:** Pages containing Emerald Tablet phrases (from task 6)
**Method:** Read surrounding context; extract full translation with metadata
**Why LLM:** Verse boundaries require semantic judgment
**Token budget:** ~20 pages × 2K = ~40K tokens

## BOUNDARY VIOLATIONS TO AVOID

| Violation | Category | Recommendation |
|-----------|----------|----------------|
| Using LLM to detect section headers | WASTE | Use regex (task 1) |
| Using LLM to count keywords | WASTE | Use Python (task 3) |
| Using LLM to detect language | WASTE | Use Unicode ranges (task 2) |
| Using regex to extract scholarly arguments | RISK | LLM needed (task 7) |
| Reading entire 800-page books with LLM | WASTE | Score pages first, read only HIGH relevance |
| Feeding OCR gibberish to LLM | WASTE | Filter pages with <20% ASCII first |

## PIPELINE: Section Marking Script

```
scripts/mark_sections.py
  INPUT: All .md files in project
  OUTPUT: staging/section_markers.json

Structure:
{
  "filename.md": {
    "total_pages": 272,
    "language_primary": "ENGLISH",
    "sections": [
      {"page_start": 1, "page_end": 12, "type": "FRONT_MATTER", "relevance": "LOW"},
      {"page_start": 13, "page_end": 45, "type": "CHAPTER", "title": "Introduction", "relevance": "HIGH", "keyword_score": 12},
      ...
    ],
    "high_relevance_pages": [13, 14, 15, 27, 28, 45, 67, ...],
    "emerald_tablet_mentions": [45, 67, 89],
    "persons_mentioned": {"ficino": [23, 45], "iamblichus": [12, 13, 14]},
    "concepts_mentioned": {"nous": [15, 27], "emanation": [45, 67]}
  }
}
```

## EXECUTION ORDER

1. **mark_sections.py** (deterministic, ~2 min) → `staging/section_markers.json`
2. Review markers, identify top 200 high-relevance pages across corpus
3. **Targeted LLM reading** of high-relevance pages in batches of 10-20 pages
4. Extract entities, concepts, definitions, arguments → `staging/llm_extractions.json`
5. Validate extractions against schema CHECK constraints
6. Load validated data into database

## TOKEN BUDGET ESTIMATE

| Task | Pages | Tokens/page | Total |
|------|-------|-------------|-------|
| Scholarly arguments | ~200 | ~2K | ~400K |
| Concept definitions | ~50 | ~2K | ~100K |
| Person-text relationships | ~100 | ~1K | ~100K |
| Translation variants | ~20 | ~2K | ~40K |
| **Total** | **~370** | | **~640K** |

This fits comfortably within a single Claude Code session (1M context).
