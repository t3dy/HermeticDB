# HermeticDB Content Style Guide

**MANDATORY: All agents, scripts, and LLM sessions contributing content to this project MUST consult this file before writing any prose for the database. This guide governs `bio_html`, `analysis_html`, `definition_long`, and `description` fields.**

---

## The Core Standard: Encyclopedia Prose

Every entry in this portal — whether a biography, a text summary, a dictionary definition, or a timeline event — must read like a **scholarly encyclopedia article**. The model is the *Dictionary of Gnosis and Western Esotericism* (Hanegraaff, Brill, 2006) and the *Encyclopaedia Iranica*: authoritative, precise, readable, and completely free of typographic or markup artifacts.

### What "Encyclopedia Prose" Means

Write in full, flowing sentences that could be read aloud without confusion. Use the third person. Do not use bullet points, numbered lists, hashtags, markdown symbols, emoji, code formatting, or template placeholders. Every paragraph must contain substantive historical or scholarly content — no filler, no meta-commentary about the entry itself.

---

## Absolute Prohibitions

The following are **never acceptable** in any prose field (`bio_html`, `analysis_html`, `definition_long`, `description`):

- **Hashtags**: `#` in any context
- **Square brackets**: `[text]` or `[[text]]`
- **Curly braces**: `{placeholder}` or `{{field}}`
- **Asterisks for emphasis**: `*text*` or `**text**`
- **Markdown headers**: `## Heading` — use `<h2>` HTML instead
- **Bullet points or hyphens as list markers**: `- item` or `* item`
- **Emoji or Unicode symbols used decoratively**: 🜍 🜂 ☿
- **Parenthetical citations in raw bracket form**: `[citeturn0search3]`
- **Template artifact strings**: `entity["people", "Name", 0]`
- **"See also" stub lines** that contain no actual content
- **Placeholder text**: "To be added," "N/A," "TBD"

---

## Required HTML Structure for Prose Fields

All `bio_html` and `analysis_html` content must use valid HTML. The structure is:

```html
<p>Opening paragraph establishing the figure's identity, dates, nationality, and primary significance within the Hermetic tradition.</p>

<h2>Section Title</h2>
<p>Substantive content for this section. Titles of books, treatises, and foreign terms should be wrapped in <i>italics</i>. Key names and concepts may be wrapped in <b>bold</b> when first introduced.</p>

<h2>Another Section</h2>
<p>Continue with another focused aspect of the entry.</p>
```

A well-formed biography has **two to four `<h2>` sections**. A well-formed text analysis has **two to three `<h2>` sections**. Dictionary definitions may have **one to two `<h2>` sections**.

The `description` field (the short card preview) must be **plain text only** — no HTML tags whatsoever. It should be one to two complete sentences.

---

## Voice and Register

Write in the voice of a senior academic who is simultaneously a clear writer. Avoid jargon where a plain word suffices. When technical terms are necessary, define them within the prose on first use. The register is formal but not obscure.

**Do not** begin entries with "This text is..." or "This figure is..." — begin with the name, title, or period directly.

**Example of poor prose (prohibited):**
> "This article discusses the figure of Albertus Magnus. He was a medieval scholar. He wrote about alchemy. **Key contributions:** - Natural philosophy - Alchemy - Theology."

**Example of correct encyclopedia prose:**
> "Albertus Magnus (c. 1200–1280), the *Doctor Universalis*, was a German Dominican friar and bishop whose encyclopedic synthesis of Aristotelian natural philosophy with Christian theology made him the most learned scholar of the 13th century. His engagement with alchemy, astrology, and the occult sciences — while cautious and critical — provided essential ecclesiastical legitimacy for the development of these disciplines as serious intellectual pursuits in the Latin West."

---

## Historiographical Terminology

Following the methodology of Wouter J. Hanegraaff, all entries must maintain a strict awareness of the distinction between **Actor Terms** and **Analyst Terms**.

An **Actor Term** is a word or concept used by historical figures themselves (e.g., *prisca theologia*, *magia naturalis*, *gnosis*). When glossing or defining these, the entry should explain what the historical actors meant by the term.

An **Analyst Term** is a retrospective scholarly category imposed by modern historians (e.g., *Hermeticism*, *Western Esotericism*, *the Yates Paradigm*). When using these, the entry must signal that they are scholarly constructions, not the self-description of historical actors.

Entries must **never conflate** these two registers. Do not write "Ficino practiced Hermeticism" — write "Ficino engaged with the Hermetic texts and integrated their Neoplatonic cosmology with his Christian philosophy."

---

## Italics Policy

The following categories of text must always be rendered in `<i>` tags in HTML fields:

- Titles of books, treatises, and manuscripts: *Corpus Hermeticum*, *De Occulta Philosophia*, *Poimandres*
- Foreign-language technical terms on first use: *prisca theologia*, *gnosis*, *nous*, *spiritus*
- Names of texts when used as titles (not as concepts): "the *Asclepius*" vs. "the Asclepian tradition"

Do not italicize proper names of persons, places, or institutions.

---

## Persons Entries (bio_html)

**Length target**: 1,200–2,200 words total (excluding the Literature section).
**Bibliographic minimum**: 5–12 items in the Literature section.

Every person entry must contain:

**Opening paragraph** (200–350 words): Full name, dates (birth–death or fl.), nationality, primary role or profession, and a substantive sentence establishing their significance to Hermeticism or related fields. State immediately whether this is a historical actor or a modern scholar. Do not begin with "This figure was..." — begin with the name.

**At least two `<h2>` sections**, each 250–400 words:

*For historical figures* — use headers such as:
- `<h2>Works and Intellectual Context</h2>` — specific texts, their arguments, their sources
- `<h2>Hermetic Significance</h2>` — how and why this figure matters to the Hermetic tradition specifically
- `<h2>Transmission and Reception</h2>` — how were they read, translated, and interpreted in subsequent centuries?
- `<h2>Scholarly Debates</h2>` — what do modern historians disagree about regarding this figure?

*For modern scholars* — use headers such as:
- `<h2>Central Argument</h2>` — their single most distinctive thesis, stated precisely
- `<h2>Methodological Approach</h2>` — what theoretical framework do they employ? (historicism, phenomenology, discourse analysis, etc.)
- `<h2>Key Works</h2>` — name and describe their 2–4 most significant publications with dates
- `<h2>Scholarly Lineage and Disputes</h2>` — who influenced them? Who do they disagree with, and on what specific point?

**`<h2>Literature</h2>`**: 5–12 bibliographic entries. For historical figures, include both primary texts and key secondary scholarship. For scholars, include their own major publications plus 2–3 critical responses.

**Checklist before saving a bio_html entry:**
- [ ] Does the opening paragraph NOT begin with "This figure" or "This scholar"?
- [ ] Is the figure's `role_primary` status (historical actor vs. SCHOLAR) clear from the prose?
- [ ] Does the entry name at least 2 specific texts with dates?
- [ ] For scholars: are at least 2 intellectual disputes named with specific opponents?
- [ ] Is total prose (excluding Literature) between 1,200 and 2,200 words?
- [ ] Does Literature contain at least 5 items?

Figures must be categorized by era: `ANTIQUITY`, `MEDIEVAL`, `RENAISSANCE`, `EARLY_MODERN`, or `MODERN`. Use `SCHOLAR` in `role_primary` for modern academic historians only.

---

## Texts Entries (analysis_html)

**Length target**: 1,000–1,800 words total (excluding the Literature section).
**Bibliographic minimum**: 5–12 items in the Literature section.

Every text entry must contain:

**Opening paragraph** (200–300 words): Full title in `<i>` tags, date of composition or earliest attestation, original language, and a substantive sentence establishing the text's place in the Hermetic canon. Is it a primary source or secondary scholarship? State this immediately.

**`<h2>Content and Doctrine</h2>`** (300–500 words): What does the text actually argue, narrate, or prescribe? What are its key doctrines, cosmological claims, ritual instructions, or narrative events? Be specific — cite tractate numbers, chapter titles, key technical terms, or notable passages. Do not summarize vaguely.

**`<h2>Transmission and Manuscript Tradition</h2>`** (200–400 words, required for primary sources): How did this text survive? Through what manuscript traditions, translations, or intermediary languages? Who were the key transmitters? If a modern critical edition exists, name it and its editor.

**`<h2>Modern Scholarship</h2>`** (150–300 words, required for significant texts): Which scholars have produced the authoritative editions, translations, or interpretations? What are the current scholarly debates about this text's dating, authorship, or significance?

**`<h2>Literature</h2>`**: 5–12 bibliographic entries. Must include the authoritative modern edition or translation (if one exists) plus 3–5 key secondary studies.

**Checklist before saving an analysis_html entry:**
- [ ] Does the opening paragraph give the date, language, and canonical status of the text?
- [ ] Does Content and Doctrine name at least 2 specific tractates, chapters, or passages?
- [ ] For primary sources: does Transmission name the manuscript tradition and key translators?
- [ ] Is total prose (excluding Literature) between 1,000 and 1,800 words?
- [ ] Does Literature contain at least 5 items, including the authoritative edition?

---

## Dictionary Entries — Two Mandatory Levels

Dictionary entries cover **concepts** — both Actor Terms and Analyst Terms. The model for every entry is the *Dictionary of Gnosis and Western Esotericism* (Hanegraaff, Brill, 2006). **Two levels are required for every concept in the database.**

---

### Level 1 — Index Card (`definition_short` field)

The index card appears on the `/dictionary/` listing page. It is the entry's public face for quick browsing.

**Format**: Plain text only — no HTML tags, no italics markup, no lists.
**Length**: 60–120 words (2–4 sentences).

**Required content** (in order):
1. The term's original-language form if it has one, and whether it is an **Actor Term** (used by historical figures) or an **Analyst Term** (retrospective scholarly category).
2. Its earliest clear attestation or the tradition from which it originates.
3. One sentence on its principal scholarly significance or the debate it sits at the center of.

**Example — Actor Term:**
> *Prisca theologia* (Latin: "ancient theology") is an Actor Term denoting the Renaissance belief that a single, primordial divine wisdom underlay all ancient philosophical and religious traditions — from Zoroaster and Hermes Trismegistus through Plato and the Hebrew prophets. The concept was given its canonical formulation by Marsilio Ficino in the 1460s and shaped a century of Florentine Neoplatonic thought. Modern scholars, particularly D. P. Walker and Wouter Hanegraaff, have analyzed it as a projective theological strategy rather than a historical thesis.

**Example — Analyst Term:**
> *Hermeticism* is an Analyst Term — a retrospective scholarly category — denoting the tradition of texts and ideas attributed to Hermes Trismegistus, spanning from Late Antique Egyptian priestly circles through the Renaissance and into modernity. It was systematized as a scholarly field primarily by Frances Yates (1964) and subsequently redefined by Wouter Hanegraaff to emphasize historiographical rigor over essentialist continuity. The boundaries of what counts as "Hermetic" remain actively contested in current scholarship.

---

### Level 2 — Encyclopedia Page (`definition_long` field)

The encyclopedia page appears at `/dictionary/[slug].html`. It is the portal's primary scholarly contribution. **Every concept must eventually have a Level 2 entry. Stubs and placeholders are not acceptable.**

**Format**: Valid HTML with `<p>`, `<h2>`, and `<i>` tags. No markdown. No bullet lists. No template artifacts.
**Length**: 1,500–2,500 words of readable prose (not counting the Literature section).
**Bibliographic minimum**: 8–15 items in the Literature section.
**Hyperlink minimum**: At least 3 `<a href>` links to related entities within the portal.

**Required structure** (use these `<h2>` headers exactly):

```html
<p>[Opening paragraph: 150–250 words. State the term in its original language if applicable.
Declare whether it is an Actor Term or Analyst Term explicitly in prose.
Give the earliest clear attestation. Establish its significance in one or two sentences.
Do NOT begin with "This term..." or "This concept..." — begin with the term itself.]</p>

<h2>Historical Usage</h2>
<p>[400–600 words. Trace how the term was used across time — from its earliest appearance
through Late Antiquity, the medieval period, the Renaissance, and early modernity as relevant.
Name specific texts, authors, and dates. Be specific: cite passages, chapter titles, dates of
composition. Show evolution or change in meaning. Do not flatten across centuries.]</p>

<h2>Scholarly Significance</h2>
<p>[400–600 words. How have modern scholars analyzed, debated, or revised understanding of
this term? Name the scholars by name. State their specific arguments. If two scholars disagree,
state the disagreement explicitly — do not synthesize it into a bland middle ground.
Engage with the Yates Paradigm where relevant and note its revision.]</p>

<h2>Transmission and Variant Forms</h2>
<p>[200–400 words. OPTIONAL — include for terms with Arabic, Greek, Latin, or Hebrew variants,
or terms whose meaning shifted significantly in transmission. Skip this section for purely
modern Analyst Terms. Cover: original language form, translation history, significant
recensions or interpretive shifts across traditions.]</p>

<h2>Related Concepts</h2>
<p>[100–200 words of prose — NOT a bullet list. Link to 3–5 related entries using
<a href="../concepts/[slug].html">[Term]</a> tags. Write in full sentences that explain
the relationship, not just a list of names. Example: "The concept of <a href="../concepts/nous.html">
<i>Nous</i></a> is inseparable from <i>gnosis</i> in the philosophical Hermetica,
where knowledge of God is always mediated through the divine intellect."]</p>

<h2>Literature</h2>
<p>[8–15 entries in DGWE-style bibliography. Format each as a separate line (use <br> between
entries or list each in a new <p> tag). Format: Author Last, First. <i>Title of Work</i>.
Place: Publisher, Year. — or for articles: Author Last, First. "Article Title."
<i>Journal Name</i> Volume (Year): Pages.]</p>
```

**Checklist before saving a Level 2 entry:**
- [ ] Does the opening paragraph NOT begin with "This term" or "This concept"?
- [ ] Is the Actor/Analyst distinction declared explicitly in prose?
- [ ] Does Historical Usage name at least 3 specific primary texts with dates?
- [ ] Does Scholarly Significance name at least 2 specific scholars with their actual arguments?
- [ ] Is total word count between 1,500 and 2,500?
- [ ] Does the Literature section contain at least 8 items?
- [ ] Are there at least 3 internal `<a href>` links?
- [ ] Are all foreign terms in `<i>` tags?

---

## The Scholars Page: Era-Based Categorization

On the Scholars index page, modern academics must be grouped by their primary area of focus, not arbitrarily. The groupings are:

- **Antiquity and Late Antique Studies** — Fowden, Mahé, Copenhaver, Bull, Litwa, Van den Kerchove
- **Medieval and Arabic Hermetica** — Lucentini, Porreca, Delp, Attrell, Saif
- **Renaissance and Early Modern Studies** — Yates, Walker, Zambelli, Gilly, Forshaw
- **Modern Esotericism and Historiography** — Hanegraaff, Faivre, von Stuckrad, Versluis, Goodrick-Clarke
- **Kabbalistic and Related Studies** — Idel, Scholem

These groupings must be reflected in a `scholar_group` or equivalent classification in the `persons` table or in the deploy script.

---

## Timeline Events (description field)

**Length**: 100–250 words. **Format**: Plain text — no HTML tags.

Every timeline event must specify:
- **Exact date or date range**: Use CE/BCE notation. "c." for approximate dates.
- **Named actors**: At least one named person, text, or institution.
- **Geographic location**: City or region where possible.
- **Historiographical significance**: One sentence explaining why this event matters to the Hermetic tradition specifically — not just to general history.

Example:
> "c. 1460, Florence: Cosimo de' Medici instructs Marsilio Ficino to interrupt his translation of Plato and begin translating a recently acquired Greek manuscript of the Corpus Hermeticum instead, ultimately producing the Latin Pimander (completed 1463). This act of cultural priority — Hermes before Plato — reflects the Renaissance belief in the superior antiquity of Hermetic wisdom and inaugurates the tradition of Florentine Hermetic Neoplatonism. The decision has been analyzed by D.P. Walker and Frances Yates as a founding moment of Renaissance Hermeticism."

---

## Bibliography Format (Literature Sections)

All `<h2>Literature</h2>` sections in encyclopedia pages use the following format, modeled on the *Dictionary of Gnosis and Western Esotericism* (Brill, 2006):

**Monograph:**
> Fowden, Garth. *The Egyptian Hermes: A Historical Approach to the Late Pagan Mind*. Cambridge: Cambridge University Press, 1986.

**Edited volume:**
> Hanegraaff, Wouter J. (ed.). *Dictionary of Gnosis and Western Esotericism*. 2 vols. Leiden: Brill, 2006.

**Article in journal:**
> Copenhaver, Brian P. "Hermes Trismegistus, Proclus, and the Question of a Philosophy of Magic in the Renaissance." *Hermeticism and the Renaissance: Intellectual History and the Occult in Early Modern Europe*. Washington: Folger Shakespeare Library, 1988. 79–110.

**Chapter in edited volume:**
> Lucentini, Paolo. "L'ermetismo magico nel secolo XIII." In *Sic itur ad astra: Studien zur Geschichte der Mathematik und Naturwissenschaften*, edited by M. Folkerts and R. Lorch. Wiesbaden: Harrassowitz, 2000. 409–450.

**Rules:**
- Author surname first, followed by comma and first name
- Book titles in `<i>` tags (HTML) or italics in plain text contexts
- Full publication data: city, publisher, year
- For articles: full page range
- Do NOT use "ibid." — repeat citations in full
- List entries alphabetically by author surname within the Literature section

---

## Source Attribution

Every substantive claim in a prose entry must be traceable to a named source. Where a claim is drawn directly from a scholar's published work, the scholar's name and the work's title must appear naturally within the prose itself. Do not use footnote-style citation brackets — integrate citations organically: "As Garth Fowden argues in *The Egyptian Hermes* (1986)..." The Literature section at the end of each entry provides the formal bibliography.

---

## Checking Your Work

Before writing any new prose entry, ask:

1. Would this passage appear unedited in a peer-reviewed encyclopedia?
2. Does it contain any prohibited symbols or formatting artifacts?
3. Are all book titles and foreign terms properly italicized in HTML?
4. Is the Actor/Analyst term distinction declared explicitly in prose?
5. Are all claims grounded in a named source?
6. Does the entry meet the minimum word count for its type?
7. Does the Literature section contain the minimum number of bibliographic items?
8. Are there at least 3 internal hyperlinks to related portal entities?

If the answer to any of these is "no," revise before inserting into the database.

---

## Quick Reference: Minimum Specifications

| Content Type | Min Words | Max Words | Min Literature Items | Min Internal Links |
|---|---|---|---|---|
| Dictionary — Level 1 (index card) | 60 | 120 | — | — |
| Dictionary — Level 2 (encyclopedia) | 1,500 | 2,500 | 8 | 3 |
| Person biography (bio_html) | 1,200 | 2,200 | 5 | 3 |
| Text analysis (analysis_html) | 1,000 | 1,800 | 5 | 2 |
| Timeline event (description) | 100 | 250 | — | — |

*These are minimums. Longer, more detailed entries are always preferable for significant figures and texts. The DGWE entry for "Hermeticism" runs to approximately 8,000 words — that is the aspirational ceiling for the portal's most important entries.*

---

*This style guide is referenced in `CLAUDE.md` and `PROMPTS.md` and must be consulted at the start of any session that will produce or modify database prose content.*
