from pathlib import Path
import json
from ollama import embed


INPUT_FILE = Path("data/chunks.jsonl")
OUTPUT_FILE = Path("data/embeddings.jsonl")
MODEL = "nomic-embed-text"


def create_embedding(text: str):
    response = embed(
        model=MODEL,
        input=text,
    )

    return response["embeddings"][0]


if not INPUT_FILE.exists():
    raise FileNotFoundError(
        f"{INPUT_FILE} does not exist. Run src/rag/load_pdfs.py first."
    )

records = []

with INPUT_FILE.open("r", encoding="utf-8") as input_file:
    for line in input_file:
        records.append(json.loads(line))

print(f"Embedding {len(records)} chunks")

with OUTPUT_FILE.open("w", encoding="utf-8") as output_file:
    for index, record in enumerate(records, start=1):
        vector = create_embedding(record["text"])

        record["embedding"] = vector
        output_file.write(json.dumps(record, ensure_ascii=False) + "\n")

        print(
            f"{index}/{len(records)} "
            f"{record['source']} page {record['page']}",
            flush=True,
        )

print(f"Saved embeddings to {OUTPUT_FILE}")