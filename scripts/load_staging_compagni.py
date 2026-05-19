"""Load Compagni biography and concept entries from staging files."""
import json, sqlite3, re

DB = r"C:\Dev\EmeraldTablet\db\emerald_tablet.db"
PERSON_JSON = r"C:\Dev\EmeraldTablet\staging\persons\compagni_essay.json"
CONCEPT_JSON = r"C:\Dev\EmeraldTablet\staging\dictionary\de_incantationibus_concepts.json"

conn = sqlite3.connect(DB)
cur = conn.cursor()


def fix_json(path):
    """Load JSON, fixing unescaped interior double quotes if needed."""
    with open(path, encoding="utf-8") as f:
        raw = f.read()
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        # State-machine fix for bare " inside strings
        result, i, n, in_string = [], 0, len(raw), False
        while i < n:
            ch = raw[i]
            if not in_string:
                result.append(ch)
                if ch == '"': in_string = True
                i += 1; continue
            if ch == "\\":
                result.append(ch); i += 1
                if i < n: result.append(raw[i]); i += 1
                continue
            if ch == '"':
                j = i + 1
                while j < n and raw[j] in " \t\r\n": j += 1
                if j < n and raw[j] in ":,}]":
                    result.append(ch); in_string = False
                else:
                    result.append('\\"')
                i += 1; continue
            result.append(ch); i += 1
        return json.loads("".join(result))


# ── person biography ────────────────────────────────────────────────────────
data = fix_json(PERSON_JSON)
# May be dict or list
if isinstance(data, list):
    entries = data
elif "persons" in data:
    entries = data["persons"]
else:
    entries = [data]

for p in entries:
    pid   = p.get("person_id")
    bio   = p.get("bio_html", "")
    desc  = p.get("description", "")
    words = len(bio.split())
    if words < 400:
        print(f"  WARN {pid}: only {words} words, skipping")
        continue
    cur.execute("UPDATE persons SET bio_html=?, description=? WHERE person_id=?", (bio, desc, pid))
    print(f"  {pid}: {'updated' if cur.rowcount else 'NOT FOUND'} ({words} words)")

conn.commit()

# ── concept entries ─────────────────────────────────────────────────────────
data = fix_json(CONCEPT_JSON)
if isinstance(data, list):
    concepts = data
elif "concepts" in data:
    concepts = data["concepts"]
else:
    concepts = [data]

for c in concepts:
    slug    = c.get("slug")
    short   = c.get("definition_short")  # None = skip (as instructed)
    long_   = c.get("definition_long", "")
    words   = len(long_.split())
    if words < 800:
        print(f"  WARN {slug}: definition_long only {words} words, skipping")
        continue
    if short is not None:
        cur.execute("UPDATE concepts SET definition_short=?, definition_long=? WHERE slug=?",
                    (short, long_, slug))
    else:
        cur.execute("UPDATE concepts SET definition_long=? WHERE slug=?", (long_, slug))
    print(f"  {slug}: {'updated' if cur.rowcount else 'NOT FOUND'} "
          f"({'short+long' if short is not None else 'long only'}, {words} words)")

conn.commit()
conn.close()
print("Done.")
