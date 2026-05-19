"""Load concept batches C and D."""
import json, sqlite3

DB = r"C:\Dev\EmeraldTablet\db\emerald_tablet.db"
FILES = [
    r"C:\Dev\EmeraldTablet\staging\dictionary\concepts_batch_C.json",
    r"C:\Dev\EmeraldTablet\staging\dictionary\concepts_batch_D.json",
]

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

for path in FILES:
    label = path.split("\\")[-1]
    print(f"\n=== {label} ===")
    data     = fix_json(path)
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

conn.close()
print("\nDone.")
