from pathlib import Path
import json

from qdrant_client import QdrantClient, models


INPUT_FILE = Path("data/embeddings.jsonl")
QDRANT_PATH = "data/qdrant"
COLLECTION_NAME = "eira_school_material"
VECTOR_SIZE = 768
BATCH_SIZE = 50


def load_records():
    with INPUT_FILE.open("r", encoding="utf-8") as file:
        for line in file:
            yield json.loads(line)


client = QdrantClient(path=QDRANT_PATH)

if client.collection_exists(COLLECTION_NAME):
    client.delete_collection(COLLECTION_NAME)

client.create_collection(
    collection_name=COLLECTION_NAME,
    vectors_config=models.VectorParams(
        size=VECTOR_SIZE,
        distance=models.Distance.COSINE,
    ),
)

batch = []
total = 0

for point_id, record in enumerate(load_records()):
    vector = record.pop("embedding")

    batch.append(
        models.PointStruct(
            id=point_id,
            vector=vector,
            payload=record,
        )
    )

    if len(batch) >= BATCH_SIZE:
        client.upsert(
            collection_name=COLLECTION_NAME,
            points=batch,
            wait=True,
        )
        total += len(batch)
        print(f"Imported {total} points", flush=True)
        batch = []

if batch:
    client.upsert(
        collection_name=COLLECTION_NAME,
        points=batch,
        wait=True,
    )
    total += len(batch)

print(f"Finished: {total} points imported")
print(client.get_collection(COLLECTION_NAME))
client.close()
