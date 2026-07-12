from fastapi import APIRouter, UploadFile, File

from app.core.logging import logger
from app.schemas.document import DocumentResponse
from app.services.document_service import DocumentService
from app.schemas.document_summary import DocumentSummary


router = APIRouter(
    prefix="/documents",
    tags=["documents"]
)

@router.post("/upload",
             summary="Upload document",
             description="Uploads a PDF, indexes it into ChromaDB and generates embeddings.",
             response_model=DocumentResponse,
             status_code=201
             )
def upload_document(file: UploadFile = File(...)):

    logger.info("Received document upload request.")
    return DocumentService().upload(file)



@router.get("",
            summary="Get all documents",
            description="Get all documents present in the database",
            status_code=200,
            response_model=list[DocumentSummary])
def list_documents():
    return DocumentService.list_documents()



@router.delete("/{document_id}",
               summary="Delete a document",
               description="Deletes a document from the database",
               status_code=204,
               )
def delete_document(document_id: str):
    return DocumentService.delete_document(document_id)