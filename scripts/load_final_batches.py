"""Load text_analyses_batch_B, historical_figures_batch_A, concepts_batch_E."""
import json, sqlite3

DB = r"C:\Dev\EmeraldTablet\db\emerald_tablet.db"

def fix_json(path):
    with open(path, encoding="utf-8") as f:
        raw = f.read()
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        result, i, n, in_str = [], 0, len(raw), False
        while i < n:
            ch = raw[i]
            if not in_str:
                result.append(ch)
                if ch == '"': in_str = True
                i += 1; continue
            if ch == "\\":
                result.append(ch); i += 1
                if i < n: result.append(raw[i]); i += 1
                continue
            if ch == '"':
                j = i + 1
                while j < n and raw[j] in " \t\r\n": j += 1
                if j < n and raw[j] in ":,}]":
                    result.append(ch); in_str = False
                else:
                    result.append('\\"')
                i += 1; continue
            result.append(ch); i += 1
        return json.loads("".join(result))

conn = sqlite3.connect(DB)
cur  = conn.cursor()

# ── Concepts batch E ─────────────────────────────────────────────────────────
print("\n=== Concepts Batch E ===")
data     = fix_json(r"C:\Dev\EmeraldTablet\staging\dictionary\concepts_batch_E.json")
concepts = data["concepts"] if isinstance(data, dict) else data
for c in concepts:
    slug  = c.get("slug")
    short = c.get("definition_short")
    long_ = c.get("definition_long", "")
    w     = len(long_.split())
    if w < 400:
        print(f"  WARN {slug}: {w} words, skipping")
        continue
    if short is not None:
        cur.execute("UPDATE concepts SET definition_short=?, definition_long=? WHERE slug=?",
                    (short, long_, slug))
    else:
        cur.execute("UPDATE concepts SET definition_long=? WHERE slug=?", (long_, slug))
    mode   = "short+long" if short is not None else "long only"
    status = "updated" if cur.rowcount else "NOT FOUND"
    print(f"  {slug}: {status} ({mode}, {w} words)")
conn.commit()

# ── Text analyses batch B ─────────────────────────────────────────────────────
print("\n=== Text Analyses Batch B ===")
data  = fix_json(r"C:\Dev\EmeraldTablet\staging\dictionary\text_analyses_batch_B.json")
texts = data["texts"] if isinstance(data, dict) else data
for t in texts:
    tid  = t.get("text_id")
    desc = t.get("description", "")
    html = t.get("analysis_html", "")
    w    = len(html.split())
    if w < 400:
        print(f"  WARN {tid}: {w} words, skipping")
        continue
    if desc:
        cur.execute("UPDATE texts SET description=?, analysis_html=? WHERE text_id=?",
                    (desc, html, tid))
    else:
        cur.execute("UPDATE texts SET analysis_html=? WHERE text_id=?", (html, tid))
    mode   = "desc+analysis" if desc else "analysis only"
    status = "updated" if cur.rowcount else "NOT FOUND"
    print(f"  {tid}: {status} ({mode}, {w} words)")
conn.commit()

# ── Historical figures batch A ────────────────────────────────────────────────
print("\n=== Historical Figures Batch A ===")
data    = fix_json(r"C:\Dev\EmeraldTablet\staging\persons\historical_figures_batch_A.json")
persons = data if isinstance(data, list) else data.get("persons", [data])
PERSON_ID_MAP = {"brian_p_copenhaver": "brian_copenhaver"}
for p in persons:
    pid  = PERSON_ID_MAP.get(p.get("person_id"), p.get("person_id"))
    desc = p.get("description", "")
    bio  = p.get("bio_html", "")
    w    = len(bio.split())
    if w < 400:
        print(f"  WARN {pid}: {w} words, skipping")
        continue
    if desc:
        cur.execute("UPDATE persons SET description=?, bio_html=? WHERE person_id=?",
                    (desc, bio, pid))
    else:
        cur.execute("UPDATE persons SET bio_html=? WHERE person_id=?", (bio, pid))
    mode   = "desc+bio" if desc else "bio only"
    status = "updated" if cur.rowcount else "NOT FOUND"
    print(f"  {pid}: {status} ({mode}, {w} words)")
conn.commit()
conn.close()
print("\nDone.")
