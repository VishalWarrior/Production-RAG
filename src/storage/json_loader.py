import json

def load_chunks(file_path: str) -> list[dict]:
    with open(file_path, "r", encoding="utf-8") as file:
        chunks = json.load(file)

    return chunks