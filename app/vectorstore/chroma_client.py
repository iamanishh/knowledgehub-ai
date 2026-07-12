import chromadb

from app.schemas.embedding_result import EmbeddingResult
from app.schemas.search_result import SearchResult
from app.core.settings import settings

class ChromaClient:

    COLLECTION_NAME = "documents"

    def __init__(self):
        self.client = chromadb.PersistentClient(path=settings.CHROMA_DIR)

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

    def get_all(self):
        return self.collection.get(
            include=["documents", "metadatas"]
        )


    def delete(self, filename: str):
        self.collection.delete(
            where={
                "filename": filename
            }
        )

    def search (self, embedding: list[float], top_k: int):

        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=top_k,
            include=["documents", "metadatas","distances"]
        )

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
        distances = results["distances"][0]

        search_results = []

        for i, document in enumerate(documents):
            result = SearchResult(
                text=document,
                filename=metadatas[i]["filename"],
                chunk=metadatas[i]["chunk"],
                distance=distances[i]
            )
            search_results.append(result)

        return search_results



