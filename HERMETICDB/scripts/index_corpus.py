import sqlite3
import hashlib
from pathlib import Path
from datetime import datetime

# --- CONFIG ---
WORKSPACE_ROOT = Path("c:/Dev/EmeraldTablet")
DB_PATH = WORKSPACE_ROOT / "db" / "emerald_tablet.db"
CORPUS_DIRS = [
    WORKSPACE_ROOT,
    WORKSPACE_ROOT / "hermetic",
]
EXTENSIONS = [".md", ".txt"]

def main():
    if not DB_PATH.exists():
        print(f"Error: Database not found at {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    indexed_count = 0

    for directory in CORPUS_DIRS:
        if not directory.exists():
            continue
        
        print(f"Scanning {directory}...")
        for ext in EXTENSIONS:
            for file_path in directory.glob(f"*{ext}"):
                # Skip specific system files
                if file_path.name in ["README.md", "CLAUDE.md", "PHASESTATUS.md", "TAKEAWAYS1.md", "INFRASTRUCTURE_NEXT.md", "HERMETICSEARCH.md", "EMERALDTABLET.md", "INFRASTRUCTURE_UPDATE_REPORT.md"]:
                    continue
                
                rel_path = file_path.relative_to(WORKSPACE_ROOT)
                slug = file_path.stem.lower().replace(" ", "_")
                
                # Check if already indexed
                cursor.execute("SELECT id FROM corpus_documents WHERE doc_id = ?", (slug,))
                if cursor.fetchone():
                    continue

                print(f"  Indexing {file_path.name}...")
                cursor.execute("""
                    INSERT INTO corpus_documents (doc_id, file_path, title, doc_family, source_type, text_quality, language)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (slug, str(rel_path), file_path.stem, 'SCHOLARLY_ARTICLE', 'PDF_EXTRACTED', 'HIGH', 'ENGLISH'))
                indexed_count += 1

    conn.commit()
    conn.close()
    print(f"Indexing complete. New: {indexed_count}")

if __name__ == "__main__":
    main()
