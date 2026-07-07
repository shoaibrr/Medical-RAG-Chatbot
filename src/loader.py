from pathlib import Path

from langchain_core.documents import Document
from src.metadata import extract_metadata


def load_text_documents(data_folder="data"):

    documents = []

    data_path = Path(data_folder)

    for file_path in data_path.rglob("*.txt"):

        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        # Extract metadata from document text
        metadata = extract_metadata(content)

        # Add file-related metadata
        metadata["file_name"] = file_path.name
        metadata["file_path"] = str(file_path)
        metadata["document_type"] = file_path.parent.name

        document = Document(
            page_content=content,
            metadata=metadata,
        )

        documents.append(document)

    return documents