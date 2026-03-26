"""
assemble_cards.py — Generate bio_html for persons and analysis_html for texts.

Stage 8 of pipeline. Assembles rich HTML card content from database fields
and cross-references. No LLM — pure template assembly from existing data.

Idempotent: overwrites bio_html/analysis_html on re-run.
Prerequisite: seed + extract + link stages must have run.
"""

import json
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "db" / "emerald_tablet.db"


def format_paragraphs(text):
    """Convert plain text with newlines to HTML paragraphs."""
    if not text:
        return ""
    paragraphs = text.split('\n\n')
    if len(paragraphs) == 1:
        paragraphs = text.split('\n')
    return ''.join(f'<p>{p.strip()}</p>' for p in paragraphs if p.strip())


def badge(label, color="#7f8c8d"):
    """Generate an inline badge."""
    return f'<span style="display:inline-block;padding:0.15rem 0.5rem;background:{color};color:white;border-radius:3px;font-size:0.75rem;font-weight:600;text-transform:uppercase;margin-left:0.3rem">{label}</span>'


ROLE_COLORS = {
    'AUTHOR': '#27ae60',
    'ATTRIBUTED_AUTHOR': '#2ecc71',
    'TRANSLATOR': '#2980b9',
    'COMMENTATOR': '#8e44ad',
    'EDITOR': '#e67e22',
    'DISCOVERER': '#c0392b',
    'COMPILER': '#16a085',
    'SCHOLAR': '#34495e',
    'MYTHICAL_FIGURE': '#9b59b6',
    'PHILOSOPHER': '#2c3e50',
}

TYPE_COLORS = {
    'PRIMARY_SOURCE': '#c0392b',
    'COMMENTARY': '#8e44ad',
    'COMPILATION': '#e67e22',
    'TREATISE': '#2980b9',
    'ENCYCLOPEDIA': '#16a085',
    'TRANSLATION': '#27ae60',
    'PSEUDO_EPIGRAPHA': '#7f8c8d',
}

CATEGORY_COLORS = {
    'COSMOLOGICAL': '#1a5276',
    'ALCHEMICAL': '#8b4513',
    'PHILOSOPHICAL': '#2c3e50',
    'LINGUISTIC': '#6c3483',
    'THEOLOGICAL': '#c0392b',
    'SCIENTIFIC': '#27ae60',
}


def assemble_person_bio(conn, person_id):
    """Assemble bio_html for a person from DB fields + cross-references."""
    person = conn.execute("""
        SELECT id, person_id, name, name_alt, birth_year, death_year,
               era, role_primary, description
        FROM persons WHERE id = ?
    """, (person_id,)).fetchone()

    if not person:
        return None

    pid, slug, name, name_alt, birth, death, era, role, desc = person

    parts = []

    # Era and dates line
    meta_parts = []
    if era:
        meta_parts.append(era)
    if birth and death:
        meta_parts.append(f"{birth}&ndash;{death}")
    elif birth:
        meta_parts.append(f"b. {birth}")
    elif death:
        meta_parts.append(f"d. {death}")
    if role:
        meta_parts.append(badge(role, ROLE_COLORS.get(role, '#7f8c8d')))

    if meta_parts:
        parts.append(f'<p class="meta" style="color:#6b5d4d;margin-bottom:1rem">{"  &middot;  ".join(meta_parts)}</p>')

    # Alternative names
    if name_alt:
        try:
            alts = json.loads(name_alt)
            if alts:
                parts.append(f'<p style="font-size:0.9rem;color:#6b5d4d;font-style:italic">Also known as: {", ".join(alts)}</p>')
        except (json.JSONDecodeError, TypeError):
            pass

    # Description
    if desc:
        parts.append(format_paragraphs(desc))

    # Associated texts (from person_text_roles)
    roles = conn.execute("""
        SELECT t.text_id, t.title, ptr.role
        FROM person_text_roles ptr
        JOIN texts t ON ptr.text_id = t.id
        WHERE ptr.person_id = ?
        ORDER BY ptr.role, t.title
    """, (pid,)).fetchall()

    if roles:
        parts.append('<h3 style="margin-top:1.5rem;font-size:1.1rem">Associated Texts</h3>')
        for text_id, title, role_name in roles:
            role_badge = badge(role_name, ROLE_COLORS.get(role_name, '#7f8c8d'))
            parts.append(f'<div style="margin:0.5rem 0;padding:0.5rem;background:#faf8f4;border-radius:4px">'
                        f'<a href="../texts/{text_id}.html" style="color:#8b4513;text-decoration:none">{title}</a> '
                        f'{role_badge}</div>')

    # Timeline events involving this person
    events = conn.execute("""
        SELECT year, title, description
        FROM timeline_events
        WHERE person_id = ?
        ORDER BY year
    """, (pid,)).fetchall()

    if events:
        parts.append('<h3 style="margin-top:1.5rem;font-size:1.1rem">Key Events</h3>')
        for year, etitle, edesc in events:
            parts.append(f'<div style="margin:0.4rem 0">'
                        f'<strong>{year}</strong> &mdash; {etitle}'
                        f'{"<br><span style=\"color:#6b5d4d;font-size:0.9rem\">" + edesc + "</span>" if edesc else ""}'
                        f'</div>')

    return '\n'.join(parts)


def assemble_text_analysis(conn, text_id):
    """Assemble analysis_html for a text from DB fields + cross-references."""
    text = conn.execute("""
        SELECT id, text_id, title, title_original, language, text_type,
               date_composed_start, date_composed_end, description, transmission_notes
        FROM texts WHERE id = ?
    """, (text_id,)).fetchone()

    if not text:
        return None

    tid, slug, title, title_orig, lang, ttype, date_start, date_end, desc, trans_notes = text

    parts = []

    # Meta line
    meta_parts = []
    if lang:
        meta_parts.append(lang)
    if ttype:
        meta_parts.append(badge(ttype, TYPE_COLORS.get(ttype, '#7f8c8d')))
    if date_start and date_end:
        meta_parts.append(f"{date_start}&ndash;{date_end} CE")
    elif date_start:
        meta_parts.append(f"ca. {date_start} CE")
    if meta_parts:
        parts.append(f'<p class="meta" style="color:#6b5d4d;margin-bottom:1rem">{"  &middot;  ".join(meta_parts)}</p>')

    # Original title
    if title_orig and title_orig != title:
        parts.append(f'<p style="font-style:italic;color:#6b5d4d">{title_orig}</p>')

    # Description
    if desc:
        parts.append(format_paragraphs(desc))

    # Transmission notes
    if trans_notes:
        parts.append('<h3 style="margin-top:1.5rem;font-size:1.1rem">Transmission</h3>')
        parts.append(format_paragraphs(trans_notes))

    # Associated persons
    persons = conn.execute("""
        SELECT p.person_id, p.name, ptr.role
        FROM person_text_roles ptr
        JOIN persons p ON ptr.person_id = p.id
        WHERE ptr.text_id = ?
        ORDER BY ptr.role, p.name
    """, (tid,)).fetchall()

    if persons:
        parts.append('<h3 style="margin-top:1.5rem;font-size:1.1rem">Associated Persons</h3>')
        for person_slug, pname, role_name in persons:
            role_badge = badge(role_name, ROLE_COLORS.get(role_name, '#7f8c8d'))
            parts.append(f'<div style="margin:0.5rem 0;padding:0.5rem;background:#faf8f4;border-radius:4px">'
                        f'<a href="../persons/{person_slug}.html" style="color:#8b4513;text-decoration:none">{pname}</a> '
                        f'{role_badge}</div>')

    # Related texts
    related = conn.execute("""
        SELECT t.text_id, t.title, tr.relationship_type, tr.notes
        FROM text_relationships tr
        JOIN texts t ON tr.child_text_id = t.id
        WHERE tr.parent_text_id = ?
        UNION
        SELECT t.text_id, t.title, tr.relationship_type, tr.notes
        FROM text_relationships tr
        JOIN texts t ON tr.parent_text_id = t.id
        WHERE tr.child_text_id = ?
    """, (tid, tid)).fetchall()

    if related:
        parts.append('<h3 style="margin-top:1.5rem;font-size:1.1rem">Related Texts</h3>')
        for rel_slug, rel_title, rel_type, notes in related:
            rel_badge = badge(rel_type, '#7f8c8d')
            parts.append(f'<div style="margin:0.5rem 0;padding:0.5rem;background:#faf8f4;border-radius:4px">'
                        f'<a href="../texts/{rel_slug}.html" style="color:#8b4513;text-decoration:none">{rel_title}</a> '
                        f'{rel_badge}'
                        f'{"<br><span style=\"font-size:0.85rem;color:#6b5d4d\">" + notes + "</span>" if notes else ""}'
                        f'</div>')

    # Related concepts
    concepts = conn.execute("""
        SELECT c.slug, c.label, c.category
        FROM concept_text_refs ctr
        JOIN concepts c ON ctr.concept_id = c.id
        WHERE ctr.text_id = ?
        ORDER BY c.label
    """, (tid,)).fetchall()

    if concepts:
        parts.append('<h3 style="margin-top:1.5rem;font-size:1.1rem">Key Concepts</h3>')
        parts.append('<div style="display:flex;flex-wrap:wrap;gap:0.5rem">')
        for cslug, clabel, ccat in concepts:
            color = CATEGORY_COLORS.get(ccat, '#7f8c8d')
            parts.append(f'<a href="../concepts/{cslug}.html" style="display:inline-block;padding:0.3rem 0.7rem;'
                        f'background:{color}22;border:1px solid {color}44;border-radius:4px;color:{color};'
                        f'text-decoration:none;font-size:0.85rem">{clabel}</a>')
        parts.append('</div>')

    # Translation count (for the Emerald Tablet)
    trans_count = conn.execute("""
        SELECT COUNT(*) FROM translations WHERE source_text_id = ?
    """, (tid,)).fetchone()[0]
    if trans_count > 0:
        verse_count = conn.execute("""
            SELECT COUNT(*) FROM translation_verses tv
            JOIN translations t ON tv.translation_id = t.id
            WHERE t.source_text_id = ?
        """, (tid,)).fetchone()[0]
        parts.append(f'<div style="margin-top:1.5rem;padding:1rem;background:#e8f4f8;border-radius:4px">'
                    f'<strong>{trans_count} translations</strong> with {verse_count} verse entries '
                    f'<a href="../translations/emerald-tablet.html" style="color:#2980b9">View parallel translations &rarr;</a>'
                    f'</div>')

    return '\n'.join(parts)


def main():
    if not DB_PATH.exists():
        print("ERROR: Database not found.")
        return

    conn = sqlite3.connect(DB_PATH)

    # Assemble person bios
    persons = conn.execute("SELECT id, person_id FROM persons ORDER BY name").fetchall()
    person_count = 0
    for pid, slug in persons:
        bio = assemble_person_bio(conn, pid)
        if bio:
            conn.execute("UPDATE persons SET bio_html = ? WHERE id = ?", (bio, pid))
            person_count += 1

    # Assemble text analyses
    texts = conn.execute("SELECT id, text_id FROM texts ORDER BY title").fetchall()
    text_count = 0
    for tid, slug in texts:
        analysis = assemble_text_analysis(conn, tid)
        if analysis:
            conn.execute("UPDATE texts SET analysis_html = ? WHERE id = ?", (analysis, tid))
            text_count += 1

    conn.commit()

    print(f"Assembled {person_count} person bios")
    print(f"Assembled {text_count} text analyses")

    # Sample output
    sample = conn.execute("""
        SELECT name, LENGTH(bio_html) FROM persons
        WHERE bio_html IS NOT NULL
        ORDER BY LENGTH(bio_html) DESC LIMIT 5
    """).fetchall()
    print("\nRichest person bios:")
    for name, size in sample:
        print(f"  {name}: {size} chars")

    sample = conn.execute("""
        SELECT title, LENGTH(analysis_html) FROM texts
        WHERE analysis_html IS NOT NULL
        ORDER BY LENGTH(analysis_html) DESC LIMIT 5
    """).fetchall()
    print("\nRichest text analyses:")
    for title, size in sample:
        safe = title[:50].encode('ascii', errors='replace').decode('ascii')
        print(f"  {safe}: {size} chars")

    conn.close()


if __name__ == "__main__":
    main()
