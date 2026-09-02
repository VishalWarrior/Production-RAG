import pymupdf
from pathlib import Path

def load_pdf(file_path: str) -> list[dict]:
    """
    Extract text from a PDF page by page.
    """
    pdf_path = Path(file_path)

    if not pdf_path.exists():
        raise FileNotFoundError(
            f"PDF not found: {pdf_path}"
        )
    document = pymupdf.open(pdf_path)
    pages =[]
    try:
        for page_number, page in enumerate(document, start=1):
            text = page.get_text("text").strip()
            if not text:
                print(
                    f"Warning : No extractable text on page {page_number}"

                )
                continue
            pages.append(
                {
                    "content": text,
                    "metadata": {
                        "source": pdf_path.name,
                        "page": page_number,
                        "file_path": str(pdf_path)
                    }
                }
            )
    finally:
        document.close()
    return pages