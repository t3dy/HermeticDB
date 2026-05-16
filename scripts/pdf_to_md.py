import fitz
import sys

def pdf_to_md(pdf_path, md_path):
    doc = fitz.open(pdf_path)
    with open(md_path, 'w', encoding='utf-8') as f:
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text = page.get_text("text")
            f.write(f"## Page {page_num + 1}\n\n")
            f.write(text)
            f.write("\n\n")
    print(f"Successfully converted to {md_path}")

if __name__ == "__main__":
    pdf_path = sys.argv[1]
    md_path = sys.argv[2]
    pdf_to_md(pdf_path, md_path)
