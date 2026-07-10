from datetime import datetime
import uuid
from fastapi import HTTPException

from app.schemas.document import  DocumentResponse
from app.utils.document_validator import DocumentValidator
from app.utils.file_manager import FileManager
from app.core.logging import logger
from app.services.indexing_service import IndexingService
from app.vectorstore.chroma_client import ChromaClient
from app.schemas.document_summary import DocumentSummary
from pathlib import Path

indexing_service = IndexingService()
client = ChromaClient()
UPLOAD_DIR = Path("uploads")


class DocumentService:

    @staticmethod
    def upload(file):

        logger.info("Starting document upload.")
        DocumentValidator.validate(file)

        stored_file_path = FileManager.save(file)

        embeddings = indexing_service.index_document(stored_file_path)

        logger.info(
            "Document indexed successfully | embeddings=%s",
            len(embeddings),
        )

        logger.info(
            "Document uploaded successfully | original_filename=%s stored_filename=%s",
            file.filename,
            stored_file_path.name,
        )

        return DocumentResponse(
            id=str(uuid.uuid4()),
            filename=file.filename,
            stored_filename=stored_file_path.name,
            content_type=file.content_type,
            uploaded_at=datetime.now(),
            status="uploaded"
        )


    @staticmethod
    def list_documents():
        data = client.get_all()

        documents = {}

        for metadata in data["metadatas"]:
            filename = metadata["filename"]

            if filename not in documents:
                documents[filename] = 1
            else:
                documents[filename] += 1


        result = []
        for filename, chunks in documents.items():
            result.append(
                DocumentSummary(
                    filename=filename,
                    chunks=chunks
               )
            )
        return result

    @staticmethod
    def delete_document(stored_filename: str):

        file_path = UPLOAD_DIR / stored_filename

        if not file_path.exists():
            raise HTTPException(
                status_code=404,
                detail="Document not found"
            )

        client.delete(stored_filename)

        file_path.unlink()

        logger.info(
            "Document deleted successfully | filename=%s",
            stored_filename
        )

        return {
            "message": "Document deleted successfully"
        }










    