from pydantic import BaseModel

class ParsedDocument(BaseModel):
    """
        Represents a parsed document after extracting content
        from the original file.
    """
    filename: str
    pages: int
    text: str
    metadata: dict
