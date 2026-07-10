from pathlib import Path

from app.schemas.embedding_result import EmbeddingResult
from app.services.document_processor import DocumentProcessor
from app.services.embedding_service import EmbeddingService
from app.chunking.text_chunker import TextChunker
from app.vectorstore.chroma_client import ChromaClient
import uuid

class IndexingService:
    """
    Coordinates the complete indexing pipelines.

    Current pipeline: PDF -> Parse -> Chunk -> Embedding
    """

    def __init__(self):
        self.processor = DocumentProcessor()
        self.chunker = TextChunker()
        self.embedding_service = EmbeddingService()
        self.vector_db = ChromaClient()

    def index_document(self, file_path: Path) -> list[EmbeddingResult]:

        parsed_document = self.processor.process(file_path)

        chunks = self.chunker.split(parsed_document)

        embeddings = []

        for i, chunk in enumerate(chunks):
            embedding = self.embedding_service.embed(chunk.text)

            self.vector_db.add(
                document_id=str(uuid.uuid4()),
                embedding=embedding,
                metadata={
                    "filename": file_path.name,
                    "chunk": i
                }
            )

            embeddings.append(embedding)

        return embeddings