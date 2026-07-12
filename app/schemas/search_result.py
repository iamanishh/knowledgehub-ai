from pydantic import BaseModel

class SearchResult(BaseModel):
    text: str
    filename: str
    chunk: int
    distance: float