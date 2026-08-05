from pathlib import Path
import json
import pymupdf


def find_pdfs(folder: Path):
    return sorted(folder.glob("*.pdf"))


def load_pdf(pdf_path: Path):
    document = pymupdf.open(pdf_path)
    pages = []

    for page_number, page in enumerate(document, start=1):
        text = page.get_text().strip()
        if text:
            pages.append((page_number, text))

    return pages


def chunk_text(text: str, chunk_size: int = 1000, overlap: int = 150):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


documents = Path("documents/nacca/mathematics")
output_file = Path("data/chunks.jsonl")
output_file.parent.mkdir(parents=True, exist_ok=True)

total_chunks = 0

with output_file.open("w", encoding="utf-8") as output:
    for pdf in find_pdfs(documents):
        print(f"Loading {pdf.name}")

        for page_number, page_text in load_pdf(pdf):
            chunks = chunk_text(page_text)

            for chunk_index, chunk in enumerate(chunks):
                record = {
                    "source": str(pdf),
                    "page": page_number,
                    "chunk_index": chunk_index,
                    "text": chunk,
                }

                output.write(json.dumps(record, ensure_ascii=False) + "\n")
                total_chunks += 1

print(f"Saved {total_chunks} chunks to {output_file}")