# Emerald Tablet Translation Sources Report

## Overview

The parallel translation viewer at `translations/emerald-tablet.html` contains **13 translations** with **190 verse entries** across 18 verse positions (0-14, with sub-verses 6a, 7a, 11a). This document records the provenance of every translation.

## Source Documents

All verse-level text was extracted from two sources:

### Source 1: History and Translations of Emerald Tablet (Bauer & Lindemann)

**File:** `History and Translations of Emerald Tablet{TEAM LAXiTY (Bauer Lindemann)}{113357991} libgen.li.pdf`
**Converted to:** `History_and_Translations_of_Emerald_Tablet.md`
**Description:** A compilation of different translations of the Emerald Tablet with verse numbering for comparison, assembled by a group including Jon Marshall, published by TEAM LAXiTY (Bauer & Lindemann). The document provides the verse-numbering scheme (0-14 with sub-verses) used as the canonical alignment key throughout this project.

**11 translations extracted from this source** via `scripts/extract_translations.py` using deterministic regex parsing of verse-numbered lines.

### Source 2: EmeraldTabletGPTandGemini.txt (Research Notes)

**File:** `EmeraldTabletGPTandGemini.txt`
**Description:** Research notes from GPT and Gemini conversations analyzing Ursula Weisser's critical edition of the Kitab Sirr al-Khaliqa. Contains transcriptions of the Arabic and Latin vulgate texts provided by GPT-4o based on its training data (not directly from the Weisser PDF).

**2 translations entered from this source** as seed data in `data/emerald_tablet_seed.json`.

---

## Translation-by-Translation Provenance

### ARABIC TRANSLATIONS

#### 1. Arabic (Sirr al-Khaliqa tradition)
- **ID:** `arabic_sirr_al_khaliqa`
- **Verses:** 14
- **Source method:** SEED_DATA (manually entered in `data/emerald_tablet_seed.json`)
- **Ultimate source:** GPT-4o transcription of the standard Arabic form associated with the Balinas tradition, as discussed in Weisser's critical edition. GPT stated this represents the tradition "as represented in this volume" (Weisser 1979) but acknowledged it is "normalized, not line-by-line diplomatic from a specific manuscript."
- **Caveat:** This is a normalized composite, not a diplomatic transcription from any single manuscript. Weisser's edition documents variants across ~17 manuscripts.
- **Tradition:** Sirr al-Khaliqa (Book of the Secret of Creation)

#### 2. Jabirian Arabic Version
- **ID:** `jabir_arabic`
- **Verses:** 10
- **Source method:** CORPUS_EXTRACTION from Bauer & Lindemann
- **Citation in source:** Holmyard 1923: 562
- **Ultimate source:** Eric Holmyard, "The Emerald Table," *Nature* 112 (1923). Holmyard found this version in the *Kitab Ustuqus al-Uss al-Thani* (Second Book of the Elements of Foundation) attributed to Jabir ibn Hayyan.
- **Note:** This is an English translation of the Arabic, not the Arabic original. Shorter than other versions (10 verses, missing several middle sections).
- **Tradition:** Jabirian corpus

#### 3. Anonymous Arabic Version (Ruska)
- **ID:** `ruska_anonymous_arabic`
- **Verses:** 17
- **Source method:** CORPUS_EXTRACTION from Bauer & Lindemann
- **Citation in source:** Anon 1985: 24-25
- **Ultimate source:** From Julius Ruska's German translation, re-translated into English by an anonymous translator. Ruska found this 12th-century recension claiming to have been dictated by Sagijus (Sergius) of Nablus. Includes the frame narrative of Balinas entering the hidden chamber.
- **Note:** Double translation (Arabic → German by Ruska → English by Anonymous). The frame narrative (verse 0) is included.
- **Tradition:** Sirr al-Khaliqa (12th-century recension)

---

### LATIN TRANSLATIONS

#### 4. Latin Vulgate
- **ID:** `latin_vulgate`
- **Verses:** 15
- **Source method:** SEED_DATA (manually entered in `data/emerald_tablet_seed.json`)
- **Ultimate source:** GPT-4o reproduction of the standard medieval vulgate Latin text. GPT stated this "matches the vulgate Latin version beginning 'Verum sine mendacio, certum, certissimum...' the form printed by Robert Steele and Dorothea Waley Singer in their 1928 study *The Emerald Table*."
- **Caveat:** GPT acknowledged this is from its training data, not transcribed from a specific manuscript or edition. It represents "the most famous later Latin recension, not 'the Latin text in Weisser,' and not necessarily the Latin text closest to the Arabic recension."
- **Scholarly reference:** Steele, Robert, and Dorothea Waley Singer, "The Emerald Table," *Proceedings of the Royal Society of Medicine* 21 (1928): 485-501.
- **Attribution:** Likely translated by Plato of Tivoli (c. 1134-1145) in Barcelona. Attribution conjectural.
- **Tradition:** Vulgate

#### 5. Twelfth Century Latin
- **ID:** `twelfth_century_latin`
- **Verses:** 17
- **Source method:** CORPUS_EXTRACTION from Bauer & Lindemann
- **Citation in source:** "From Latin in Steele and Singer 1928: 492"
- **Ultimate source:** Steele and Singer (1928), who printed this from medieval Latin manuscripts. The Bauer & Lindemann compilation presents it in English translation.
- **Note:** Despite the label "Twelfth Century Latin," the text as printed in the Bauer & Lindemann compilation is in **English** (a translation from the Latin). The original Latin text would be in Steele & Singer's 1928 article. Includes verse 0 (frame narrative).
- **Tradition:** Vulgate

#### 6. Translation of Beato
- **ID:** `beato_latin`
- **Verses:** 15
- **Source method:** CORPUS_EXTRACTION from Bauer & Lindemann
- **Citation in source:** Davis 1926: 874
- **Ultimate source:** Tenney L. Davis, "The Emerald Tablet of Hermes Trismegistus: Three Latin Versions Which Were Current Among Later Alchemists," *Journal of Chemical Education* 3 (1926): 863-875. From *Aurelium Occultae Philosophorum... Georgio Beato*.
- **Note:** Presented in English translation. No verse 0 (frame narrative).
- **Tradition:** Independent Latin tradition

#### 7. Hugo of Santalla Latin
- **ID:** `hugo_latin`
- **Verses:** 0 (not yet populated)
- **Source method:** N/A — translation record exists but no verse data extracted
- **Scholarly reference:** Françoise Hudry, "Le De secretis nature du ps.-Apollonius de Tyane, traduction latine par Hugues de Santalla du Kitâb sirr al-halîqa," *Chrysopoeia* 6 (1997-1999): 1-154.
- **Note:** Hugo's version is a different Latin text beginning "Superiora de inferioribus, inferiora de superioribus." It preserves the Arabic "from" relation rather than the vulgate's "is like." Not included in the Bauer & Lindemann compilation. Would need to be sourced from Hudry's edition.
- **Tradition:** Hugo of Santalla (De secretis naturae)

#### 8. Secretum Secretorum Latin
- **ID:** `secretum_secretorum_latin`
- **Verses:** 0 (not yet populated)
- **Source method:** N/A — translation record exists but no verse data extracted
- **Note:** Philip of Tripoli's translation within the Secretum Secretorum (c. 1243). Not included in the Bauer & Lindemann compilation.
- **Tradition:** Secretum Secretorum

---

### ENGLISH TRANSLATIONS

#### 9. Newton's English Translation
- **ID:** `newton_english`
- **Verses:** 15
- **Source method:** CORPUS_EXTRACTION from Bauer & Lindemann
- **Citation in source:** Dobbs 1988: 183-184
- **Ultimate source:** Betty Jo Teeter Dobbs, *The Foundations of Newton's Alchemy* (Cambridge, 1988). Newton's autograph translation survives in Keynes MS 28, King's College Library, Cambridge. Translated c. 1680 from the Latin vulgate.
- **Key feature:** Newton replaced the unintelligible Latin "telesmi" with "perfection" — a substitution that reflected his own alchemical theology rather than the Arabic original (abu al-tilasmat, "father of talismans").
- **Tradition:** Vulgate (English from Latin)

#### 10. Bacstrom's English Translation
- **ID:** `bacstrom_english`
- **Verses:** 17
- **Source method:** CORPUS_EXTRACTION from Bauer & Lindemann
- **Citation in source:** "See Hall 1977: CLVIII" (Manly P. Hall, *The Secret Teachings of All Ages*, 1928/1977)
- **Ultimate source:** Sigismond Bacstrom (late 18th century), allegedly translated from "Chaldean." Bacstrom was a Rosicrucian and alchemist.
- **Note:** The claim of Chaldean origin is pseudepigraphical. The text follows the Latin vulgate tradition with Rosicrucian embellishments (e.g., "CHIRAM ONE in essence, but three in aspect").
- **Tradition:** Independent (Rosicrucian)

#### 11. Blavatsky's Translation
- **ID:** `blavatsky_english`
- **Verses:** 9 (incomplete — missing verses 0, 1, 5, 8, 12, 13, 14)
- **Source method:** CORPUS_EXTRACTION from Bauer & Lindemann
- **Citation in source:** Blavatsky 1972: 507 (reprint of *Isis Unveiled* or *Secret Doctrine*)
- **Ultimate source:** H. P. Blavatsky, likely from *Isis Unveiled* (1877) or *The Secret Doctrine* (1888). Partial rendering only.
- **Tradition:** Independent (Theosophical)

#### 12. Idries Shah Translation
- **ID:** `idries_shah_english`
- **Verses:** 14
- **Source method:** CORPUS_EXTRACTION from Bauer & Lindemann
- **Citation in source:** Shah 1964: 198
- **Ultimate source:** Idries Shah, *The Sufis* (London: W.H. Allen, 1964). Shah presents the Tablet within a Sufi interpretive framework.
- **Note:** Some verse numbering differs slightly from other versions. Missing verse 2 and 9 as separate entries (content merged into adjacent verses).
- **Tradition:** Independent (Sufi)

---

### FRENCH TRANSLATIONS

#### 13. Fulcanelli Translation (version 1)
- **ID:** `fulcanelli_french_1`
- **Verses:** 16
- **Source method:** CORPUS_EXTRACTION from Bauer & Lindemann
- **Citation in source:** Sadoul 1972: 25-26
- **Ultimate source:** Fulcanelli, as quoted in Jacques Sadoul, *Alchemists and Gold* (London, 1972). English translation by Sieveking. Fulcanelli was the pseudonymous author of *Le Mystère des Cathédrales* (1926) and *Les Demeures Philosophales* (1930).
- **Note:** This is an English translation of Fulcanelli's French rendering.
- **Tradition:** Independent (French alchemical)

#### 14. Fulcanelli Translation (version 2)
- **ID:** `fulcanelli_french_2`
- **Verses:** 15
- **Source method:** CORPUS_EXTRACTION from Bauer & Lindemann
- **Citation in source:** "Translated from Fulcanelli 1964: 312"
- **Ultimate source:** Fulcanelli, *Les Demeures Philosophales* (Paris, 1964 edition): 312. A new English translation (different from the Sieveking version above).
- **Note:** Uses "Theleme" instead of "telesmi" in verse 6 — a distinct textual tradition.
- **Tradition:** Independent (French alchemical)

---

### OTHER

#### 15. Kriegsmann Translation (Phoenician)
- **ID:** `kriegsmann_translation`
- **Verses:** 16
- **Source method:** CORPUS_EXTRACTION from Bauer & Lindemann
- **Citation in source:** Davis 1926: 875, "slightly modified"
- **Ultimate source:** Wilhelm Christoph Kriegsmann (1657), who claimed to have recovered the original Phoenician text. Modern scholarship considers this a fabrication — Kriegsmann constructed a pseudo-Phoenician version to support his theory of Phoenician origins for Hermetic wisdom.
- **Note:** Despite its spurious origins, this version is historically significant as evidence of 17th-century antiquarian interest in the Tablet's pre-Arabic origins.
- **Tradition:** Independent (speculative reconstruction)

---

## Translations NOT YET in the Database

| Translation | Source Needed | Status |
|------------|--------------|--------|
| Hugo of Santalla Latin | Hudry, *Chrysopoeia* 6 (1997-1999) | Record exists, 0 verses |
| Secretum Secretorum Latin | Manzalaoui (1977) or manuscript | Record exists, 0 verses |
| Hypothetical Chinese Original | Needham 1980: 371 | Not entered (speculative) |
| Hortulanus Commentary (verse-by-verse) | Direct from Hortulanus text | Not entered |
| Arabic (diplomatic from Weisser Rec. A) | Weisser 1979 critical edition | Not entered |
| Arabic (diplomatic from Weisser Rec. B) | Weisser 1979 critical edition | Not entered |

## Key Caveats

1. **The Arabic text is a GPT composite, not a diplomatic transcription.** The arabic_sirr_al_khaliqa entry was generated by GPT-4o from its training data, representing a normalized version of the tradition. It does not correspond to any single manuscript witness. A proper critical edition would require diplomatic transcriptions from Weisser's Recension A and B manuscripts.

2. **The Latin vulgate is likewise a GPT reproduction.** It matches the well-known form from Steele & Singer (1928) but was reproduced from training data, not transcribed from the 1928 article or any manuscript.

3. **Several "translations" are actually translations of translations.** The Jabirian version is English from Arabic. The Ruska/Anonymous version is English from German from Arabic. The Fulcanelli versions are English from French from Latin. The Kriegsmann is English from Latin from pseudo-Phoenician. Each layer introduces interpretive drift.

4. **The "Twelfth Century Latin" is presented in English.** Despite its label, the text in the Bauer & Lindemann compilation is an English rendering of the Latin, not the Latin original.

5. **Verse numbering is editorial, not original.** The 0-14 scheme with sub-verses (6a, 7a, 11a) was imposed by the Bauer & Lindemann compilers for comparison. The original texts do not have verse numbers. Some translations merge or split verses differently.

## Extraction Method

Verses were extracted by `scripts/extract_translations.py` using deterministic regex parsing:
- Pattern: `^(\d+)(a)?\)\s*(.*)` matches verse-numbered lines
- Section boundaries detected by translation header patterns (e.g., "From Jabir ibn Hayyan", "Translation of Issac Newton")
- Citation lines (bracketed references) stripped from verse text
- Arabic and Latin vulgate verses entered as seed data, not extracted

All extraction is tagged with `source_method = 'CORPUS_EXTRACTION'` or `source_method = 'SEED_DATA'` in the `translation_verses` table.
