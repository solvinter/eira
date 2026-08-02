from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

client = QdrantClient("127.0.0.1", port=6333)

client.recreate_collection(
    collection_name="nacca",
    vectors_config=VectorParams(
        size=768,
        distance=Distance.COSINE,
    ),
)

print("Collection created!")
