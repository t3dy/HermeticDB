"""Fix unescaped double quotes inside JSON string values in scholar_essays_batch1.json."""
import json
import re

INPUT = r"C:\Dev\EmeraldTablet\staging\persons\scholar_essays_batch1.json"

with open(INPUT, encoding="utf-8") as f:
    content = f.read()

# State-machine: walk through the file, track whether we are inside a JSON string.
# When inside a string, any bare " that is not preceded by \ and is not the closing "
# needs to be escaped. We detect the closing " by checking what follows it.

result = []
i = 0
n = len(content)
in_string = False

while i < n:
    ch = content[i]

    if not in_string:
        result.append(ch)
        if ch == '"':
            in_string = True
        i += 1
        continue

    # Inside a string
    if ch == "\\":
        # Escape sequence: consume the next char too
        result.append(ch)
        i += 1
        if i < n:
            result.append(content[i])
            i += 1
        continue

    if ch == '"':
        # Is this the closing quote?
        # Look past optional whitespace to see if the next non-space char is :, ,, }, ]
        j = i + 1
        while j < n and content[j] in " \t\r\n":
            j += 1
        next_ch = content[j] if j < n else ""
        if next_ch in ":,}]":
            # This is the closing quote
            result.append(ch)
            in_string = False
        else:
            # Unescaped interior quote — escape it
            result.append('\\"')
        i += 1
        continue

    result.append(ch)
    i += 1

fixed = "".join(result)

try:
    data = json.loads(fixed)
    print(f"Valid JSON: {len(data)} entries")
    # Re-serialize cleanly to normalize escaping
    with open(INPUT, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("File saved.")
except json.JSONDecodeError as e:
    print(f"Still invalid at line {e.lineno} col {e.colno}: {e.msg}")
    lines = fixed.split("\n")
    ln = e.lineno - 1
    print(repr(lines[ln][max(0, e.colno - 30) : e.colno + 20]))
