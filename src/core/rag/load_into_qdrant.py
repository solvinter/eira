import json
from pathlib import Path

from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct

EMBEDDINGS_FILE = Path("data/embeddings.jsonl")

client = QdrantClient(path="data/qdrant")


with open(EMBEDDINGS_FILE, "r", encoding="utf-8") as f:

    points = []

    for idx, line in enumerate(f):

        record = json.loads(line)

        points.append(
            PointStruct(
                id=idx,
                vector=record["embedding"],
                payload={
                    "text": record["text"],
                    "source": record["source"],
                    "page": record["page"],
                },
            )
        )

    client.upsert(
        collection_name="nacca",
        points=points,
    )

print(f"Inserted {len(points)} vectors.")

