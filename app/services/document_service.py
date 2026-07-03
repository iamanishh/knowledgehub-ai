from datetime import datetime
import uuid

from app.schemas.document import  DocumentResponse
from app.utils.document_validator import DocumentValidator
from app.utils.file_manager import FileManager
from app.core.logging import logger
from app.services.document_processor import DocumentProcessor

processor = DocumentProcessor()

class DocumentService:

    @staticmethod
    def upload(file):

        logger.info("Starting document upload.")

        DocumentValidator.validate(file)
        stored_file_path = FileManager.save(file)

        parsed_document = processor.process(stored_file_path)

        logger.info(
            "Document processed | pages=%s text_length=%s",
            parsed_document.pages,
            len(parsed_document.text),
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

    