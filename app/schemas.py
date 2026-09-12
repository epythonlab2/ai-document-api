from pydantic import BaseModel, Field,HttpUrl
from enum import Enum

class DocumentCategory(str, Enum):
    programming = "programming"
    research = "research"
    business = "business"
    finance = "finance"


class DocumentSource(BaseModel):
    name: str
    url: HttpUrl | None = None

class DocumentBase(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: str | None = Field(
        default=None,
        max_length=2000
    )
    category: DocumentCategory | None = None
    
class DocumentCreate(DocumentBase):
    
    priority: int = Field(default=3, ge=1, le=5)

    source: DocumentSource | None = None


class DocumentResponse(DocumentBase):
    id: int
