from pathlib import Path
from langchain_community.document_loaders import (
    WebBaseLoader,
    PyPDFLoader
)
def load_documents():

    docs = []

    # Locate the project root
    BASE_DIR = Path(__file__).resolve().parent.parent.parent

    # datasets_pdf folder
    pdf_folder = BASE_DIR / "datasets_pdf"

    # Load NIST PDF
    nist_pdf = pdf_folder / "NIST.SP.800-61r3.pdf"

    docs.extend(
        PyPDFLoader(str(nist_pdf)).load()
    )

    urls = [
        "https://www.rfc-editor.org/rfc/rfc3031.html",
        "https://www.rfc-editor.org/rfc/rfc5036.html",
        "https://docs.frrouting.org/en/latest/_sources/index.rst.txt",
        "https://www.rfc-editor.org/rfc/rfc4271.html",
        "https://www.rfc-editor.org/rfc/rfc3270.html"
    ]

    for url in urls:
        docs.extend(
            WebBaseLoader(url).load()
        )

    print("Data loaded successfully")

    return docs