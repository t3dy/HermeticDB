import json
import sqlite3
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR.parent / "db" / "emerald_tablet.db"
TASKS_DIR = BASE_DIR / "staging" / "claims_tasks"
RESULTS_DIR = BASE_DIR / "staging" / "claims_results"

def process_task(task):
    seg_id = task["segment_id"]
    text = task["text"]
    
    # Simple deterministic extraction based on regex
    # Matches: [[Entity:Type:Claim]]
    # or just looks for known entities and surrounding context
    claims = []
    
    # Pattern: "Entity (person/text/concept) was/is/did ..."
    entities_regex = r"([A-Z][a-z]+(?:\s[A-Z][a-z]+)*)"
    matches = re.finditer(entities_regex, text)
    
    for m in matches:
        entity = m.group(1)
        # Context extraction
        start = max(0, m.start() - 50)
        end = min(len(text), m.end() + 150)
        context = text[start:end].strip()
        
        if len(context) > 20:
            claims.append({
                "entity_id": entity.lower().replace(" ", "_"),
                "entity_type": "PERSON", # Default for regex
                "claim_text": context,
                "source_quote": context[:100]
            })
            
    return {"segment_id": seg_id, "claims": claims}

def main():
    if not TASKS_DIR.exists():
        print("No tasks found.")
        return
    
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    task_files = list(TASKS_DIR.glob("*.json"))
    print(f"Processing {len(task_files)} tasks...")
    
    for tf in task_files:
        with open(tf, "r", encoding="utf-8") as f:
            task = json.load(f)
        
        result = process_task(task)
        if result["claims"]:
            with open(RESULTS_DIR / tf.name, "w", encoding="utf-8") as f:
                json.dump(result, f)

if __name__ == "__main__":
    main()
