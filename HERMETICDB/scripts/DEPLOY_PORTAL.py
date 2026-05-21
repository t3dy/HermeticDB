import sqlite3
import os
import shutil
import re
import json
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
    replacements = {
        "Â·": "·",
        "â†": "←",
        "â€“": "-",
        "â€”": "-",
        "Ã©": "é",
        "Ã¨": "è",
        "Ã§": "ç",
        "Ã¼": "ü",
        "Ã¶": "ö",
    }
    for bad, good in replacements.items():
        text = text.replace(bad, good)
    text = re.sub(r'</?(?:ol|ul)[^>]*>', '', text)
    text = re.sub(r'<li[^>]*>\s*(.*?)\s*</li>', r'<p>\1</p>', text, flags=re.IGNORECASE | re.DOTALL)
    # Strip hashtags, brackets, and other code-like artifacts
    text = re.sub(r'[#\[\]{}*]', '', text)
    # Ensure it's treated as a single block of prose
    return text.strip()

def clean_inline(text):
    if not text:
        return ""
    return clean_prose(str(text))

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
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
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
            <a class="nav-link" href="{REPO_URL}/debates.html">Debates</a>
            <a class="nav-link" href="{REPO_URL}/timeline.html">Timeline</a>
            <a class="nav-link" href="{REPO_URL}/map.html">Interactive Map</a>
            <a class="nav-link" href="{REPO_URL}/graph.html" style="color:var(--accent); font-weight:bold">Relationship Graph</a>
            <a class="nav-link" href="{REPO_URL}/about.html">Methodology</a>
            <button id="gs-btn" title="Search (press /)"
                style="background:none;border:1px solid var(--border);color:var(--text-muted);border-radius:6px;
                       padding:0.3rem 0.7rem;font-size:1rem;cursor:pointer;transition:all 0.2s;line-height:1"
                onmouseover="this.style.borderColor='var(--accent)';this.style.color='var(--accent)'"
                onmouseout="this.style.borderColor='var(--border)';this.style.color='var(--text-muted)'">⌕</button>
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

    <!-- Back-to-top -->
    <button id="btt" onclick="window.scrollTo({{top:0,behavior:'smooth'}})"
        style="display:none;position:fixed;bottom:2rem;right:2rem;z-index:500;background:var(--bg-card);
               border:1px solid var(--border);color:var(--accent);border-radius:50%;width:44px;height:44px;
               font-size:1.2rem;cursor:pointer;transition:all 0.2s;box-shadow:0 4px 16px rgba(0,0,0,0.4)">↑</button>
    <script>
    (function(){{
        var btn = document.getElementById('btt');
        window.addEventListener('scroll', function(){{
            btn.style.display = window.scrollY > 400 ? 'block' : 'none';
        }}, {{passive:true}});
    }})();
    </script>

    <!-- Global search overlay -->
    <div id="gs-overlay" style="display:none;position:fixed;inset:0;z-index:9999;background:rgba(0,0,0,0.87);backdrop-filter:blur(6px);padding:8vh 2rem 2rem">
        <div style="max-width:680px;margin:0 auto">
            <div style="position:relative;margin-bottom:1.2rem">
                <span style="position:absolute;left:1.1rem;top:50%;transform:translateY(-50%);color:var(--accent);font-size:1.2rem;pointer-events:none">⌕</span>
                <input id="gs-input" type="text" placeholder="Search persons, texts, concepts…" autocomplete="off"
                    style="width:100%;box-sizing:border-box;background:#141418;border:1px solid rgba(212,175,55,0.5);
                           color:#e0e0e0;font-size:1.2rem;padding:0.9rem 3rem 0.9rem 3rem;border-radius:12px;
                           font-family:Inter,sans-serif;outline:none">
                <button onclick="gsClose()" style="position:absolute;right:1rem;top:50%;transform:translateY(-50%);
                    background:none;border:none;color:#a0a0a0;font-size:1.3rem;cursor:pointer;line-height:1">✕</button>
            </div>
            <div id="gs-results" style="max-height:58vh;overflow-y:auto;border-radius:8px"></div>
            <div style="margin-top:0.8rem;font-size:0.75rem;color:#444;text-align:center">Press <kbd style="background:#222;border:1px solid #444;padding:0.1rem 0.4rem;border-radius:3px">/</kbd> to open &nbsp;·&nbsp; <kbd style="background:#222;border:1px solid #444;padding:0.1rem 0.4rem;border-radius:3px">Esc</kbd> to close</div>
        </div>
    </div>

    <!-- Hover preview card -->
    <div id="hc-card" style="display:none;position:fixed;z-index:8888;max-width:310px;background:#141418;
        border:1px solid rgba(212,175,55,0.35);border-radius:10px;padding:1rem 1.2rem;
        pointer-events:none;box-shadow:0 8px 32px rgba(0,0,0,0.65)">
        <div id="hc-label" style="font-family:Outfit,sans-serif;font-size:1rem;color:#f1d37e;font-weight:600;margin-bottom:0.25rem"></div>
        <div id="hc-meta" style="font-size:0.7rem;color:var(--accent);text-transform:uppercase;letter-spacing:0.08em;margin-bottom:0.5rem"></div>
        <div id="hc-desc" style="font-size:0.85rem;color:#a8a8a8;line-height:1.5"></div>
        <div style="margin-top:0.6rem;font-size:0.72rem;color:#444;font-style:italic">click for full entry</div>
    </div>

    <script>
    (function(){{
        var REPO = '{REPO_URL}';
        var idx = null;

        function loadIdx(cb) {{
            if (idx) return cb(idx);
            fetch(REPO + '/search_index.json')
                .then(function(r){{ return r.json(); }})
                .then(function(d){{ idx = d; cb(d); }})
                .catch(function(){{ idx = []; cb([]); }});
        }}

        // --- GLOBAL SEARCH ---
        var overlay = document.getElementById('gs-overlay');
        var gsInput = document.getElementById('gs-input');
        var gsResults = document.getElementById('gs-results');
        var TYPE_COLOR = {{ PERSON: '#4a9eff', TEXT: '#d4af37', CONCEPT: '#20c997' }};

        window.gsClose = function() {{ overlay.style.display = 'none'; }};
        function gsOpen() {{ overlay.style.display = 'block'; gsInput.focus(); gsInput.select(); }}

        document.addEventListener('keydown', function(e){{
            if (e.key === '/' && document.activeElement.tagName !== 'INPUT' && document.activeElement.tagName !== 'TEXTAREA') {{
                e.preventDefault(); gsOpen();
            }}
            if (e.key === 'Escape') gsClose();
        }});
        overlay.addEventListener('click', function(e){{ if (e.target === overlay) gsClose(); }});

        var gsBtn = document.getElementById('gs-btn');
        if (gsBtn) gsBtn.addEventListener('click', gsOpen);

        function renderResults(items) {{
            if (!items.length) {{
                gsResults.innerHTML = '<p style="color:#555;text-align:center;padding:2rem 0">No matches found</p>';
                return;
            }}
            gsResults.innerHTML = items.slice(0, 14).map(function(r){{
                var c = TYPE_COLOR[r.type] || '#888';
                return '<a href="' + r.url + '" onclick="gsClose()" style="display:block;padding:0.8rem 1rem;margin-bottom:0.3rem;background:#1a1a20;'
                    + 'border:1px solid rgba(255,255,255,0.05);border-radius:8px;text-decoration:none;transition:border-color 0.15s" '
                    + 'onmouseover="this.style.borderColor=\'rgba(212,175,55,0.4)\'" onmouseout="this.style.borderColor=\'rgba(255,255,255,0.05)\'">'
                    + '<span style="display:inline-block;padding:0.12rem 0.45rem;background:' + c + '22;color:' + c + ';border-radius:4px;font-size:0.68rem;text-transform:uppercase;letter-spacing:0.07em;margin-right:0.4rem">' + r.type + '</span>'
                    + '<strong style="color:#e0e0e0">' + r.label + '</strong>'
                    + '<span style="display:block;color:#777;font-size:0.8rem;margin-top:0.25rem">' + (r.desc || '').slice(0, 100) + (r.desc && r.desc.length > 100 ? '…' : '') + '</span>'
                    + '</a>';
            }}).join('');
        }}

        var gsTimer;
        gsInput.addEventListener('input', function(){{
            clearTimeout(gsTimer);
            var q = this.value.trim().toLowerCase();
            if (!q) {{ gsResults.innerHTML = ''; return; }}
            gsTimer = setTimeout(function(){{
                loadIdx(function(data){{
                    var hits = data.filter(function(r){{
                        return r.label.toLowerCase().indexOf(q) !== -1 || (r.desc && r.desc.toLowerCase().indexOf(q) !== -1);
                    }}).sort(function(a, b){{
                        var al = a.label.toLowerCase().indexOf(q) === 0 ? 0 : 1;
                        var bl = b.label.toLowerCase().indexOf(q) === 0 ? 0 : 1;
                        return al - bl;
                    }});
                    renderResults(hits);
                }});
            }}, 150);
        }});

        // --- HOVER PREVIEW ---
        var hcCard = document.getElementById('hc-card');
        var hcLabel = document.getElementById('hc-label');
        var hcMeta = document.getElementById('hc-meta');
        var hcDesc = document.getElementById('hc-desc');
        var hcTimer;
        var PATHS = ['/biographies/', '/scholars/', '/dictionary/', '/concepts/', '/texts/'];

        function slugFromHref(href) {{
            var m = href.match(/\\/([^\\/]+)\\.html$/);
            return m ? m[1] : null;
        }}

        document.addEventListener('mouseover', function(e){{
            var a = e.target.closest('a[href]');
            if (!a) return;
            var href = a.getAttribute('href') || '';
            if (!PATHS.some(function(p){{ return href.indexOf(p) !== -1; }})) return;
            var slug = slugFromHref(href);
            if (!slug) return;
            clearTimeout(hcTimer);
            hcTimer = setTimeout(function(){{
                loadIdx(function(data){{
                    var entry = null;
                    for (var i = 0; i < data.length; i++) {{
                        if (data[i].id === slug) {{ entry = data[i]; break; }}
                    }}
                    if (!entry) return;
                    hcLabel.textContent = entry.label;
                    hcMeta.textContent = entry.meta;
                    hcDesc.textContent = (entry.desc || '').slice(0, 130) + ((entry.desc && entry.desc.length > 130) ? '…' : '');
                    var rect = a.getBoundingClientRect();
                    var left = Math.min(rect.left + window.scrollX, window.innerWidth - 330);
                    hcCard.style.left = Math.max(8, left) + 'px';
                    hcCard.style.top = (rect.bottom + window.scrollY + 8) + 'px';
                    hcCard.style.display = 'block';
                }});
            }}, 280);
        }});

        document.addEventListener('mouseout', function(e){{
            var a = e.target.closest('a[href]');
            if (!a) return;
            clearTimeout(hcTimer);
            hcCard.style.display = 'none';
        }});
    }})();
    </script>
</body>
</html>
"""

ERA_STRIPE = {
    "ANTIQUITY": "#d4af37",
    "MEDIEVAL": "#20c997",
    "RENAISSANCE": "#e67e22",
    "EARLY MODERN": "#9b59b6",
    "MODERN": "#4a9eff",
}

SOURCE_BADGE = {
    "PRIMARY_SOURCE": ('<span style="display:inline-block;padding:0.15rem 0.5rem;background:rgba(212,175,55,0.15);'
                       'color:#d4af37;border-radius:4px;font-size:0.7rem;font-weight:600;text-transform:uppercase;'
                       'letter-spacing:0.06em;margin-bottom:0.5rem">Primary Source</span><br>'),
    "SCHOLARSHIP":    ('<span style="display:inline-block;padding:0.15rem 0.5rem;background:rgba(74,158,255,0.15);'
                       'color:#4a9eff;border-radius:4px;font-size:0.7rem;font-weight:600;text-transform:uppercase;'
                       'letter-spacing:0.06em;margin-bottom:0.5rem">Scholarship</span><br>'),
    "COMMENTARY":     ('<span style="display:inline-block;padding:0.15rem 0.5rem;background:rgba(74,158,255,0.12);'
                       'color:#4a9eff;border-radius:4px;font-size:0.7rem;font-weight:600;text-transform:uppercase;'
                       'letter-spacing:0.06em;margin-bottom:0.5rem">Commentary</span><br>'),
}

TERM_BADGE = {
    "ACTOR_TERM":   ('<span style="display:inline-block;padding:0.15rem 0.5rem;background:rgba(32,201,151,0.15);'
                     'color:#20c997;border-radius:4px;font-size:0.7rem;font-weight:600;text-transform:uppercase;'
                     'letter-spacing:0.06em;margin-bottom:0.5rem">Actor Term</span><br>'),
    "ANALYST_TERM": ('<span style="display:inline-block;padding:0.15rem 0.5rem;background:rgba(155,89,182,0.15);'
                     'color:#9b59b6;border-radius:4px;font-size:0.7rem;font-weight:600;text-transform:uppercase;'
                     'letter-spacing:0.06em;margin-bottom:0.5rem">Analyst Term</span><br>'),
    "HYBRID":       ('<span style="display:inline-block;padding:0.15rem 0.5rem;background:rgba(149,165,166,0.15);'
                     'color:#95a5a6;border-radius:4px;font-size:0.7rem;font-weight:600;text-transform:uppercase;'
                     'letter-spacing:0.06em;margin-bottom:0.5rem">Hybrid</span><br>'),
}

def generate_entity_card(title, meta, desc, link, data_attrs=None):
    if not desc or len(desc.strip()) < 20:
        desc_text = "<em style='color:var(--text-muted)'>Entry in progress — check back soon.</em>"
    else:
        desc_text = clean_inline(" ".join(desc.split()[:30])) + "…"
    attrs_str = ""
    badge = ""
    era_color = None
    if data_attrs:
        term_type = data_attrs.get("termtype", "")
        text_type = data_attrs.get("type", "")
        era_val = data_attrs.get("era", "")
        badge = TERM_BADGE.get(term_type, "") or SOURCE_BADGE.get(text_type, "")
        era_color = ERA_STRIPE.get(era_val)
        attrs_str = " ".join(f'data-{k}="{v}"' for k, v in data_attrs.items())
    stripe = f'border-left-color:{era_color}' if era_color else ''
    return f"""
    <a class="card" href="{link}" {attrs_str} style="{stripe}">
        {badge}<div class="card-title">{clean_inline(title)}</div>
        <div class="card-meta">{meta}</div>
        <div class="card-desc">{desc_text}</div>
    </a>
    """


FILTER_CSS = """
.filter-bar {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.5rem 2rem;
    margin-bottom: 2.5rem;
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    align-items: center;
}
.filter-bar-label {
    font-size: 0.75rem;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.1em;
    white-space: nowrap;
    margin-right: 0.5rem;
}
.filter-group {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    align-items: center;
}
.filter-btn {
    background: transparent;
    border: 1px solid var(--border);
    color: var(--text-muted);
    border-radius: 20px;
    padding: 0.3rem 0.9rem;
    font-size: 0.78rem;
    font-family: var(--font-body);
    cursor: pointer;
    transition: all 0.2s;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}
.filter-btn:hover { border-color: var(--accent); color: var(--accent); }
.filter-btn.active {
    background: var(--accent);
    border-color: var(--accent);
    color: #000;
    font-weight: 600;
}
.filter-search {
    background: var(--bg);
    border: 1px solid var(--border);
    color: var(--text-main);
    border-radius: 8px;
    padding: 0.4rem 0.9rem;
    font-size: 0.9rem;
    font-family: var(--font-body);
    flex: 1;
    min-width: 180px;
    max-width: 300px;
    outline: none;
    transition: border-color 0.2s;
}
.filter-search:focus { border-color: var(--accent); }
.filter-search::placeholder { color: var(--text-muted); }
.sort-btn {
    background: transparent;
    border: 1px solid var(--border);
    color: var(--text-muted);
    border-radius: 6px;
    padding: 0.3rem 0.7rem;
    font-size: 0.75rem;
    font-family: var(--font-body);
    cursor: pointer;
    transition: all 0.2s;
}
.sort-btn:hover, .sort-btn.active { border-color: var(--accent); color: var(--accent); }
.filter-count {
    font-size: 0.8rem;
    color: var(--text-muted);
    margin-left: auto;
    white-space: nowrap;
}
.section-header { transition: opacity 0.2s; }
.section-header.hidden { display: none; }
"""

FILTER_JS = """
(function() {
    var cards = Array.from(document.querySelectorAll('.card'));
    var countEl = document.querySelector('.filter-count');
    var activeFilters = {};

    function updateCount() {
        var vis = cards.filter(function(c) { return c.style.display !== 'none'; }).length;
        if (countEl) countEl.textContent = vis + ' of ' + cards.length + ' entries';
    }

    function applyFilters() {
        var searchVal = (document.querySelector('.filter-search') || {value:''}).value.toLowerCase().trim();
        cards.forEach(function(card) {
            var show = true;
            // text search
            if (searchVal) {
                var text = (card.querySelector('.card-title') || {textContent:''}).textContent.toLowerCase()
                         + ' ' + (card.querySelector('.card-desc') || {textContent:''}).textContent.toLowerCase();
                if (text.indexOf(searchVal) === -1) show = false;
            }
            // attribute filters — each filter group: OR within group, AND across groups
            Object.keys(activeFilters).forEach(function(attr) {
                if (activeFilters[attr].length === 0) return;
                var val = (card.getAttribute('data-' + attr) || '').toLowerCase();
                var match = activeFilters[attr].some(function(f) { return val === f.toLowerCase(); });
                if (!match) show = false;
            });
            card.style.display = show ? '' : 'none';
        });
        // hide/show section headers
        document.querySelectorAll('.section-header').forEach(function(h) {
            var grid = h.nextElementSibling;
            if (!grid) return;
            var visible = Array.from(grid.querySelectorAll('.card')).some(function(c) { return c.style.display !== 'none'; });
            h.classList.toggle('hidden', !visible);
        });
        updateCount();
    }

    // Wire filter buttons
    document.querySelectorAll('.filter-btn').forEach(function(btn) {
        var attr = btn.getAttribute('data-filter-attr');
        var val = btn.getAttribute('data-filter-val');
        if (!activeFilters[attr]) activeFilters[attr] = [];
        btn.addEventListener('click', function() {
            btn.classList.toggle('active');
            if (btn.classList.contains('active')) {
                activeFilters[attr].push(val);
            } else {
                activeFilters[attr] = activeFilters[attr].filter(function(v) { return v !== val; });
            }
            applyFilters();
        });
    });

    // Wire search
    var searchEl = document.querySelector('.filter-search');
    if (searchEl) {
        var timer;
        searchEl.addEventListener('input', function() {
            clearTimeout(timer);
            timer = setTimeout(applyFilters, 180);
        });
    }

    // Wire sort buttons
    document.querySelectorAll('.sort-btn').forEach(function(btn) {
        btn.addEventListener('click', function() {
            document.querySelectorAll('.sort-btn').forEach(function(b) { b.classList.remove('active'); });
            btn.classList.add('active');
            var mode = btn.getAttribute('data-sort');
            document.querySelectorAll('.grid').forEach(function(grid) {
                var items = Array.from(grid.querySelectorAll('.card'));
                items.sort(function(a, b) {
                    if (mode === 'az') return (a.querySelector('.card-title') || {textContent:''}).textContent.localeCompare((b.querySelector('.card-title') || {textContent:''}).textContent);
                    if (mode === 'za') return (b.querySelector('.card-title') || {textContent:''}).textContent.localeCompare((a.querySelector('.card-title') || {textContent:''}).textContent);
                    return 0;
                });
                items.forEach(function(item) { grid.appendChild(item); });
            });
        });
    });

    updateCount();
})();
"""


def build_filter_bar(table, era_groups):
    """Build a filter bar appropriate for the given section."""
    buttons_html = ""

    if table == "persons":
        eras = ["ANTIQUITY", "MEDIEVAL", "RENAISSANCE", "EARLY MODERN", "MODERN"]
        roles = sorted(set(r['role_primary'] for rows in era_groups.values() for r in rows if ('role_primary' in r.keys() and r['role_primary']) and r['role_primary'] != 'SCHOLAR'))
        buttons_html += '<span class="filter-bar-label">Era</span><div class="filter-group">'
        for e in eras:
            buttons_html += f'<button class="filter-btn" data-filter-attr="era" data-filter-val="{e}">{e.replace("_"," ").title()}</button>'
        buttons_html += '</div>'
        if roles:
            buttons_html += '<span class="filter-bar-label" style="margin-left:1rem">Role</span><div class="filter-group">'
            for role in roles:
                buttons_html += f'<button class="filter-btn" data-filter-attr="role" data-filter-val="{role}">{role.replace("_"," ").title()}</button>'
            buttons_html += '</div>'

    elif table == "scholars":
        groups = sorted(era_groups.keys())
        buttons_html += '<span class="filter-bar-label">Focus Area</span><div class="filter-group">'
        for g in groups:
            safe = g.replace('"', '')
            buttons_html += f'<button class="filter-btn" data-filter-attr="group" data-filter-val="{safe}">{safe}</button>'
        buttons_html += '</div>'

    elif table == "texts":
        ttypes = sorted(set(r['text_type'] for rows in era_groups.values() for r in rows if ('text_type' in r.keys() and r['text_type'])))
        buttons_html += '<span class="filter-bar-label">Type</span><div class="filter-group">'
        for t in ttypes:
            buttons_html += f'<button class="filter-btn" data-filter-attr="type" data-filter-val="{t}">{t.replace("_"," ").title()}</button>'
        buttons_html += '</div>'

    elif table == "concepts":
        cats = sorted(set(r['category'] for rows in era_groups.values() for r in rows if ('category' in r.keys() and r['category'])))
        ctypes = ["ACTOR_TERM", "ANALYST_TERM", "HYBRID"]
        buttons_html += '<span class="filter-bar-label">Category</span><div class="filter-group">'
        for cat in cats:
            buttons_html += f'<button class="filter-btn" data-filter-attr="cat" data-filter-val="{cat}">{cat.replace("_"," ").title()}</button>'
        buttons_html += '</div>'
        buttons_html += '<span class="filter-bar-label" style="margin-left:1rem">Term Type</span><div class="filter-group">'
        for ct in ctypes:
            label = ct.replace("_", " ").title().replace("Term", "Term")
            buttons_html += f'<button class="filter-btn" data-filter-attr="termtype" data-filter-val="{ct}">{label}</button>'
        buttons_html += '</div>'

    sort_bar = ('<div class="filter-group" style="margin-left:auto">'
                '<span class="filter-bar-label">Sort</span>'
                '<button class="sort-btn active" data-sort="default">Default</button>'
                '<button class="sort-btn" data-sort="az">A–Z</button>'
                '<button class="sort-btn" data-sort="za">Z–A</button>'
                '</div>')

    return (f'<style>{FILTER_CSS}</style>'
            f'<div class="filter-bar">'
            f'<input class="filter-search" type="text" placeholder="Search entries…">'
            f'{buttons_html}'
            f'{sort_bar}'
            f'<span class="filter-count"></span>'
            f'</div>'
            f'<script>{FILTER_JS}</script>')

def slug_for_row(table, row):
    if table == "texts":
        return row["text_id"]
    if table == "concepts":
        return row["slug"]
    return row["person_id"]

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
            content = re.sub(r'(?m)^\s*[-*]\s+', '', content)
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
    (target_dir / "dictionary").mkdir(exist_ok=True)

    # --- Build search index (used by global search overlay + hover cards) ---
    search_index = []
    cursor.execute("SELECT person_id, name, role_primary, era, description FROM persons")
    for r in cursor.fetchall():
        folder = "scholars" if r["role_primary"] == "SCHOLAR" else "biographies"
        search_index.append({
            "id": r["person_id"], "label": r["name"], "type": "PERSON",
            "meta": f"{(r['era'] or '').replace('_',' ')} · {r['role_primary'] or 'Figure'}",
            "desc": (r["description"] or "")[:130],
            "url": f"{REPO_URL}/{folder}/{r['person_id']}.html"
        })
    cursor.execute("SELECT text_id, title, text_type, description FROM texts")
    for r in cursor.fetchall():
        search_index.append({
            "id": r["text_id"], "label": r["title"], "type": "TEXT",
            "meta": r["text_type"] or "TEXT",
            "desc": (r["description"] or "")[:130],
            "url": f"{REPO_URL}/texts/{r['text_id']}.html"
        })
    cursor.execute("SELECT slug, label, category, definition_short FROM concepts")
    for r in cursor.fetchall():
        search_index.append({
            "id": r["slug"], "label": r["label"], "type": "CONCEPT",
            "meta": r["category"] or "CONCEPT",
            "desc": (r["definition_short"] or "")[:130],
            "url": f"{REPO_URL}/dictionary/{r['slug']}.html"
        })
    import json as _json
    with open(target_dir / "search_index.json", "w", encoding="utf-8") as _f:
        _json.dump(search_index, _f, ensure_ascii=False)

    # --- Build entity link map for timeline auto-linking ---
    entity_link_map = {}
    cursor.execute("SELECT person_id, name, role_primary FROM persons ORDER BY length(name) DESC")
    for r in cursor.fetchall():
        folder = "scholars" if r["role_primary"] == "SCHOLAR" else "biographies"
        entity_link_map[r["name"]] = f"{REPO_URL}/{folder}/{r['person_id']}.html"
    cursor.execute("SELECT text_id, title FROM texts ORDER BY length(title) DESC")
    for r in cursor.fetchall():
        entity_link_map[r["title"]] = f"{REPO_URL}/texts/{r['text_id']}.html"

    def auto_link_entities(html_text):
        """Link first occurrence of each person/text name in prose HTML, skipping existing tags."""
        if not html_text:
            return html_text
        parts = re.split(r'(<[^>]+>)', html_text)
        linked = set()
        result = []
        for i, part in enumerate(parts):
            if i % 2 == 1:
                result.append(part)
            else:
                for name, url in entity_link_map.items():
                    if name in linked or name not in part:
                        continue
                    part = part.replace(
                        name,
                        f'<a href="{url}" class="nav-link" style="color:var(--accent)">{name}</a>',
                        1
                    )
                    linked.add(name)
                result.append(part)
        return "".join(result)

    # --- Helper: key figures for a concept (persons linked via shared texts) ---
    def get_concept_figures_html(cursor, slug):
        try:
            cursor.execute("""
                SELECT DISTINCT p.person_id, p.name, p.role_primary, p.era
                FROM concept_text_refs ctr
                JOIN concepts c ON ctr.concept_id = c.id
                JOIN texts t ON ctr.text_id = t.id
                JOIN person_text_refs ptr ON ptr.text_id = t.text_id
                JOIN persons p ON ptr.person_id = p.person_id
                WHERE c.slug = ?
                ORDER BY p.era, p.name
                LIMIT 10
            """, (slug,))
            rows = cursor.fetchall()
        except Exception:
            return ""
        if not rows:
            return ""
        actors = [(r["person_id"], r["name"], r["role_primary"]) for r in rows if r["role_primary"] != "SCHOLAR"]
        analysts = [(r["person_id"], r["name"], r["role_primary"]) for r in rows if r["role_primary"] == "SCHOLAR"]
        html = '<div style="margin-top:3rem;padding-top:2rem;border-top:1px solid var(--border)">'
        html += '<h2 style="font-family:var(--font-display);color:var(--accent);margin-bottom:1rem">Key Figures</h2>'
        if actors:
            html += '<p style="font-size:0.8rem;color:var(--text-muted);text-transform:uppercase;letter-spacing:0.1em;margin-bottom:0.7rem">Historical Actors</p>'
            html += '<ul style="list-style:none;padding:0;margin-bottom:1.5rem">'
            for pid, name, role in actors:
                html += f'<li style="margin-bottom:0.4rem"><a href="{REPO_URL}/biographies/{pid}.html" class="nav-link">{name}</a> <span style="color:var(--text-muted);font-size:0.82rem">({(role or "figure").lower().replace("_"," ")})</span></li>'
            html += '</ul>'
        if analysts:
            html += '<p style="font-size:0.8rem;color:var(--text-muted);text-transform:uppercase;letter-spacing:0.1em;margin-bottom:0.7rem">Modern Scholars</p>'
            html += '<ul style="list-style:none;padding:0">'
            for pid, name, role in analysts:
                html += f'<li style="margin-bottom:0.4rem"><a href="{REPO_URL}/scholars/{pid}.html" class="nav-link">{name}</a></li>'
            html += '</ul>'
        html += '</div>'
        return html

    # --- Helper: key concepts for a person (via shared texts) ---
    def get_person_concepts_html(cursor, pid):
        try:
            cursor.execute("""
                SELECT DISTINCT c.slug, c.label, c.category_type
                FROM person_text_refs ptr
                JOIN texts t ON ptr.text_id = t.text_id
                JOIN concept_text_refs ctr ON ctr.text_id = t.id
                JOIN concepts c ON ctr.concept_id = c.id
                WHERE ptr.person_id = ?
                ORDER BY c.label
                LIMIT 12
            """, (pid,))
            rows = cursor.fetchall()
        except Exception:
            return ""
        if not rows:
            return ""
        html = '<div style="margin-top:2.5rem;padding-top:1.5rem;border-top:1px solid var(--border)">'
        html += '<h2 style="font-family:var(--font-display);font-size:1.1rem;color:var(--accent);margin-bottom:1rem">Key Concepts</h2>'
        html += '<div style="display:flex;flex-wrap:wrap;gap:0.5rem">'
        for slug, label, cat_type in rows:
            badge_color = "rgba(32,201,151,0.15)" if cat_type == "ACTOR_TERM" else "rgba(74,158,255,0.15)"
            border_color = "rgba(32,201,151,0.4)" if cat_type == "ACTOR_TERM" else "rgba(74,158,255,0.4)"
            html += (f'<a href="{REPO_URL}/dictionary/{slug}.html" '
                     f'style="padding:0.25rem 0.7rem;background:{badge_color};border:1px solid {border_color};'
                     f'border-radius:20px;color:var(--text-main);font-size:0.82rem;text-decoration:none">{label}</a>')
        html += '</div></div>'
        return html

    # PAGE GENERATION LOGIC
    
    def get_person_locations_html(cursor, pid):
        """Return an HTML block showing key locations for a person, if any."""
        try:
            cursor.execute("""
                SELECT l.slug, l.label, pl.role, pl.note
                FROM person_locations pl
                JOIN locations l ON pl.location_slug = l.slug
                WHERE pl.person_id = ?
                ORDER BY pl.role, l.label
            """, (pid,))
            locs = cursor.fetchall()
        except Exception:
            return ""
        if not locs:
            return ""
        items = "".join(
            f'<li style="margin-bottom:0.4rem"><a href="{REPO_URL}/map.html" class="nav-link">{lslug_label}</a>'
            f' <span style="color:var(--text-muted);font-size:0.85rem">({role.lower()})</span></li>'
            for _, lslug_label, role, note in locs
        )
        return (f'<div style="margin-top:2.5rem;padding-top:1.5rem;border-top:1px solid var(--border)">'
                f'<h2 style="font-family:var(--font-display);font-size:1.1rem;color:var(--accent);margin-bottom:1rem">Key Locations</h2>'
                f'<ul style="list-style:none;padding:0">{items}</ul></div>')

    # 1. BIOGRAPHIES
    cursor.execute("SELECT * FROM persons WHERE role_primary != 'SCHOLAR' OR role_primary IS NULL")
    for row in cursor.fetchall():
        pid, name, content = row['person_id'], row['name'], italicize_terms(row['bio_html'] or f"<p>{row['description']}</p>")
        fragments = italicize_terms(get_fragments(cursor, pid, "PERSON"))
        locs_html = get_person_locations_html(cursor, pid)
        concepts_html = get_person_concepts_html(cursor, pid)
        era = (row['era'] or 'Unknown').replace('_', ' ')
        role = row['role_primary'] or 'Figure'
        meta = f"{era} · {role}"
        era_stripe_color = {"ANTIQUITY": "#d4af37", "MEDIEVAL": "#20c997", "RENAISSANCE": "#e67e22", "EARLY MODERN": "#9b59b6", "MODERN": "#4a9eff"}.get(era, "var(--accent)")
        header = (f'<div style="border-left:4px solid {era_stripe_color};padding-left:1.5rem;margin-bottom:3rem">'
                  f'<a href="{REPO_URL}/biographies.html" class="back-link" style="display:block;margin-bottom:0.75rem">← Return to Archives</a>'
                  f'<h1 class="title-large" style="margin-bottom:0.5rem">{name}</h1>'
                  f'<div class="card-meta">{meta}</div></div>')
        html = BASE_TEMPLATE.replace("{{title}}", name).replace("{{css}}", CSS).replace("{{nav}}", NAV_BAR).replace("{{content}}", f'<main class="page-container">{header}<div class="prose-content">{content}{locs_html}{concepts_html}{fragments}</div></main>')
        with open(target_dir / "biographies" / f"{pid}.html", "w", encoding="utf-8") as f: f.write(html)

    # 2. SCHOLARS
    cursor.execute("SELECT * FROM persons WHERE role_primary = 'SCHOLAR'")
    for row in cursor.fetchall():
        pid, name, content = row['person_id'], row['name'], italicize_terms(row['bio_html'] or f"<p>{row['description']}</p>")
        fragments = italicize_terms(get_fragments(cursor, pid, "PERSON"))
        locs_html = get_person_locations_html(cursor, pid)
        concepts_html = get_person_concepts_html(cursor, pid)
        html = BASE_TEMPLATE.replace("{{title}}", name).replace("{{css}}", CSS).replace("{{nav}}", NAV_BAR).replace("{{content}}", f'<main class="page-container"><a href="{REPO_URL}/scholars.html" class="back-link">← Return to Faculty</a><h1 class="title-large">{name}</h1><div class="card-meta" style="margin-bottom:3rem">Scholarly Authority</div><div class="prose-content">{content}{locs_html}{concepts_html}{fragments}</div></main>')
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
        dict_crosslink = (f'<div style="margin-bottom:2rem;padding:1rem 1.5rem;background:rgba(212,175,55,0.06);'
                          f'border:1px solid var(--border);border-radius:8px;display:flex;justify-content:space-between;align-items:center">'
                          f'<span style="color:var(--text-muted);font-size:0.9rem">Relational connections for <strong style="color:var(--text-main)">{row["label"]}</strong></span>'
                          f'<a href="{REPO_URL}/dictionary/{slug}.html" class="nav-link" style="color:var(--accent);font-size:0.9rem;font-weight:600">'
                          f'Read full encyclopedia entry →</a></div>')
        figures_html = get_concept_figures_html(cursor, slug)
        html = BASE_TEMPLATE.replace("{{title}}", label).replace("{{css}}", CSS).replace("{{nav}}", NAV_BAR).replace("{{content}}", f'<main class="page-container"><a href="{REPO_URL}/dictionary.html" class="back-link">← Return to Dictionary</a><h1 class="title-large">{label}</h1><div class="card-meta" style="margin-bottom:1.5rem">{meta_label}</div>{dict_crosslink}<div class="prose-content">{content}{figures_html}{fragments}</div></main>')
        with open(target_dir / "concepts" / f"{slug}.html", "w", encoding="utf-8") as f: f.write(html)

    # 4B. DICTIONARY PAGES (Full Encyclopedia Entries)
    cursor.execute("SELECT * FROM concepts ORDER BY label")
    for row in cursor.fetchall():
        slug = row['slug']
        label = italicize_terms(row['label'])

        # Main content: definition_long (encyclopedia entry)
        definition = italicize_terms(row['definition_long']) if row['definition_long'] else f"<p><em>No full encyclopedia entry yet. See brief definition:</em></p><p>{row['definition_short']}</p>"

        # Related concepts (concept_links)
        related_html = ""
        cursor.execute("""
            SELECT c2.slug, c2.label, cl.relationship
            FROM concept_links cl
            JOIN concepts c2 ON cl.to_concept_id = c2.id
            WHERE cl.from_concept_id = (SELECT id FROM concepts WHERE slug = ?)
            ORDER BY c2.label
        """, (slug,))
        related = cursor.fetchall()
        if related:
            related_html = '<div style="margin-top: 3rem; padding-top: 2rem; border-top: 1px solid var(--border)"><h2 class="title-medium">Related Concepts</h2><ul style="list-style: none; padding: 0">'
            for rslug, rlabel, rel_type in related:
                related_html += f'<li style="margin-bottom: 0.5rem"><a href="{REPO_URL}/dictionary/{rslug}.html" class="nav-link">{rlabel}</a> <span style="color: var(--text-muted); font-size: 0.85rem">({rel_type.replace("_", " ")})</span></li>'
            related_html += '</ul></div>'

        # Literature: texts that reference this concept
        lit_html = ""
        cursor.execute("""
            SELECT DISTINCT t.text_id, t.title, t.text_type
            FROM concept_text_refs ctr
            JOIN texts t ON ctr.text_id = t.id
            WHERE ctr.concept_id = (SELECT id FROM concepts WHERE slug = ?)
            ORDER BY t.title
        """, (slug,))
        texts = cursor.fetchall()
        if texts:
            lit_html = '<div style="margin-top: 3rem; padding-top: 2rem; border-top: 1px solid var(--border)"><h2 class="title-medium">In the Literature</h2><ul style="list-style: none; padding: 0">'
            for text_id, ttitle, ttype in texts:
                lit_html += f'<li style="margin-bottom: 0.5rem"><a href="{REPO_URL}/texts/{text_id}.html" class="nav-link">{ttitle}</a> <span style="color: var(--text-muted); font-size: 0.85rem">[{ttype}]</span></li>'
            lit_html += '</ul></div>'

        cat_type = row['category_type'] if 'category_type' in row.keys() and row['category_type'] else 'HYBRID'
        meta_label = f"{row['category'] or 'General'} Concept · {cat_type.replace('_', ' ')}"

        concepts_crosslink = (f'<div style="margin-bottom:2rem;padding:1rem 1.5rem;background:rgba(212,175,55,0.06);'
                              f'border:1px solid var(--border);border-radius:8px;display:flex;justify-content:space-between;align-items:center">'
                              f'<span style="color:var(--text-muted);font-size:0.9rem">Encyclopedia entry for <strong style="color:var(--text-main)">{row["label"]}</strong></span>'
                              f'<a href="{REPO_URL}/concepts/{slug}.html" class="nav-link" style="color:var(--accent);font-size:0.9rem;font-weight:600">'
                              f'← Browse relational connections</a></div>')
        dict_figures_html = get_concept_figures_html(cursor, slug)
        content_html = f'<main class="page-container"><a href="{REPO_URL}/dictionary.html" class="back-link">← Dictionary Index</a><h1 class="title-large">{label}</h1><div class="card-meta" style="margin-bottom:1.5rem">{meta_label}</div>{concepts_crosslink}<div class="prose-content">{definition}{dict_figures_html}{related_html}{lit_html}</div></main>'
        html = BASE_TEMPLATE.replace("{{title}}", row['label']).replace("{{css}}", CSS).replace("{{nav}}", NAV_BAR).replace("{{content}}", content_html)

        with open(target_dir / "dictionary" / f"{slug}.html", "w", encoding="utf-8") as f: f.write(html)

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
                if row['text_type'] in ('COMMENTARY', 'SCHOLARSHIP'):
                    era_groups["MODERN SCHOLARSHIP"].append(row)
                else:
                    era_groups["PRIMARY SOURCES"].append(row)
        elif table == "scholars":
            cursor.execute("SELECT * FROM persons WHERE role_primary = 'SCHOLAR' ORDER BY scholar_group, name")
            for row in cursor.fetchall():
                group = row['scholar_group'] if 'scholar_group' in row.keys() and row['scholar_group'] else "Modern Esotericism and Historiography"
                if group not in era_groups: era_groups[group] = []
                era_groups[group].append(row)
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
                desc = clean_prose(desc)

                target_folder = target
                link = f"{REPO_URL}/{target_folder}/{slug_for_row(table, row)}.html"

                # Build data attributes for filtering
                data_attrs = {"name": name.replace('"', '')}
                if 'era' in row.keys() and row['era']:
                    data_attrs['era'] = row['era'].replace('_', ' ')
                if 'role_primary' in row.keys() and row['role_primary']:
                    data_attrs['role'] = row['role_primary']
                if 'text_type' in row.keys() and row['text_type']:
                    data_attrs['type'] = row['text_type']
                if 'category' in row.keys() and row['category']:
                    data_attrs['cat'] = row['category']
                if 'category_type' in row.keys() and row['category_type']:
                    data_attrs['termtype'] = row['category_type']
                if 'scholar_group' in row.keys() and row['scholar_group']:
                    data_attrs['group'] = row['scholar_group'].replace('"', '')

                cards += generate_entity_card(name, meta, desc, link, data_attrs)
                era_links.append(f'<a href="{link}" class="nav-link" style="font-size:0.9rem; padding:0.2rem 0.5rem; border:1px solid var(--border); border-radius:4px">{name}</a>')

            sections_html += (f'<h2 class="title-medium section-header" style="margin-top:4rem; border-bottom: 2px solid var(--accent); display:inline-block">{era}</h2>'
                              f'<div class="grid">{cards}</div>')
            compact_list_html += f'<div style="width:100%; margin-top:1rem; font-weight:bold; color:var(--text-muted); font-size:0.8rem">{era}</div>'
            compact_list_html += "".join(era_links)

        compact_list_html += '</div></div>'
        filter_bar = build_filter_bar(table, era_groups)
        content = (f'<main class="page-container">'
                   f'<h1 class="title-large">{title}</h1>'
                   f'<p class="text-subtitle" style="margin-bottom:2rem">{sub}</p>'
                   f'{filter_bar}'
                   f'{compact_list_html}'
                   f'{sections_html}'
                   f'</main>')
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
        
        # Persons
        cursor.execute("SELECT * FROM persons WHERE era = ? ORDER BY name", (db_era,))
        era_cards = ""
        for row in cursor.fetchall():
            person_folder = "scholars" if row['role_primary'] == "SCHOLAR" else "biographies"
            era_cards += generate_entity_card(row['name'], row['role_primary'], row['description'], f"{REPO_URL}/{person_folder}/{row['person_id']}.html")
        
        # Texts
        date_query = ""
        if db_era == 'ANTIQUITY': date_query = "date_composed_start < 600"
        elif db_era == 'MEDIEVAL': date_query = "date_composed_start >= 600 AND date_composed_start < 1400"
        elif db_era == 'RENAISSANCE': date_query = "date_composed_start >= 1400 AND date_composed_start < 1600"
        elif db_era == 'EARLY_MODERN': date_query = "date_composed_start >= 1600 AND date_composed_start < 1850"
        elif db_era == 'MODERN': date_query = "date_composed_start >= 1850"
        
        text_cards = ""
        if date_query:
            cursor.execute(f"SELECT * FROM texts WHERE {date_query} ORDER BY title")
            for row in cursor.fetchall():
                text_cards += generate_entity_card(row['title'], row['text_type'], row['description'], f"{REPO_URL}/texts/{row['text_id']}.html")
        
        prose = ERA_PROSE.get(db_era, "")
        
        sections_html = ""
        if era_cards:
            sections_html += f'<h2 style="color:var(--accent); margin-top:4rem; border-bottom: 1px solid var(--border); padding-bottom: 1rem">Figures</h2><div class="grid">{era_cards}</div>'
        if text_cards:
            sections_html += f'<h2 style="color:var(--accent); margin-top:4rem; border-bottom: 1px solid var(--border); padding-bottom: 1rem">Manuscripts & Texts</h2><div class="grid">{text_cards}</div>'
            
        content = f'<main class="page-container"><h1 class="title-large">{era_name} Archives</h1><p class="text-subtitle">Figures and manuscripts of the {era_name} period.</p>{prose}{sections_html}</main>'
        with open(target_dir / "eras" / f"{era_id}.html", "w", encoding="utf-8") as f: f.write(BASE_TEMPLATE.replace("{{title}}", era_name).replace("{{css}}", CSS).replace("{{nav}}", NAV_BAR).replace("{{content}}", content))

    # 6.5. TIMELINE
    def year_to_era(year):
        if year is None: return "UNKNOWN"
        y = int(year)
        if y < 600: return "ANTIQUITY"
        if y < 1400: return "MEDIEVAL"
        if y < 1600: return "RENAISSANCE"
        if y < 1850: return "EARLY_MODERN"
        return "MODERN"

    cursor.execute("SELECT * FROM timeline_events ORDER BY year ASC")
    timeline_cards = ""
    for row in cursor.fetchall():
        year_str = str(row['year'])
        if row['year_end']:
            year_str += f" - {row['year_end']}"
        era = year_to_era(row['year'])
        era_label = era.replace("_", " ").title()
        meta = f"{year_str} · {row['event_type'] or 'EVENT'} · {era_label}"
        desc = auto_link_entities(row['description_long'] or f"<p>{row['description']}</p>")

        timeline_cards += f"""
        <div class="card" data-era="{era}" style="margin-bottom: 1rem;">
            <div class="card-title">{row['title']}</div>
            <div class="card-meta">{meta}</div>
            <div class="prose-content" style="padding: 1rem; margin-top: 1rem; border: none; background: rgba(0,0,0,0.2);">{desc}</div>
        </div>
        """

    timeline_filter = (f'<style>{FILTER_CSS}</style>'
                       f'<div class="filter-bar">'
                       f'<span class="filter-bar-label">Era</span>'
                       f'<div class="filter-group">'
                       f'<button class="filter-btn" data-filter-attr="era" data-filter-val="ANTIQUITY">Antiquity</button>'
                       f'<button class="filter-btn" data-filter-attr="era" data-filter-val="MEDIEVAL">Medieval</button>'
                       f'<button class="filter-btn" data-filter-attr="era" data-filter-val="RENAISSANCE">Renaissance</button>'
                       f'<button class="filter-btn" data-filter-attr="era" data-filter-val="EARLY_MODERN">Early Modern</button>'
                       f'<button class="filter-btn" data-filter-attr="era" data-filter-val="MODERN">Modern</button>'
                       f'</div>'
                       f'<span class="filter-count"></span>'
                       f'</div>'
                       f'<script>{FILTER_JS}</script>')

    content = (f'<main class="page-container">'
               f'<h1 class="title-large">Timeline of Hermeticism</h1>'
               f'<p class="text-subtitle">Key events, publications, and movements.</p>'
               f'{timeline_filter}'
               f'<div style="display:flex;flex-direction:column;gap:1rem;">{timeline_cards}</div>'
               f'</main>')
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

    # Augment locations with associated persons and texts from the DB
    cursor.execute("SELECT person_id, name, era FROM persons ORDER BY era, name")
    all_persons = cursor.fetchall()
    cursor.execute("SELECT text_id, title, text_type FROM texts WHERE text_type IN ('PRIMARY_SOURCE','TREATISE') ORDER BY title")
    all_texts = cursor.fetchall()

    # Extended location data with scholarly context
    LOCATION_EXTRAS = {
        "alexandria": {
            "figures": ["Zosimos of Panopolis", "Clement of Alexandria", "Cyril of Alexandria", "Plotinus (studied here)", "Iamblichus (visited)"],
            "texts": ["Corpus Hermeticum (composed here, c. 100–300 CE)", "Stobaean Fragments", "Nag Hammadi texts (nearby)"],
            "archives": ["Bibliotheca Alexandrina (modern reconstruction)", "Various Coptic monasteries preserve related manuscripts"],
            "note": "The intellectual cradle of Greco-Egyptian syncretism and the probable site of composition of the philosophical Hermetica."
        },
        "hermopolis": {
            "figures": ["Thoth (mythological patron)", "Hermes Trismegistus (legendary home)"],
            "texts": ["Book of Thoth (legendary)", "Early Egyptian priestly literature"],
            "archives": [],
            "note": "Hermopolis Magna (Egyptian: Khmun) was the cult center of Thoth and was identified by ancient and modern scholars alike as the mythological home of Hermetic wisdom."
        },
        "florence": {
            "figures": ["Marsilio Ficino", "Giovanni Pico della Mirandola", "Lorenzo de' Medici", "Cosimo de' Medici"],
            "texts": ["Corpus Hermeticum (Latin Pimander, 1463)", "Theologia Platonica", "De Vita Libri Tres"],
            "archives": ["Biblioteca Medicea Laurenziana — holds key Hermetic manuscripts including the Greek CH codex"],
            "note": "The epicenter of Renaissance Hermeticism. Cosimo de' Medici commissioned Ficino to translate the Corpus Hermeticum here in 1460–63, prioritizing it over his Plato translation."
        },
        "harran": {
            "figures": ["Thabit ibn Qurra", "The Sabian community (8th–13th c.)", "Al-Battani"],
            "texts": ["Arabic Hermetic treatises preserved by the Sabians", "Astronomical works"],
            "archives": [],
            "note": "Harran (modern southeastern Turkey) was home to the Sabian community who maintained Neoplatonic and Hermetic traditions well into the Islamic period, serving as a crucial bridge between Late Antique and medieval Hermeticism."
        },
        "baghdad": {
            "figures": ["Hunayn ibn Ishaq (translator)", "Al-Kindi", "Abu Ma'shar", "Jabir ibn Hayyan (associated)"],
            "texts": ["Arabic translations of Greek Hermetic texts", "Kitab Sirr al-Khaliqa (Book of the Secret of Creation)", "Picatrix (compiled nearby)"],
            "archives": ["Dar al-Hikma (House of Wisdom) — key transmission site"],
            "note": "Baghdad under the Abbasid caliphate was the central site of Arabic Hermetic transmission. The translation movement (8th–10th c.) brought Greek Hermetic texts into Arabic, often with commentary and expansion."
        },
        "akhmim": {
            "figures": ["Zosimos of Panopolis (c. 300 CE)", "Theosebia (correspondent of Zosimos)"],
            "texts": ["Zosimos's alchemical treatises", "Cheirokmeta (On the Effects of Craft)"],
            "archives": [],
            "note": "Akhmim (ancient Panopolis) in Upper Egypt was the home of Zosimos, the most important alchemical writer of Late Antiquity, whose works blend practical chemistry with Hermetic spiritual symbolism."
        },
        "panopolis": {
            "figures": ["Zosimos of Panopolis"],
            "texts": ["Zosimos's alchemical corpus"],
            "archives": [],
            "note": "Alternative name for Akhmim. See Akhmim entry."
        },
        "toledo": {
            "figures": ["Herman the German", "Gerard of Cremona", "Dominicus Gundissalinus", "Hugo of Santalla"],
            "texts": ["Latin translations of Arabic Hermetic texts", "Picatrix (Latin, c. 1256)", "Liber de causis"],
            "archives": ["Cathedral of Toledo library — medieval translation center"],
            "note": "Toledo was the primary center of the 12th-century translation movement, where Arabic Hermetic and philosophical texts were translated into Latin by a school of translators working under Archbishop Raymond."
        },
        "rome": {
            "figures": ["Athanasius Kircher (worked here)", "G.R.S. Mead (visited)", "Pico della Mirandola (debated here)"],
            "texts": ["Kircher's Oedipus Aegyptiacus (1652–54)", "Various Rosicrucian publications"],
            "archives": ["Vatican Library — Reg. Lat. 1290 (Corpus Hermeticum manuscript)", "Biblioteca Nazionale Centrale"],
            "note": "Rome was a significant center for early modern Hermeticism, especially through Kircher's Egyptological projects and the Jesuit engagement with Hermetic symbolism."
        },
        "memphis": {
            "figures": ["Ptah (patron deity)", "Egyptian priests of Memphis", "Hermes Trismegistus (legendary connection)"],
            "texts": ["Memphite creation theology", "Hermetic texts derived from Memphis tradition", "Egyptian priestly literature"],
            "archives": [],
            "note": "According to Christian Bull's thesis, the Hermetic priesthood rooted themselves in the Memphite theological tradition, translating the cosmology of Ptah into Greek philosophical language."
        },
        "thebes": {
            "figures": ["Egyptian priesthood of Amun", "Amun-Ra devotees"],
            "texts": ["Theban temple inscriptions", "Amun theology", "Egyptian priestly hymns"],
            "archives": [],
            "note": "Thebes was the great religious capital of Upper Egypt and a primary center of priesthood and theological learning that influenced Hermetic synthesis."
        },
        "coptos": {
            "figures": ["Hermetic merchants", "Pilgrimage communities"],
            "texts": ["Trade route texts", "Coptic Christian manuscripts"],
            "archives": [],
            "note": "A crucial trading hub where commerce, religious practice, and philosophical transmission intersected along the Red Sea route."
        },
        "assuan": {
            "figures": ["Nubian priesthood", "Egyptian priests", "Southern temple communities"],
            "texts": ["Nubian-Egyptian syncretic texts", "Temple inscriptions"],
            "archives": [],
            "note": "The southern border city of Egypt, home to significant temple traditions that preserved Egyptian religious knowledge."
        },
        "akhmim_expanded": {
            "figures": ["Zosimos of Panopolis (fl. 300 CE)", "Theosebia (correspondent)", "Upper Egyptian alchemists"],
            "texts": ["Zosimos's Visiones", "Cheirokmeta (On the Effects of Craft)", "Zosimos's alchemical corpus"],
            "archives": ["Byzantine Greek manuscripts", "Arabic recensions and commentaries"],
            "note": "Home of Zosimos, the most important surviving alchemical author of Late Antiquity. His vision-narratives integrate Hermetic principle of correspondence with laboratory practice."
        },
        "antioch": {
            "figures": ["John Chrysostom", "Later Neoplatonic philosophers", "Christian theologians"],
            "texts": ["Syriac philosophical translations", "Neoplatonic commentaries", "Christian-Hermetic synthesis texts"],
            "archives": [],
            "note": "A major center of late antique synthesis between Christian theology, Neoplatonism, and Hermetic cosmology."
        },
        "constantinople": {
            "figures": ["Byzantine scholars", "Photios (Patriarch)", "Psellus", "Neoplatonic commentators"],
            "texts": ["Corpus Hermeticum Greek manuscripts", "Byzantine commentaries", "Philosophical translations"],
            "archives": ["Patriarchal Library (partially surviving manuscripts)", "Imperial libraries"],
            "note": "The Byzantine capital and primary custodian of Greek learning. Constantinople preserved Hermetic texts and hosted detailed scholarly engagement with the Hermetica."
        },
        "damascus": {
            "figures": ["Al-Kindi's circle", "Islamic philosophers", "Sabian scholars"],
            "texts": ["Arabic Hermetic translations", "Neoplatonic philosophical texts", "Occult sciences treatises"],
            "archives": [],
            "note": "A major Islamic intellectual center where Hermetic texts were preserved, translated, and studied."
        },
        "cairo": {
            "figures": ["Islamic alchemists", "Natural philosophers", "Sufi scholars"],
            "texts": ["Hermetic alchemical corpus", "Arabic translations", "Technical treatises"],
            "archives": [],
            "note": "The great Islamic capital maintaining continuity with ancient Egyptian Hermetic tradition and serving as a center for alchemical transmission."
        },
        "cordoba": {
            "figures": ["Al-Majriti", "Ibn Sina (Avicenna)", "Islamic-Andalusian scholars"],
            "texts": ["Picatrix (in Arabic)", "Neoplatonic philosophical works", "Alchemical treatises"],
            "archives": [],
            "note": "A major center of Islamic-Andalusian learning where Greek philosophical and Hermetic texts were preserved and studied."
        },
        "toledo": {
            "figures": ["Gerard of Cremona", "Herman the German", "Dominicus Gundissalinus", "Hugo of Santalla"],
            "texts": ["Picatrix (Latin translation, c. 1256)", "Liber de causis", "Arabic Hermetic texts in Latin"],
            "archives": ["Cathedral of Toledo library — medieval translation center"],
            "note": "The primary site of the 12th-century translation movement where Arabic Hermetic texts entered medieval Christian Europe in Latin translation."
        },
        "venice": {
            "figures": ["Renaissance collectors", "Greek manuscript traders", "Aldus Manutius"],
            "texts": ["Greek Hermetic manuscripts", "Neoplatonic texts", "Renaissance printed editions"],
            "archives": ["Biblioteca Marciana — holds Renaissance Hermetic manuscripts"],
            "note": "A major trading hub with connections to Byzantine and Islamic worlds, serving as a crucial source of Greek manuscripts during the Renaissance."
        },
        "mantua": {
            "figures": ["Giambattista della Porta", "Renaissance magicians", "Gonzaga patrons"],
            "texts": ["Hermetic philosophical works", "Alchemical treatises", "Magic and natural philosophy texts"],
            "archives": [],
            "note": "The court of the Gonzaga family, a major center of Renaissance humanism and Hermetic scholarship under ducal patronage."
        },
        "prague_hermetic": {
            "figures": ["Emperor Rudolf II", "John Dee", "Edward Kelley", "Tycho Brahe"],
            "texts": ["Alchemical manuscripts and printed works", "Hermetic philosophical treatises", "Occult and astrological texts"],
            "archives": ["Kunstkammer collection (Alchemical and occult manuscripts)", "Imperial libraries"],
            "note": "The alchemical capital of 16th-17th century Europe, where Rudolf II's patronage attracted the most significant alchemists and Hermetic practitioners."
        },
        "strasbourg": {
            "figures": ["Renaissance alchemists", "Paracelsians", "Early modern printers"],
            "texts": ["Alchemical texts", "Paracelsian works", "Hermetic philosophical treatises"],
            "archives": [],
            "note": "A major center of Renaissance alchemy and Hermetic studies, hosting important alchemists and publishers."
        },
        "paris": {
            "figures": ["Nicolas Flamel", "Medieval scholars", "Later Renaissance philosophers"],
            "texts": ["Hermetic and alchemical texts", "Philosophical treatises", "Occult knowledge books"],
            "archives": ["Bibliothèque Nationale de France"],
            "note": "A major center of medieval learning where Hermetic and alchemical texts circulated among scholars."
        },
        "oxford": {
            "figures": ["Roger Bacon", "Robert Grosseteste", "Later natural philosophers"],
            "texts": ["Hermetic and alchemical treatises", "Natural philosophy texts", "Occult sciences works"],
            "archives": ["Bodleian Library"],
            "note": "A center of medieval and early modern Hermetic learning where scholars engaged with alchemical and Hermetic philosophical ideas."
        },
        "basra": {
            "figures": ["Ikhwan al-Safa (Brethren of Purity)", "Islamic philosophers", "Al-Kindi's associates"],
            "texts": ["Epistles of the Brethren of Purity", "Neoplatonic philosophical works", "Hermetic texts in Arabic"],
            "archives": [],
            "note": "Home of the Ikhwan al-Safa, whose Epistles synthesized Neoplatonic, Hermetic, and Islamic theology into a comprehensive philosophical encyclopedia."
        },
        "cologne": {
            "figures": ["Heinrich Cornelius Agrippa (born here)", "Albertus Magnus (Dominican studium)", "Johannes Duns Scotus (buried here)"],
            "texts": ["De Occulta Philosophia libri tres (Agrippa, 1531 — published here)", "Albertus Magnus's natural philosophy commentaries"],
            "archives": ["Cologne Cathedral archive", "Historical Archive of the City of Cologne"],
            "note": "Agrippa's birthplace and publishing centre. Albertus Magnus led the Dominican studium here, shaping the scholastic reception of Arabic natural philosophy and Hermetic cosmology. The final edition of De Occulta Philosophia (1531), the most ambitious synthesis of Renaissance Hermetic and magical philosophy, was printed in Cologne."
        },
        "wurzburg": {
            "figures": ["Johannes Trithemius (Abbot of St James, 1506–16)", "Heinrich Cornelius Agrippa (visitor, 1509–10)"],
            "texts": ["De Occulta Philosophia (first draft completed here, 1510)", "Trithemius, Steganographia (written here)", "Trithemius, Antipalus Maleficiorum"],
            "archives": ["Würzburg University Library — Trithemius manuscripts"],
            "note": "Würzburg was the seat of Trithemius's abbey of St James and the site of one of the defining encounters in Renaissance Hermetic history: Agrippa visited Trithemius in 1509–10, showed him the manuscript of De Occulta Philosophia, and refined it under the abbot's guidance before its eventual publication."
        },
    }

    LOCATION_TAGLINES = {
        "alexandria":        "Probable site of the philosophical Hermetica; cradle of Greco-Egyptian syncretism",
        "hermopolis":        "Cult city of Thoth; mythological homeland of Hermetic wisdom",
        "florence":          "Ficino's 1463 Corpus Hermeticum translation; heart of Renaissance Hermeticism",
        "harran":            "Sabian community maintaining Neoplatonic and Hermetic traditions into the Islamic period",
        "baghdad":           "Central site of Arabic Hermetic transmission under the Abbasid caliphate",
        "akhmim":            "Birthplace of Zosimos, Late Antiquity's foremost alchemical author",
        "akhmim_expanded":   "Home of Zosimos; site of Hermetic alchemical and visionary literature, c. 300 CE",
        "panopolis":         "Panopolis / Akhmim — home of Zosimos of Panopolis (fl. c. 300 CE)",
        "toledo":            "12th-century translation centre; Arabic Hermetic texts enter Latin Europe",
        "rome":              "Neoplatonic philosophy; Kircher's Egyptology; Bruno's martyrdom (1600)",
        "memphis":           "Memphite theology of Ptah as a source of Hermetic cosmology",
        "thebes":            "Great temple city whose Amun theology informed Hermetic religious synthesis",
        "coptos":            "Crossroads of Hermetic pilgrimage routes and trans-Egyptian commerce",
        "assuan":            "Southern Egyptian temple traditions preserving ancient priestly knowledge",
        "antioch":           "Base of Iamblichus's Neoplatonic-theurgic school, c. 300–325 CE",
        "constantinople":    "Byzantine custodian of the Greek Hermetic manuscript tradition",
        "damascus":          "Major Islamic centre for preservation and study of Hermetic texts",
        "cairo":             "Arabic alchemical synthesis; Khalid ibn Yazid's circle; Fatimid learning",
        "cordoba":           "Islamic Andalusia: Picatrix tradition and Hermetic natural philosophy",
        "venice":            "Gateway for Greek manuscripts; Renaissance Hermetic printing centre",
        "mantua":            "Gonzaga court patronage of Renaissance humanism and Hermetic scholarship",
        "prague_hermetic":   "Alchemical capital of Europe under Rudolf II, r. 1576–1612",
        "prague":            "Prague: centre of Rudolf II's court alchemy and occult patronage",
        "strasbourg":        "Centre of Paracelsian medicine and early Rosicrucian activity",
        "paris":             "Scholastic and alchemical learning; major Hermetic manuscript centre",
        "oxford":            "Medieval natural philosophy; Roger Bacon; Newton's alchemical studies",
        "basra":             "Home of the Ikhwan al-Safa, synthesisers of Hermetic and Islamic thought",
        "london":            "English alchemy, Rosicrucian debate, and Royal Society natural philosophy",
        "cologne":           "Agrippa's birthplace; Albertus Magnus's studium; De Occulta Philosophia (1531)",
        "wurzburg":          "Trithemius's abbey; where Agrippa drafted De Occulta Philosophia (1510)",
    }

    # Build person_locations lookup: slug -> list of (person_id, name, role, role_primary)
    person_loc_lookup = {}
    try:
        cursor.execute("""
            SELECT pl.location_slug, p.person_id, p.name, pl.role, p.role_primary
            FROM person_locations pl
            JOIN persons p ON pl.person_id = p.person_id
            ORDER BY pl.location_slug, p.name
        """)
        for loc_slug, pid, pname, prole, role_primary in cursor.fetchall():
            person_loc_lookup.setdefault(loc_slug, []).append((pid, pname, prole, role_primary))
    except Exception:
        pass

    loc_js_objects = []
    for l in locs:
        slug = l["slug"] if "slug" in l.keys() else ""
        desc = (l["description"] or "").replace('"', "'").replace('\n', ' ')
        extras = LOCATION_EXTRAS.get(slug, {})
        # Enrich figures from person_locations DB — build hyperlinks
        db_figure_links = []
        for pid, pname, prole, role_primary in person_loc_lookup.get(slug, []):
            folder = "scholars" if role_primary == "SCHOLAR" else "biographies"
            link = f"{REPO_URL}/{folder}/{pid}.html"
            db_figure_links.append(f"<a href='{link}' style='color:#d4af37;text-decoration:underline;text-decoration-color:rgba(212,175,55,0.4)'>{pname}</a> ({prole.lower()})")
        extra_figures = extras.get("figures", [])
        all_figures = db_figure_links if db_figure_links else extra_figures
        figures_html = ""
        if all_figures:
            figures_html = "<br><b style='color:#d4af37'>Key Figures:</b> " + "; ".join(all_figures)
        texts_html = ""
        if extras.get("texts"):
            texts_html = "<br><b style='color:#d4af37'>Key Texts:</b> " + "; ".join(extras["texts"])
        archives_html = ""
        if extras.get("archives"):
            archives_html = "<br><b style='color:#d4af37'>Manuscript Archives:</b> " + "; ".join(extras["archives"])
        note_html = ""
        if extras.get("note"):
            note_html = f"<br><br><em style='color:#a0a0a0'>{extras['note']}</em>"
        full_popup = f"{desc}{figures_html}{texts_html}{archives_html}{note_html}"
        tagline = LOCATION_TAGLINES.get(slug, "")
        loc_js_objects.append(
            f'{{ "label": {repr(l["label"])}, "lat": {l["lat"]}, "lng": {l["lng"]}, '
            f'"tagline": {repr(tagline)}, '
            f'"desc": {repr(l["description"] or "")}, "popup": {repr(full_popup)} }}'
        )

    loc_js_array = "[" + ",\n".join(loc_js_objects) + "]"

    # ── PEREGRINATIONS DATA ────────────────────────────────────────────────────
    JOURNEYS = {
        "giordano_bruno": {
            "name": "Giordano Bruno",
            "life": "Philosopher & Cosmologist, 1548–1600",
            "stops": [
                {"label": "Nola / Naples", "lat": 40.85, "lng": 14.27, "year": "1548–1576",
                 "bullets": ["Born at Nola, near Naples, c. 1548, son of a soldier", "Entered the Dominican Order at the convent of San Domenico Maggiore, Naples, 1565", "Absorbed Hermetic philosophy, the art of memory, and Lullian combinatorics", "Suspected of heresy for concealing forbidden books; fled the order in 1576"]},
                {"label": "Rome", "lat": 41.90, "lng": 12.50, "year": "1576",
                 "bullets": ["Brief stop in Rome, where his troubles with the Church followed him", "Left Italy for good, crossing the Alps into Protestant Europe", "Began the wandering life that would define the rest of his career"]},
                {"label": "Geneva", "lat": 46.20, "lng": 6.14, "year": "1578–1579",
                 "bullets": ["Joined the Calvinist community but quickly attacked a professor's logic in print", "Arrested and forced to recant; excommunicated by the Calvinist consistory", "Remarked that he had merely moved from one Inquisition to another"]},
                {"label": "Paris", "lat": 48.86, "lng": 2.35, "year": "1579–1583",
                 "bullets": ["Lectured at the Sorbonne on Aristotle; won the favour of Henri III", "Demonstrated his extraordinary artificial memory system before the king", "Published De umbris idearum (1582) and the comedy Il Candelaio", "Entered the household of the French ambassador Michel de Castelnau"]},
                {"label": "London", "lat": 51.51, "lng": -0.13, "year": "1583–1585",
                 "bullets": ["Lived at the French embassy in London under Castelnau's protection", "Moved in circles around Philip Sidney, Fulke Greville, and John Florio", "Wrote his six major Italian Hermetic dialogues: La cena de le ceneri, De la causa, De l'infinito", "His Copernican cosmology and infinite-universe metaphysics scandalised Oxford scholars"]},
                {"label": "Frankfurt", "lat": 50.11, "lng": 8.68, "year": "1590–1591",
                 "bullets": ["Lodged with a Carmelite convent while using Frankfurt's printers", "Published his Latin metaphysical trilogy: De monade, De minimo, De immenso", "These works elaborate his Hermetic-Neoplatonic vision of the One and the infinite", "Accepted a fatal invitation from the Venetian nobleman Giovanni Mocenigo"]},
                {"label": "Venice", "lat": 45.44, "lng": 12.32, "year": "1591–1592",
                 "bullets": ["Invited by Mocenigo to teach him the art of memory and secret philosophy", "Mocenigo, disappointed by the instruction, denounced him to the Inquisition, May 1592", "Arrested by the Venetian Inquisition; transferred to Rome and imprisoned in Castel Sant'Angelo"]},
                {"label": "Rome", "lat": 41.90, "lng": 12.50, "year": "1593–1600",
                 "bullets": ["Eight years of imprisonment and interrogation by the Roman Inquisition", "Refused to recant his cosmological and metaphysical positions despite sustained pressure", "Burned at the stake at Campo de' Fiori, 17 February 1600", "Became a martyr of free thought for Enlightenment and Hermetic traditions alike"]},
            ]
        },
        "pico_della_mirandola": {
            "name": "Giovanni Pico della Mirandola",
            "life": "Philosopher & Kabbalist, 1463–1494",
            "stops": [
                {"label": "Mirandola", "lat": 44.88, "lng": 11.06, "year": "1463–1477",
                 "bullets": ["Born 24 February 1463, scion of the ruling dynasty of Mirandola", "Prodigious child; reportedly memorised the Psalter by age ten", "Destined for a Church career and sent to Bologna to study canon law"]},
                {"label": "Bologna", "lat": 44.50, "lng": 11.34, "year": "1477–1479",
                 "bullets": ["Studies canon law at the University of Bologna", "Quickly abandons law for philosophy and theology", "Begins intensive study of Greek, Latin, Hebrew, and Arabic"]},
                {"label": "Ferrara", "lat": 44.84, "lng": 11.62, "year": "1479–1480",
                 "bullets": ["Studies at the University of Ferrara under distinguished humanists", "Extends knowledge of Arabic philosophy through Averroist commentaries", "First encounters with Kabbalistic texts, transmitted by Jewish scholars"]},
                {"label": "Padua", "lat": 45.41, "lng": 11.88, "year": "1480–1482",
                 "bullets": ["Studies Averroist Aristotelianism at the leading Italian philosophical centre", "Meets Elia del Medigo, who teaches him Hebrew and opens the Kabbalistic tradition", "Acquires manuscripts of Jewish mystical texts that will shape his later synthesis"]},
                {"label": "Florence", "lat": 43.77, "lng": 11.26, "year": "1484–1485",
                 "bullets": ["Meets Marsilio Ficino; immerses in the Neoplatonic circle of the Medici", "Reads the freshly translated Corpus Hermeticum alongside Ficino's Theologia Platonica", "Lorenzo de' Medici becomes his patron, protector, and close friend"]},
                {"label": "Paris", "lat": 48.86, "lng": 2.35, "year": "1485–1486",
                 "bullets": ["Studies theology at the University of Paris", "Acquires deeper knowledge of Kabbalistic texts from Jewish scholars in France", "Plans his audacious 900 Theses, to be defended before all of Christendom in Rome"]},
                {"label": "Rome", "lat": 41.90, "lng": 12.50, "year": "1486–1488",
                 "bullets": ["Proposes 900 Theses from all branches of philosophy for open public disputation", "Writes the Oratio de dignitate hominis (Oration on the Dignity of Man) as the introduction", "Thirteen of his theses condemned by Pope Innocent VIII; he publishes an Apology", "Arrested at Vincennes on papal orders; released through Medici diplomatic pressure"]},
                {"label": "Florence", "lat": 43.77, "lng": 11.26, "year": "1488–1494",
                 "bullets": ["Returns under Lorenzo de' Medici's protection; the Pope eventually grants a pardon", "Writes Heptaplus (seven-fold allegorical commentary on Genesis) and De ente et uno", "Falls increasingly under the influence of the fiery Dominican Savonarola", "Dies 17 November 1494, aged 31, on the very day Charles VIII of France entered Florence"]},
            ]
        },
        "cornelius_agrippa": {
            "name": "Heinrich Cornelius Agrippa",
            "life": "Philosopher & Occultist, 1486–1535",
            "stops": [
                {"label": "Cologne", "lat": 50.94, "lng": 6.96, "year": "1486–c.1506",
                 "bullets": ["Born at Nettesheim near Cologne, 14 September 1486", "Educated at the University of Cologne in the arts and humanities", "Enters the secretarial service of Maximilian I's imperial court", "Begins forming a circle of friends devoted to occult philosophy"]},
                {"label": "Paris", "lat": 48.86, "lng": 2.35, "year": "c.1506–1507",
                 "bullets": ["Studies in Paris; forms a secret philosophical society", "Absorbs the full range of Neoplatonic, Hermetic, and Kabbalistic literature", "Begins drafting the project that will become De Occulta Philosophia"]},
                {"label": "Dole, Burgundy", "lat": 47.10, "lng": 5.49, "year": "1509",
                 "bullets": ["Lectures publicly on Johann Reuchlin's De verbo mirifico", "A Franciscan friar accuses him of Judaizing before Margaret of Austria", "Forced to leave Dole; first of many collisions with ecclesiastical authority"]},
                {"label": "Würzburg", "lat": 49.80, "lng": 9.94, "year": "1509–1510",
                 "bullets": ["Visits the Abbot Trithemius, the greatest living authority on ceremonial magic", "Presents his manuscript of De Occulta Philosophia; Trithemius responds with enthusiasm", "Trithemius urges him to communicate the work only to the learned and worthy", "The visit is the defining mentorship of Renaissance Hermetic philosophy"]},
                {"label": "Pavia", "lat": 45.19, "lng": 9.16, "year": "1512–1515",
                 "bullets": ["Lectures at the University of Pavia on Hermes Trismegistus and the Pauline epistles", "Marries his first wife; develops his Hermetic theology in dialogue with colleagues", "Loses his position when French forces sack Pavia; begins wandering again"]},
                {"label": "Metz", "lat": 49.12, "lng": 6.18, "year": "1518–1520",
                 "bullets": ["Serves as city advocate (syndic) of Metz", "Famously defends a woman accused of witchcraft, attacking the Malleus Maleficarum", "His defence enrages the Dominican inquisitor Nicolas Savin; he is forced to leave"]},
                {"label": "Lyon", "lat": 45.75, "lng": 4.83, "year": "1524–1527",
                 "bullets": ["Serves as personal physician to Louise of Savoy, mother of Francis I", "Writes De incertitudine et vanitate scientiarum (On the Vanity of the Arts and Sciences)", "Falls from royal favour; Louise refuses to pay his salary; leaves in bitter poverty"]},
                {"label": "Antwerp", "lat": 51.22, "lng": 4.40, "year": "1528–1530",
                 "bullets": ["Appointed court historian and archivist to Margaret of Austria", "Prepares De Occulta Philosophia for its definitive revision and eventual publication", "Writes defences of women's learning and dignity; advocates for imprisoned debtors"]},
                {"label": "Cologne", "lat": 50.94, "lng": 6.96, "year": "1531",
                 "bullets": ["Publishes De Occulta Philosophia libri tres — the most ambitious synthesis of Renaissance magic", "Also publishes De incertitudine et vanitate scientiarum", "Immediately attacked by Dominican theologians across Europe", "Arrested briefly in Bonn (1532); releases a bitter defence of his work"]},
            ]
        },
        "john_dee": {
            "name": "John Dee",
            "life": "Mathematician, Astrologer & Angelic Philosopher, 1527–1608",
            "stops": [
                {"label": "London", "lat": 51.51, "lng": -0.13, "year": "1527–1542",
                 "bullets": ["Born 13 July 1527 in Tower Ward, London, son of a minor royal official", "Early genius for mathematics and natural philosophy", "Enters St John's College, Cambridge, aged 15"]},
                {"label": "Cambridge", "lat": 52.21, "lng": 0.12, "year": "1542–1546",
                 "bullets": ["Studies at St John's College; studies 18 hours a day, sleeps only four", "Becomes one of the original Fellows of the newly founded Trinity College", "Passionate about mathematics, astronomy, and navigation"]},
                {"label": "Louvain", "lat": 50.88, "lng": 4.70, "year": "1547–1550",
                 "bullets": ["Studies with the cartographer Gerardus Mercator and mathematician Gemma Frisius", "Acquires rare mathematical instruments, globes, and manuscripts", "Develops world-leading expertise in navigation, practical mathematics, and astronomy"]},
                {"label": "Paris", "lat": 48.86, "lng": 2.35, "year": "1550",
                 "bullets": ["Lectures on Euclid's Elements at the Collège de Reims to reportedly overflowing audiences", "Offered prestigious permanent positions by the French court; declines all of them", "Returns to England laden with instruments and books"]},
                {"label": "Mortlake, London", "lat": 51.51, "lng": -0.13, "year": "1551–1583",
                 "bullets": ["Builds one of Europe's greatest private libraries at his Mortlake home: over 3,000 volumes", "Serves as astrologer and advisor to Elizabeth I; selects her coronation date", "Begins angelic conversations (the 'actions') with the medium Edward Kelley using a crystal stone", "The Enochian language, revealed by the angels, becomes central to Western esoteric tradition"]},
                {"label": "Kraków", "lat": 50.06, "lng": 19.94, "year": "1583–1584",
                 "bullets": ["Departs England with Kelley under the patronage of Polish nobleman Albert Łaski", "Continues the angel conversations; Uriel and other spirits deliver extensive instructions", "Moves toward the Habsburg imperial court seeking a royal audience"]},
                {"label": "Prague", "lat": 50.08, "lng": 14.44, "year": "1584–1585",
                 "bullets": ["Granted audience with Emperor Rudolf II at Prague Castle", "Presents the angels' cosmological messages to the Emperor; Rudolf II is intrigued but cautious", "Expelled from Bohemia by the papal nuncio after eight months"]},
                {"label": "Třeboň, Bohemia", "lat": 49.01, "lng": 14.77, "year": "1586–1589",
                 "bullets": ["Hosted by the Bohemian nobleman Wilhelm von Rosenberg at Třeboň Castle", "The angels command Dee and Kelley to share their wives — a crisis that fractures their partnership", "Kelley (now a celebrated alchemist) parts ways with Dee permanently", "Dee resolves to return to England after years of fruitless wandering"]},
                {"label": "Mortlake, London", "lat": 51.51, "lng": -0.13, "year": "1589–1608",
                 "bullets": ["Returns to Mortlake to find his library plundered of some 800 books and instruments", "Appointed Warden of Christ's College, Manchester (1595–1604); meets local hostility", "Falls into poverty and obscurity; his supernatural claims discredited by the new generation", "Dies in his home at Mortlake, December 1608/9"]},
            ]
        },
        "johannes_trithemius": {
            "name": "Johannes Trithemius",
            "life": "Abbot, Encyclopedist & Cryptographer, 1462–1516",
            "stops": [
                {"label": "Trittenheim", "lat": 49.84, "lng": 6.89, "year": "1462–c.1479",
                 "bullets": ["Born 1 February 1462 at Trittenheim on the Moselle River", "Childhood marked by poverty and a harsh stepfather; intellectual gifts appear early", "Escapes by walking to Heidelberg to find education and a better life"]},
                {"label": "Heidelberg", "lat": 49.40, "lng": 8.69, "year": "c.1479–1482",
                 "bullets": ["Studies at the University of Heidelberg: logic, rhetoric, Latin poetry, philosophy", "Seeks out the most learned teachers of his generation", "Embraces the ideals of the Rhenish Humanists; dreams of a great scholarly library"]},
                {"label": "Sponheim", "lat": 49.89, "lng": 7.57, "year": "1483–1506",
                 "bullets": ["Arrives at the Benedictine monastery of Sponheim almost by accident during a snowstorm", "Elected Abbot aged 21; the community had only ten monks and forty-eight books", "Builds the library from forty-eight to over 2,000 volumes through relentless acquisition", "Writes Liber de scriptoribus ecclesiasticis (1494) — the first printed bio-bibliography", "Writes the Steganographia, a controversial system of angelic cryptography"]},
                {"label": "Frankfurt", "lat": 50.11, "lng": 8.68, "year": "c.1490s–1506",
                 "bullets": ["Attends the Frankfurt Book Fair annually to acquire manuscripts and printed books", "Establishes correspondence with Erasmus, Reuchlin, and the leading humanists of Europe", "Becomes the most widely connected German scholar of his generation"]},
                {"label": "Würzburg", "lat": 49.80, "lng": 9.94, "year": "1506–1516",
                 "bullets": ["Forced from Sponheim by his own monks after disputes over his strict rule", "Appointed Abbot of the Scots Monastery (St James) in Würzburg by the Bishop", "Receives Agrippa's visit in 1509–10; approves the manuscript of De Occulta Philosophia", "Writes the Polygraphia (on ciphers and secret writing), presented to Maximilian I", "Dies at Würzburg, 13 December 1516; epitaph honours him as 'a most learned man'"]},
            ]
        },
        "kenelm_digby": {
            "name": "Sir Kenelm Digby",
            "life": "Natural Philosopher, Alchemist & Founding Fellow of the Royal Society, 1603–1665",
            "stops": [
                {"label": "Gayhurst, Bucks.", "lat": 52.07, "lng": -0.74, "year": "1603–1618",
                 "bullets": ["Born 11 July 1603 at Gayhurst (then called Gothurst), Buckinghamshire", "Father executed for the Gunpowder Plot (1606); Digby raised a Catholic in Protestant England", "Recognised as a prodigy in mathematics and languages from childhood"]},
                {"label": "Oxford", "lat": 51.75, "lng": -1.25, "year": "1618",
                 "bullets": ["Matriculates at Gloucester Hall (later Worcester College), Oxford", "Leaves without a degree, as was customary for Catholic gentlemen", "Begins tours of France and Spain in the company of his guardian, the diplomat Sir John Digby"]},
                {"label": "Florence", "lat": 43.77, "lng": 11.26, "year": "c.1620",
                 "bullets": ["Tours Italy with Sir John Digby's diplomatic entourage", "Reconverts fully to Catholicism in Florence", "Encounters Italian natural philosophy, Neoplatonism, and the memory of the Hermetic tradition"]},
                {"label": "London", "lat": 51.51, "lng": -0.13, "year": "1623–1627",
                 "bullets": ["Secretly marries the celebrated beauty Venetia Stanley in 1625", "Serves at court; involved in diplomatic intrigues on behalf of Charles I", "Begins experiments in chemistry and natural philosophy in his private laboratory"]},
                {"label": "Scanderoon (Iskenderun)", "lat": 36.60, "lng": 36.17, "year": "1627–1628",
                 "bullets": ["Commands a royal naval expedition to the Eastern Mediterranean", "Battle of Scanderoon, June 1628: defeats a combined Venetian and French fleet", "The victory makes him famous across Europe; he returns to England a celebrated hero"]},
                {"label": "Paris", "lat": 48.86, "lng": 2.35, "year": "1636–1637",
                 "bullets": ["Venetia dies suddenly in May 1633; Digby retires to Paris in grief and study", "Meets René Descartes; they hold extended philosophical conversations", "Attends Mersenne's circle; meets Hobbes, Gassendi, and the leading natural philosophers of Europe", "Begins systematic chemical experiments that will result in his major works"]},
                {"label": "London", "lat": 51.51, "lng": -0.13, "year": "1643",
                 "bullets": ["Returns briefly to England during the Civil War", "Experiments with the 'powder of sympathy' (weapon salve) for wound-healing by action at a distance", "His theory draws on Paracelsian and Helmontian natural philosophy"]},
                {"label": "Paris", "lat": 48.86, "lng": 2.35, "year": "1644–1660",
                 "bullets": ["Long Royalist exile; continues chemical experiments and philosophical writing", "Discourse on the Vegetation of Plants (delivered at the Montmor Academy, 1658) — landmark in natural philosophy", "Maintains the Hartlib correspondence network as a bridge between English and Continental learning"]},
                {"label": "London", "lat": 51.51, "lng": -0.13, "year": "1660–1665",
                 "bullets": ["Returns with the Restoration of Charles II", "Among the founding Fellows of the Royal Society (1660) — linking Hermetic natural philosophy to the new science", "Gives famous demonstrations of the 'powder of sympathy' before the Royal Society", "Dies 11 June 1665; remembered as an eccentric genius at the crossroads of two intellectual worlds"]},
            ]
        },
    }
    journeys_json = json.dumps(JOURNEYS, ensure_ascii=False)

    map_content = f"""
    <main class="page-container">
        <h1 class="title-large">Interactive Geography of Hermeticism</h1>
        <p class="text-subtitle">Major centres of transmission, translation, and practice across the ancient and medieval world.</p>

        <div id="map-info-panel" style="display:none; margin-bottom:1rem; padding:1.5rem 2rem; background:var(--bg-card); border:1px solid var(--border); border-radius:12px; border-left:4px solid var(--accent);">
            <div id="map-info-title" style="font-family:var(--font-display); font-size:1.4rem; color:var(--accent-light); margin-bottom:0.5rem;"></div>
            <div id="map-info-body" style="font-size:0.95rem; line-height:1.7; color:var(--text-main);"></div>
        </div>

        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin=""/>
        <link rel="stylesheet" href="https://unpkg.com/leaflet.markercluster@1.4.1/dist/MarkerCluster.css" crossorigin=""/>
        <link rel="stylesheet" href="https://unpkg.com/leaflet.markercluster@1.4.1/dist/MarkerCluster.Default.css" crossorigin=""/>
        <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>
        <script src="https://unpkg.com/leaflet.markercluster@1.4.1/dist/leaflet.markercluster.js" crossorigin=""></script>

        <!-- Mode switcher -->
        <div class="hm-mode-bar">
            <button id="btn-explore-mode" class="hm-mode-btn hm-mode-active">&#9711; Map</button>
            <button id="btn-journey-mode" class="hm-mode-btn">&#10022; Peregrinations</button>
        </div>

        <!-- Main flex row: left panel | map | journey slides -->
        <div id="map-flex-row" style="display:flex; gap:0; align-items:flex-start;">

            <!-- Left panel (185px) -->
            <div id="map-left-col" style="width:185px; flex-shrink:0; background:var(--bg-card); border:1px solid var(--border); border-radius:8px 0 0 8px; height:600px; overflow:hidden; display:flex; flex-direction:column;">
                <!-- Explore mode: location list -->
                <div id="panel-explore" style="display:flex; flex-direction:column; height:100%;">
                    <div class="hm-panel-hdr">Locations</div>
                    <div id="sidebar-list" style="flex:1; overflow-y:auto; padding:0.2rem 0;"></div>
                </div>
                <!-- Journey mode: figure selector -->
                <div id="panel-journey" style="display:none; flex-direction:column; height:100%;">
                    <div class="hm-panel-hdr">Select figure</div>
                    <div id="journey-figure-list" style="flex:1; overflow-y:auto; padding:0.2rem 0;"></div>
                </div>
            </div>

            <!-- Map -->
            <div id="map" style="flex:1; height:600px; border-top:1px solid var(--border); border-bottom:1px solid var(--border); background:var(--bg-card);"></div>

            <!-- Journey slide panel (hidden until a figure is selected) -->
            <div id="journey-slides" style="display:none; width:275px; flex-shrink:0; height:600px; background:var(--bg-card); border:1px solid var(--border); border-radius:0 8px 8px 0; flex-direction:column; overflow:hidden;">
                <div style="padding:1rem 1rem 0.75rem; border-bottom:1px solid var(--border); background:rgba(212,175,55,0.05); flex-shrink:0;">
                    <div id="js-figure-name" style="font-family:var(--font-display); font-size:1rem; color:var(--accent-light); line-height:1.3; font-weight:600;"></div>
                    <div id="js-figure-life" style="font-size:0.72rem; color:var(--text-muted); margin-top:0.2rem;"></div>
                </div>
                <div style="padding:0.7rem 1rem 0.5rem; border-bottom:1px solid rgba(255,255,255,0.05); flex-shrink:0;">
                    <div style="display:flex; align-items:baseline; gap:0.5rem; margin-bottom:0.15rem;">
                        <span id="js-stop-num" style="font-size:0.68rem; font-weight:700; color:var(--accent); background:rgba(212,175,55,0.14); padding:0.1rem 0.4rem; border-radius:3px; white-space:nowrap;"></span>
                        <span id="js-stop-city" style="font-size:0.92rem; font-weight:600; color:var(--text-main);"></span>
                    </div>
                    <div id="js-stop-year" style="font-size:0.75rem; color:var(--text-muted); font-style:italic;"></div>
                </div>
                <ul id="js-bullets" style="flex:1; overflow-y:auto; margin:0; padding:0.7rem 1rem 0.7rem 1.6rem; font-size:0.8rem; line-height:1.65; color:var(--text-main); list-style:disc;"></ul>
                <div style="padding:0.6rem 0.8rem; border-top:1px solid var(--border); display:flex; align-items:center; gap:0.4rem; flex-shrink:0;">
                    <button id="js-prev" class="jp-ctrl-btn" title="Previous stop">&#9664;</button>
                    <button id="js-play" class="jp-ctrl-btn jp-play-btn" title="Play / Pause">&#9646;&#9646;</button>
                    <button id="js-next" class="jp-ctrl-btn" title="Next stop">&#9654;</button>
                    <span id="js-progress" style="font-size:0.7rem; color:var(--text-muted); margin-left:auto;"></span>
                </div>
            </div>

        </div><!-- end flex row -->

        <div id="explore-footer" style="margin-top:1.5rem; padding:1rem 2rem; background:var(--bg-card); border:1px solid var(--border); border-radius:8px; font-size:0.85rem; color:var(--text-muted);">
            <strong style="color:var(--accent)">Map:</strong> Hover a marker for its tagline. Click for full details — key figures, texts, archives. Use the sidebar to jump to any location. &nbsp;|&nbsp;
            <strong style="color:var(--accent)">Peregrinations:</strong> Select a philosopher to animate their journey across the map, stop by stop.
        </div>

        <script>
        document.addEventListener('DOMContentLoaded', function() {{

            // ── MAP SETUP ──────────────────────────────────────────────────
            const HERMETIC_BOUNDS = [[19, -16], [58, 56]];
            const map = L.map('map', {{
                maxBounds: HERMETIC_BOUNDS,
                maxBoundsViscosity: 0.85,
                minZoom: 3
            }}).fitBounds([[23, -6], [53, 50]]);
            L.tileLayer('https://{{s}}.basemaps.cartocdn.com/dark_all/{{z}}/{{x}}/{{y}}{{r}}.png', {{
                attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
                maxZoom: 18
            }}).addTo(map);

            const locations = {loc_js_array};
            const journeys  = {journeys_json};

            const hermeticIcon = L.divIcon({{
                className: 'hermetic-marker',
                html: '<div class="hm-dot"></div>',
                iconSize: [16, 16], iconAnchor: [8, 8]
            }});

            const infoPanel = document.getElementById('map-info-panel');
            const infoTitle = document.getElementById('map-info-title');
            const infoBody  = document.getElementById('map-info-body');

            const clusterGroup = L.markerClusterGroup({{
                maxClusterRadius: 40,
                iconCreateFunction: function(cluster) {{
                    return L.divIcon({{
                        className: 'hermetic-cluster',
                        html: '<div class="hc-dot">' + cluster.getChildCount() + '</div>',
                        iconSize: [34, 34], iconAnchor: [17, 17]
                    }});
                }}
            }});
            const markerRefs = {{}};

            // Build explore sidebar
            const sidebarList = document.getElementById('sidebar-list');
            [...locations].sort((a,b) => a.label.localeCompare(b.label)).forEach(loc => {{
                const btn = document.createElement('button');
                btn.textContent = loc.label;
                btn.dataset.label = loc.label;
                btn.className = 'sidebar-loc-btn';
                btn.addEventListener('click', function() {{
                    document.querySelectorAll('.sidebar-loc-btn').forEach(b => b.classList.remove('active'));
                    btn.classList.add('active');
                    const ref = markerRefs[loc.label];
                    if (ref) clusterGroup.zoomToShowLayer(ref, () => ref.fire('click'));
                }});
                sidebarList.appendChild(btn);
            }});

            // Add explore markers
            locations.forEach(loc => {{
                const marker = L.marker([loc.lat, loc.lng], {{icon: hermeticIcon}});
                const ttHtml = loc.tagline
                    ? `<b style="font-size:0.88rem">${{loc.label}}</b><br><span style="font-size:0.78rem;color:#c8a84b;font-weight:400">${{loc.tagline}}</span>`
                    : `<b>${{loc.label}}</b>`;
                marker.bindTooltip(ttHtml, {{permanent:false, direction:'top', offset:[0,-10], className:'hermetic-tooltip'}});
                marker.on('click', function() {{
                    infoTitle.textContent = loc.label;
                    infoBody.innerHTML = loc.popup;
                    infoPanel.style.display = 'block';
                    infoPanel.scrollIntoView({{behavior:'smooth', block:'nearest'}});
                    document.querySelectorAll('.sidebar-loc-btn').forEach(b => b.classList.toggle('active', b.dataset.label === loc.label));
                }});
                marker.bindPopup(`<b style="font-size:1.05rem;color:#d4af37">${{loc.label}}</b><br><br>${{loc.desc}}<br><br><em style="font-size:0.8rem;color:#888">Click marker or scroll up for full details</em>`, {{className:'hermetic-popup', maxWidth:320}});
                markerRefs[loc.label] = marker;
                clusterGroup.addLayer(marker);
            }});
            clusterGroup.addTo(map);

            // ── PEREGRINATIONS ─────────────────────────────────────────────
            let currentJourney = null;
            let currentStop    = 0;
            let journeyTimer   = null;
            let isPlaying      = false;
            let jMarkers       = [];
            let jLines         = [];
            const STOP_INTERVAL = 5000; // ms per stop when auto-playing

            // Build figure list in the journey panel
            const figListEl = document.getElementById('journey-figure-list');
            Object.entries(journeys).forEach(([id, j]) => {{
                const btn = document.createElement('button');
                btn.textContent = j.name;
                btn.dataset.figId = id;
                btn.className = 'jp-figure-btn';
                btn.addEventListener('click', () => selectJourney(id));
                figListEl.appendChild(btn);
            }});

            function selectJourney(figId) {{
                clearJourney();
                currentJourney = journeys[figId];
                if (!currentJourney) return;

                // Highlight selected button
                document.querySelectorAll('.jp-figure-btn').forEach(b => b.classList.remove('active'));
                document.querySelector(`[data-fig-id="${{figId}}"]`)?.classList.add('active');

                // Populate figure header
                document.getElementById('js-figure-name').textContent = currentJourney.name;
                document.getElementById('js-figure-life').textContent = currentJourney.life;

                // Show slide panel
                const slides = document.getElementById('journey-slides');
                slides.style.display = 'flex';
                slides.style.flexDirection = 'column';

                // Draw faint full route
                const coords = currentJourney.stops.map(s => [s.lat, s.lng]);
                const routeLine = L.polyline(coords, {{color:'rgba(212,175,55,0.25)', weight:1.5, dashArray:'4,7'}}).addTo(map);
                jLines.push(routeLine);

                // Add numbered stop markers
                currentJourney.stops.forEach((stop, i) => {{
                    const m = L.marker([stop.lat, stop.lng], {{
                        icon: L.divIcon({{
                            className: 'hm-journey-stop',
                            html: `<div class="hjm-dot" id="hjm-${{i}}">${{i+1}}</div>`,
                            iconSize: [26, 26], iconAnchor: [13, 13]
                        }}),
                        zIndexOffset: 900
                    }}).addTo(map);
                    m.on('click', () => {{ pausePlay(); goToStop(i, true); }});
                    jMarkers.push(m);
                }});

                map.fitBounds(routeLine.getBounds(), {{padding:[50, 50]}});
                goToStop(0, false);
                startPlay();
            }}

            function goToStop(i, fly) {{
                if (!currentJourney) return;
                currentStop = i;
                const stop  = currentJourney.stops[i];
                const total = currentJourney.stops.length;

                // Active marker style
                document.querySelectorAll('.hjm-dot').forEach((el, j) => el.classList.toggle('active', j === i));

                // Slide content
                document.getElementById('js-stop-num').textContent  = `Stop ${{i+1}} of ${{total}}`;
                document.getElementById('js-stop-city').textContent = stop.label;
                document.getElementById('js-stop-year').textContent = stop.year;
                document.getElementById('js-bullets').innerHTML = stop.bullets.map(b => `<li>${{b}}</li>`).join('');
                document.getElementById('js-progress').textContent  = `${{i+1}} / ${{total}}`;
                document.getElementById('js-prev').disabled = i === 0;
                document.getElementById('js-next').disabled = i === total - 1;

                // Draw progress line (golden, up to current stop)
                jLines.filter(l => l._jp).forEach(l => map.removeLayer(l));
                jLines = jLines.filter(l => !l._jp);
                if (i > 0) {{
                    const prog = L.polyline(
                        currentJourney.stops.slice(0, i+1).map(s => [s.lat, s.lng]),
                        {{color:'#d4af37', weight:2.5, opacity:0.9}}
                    ).addTo(map);
                    prog._jp = true;
                    jLines.push(prog);
                }}

                // Pan map
                if (fly) map.flyTo([stop.lat, stop.lng], 6, {{duration:1.4, easeLinearity:0.25}});
            }}

            function startPlay() {{
                pausePlay();
                isPlaying = true;
                document.getElementById('js-play').innerHTML = '&#9646;&#9646;';
                journeyTimer = setInterval(() => {{
                    if (currentStop < currentJourney.stops.length - 1) {{
                        goToStop(currentStop + 1, true);
                    }} else {{
                        pausePlay();
                    }}
                }}, STOP_INTERVAL);
            }}

            function pausePlay() {{
                isPlaying = false;
                clearInterval(journeyTimer);
                document.getElementById('js-play').innerHTML = '&#9654;';
            }}

            function clearJourney() {{
                pausePlay();
                jMarkers.forEach(m => map.removeLayer(m));
                jLines.forEach(l => map.removeLayer(l));
                jMarkers = []; jLines = [];
                currentJourney = null;
                document.getElementById('journey-slides').style.display = 'none';
            }}

            // Mode switching
            function setMode(m) {{
                if (m === 'explore') {{
                    clearJourney();
                    clusterGroup.addTo(map);
                    infoPanel.style.display = 'none';
                    document.getElementById('panel-explore').style.display  = 'flex';
                    document.getElementById('panel-journey').style.display  = 'none';
                    document.getElementById('explore-footer').style.display = '';
                    document.getElementById('btn-explore-mode').classList.add('hm-mode-active');
                    document.getElementById('btn-journey-mode').classList.remove('hm-mode-active');
                    map.fitBounds([[23,-6],[53,50]]);
                }} else {{
                    clusterGroup.remove();
                    infoPanel.style.display = 'none';
                    document.getElementById('panel-explore').style.display  = 'none';
                    document.getElementById('panel-journey').style.display  = 'flex';
                    document.getElementById('explore-footer').style.display = 'none';
                    document.getElementById('btn-explore-mode').classList.remove('hm-mode-active');
                    document.getElementById('btn-journey-mode').classList.add('hm-mode-active');
                }}
            }}

            document.getElementById('btn-explore-mode').addEventListener('click', () => setMode('explore'));
            document.getElementById('btn-journey-mode').addEventListener('click', () => setMode('journey'));
            document.getElementById('js-prev').addEventListener('click', () => {{ pausePlay(); if (currentStop > 0) goToStop(currentStop-1, true); }});
            document.getElementById('js-next').addEventListener('click', () => {{ pausePlay(); if (currentJourney && currentStop < currentJourney.stops.length-1) goToStop(currentStop+1, true); }});
            document.getElementById('js-play').addEventListener('click', () => isPlaying ? pausePlay() : startPlay());

        }});
        </script>
        <style>
            /* ── explore markers ── */
            .hm-dot {{
                width:14px; height:14px;
                background:#d4af37; border:2px solid #fff; border-radius:50%;
                box-shadow:0 0 12px #d4af37, 0 0 4px rgba(212,175,55,0.8);
                transition:transform 0.15s; cursor:pointer;
            }}
            .hermetic-marker:hover .hm-dot {{ transform:scale(1.5); box-shadow:0 0 20px #d4af37; }}
            .hc-dot {{
                width:30px; height:30px;
                background:rgba(212,175,55,0.15); border:2px solid #d4af37; border-radius:50%;
                display:flex; align-items:center; justify-content:center;
                color:#d4af37; font-size:11px; font-weight:700;
                box-shadow:0 0 10px rgba(212,175,55,0.35);
            }}
            /* ── popups & tooltips ── */
            .hermetic-popup .leaflet-popup-content-wrapper {{
                background:#141418; color:#e0e0e0;
                border:1px solid rgba(212,175,55,0.4); border-radius:10px;
                font-family:'Inter',sans-serif; font-size:0.9rem; line-height:1.6;
            }}
            .hermetic-popup .leaflet-popup-tip {{ background:#141418; }}
            .hermetic-popup .leaflet-popup-close-button {{ color:#a0a0a0 !important; }}
            .hermetic-tooltip {{
                background:#141418; border:1px solid rgba(212,175,55,0.6); color:#f1d37e;
                font-family:'Outfit',sans-serif; font-size:0.85rem;
                padding:0.4rem 0.85rem; border-radius:6px; font-weight:600;
                box-shadow:0 4px 12px rgba(0,0,0,0.5);
                max-width:280px; line-height:1.4; white-space:normal;
            }}
            .hermetic-tooltip::before {{ border-top-color:rgba(212,175,55,0.6) !important; }}
            /* ── explore sidebar buttons ── */
            .sidebar-loc-btn {{
                display:block; width:100%; text-align:left;
                padding:0.38rem 0.8rem; background:none; border:none;
                border-bottom:1px solid rgba(255,255,255,0.04);
                color:var(--text-main); font-size:0.78rem; cursor:pointer;
                transition:background 0.12s,color 0.12s; line-height:1.3;
            }}
            .sidebar-loc-btn:hover, .sidebar-loc-btn.active {{
                background:rgba(212,175,55,0.12); color:#d4af37;
            }}
            /* ── mode bar ── */
            .hm-mode-bar {{
                display:flex; gap:0.5rem; margin:1rem 0 0;
            }}
            .hm-mode-btn {{
                padding:0.45rem 1.1rem; border-radius:6px 6px 0 0;
                background:var(--bg-card); border:1px solid var(--border); border-bottom:none;
                color:var(--text-muted); font-size:0.85rem; cursor:pointer;
                font-family:'Outfit',sans-serif; font-weight:600; letter-spacing:0.03em;
                transition:color 0.15s, background 0.15s;
            }}
            .hm-mode-btn.hm-mode-active {{
                color:var(--accent); background:rgba(212,175,55,0.08);
            }}
            .hm-panel-hdr {{
                font-size:0.72rem; font-weight:700; color:var(--accent);
                padding:0.55rem 0.8rem; border-bottom:1px solid var(--border);
                letter-spacing:0.1em; text-transform:uppercase; flex-shrink:0;
            }}
            /* ── journey figure buttons ── */
            .jp-figure-btn {{
                display:block; width:100%; text-align:left;
                padding:0.5rem 0.8rem; background:none; border:none;
                border-bottom:1px solid rgba(255,255,255,0.04);
                color:var(--text-main); font-size:0.78rem; cursor:pointer;
                transition:background 0.12s,color 0.12s; line-height:1.35;
            }}
            .jp-figure-btn:hover, .jp-figure-btn.active {{
                background:rgba(212,175,55,0.12); color:#d4af37;
            }}
            /* ── journey stop markers ── */
            .hjm-dot {{
                width:24px; height:24px;
                background:#1a1a20; border:2px solid rgba(212,175,55,0.6); border-radius:50%;
                display:flex; align-items:center; justify-content:center;
                color:#d4af37; font-size:10px; font-weight:700; cursor:pointer;
                transition:all 0.2s; box-shadow:0 0 6px rgba(212,175,55,0.3);
            }}
            .hjm-dot.active {{
                background:#d4af37; color:#0a0a0e; border-color:#fff;
                box-shadow:0 0 18px #d4af37, 0 0 6px rgba(212,175,55,0.9);
                transform:scale(1.35);
            }}
            /* ── slide panel controls ── */
            .jp-ctrl-btn {{
                padding:0.35rem 0.7rem; border-radius:5px;
                background:rgba(212,175,55,0.1); border:1px solid rgba(212,175,55,0.35);
                color:#d4af37; cursor:pointer; font-size:0.8rem;
                transition:background 0.12s;
            }}
            .jp-ctrl-btn:hover {{ background:rgba(212,175,55,0.25); }}
            .jp-ctrl-btn:disabled {{ opacity:0.3; cursor:default; }}
            .jp-play-btn {{ min-width:3.5rem; }}
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
        folder = "scholars" if r[2] == "SCHOLAR" else "biographies"
        nodes.append({ "id": r[0], "label": r[1], "group": "PERSON", "role": r[2], "url": f"{REPO_URL}/{folder}/{r[0]}.html" })

    # 2. TEXTS
    cursor.execute("SELECT text_id, title, text_type FROM texts")
    for r in cursor.fetchall():
        nodes.append({ "id": r[0], "label": r[1], "group": "TEXT", "role": r[2], "url": f"{REPO_URL}/texts/{r[0]}.html" })

    # 3. CONCEPTS
    cursor.execute("SELECT slug, label, category FROM concepts")
    for r in cursor.fetchall():
        nodes.append({ "id": r[0], "label": r[1], "group": "CONCEPT", "role": r[2], "url": f"{REPO_URL}/dictionary/{r[0]}.html" })
    
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
            <div style="position:absolute; top:20px; right:20px; z-index:10;">
                <input id="graph-search" type="text" placeholder="Search nodes…" style="background:#141418; border:1px solid rgba(212,175,55,0.5); color:#e0e0e0; padding:0.4rem 0.85rem; border-radius:6px; font-size:0.85rem; outline:none; width:210px; font-family:'Inter',sans-serif;">
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

            const edgeColors = {{
                'DERIVED_FROM': '#9b59b6', 'EXPLAINS': '#27ae60', 'SUBSET_OF': '#3498db',
                'OPPOSED_TO': '#e74c3c', 'RELATED': '#95a5a6', 'THEME': '#d4af37',
                'AUTHORED': '#4a9eff', 'TRANSLATED': '#e67e22', 'INFLUENCED': '#1abc9c',
                'QUOTED': '#f39c12', 'COMMENTED': '#e91e63', 'CRITICIZED': '#ff6b6b',
                'TEACHER_OF': '#f39c12', 'STUDENT_OF': '#a8d8ea', 'CONTEMPORARY': '#888'
            }};
            function edgeColor(d) {{
                return edgeColors[d.type] || 'rgba(255,255,255,0.15)';
            }}

            // Edge hit area (invisible thick line for easier hover)
            const linkHit = svg.append("g")
                .selectAll("line")
                .data(data.links)
                .join("line")
                .attr("stroke", "transparent")
                .attr("stroke-width", 10)
                .style("cursor", "default");

            // Hover tooltip element
            const edgeTip = d3.select("body").append("div")
                .style("position", "fixed")
                .style("display", "none")
                .style("background", "#141418")
                .style("border", "1px solid rgba(212,175,55,0.5)")
                .style("color", "#e0e0e0")
                .style("font-size", "0.8rem")
                .style("padding", "0.4rem 0.8rem")
                .style("border-radius", "6px")
                .style("pointer-events", "none")
                .style("z-index", "9999");

            linkHit.on("mouseover", (event, d) => {{
                const src = typeof d.source === 'object' ? d.source.label : d.source;
                const tgt = typeof d.target === 'object' ? d.target.label : d.target;
                edgeTip.style("display", "block")
                    .html(`<span style="color:${{edgeColors[d.type] || '#aaa'}};font-weight:600">${{d.type || 'RELATED'}}</span><br>${{src}} → ${{tgt}}`);
            }})
            .on("mousemove", event => {{
                edgeTip.style("left", (event.clientX + 14) + "px").style("top", (event.clientY - 10) + "px");
            }})
            .on("mouseout", () => edgeTip.style("display", "none"));

            const link = svg.append("g")
                .selectAll("line")
                .data(data.links)
                .join("line")
                .attr("stroke", d => edgeColor(d))
                .attr("stroke-opacity", 0.5)
                .attr("stroke-width", d => Math.sqrt(d.value))
                .style("pointer-events", "none");

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
                    link.style("stroke", l => (l.source.id === d.id || l.target.id === d.id) ? edgeColor(l) : "rgba(255,255,255,0.05)")
                        .style("stroke-opacity", l => (l.source.id === d.id || l.target.id === d.id) ? 1 : 0.1);
                }})
                .on("mouseout", () => {{
                    link.style("stroke", d => edgeColor(d)).style("stroke-opacity", 0.5);
                }});

            node.on("click", (event, d) => {{
                if (d.url) {{
                    if (event.ctrlKey || event.metaKey) {{
                        window.open(d.url, "_blank");
                    }} else {{
                        window.location.href = d.url;
                    }}
                }}
            }});

            node.append("circle")
                .attr("r", d => d.group === "PERSON" ? 8 : (d.group === "TEXT" ? 6 : 4))
                .attr("fill", d => {{
                    if (d.group === "PERSON") return "#4a9eff";
                    if (d.group === "TEXT") return "#d4af37";
                    return "#20c997";
                }})
                .attr("stroke", "#fff")
                .attr("stroke-width", 1.5)
                .style("cursor", d => d.url ? "pointer" : "default");

            node.append("text")
                .attr("x", 12)
                .attr("y", 4)
                .text(d => d.label)
                .attr("fill", "#fff")
                .style("font-size", "10px")
                .style("pointer-events", "none")
                .style("opacity", 0.7);

            simulation.on("tick", () => {{
                [link, linkHit].forEach(sel => sel
                    .attr("x1", d => d.source.x)
                    .attr("y1", d => d.source.y)
                    .attr("x2", d => d.target.x)
                    .attr("y2", d => d.target.y)
                );
                node.attr("transform", d => `translate(${{d.x}}, ${{d.y}})`);
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

            // Node search / highlight
            document.getElementById('graph-search').addEventListener('input', function() {{
                const q = this.value.toLowerCase().trim();
                if (!q) {{
                    node.style("opacity", 1);
                    node.selectAll("circle").attr("r", d => d.group === "PERSON" ? 8 : (d.group === "TEXT" ? 6 : 4));
                }} else {{
                    node.style("opacity", d => d.label.toLowerCase().includes(q) ? 1 : 0.08);
                    node.selectAll("circle").attr("r", d => {{
                        const base = d.group === "PERSON" ? 8 : (d.group === "TEXT" ? 6 : 4);
                        return d.label.toLowerCase().includes(q) ? base * 2.2 : base;
                    }});
                }}
            }});
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

    # 9. DEBATES PAGE
    DEBATES_CONTENT = """
    <main class="page-container">
        <h1 class="title-large">Modern Historiographical Debates</h1>
        <p class="text-subtitle">Core scholarly arguments and paradigm shifts in the study of Hermeticism.</p>
        
        <div class="prose-content">
            <h2 class="title-medium">1. The Yates Paradigm: Magic and Science</h2>
            <p>Perhaps the most famous debate in the field centers on <b>Frances Yates's</b> thesis that the Renaissance revival of Hermeticism was a primary catalyst for the Scientific Revolution. Yates proposed that the figures of the 'Magus' (Agrippa, Bruno, Dee) were the direct ancestors of the modern scientist.</p>
            <p><b>The Critique:</b> While groundbreaking, later historians like <b>Brian Copenhaver</b> and <b>Edward Grant</b> have argued that the 'Yates Paradigm' overestimates the internal coherence of the 'tradition' and underestimates the role of medieval scholasticism and mechanical philosophy in the rise of science.</p>

            <h2 class="title-medium">2. The Egyptian Hermes vs. The Greek Hermes</h2>
            <p>For much of the 20th century, led by <b>A.J. Festugière</b>, the <i>Corpus Hermeticum</i> was viewed as purely 'Greek' philosophy (Platonic and Stoic) dressed in thin Egyptian costume. This 'Greek' reading saw no real connection to historical Egyptian religion.</p>
            <p><b>The Re-Egyptianization:</b> Starting in the 1980s with <b>Garth Fowden</b> and <b>Jean-Pierre Mahé</b>, scholars began to demonstrate that the Hermetica were deeply rooted in the social and religious landscape of Roman Egypt, with significant links to the Egyptian priesthood and traditional temple cults.</p>

            <h2 class="title-medium">3. The Problem of the 'Two Hermetisms'</h2>
            <p>Scholars traditionally divided the Hermetica into two unrelated groups: the 'Philosophical' Hermetica (contemplative) and the 'Technical' Hermetica (astrology, alchemy, magic). It was assumed they belonged to different social classes or traditions.</p>
            <p><b>The 'Way of Hermes':</b> Current scholarship (notably Fowden) argues for a unified 'Way of Hermes,' where the technical sciences were seen as the practical application of the philosophical principles. They were likely practiced by the same small <b>Hermetic Circles</b> under a master.</p>

            <h2 class="title-medium">4. Gnosis: Dualistic or Monistic?</h2>
            <p>Is Hermeticism a form of Gnosticism? <b>Hans Jonas</b> and others grouped them together as 'dualistic' systems that viewed the material world as evil. However, modern scholars like <b>Wouter Hanegraaff</b> emphasize that most Hermetic texts are 'cosmic-optimistic,' viewing the world as a beautiful manifestation of God.</p>

            <h2 class="title-medium">5. The Casaubon Watershed</h2>
            <p>The 1614 dating of the <i>Corpus Hermeticum</i> by <b>Isaac Casaubon</b> effectively ended the <i>Prisca Theologia</i> narrative. This debate focuses on the <i>Reception History</i>: how did the Hermetic tradition survive as 'Rejected Knowledge' after its claims to ancient Egyptian antiquity were debunked?</p>

            <h2 class="title-medium">6. The Immanence of Ratio</h2>
            <p>A more recent historiographical debate, led by scholars like <b>Mark Damien Delp</b> and <b>David Porreca</b>, focuses on the role of Hermeticism in 12th-century Latin scholasticism. Delp argues that texts like <i>De sex rerum principiis</i> represent an 'immanence of ratio,' where Hermetic cosmology was not seen as external magic but as a rational framework for understanding the physical universe.</p>
            <p><b>Scholastic Integration:</b> This challenges the traditional view that the medieval Church was uniformly hostile to 'pagan' Hermes, showing instead that he was often integrated as a source of legitimate natural philosophy.</p>
        </div>
    </main>
    """
    with open(target_dir / "debates.html", "w", encoding="utf-8") as f:
        f.write(BASE_TEMPLATE.replace("{{title}}", "Historiographical Debates").replace("{{css}}", CSS).replace("{{nav}}", NAV_BAR).replace("{{content}}", DEBATES_CONTENT))

def main():
    try:
        conn = sqlite3.connect(DB_PATH)
    except sqlite3.OperationalError:
        conn = sqlite3.connect(f"file:{DB_PATH.as_posix()}?mode=ro&immutable=1", uri=True)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    # Dual Deployment to fix 404s
    deploy_to(DOCS_DIR, cursor)
    deploy_to(SITE_DIR, cursor)
    
    conn.close()
    print("Dual Deployment complete.")

if __name__ == "__main__":
    main()
