from qdrant_client import QdrantClient
from ollama import embed, chat


COLLECTION = "eira_school_material"
EMBEDDING_MODEL = "nomic-embed-text"
LANGUAGE_MODEL = "gemma3:4b"
QDRANT_PATH = "data/qdrant"
NUMBER_OF_CHUNKS = 5


def create_embedding(text: str):
    response = embed(
        model=EMBEDDING_MODEL,
        input=text,
    )
    return response["embeddings"][0]


def retrieve_context(client: QdrantClient, question: str):
    query_vector = create_embedding(question)

    results = client.query_points(
        collection_name=COLLECTION,
        query=query_vector,
        limit=NUMBER_OF_CHUNKS,
        with_payload=True,
    )

    return results.points


def build_context(points):
    sections = []

    for index, point in enumerate(points, start=1):
        payload = point.payload or {}

        source = payload.get("source", "Unknown source")
        page = payload.get("page", "Unknown page")
        text = payload.get("text", "")

        sections.append(
            f"[Source {index}: {source}, page {page}]\n{text}"
        )

    return "\n\n".join(sections)


def answer_question(question: str, context: str):
    system_prompt = """
You are Eira, an educational assistant.

Answer the question using the supplied curriculum context as your primary
source. Do not invent curriculum requirements.

You may use your general knowledge to explain concepts clearly, but clearly
distinguish general explanation from information stated in the curriculum.

If the context does not contain enough information, say so.

End your answer with a short Sources section listing the source numbers and
pages you relied upon.
""".strip()

    user_prompt = f"""
CURRICULUM CONTEXT

{context}

QUESTION

{question}
""".strip()

    response = chat(
        model=LANGUAGE_MODEL,
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ],
    )

    return response["message"]["content"]


def main():
    question = input("Question: ").strip()

    if not question:
        print("No question entered.")
        return

    client = QdrantClient(path=QDRANT_PATH)

    try:
        points = retrieve_context(client, question)

        if not points:
            print("No relevant curriculum passages were found.")
            return

        context = build_context(points)

        print("\nRetrieved sources:")
        for index, point in enumerate(points, start=1):
            payload = point.payload or {}
            print(
                f"{index}. Score {point.score:.3f} — "
                f"{payload.get('source')} page {payload.get('page')}"
            )

        print("\nGemma is answering...\n")

        answer = answer_question(question, context)
        print(answer)

    finally:
        client.close()


if __name__ == "__main__":
    main()
