"""
assemble_prose.py — Pass 4: Narrative Synthesis (AI-Augmented)

Takes atomic claims from `entity_claims` and synthesizes them into clean, 
professional, scholarly prose using Gemini, while strictly maintaining 
citation integrity.
"""

import sqlite3
import os
from pathlib import Path
import google.generativeai as genai

# Setup paths
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "db" / "emerald_tablet.db"

# AI Configuration
API_KEY = os.environ.get("GOOGLE_API_KEY")
if API_KEY:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    model = None

def get_claims_for_entity(conn, entity_id):
    """Retrieves all claims and citations for an entity."""
    query = """
    SELECT claim_text, segment_id, source_quote, claim_type
    FROM entity_claims
    WHERE entity_id = ? AND review_status != 'REJECTED'
    """
    return conn.execute(query, (entity_id,)).fetchall()

def synthesize_with_ai(entity_name, claims):
    """Uses LLM to weave claims into clean, scholarly prose."""
    if not model:
        return None # Fallback to deterministic

    # Format claims for prompt
    claims_list = []
    for c in claims:
        text, sid, quote, ctype = c
        claims_list.append(f"- FACT: {text} [CIT: {sid}]")

    prompt = f"""
You are a senior academic scholar specializing in Hermeticism and Alchemical history.
Your task is to write a clean, flowing, professional, and deep biographical/conceptual entry for "{entity_name}".

INPUT DATA:
{chr(10).join(claims_list)}

STRICT REQUIREMENTS:
1. PROSE QUALITY: Write high-quality, scholarly narrative. No garlicky lists. Use complex but clear sentence structures.
2. CITATION INTEGRITY: You MUST append the citation tag [Segment_ID] (e.g., [doc_id:page_5]) to the end of EVERY sentence or clause that relies on that specific fact.
3. NO HALLUCINATION: Do NOT add any historical facts, dates, or details not found in the input list.
4. STRUCTURE: Use Markdown. Use sections like ## Historical Context, ## Academic Analysis, and ## Legacy.
5. LENGTH: Expand the writing to be as detailed as the facts allow.

Write the entry now:
"""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"  AI Synthesis failed for {entity_name}: {e}")
        return None

def build_deterministic_prose(entity_name, claims):
    """Fallback logic if AI is unavailable."""
    sections = {
        "Historical Context": [],
        "Academic Analysis": [],
        "Provenance & Legacy": []
    }
    
    for c in claims:
        text, sid, quote, ctype = c
        sentence = f"{text} [{sid}]"
        
        if ctype == 'BIOGRAPHICAL' or ctype == 'CONTEXT':
            sections["Historical Context"].append(sentence)
        elif ctype == 'SCHOLARSHIP' or ctype == 'ANALYSIS':
            sections["Academic Analysis"].append(sentence)
        else:
            sections["Provenance & Legacy"].append(sentence)

    output = f"# {entity_name}\n\n"
    for title, sentences in sections.items():
        if sentences:
            output += f"## {title}\n\n"
            output += " ".join(sentences) + "\n\n"
    return output

def main():
    if not DB_PATH.exists():
        print("Error: Database not found.")
        return

    conn = sqlite3.connect(DB_PATH)
    
    # Get all entities with claims
    entities = conn.execute("SELECT DISTINCT entity_id, entity_type FROM entity_claims").fetchall()
    print(f"Synthesizing prose for {len(entities)} entities...")

    for eid, etype in entities:
        # Get claims
        claims = get_claims_for_entity(conn, eid)
        if not claims: continue

        # Resolve display name
        name = eid.replace('_', ' ').title()
        if etype == 'PERSON':
            row = conn.execute("SELECT name FROM persons WHERE person_id = ?", (eid,)).fetchone()
            if row: name = row[0]
            table, col, id_col = 'persons', 'bio_html', 'person_id'
        elif etype == 'CONCEPT':
            row = conn.execute("SELECT label FROM concepts WHERE slug = ?", (eid,)).fetchone()
            if row: name = row[0]
            table, col, id_col = 'concepts', 'definition_long', 'slug'
        elif etype == 'TEXT':
            row = conn.execute("SELECT title FROM texts WHERE text_id = ?", (eid,)).fetchone()
            if row: name = row[0]
            table, col, id_col = 'texts', 'analysis_html', 'text_id'
        else: continue

        print(f"  -> Synthesizing: {name} ({etype})...")
        
        # Try AI first, then fallback
        prose = synthesize_with_ai(name, claims)
        if not prose:
            print("     (Falling back to deterministic mode)")
            prose = build_deterministic_prose(name, claims)
        
        # Update DB
        conn.execute(f"UPDATE {table} SET {col} = ? WHERE {id_col} = ?", (prose, eid))
        conn.commit()

    conn.close()
    print("Synthesis complete.")

if __name__ == "__main__":
    main()
