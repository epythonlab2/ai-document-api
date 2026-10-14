from fastapi import APIRouter, Query, status, Depends, HTTPException

from schemas import DocumentCreate, DocumentResponse

from sqlalchemy import select

from sqlalchemy.orm import Session

from models import Document

from database import get_db

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


@router.get("",
            response_model=list[DocumentResponse],
            status_code=status.HTTP_200_OK)

def list_documents(
    search: str | None = None,
    skip: int= Query(default=0, ge=0),
    limit: int = Query(default=10, le=100),
    db:Session = Depends(get_db)
   
):
    statement = select(Document)

    if search:
        statement = statement.where(
            Document.title.ilike(f"%{search}%")
        )

    statement = (
        statement
        .order_by(Document.id)
        .offset(skip)
        .limit(limit)
    )
    
    documents = db.scalars(statement).all()

    return documents


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
    