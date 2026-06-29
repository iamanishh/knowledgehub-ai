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
    pass

