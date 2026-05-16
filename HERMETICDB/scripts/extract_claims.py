import sqlite3
import json
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR.parent / "db" / "emerald_tablet.db"
TASKS_DIR = BASE_DIR / "staging" / "claims_tasks"

def main():
    if not DB_PATH.exists():
        print("DB missing.")
        return
        
    TASKS_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    
    # Get high-relevance segments
    segments = conn.execute("SELECT segment_id, text_content FROM corpus_segments WHERE relevance_score > 0").fetchall()
    print(f"Preparing {len(segments)} tasks...")
    
    for sid, content in segments:
        task = {
            "segment_id": sid,
            "text": content
        }
        with open(TASKS_DIR / f"{sid.replace(':', '_')}.json", "w", encoding="utf-8") as f:
            json.dump(task, f)
            
    print("Tasks prepared.")

if __name__ == "__main__":
    main()
