#!/usr/bin/env python3
import sqlite3

db = r'C:\Dev\EmeraldTablet\db\emerald_tablet.db'
conn = sqlite3.connect(db)
c = conn.cursor()

c.execute("SELECT COUNT(*) FROM texts WHERE length(coalesce(analysis_html, '')) >= 1000")
done = c.fetchone()[0]

c.execute("SELECT COUNT(*) FROM texts")
total = c.fetchone()[0]

pct = (100 * done) // total
print(f"Text Analyses Complete: {done}/{total} ({pct}%)")
print(f"Remaining: {total - done} texts need work")

# Show which ones are still short
c.execute("SELECT text_id, length(coalesce(analysis_html, '')) FROM texts WHERE length(coalesce(analysis_html, '')) < 1000 ORDER BY 2 DESC LIMIT 10")
print("\nTop 10 remaining short texts:")
for text_id, length in c.fetchall():
    print(f"  {text_id:<30} | {length:>5} chars")
