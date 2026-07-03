import fitz
from pathlib import Path
from app.schemas.parsed_document import ParsedDocument


class PDFParser:
    def parse(self, file_path: Path) -> ParsedDocument:
        """
        Parses a PDF and extracts text + metadata.
        """

        document = fitz.open(file_path)

        text = ""

        for page in document:
            text += page.get_text()

        parsed_document = ParsedDocument(
            filename=file_path.name,
            pages=len(document),
            text=text,
            metadata=document.metadata or {}
        )
        document.close()

        return parsed_document

