import re

def split_sentence(text: str) -> list[str]:
    """
    Basic sentence splitter
    """
    return re.split(r'(?<=[.!?])\s+', text)

def smart_chunk_text(
    text: str,
    chunk_size: int = 500,
    overlap: int = 50
) -> list[str]:

    sentences = split_sentence(text)

    chunks = []
    current_chunk = ""

    for sentence in sentences:

        sentence = sentence.strip()

        if not sentence:
            continue

        # If adding sentence stays within chunk limit
        if len(current_chunk) + len(sentence) + 1 <= chunk_size:

            current_chunk += sentence + " "

        else:

            # Save current chunk
            chunks.append(current_chunk.strip())

            # Start new chunk
            current_chunk = sentence + " "

    # Add last remaining chunk
    if current_chunk.strip():
        chunks.append(current_chunk.strip())

    return chunks