import json
from pathlib import Path


def save_chunks(
    chunks: list[dict],
    output_path: str
) -> None:

    path = Path(output_path)

    # Parent directory create if missing
    path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            chunks,
            file,
            indent=4,
            ensure_ascii=False
        )

    print(
        f"\nSuccessfully saved {len(chunks)} chunks"
    )

    print(
        f"Location: {path}"
    )