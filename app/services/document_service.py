from datetime import datetime
import uuid

from app.schemas.document import  DocumentResponse
from app.utils.document_validator import DocumentValidator
from app.utils.file_manager import FileManager
from app.core.logging import logger

class DocumentService:

    @staticmethod
    def upload(file):

        logger.info("Starting document upload.")
        DocumentValidator.validate(file)

        stored_filename = FileManager.save(file)
        logger.info("Document uploaded successfully | "
                    "original_filename=%s  stored_filename=%s content_type=%s ",
                    file.filename,
                    stored_filename,
                    file.content_type
        )

        return DocumentResponse(
            id=str(uuid.uuid4()),
            filename=file.filename,
            stored_filename=stored_filename,
            content_type=file.content_type,
            uploaded_at=datetime.now(),
            status="uploaded"
        )

    