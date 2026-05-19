"""Load scholars batch C: Postel, Trithemius, Versluis, Attrell."""
import json, sqlite3

DB   = r"C:\Dev\EmeraldTablet\db\emerald_tablet.db"
PATH = r"C:\Dev\EmeraldTablet\staging\persons\scholars_batch_C.json"

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

data    = fix_json(PATH)
persons = data if isinstance(data, list) else data.get("persons", [data])

for p in persons:
    pid  = p.get("person_id")
    desc = p.get("description", "")
    bio  = p.get("bio_html", "")
    w    = len(bio.split())
    if w < 400:
        print(f"  WARN {pid}: bio_html only {w} words, skipping")
        continue
    if desc:
        cur.execute("UPDATE persons SET description=?, bio_html=? WHERE person_id=?",
                    (desc, bio, pid))
    else:
        cur.execute("UPDATE persons SET bio_html=? WHERE person_id=?", (bio, pid))
    print(f"  {pid}: {'updated' if cur.rowcount else 'NOT FOUND'} ({w} words)")

conn.commit()
conn.close()
print("Done.")
