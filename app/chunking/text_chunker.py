from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.schemas.document_chunk import DocumentChunk
from app.schemas.parsed_document import ParsedDocument


class TextChunker:

    def __init__(self):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=150,
            length_function=len,
            is_separator_regex=False
        )

    def split(self, document: ParsedDocument) -> list[DocumentChunk]:

        chunks = self.splitter.split_text(document.text)

        result = []

        for index, chunk in enumerate(chunks):
            result.append(
                DocumentChunk(
                    chunk_id=index + 1,
                    text=chunk,
                    source_document=document.filename,
                    metadata=document.metadata,
                )
            )
        return result