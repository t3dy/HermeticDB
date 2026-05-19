"""Load all batch staging files produced by writing agents on 2026-05-18.
Files: concepts_batch_A.json, concepts_batch_B.json,
       text_analyses_batch_A.json, scholars_batch_B.json
Idempotent — safe to re-run.
"""
import json, sqlite3, re

DB = r"C:\Dev\EmeraldTablet\db\emerald_tablet.db"

CONCEPTS_A  = r"C:\Dev\EmeraldTablet\staging\dictionary\concepts_batch_A.json"
CONCEPTS_B  = r"C:\Dev\EmeraldTablet\staging\dictionary\concepts_batch_B.json"
TEXTS_A     = r"C:\Dev\EmeraldTablet\staging\dictionary\text_analyses_batch_A.json"
SCHOLARS_B  = r"C:\Dev\EmeraldTablet\staging\persons\scholars_batch_B.json"

conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
cur = conn.cursor()


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


def wc(text):
    return len((text or "").split())


# ── Concepts batch A ─────────────────────────────────────────────────────────
print("\n=== Concepts Batch A ===")
data = fix_json(CONCEPTS_A)
concepts = data["concepts"] if isinstance(data, dict) else data
for c in concepts:
    slug  = c.get("slug")
    short = c.get("definition_short")
    long_ = c.get("definition_long", "")
    w = wc(long_)
    if w < 400:
        print(f"  WARN {slug}: definition_long only {w} words, skipping")
        continue
    if short is not None:
        cur.execute("UPDATE concepts SET definition_short=?, definition_long=? WHERE slug=?",
                    (short, long_, slug))
    else:
        cur.execute("UPDATE concepts SET definition_long=? WHERE slug=?", (long_, slug))
    status = "NOT FOUND" if cur.rowcount == 0 else "updated"
    mode   = "short+long" if short is not None else "long only"
    print(f"  {slug}: {status} ({mode}, {w} words)")
conn.commit()


# ── Concepts batch B ─────────────────────────────────────────────────────────
print("\n=== Concepts Batch B ===")
data = fix_json(CONCEPTS_B)
concepts = data["concepts"] if isinstance(data, dict) else data
for c in concepts:
    slug  = c.get("slug")
    short = c.get("definition_short")
    long_ = c.get("definition_long", "")
    w = wc(long_)
    if w < 400:
        print(f"  WARN {slug}: definition_long only {w} words, skipping")
        continue
    if short is not None:
        cur.execute("UPDATE concepts SET definition_short=?, definition_long=? WHERE slug=?",
                    (short, long_, slug))
    else:
        cur.execute("UPDATE concepts SET definition_long=? WHERE slug=?", (long_, slug))
    status = "NOT FOUND" if cur.rowcount == 0 else "updated"
    mode   = "short+long" if short is not None else "long only"
    print(f"  {slug}: {status} ({mode}, {w} words)")
conn.commit()


# ── Text analyses batch A ─────────────────────────────────────────────────────
print("\n=== Text Analyses Batch A ===")
data = fix_json(TEXTS_A)
texts = data["texts"] if isinstance(data, dict) else data
for t in texts:
    tid  = t.get("text_id")
    desc = t.get("description", "")
    html = t.get("analysis_html", "")
    w = wc(html)
    if w < 400:
        print(f"  WARN {tid}: analysis_html only {w} words, skipping")
        continue
    if desc:
        cur.execute("UPDATE texts SET description=?, analysis_html=? WHERE text_id=?",
                    (desc, html, tid))
    else:
        cur.execute("UPDATE texts SET analysis_html=? WHERE text_id=?", (html, tid))
    status = "NOT FOUND" if cur.rowcount == 0 else "updated"
    mode   = "desc+analysis" if desc else "analysis only"
    print(f"  {tid}: {status} ({mode}, {w} words)")
conn.commit()


# ── Scholars batch B ─────────────────────────────────────────────────────────
print("\n=== Scholars Batch B ===")
data = fix_json(SCHOLARS_B)
persons = data if isinstance(data, list) else data.get("persons", [data])

PERSON_ID_MAP = {
    "brian_p_copenhaver": "brian_copenhaver",
}

for p in persons:
    pid  = p.get("person_id")
    pid  = PERSON_ID_MAP.get(pid, pid)
    desc = p.get("description", "")
    bio  = p.get("bio_html", "")
    w = wc(bio)
    if w < 400:
        print(f"  WARN {pid}: bio_html only {w} words, skipping")
        continue
    if desc:
        cur.execute("UPDATE persons SET description=?, bio_html=? WHERE person_id=?",
                    (desc, bio, pid))
    else:
        cur.execute("UPDATE persons SET bio_html=? WHERE person_id=?", (bio, pid))
    status = "NOT FOUND" if cur.rowcount == 0 else "updated"
    mode   = "desc+bio" if desc else "bio only"
    print(f"  {pid}: {status} ({mode}, {w} words)")
conn.commit()
conn.close()
print("\nDone.")
