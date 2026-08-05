import json
from pathlib import Path

EMBEDDINGS_FILE = Path("data/embeddings.jsonl")


def load_embeddings():
    with open(EMBEDDINGS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            yield json.loads(line)


if __name__ == "__main__":
    count = 0

    for record in load_embeddings():
        count += 1

    print(f"Loaded {count} embeddings")
