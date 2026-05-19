"""
Replace all BASE_TEMPLATE.replace("{{title}}", X).replace("{{css}}", CSS).replace("{{nav}}", NAV_BAR).replace("{{content}}", Y)
with render(X, CSS, NAV_BAR, Y) in DEPLOY_PORTAL.py.
Also adds the concept_index_js placeholder to BASE_TEMPLATE if not already present.
"""
import re

PATH = r"C:\Dev\EmeraldTablet\.claude\worktrees\distracted-darwin-92195e\HERMETICDB\scripts\DEPLOY_PORTAL.py"

with open(PATH, encoding="utf-8") as f:
    src = f.read()

# Replace chained BASE_TEMPLATE.replace calls with render()
# Pattern: BASE_TEMPLATE.replace("{{title}}", TITLE).replace("{{css}}", CSS).replace("{{nav}}", NAV_BAR).replace("{{content}}", CONTENT)
# We need to handle this carefully since CONTENT can be multiline

pattern = re.compile(
    r'BASE_TEMPLATE\.replace\("{{title}}", ([^)]+)\)\.replace\("{{css}}", CSS\)\.replace\("{{nav}}", NAV_BAR\)\.replace\("{{content}}", (.*?)\)',
    re.DOTALL
)

def replacer(m):
    title_arg = m.group(1).strip()
    content_arg = m.group(2).strip()
    return f'render({title_arg}, CSS, NAV_BAR, {content_arg})'

new_src = pattern.sub(replacer, src)

count_before = src.count('BASE_TEMPLATE.replace')
count_after = new_src.count('BASE_TEMPLATE.replace')
print(f"BASE_TEMPLATE.replace calls: {count_before} -> {count_after}")

with open(PATH, "w", encoding="utf-8") as f:
    f.write(new_src)
print("Patched.")
