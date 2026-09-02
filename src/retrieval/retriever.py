def format_retrieval_results(results):

    retrieved_chunks = []

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    for index, document in enumerate(documents):

        retrieved_chunks.append(
            {
                "rank": index + 1,
                "content": document,
                "metadata": metadatas[index],
                "distance": distances[index]
            }
        )

    return retrieved_chunks

def is_relevant(
        retrieved_chunks,
        max_distance=0.9
):
    if not retrieved_chunks:
        return False
    best_distance = retrieved_chunks[0]["distance"]
    return best_distance<=max_distance