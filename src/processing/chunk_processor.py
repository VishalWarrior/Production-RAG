from src.chunking.recursive_chunker import recursive_chunk_text


def create_chunks(pages: list[dict]) -> list[dict]:

    processed_chunks = []

    for page in pages:

        page_number = page["metadata"]["page"]
        source = page["metadata"]["source"]

        chunks = recursive_chunk_text(
            text=page["content"],
            chunk_size=500,
            chunk_overlap=75
        )

        for index, chunk in enumerate(chunks, start=1):

            chunk_id = (
                f"{source}_p{page_number}_c{index}"
            )

            processed_chunks.append(
                {
                    "content": chunk,
                    "metadata": {
                        **page["metadata"],
                        "chunk_id": chunk_id,
                        "chunk_index": index
                    }
                }
            )

    return processed_chunks