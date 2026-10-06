from fastapi import APIRouter, Query, status, Depends

from schemas import DocumentCreate, DocumentResponse

from sqlalchemy.orm import Session

from models import Document

from database import get_db

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


@router.get("")
async def list_documents(
    search: str | None = None,
    skip: int=0,
    limit: int = Query(default=10, le=100)
):

    return {
        "search": search,
        "skip": skip,
        "limit": limit
    }

@router.get("/{document_id}")
async def get_document(
    document_id: int
):
    return {
        "document_id": document_id
    }


@router.post("", 
          response_model=DocumentResponse,
          status_code=status.HTTP_201_CREATED
          )
def create_document(
    document: DocumentCreate,
    db: Session = Depends(get_db)):  

    db_document = Document(
        title=document.title,
        description=document.description,
        category=document.category,
        priority=document.priority
    )  
    try:
        db.add(db_document)
        db.commit()
        db.refresh(db_document)

    except:
        db.rollback()
        raise


    return db_document