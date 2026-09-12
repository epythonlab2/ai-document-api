from fastapi import FastAPI, Query, status

from schemas import DocumentCreate, DocumentResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "AI Document API"}

@app.get("/documents")
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

@app.get("/users/{user_id}/documents/{document_id}")
async def get_user_document(
    user_id: int,
    document_id: int
):
    return {
        "user_id": user_id,
        "document_id": document_id
    }

@app.post("/documents", 
          response_model=DocumentResponse,
          status_code=status.HTTP_201_CREATED
          )
async def create_document(document: DocumentCreate):
    return {
        "id": 1,
        "title": document.title,
        "description": document.description,
        "category": document.category
    }
