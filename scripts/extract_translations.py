"""
extract_translations.py — Parse verse-level translations from History_and_Translations markdown.

Stage 6 of pipeline. Extracts numbered verses from each translation section,
aligns them to the canonical 0-14 verse numbering scheme.

Also inserts Arabic and Latin vulgate verses from EmeraldTabletGPTandGemini.txt.

Idempotent: uses INSERT OR IGNORE.
Prerequisite: seed_from_json.py must have run (translations table populated).
"""

import re
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "db" / "emerald_tablet.db"
HISTORY_PATH = BASE_DIR / "History_and_Translations_of_Emerald_Tablet.md"

# Translation sections in the History file, mapped to translation_ids
TRANSLATION_SECTIONS = [
    {
        "header_pattern": r"From Jabir ibn Hayyan",
        "translation_id": "jabir_arabic",
    },
    {
        "header_pattern": r"Another Arabic Version.*Ruska",
        "translation_id": "ruska_anonymous_arabic",
    },
    {
        "header_pattern": r"Twelfth Century Latin",
        "translation_id": "twelfth_century_latin",
    },
    {
        "header_pattern": r"Georgio Beato",
        "translation_id": "beato_latin",
    },
    {
        "header_pattern": r"Translation of Issac Newton",
        "translation_id": "newton_english",
    },
    {
        "header_pattern": r"Kriegsmann.*Phoenician",
        "translation_id": "kriegsmann_translation",
    },
    {
        "header_pattern": r"Sigismund Bacstrom",
        "translation_id": "bacstrom_english",
    },
    {
        "header_pattern": r"From Madame Blavatsky",
        "translation_id": "blavatsky_english",
    },
    {
        "header_pattern": r"From Fulcanelli.*Sieveking",
        "translation_id": "fulcanelli_french_1",
    },
    {
        "header_pattern": r"From Fulcanelli.*new translation",
        "translation_id": "fulcanelli_french_2",
    },
    {
        "header_pattern": r"From Idres Shah",
        "translation_id": "idries_shah_english",
    },
    {
        "header_pattern": r"Hypothetical Chinese",
        "translation_id": None,  # Skip — not a real translation
    },
]

# Arabic verses from EmeraldTabletGPTandGemini.txt (manually curated)
ARABIC_VERSES = {
    "1": "حقًّا يقينًا لا شك فيه",
    "2": "إنّ الأعلى من الأسفل، والأسفل من الأعلى",
    "3": "يعمل عجائب شيء واحد\nوكما كانت الأشياء كلها من واحد بتدبير واحد\nفكذلك ولدت من هذا الشيء الواحد بتدبير",
    "4": "أبوه الشمس، وأمه القمر",
    "5": "حملته الريح في بطنها، أرضته الأرض",
    "6": "هو أبو كل طلسم في العالم كله",
    "6a": "قوته تامّة إذا تحولت إلى الأرض",
    "7": "تفصل الأرض من النار، اللطيف من الكثيف برفق وحكمة",
    "8": "يصعد من الأرض إلى السماء، ثم ينزل إلى الأرض\nفيأخذ قوة العلويات والسفليات",
    "9": "فبهذا يكون لك مجد العالم كله\nلذلك يهرب منك كل ظلمة",
    "10": "هذه قوة القوى كلها، لأنها تغلب كل شيء لطيف وتدخل في كل شيء كثيف",
    "11": "هكذا خلق العالم",
    "12": "من هذا تكون العجائب، ووسائله هذه",
    "13": "ولذلك سميت هرمس مثلث بالحكمة",
}

# Latin vulgate verses (standard medieval form)
LATIN_VULGATE_VERSES = {
    "1": "Verum, sine mendacio, certum et verissimum:",
    "2": "Quod est inferius est sicut quod est superius,\net quod est superius est sicut quod est inferius,\nad perpetranda miracula rei unius.",
    "3": "Et sicut omnes res fuerunt ab uno, meditatione unius,\nsic omnes res natae fuerunt ab hac una re, adaptatione.",
    "4": "Pater eius est Sol, mater eius Luna;",
    "5": "portavit illud ventus in ventre suo;\nnutrix eius terra est.",
    "6": "Pater omnis telesmi totius mundi est hic.",
    "6a": "Vis eius integra est, si versa fuerit in terram.",
    "7": "Separabis terram ab igne, subtile a spisso, suaviter cum magno ingenio.",
    "8": "Ascendit a terra in caelum, iterumque descendit in terram,\net recipit vim superiorum et inferiorum.",
    "9": "Sic habebis gloriam totius mundi;\nideo fugiet a te omnis obscuritas.",
    "10": "Haec est totius fortitudinis fortitudo fortis,\nquia vincet omnem rem subtilem, omnemque solidam penetrabit.",
    "11": "Sic mundus creatus est.",
    "12": "Hinc erunt adaptationes mirabiles, quarum modus est hic.",
    "13": "Itaque vocatus sum Hermes Trismegistus, habens tres partes philosophiae totius mundi.",
    "14": "Completum est quod dixi de operatione Solis.",
}


def find_sections(content):
    """Find translation section boundaries in the History markdown."""
    sections = []
    lines = content.split('\n')

    for i, section_def in enumerate(TRANSLATION_SECTIONS):
        pattern = section_def["header_pattern"]
        for line_num, line in enumerate(lines):
            if re.search(pattern, line, re.IGNORECASE):
                sections.append({
                    "translation_id": section_def["translation_id"],
                    "start_line": line_num,
                    "header": line.strip(),
                })
                break

    # Sort by start line
    sections.sort(key=lambda s: s["start_line"])

    # Set end lines
    for i, sec in enumerate(sections):
        if i + 1 < len(sections):
            sec["end_line"] = sections[i + 1]["start_line"]
        else:
            # Find TEXTUAL REMARKS as end
            for line_num, line in enumerate(lines):
                if "TEXTUAL REMARKS" in line:
                    sec["end_line"] = line_num
                    break
            else:
                sec["end_line"] = len(lines)

    return sections, lines


def parse_verses(lines, start, end):
    """Extract numbered verses from a section. Returns dict of verse_number → text."""
    verses = {}
    current_verse = None
    current_text = []
    section_text = lines[start:end]

    for line in section_text:
        line = line.strip()
        if not line:
            continue

        # Match verse numbers: "0)", "1)", "2)", "6a)", "7a)", "11a)", "14)"
        match = re.match(r'^(\d+)(a)?\)\s*(.*)', line)
        if match:
            # Save previous verse
            if current_verse is not None:
                text = ' '.join(current_text).strip()
                if text:
                    verses[current_verse] = text
            # Start new verse
            num = match.group(1)
            sub = match.group(2) or ""
            verse_key = f"{num}{sub}" if sub else num
            current_verse = verse_key
            current_text = [match.group(3)] if match.group(3) else []
        elif current_verse is not None:
            # Skip citation lines
            if line.startswith('[') and line.endswith(']'):
                continue
            # Skip section headers
            if line.startswith('From ') or line.startswith('Translation'):
                continue
            current_text.append(line)

    # Save last verse
    if current_verse is not None:
        text = ' '.join(current_text).strip()
        # Remove trailing citation
        text = re.sub(r'\s*\[.*?\]\s*$', '', text)
        if text:
            verses[current_verse] = text

    return verses


def normalize_verse_number(key):
    """Split '6a' into ('6', 'a') and '11a' into ('11', 'a')."""
    match = re.match(r'^(\d+)(a)?$', key)
    if match:
        return match.group(1), match.group(2)
    return key, None


def insert_verses(conn, translation_id, verses, source_method="CORPUS_EXTRACTION"):
    """Insert verse rows for a translation."""
    # Resolve translation FK
    row = conn.execute(
        "SELECT id FROM translations WHERE translation_id = ?", (translation_id,)
    ).fetchone()
    if not row:
        print(f"  WARNING: translation_id '{translation_id}' not found in translations table. Skipping.")
        return 0

    trans_pk = row[0]
    inserted = 0

    for verse_key, text in verses.items():
        verse_num, verse_sub = normalize_verse_number(verse_key)
        conn.execute("""
            INSERT OR IGNORE INTO translation_verses
                (translation_id, verse_number, verse_sub, verse_text, source_method, confidence)
            VALUES (?, ?, ?, ?, ?, 'HIGH')
        """, (trans_pk, verse_num, verse_sub, text, source_method))
        inserted += 1

    return inserted


def main():
    if not DB_PATH.exists():
        print("ERROR: Database not found. Run init_db.py + seed_from_json.py first.")
        return

    if not HISTORY_PATH.exists():
        print(f"ERROR: Source file not found: {HISTORY_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    content = HISTORY_PATH.read_text(encoding='utf-8', errors='replace')
    total_inserted = 0

    # 1. Parse History_and_Translations sections
    sections, lines = find_sections(content)
    print(f"Found {len(sections)} translation sections")

    for sec in sections:
        tid = sec["translation_id"]
        if tid is None:
            print(f"  Skipping: {sec['header'][:60]}")
            continue

        verses = parse_verses(lines, sec["start_line"], sec["end_line"])
        if verses:
            count = insert_verses(conn, tid, verses)
            total_inserted += count
            print(f"  {tid}: {count} verses ({', '.join(sorted(verses.keys(), key=lambda x: (int(re.match(r'\d+', x).group()), x)))})")
        else:
            print(f"  {tid}: no verses found")

    # 2. Insert Arabic verses (from research notes)
    count = insert_verses(conn, "arabic_sirr_al_khaliqa", ARABIC_VERSES, "SEED_DATA")
    total_inserted += count
    print(f"  arabic_sirr_al_khaliqa: {count} verses")

    # 3. Insert Latin vulgate verses
    count = insert_verses(conn, "latin_vulgate", LATIN_VULGATE_VERSES, "SEED_DATA")
    total_inserted += count
    print(f"  latin_vulgate: {count} verses")

    conn.commit()

    # Report
    total = conn.execute("SELECT COUNT(*) FROM translation_verses").fetchone()[0]
    translations_with_verses = conn.execute("""
        SELECT COUNT(DISTINCT translation_id) FROM translation_verses
    """).fetchone()[0]
    print(f"\nTotal: {total} verses across {translations_with_verses} translations")

    # Verse coverage
    print("\nVerse coverage by translation:")
    rows = conn.execute("""
        SELECT t.translation_id, t.title, COUNT(tv.id) as verse_count
        FROM translations t
        LEFT JOIN translation_verses tv ON t.id = tv.translation_id
        GROUP BY t.id
        ORDER BY verse_count DESC
    """).fetchall()
    for tid, title, count in rows:
        status = "+" if count > 0 else "-"
        print(f"  {status} {tid}: {count} verses -- {title[:50]}")

    conn.close()


if __name__ == "__main__":
    main()
