# Medieval Hermeticism Search Report

**Date:** 2026-03-25
**Scope:** Full-text search of PDF library (1,796 files) and ChatGPT/LLM chat archives across the computer
**Keywords:** hermetic, hermeticism, hermetica, hermes trismegistus, corpus hermeticum, asclepius, poimandres, pimander, emerald tablet, tabula smaragdina, debus, yates, copenhaver, fowden, hanegraaff, picatrix, ficino, prisca theologia, medieval hermetic, arabic hermetica, book of hermes, liber hermetis

---

## Tools Created

Two Python scripts were created in `C:\Dev\EmeraldTablet\`:

1. **`search_pdfs_hermeticism.py`** — Uses PyMuPDF (fitz) for fast full-text extraction from PDFs. Searches 1,796 PDFs across Desktop, Dev, Documents, and Downloads. Two-phase approach: filename matching then full-text search.
2. **`search_chats_hermeticism.py`** — Searches ChatGPT `conversations.json` export (774 conversations) and all HTML/MD/TXT chat files across the computer.

---

## Chat Search Results

### Source Locations

| Source | Location | Format | Count |
|--------|----------|--------|-------|
| ChatGPT main export | `C:\Users\PC\Desktop\GPT Data\conversations.json` | JSON (308 MB) | 774 total conversations |
| ChatGPT individual chats | `C:\Users\PC\Desktop\GPT Data\Individual Chats\` | HTML folders | 774 folders |
| ChatGPT rendered view | `C:\Users\PC\Desktop\GPT Data\chat.html` | HTML (312 MB) | Browsable |
| Recent chats (2025-2026) | `C:\Dev\GPTmarch172026\` | Markdown | Organized by date |
| Recent chats (mirror) | `C:\Dev\megabase\` | Markdown | Organized by date |
| LLM conversation logs | `C:\Users\PC\Downloads\LLM logs\` | HTML folders | Multiple subdirectories |

### Matching Conversations: 276 from conversations.json + additional MD/HTML files

All 276+ matching chats have been copied to **`C:\Dev\EmeraldTablet\HermeticChats\`** (980 files total across 4 subdirectories).

### HermeticChats Folder Structure

```
C:\Dev\EmeraldTablet\HermeticChats\
  GPT_Data\           — 206 individual chat folders (HTML) from Desktop\GPT Data
  GPTmarch2026\       — 178 markdown chats from C:\Dev\GPTmarch172026
  LLM_logs\           — 202 chat folders (HTML) from Downloads\LLM logs
  megabase\           — 270 markdown chats from C:\Dev\megabase
```

---

## Specifically Requested Chat: Merkel/Debus + Delp + De sex rerum principiis

The user recalled a recent chat about medieval hermeticism after converting Merkel/Debus and discussing Delp's edition of *De sex rerum principiis*.

### Found: February 2026 chat cluster

The specific chats are in `C:\Dev\GPTmarch172026\chats_2026\`:

| Date | File | Description |
|------|------|-------------|
| **2026-02-11** | `2026-02-11_Hermetism Volume Summary.md` | Uploaded Lucentini/Parri/Perrone Compagni, *Hermetism from Late Antiquity to Humanism* (Brepols, 2003, IPM 40) to ChatGPT for chapter summarization |
| **2026-02-12** | `2026-02-12_Hermetism in Antiquity to Humanism.md` | Continued discussion of the same volume — OCR'd text discussion including Delp, Porreca, Burnett, Lucentini, and other contributors. Full praefatio analysis. |
| **2026-02-12** | `2026-02-12_Book Review Summary.md` | Related book review discussion (Delp, Merkel, Debus present in text) |

#### About the Volume
*Hermetism from Late Antiquity to Humanism* (Instrumenta Patristica et Mediaevalia 40, Brepols 2003), edited by Paolo Lucentini, Ilaria Parri, and Vittoria Perrone Compagni. Proceedings of the 2001 Naples conference organized by the "Hermes Latinus" research group. Contributors include Mark Damien Delp, David Porreca, Charles Burnett, Moshe Idel, and many others. Four sections: I. Philosophical Hermetism, II. Philosophical Hermetism in the Middle Ages and Renaissance, III. Arabic and Hebrew Hermetism, IV. Operative Hermetism (astrology, magic, alchemy).

#### Also on disk
The OCR'd text of this volume is at: `C:\Users\PC\Downloads\Hermetism_OCR\hermetism_FULL.txt`

### Related October 2025 chats (also high-scoring)

| Date | File | Description |
|------|------|-------------|
| 2025-10-28 | `2025-10-28_Hermetic medieval to bruno.md` | BPH/Ritman newsletter discussion — Hermetic definition of God, Book of 24 Philosophers, medieval hermetic miscellanea |
| 2025-10-28 | `2025-10-28_Continue summary synthesis.md` | Continuation — Delp, Debus, Merkel, medieval hermetic all present |
| 2025-10-29 | `2025-10-29_Cutting edge in Pico studies.md` | Pico scholarship with medieval hermetic context |

---

## Top ChatGPT Conversations by Category

### Core Hermeticism & Hermetic Texts
- Hermeticism in Iamblichus Mysteries
- Hermetic Alchemy and Enoch (Bull's *Physica* of Hermes)
- Hermetic Spirituality Hanegraaff
- Hermetica Book Summary Request (Copenhaver's *Hermetica*)
- Hermetism Volume Summary (Lucentini et al.)
- Hermetism in Antiquity to Humanism
- Christian Bull's Hermeticism Contributions
- Studia Hermetica translations Phoenix (CCCM Asclepius)
- Custom GPT Summarization Tips (Corpus Hermeticum)
- Table Summary Request (Hermes Christianus — Moreschini)

### Medieval & Arabic Hermeticism
- Medieval Magic Summary Request (Sannino, "From Hermetic magic to magic of marvels")
- Burnett 12th Century Renaissance (Hugo of Santalla, translations)
- Alchemy quest for longevity (Arabic-Latin hermetic transmission)
- Al-Buni Gardiner (Picatrix, Yates paradigm)
- Magical Materials in Picatrix
- Burnett Runes (Sloane 3854, Arabic hermetic astral magic)
- Alchemy in Byzantium (Corpus Hermeticum, Gnostic/Hermetic ideas)

### Debus & Key Scholars
- alchemy scholarship atalanta doc (Debus's *Chemical Philosophy*, Yates)
- Alchemy Historiography Summary (Debus, Emerald Tablet)
- Alchemy Chemistry summary (Debus on Galenic vs hermetic thought)
- Fanger Ritual Magic (Yates, Picatrix)
- Critiques of Yates's Magic
- Frances Yates Renaissance Magic
- Esotericism Scholars Overview
- Hanegraaff articles Taves/Yates (medieval reception of Hermetism)

### Ficino & Renaissance Reception
- Plato Neoplatonism and Renaissance Magic
- Document Overview Summary (Copenhaver, Yates, Ficino)
- Alchemy Hiro Hirai Bodies Internal Powers (prisca theologia)
- Christian Platonism Overview (Ficino chapter)
- Table summary request (Ficino's Augustinianism + Hermetic traditions)

### Philip K. Dick & Hermeticism
- Philip K Dick Hermeticism (VALIS and Hermetic themes)
- Hermeticism and Philip K Dick (Paracelsus inner firmament)
- PKD Letters (Zoroastrian/Hermetic traditions)

### Game & App Design (Hermetic themes)
- Renaissance Magicians MTG Cards (Picatrix, Ficino)
- Roguelike Game Development Plan (Hermeticism, Ficino)
- Alchemical Puzzle Game Mechanics
- Renaissance Magic Board Game (Bruno, Hermetic philosophy)
- Book of Nature/Soul Game Feature Development

---

## PDF Library Results

### Filename Matches: 42 PDFs

#### Dedicated Hermetic Collection: `C:\Dev\EmeraldTablet\hermetic\`

| PDF | Author/Editor | Key Content |
|-----|--------------|-------------|
| Brian P Copenhaver Hermetica | Copenhaver | Greek Corpus Hermeticum + Latin Asclepius, new English translation |
| Christian H Bull The Tradition of Hermes Trismegistus | Bull | Egyptian priestly figure as teacher of Hellenized wisdom (Brill) |
| Claudio Moreschini Hermes Christianus | Moreschini | Intermingling of Hermetic piety and Christian thought (Brepols) |
| M David Litwa Hermetica II | Litwa | Stobaeus excerpts, papyrus fragments, ancient testimonies |
| Ingrid Merkel_ Allen G Debus... Hermeticism and the Renaissance | Merkel/Debus (eds.) | **THE Debus-edited volume** — Folger Institute, intellectual history and occult |
| Glenn Alexander Magee Hegel and the Hermetic Tradition | Magee | Cornell UP |
| Wouter J Hanegraaff... Lodovico Lazzarelli Hermetic Writings | Hanegraaff/Bouthoorn | ACMRS |
| Wouter J Hanegraaff... Hermes Explains | Hanegraaff/Forshaw/Pasi | 30 Questions about Western Esotericism (AUP) |
| Joscelyn Godwin... Hermetic Brotherhood of Luxor | Godwin et al. | Initiatic and Historical Documents |

#### Medieval Hermeticism specifically

| PDF | Key Content |
|-----|-------------|
| Porreca, "Hermes Philosophus: Ramón Martí's Singular Use" (*La corónica* 36.1) | Medieval reception of Hermes as philosophical authority |
| Speculum reviews of Lucentini/Delp ed. of *De sex rerum principiis* | Reviews of key medieval hermetic text edition |
| Corpus Christianorum Continuatio Mediaevalis 143 — Ps-Apuleus Asclepius | Critical edition of Latin Asclepius |
| Bull, "The Arabic Hermes" review (*Numen* 59.1) | van Bladel's book on Arabic Hermes |
| Bull, "Hermes Trismegistus: Special Issue" (*Gnosis* 3.1) | Special issue on Hermes Trismegistus |

#### Debus

| PDF | Location |
|-----|----------|
| Debus, Allen G - *The Chemical Philosophy* | `C:\Dev\EmeraldTablet\` |
| Merkel/Debus (eds.) - *Hermeticism and the Renaissance* | `C:\Dev\EmeraldTablet\hermetic\` |

#### Asclepius-related

| PDF | Location |
|-----|----------|
| Ps-Apuleus Asclepius (CCCM 143) | `hermetic\` |
| Ilaria Parri, *La via filosofica di Ermete: Studio sull'Asclepius* | `hermetic\` |
| Matteo Stefani, Ficino lettore dell'Asclepius | `hermetic\` |
| Jeffrey B Pettis, *The Sleeper's Dream: Asclepius Ritual* | `hermetic\` |

#### Ficino Collection: `C:\Dev\renaissance magic\Ficino\`

7 PDFs including Voss, Farndell, Kaske/Clark (*Three Books on Life*), Attrell/Bartlett/Porreca (*On the Christian Religion*), Allen, Howlett, Jones.

#### Other Renaissance Hermetic PDFs

| PDF | Location |
|-----|----------|
| Frances A Yates, *Giordano Bruno and the Hermetic Tradition* | `renaissance magic\` |
| Joscelyn Godwin, *Robert Fludd: Hermetic Philosopher* | `renaissance magic\Fludd\` |
| Copenhaver, "A Grand End for a Grand Narrative" (Lazzarelli, Renaissance Hermetica) | `renaissance magic\Copenhaver\` |
| Copenhaver review of *Hermetica* (*BJHS* 1993) | `renaissance magic\Copenhaver\` |
| Compagni, "Alchemy and Hermeticism: Dispersa Intentio" (Agrippa) | `EmeraldTablet\` |
| *Hermetis Trismegisti Phoenicum Aegyptior...* | `EmeraldTablet\` |
| *History and Translations of Emerald Tablet* (Bauer/Lindemann) | `EmeraldTablet\` |

### Full-Text Search (partial — interrupted after processing ~600 of 1,796 PDFs)

The full-text search was still running when stopped. The filename matches above represent the strongest results. To complete the full-text scan, run:

```bash
python C:\Dev\EmeraldTablet\search_pdfs_hermeticism.py 2>&1 | tee pdf_search_results.txt
```

---

## OCR Resources Found

An OCR'd version of the Lucentini/Parri/Perrone Compagni *Hermetism* volume exists at:
- `C:\Users\PC\Downloads\Hermetism_OCR\hermetism_FULL.txt`
- Chunked pages: `C:\Users\PC\Downloads\Hermetism_OCR\hermetism_pages_*.txt`

---

## Summary Statistics

| Category | Count |
|----------|-------|
| ChatGPT conversations matched (conversations.json) | 276 |
| Additional chat files matched (MD/HTML across computer) | 700+ |
| Total files copied to HermeticChats | 980 |
| PDFs with hermeticism keywords in filename | 42 |
| PDFs in dedicated `hermetic\` folder | 23 |
| Ficino PDFs | 14 |
| Total PDFs scanned/in progress | 1,796 |

---

## File Locations Quick Reference

| What | Where |
|------|-------|
| HermeticChats collection | `C:\Dev\EmeraldTablet\HermeticChats\` |
| PDF search script | `C:\Dev\EmeraldTablet\search_pdfs_hermeticism.py` |
| Chat search script | `C:\Dev\EmeraldTablet\search_chats_hermeticism.py` |
| Hermetic PDF collection | `C:\Dev\EmeraldTablet\hermetic\` |
| Ficino PDFs | `C:\Dev\renaissance magic\Ficino\` |
| Copenhaver articles | `C:\Dev\renaissance magic\Copenhaver\` |
| ChatGPT export (all) | `C:\Users\PC\Desktop\GPT Data\` |
| Recent chats (2025-2026) | `C:\Dev\GPTmarch172026\` |
| Hermetism OCR text | `C:\Users\PC\Downloads\Hermetism_OCR\` |
