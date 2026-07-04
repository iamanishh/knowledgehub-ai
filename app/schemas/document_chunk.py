from pydantic import BaseModel

class DocumentChunk(BaseModel):
    chunk_id: int
    text: str
    source_document: str
    metadata: dict
