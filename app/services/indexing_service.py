from pathlib import Path

from app.schemas.embedding_result import EmbeddingResult
from app.services.document_processor import DocumentProcessor
from app.services.embedding_service import EmbeddingService
from app.chunking.text_chunker import TextChunker

class IndexingService:
    """
    Coordinates the complete indexing pipelines.

    Current pipeline: PDF -> Parse -> Chunk -> Embedding
    """

    def __init__(self):
        self.processor = DocumentProcessor()
        self.chunker = TextChunker()
        self.embedding_service = EmbeddingService()

    def index_document(self, file_path: Path) -> list[EmbeddingResult]:

        parsed_document = self.processor.process(file_path)

        chunks = self.chunker.split(parsed_document)

        embeddings = []

        for chunk in chunks:
            embedding = self.embedding_service.embed(chunk.text)
            embeddings.append(embedding)

        return embeddings