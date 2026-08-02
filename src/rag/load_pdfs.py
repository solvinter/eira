from pathlib import Path
import pymupdf


def find_pdfs(folder):
    return list(folder.glob("*.pdf"))


def load_pdf(pdf_path):
    document = pymupdf.open(pdf_path)

    text = ""

    for page in document:
        text += page.get_text()

    return text

def chunk_text(text, chunk_size=1000):
    chunks = []

    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])

    return chunks


documents = Path("documents/nacca/mathematics")

pdfs = find_pdfs(documents)

for pdf in pdfs:
    print(f"\nLoading {pdf.name}")

    text = load_pdf(pdf)

    chunks = chunk_text(text)

    print(f"{len(chunks)} chunks created")

    if chunks:
        print(chunks[0][:500])

    print("-" * 80)