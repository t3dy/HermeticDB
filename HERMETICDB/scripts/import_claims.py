import json
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR.parent / "db" / "emerald_tablet.db"
RESULTS_DIR = BASE_DIR / "staging" / "claims_results"

def register_new_entity(conn, entity_type, entity_id):
    name_display = entity_id.replace('_', ' ').title()
    if entity_type == 'PERSON':
        conn.execute("INSERT OR IGNORE INTO persons (person_id, name) VALUES (?, ?)", (entity_id, name_display))
    elif entity_type == 'CONCEPT':
        conn.execute("INSERT OR IGNORE INTO concepts (slug, label) VALUES (?, ?)", (entity_id, name_display))
    elif entity_type == 'TEXT':
        conn.execute("INSERT OR IGNORE INTO texts (text_id, title) VALUES (?, ?)", (entity_id, name_display))

def main():
    if not RESULTS_DIR.exists():
        print("No results.")
        return

    conn = sqlite3.connect(DB_PATH)
    # Ensure table exists
    conn.execute("""
    CREATE TABLE IF NOT EXISTS entity_claims (
        claim_id INTEGER PRIMARY KEY AUTOINCREMENT,
        entity_type TEXT,
        entity_id TEXT,
        claim_type TEXT,
        claim_text TEXT,
        segment_id TEXT,
        source_quote TEXT,
        review_status TEXT,
        confidence TEXT
    )
    """)
    
    files = list(RESULTS_DIR.glob("*.json"))
    for rf in files:
        with open(rf, "r") as f:
            data = json.load(f)
        
        sid = data["segment_id"]
        for claim in data["claims"]:
            eid = claim["entity_id"]
            etype = claim.get("entity_type", "PERSON")
            
            register_new_entity(conn, etype, eid)
            
            conn.execute("""
            INSERT INTO entity_claims (entity_type, entity_id, claim_text, segment_id, source_quote, review_status)
            VALUES (?, ?, ?, ?, ?, 'DRAFT')
            """, (etype, eid, claim["claim_text"], sid, claim["source_quote"]))
    
    conn.commit()
    print("Import complete.")

if __name__ == "__main__":
    main()
