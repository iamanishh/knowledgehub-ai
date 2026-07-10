from pydantic import BaseModel

class DocumentSummary(BaseModel):

    """
    Summary of one indexed document
    """

    filename: str
    chunks: int 