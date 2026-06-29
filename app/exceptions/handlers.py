from fastapi import Request
from fastapi.responses import JSONResponse

from app.exceptions.custom_exceptions import (
    InvalidFileTypeError,
    EmptyFilenameError,
    FileTooLargeError,
    DocumentSaveError
)

def register_exception_handlers(app):

    @app.exception_handler(InvalidFileTypeError)
    async def invalid_file_type_handler(request: Request, exc: InvalidFileTypeError):
        return JSONResponse(
            status_code=415,
            content={"detail": "Unsupported File Type"},
        )

    @app.exception_handler(EmptyFilenameError)
    async def empty_filename_handler(request: Request, exc: EmptyFilenameError):
        return JSONResponse(
            status_code=400,
            content={"detail": "Filename is required."},
        )

    @app.exception_handler(FileTooLargeError)
    async def file_too_large_handler(request: Request, exc: FileTooLargeError):
        return JSONResponse(
            status_code=413,
            content={"detail": "Maximum upload size is 20 MB."},
        )

    @app.exception_handler(DocumentSaveError)
    async def document_save_handler(request: Request, exc: DocumentSaveError):
        return JSONResponse(
            status_code=500,
            content={"detail": "Document upload failed."},
        )



























