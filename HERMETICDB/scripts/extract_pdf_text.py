import sys
from pypdf import PdfReader

def extract_text(pdf_path, max_pages=10):
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for i in range(min(max_pages, len(reader.pages))):
            text += reader.pages[i].extract_text() + "\n"
        return text
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_pdf_text.py <pdf_path> [max_pages]")
    else:
        path = sys.argv[1]
        pages = int(sys.argv[2]) if len(sys.argv) > 2 else 10
        print(extract_text(path, pages))
