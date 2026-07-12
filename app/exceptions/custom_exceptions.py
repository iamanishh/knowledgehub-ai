class ApplicationError(Exception):
    """ Base class for all application exception."""
    pass

class InvalidFileTypeError(ApplicationError):
    pass

class FileTooLargeError(ApplicationError):
    pass

class EmptyFilenameError(ApplicationError):
    pass

class DocumentSaveError(ApplicationError):
    def __init__(self, filename: str):
        super().__init__(f"Failed to save document '{filename}'.")
        self.filename = filename


class DocumentNotFoundError(ApplicationError):
    def __init__(self, filename: str):
        super().__init__(f"Document '{filename}' not found")
        self.filename = filename
