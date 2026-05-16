import sys
import fitz  # PyMuPDF

def extract_text(pdf_path, output_path, max_pages=50):
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for i in range(min(max_pages, len(doc))):
            text += doc[i].get_text() + "\n"
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)
        return f"Successfully extracted {min(max_pages, len(doc))} pages to {output_path}"
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python extract_pdf_to_file.py <pdf_path> <output_path> [max_pages]")
    else:
        path = sys.argv[1]
        out = sys.argv[2]
        pages = int(sys.argv[3]) if len(sys.argv) > 3 else 50
        print(extract_text(path, out, pages))
