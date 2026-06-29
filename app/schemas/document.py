from pydantic import BaseModel
from datetime import datetime

class DocumentResponse(BaseModel):

    id: str
    filename: str
    stored_filename: str
    content_type: str
    uploaded_at: datetime
    status: str