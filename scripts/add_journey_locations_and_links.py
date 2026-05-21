"""
Add journey-stop locations not yet in the locations table, then link all
peregrination figures to each of their stops via person_locations.
Idempotent: safe to re-run.
"""
import sqlite3
from pathlib import Path

DB = Path(r"c:\Dev\EmeraldTablet\db\emerald_tablet.db")
conn = sqlite3.connect(DB)
c = conn.cursor()

# ── 1. NEW LOCATIONS ─────────────────────────────────────────────────────────

new_locations = [
    # Bruno stops
    {
        "slug": "toulouse",
        "label": "Toulouse, France",
        "lat": 43.60,
        "lng": 1.44,
        "description": (
            "Toulouse was a major centre of Averroist Aristotelianism and hosted "
            "Giordano Bruno during his most productive French years (1579–81), when he "
            "took his doctorate in theology at the university and delivered his first "
            "major public lectures on Aristotle's De anima and his own mnemonic art. "
            "The city's parlementaire culture tolerated his unorthodox views more than "
            "Geneva had, providing a brief respite before his move to Paris."
        ),
        "region": "EUROPE",
        "era_primary": "RENAISSANCE",
        "source_method": "MANUAL",
        "confidence": "HIGH",
        "review_status": "REVIEWED",
    },
    {
        "slug": "wittenberg",
        "label": "Wittenberg, Germany",
        "lat": 51.87,
        "lng": 12.64,
        "description": (
            "Wittenberg, Luther's own city and the cradle of the Protestant Reformation, "
            "received Giordano Bruno warmly at its university (1586–88). Bruno delivered "
            "a celebrated farewell oration praising Luther as a liberator of the intellect. "
            "His enthusiasm was strategic rather than theological: he saw Lutheran humanism "
            "as an ally against scholastic Aristotelianism, not as a genuine conversion to "
            "Protestantism. The city illustrates the paradoxical hospitality that Bruno "
            "repeatedly found and lost across confessional Europe."
        ),
        "region": "EUROPE",
        "era_primary": "RENAISSANCE",
        "source_method": "MANUAL",
        "confidence": "HIGH",
        "review_status": "REVIEWED",
    },
    {
        "slug": "helmstedt",
        "label": "Helmstedt, Germany",
        "lat": 52.23,
        "lng": 11.01,
        "description": (
            "The newly founded University of Helmstedt, under the protection of Julius, "
            "Duke of Brunswick, received Bruno in 1589. He delivered an oration "
            "commemorating the Duke — his most direct public statement of Hermes-inflected "
            "natural theology. He was subsequently excommunicated by the Lutheran consistory "
            "after a dispute with the local superintendent, exhausting his last refuge in "
            "Protestant Germany and precipitating his fatal return toward Italy."
        ),
        "region": "EUROPE",
        "era_primary": "RENAISSANCE",
        "source_method": "MANUAL",
        "confidence": "HIGH",
        "review_status": "REVIEWED",
    },
    # Agrippa stops
    {
        "slug": "grenoble",
        "label": "Grenoble, France",
        "lat": 45.19,
        "lng": 5.72,
        "description": (
            "Grenoble was the final refuge of Heinrich Cornelius Agrippa, who died here "
            "in early 1535, aged 48, in poverty after fleeing further pursuit by Dominican "
            "inquisitors and creditors across Germany. His death brought no closure to the "
            "controversies he had ignited: De Occulta Philosophia continued to circulate "
            "and shape European occult philosophy for two centuries. Later traditions "
            "embellished his end with legends of a demon-familiar dog who abandoned him "
            "at the moment of death, illustrating the mythologisation of the Hermetic "
            "philosopher in popular imagination."
        ),
        "region": "EUROPE",
        "era_primary": "RENAISSANCE",
        "source_method": "MANUAL",
        "confidence": "HIGH",
        "review_status": "REVIEWED",
    },
    {
        "slug": "dole",
        "label": "Dole, Burgundy, France",
        "lat": 47.10,
        "lng": 5.49,
        "description": (
            "Dole in Burgundy was the site of Agrippa's first major public controversy "
            "in 1509, where he lectured on Johann Reuchlin's De verbo mirifico and was "
            "accused by a Franciscan friar of Judaizing before Margaret of Austria. "
            "This collision with ecclesiastical authority foreshadowed the pattern of "
            "his entire career: brilliant public intellectual performance followed by "
            "institutional resistance and forced departure."
        ),
        "region": "EUROPE",
        "era_primary": "RENAISSANCE",
        "source_method": "MANUAL",
        "confidence": "HIGH",
        "review_status": "REVIEWED",
    },
    {
        "slug": "pavia",
        "label": "Pavia, Italy",
        "lat": 45.19,
        "lng": 9.16,
        "description": (
            "Pavia was home to one of Italy's oldest universities and was the site of "
            "Agrippa's remarkable lectures (1512–15) on Hermes Trismegistus and the "
            "Pauline epistles — possibly the first university lecture course in history "
            "devoted explicitly to the Hermetic Corpus. The city's French overlords "
            "eventually sacked Pavia, ending Agrippa's position and inaugurating his "
            "decades of wandering. Pavia also hosted important currents of Neoplatonic "
            "and mathematical humanism that shaped the Italian Renaissance."
        ),
        "region": "EUROPE",
        "era_primary": "RENAISSANCE",
        "source_method": "MANUAL",
        "confidence": "HIGH",
        "review_status": "REVIEWED",
    },
    {
        "slug": "metz",
        "label": "Metz, France",
        "lat": 49.12,
        "lng": 6.18,
        "description": (
            "Metz was the city where Agrippa served as city advocate (syndic) from "
            "1518–1520 and famously defended a woman accused of witchcraft, attacking "
            "the Malleus Maleficarum as an instrument of clerical persecution. His "
            "defence enraged the Dominican inquisitor Nicolas Savin and forced him to "
            "leave — one of the most consequential episodes in the early modern debate "
            "over witchcraft theory and the limits of ecclesiastical coercion."
        ),
        "region": "EUROPE",
        "era_primary": "RENAISSANCE",
        "source_method": "MANUAL",
        "confidence": "HIGH",
        "review_status": "REVIEWED",
    },
    {
        "slug": "lyon",
        "label": "Lyon, France",
        "lat": 45.75,
        "lng": 4.83,
        "description": (
            "Lyon was the base of Agrippa's service as personal physician to Louise "
            "of Savoy (1524–27), mother of Francis I. Here he composed De incertitudine "
            "et vanitate scientiarum (On the Vanity of the Arts and Sciences), his "
            "most sceptical and rhetorically brilliant work. His fall from royal favour "
            "and Louise's refusal to pay his salary drove him into the bitter poverty "
            "he described in his correspondence. Lyon was also one of the great printing "
            "and commercial centres of Renaissance France."
        ),
        "region": "EUROPE",
        "era_primary": "RENAISSANCE",
        "source_method": "MANUAL",
        "confidence": "HIGH",
        "review_status": "REVIEWED",
    },
    {
        "slug": "antwerp",
        "label": "Antwerp, Belgium",
        "lat": 51.22,
        "lng": 4.40,
        "description": (
            "Antwerp was the commercial and printing capital of the northern Renaissance "
            "and the seat of Agrippa's appointment as court historian and archivist to "
            "Margaret of Austria (1528–30). Here he prepared De Occulta Philosophia for "
            "its definitive revision and eventual publication. Antwerp's extraordinary "
            "printing industry made it the natural home for a work of such ambition and "
            "continental scope; the definitive edition was ultimately published in Cologne."
        ),
        "region": "EUROPE",
        "era_primary": "RENAISSANCE",
        "source_method": "MANUAL",
        "confidence": "HIGH",
        "review_status": "REVIEWED",
    },
    # Dee stops
    {
        "slug": "cambridge",
        "label": "Cambridge, England",
        "lat": 52.21,
        "lng": 0.12,
        "description": (
            "Cambridge, and specifically St John's College and the newly founded Trinity "
            "College, was where John Dee received his formation as a mathematician and "
            "natural philosopher (1542–46). His extraordinary early aptitude — reportedly "
            "studying eighteen hours a day and sleeping only four — established the "
            "intellectual foundation for his later career as England's foremost "
            "mathematician and the most learned natural philosopher of Elizabethan England. "
            "Cambridge also hosted Robert Grosseteste's intellectual legacy in natural "
            "philosophy and Roger Bacon's mathematical tradition."
        ),
        "region": "EUROPE",
        "era_primary": "RENAISSANCE",
        "source_method": "MANUAL",
        "confidence": "HIGH",
        "review_status": "REVIEWED",
    },
    {
        "slug": "louvain",
        "label": "Louvain (Leuven), Belgium",
        "lat": 50.88,
        "lng": 4.70,
        "description": (
            "Louvain (Leuven) was the leading northern European centre for cosmography "
            "and applied mathematics in the mid-16th century. John Dee studied here "
            "with the cartographer Gerardus Mercator and the mathematician Gemma Frisius "
            "(1547–50), acquiring rare mathematical instruments, globes, and manuscripts "
            "that became the foundation of his celebrated Mortlake library. His Louvain "
            "connections gave him world-leading expertise in navigation and practical "
            "astronomy at a moment when England was beginning to project maritime power."
        ),
        "region": "EUROPE",
        "era_primary": "RENAISSANCE",
        "source_method": "MANUAL",
        "confidence": "HIGH",
        "review_status": "REVIEWED",
    },
    {
        "slug": "krakow",
        "label": "Kraków, Poland",
        "lat": 50.06,
        "lng": 19.94,
        "description": (
            "Kraków was the capital of the Polish-Lithuanian Commonwealth and the city "
            "to which John Dee and Edward Kelley travelled in 1583–84 under the patronage "
            "of the Polish nobleman Albert Łaski. The city's Jagiellonian University "
            "had long been a centre of Neoplatonic and astronomical humanism, and Dee's "
            "presence there continued the angel conversations begun at Mortlake. Kraków "
            "served as his staging post toward the Habsburg imperial court at Prague."
        ),
        "region": "EUROPE",
        "era_primary": "RENAISSANCE",
        "source_method": "MANUAL",
        "confidence": "HIGH",
        "review_status": "REVIEWED",
    },
    {
        "slug": "trebon",
        "label": "Třeboň, Bohemia",
        "lat": 49.01,
        "lng": 14.77,
        "description": (
            "Třeboň Castle in southern Bohemia was the seat of Wilhelm von Rosenberg "
            "and the final Continental refuge of John Dee and Edward Kelley (1586–89). "
            "Here Kelley claimed to achieve transmutation of base metal into gold — "
            "winning a knighthood and a manor from Rudolf II. The angels' command that "
            "Dee and Kelley share their wives fractured their partnership permanently. "
            "Třeboň was a node in the broader Rudolphine alchemical network that "
            "connected Prague, Vienna, and the Bohemian nobility."
        ),
        "region": "EUROPE",
        "era_primary": "RENAISSANCE",
        "source_method": "MANUAL",
        "confidence": "HIGH",
        "review_status": "REVIEWED",
    },
    # Trithemius stops
    {
        "slug": "trittenheim",
        "label": "Trittenheim, Germany",
        "lat": 49.84,
        "lng": 6.89,
        "description": (
            "Trittenheim on the Moselle River was the birthplace of Johannes Trithemius "
            "on 1 February 1462. His childhood here was marked by poverty and a harsh "
            "stepfather; his intellectual gifts appeared early and drove him to escape "
            "on foot to Heidelberg in search of education. The village gave him the "
            "name by which history knows him — Trithemius — though he was born "
            "Johann Heidenberg."
        ),
        "region": "EUROPE",
        "era_primary": "MEDIEVAL",
        "source_method": "MANUAL",
        "confidence": "HIGH",
        "review_status": "REVIEWED",
    },
    {
        "slug": "heidelberg",
        "label": "Heidelberg, Germany",
        "lat": 49.40,
        "lng": 8.69,
        "description": (
            "Heidelberg and its university were the intellectual centre of the Rhenish "
            "Humanists, and it was here that Trithemius received his formation in logic, "
            "rhetoric, Latin poetry, and philosophy (c. 1479–82). The city's humanist "
            "culture shaped his lifelong commitment to building learned library networks "
            "and establishing correspondence with Europe's most eminent scholars. "
            "Heidelberg also later hosted the Palatine court's alchemical interests "
            "during the early Rosicrucian period."
        ),
        "region": "EUROPE",
        "era_primary": "MEDIEVAL",
        "source_method": "MANUAL",
        "confidence": "HIGH",
        "review_status": "REVIEWED",
    },
    {
        "slug": "sponheim",
        "label": "Sponheim, Germany",
        "lat": 49.89,
        "lng": 7.57,
        "description": (
            "The Benedictine monastery of Sponheim was where Trithemius built his "
            "legendary library from forty-eight books to over 2,000 volumes and composed "
            "his most important works (1483–1506): the Liber de scriptoribus ecclesiasticis "
            "(1494), the first printed bio-bibliography of Christian authors, and the "
            "Steganographia, whose system of apparent angelic communication was revealed "
            "by scholars in 1996–98 to encode genuine cryptographic ciphers. Sponheim "
            "became the most celebrated monastic library in German lands under his abbacy."
        ),
        "region": "EUROPE",
        "era_primary": "MEDIEVAL",
        "source_method": "MANUAL",
        "confidence": "HIGH",
        "review_status": "REVIEWED",
    },
    # Pico stops
    {
        "slug": "mirandola",
        "label": "Mirandola, Italy",
        "lat": 44.88,
        "lng": 11.06,
        "description": (
            "Mirandola near Ferrara was the ancestral seat of the della Mirandola dynasty "
            "and the birthplace of Giovanni Pico della Mirandola (24 February 1463). "
            "The small principality's rulers had cultivated humanist learning, and Pico's "
            "prodigious childhood — he reportedly memorised the Psalter by age ten — "
            "was shaped by this environment. Mirandola is less a centre of Hermetic "
            "transmission than the biographical origin point of its most ambitious "
            "synthesiser."
        ),
        "region": "EUROPE",
        "era_primary": "RENAISSANCE",
        "source_method": "MANUAL",
        "confidence": "HIGH",
        "review_status": "REVIEWED",
    },
    {
        "slug": "bologna",
        "label": "Bologna, Italy",
        "lat": 44.50,
        "lng": 11.34,
        "description": (
            "Bologna's university, the oldest in Europe, was where Pico began his formal "
            "education in canon law (1477–79) before quickly abandoning it for philosophy "
            "and theology. Bologna also hosted significant currents of Averroist "
            "Aristotelianism that shaped the Italian philosophical milieu Pico would "
            "eventually synthesise. Later, Cornelius Agrippa travelled through Bologna "
            "on his Italian journeys, and the city's university remained an important "
            "centre of natural philosophy throughout the Renaissance."
        ),
        "region": "EUROPE",
        "era_primary": "RENAISSANCE",
        "source_method": "MANUAL",
        "confidence": "HIGH",
        "review_status": "REVIEWED",
    },
    {
        "slug": "ferrara",
        "label": "Ferrara, Italy",
        "lat": 44.84,
        "lng": 11.62,
        "description": (
            "Ferrara under the Este court was one of the great centres of Renaissance "
            "humanism and patronage. Pico studied at the university here (c. 1479–80) "
            "under distinguished humanists and had first encounters with Kabbalistic "
            "texts transmitted by Jewish scholars. The Este court's cosmopolitan "
            "tolerance — extending to large and intellectually active Jewish communities "
            "— made Ferrara a uniquely productive environment for the meeting of Hebrew, "
            "Arabic, and Latin scholarly traditions."
        ),
        "region": "EUROPE",
        "era_primary": "RENAISSANCE",
        "source_method": "MANUAL",
        "confidence": "HIGH",
        "review_status": "REVIEWED",
    },
    {
        "slug": "padua",
        "label": "Padua, Italy",
        "lat": 45.41,
        "lng": 11.88,
        "description": (
            "Padua's university was the pre-eminent centre of Averroist Aristotelianism "
            "in Europe and the institution where Pico studied its philosophical currents "
            "(1480–82), meeting Elia del Medigo who opened the Kabbalistic tradition to "
            "him. Padua was also central to the careers of Pietro Pomponazzi and other "
            "Italian naturalist philosophers whose radical Aristotelianism posed a "
            "challenge to scholastic orthodoxy that the Hermetic and Neoplatonic "
            "syntheses of Ficino and Pico sought to answer."
        ),
        "region": "EUROPE",
        "era_primary": "RENAISSANCE",
        "source_method": "MANUAL",
        "confidence": "HIGH",
        "review_status": "REVIEWED",
    },
    # Digby stops
    {
        "slug": "gayhurst",
        "label": "Gayhurst, Buckinghamshire, England",
        "lat": 52.07,
        "lng": -0.74,
        "description": (
            "Gayhurst (then Gothurst) in Buckinghamshire was the country seat where "
            "Sir Kenelm Digby was born on 11 July 1603 and raised. His father, Sir "
            "Everard Digby, was executed for his role in the Gunpowder Plot (1606), "
            "leaving Kenelm to be brought up a Catholic in Protestant England — a "
            "social position that paradoxically gave him extraordinary intellectual "
            "and diplomatic range across confessional boundaries. The house remained "
            "associated with Catholic recusant networks throughout the early Stuart period."
        ),
        "region": "EUROPE",
        "era_primary": "EARLY_MODERN",
        "source_method": "MANUAL",
        "confidence": "HIGH",
        "review_status": "REVIEWED",
    },
    {
        "slug": "algiers",
        "label": "Algiers, Algeria",
        "lat": 36.73,
        "lng": 3.09,
        "description": (
            "Algiers under the Ottoman Regency was the most important Barbary corsair "
            "port in the western Mediterranean and a major centre for the slave trade "
            "in European captives. Digby's squadron anchored off Algiers in February "
            "1628 to negotiate the ransom of English captives — a humanitarian and "
            "diplomatic mission combined with privateering objectives. The episode "
            "illustrates the dual role of the English gentleman-adventurer at the "
            "intersection of diplomacy, commerce, and naval force in the early "
            "17th-century Mediterranean."
        ),
        "region": "AFRICA",
        "era_primary": "EARLY_MODERN",
        "source_method": "MANUAL",
        "confidence": "HIGH",
        "review_status": "REVIEWED",
    },
    {
        "slug": "milos",
        "label": "Milos, Greece",
        "lat": 36.69,
        "lng": 24.43,
        "description": (
            "The Aegean island of Milos in the Cyclades was the site of Digby's first "
            "documented alchemical experiment at sea (spring 1628): an attempt to treat "
            "wounded sailors using vitriol as an ingredient in the powder of sympathy — "
            "action-at-a-distance wound healing derived from Paracelsian and Helmontian "
            "natural philosophy. The experiment, later described in his Discourse on "
            "the Powder of Sympathy, became famous across Europe and was debated at "
            "the Royal Society decades later. Milos fuses his naval command with his "
            "emerging career as an experimenter in Hermetic natural philosophy."
        ),
        "region": "EUROPE",
        "era_primary": "EARLY_MODERN",
        "source_method": "MANUAL",
        "confidence": "HIGH",
        "review_status": "REVIEWED",
    },
    {
        "slug": "scanderoon",
        "label": "Scanderoon (Iskenderun), Turkey",
        "lat": 36.60,
        "lng": 36.17,
        "description": (
            "Scanderoon (modern Iskenderun) on the Gulf of Alexandretta was the site "
            "of Digby's greatest naval action: the Battle of Scanderoon in June 1628, "
            "where he defeated a combined Venetian and French fleet with a much smaller "
            "English squadron. The victory made him famous across Europe and was the "
            "military foundation of his subsequent diplomatic career. The port was an "
            "important node in the Levant trade connecting the eastern Mediterranean "
            "to Venice, Genoa, and England."
        ),
        "region": "ASIA",
        "era_primary": "EARLY_MODERN",
        "source_method": "MANUAL",
        "confidence": "HIGH",
        "review_status": "REVIEWED",
    },
    # Trithemius — Frankfurt
    {
        "slug": "frankfurt",
        "label": "Frankfurt, Germany",
        "lat": 50.11,
        "lng": 8.68,
        "description": (
            "Frankfurt's annual book fair was the most important intellectual marketplace "
            "in early modern Europe and the hub of Trithemius's correspondence network "
            "with Erasmus, Reuchlin, and the leading humanists of his generation. "
            "Giordano Bruno lodged in Frankfurt (1590–91) while using the city's "
            "printers to publish his Latin metaphysical trilogy (De monade, De minimo, "
            "De immenso), and Michael Maier was also active in Frankfurt's alchemical "
            "publishing world. The city thus served as a node for both the humanist "
            "Republic of Letters and the later Hermetic-alchemical print culture."
        ),
        "region": "EUROPE",
        "era_primary": "RENAISSANCE",
        "source_method": "MANUAL",
        "confidence": "HIGH",
        "review_status": "REVIEWED",
    },
    # Geneva (Bruno)
    {
        "slug": "geneva",
        "label": "Geneva, Switzerland",
        "lat": 46.20,
        "lng": 6.14,
        "description": (
            "Geneva under Jean Calvin and his successors was the most rigidly "
            "disciplined Protestant city in Europe. Giordano Bruno arrived in 1578 "
            "seeking refuge from the Italian Inquisition, joined the Calvinist "
            "community, and promptly attacked a professor's logic in print — resulting "
            "in arrest, forced recantation, and excommunication by the Calvinist "
            "consistory. His famous remark that he had merely moved from one Inquisition "
            "to another captures Geneva's role as both refuge and trap for intellectuals "
            "fleeing Catholic orthodoxy."
        ),
        "region": "EUROPE",
        "era_primary": "RENAISSANCE",
        "source_method": "MANUAL",
        "confidence": "HIGH",
        "review_status": "REVIEWED",
    },
]

# ── Check which cols exist ────────────────────────────────────────────────────
c.execute("PRAGMA table_info(locations)")
loc_cols = {row[1] for row in c.fetchall()}

inserted = 0
for loc in new_locations:
    row = {k: v for k, v in loc.items() if k in loc_cols}
    placeholders = ", ".join(["?"] * len(row))
    col_names = ", ".join(row.keys())
    c.execute(
        f"INSERT OR IGNORE INTO locations ({col_names}) VALUES ({placeholders})",
        list(row.values()),
    )
    if c.rowcount:
        inserted += 1
        print(f"  + location: {loc['slug']}")
    else:
        print(f"  = location exists: {loc['slug']}")

conn.commit()
print(f"\n{inserted} new locations inserted.\n")

# ── 2. PERSON-LOCATION ASSOCIATIONS ─────────────────────────────────────────

c.execute("PRAGMA table_info(person_locations)")
pl_cols = {row[1] for row in c.fetchall()}

associations = [
    # Giordano Bruno — full itinerary
    ("giordano_bruno", "rome",        "BORN",    "MANUAL", "HIGH"),    # fled to Rome 1576
    ("giordano_bruno", "geneva",      "VISITED", "MANUAL", "HIGH"),
    ("giordano_bruno", "toulouse",    "ACTIVE",  "MANUAL", "HIGH"),
    ("giordano_bruno", "paris",       "ACTIVE",  "MANUAL", "HIGH"),
    ("giordano_bruno", "london",      "ACTIVE",  "MANUAL", "HIGH"),
    ("giordano_bruno", "wittenberg",  "VISITED", "MANUAL", "HIGH"),
    ("giordano_bruno", "helmstedt",   "VISITED", "MANUAL", "HIGH"),
    ("giordano_bruno", "frankfurt",   "ACTIVE",  "MANUAL", "HIGH"),

    # Giovanni Pico
    ("giovanni_pico",  "mirandola",   "BORN",    "MANUAL", "HIGH"),
    ("giovanni_pico",  "bologna",     "STUDIED", "MANUAL", "HIGH"),
    ("giovanni_pico",  "ferrara",     "STUDIED", "MANUAL", "HIGH"),
    ("giovanni_pico",  "padua",       "STUDIED", "MANUAL", "HIGH"),
    ("giovanni_pico",  "paris",       "STUDIED", "MANUAL", "HIGH"),
    ("giovanni_pico",  "rome",        "ACTIVE",  "MANUAL", "HIGH"),

    # Cornelius Agrippa — full itinerary
    ("cornelius_agrippa", "paris",    "STUDIED", "MANUAL", "HIGH"),
    ("cornelius_agrippa", "dole",     "ACTIVE",  "MANUAL", "HIGH"),
    ("cornelius_agrippa", "london",   "VISITED", "MANUAL", "HIGH"),
    ("cornelius_agrippa", "pavia",    "ACTIVE",  "MANUAL", "HIGH"),
    ("cornelius_agrippa", "metz",     "ACTIVE",  "MANUAL", "HIGH"),
    ("cornelius_agrippa", "lyon",     "ACTIVE",  "MANUAL", "HIGH"),
    ("cornelius_agrippa", "antwerp",  "ACTIVE",  "MANUAL", "HIGH"),
    ("cornelius_agrippa", "grenoble", "DIED",    "MANUAL", "HIGH"),

    # John Dee — full itinerary
    ("john_dee", "cambridge",  "STUDIED", "MANUAL", "HIGH"),
    ("john_dee", "louvain",    "STUDIED", "MANUAL", "HIGH"),
    ("john_dee", "paris",      "ACTIVE",  "MANUAL", "HIGH"),
    ("john_dee", "krakow",     "VISITED", "MANUAL", "HIGH"),
    ("john_dee", "trebon",     "ACTIVE",  "MANUAL", "HIGH"),

    # Johannes Trithemius — full itinerary
    ("johannes_trithemius", "trittenheim", "BORN",    "MANUAL", "HIGH"),
    ("johannes_trithemius", "heidelberg",  "STUDIED", "MANUAL", "HIGH"),
    ("johannes_trithemius", "sponheim",    "ACTIVE",  "MANUAL", "HIGH"),
    ("johannes_trithemius", "frankfurt",   "ACTIVE",  "MANUAL", "HIGH"),

    # Kenelm Digby — full itinerary
    ("kenelm_digby", "gayhurst",    "BORN",    "MANUAL", "HIGH"),
    ("kenelm_digby", "oxford",      "STUDIED", "MANUAL", "HIGH"),
    ("kenelm_digby", "florence",    "VISITED", "MANUAL", "HIGH"),
    ("kenelm_digby", "london",      "ACTIVE",  "MANUAL", "HIGH"),
    ("kenelm_digby", "algiers",     "VISITED", "MANUAL", "HIGH"),
    ("kenelm_digby", "milos",       "VISITED", "MANUAL", "HIGH"),
    ("kenelm_digby", "scanderoon",  "ACTIVE",  "MANUAL", "HIGH"),
    ("kenelm_digby", "paris",       "ACTIVE",  "MANUAL", "HIGH"),
]

pl_inserted = 0
for person_id, loc_slug, role, src, conf in associations:
    c.execute("SELECT 1 FROM persons WHERE person_id=?", (person_id,))
    if not c.fetchone():
        print(f"  SKIP (person not found): {person_id}")
        continue
    c.execute("SELECT 1 FROM locations WHERE slug=?", (loc_slug,))
    if not c.fetchone():
        print(f"  SKIP (location not found): {loc_slug}")
        continue

    row_data = {"person_id": person_id, "location_slug": loc_slug, "role": role}
    if "source_method" in pl_cols:
        row_data["source_method"] = src
    if "confidence" in pl_cols:
        row_data["confidence"] = conf

    placeholders = ", ".join(["?"] * len(row_data))
    col_names = ", ".join(row_data.keys())
    c.execute(
        f"INSERT OR IGNORE INTO person_locations ({col_names}) VALUES ({placeholders})",
        list(row_data.values()),
    )
    if c.rowcount:
        pl_inserted += 1
        print(f"  + {person_id} -> {loc_slug} ({role})")
    else:
        print(f"  = exists: {person_id} -> {loc_slug}")

conn.commit()
conn.close()
print(f"\n{pl_inserted} new person_location rows inserted.")
print("Done.")
