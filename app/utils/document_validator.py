from fastapi import FastAPI, UploadFile, HTTPException
from app.exceptions.custom_exceptions import InvalidFileTypeError,EmptyFilenameError
from app.core.logging import logger
class DocumentValidator:

    @staticmethod
    def validate(file: UploadFile):
        if not file.filename:
            raise EmptyFilenameError

        if not file.filename.lower().endswith(".pdf"):
            logger.warning(
                "Rejected upload due to unsupported file type: %s",
                file.filename
            )
            raise InvalidFileTypeError


