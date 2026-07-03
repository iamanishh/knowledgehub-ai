from pathlib import Path

from app.parsers.pdf_parser import PDFParser
from app.schemas.parsed_document import ParsedDocument

class DocumentProcessor:
    """
       Processes a saved document.

       Current responsibilities:
       - Parse PDF
       - Clean extracted text

       Later this class will also:
       - OCR
       - Metadata enrichment
       - Language detection
       """

    def __init__(self):
        self.parser = PDFParser()

    def process(self, file_path: Path) -> ParsedDocument:
        parsed_document = self.parser.parse(file_path)

        cleaned_text = self._clean_text(parsed_document.text)

        return ParsedDocument(
            filename=parsed_document.filename,
            pages=parsed_document.pages,
            text=cleaned_text,
            metadata=parsed_document.metadata
        )

    @staticmethod
    def _clean_text(text: str) -> str:
        """
        Removes excessive whitespace/newlines.
        """
        return " ".join(text.split())



