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

def italicize_terms(text):
    if not text:
        return text
    for term in sorted(ITALIC_TERMS, key=len, reverse=True):
        pattern = r'(?<![<\w/])(' + re.escape(term) + r')(?![>\w/])'
        text = re.sub(pattern, r'<em>\1</em>', text)
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
            <a class="nav-link" href="{REPO_URL}/texts.html">Texts</a>
            <a class="nav-link" href="{REPO_URL}/biographies.html">Biographies</a>
            <a class="nav-link" href="{REPO_URL}/scholars.html">Scholars</a>
            <a class="nav-link" href="{REPO_URL}/dictionary.html">Dictionary</a>
            <a class="nav-link" href="{REPO_URL}/timeline.html">Timeline</a>
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
    """Fetch corpus fragments that mention the entity."""
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
        tid, title, content = row['text_id'], italicize_terms(row['title']), italicize_terms(row['analysis_html'] or f"<p>{row['description']}</p>")
        html = BASE_TEMPLATE.replace("{{title}}", title).replace("{{css}}", CSS).replace("{{nav}}", NAV_BAR).replace("{{content}}", f'<main class="page-container"><a href="{REPO_URL}/texts.html" class="back-link">← Return to Library</a><h1 class="title-large">{title}</h1><div class="card-meta" style="margin-bottom:3rem">{row["text_type"]}</div><div class="prose-content">{content}</div></main>')
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
        if table == "texts": cursor.execute("SELECT * FROM texts ORDER BY title")
        elif table == "scholars": cursor.execute("SELECT * FROM persons WHERE role_primary = 'SCHOLAR' ORDER BY name")
        elif table == "persons": cursor.execute("SELECT * FROM persons WHERE role_primary != 'SCHOLAR' OR role_primary IS NULL ORDER BY name")
        elif table == "concepts": cursor.execute("SELECT * FROM concepts ORDER BY label")
            
        cards = ""
        for row in cursor.fetchall():
            name = row['name'] if 'name' in row.keys() else (row['title'] if 'title' in row.keys() else row['label'])
            cat_type = ""
            if table == "concepts" and 'category_type' in row.keys() and row['category_type']:
                cat_type = f" · {row['category_type'].replace('_', ' ')}"
            meta = row['text_type'] if 'text_type' in row.keys() else (f"{(row['era'] or 'Unknown').replace('_',' ')} · {row['role_primary'] or 'Figure'}" if 'era' in row.keys() else f"{row['category']}{cat_type}")
            desc = row['description'] if 'description' in row.keys() else row['definition_short']
            target_folder = target if target != "dictionary" else "concepts"
            link = f"{REPO_URL}/{target_folder}/{row[0]}.html"
            cards += generate_entity_card(name, meta, desc, link)
        content = f'<main class="page-container"><h1 class="title-large">{title}</h1><p class="text-subtitle">{sub}</p><div class="grid">{cards}</div></main>'
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
