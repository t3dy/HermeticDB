import sqlite3
import sys

def migrate():
    conn = sqlite3.connect("db/emerald_tablet.db")
    cursor = conn.cursor()
    
    # Disable foreign keys temporarily
    cursor.execute("PRAGMA foreign_keys = OFF;")
    
    # Create new texts table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS texts_new (
        id                  INTEGER PRIMARY KEY,
        text_id             TEXT UNIQUE NOT NULL,
        title               TEXT NOT NULL,
        title_original      TEXT,
        language            TEXT CHECK(language IN ('ARABIC','LATIN','GREEK','SYRIAC','GERMAN','ENGLISH','PERSIAN','HEBREW') OR language IS NULL),
        text_type           TEXT CHECK(text_type IN ('PRIMARY_SOURCE','COMMENTARY','COMPILATION','TREATISE','ENCYCLOPEDIA','TRANSLATION','PSEUDO_EPIGRAPHA','SCHOLARSHIP','MANIFESTO') OR text_type IS NULL),
        date_composed_start INTEGER,
        date_composed_end   INTEGER,
        description         TEXT,
        analysis_html       TEXT,
        transmission_notes  TEXT,
        source_method       TEXT DEFAULT 'SEED_DATA',
        review_status       TEXT DEFAULT 'DRAFT' CHECK(review_status IN ('DRAFT','REVIEWED','VERIFIED')),
        confidence          TEXT DEFAULT 'MEDIUM' CHECK(confidence IN ('HIGH','MEDIUM','LOW'))
    );
    """)
    
    # Copy data
    cursor.execute("INSERT INTO texts_new SELECT * FROM texts;")
    
    # Drop old and rename
    cursor.execute("DROP TABLE texts;")
    cursor.execute("ALTER TABLE texts_new RENAME TO texts;")
    
    # Re-enable foreign keys
    cursor.execute("PRAGMA foreign_keys = ON;")
    
    conn.commit()
    conn.close()
    print("Migration successful")

if __name__ == "__main__":
    migrate()
