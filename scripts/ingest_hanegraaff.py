import sqlite3
import json
from pathlib import Path

DB_PATH = Path("db/emerald_tablet.db")

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 1. Update/Insert Wouter Hanegraaff in persons table
    cursor.execute("""
    INSERT INTO persons (person_id, name, name_alt, era, role_primary, description, bio_html, source_method, review_status, confidence)
    VALUES (
        'wouter_hanegraaff', 
        'Wouter J. Hanegraaff', 
        NULL, 
        'MODERN', 
        'SCHOLAR', 
        'Professor of History of Hermetic Philosophy and Related Currents. Author of Hermetic Spirituality and the Historical Imagination.',
        '<p>Wouter J. Hanegraaff is a Professor of History of Hermetic Philosophy and Related Currents at the University of Amsterdam. In his 2022 monograph <i>Hermetic Spirituality and the Historical Imagination</i>, he argues that the Way of Hermes involved experiential practices intended to heal the soul from mental delusion through radical alterations of consciousness. He challenges the dominant narrative that Hermetic texts are merely philosophical treatises.</p>',
        'SCRIPT_INGEST', 
        'VERIFIED', 
        'HIGH'
    ) ON CONFLICT(person_id) DO UPDATE SET 
        bio_html = '<p>Wouter J. Hanegraaff is a Professor of History of Hermetic Philosophy and Related Currents at the University of Amsterdam. He has been instrumental in establishing Western Esotericism as a legitimate and rigorous academic field.</p><p><b>Core Methodology:</b> Hanegraaff advocates for a ''discursive'' approach that avoids the pitfalls of ''perennialism'' and ''religionism''. His 2022 monograph, <i>Hermetic Spirituality and the Historical Imagination</i>, revolutionizes the understanding of the Hermetica by demonstrating that these texts were experiential manuals designed to induce altered states of knowledge, rather than mere theoretical philosophy.</p>',
        description = 'Professor of History of Hermetic Philosophy and Related Currents. Author of Hermetic Spirituality and the Historical Imagination.'
    """)

    # 2. Insert the book into bibliography
    cursor.execute("""
    INSERT OR IGNORE INTO bibliography (source_id, author, title, year, publisher, pub_type, relevance)
    VALUES (
        'hanegraaff_2022',
        'Wouter J. Hanegraaff',
        'Hermetic Spirituality and the Historical Imagination: Altered States of Knowledge in Late Antiquity',
        2022,
        'Cambridge University Press',
        'MONOGRAPH',
        'PRIMARY'
    )
    """)

    # 3. Insert the book into texts
    cursor.execute("""
    INSERT INTO texts (text_id, title, language, text_type, date_composed_start, date_composed_end, description, analysis_html, source_method, review_status, confidence)
    VALUES (
        'hermetic_spirituality_hanegraaff',
        'Hermetic Spirituality and the Historical Imagination',
        'ENGLISH',
        'SCHOLARSHIP',
        2022,
        2022,
        'A groundbreaking monograph by Wouter J. Hanegraaff arguing that the Hermetica describe experiential spiritual practices rather than abstract philosophy.',
        '<p>In <i>Hermetic Spirituality and the Historical Imagination</i> (2022), Wouter J. Hanegraaff challenges the long-standing scholarly assumption that the philosophical Hermetica are purely theoretical treatises. He argues instead that they are practical manuals designed for a contemplative regimen—the \"Way of Hermes\"—that induces radical alterations of consciousness.</p><p>By overcoming the hallucinatory veil of appearances (<i>phantasmata</i>), the practitioner attains a direct, unmediated knowledge of reality known as gnosis. Hanegraaff''s approach relies heavily on maintaining a strict actor/analyst distinction, carefully separating what historical practitioners experienced from how modern historians categorize those experiences.</p>',
        'SCRIPT_INGEST',
        'VERIFIED',
        'HIGH'
    ) ON CONFLICT(text_id) DO UPDATE SET
        analysis_html = excluded.analysis_html
    """)

    # Link Hanegraaff to the text
    cursor.execute("SELECT id FROM persons WHERE person_id = 'wouter_hanegraaff'")
    hanegraaff_id = cursor.fetchone()[0]

    cursor.execute("SELECT id FROM texts WHERE text_id = 'hermetic_spirituality_hanegraaff'")
    text_id = cursor.fetchone()[0]

    cursor.execute("""
    INSERT OR IGNORE INTO person_text_roles (person_id, text_id, role, confidence)
    VALUES (?, ?, 'AUTHOR', 'HIGH')
    """, (hanegraaff_id, text_id))

    # 4. Insert Concepts
    concepts = [
        (
            'altered_states_of_knowledge',
            'Altered States of Knowledge',
            'PHILOSOPHICAL',
            'ANALYST_TERM',
            'Scholarly framework for understanding gnosis as a profound cognitive shift.',
            '<p>An <b>ANALYST_TERM</b> introduced by Wouter J. Hanegraaff to describe the epistemological shift practitioners of the Way of Hermes underwent. Rather than simply acquiring new information, the practitioner entered a different state of consciousness that allowed for direct, unmediated apprehension of reality, contrasting with ordinary discursive reasoning.</p>'
        ),
        (
            'phantasmata',
            'Phantasmata',
            'PHILOSOPHICAL',
            'ACTOR_TERM',
            'Mental imagery or illusions that cloud the mind from perceiving divine truth.',
            '<p>An <b>ACTOR_TERM</b> denoting the stream of mental imagery, emotions, and sensory illusions that constitute ordinary human consciousness. In Hermetic spirituality, the practitioner must overcome the spell of <i>phantasmata</i> to achieve spiritual death and rebirth, perceiving reality beyond the hallucinatory veil of appearances.</p>'
        ),
        (
            'way_of_hermes',
            'Way of Hermes',
            'THEOLOGICAL',
            'ACTOR_TERM',
            'The experiential and contemplative path leading to Hermetic gnosis.',
            '<p>An <b>ACTOR_TERM</b> describing the specific spiritual regimen practiced by followers of Hermes Trismegistus. As delineated by Wouter J. Hanegraaff and Garth Fowden, this was not merely an intellectual study but a profound experiential practice involving healing the soul, exorcism, luminous visions, and ultimately, union with the divine.</p>'
        ),
        (
            'historical_imagination',
            'Historical Imagination',
            'PHILOSOPHICAL',
            'ANALYST_TERM',
            'The framework through which scholars construct and tell the narrative of history.',
            '<p>An <b>ANALYST_TERM</b> referring to the constructive narrative power of historians. Wouter J. Hanegraaff explores how language and historiography are not just descriptive but act as a form of enchantment, shaping how subsequent generations perceive ancient spiritual currents.</p>'
        )
    ]

    for slug, label, category, cat_type, short_def, long_def in concepts:
        cursor.execute(f"""
        INSERT INTO concepts (slug, label, category, category_type, definition_short, definition_long, source_method, review_status, confidence)
        VALUES (?, ?, ?, ?, ?, ?, 'SCRIPT_INGEST', 'VERIFIED', 'HIGH')
        ON CONFLICT(slug) DO UPDATE SET
            definition_long = excluded.definition_long,
            category_type = excluded.category_type
        """, (slug, label, category, cat_type, short_def, long_def))

        # Link concept to Hanegraaff's text
        cursor.execute("SELECT id FROM concepts WHERE slug = ?", (slug,))
        concept_id = cursor.fetchone()[0]

        cursor.execute("""
        INSERT OR IGNORE INTO concept_text_refs (concept_id, text_id, notes)
        VALUES (?, ?, 'Analyzed in Hanegraaff 2022')
        """, (concept_id, text_id))

    conn.commit()
    conn.close()
    print("Ingestion complete.")

if __name__ == "__main__":
    main()
