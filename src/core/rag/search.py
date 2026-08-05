from ollama import embed
from qdrant_client import QdrantClient

client = QdrantClient(path="data/qdrant")


def search(query):

    response = embed(
        model="nomic-embed-text",
        input=query,
    )

    vector = response["embeddings"][0]

    results = client.query_points(
        collection_name="nacca",
        query=vector,
        limit=5,
    )

    return results.points


if __name__ == "__main__":

    question = "How are fractions introduced in Basic 4?"

    hits = search(question)

    for i, hit in enumerate(hits, start=1):

        print(f"\nResult {i}")
        print(f"Score: {hit.score:.3f}")

        payload = hit.payload

        print(f"Source: {payload['source']}")
        print(f"Page: {payload['page']}")
        print()
        print(payload["text"][:800])
        print("-" * 80)
