import sqlite3
from pathlib import Path

DB_PATH = Path(r"c:\Dev\EmeraldTablet\db\emerald_tablet.db")

SCHOLAR_ENRICHMENTS = {
    "frances_yates": """
        <p>Frances Yates (1899–1981) was a British historian who revolutionized the study of the Renaissance by placing the Hermetic tradition and magic at its center. Her landmark work, <i>Giordano Bruno and the Hermetic Tradition</i> (1964), argued that the recovery of the Hermetica was a primary catalyst for the Renaissance world-view and the subsequent Scientific Revolution.</p>
        <p><b>Analytical Significance:</b> The 'Yates Paradigm' proposed that the 'Magus' was the ancestor of the modern scientist. While later scholars have critiqued her for over-generalizing the coherence of a 'tradition', her work remain the cornerstone of modern esoteric studies.</p>
    """,
    "wouter_hanegraaff": """
        <p>Wouter J. Hanegraaff is a Professor of History of Hermetic Philosophy and Related Currents at the University of Amsterdam. He is arguably the most influential figure in the modern academic formalization of Western Esotericism as a field of study.</p>
        <p><b>Analytical Significance:</b> Hanegraaff introduced critical historiographical rigor to the field, moving away from 'perennialist' or 'religionist' interpretations toward a discursive and historical approach. His work emphasizes the role of esotericism as the 'rejected knowledge' of Western modernity.</p>
    """,
    "garth_fowden": """
        <p>Garth Fowden is a historian of Late Antiquity whose work <i>The Egyptian Hermes</i> (1986) fundamentally challenged the 'Greek' reading of Hermeticism championed by Festugière. Fowden argued that the Hermetica were deeply rooted in the social and religious landscape of Roman Egypt.</p>
        <p><b>Analytical Significance:</b> Fowden's 'Historical Approach' bridged the gap between the philosophical Hermetica and the technical/practical texts (alchemy, astrology), viewing them as a single, living tradition practiced by small 'Hermetic circles'.</p>
    """,
    "bruce_codex": "The Bruce Codex (Codex Brucianus) is a Gnostic and Hermetic manuscript discovered in Egypt in 1769, containing the Books of Jeu and other essential texts for understanding the Egyptian-Gnostic-Hermetic milieu.",
    "christoph_kriegsmann": "Christoph Kriegsmann was a 17th-century scholar who attempted to reconcile the Emerald Tablet with biblical and Phoenician antiquities, representing the late stage of the pre-Casaubon Hermetic tradition."
}

def enrich():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for slug, bio in SCHOLAR_ENRICHMENTS.items():
        # Check if we should update analysis_html or description
        # We'll use analysis_html for the rich prose
        cursor.execute("UPDATE persons SET description = ?, analysis_html = ? WHERE person_id = ?", (bio[:200] + "...", bio, slug))

    conn.commit()
    conn.close()
    print("Scholar bios enriched.")

if __name__ == "__main__":
    enrich()
