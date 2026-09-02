def build_rag_prompt(query, retrieved_chunks):
    context_parts = []
    for chunk in retrieved_chunks:

        source = chunk["metadata"]["source"]
        page = chunk["metadata"]["page"]
        content = chunk["content"]

        context_parts.append(
            f"Source: {source}, Page:{page}\n"
            f"{content}"
        )

    context = "\n\n---\n\n".join(
        context_parts
    )

    prompt = f"""
    You are an enterprise knowledge assistant.
    Answer the user's question using ONLY the provided context.

    Rules:
    1. Do not use information outside the context.
    2. If the answer is not available in the context, say: "I don't know based on the provided documents."
    3. Do not make up information.
    4. Give a concise and accurate answer.

    Context:
    {context}

    User Question:
    {query}

    Answer:
    """
    return prompt