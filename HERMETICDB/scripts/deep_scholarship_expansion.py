import sqlite3
import os
import sys
from pathlib import Path
import google.generativeai as genai

# Setup paths
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR.parent / "db" / "emerald_tablet.db"

# AI Configuration
API_KEY = os.environ.get("GOOGLE_API_KEY")
if API_KEY:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    print("Error: GOOGLE_API_KEY not found. Synthesis inhibited.")
    sys.exit(1)

def generate_scholarly_prose(name, role, era, description):
    prompt = f"""
    You are a world-leading professor of Western Esotericism and Hermetic Studies.
    Your task is to write a deeply scholarly, professional, and dense narrative entry for an encyclopedia of Hermeticism.
    
    ENTITY: {name}
    ROLE: {role}
    ERA: {era}
    CURRENT DESCRIPTION: {description}
    
    INSTRUCTIONS:
    1. PROSE: Use sophisticated, academic language. Avoid bullet points at all costs.
    2. DEPTH: Expand on the historical significance of this entity within the Hermetic tradition.
    3. TONE: Scholarly, objective, and authoritative.
    4. STRUCTURE: Use Markdown. Include sections like ## Historical Context and ## Scholarly Significance.
    5. CITATIONS: Since this is an encyclopedia entry, use a formal bibliographic tone. If specific works are mentioned, ensure they are in italics.
    
    Write the entry now (approx 300-500 words):
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error generating prose for {name}: {e}")
        return None

def main():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # 1. PROCESS PERSONS
    cursor.execute("SELECT * FROM persons")
    persons = cursor.fetchall()
    print(f"Expanding scholarship for {len(persons)} persons...")
    
    for row in persons:
        pid = row['person_id']
        name = row['name']
        role = row['role_primary'] or "Figure"
        era = row['era'] or "Unknown"
        desc = row['description'] or ""
        
        # Skip if already high quality (optional check, but user said ALL)
        print(f"  -> Synthesizing biography for {name}...")
        prose = generate_scholarly_prose(name, role, era, desc)
        if prose:
            # We save as HTML by converting MD to basic HTML wrapper if needed, 
            # or just leave as MD if our page generator handles it.
            # My page generator just injects {content}.
            # I'll wrap it in a simple div for safety.
            import markdown
            html_prose = markdown.markdown(prose)
            
            cursor.execute("UPDATE persons SET bio_html = ? WHERE person_id = ?", (html_prose, pid))
            conn.commit()

    # 2. PROCESS TEXTS
    cursor.execute("SELECT * FROM texts")
    texts = cursor.fetchall()
    print(f"Expanding scholarship for {len(texts)} texts...")
    
    for row in texts:
        tid = row['text_id']
        title = row['title']
        ttype = row['text_type'] or "Text"
        desc = row['description'] or ""
        
        print(f"  -> Synthesizing analysis for {title}...")
        prose = generate_scholarly_prose(title, ttype, "Hermetic Tradition", desc)
        if prose:
            import markdown
            html_prose = markdown.markdown(prose)
            
            cursor.execute("UPDATE texts SET analysis_html = ? WHERE text_id = ?", (html_prose, tid))
            conn.commit()

    conn.close()
    print("Deep scholarship expansion complete.")

if __name__ == "__main__":
    main()
