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

Every person entry must contain:

1. **Opening paragraph**: Full name, dates, nationality, primary role or profession, and one sentence establishing their significance to Hermeticism or related fields.
2. **At least one `<h2>` section**: Covering their most important scholarly, philosophical, or historical contribution in substantive detail.
3. **Historiographical context** (where applicable): Where does this figure sit in the scholarly debates? Were they a primary actor, a translator, a transmitter, a modern historian?

Figures should be categorized by era in their `era` field: `ANTIQUITY`, `MEDIEVAL`, `RENAISSANCE`, `EARLY_MODERN`, or `MODERN`. The distinction between historical/mythical figures (e.g., Hermes Trismegistus, Zosimos) and modern scholars (e.g., Wouter Hanegraaff, Garth Fowden) must be clearly maintained by the `role_primary` field: use `SCHOLAR` for modern academic historians.

---

## Texts Entries (analysis_html)

Every text entry must contain:

1. **Opening paragraph**: Full title (in italics), date or date range, language, and a sentence establishing the text's place in the Hermetic canon.
2. **Content section**: What does the text actually argue or narrate? What are its key doctrines or narrative events? Be specific — cite chapter titles, key terms, or notable passages.
3. **Transmission section** (for ancient or medieval texts): How did the text survive? What were the major manuscript traditions, translations, or editions?
4. **Modern scholarship** (optional): Which scholars have produced the authoritative editions or interpretations?

---

## Dictionary Entries (definition_long)

Dictionary entries cover **concepts** — both Actor Terms and Analyst Terms. They must contain:

1. **Opening paragraph**: The term in its original language (if applicable), a clear definition, and its category (Actor Term or Analyst Term, clearly labeled in prose — not as a code field).
2. **One or two `<h2>` sections**: Historical usage and scholarly significance.

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

## Source Attribution

Every substantive claim in a prose entry must be traceable to a primary or secondary source that exists in the `texts` or `bibliography` tables. Where a claim is drawn directly from a scholar's published work, the scholar's name and the work's title must appear naturally within the prose itself. Do not use footnote-style citation brackets — integrate citations organically: "As Garth Fowden argues in *The Egyptian Hermes* (1986)..."

---

## Checking Your Work

Before writing any new prose entry, ask:

1. Would this passage appear unedited in a peer-reviewed encyclopedia?
2. Does it contain any prohibited symbols or formatting artifacts?
3. Are all book titles and foreign terms properly italicized in HTML?
4. Is the Actor/Analyst term distinction maintained?
5. Are all claims grounded in a named source?

If the answer to any of these is "no," revise before inserting into the database.

---

*This style guide is referenced in `CLAUDE.md` and must be consulted at the start of any session that will produce or modify database prose content.*
