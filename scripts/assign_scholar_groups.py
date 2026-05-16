"""
Assigns scholar_group values to all persons with role_primary = 'SCHOLAR'
so the website can group them by area of specialization.
"""
import sqlite3
from pathlib import Path

DB_PATH = Path(r"c:\Dev\EmeraldTablet\db\emerald_tablet.db")

SCHOLAR_GROUPS = {
    # Antiquity and Late Antique Studies
    "garth_fowden":             "Antiquity and Late Antique Studies",
    "jean_pierre_mahe":         "Antiquity and Late Antique Studies",
    "copenhaver_hermetica":     "Antiquity and Late Antique Studies",
    "brian_copenhaver":         "Antiquity and Late Antique Studies",
    "christian_bull":           "Antiquity and Late Antique Studies",
    "m_david_litwa":            "Antiquity and Late Antique Studies",
    "anna_van_den_kerchove":    "Antiquity and Late Antique Studies",
    "gilles_quispel":           "Antiquity and Late Antique Studies",
    "roelof_van_den_broek":     "Antiquity and Late Antique Studies",
    "claudio_moreschini":       "Antiquity and Late Antique Studies",
    "jeffrey_pettis":           "Antiquity and Late Antique Studies",

    # Medieval and Arabic Hermetica
    "paolo_lucentini":          "Medieval and Arabic Hermetica",
    "david_porreca":            "Medieval and Arabic Hermetica",
    "mark_damien_delp":         "Medieval and Arabic Hermetica",
    "dan_attrell":              "Medieval and Arabic Hermetica",
    "liana_saif":               "Medieval and Arabic Hermetica",
    "kevin_van_bladel":         "Medieval and Arabic Hermetica",
    "charles_burnett":          "Medieval and Arabic Hermetica",
    "seyyed_hossein_nasr":      "Medieval and Arabic Hermetica",

    # Renaissance and Early Modern Studies
    "frances_yates":            "Renaissance and Early Modern Studies",
    "dp_walker":                "Renaissance and Early Modern Studies",
    "paola_zambelli":           "Renaissance and Early Modern Studies",
    "carlos_gilly":             "Renaissance and Early Modern Studies",
    "peter_forshaw":            "Renaissance and Early Modern Studies",
    "frank_klaassen":           "Renaissance and Early Modern Studies",
    "nicholas_clulee":          "Renaissance and Early Modern Studies",
    "vittoria_perrone_compagni":"Renaissance and Early Modern Studies",

    # Modern Esotericism and Historiography
    "wouter_hanegraaff":        "Modern Esotericism and Historiography",
    "antoine_faivre":           "Modern Esotericism and Historiography",
    "kocku_von_stuckrad":       "Modern Esotericism and Historiography",
    "arthur_versluis":          "Modern Esotericism and Historiography",
    "nicholas_goodrick_clarke": "Modern Esotericism and Historiography",
    "marco_pasi":               "Modern Esotericism and Historiography",
    "wouter_j_hanegraaff":      "Modern Esotericism and Historiography",
    "glenn_magee":              "Modern Esotericism and Historiography",

    # Kabbalistic and Related Studies
    "moshe_idel":               "Kabbalistic and Related Studies",
    "gershom_scholem":          "Kabbalistic and Related Studies",
}

def assign_groups():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Add scholar_group column if missing
    try:
        cursor.execute("ALTER TABLE persons ADD COLUMN scholar_group TEXT")
        print("Added scholar_group column.")
    except Exception:
        pass  # Already exists

    # Update known scholars
    updated = 0
    for pid, group in SCHOLAR_GROUPS.items():
        cursor.execute("UPDATE persons SET scholar_group = ? WHERE person_id = ?", (group, pid))
        updated += cursor.rowcount

    # For all remaining SCHOLAR-role persons without a group, assign Modern Esotericism
    cursor.execute("""
        UPDATE persons SET scholar_group = 'Modern Esotericism and Historiography'
        WHERE role_primary = 'SCHOLAR' AND (scholar_group IS NULL OR scholar_group = '')
    """)
    updated += cursor.rowcount

    conn.commit()
    conn.close()
    print(f"Scholar groups assigned. {updated} rows updated.")

if __name__ == "__main__":
    assign_groups()
