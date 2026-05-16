import sqlite3
import os
import shutil
import re
from pathlib import Path

ITALIC_TERMS = [
    "anima mundi", "spiritus mundi", "prisca theologia", "philosophia occulta",
    "magia naturalis", "magia ceremonialis", "magia daemonica", "De Occulta Philosophia",
    "De Vita Libri Tres", "Corpus Hermeticum", "De Mysteriis", "Theologia Platonica",
    "De Vanitate Scientiarum", "Tabula Smaragdina", "Ars Magna", "Ars Notoria",
    "De Docta Ignorantia", "De Radiis Stellarum", "Speculum Astronomiae",
    "Monas Hieroglyphica", "Steganographia", "Polygraphia", "Utriusque Cosmi Historia",
    "De Arte Cabalistica", "De Verbo Mirifico", "De Umbris Idearum",
    "De la Causa, Principio et Uno", "Conclusiones Nongentae",
    "Oratio de Hominis Dignitate", "Kabbala Denudata", "Opus Majus",
    "Disputationes adversus astrologiam divinatricem",
    "coincidentia oppositorum", "docta ignorantia",
    "scientia experimentalis", "tria prima", "solve et coagula", "lapis philosophorum",
    "magia", "theurgia", "theologia", "philosophia",
    "demiurgus", "nous", "pneuma", "epistrophe", "proodos",
    "sephiroth", "sefirot", "ein sof", "ain soph",
    "gematria", "notarikon", "temurah", "gilgul",
    "nefesh", "ruach", "neshamah", "okhema", "spiritus"
]

def clean_prose(text):
    if not text: return ""
    # Strip hashtags, brackets, and other code-like artifacts
    text = re.sub(r'[#\[\]{}*]', '', text)
    # Ensure it's treated as a single block of prose
    return text.strip()

def italicize_terms(text):
    if not text: return ""
    # Strip artifacts first
    text = clean_prose(text)
    # Wrap in p if not present
    if not text.startswith("<p>"):
        text = f"<p>{text}</p>"
    
    # Custom italics for common Hermetic terms
    terms = ["Nous", "Logos", "Pneuma", "Gnosis", "Eusebeia", "Thriskeia", "Poimandres", "Asklepios", "Palingenesia", "Sympatheia"]
    for term in terms:
        text = re.sub(rf'\b{term}\b', f'<i>{term}</i>', text, flags=re.IGNORECASE)
    return text

# --- CONFIG ---
WORKSPACE_ROOT = Path("c:/Dev/EmeraldTablet")
DB_PATH = WORKSPACE_ROOT / "db" / "emerald_tablet.db"
DOCS_DIR = WORKSPACE_ROOT / "docs"
SITE_DIR = WORKSPACE_ROOT / "site"
SITE_NAME = "HermeticDB"
REPO_URL = f"/{SITE_NAME}" 

# --- SHARED STYLES ---
CSS = """
:root {
    --bg: #0a0a0c;
    --bg-card: #141418;
    --accent: #d4af37;
    --accent-light: #f1d37e;
    --text-main: #e0e0e0;
    --text-muted: #a0a0a0;
    --border: rgba(212, 175, 55, 0.2);
    --font-display: 'Outfit', sans-serif;
    --font-body: 'Inter', sans-serif;
}

body {
    background-color: var(--bg);
    color: var(--text-main);
    font-family: var(--font-body);
    line-height: 1.6;
    margin: 0;
    padding: 0;
}

.site-nav {
    background: rgba(10, 10, 12, 0.9);
    backdrop-filter: blur(10px);
    border-bottom: 1px solid var(--border);
    position: sticky;
    top: 0;
    z-index: 1000;
    padding: 1rem 0;
}

.nav-container {
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 2rem;
}

.nav-logo {
    font-family: var(--font-display);
    font-size: 1.5rem;
    font-weight: 600;
    color: var(--accent);
    text-decoration: none;
    letter-spacing: 1px;
}

.nav-links {
    display: flex;
    gap: 1.5rem;
    align-items: center;
}

.nav-link {
    color: var(--text-main);
    text-decoration: none;
    font-size: 0.9rem;
    font-weight: 500;
    transition: color 0.3s;
}

.nav-link:hover {
    color: var(--accent);
}

.page-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 4rem 2rem;
}

.title-large {
    font-family: var(--font-display);
    font-size: 3.5rem;
    color: var(--accent-light);
    margin-bottom: 1rem;
}

.text-subtitle {
    color: var(--text-muted);
    font-size: 1.2rem;
    margin-bottom: 3rem;
}

.grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    gap: 2rem;
}

.card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 2rem;
    transition: all 0.3s ease;
    text-decoration: none;
    color: inherit;
    display: flex;
    flex-direction: column;
    position: relative;
    overflow: hidden;
}

.card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; width: 4px; height: 100%;
    background: var(--accent);
    opacity: 0;
    transition: opacity 0.3s;
}

.card:hover {
    transform: translateY(-5px);
    border-color: var(--accent);
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
}

.card:hover::before {
    opacity: 1;
}

.card-title {
    font-family: var(--font-display);
    font-size: 1.6rem;
    color: var(--accent-light);
    margin-bottom: 0.5rem;
}

.card-meta {
    font-size: 0.8rem;
    color: var(--accent);
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 1rem;
    font-weight: 600;
}

.card-desc {
    font-size: 0.95rem;
    color: var(--text-muted);
}

.prose-content {
    background: var(--bg-card);
    padding: 3rem;
    border-radius: 12px;
    border: 1px solid var(--border);
    font-size: 1.15rem;
    color: #d8d8d8;
}

.prose-content h2 {
    font-family: var(--font-display);
    color: var(--accent);
    border-bottom: 1px solid var(--border);
    padding-bottom: 0.5rem;
    margin-top: 2rem;
}

.prose-content p {
    margin-bottom: 1.5rem;
}

.back-link {
    color: var(--accent);
    text-decoration: none;
    display: inline-block;
    margin-bottom: 2rem;
    font-size: 0.9rem;
}

.scholarly-fragment {
    border-left: 3px solid var(--accent);
    background: rgba(212, 175, 55, 0.05);
    padding: 1.5rem;
    margin-top: 2rem;
    font-style: italic;
    font-size: 0.95rem;
    color: var(--text-muted);
}

.fragment-source {
    display: block;
    margin-top: 1rem;
    font-weight: 600;
    font-style: normal;
    color: var(--accent);
    font-size: 0.8rem;
    text-transform: uppercase;
}
"""

NAV_BAR = f"""
<nav class="site-nav">
    <div class="nav-container">
        <a class="nav-logo" href="{REPO_URL}">HERMETICDB</a>
        <div class="nav-links">
            <a class="nav-link" href="{REPO_URL}/eras/late-antiquity.html">Late Antiquity</a>
            <a class="nav-link" href="{REPO_URL}/eras/medieval.html">Medieval</a>
            <a class="nav-link" href="{REPO_URL}/eras/renaissance.html">Renaissance</a>
            <div style="width:1px;height:20px;background:rgba(255,255,255,0.1)"></div>
            <a class="nav-link" href="{REPO_URL}/corpus.html" style="color:var(--accent-light); font-weight:bold">Corpus Map</a>
            <a class="nav-link" href="{REPO_URL}/texts.html">Texts</a>
            <a class="nav-link" href="{REPO_URL}/biographies.html">Biographies</a>
            <a class="nav-link" href="{REPO_URL}/scholars.html">Scholars</a>
            <a class="nav-link" href="{REPO_URL}/dictionary.html">Dictionary</a>
            <a class="nav-link" href="{REPO_URL}/timeline.html">Timeline</a>
            <a class="nav-link" href="{REPO_URL}/map.html">Interactive Map</a>
            <a class="nav-link" href="{REPO_URL}/graph.html" style="color:var(--accent); font-weight:bold">Relationship Graph</a>
            <a class="nav-link" href="{REPO_URL}/about.html">Methodology</a>
        </div>
    </div>
</nav>
"""

BASE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1"/>
    <title>{{title}} - HermeticDB</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600&family=Inter:wght@400;500&display=swap" rel="stylesheet">
    <style>
        {{css}}
    .theme-tag {
    display: inline-block;
    padding: 0.2rem 0.6rem;
    background: rgba(212, 175, 55, 0.1);
    border: 1px solid var(--border);
    border-radius: 4px;
    color: var(--accent);
    text-decoration: none;
    font-size: 0.8rem;
    margin-right: 0.5rem;
    margin-bottom: 0.5rem;
}
.theme-tag:hover {
    background: var(--accent);
    color: var(--bg);
}
</style>
</head>
<body>
    {{nav}}
    {{content}}
    <footer style="text-align:center; padding: 6rem 2rem; color: var(--text-muted); border-top: 1px solid var(--border); background: #08080a">
        &copy; 2026 The Hermetic Knowledge Portal<br/>
        <span style="font-size: 0.7rem; opacity: 0.5; margin-top: 1rem; display: block">Curated Scholar-Synthesized Narrative Database</span>
    </footer>
</body>
</html>
"""

def generate_entity_card(title, meta, desc, link):
    desc_text = italicize_terms(" ".join(desc.split()[:25]) if desc else "No short definition available") + "..."
    return f"""
    <a class="card" href="{link}">
        <div class="card-title">{italicize_terms(title)}</div>
        <div class="card-meta">{meta}</div>
        <div class="card-desc">{desc_text}</div>
    </a>
    """

def get_fragments(cursor, entity_id, entity_type):
    """Fetch corpus fragments that mention the entity or are part of the document."""
    if entity_type == "TEXT":
        # For texts, we fetch segments where the document matches
        cursor.execute("""
            SELECT s.text_content, d.title as doc_title 
            FROM corpus_segments s
            JOIN corpus_documents d ON s.doc_id = d.id
            WHERE d.doc_id = ?
            LIMIT 5
        """, (entity_id,))
    else:
        col = "persons_mentioned" if entity_type == "PERSON" else "concepts_mentioned"
        cursor.execute(f"""
            SELECT s.text_content, d.title as doc_title 
            FROM corpus_segments s
            JOIN corpus_documents d ON s.doc_id = d.id
            WHERE s.{col} LIKE ?
        """, (f"%{entity_id}%",))
    
    html = ""
    rows = cursor.fetchall()
    if rows:
        html += '<h2 style="margin-top:4rem">Scholarly Fragments</h2>'
        for row in rows:
            content = row['text_content'].strip()
            # Clean possible markdown headers in content
            content = re.sub(r'#+\s+', '', content)
            html += f"""
            <div class="scholarly-fragment">
                {content}
                <span class="fragment-source">Source: {row['doc_title']}</span>
            </div>
            """
    return html

import re

def deploy_to(target_dir, cursor):
    print(f"Deploying to {target_dir}...")
    if target_dir.exists():
        for item in target_dir.iterdir():
            if item.name in [".nojekyll", ".git"]: continue
            if item.is_dir(): shutil.rmtree(item)
            else: item.unlink()
    else:
        target_dir.mkdir(parents=True)

    (target_dir / "biographies").mkdir(exist_ok=True)
    (target_dir / "scholars").mkdir(exist_ok=True)
    (target_dir / "texts").mkdir(exist_ok=True)
    (target_dir / "eras").mkdir(exist_ok=True)
    (target_dir / "concepts").mkdir(exist_ok=True)

    # PAGE GENERATION LOGIC
    # ... (similar to previous version but with fragments integrated)
    
    # 1. BIOGRAPHIES
    cursor.execute("SELECT * FROM persons WHERE role_primary != 'SCHOLAR' OR role_primary IS NULL")
    for row in cursor.fetchall():
        pid, name, content = row['person_id'], row['name'], italicize_terms(row['bio_html'] or f"<p>{row['description']}</p>")
        fragments = italicize_terms(get_fragments(cursor, pid, "PERSON"))
        meta = f"{(row['era'] or 'Unknown').replace('_',' ')} · {row['role_primary'] or 'Figure'}"
        html = BASE_TEMPLATE.replace("{{title}}", name).replace("{{css}}", CSS).replace("{{nav}}", NAV_BAR).replace("{{content}}", f'<main class="page-container"><a href="{REPO_URL}/biographies.html" class="back-link">← Return to Archives</a><h1 class="title-large">{name}</h1><div class="card-meta" style="margin-bottom:3rem">{meta}</div><div class="prose-content">{content}{fragments}</div></main>')
        with open(target_dir / "biographies" / f"{pid}.html", "w", encoding="utf-8") as f: f.write(html)

    # 2. SCHOLARS
    cursor.execute("SELECT * FROM persons WHERE role_primary = 'SCHOLAR'")
    for row in cursor.fetchall():
        pid, name, content = row['person_id'], row['name'], italicize_terms(row['bio_html'] or f"<p>{row['description']}</p>")
        fragments = italicize_terms(get_fragments(cursor, pid, "PERSON"))
        html = BASE_TEMPLATE.replace("{{title}}", name).replace("{{css}}", CSS).replace("{{nav}}", NAV_BAR).replace("{{content}}", f'<main class="page-container"><a href="{REPO_URL}/scholars.html" class="back-link">← Return to Faculty</a><h1 class="title-large">{name}</h1><div class="card-meta" style="margin-bottom:3rem">Scholarly Authority</div><div class="prose-content">{content}{fragments}</div></main>')
        with open(target_dir / "scholars" / f"{pid}.html", "w", encoding="utf-8") as f: f.write(html)

    # 3. TEXTS
    cursor.execute("SELECT * FROM texts")
    for row in cursor.fetchall():
        tid = row['text_id']
        title = row['title']
        summary = row['analysis_html'] or row['description'] or ""
        
        # Fetch related themes
        cursor.execute("""
            SELECT c.label, c.slug FROM concepts c
            JOIN concept_text_refs r ON c.id = r.concept_id
            WHERE r.text_id = ?
        """, (row['id'],))
        themes = cursor.fetchall()
        themes_html = ""
        if themes:
            themes_html = '<div class="themes-container" style="margin-top: 2rem; padding-top: 1rem; border-top: 1px solid var(--border)">'
            themes_html += '<span style="color:var(--text-muted); font-size:0.9rem; margin-right:1rem">KEY THEMES:</span>'
            themes_html += " ".join([f'<a href="{REPO_URL}/concepts/{t[1]}.html" class="theme-tag">{t[0]}</a>' for t in themes])
            themes_html += '</div>'

        content = italicize_terms(summary)
        fragments = get_fragments(cursor, tid, "TEXT")
        
        html = BASE_TEMPLATE.replace("{{title}}", title).replace("{{css}}", CSS).replace("{{nav}}", NAV_BAR).replace("{{content}}", f'<main class="page-container"><a href="{REPO_URL}/texts.html" class="back-link">← Return to Library</a><h1 class="title-large">{title}</h1><div class="card-meta" style="margin-bottom:3rem">{row["text_type"]}</div><div class="prose-content">{content}{themes_html}{fragments}</div></main>')
        with open(target_dir / "texts" / f"{tid}.html", "w", encoding="utf-8") as f: f.write(html)

    # 4. CONCEPTS
    cursor.execute("SELECT * FROM concepts")
    for row in cursor.fetchall():
        slug, label, content = row['slug'], italicize_terms(row['label']), italicize_terms(row['definition_long'] or f"<p>{row['definition_short']}</p>")
        fragments = italicize_terms(get_fragments(cursor, slug, "CONCEPT"))
        cat_type = row['category_type'] if 'category_type' in row.keys() and row['category_type'] else 'HYBRID'
        meta_label = f"{row['category']} Concept · {cat_type.replace('_', ' ')}"
        html = BASE_TEMPLATE.replace("{{title}}", label).replace("{{css}}", CSS).replace("{{nav}}", NAV_BAR).replace("{{content}}", f'<main class="page-container"><a href="{REPO_URL}/dictionary.html" class="back-link">← Return to Dictionary</a><h1 class="title-large">{label}</h1><div class="card-meta" style="margin-bottom:3rem">{meta_label}</div><div class="prose-content">{content}{fragments}</div></main>')
        with open(target_dir / "concepts" / f"{slug}.html", "w", encoding="utf-8") as f: f.write(html)

    # 5. INDEXES
    for table, title, sub, target in [("texts", "The Emerald Library", "Canonical treatises and manuscript lineages.", "texts"),
                                      ("persons", "The Hermetic Lineage", "Sages, alchemists, and philosophers of the Thrice-Greatest.", "biographies"),
                                      ("scholars", "Modern Scholarship", "Key academic authorities and commentary traditions.", "scholars"),
                                      ("concepts", "Hermetic Dictionary", "Encyclopedic index of philosophical and alchemical concepts.", "dictionary")]:
        
        era_groups = {}
        if table == "texts":
            # We will use two top-level groups: Primary and Secondary
            era_groups["PRIMARY SOURCES"] = []
            era_groups["MODERN SCHOLARSHIP"] = []
            
            cursor.execute("SELECT * FROM texts ORDER BY text_type, title")
            for row in cursor.fetchall():
                if row['text_type'] == 'COMMENTARY':
                    era_groups["MODERN SCHOLARSHIP"].append(row)
                else:
                    era_groups["PRIMARY SOURCES"].append(row)
        elif table == "scholars":
            cursor.execute("SELECT * FROM persons WHERE role_primary = 'SCHOLAR' ORDER BY name")
            era_groups["MODERN"] = cursor.fetchall()
        elif table == "persons":
            cursor.execute("SELECT * FROM persons WHERE role_primary != 'SCHOLAR' OR role_primary IS NULL ORDER BY era, name")
            for row in cursor.fetchall():
                era = (row['era'] or "UNKNOWN").replace("_", " ")
                if era not in era_groups: era_groups[era] = []
                era_groups[era].append(row)
        elif table == "concepts":
            cursor.execute("SELECT * FROM concepts ORDER BY category, label")
            for row in cursor.fetchall():
                era = (row['category'] or "GENERAL").replace("_", " ")
                if era not in era_groups: era_groups[era] = []
                era_groups[era].append(row)

        sections_html = ""
        compact_list_html = '<div class="compact-directory" style="margin-bottom: 4rem; padding: 2rem; background: var(--bg-card); border-radius: 12px; border: 1px solid var(--border)">'
        compact_list_html += '<h3 style="margin-top:0; color:var(--accent)">Compact Directory</h3><div style="display: flex; flex-wrap: wrap; gap: 1rem;">'

        for era, rows in era_groups.items():
            cards = ""
            era_links = []
            for row in rows:
                name = row['name'] if 'name' in row.keys() else (row['title'] if 'title' in row.keys() else row['label'])
                cat_type = ""
                if table == "concepts" and 'category_type' in row.keys() and row['category_type']:
                    cat_type = f" · {row['category_type'].replace('_', ' ')}"
                
                meta = row['text_type'] if 'text_type' in row.keys() else (f"{(row['era'] or 'Unknown').replace('_',' ')} · {row['role_primary'] or 'Figure'}" if 'era' in row.keys() else f"{row['category']}{cat_type}")
                desc = row['description'] if 'description' in row.keys() else row['definition_short']
                # CLEAN PROSE
                desc = clean_prose(desc)

                target_folder = target if target != "dictionary" else "concepts"
                link = f"{REPO_URL}/{target_folder}/{row[0]}.html"
                cards += generate_entity_card(name, meta, desc, link)
                era_links.append(f'<a href="{link}" class="nav-link" style="font-size:0.9rem; padding:0.2rem 0.5rem; border:1px solid var(--border); border-radius:4px">{name}</a>')
            
            sections_html += f'<h2 class="title-medium" style="margin-top:4rem; border-bottom: 2px solid var(--accent); display:inline-block">{era}</h2><div class="grid">{cards}</div>'
            compact_list_html += f'<div style="width:100%; margin-top:1rem; font-weight:bold; color:var(--text-muted); font-size:0.8rem">{era}</div>'
            compact_list_html += "".join(era_links)

        compact_list_html += '</div></div>'
        content = f'<main class="page-container"><h1 class="title-large">{title}</h1><p class="text-subtitle" style="margin-bottom:3rem">{sub}</p>{compact_list_html}{sections_html}</main>'
        with open(target_dir / f"{target}.html", "w", encoding="utf-8") as f: f.write(BASE_TEMPLATE.replace("{{title}}", title).replace("{{css}}", CSS).replace("{{nav}}", NAV_BAR).replace("{{content}}", content))

    # 6. ERAS
    ERA_PROSE = {
        "ANTIQUITY": """
            <div class="prose-content" style="margin-bottom: 3rem; border-left: 2px solid var(--accent-light); padding-left: 2rem">
                <p>Hermeticism in Late Antiquity (c. 100–500 CE) was a diverse, living ritual and philosophical milieu centered in Roman Egypt. Following the landmark work of <b>Garth Fowden</b> and <b>Jean-Pierre Mahé</b>, we understand this period not as the work of isolated 'armchair' philosophers, but as a technical 'Way of Hermes' (<i>hermaike hodos</i>). This way involved spiritual exercises, liturgical hymns, and alchemical internalizations designed to lead the practitioner toward <i>gnosis</i> and deification.</p>
                <p>The philosophical Hermetica (like the <i>Poimandres</i>) and the technical Hermetica (astrology, alchemy, magic) were originally two sides of the same Egyptian temple coin. Figures like <b>Zosimos of Panopolis</b> prove that the boundaries between 'rational' philosophy and 'irrational' magic are modern scholarly impositions.</p>
            </div>
        """,
        "MEDIEVAL": """
            <div class="prose-content" style="margin-bottom: 3rem; border-left: 2px solid var(--accent-light); padding-left: 2rem">
                <p>The Medieval period saw the survival and expansion of Hermeticism primarily through the Islamic world. Arabic scholars integrated 'Hermes' into the prophetic lineage of Idris and Enoch, producing foundational texts like the <i>Sirr al-Khaliqa</i> (The Secret of Creation) and the <i>Picatrix</i>.</p>
                <p>In the 12th century, the translation of these Arabic texts into Latin introduced the <i>Emerald Tablet</i> and the technical Hermetica to Europe, influencing theologians like <b>Albertus Magnus</b> and <b>Roger Bacon</b>. This 'Medieval Hermetica' laid the structural groundwork for the more famous Renaissance 'rediscovery'.</p>
            </div>
        """,
        "RENAISSANCE": """
            <div class="prose-content" style="margin-bottom: 3rem; border-left: 2px solid var(--accent-light); padding-left: 2rem">
                <p>The Renaissance (c. 1460–1600) represents the 'golden age' of Western Hermeticism, initiated by <b>Marsilio Ficino's</b> translation of the <i>Corpus Hermeticum</i> into Latin. This period saw the synthesis of Hermeticism with Christian Kabbalah, Neoplatonism, and humanism.</p>
                <p>Figures like <b>Pico della Mirandola</b> and <b>Giordano Bruno</b> utilized the 'Yates Paradigm' of the active magus to challenge traditional scholasticism, while <b>Cornelius Agrippa</b> provided the definitive synthesis of 'Occult Philosophy' that would define the era's magical worldview.</p>
            </div>
        """
    }

    for era_id, era_name in [("late-antiquity", "Late Antiquity"), ("medieval", "Medieval"), ("renaissance", "Renaissance"), ("early-modern", "Early Modern"), ("modern", "Modern")]:
        db_era = "ANTIQUITY" if era_id == "late-antiquity" else era_id.upper().replace("-", "_")
        cursor.execute("SELECT * FROM persons WHERE era = ? ORDER BY name", (db_era,))
        era_cards = ""
        for row in cursor.fetchall():
            era_cards += generate_entity_card(row['name'], row['role_primary'], row['description'], f"{REPO_URL}/biographies/{row['person_id']}.html")
        prose = ERA_PROSE.get(db_era, "")
        content = f'<main class="page-container"><h1 class="title-large">{era_name} Archives</h1><p class="text-subtitle">Figures and manuscripts of the {era_name} period.</p>{prose}<div class="grid">{era_cards}</div></main>'
        with open(target_dir / "eras" / f"{era_id}.html", "w", encoding="utf-8") as f: f.write(BASE_TEMPLATE.replace("{{title}}", era_name).replace("{{css}}", CSS).replace("{{nav}}", NAV_BAR).replace("{{content}}", content))

    # 6.5. TIMELINE
    cursor.execute("SELECT * FROM timeline_events ORDER BY year ASC")
    timeline_cards = ""
    for row in cursor.fetchall():
        year_str = str(row['year'])
        if row['year_end']:
            year_str += f" - {row['year_end']}"
        meta = f"{year_str} · {row['event_type'] or 'EVENT'}"
        desc = row['description_long'] or f"<p>{row['description']}</p>"
        
        timeline_cards += f"""
        <div class="card" style="margin-bottom: 1rem;">
            <div class="card-title">{row['title']}</div>
            <div class="card-meta">{meta}</div>
            <div class="prose-content" style="padding: 1rem; margin-top: 1rem; border: none; background: rgba(0,0,0,0.2);">{desc}</div>
        </div>
        """
    content = f'<main class="page-container"><h1 class="title-large">Timeline of Hermeticism</h1><p class="text-subtitle">Key events, publications, and movements.</p><div style="display:flex;flex-direction:column;gap:1rem;">{timeline_cards}</div></main>'
    with open(target_dir / "timeline.html", "w", encoding="utf-8") as f: f.write(BASE_TEMPLATE.replace("{{title}}", "Timeline").replace("{{css}}", CSS).replace("{{nav}}", NAV_BAR).replace("{{content}}", content))

    # 6.6 ABOUT / METHODOLOGY PAGE
    about_content = f"""
    <main class="page-container">
        <h1 class="title-large">Methodology & Scope</h1>
        <div class="prose-content">
            <h2>Historiographical Principles</h2>
            <p>Following the methodology established by Wouter J. Hanegraaff in the <i>Dictionary of Gnosis & Western Esotericism</i>, this database maintains a strict terminological self-awareness. We differentiate between <b>Actor Terms</b> (words used by historical figures, e.g., <i>prisca theologia</i>) and <b>Analyst Terms</b> (retrospective scholarly categories, e.g., <i>Hermeticism</i>, <i>Esotericism</i>).</p>
            <h2>The "Reification" Problem</h2>
            <p>We explicitly reject the "reification" of magic and esotericism into coherent, bounded traditions. Instead, our biographical and conceptual entries embrace the multi-dimensionality and contradictions of historical actors. A figure like Marsilio Ficino is presented not just within a "tradition box," but as a complex actor embedded in theological, political, and medical contexts.</p>
            <h2>Pragmatic Scope</h2>
            <p>Our corpus centers on the transmission of the Greco-Egyptian Hermetica through the Islamic world into the Latin West. While we recognize the profound importance of overlapping traditions (like Kabbalah and indigenous Arabic magic), our primary focus remains tethered to the lineage of texts directly engaging with the figure of Hermes Trismegistus, largely aligned with Brian P. Copenhaver's translation of the <i>Corpus Hermeticum</i>.</p>
            <h2>Zero-Loss Provenance</h2>
            <p>Every claim in this database is strictly tied to a primary or secondary source, allowing scholars to trace the exact lineage of any assertion back to its original academic or historical text.</p>
        </div>
    </main>
    """
    with open(target_dir / "about.html", "w", encoding="utf-8") as f: f.write(BASE_TEMPLATE.replace("{{title}}", "Methodology").replace("{{css}}", CSS).replace("{{nav}}", NAV_BAR).replace("{{content}}", about_content))

    # 6.7 HERMETIC CORPUS MAP
    cursor.execute("SELECT * FROM texts WHERE transmission_notes = 'THEOLOGICAL_HERMETICA' ORDER BY title")
    theo_cards = ""
    for row in cursor.fetchall():
        theo_cards += generate_entity_card(row['title'], "Theological Hermetica", row['description'], f"{REPO_URL}/texts/{row['text_id']}.html")
    
    cursor.execute("SELECT * FROM texts WHERE transmission_notes = 'TECHNICAL_HERMETICA' ORDER BY title")
    tech_cards = ""
    for row in cursor.fetchall():
        tech_cards += generate_entity_card(row['title'], "Technical Hermetica", row['description'], f"{REPO_URL}/texts/{row['text_id']}.html")
    
    corpus_content = f"""
    <main class="page-container">
        <h1 class="title-large">The Hermetic Corpus Map</h1>
        <p class="text-subtitle">A topographical guide to the Theological and Technical Hermetica.</p>
        
        <h2 style="color:var(--accent); margin-top:4rem; border-bottom: 1px solid var(--border); padding-bottom: 1rem">I. Theological Hermetica (Philosophical)</h2>
        <p class="text-muted" style="margin-bottom: 2rem">Treatises focused on the nature of God (Nous), the soul's ascent, and the spiritual rebirth of the practitioner.</p>
        <div class="grid">{theo_cards}</div>
        
        <h2 style="color:var(--accent); margin-top:6rem; border-bottom: 1px solid var(--border); padding-bottom: 1rem">II. Technical Hermetica (Practical)</h2>
        <p class="text-muted" style="margin-bottom: 2rem">Writings attributed to Hermes concerning the practical sciences of alchemy, astrology, and natural magic (sympatheia).</p>
        <div class="grid">{tech_cards}</div>
    </main>
    """
    with open(target_dir / "corpus.html", "w", encoding="utf-8") as f: f.write(BASE_TEMPLATE.replace("{{title}}", "Corpus Map").replace("{{css}}", CSS).replace("{{nav}}", NAV_BAR).replace("{{content}}", corpus_content))

    # 6.8 INTERACTIVE MAP
    cursor.execute("SELECT * FROM locations")
    locs = cursor.fetchall()
    loc_js_objects = []
    for l in locs:
        loc_js_objects.append(f'{{ "label": "{l["label"]}", "lat": {l["lat"]}, "lng": {l["lng"]}, "desc": "{l["description"]}" }}')
    
    loc_js_array = "[" + ",".join(loc_js_objects) + "]"
    
    map_content = f"""
    <main class="page-container">
        <h1 class="title-large">Interactive Geography of Hermeticism</h1>
        <p class="text-subtitle">Major centers of transmission, translation, and practice.</p>
        <div id="map" style="height: 600px; border-radius: 12px; border: 1px solid var(--border); background: var(--bg-card);"></div>
        
        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin=""/>
        <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>
        
        <script>
            document.addEventListener('DOMContentLoaded', function() {{
                const map = L.map('map').setView([35, 20], 3);
                L.tileLayer('https://{{s}}.basemaps.cartocdn.com/dark_all/{{z}}/{{x}}/{{y}}{{r}}.png', {{
                    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>'
                }}).addTo(map);

                const locations = {loc_js_array};
                
                const hermeticIcon = L.divIcon({{
                    className: 'hermetic-marker',
                    html: '<div style="width:12px; height:12px; background:var(--accent); border:2px solid #fff; border-radius:50%; box-shadow: 0 0 10px var(--accent);"></div>',
                    iconSize: [12, 12]
                }});

                locations.forEach(loc => {{
                    L.marker([loc.lat, loc.lng], {{icon: hermeticIcon}})
                        .addTo(map)
                        .bindPopup(`<b>${{loc.label}}</b><br><br>${{loc.desc}}`, {{
                            className: 'hermetic-popup'
                        }});
                }});
            }});
        </script>
        <style>
            .hermetic-popup .leaflet-popup-content-wrapper {{
                background: var(--bg-card);
                color: var(--text-main);
                border: 1px solid var(--border);
                font-family: var(--font-body);
            }}
            .hermetic-popup .leaflet-popup-tip {{
                background: var(--bg-card);
            }}
        </style>
    </main>
    """
    with open(target_dir / "map.html", "w", encoding="utf-8") as f: f.write(BASE_TEMPLATE.replace("{{title}}", "Interactive Map").replace("{{css}}", CSS).replace("{{nav}}", NAV_BAR).replace("{{content}}", map_content))

    # 6.9 RELATIONSHIP GRAPH (D3.JS)
    nodes = []
    links = []
    
    # 1. PERSONS
    cursor.execute("SELECT person_id, name, role_primary FROM persons")
    for r in cursor.fetchall():
        nodes.append({ "id": r[0], "label": r[1], "group": "PERSON", "role": r[2] })
    
    # 2. TEXTS
    cursor.execute("SELECT text_id, title, text_type FROM texts")
    for r in cursor.fetchall():
        nodes.append({ "id": r[0], "label": r[1], "group": "TEXT", "role": r[2] })
    
    # 3. CONCEPTS
    cursor.execute("SELECT slug, label, category FROM concepts")
    for r in cursor.fetchall():
        nodes.append({ "id": r[0], "label": r[1], "group": "CONCEPT", "role": r[2] })
    
    # 4. EDGES (Person <-> Text)
    cursor.execute("SELECT person_id, text_id, rel_type FROM person_text_refs")
    for r in cursor.fetchall():
        links.append({ "source": r[0], "target": r[1], "value": 2, "type": r[2] })
    
    # 5. EDGES (Concept <-> Text)
    cursor.execute("""
        SELECT c.slug, t.text_id 
        FROM concept_text_refs r
        JOIN concepts c ON r.concept_id = c.id
        JOIN texts t ON r.text_id = t.id
    """)
    for r in cursor.fetchall():
        links.append({ "source": r[0], "target": r[1], "value": 1, "type": "THEME" })

    # 6. EDGES (Person <-> Person)
    cursor.execute("SELECT person_a, person_b, rel_type FROM person_person_refs")
    for r in cursor.fetchall():
        links.append({ "source": r[0], "target": r[1], "value": 3, "type": r[2] })

    # 7. EDGES (Text <-> Text)
    cursor.execute("SELECT text_a, text_b, rel_type FROM text_text_refs")
    for r in cursor.fetchall():
        links.append({ "source": r[0], "target": r[1], "value": 3, "type": r[2] })

    import json
    graph_data = { "nodes": nodes, "links": links }
    
    graph_content = f"""
    <main class="page-container" style="max-width: 100%; padding: 0;">
        <div style="padding: 4rem 2rem 1rem 2rem">
            <h1 class="title-large">Hermetic Relationship Graph</h1>
            <p class="text-subtitle">Visualizing the connections between sages, treatises, and concepts.</p>
        </div>
        
        <div id="graph-container" style="width: 100%; height: 80vh; background: var(--bg-card); border-top: 1px solid var(--border); position: relative; overflow: hidden;">
            <div id="graph-info" style="position: absolute; top: 20px; left: 20px; background: rgba(0,0,0,0.8); padding: 1rem; border: 1px solid var(--border); border-radius: 8px; z-index: 10; max-width: 300px; display:none">
                <h3 id="info-title" style="color:var(--accent); margin:0"></h3>
                <p id="info-type" style="font-size:0.8rem; color:var(--text-muted); margin: 0.5rem 0"></p>
                <p id="info-desc" style="font-size:0.9rem; margin:0"></p>
            </div>
            <svg id="network-graph" style="width:100%; height:100%"></svg>
        </div>

        <script src="https://d3js.org/d3.v7.min.js"></script>
        <script>
            const data = {json.dumps(graph_data)};
            const svg = d3.select("#network-graph");
            const width = window.innerWidth;
            const height = window.innerHeight * 0.8;
            
            const simulation = d3.forceSimulation(data.nodes)
                .force("link", d3.forceLink(data.links).id(d => d.id).distance(100))
                .force("charge", d3.forceManyBody().strength(-300))
                .force("center", d3.forceCenter(width / 2, height / 2))
                .force("x", d3.forceX(width / 2).strength(0.1))
                .force("y", d3.forceY(height / 2).strength(0.1));

            const link = svg.append("g")
                .attr("stroke", "rgba(255,255,255,0.1)")
                .attr("stroke-opacity", 0.6)
                .selectAll("line")
                .data(data.links)
                .join("line")
                .attr("stroke-width", d => Math.sqrt(d.value));

            const node = svg.append("g")
                .selectAll("g")
                .data(data.nodes)
                .join("g")
                .call(drag(simulation))
                .on("mouseover", (event, d) => {{
                    d3.select("#graph-info").style("display", "block");
                    d3.select("#info-title").text(d.label);
                    d3.select("#info-type").text(d.group + " · " + (d.role || ""));
                    
                    // Show connections in info box
                    const connections = data.links
                        .filter(l => l.source.id === d.id || l.target.id === d.id)
                        .map(l => {{
                            const other = l.source.id === d.id ? l.target : l.source;
                            return `<li><b>${{l.type}}</b>: ${{other.label}}</li>`;
                        }})
                        .join("");
                    d3.select("#info-desc").html(`<ul style="list-style:none; padding:0; margin:1rem 0">${{connections}}</ul>`);

                    // Highlight connections
                    link.style("stroke", l => (l.source.id === d.id || l.target.id === d.id) ? "var(--accent)" : "rgba(255,255,255,0.1)")
                        .style("stroke-opacity", l => (l.source.id === d.id || l.target.id === d.id) ? 1 : 0.1);
                }})
                .on("mouseout", () => {{
                    // d3.select("#graph-info").style("display", "none");
                    link.style("stroke", "rgba(255,255,255,0.1)").style("stroke-opacity", 0.6);
                }});

            node.append("circle")
                .attr("r", d => d.group === "PERSON" ? 8 : (d.group === "TEXT" ? 6 : 4))
                .attr("fill", d => {{
                    if (d.group === "PERSON") return "#4a9eff";
                    if (d.group === "TEXT") return "#d4af37";
                    return "#20c997";
                }})
                .attr("stroke", "#fff")
                .attr("stroke-width", 1.5);

            node.append("text")
                .attr("x", 12)
                .attr("y", 4)
                .text(d => d.label)
                .attr("fill", "#fff")
                .style("font-size", "10px")
                .style("pointer-events", "none")
                .style("opacity", 0.7);

            simulation.on("tick", () => {{
                link
                    .attr("x1", d => d.source.x)
                    .attr("y1", d => d.source.y)
                    .attr("x2", d => d.target.x)
                    .attr("y2", d => d.target.y);

                node
                    .attr("transform", d => `translate(${{d.x}}, ${{d.y}})`);
            }});

            function drag(simulation) {{
                function dragstarted(event) {{
                    if (!event.active) simulation.alphaTarget(0.3).restart();
                    event.subject.fx = event.subject.x;
                    event.subject.fy = event.subject.y;
                }}
                
                function dragged(event) {{
                    event.subject.fx = event.x;
                    event.subject.fy = event.y;
                }}
                
                function dragended(event) {{
                    if (!event.active) simulation.alphaTarget(0);
                    event.subject.fx = null;
                    event.subject.fy = null;
                }}
                
                return d3.drag()
                    .on("start", dragstarted)
                    .on("drag", dragged)
                    .on("end", dragended);
            }}
        </script>
    </main>
    """
    with open(target_dir / "graph.html", "w", encoding="utf-8") as f: f.write(BASE_TEMPLATE.replace("{{title}}", "Relationship Graph").replace("{{css}}", CSS).replace("{{nav}}", NAV_BAR).replace("{{content}}", graph_content))

    # 7. LANDING PAGE
    landing_content = f"""
    <main class="page-container" style="text-align:center; padding-top: 8rem">
        <h1 style="font-family: var(--font-display); font-size: 5rem; color: var(--accent-light); margin-bottom: 0.5rem; letter-spacing: -2px">Hermetic Knowledge Portal</h1>
        <p style="color: var(--accent); font-size: 1.5rem; text-transform: uppercase; letter-spacing: 5px; margin-bottom: 4rem">The Emerald Tablet Database</p>
        <div class="grid" style="margin-top: 6rem">
            <a class="card" href="{REPO_URL}/eras/late-antiquity.html">
                <div class="card-title">Late Antiquity</div>
                <div class="card-desc">Greco-Egyptian origins and the birth of the Corpus Hermeticum.</div>
            </a>
            <a class="card" href="{REPO_URL}/eras/medieval.html">
                <div class="card-title">Medieval</div>
                <div class="card-desc">The Arabic tradition and the Latin alchemy of the High Middle Ages.</div>
            </a>
            <a class="card" href="{REPO_URL}/eras/renaissance.html">
                <div class="card-title">Renaissance</div>
                <div class="card-desc">Ficino, the Florentine Academy, and the Prisca Theologia.</div>
            </a>
        </div>
    </main>
    """
    with open(target_dir / "index.html", "w", encoding="utf-8") as f:
        f.write(BASE_TEMPLATE.replace("{{title}}", "Home").replace("{{css}}", CSS).replace("{{nav}}", NAV_BAR).replace("{{content}}", landing_content))

def main():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    # Dual Deployment to fix 404s
    deploy_to(DOCS_DIR, cursor)
    deploy_to(SITE_DIR, cursor)
    
    conn.close()
    print("Dual Deployment complete.")

if __name__ == "__main__":
    main()
