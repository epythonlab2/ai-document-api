from fastapi import FastAPI, Query, status

from routes.documents import router as documents_router

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "AI Document API"}


app.include_router(documents_router)


