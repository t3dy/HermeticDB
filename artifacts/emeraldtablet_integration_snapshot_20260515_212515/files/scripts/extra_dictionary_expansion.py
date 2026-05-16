import sqlite3
from pathlib import Path

DB_PATH = Path(r"c:\Dev\EmeraldTablet\db\emerald_tablet.db")

EXTRA_CONCEPTS = [
    ('imagination_magical', 'Magical Imagination', 'In the Picatrix, the imagination is not merely a mental faculty but a creative force capable of shaping reality and establishing links with the celestial spheres.', 'PHILOSOPHICAL', 'ACTOR_TERM'),
    ('planetary_spirits', 'Planetary Spirits', 'The intelligent, celestial entities associated with the seven planets, which the practitioner of the Picatrix seeks to petition and bind through ritual.', 'THEOLOGICAL', 'ACTOR_TERM'),
    ('monas_generativa', 'Monas Generativa', 'From Liber XXIV: "God is the Monad, generating the Monad, reflecting upon itself the fire of love."', 'THEOLOGICAL', 'ACTOR_TERM'),
    ('anima_mundi_divine', 'Anima Mundi (Divine Soul)', 'From Liber XXIV: "God is the soul of the world, whose body is the universe."', 'COSMOLOGICAL', 'ACTOR_TERM')
]

def expand():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for slug, label, desc, cat, ctype in EXTRA_CONCEPTS:
        cursor.execute("""
            INSERT OR IGNORE INTO concepts (slug, label, definition_short, category, category_type, source_method)
            VALUES (?, ?, ?, ?, ?, 'SEED_DATA')
        """, (slug, label, desc, cat, ctype))

    conn.commit()
    conn.close()
    print("Extra dictionary concepts added.")

if __name__ == "__main__":
    expand()
