import fitz
from pathlib import Path

PDF_PATH = r"C:\Users\PC\Downloads\[Mythos The Princeton-Bollingen Series in World Mythology] Garth Fowden - The Egyptian Hermes_ A Historical Approach to the Late Pagan Mind (1993, Princeton University Press) - libgen.li.pdf"
OUTPUT_TXT = r"C:\Users\PC\Downloads\fowden_extracted.txt"

def convert():
    doc = fitz.open(PDF_PATH)
    text = ""
    for page in doc:
        text += f"--- PAGE {page.number + 1} ---\n"
        text += page.get_text()
    
    with open(OUTPUT_TXT, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Extracted {len(text)} characters to {OUTPUT_TXT}")

if __name__ == "__main__":
    convert()
