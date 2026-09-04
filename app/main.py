from fastapi import FastAPI, Query

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