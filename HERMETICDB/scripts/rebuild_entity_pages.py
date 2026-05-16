import sqlite3
import os
import sys
from pathlib import Path

# Force UTF-8 for Windows console
if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR.parent / "db" / "emerald_tablet.db"

# HTML Template for Entity Pages
TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1"/>
    <title>{title} - HermeticDB</title>
    <link rel="stylesheet" href="/HermeticDB/_next/static/chunks/08.gpcoa-2x-j.css"/>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600&family=Inter:wght@400;500&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg: #0a0a0c;
            --bg-card: #141418;
            --accent: #d4af37;
            --accent-light: #f1d37e;
            --text-main: #e0e0e0;
            --text-muted: #a0a0a0;
            --border: rgba(212, 175, 55, 0.2);
            --font-display: 'Outfit', sans-serif;
            --font-body: 'Inter', sans-serif;
        }}

        body {{
            background-color: var(--bg);
            color: var(--text-main);
            font-family: var(--font-body);
            line-height: 1.6;
            margin: 0;
            padding: 0;
            overflow-x: hidden;
        }}

        .site-nav {{
            background: rgba(10, 10, 12, 0.8);
            backdrop-filter: blur(10px);
            border-bottom: 1px solid var(--border);
            position: sticky;
            top: 0;
            z-index: 1000;
            padding: 1rem 0;
        }}

        .nav-container {{
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 2rem;
        }}

        .nav-logo {{
            font-family: var(--font-display);
            font-size: 1.5rem;
            font-weight: 600;
            color: var(--accent);
            text-decoration: none;
            letter-spacing: 1px;
        }}

        .nav-links {{
            display: flex;
            gap: 1.5rem;
            align-items: center;
        }}

        .nav-link {{
            color: var(--text-main);
            text-decoration: none;
            font-size: 0.9rem;
            font-weight: 500;
            transition: color 0.3s;
            opacity: 0.8;
        }}

        .nav-link:hover {{
            color: var(--accent);
            opacity: 1;
        }}

        .page-header {{
            background: linear-gradient(to bottom, #1a1a20, #0a0a0c);
            padding: 4rem 2rem;
            text-align: center;
            border-bottom: 1px solid var(--border);
        }}

        .entity-title {{
            font-family: var(--font-display);
            font-size: 3.5rem;
            margin: 0;
            color: var(--accent-light);
            text-shadow: 0 2px 10px rgba(0,0,0,0.5);
        }}

        .entity-meta {{
            color: var(--accent);
            text-transform: uppercase;
            letter-spacing: 2px;
            font-size: 0.9rem;
            margin-top: 1rem;
            opacity: 0.8;
        }}

        .content-container {{
            max-width: 800px;
            margin: -2rem auto 4rem;
            background: var(--bg-card);
            padding: 3rem;
            border-radius: 12px;
            border: 1px solid var(--border);
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            position: relative;
        }}

        .prose-content {{
            font-size: 1.1rem;
            color: #d1d1d1;
        }}

        .prose-content h2 {{
            font-family: var(--font-display);
            color: var(--accent);
            border-bottom: 1px solid var(--border);
            padding-bottom: 0.5rem;
            margin-top: 2.5rem;
        }}

        .prose-content p {{
            margin-bottom: 1.5rem;
        }}

        .citation {{
            color: var(--accent);
            font-size: 0.8rem;
            vertical-align: super;
            text-decoration: none;
            cursor: help;
        }}

        .back-link {{
            display: inline-block;
            margin-bottom: 2rem;
            color: var(--accent);
            text-decoration: none;
            font-size: 0.9rem;
            transition: transform 0.3s;
        }}

        .back-link:hover {{
            transform: translateX(-5px);
        }}

        footer {{
            text-align: center;
            padding: 4rem 2rem;
            color: var(--text-muted);
            font-size: 0.8rem;
            border-top: 1px solid var(--border);
        }}
    </style>
</head>
<body>
    <nav class="site-nav">
        <div class="nav-container">
            <a class="nav-logo" href="/HermeticDB">HERMETICDB</a>
            <div class="nav-links">
                <a class="nav-link" href="/HermeticDB/eras/late-antiquity">Late Antiquity</a>
                <a class="nav-link" href="/HermeticDB/eras/medieval">Medieval</a>
                <a class="nav-link" href="/HermeticDB/eras/renaissance">Renaissance</a>
                <div style="width:1px;height:20px;background:rgba(255,255,255,0.1);margin:0 5px"></div>
                <a class="nav-link" href="/HermeticDB/texts">Texts</a>
                <a class="nav-link" href="/HermeticDB/biographies">Biographies</a>
                <a class="nav-link" href="/HermeticDB/scholars">Scholars</a>
                <a class="nav-link" href="/HermeticDB/dictionary">Dictionary</a>
            </div>
        </div>
    </nav>

    <header class="page-header">
        <h1 class="entity-title">{title}</h1>
        <div class="entity-meta">{meta}</div>
    </header>

    <main class="content-container">
        <a href="javascript:history.back()" class="back-link">← Back to Directory</a>
        <div class="prose-content">
            {content}
        </div>
    </main>

    <footer>
        &copy; 2026 The Hermetic Knowledge Portal · Provenance-Backed Synthesis
    </footer>
</body>
</html>
"""

def generate_page(title, meta, content, output_path):
    html = TEMPLATE.format(title=title, meta=meta, content=content)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

def main():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # 1. BIOGRAPHIES (Historical authors)
    cursor.execute("SELECT * FROM persons WHERE role_primary != 'SCHOLAR' OR role_primary IS NULL")
    for row in cursor.fetchall():
        pid = row['person_id']
        name = row['name']
        era = (row['era'] or "Unknown Era").replace("_", " ").title()
        role = (row['role_primary'] or "Figure").replace("_", " ").title()
        content = row['bio_html'] or f"<p>{row['description'] or 'Biographical details pending scholarly synthesis.'}</p>"
        
        output_path = BASE_DIR / "biographies" / f"{pid}.html"
        print(f"Generating biography for {name}...")
        generate_page(name, f"{era} · {role}", content, output_path)

    # 2. SCHOLARS (Modern academics)
    cursor.execute("SELECT * FROM persons WHERE role_primary = 'SCHOLAR'")
    for row in cursor.fetchall():
        pid = row['person_id']
        name = row['name']
        role = "Scholarly Authority"
        content = row['bio_html'] or f"<p>{row['description'] or 'Scholarly profile pending expansion.'}</p>"
        
        output_path = BASE_DIR / "scholars" / f"{pid}.html"
        print(f"Generating scholarly profile for {name}...")
        generate_page(name, role, content, output_path)

    # 3. TEXTS
    cursor.execute("SELECT * FROM texts")
    for row in cursor.fetchall():
        tid = row['text_id']
        title = row['title']
        ttype = (row['text_type'] or "Primary Source").replace("_", " ").title()
        content = row['analysis_html'] or f"<p>{row['description'] or 'Textual analysis pending scholarly synthesis.'}</p>"
        
        output_path = BASE_DIR / "texts" / f"{tid}.html"
        print(f"Generating text page for {title}...")
        generate_page(title, ttype, content, output_path)

    conn.close()
    print("Static site rebuild complete.")

if __name__ == "__main__":
    main()
