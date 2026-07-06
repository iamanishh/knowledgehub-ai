import chromadb

from app.schemas.embedding_result import EmbeddingResult


class ChromaClient:

    COLLECTION_NAME = "documents"

    def __init__(self):
        self.client = chromadb.PersistentClient(path="./chroma_db")

        self.collection = self.client.get_or_create_collection(
            name=self.COLLECTION_NAME
        )

    def add(self, document_id, embedding: EmbeddingResult, metadata: dict):

        self.collection.add(
            ids=[document_id],
            embeddings=[embedding.embedding],
            documents=[embedding.text],
            metadatas=[metadata]
        )