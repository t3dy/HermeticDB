import sqlite3
import re
from pathlib import Path

# --- CONFIG ---
WORKSPACE_ROOT = Path("c:/Dev/EmeraldTablet")
DB_PATH = WORKSPACE_ROOT / "db" / "emerald_tablet.db"

def segment_markdown(text):
    """Simple segmentation by paragraphs or header markers."""
    segments = re.split(r'\n\s*\n', text)
    return [s.strip() for s in segments if s.strip()]

def main():
    if not DB_PATH.exists():
        print("DB not found.")
        return

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # Find docs that haven't been segmented yet
    cursor.execute("""
        SELECT * FROM corpus_documents 
        WHERE id NOT IN (SELECT DISTINCT doc_id FROM corpus_segments)
    """)
    docs = cursor.fetchall()
    
    if not docs:
        print("No documents requiring segmentation.")
        conn.close()
        return

    for doc in docs:
        db_internal_id = doc['id']
        file_path = WORKSPACE_ROOT / doc['file_path']
        print(f"Segmenting {doc['title']}...")

        if not file_path.exists():
            print(f"  Warning: File not found {file_path}")
            continue

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        segments = segment_markdown(content)
        
        for i, seg_text in enumerate(segments):
            seg_id = f"seg_{i:04d}"
            cursor.execute("""
                INSERT INTO corpus_segments 
                (doc_id, segment_id, text_content, char_count, section_type)
                VALUES (?, ?, ?, ?, ?)
            """, (db_internal_id, seg_id, seg_text, len(seg_text), 'SECTION'))

    conn.commit()
    conn.close()
    print("Segmentation complete.")

if __name__ == "__main__":
    main()
