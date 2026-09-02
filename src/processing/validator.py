from collections import Counter


def validate_chunks(
    chunks: list[dict],
    min_chunk_length: int = 50,
    max_chunk_length: int = 600
) -> dict:

    errors = []
    warnings = []

    chunk_ids = []
    contents = []

    for index, chunk in enumerate(chunks, start=1):

        content = chunk.get("content", "").strip()
        metadata = chunk.get("metadata", {})

        # 1. Empty chunk
        if not content:
            errors.append(
                f"Chunk {index}: Empty content"
            )
            continue

        # 2. Chunk size validation
        content_length = len(content)

        if content_length < min_chunk_length:
            warnings.append(
                f"Chunk {index}: Too small "
                f"({content_length} characters)"
            )

        if content_length > max_chunk_length:
            warnings.append(
                f"Chunk {index}: Too large "
                f"({content_length} characters)"
            )

        # 3. Required metadata
        required_fields = [
            "source",
            "page",
            "chunk_id",
            "chunk_index"
        ]

        for field in required_fields:

            if field not in metadata:
                errors.append(
                    f"Chunk {index}: Missing metadata '{field}'"
                )

        chunk_ids.append(
            metadata.get("chunk_id")
        )

        contents.append(content)

    # 4. Duplicate IDs
    id_counts = Counter(chunk_ids)

    for chunk_id, count in id_counts.items():

        if chunk_id and count > 1:

            errors.append(
                f"Duplicate chunk_id: {chunk_id}"
            )

    # 5. Exact duplicate content
    content_counts = Counter(contents)

    duplicate_count = sum(
        count - 1
        for count in content_counts.values()
        if count > 1
    )

    if duplicate_count > 0:

        warnings.append(
            f"{duplicate_count} duplicate chunk(s) found"
        )

    return {
        "is_valid": len(errors) == 0,
        "total_chunks": len(chunks),
        "errors": errors,
        "warnings": warnings
    }