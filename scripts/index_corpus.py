"""
index_corpus.py — Scan all corpus files and register them in corpus_documents.

Stage 2 of pipeline. Scans root, hermetic/, KeyHermeticChats/ for .md and .txt files.
Classifies each by doc_family, language, text_quality, source_type.

Idempotent: uses INSERT OR IGNORE on doc_id.
Prerequisite: init_db.py + migrate_v2.py must have run.
"""

import re
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "db" / "emerald_tablet.db"

# Directories to scan (relative to BASE_DIR)
SCAN_DIRS = [
    BASE_DIR,                          # root .md/.txt files
    BASE_DIR / "hermetic",             # scholarly PDFs converted to .md
    BASE_DIR / "KeyHermeticChats",     # curated research chats
]

# Files to skip (project docs, not corpus)
SKIP_FILES = {
    'CLAUDE.md', 'PHASESTATUS.md', 'TAKEAWAYS1.md', 'HERMETICSEARCH.md',
    'INFRASTRUCTURE_NEXT.md', 'INFRASTRUCTURE_UPDATE_REPORT.md',
}
SKIP_DIRS = {'docs', 'scripts', 'data', 'db', 'site', 'staging', 'source',
             '.claude', '.git', 'HermeticChats', 'Hermetis_Trismegisti_images'}


def slugify(name):
    """Create a stable slug from filename."""
    slug = re.sub(r'[^\w\s-]', '', name.lower())
    slug = re.sub(r'[\s_]+', '_', slug).strip('_')
    return slug[:120]


def classify_doc_family(path, content):
    """Classify document family from path and content heuristics."""
    name = path.name.lower()
    parent = path.parent.name.lower()

    if parent == 'keyhermeticchats' or 'chat' in parent:
        return 'CHAT_SUMMARY'
    if name.endswith('.maier_extract.txt'):
        return 'MAIER_EXTRACT'
    if name.startswith('20') and '_' in name[:12]:
        # Dated research files like 2025-08-17_Iamblichus...
        return 'RESEARCH_NOTES'
    if 'emeraldtabletgpt' in name or 'medievalhermeticgemini' in name:
        return 'RESEARCH_NOTES'

    # Journal articles (bracketed names)
    if name.startswith('['):
        for journal_marker in ['speculum', 'numen', 'journal', 'review', 'aries',
                               'vigiliae', 'viator', 'ambix', 'anglia', 'gnosis',
                               'studia', 'philosophia', 'archiv', 'renaissance']:
            if journal_marker in name:
                return 'SCHOLARLY_ARTICLE'
        return 'SCHOLARLY_ARTICLE'

    # Known monographs / critical editions
    if any(k in name for k in ['corpus christianorum', 'asclepius']):
        return 'CRITICAL_EDITION'
    if any(k in name for k in ['copenhaver hermetica', 'litwa hermetica']):
        return 'HERMETIC_CORPUS'
    if any(k in name for k in ['bull the tradition', 'moreschini hermes',
                                'ebeling.*secret history', 'hanegraaff.*hermetic']):
        return 'SCHOLARLY_MONOGRAPH'
    if any(k in name for k in ['needham', 'debus.*chemical', 'nasr.*anthology']):
        return 'REFERENCE_WORK'
    if any(k in name for k in ['alchemy', 'alchemical', 'al.razi']):
        return 'ALCHEMICAL'
    if any(k in name for k in ['hermes', 'hermetic', 'hermetis', 'hermetism']):
        return 'HERMETIC_CORPUS'
    if any(k in name for k in ['khunrath', 'agrippa', 'lazzarelli', 'ficino', 'bruno']):
        return 'SCHOLARLY_MONOGRAPH'

    # Fallback based on size
    if content and len(content) > 100000:
        return 'SCHOLARLY_MONOGRAPH'
    return 'SCHOLARLY_ARTICLE'


def detect_source_type(path):
    """Detect how the file was produced."""
    name = path.name.lower()
    if name.endswith('.maier_extract.txt'):
        return 'MAIER_EXTRACT'
    if path.parent.name.lower() == 'keyhermeticchats':
        return 'CHAT_EXPORT'
    if name.startswith('20') and '_' in name[:12]:
        return 'RESEARCH_NOTES'
    if 'gptandgemini' in name or 'gemini' in name:
        return 'RESEARCH_NOTES'
    # Check content for OCR markers
    return 'PDF_EXTRACTED'


def detect_language(content):
    """Detect primary language from character analysis."""
    if not content:
        return 'UNKNOWN'
    sample = content[:10000]
    arabic = len(re.findall(r'[\u0600-\u06FF]', sample))
    greek = len(re.findall(r'[\u0370-\u03FF]', sample))
    german_markers = len(re.findall(r'\b(und|der|die|das|ist|ein|von|mit|für|über)\b', sample, re.IGNORECASE))
    french_markers = len(re.findall(r'\b(les|des|une|est|dans|pour|avec|sur|cette)\b', sample, re.IGNORECASE))
    italian_markers = len(re.findall(r'\b(della|nella|alla|sono|questa|degli|delle)\b', sample, re.IGNORECASE))
    latin_markers = len(re.findall(r'\b(est|sunt|quod|cum|enim|autem|vel|sed|non)\b', sample))

    total = len(sample)
    if arabic / max(total, 1) > 0.1:
        return 'ARABIC'
    if greek / max(total, 1) > 0.05:
        return 'GREEK'
    if german_markers > 20:
        return 'GERMAN'
    if french_markers > 20:
        return 'FRENCH'
    if italian_markers > 20:
        return 'ITALIAN'
    if latin_markers > 30 and german_markers < 5 and french_markers < 5:
        return 'LATIN'
    return 'ENGLISH'


def assess_quality(content):
    """Assess text quality."""
    if not content or len(content.strip()) < 100:
        return 'EMPTY'
    sample = content[:5000]
    # Check for OCR artifacts: high ratio of non-ASCII, garbled words
    ascii_ratio = sum(1 for c in sample if c.isascii()) / max(len(sample), 1)
    if ascii_ratio < 0.5:
        return 'LOW'
    # Check for run-together words (camelCase artifacts)
    camel_count = len(re.findall(r'[a-z][A-Z]', sample))
    if camel_count > 20:
        return 'MEDIUM'
    return 'HIGH'


def count_pages(content):
    """Count ## Page N headers."""
    return len(re.findall(r'^## Page \d+', content, re.MULTILINE))


def clean_title(path):
    """Extract a clean title from filename."""
    name = path.stem
    # Strip common suffixes
    name = re.sub(r'\s*-?\s*libgen[\._]li$', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\{[^}]*\}', '', name)
    name = re.sub(r'\[[\d\._]+\]', '', name)
    name = re.sub(r'\(\d{4}[^)]*\)', '', name)
    name = re.sub(r'\.maier_extract$', ' (Maier extract)', name)
    name = re.sub(r'\s+', ' ', name).strip()
    if len(name) > 200:
        name = name[:200]
    return name


def main():
    if not DB_PATH.exists():
        print(f"ERROR: Database not found at {DB_PATH}. Run init_db.py + migrate_v2.py first.")
        return

    conn = sqlite3.connect(DB_PATH)

    # Verify corpus_documents table exists
    tables = [r[0] for r in conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table'"
    ).fetchall()]
    if 'corpus_documents' not in tables:
        print("ERROR: corpus_documents table not found. Run migrate_v2.py first.")
        conn.close()
        return

    indexed = 0
    skipped = 0

    for scan_dir in SCAN_DIRS:
        if not scan_dir.exists():
            continue

        # Only scan direct children (not recursive into HermeticChats etc.)
        for ext in ['*.md', '*.txt']:
            for path in sorted(scan_dir.glob(ext)):
                # Skip project docs
                if path.name in SKIP_FILES:
                    skipped += 1
                    continue

                # Skip if in a skip directory
                rel = path.relative_to(BASE_DIR)
                if any(part in SKIP_DIRS for part in rel.parts[:-1]):
                    skipped += 1
                    continue

                # Read content
                try:
                    content = path.read_text(encoding='utf-8', errors='replace')
                except Exception:
                    content = ''

                doc_id = slugify(path.stem)
                file_path = str(path.relative_to(BASE_DIR)).replace('\\', '/')
                title = clean_title(path)
                doc_family = classify_doc_family(path, content)
                source_type = detect_source_type(path)
                language = detect_language(content)
                quality = assess_quality(content)
                pages = count_pages(content)

                conn.execute("""
                    INSERT OR IGNORE INTO corpus_documents
                        (doc_id, file_path, title, doc_family, language,
                         text_quality, source_type, page_count,
                         source_method, confidence)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'DETERMINISTIC', 'HIGH')
                """, (
                    doc_id, file_path, title, doc_family, language,
                    quality, source_type, pages if pages > 0 else None
                ))
                indexed += 1

    conn.commit()

    # Report
    total = conn.execute("SELECT COUNT(*) FROM corpus_documents").fetchone()[0]
    print(f"Indexed: {indexed} files ({skipped} skipped)")
    print(f"Total corpus_documents: {total}")

    # Breakdown by family
    families = conn.execute(
        "SELECT doc_family, COUNT(*) FROM corpus_documents GROUP BY doc_family ORDER BY COUNT(*) DESC"
    ).fetchall()
    for family, count in families:
        print(f"  {family or 'NULL'}: {count}")

    conn.close()


if __name__ == "__main__":
    main()
