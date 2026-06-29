from fastapi import APIRouter, UploadFile, File

from app.core.logging import logger
from app.schemas.document import DocumentResponse
from app.services.document_service import DocumentService

router = APIRouter(
    prefix="/documents",
    tags=["documents"]
)

@router.post("/upload", response_model=DocumentResponse)
def upload_document(file: UploadFile = File(...)):

    logger.info("Received document upload request.")
    return DocumentService().upload(file)