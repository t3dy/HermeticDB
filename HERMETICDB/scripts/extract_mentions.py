import sqlite3
import re
from pathlib import Path

# --- CONFIG ---
WORKSPACE_ROOT = Path("c:/Dev/EmeraldTablet")
DB_PATH = WORKSPACE_ROOT / "db" / "emerald_tablet.db"

def main():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # Load entities
    cursor.execute("SELECT person_id, name FROM persons")
    persons = {row['name'].lower(): row['person_id'] for row in cursor.fetchall()}
    
    cursor.execute("SELECT slug, label FROM concepts")
    concepts = {row['label'].lower(): row['slug'] for row in cursor.fetchall()}
    
    cursor.execute("SELECT text_id, title FROM texts")
    texts = {row['title'].lower(): row['text_id'] for row in cursor.fetchall()}

    # Scan segments
    cursor.execute("SELECT id, text_content FROM corpus_segments")
    segments = cursor.fetchall()

    print(f"Analyzing {len(segments)} segments for entity mentions...")
    
    for seg in segments:
        seg_id = seg['id']
        content = seg['text_content'].lower()
        
        found_persons = [pid for name, pid in persons.items() if name in content]
        found_concepts = [slug for label, slug in concepts.items() if label in content]
        found_texts = [tid for title, tid in texts.items() if title in content]
        
        if found_persons or found_concepts or found_texts:
            merged_persons = ",".join(found_persons)
            merged_concepts = ",".join(found_concepts)
            
            cursor.execute("""
                UPDATE corpus_segments 
                SET persons_mentioned = ?, concepts_mentioned = ? 
                WHERE id = ?
            """, (merged_persons, merged_concepts, seg_id))

    conn.commit()
    conn.close()
    print("Mention extraction complete.")

if __name__ == "__main__":
    main()
