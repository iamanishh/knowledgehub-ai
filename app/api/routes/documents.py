from fastapi import APIRouter, UploadFile, File

from app.core.logging import logger
from app.schemas.document import DocumentResponse
from app.services.document_service import DocumentService
from app.schemas.document_summary import DocumentSummary


router = APIRouter(
    prefix="/documents",
    tags=["documents"]
)

@router.post("/upload", response_model=DocumentResponse)
def upload_document(file: UploadFile = File(...)):

    logger.info("Received document upload request.")
    return DocumentService().upload(file)

@router.get("", response_model=list[DocumentSummary])
def list_documents():
    return DocumentService.list_documents()

@router.delete("/{document_id}")
def delete_document(document_id: str):
    return DocumentService.delete_document(document_id)