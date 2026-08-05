from qdrant_client import QdrantClient
from ollama import embed

COLLECTION = "eira_school_material"
MODEL = "nomic-embed-text"

client = QdrantClient(path="data/qdrant")


def create_embedding(text):
    response = embed(
        model=MODEL,
        input=text
    )
    return response["embeddings"][0]


query = input("Question: ")

query_vector = create_embedding(query)

results = client.query_points(
    collection_name=COLLECTION,
    query=query_vector,
    limit=5,
)

print("\nTop matches:\n")

for i, point in enumerate(results.points, start=1):
    payload = point.payload

    print(f"{i}. Score: {point.score:.3f}")
    print(f"Source: {payload['source']}")
    print(f"Page: {payload['page']}")
    print(payload["text"][:500])
    print("-" * 80)

client.close()
