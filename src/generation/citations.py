def format_sources(retrieved_chunks):

    sources = []

    seen = set()

    for chunk in retrieved_chunks:

        metadata = chunk["metadata"]

        source = metadata.get("source", "Unknown")
        page = metadata.get("page", "Unknown")

        source_key = f"{source}_{page}"

        if source_key not in seen:

            sources.append(
                f"- {source} — Page {page}"
            )

            seen.add(source_key)

    return "\n".join(sources)