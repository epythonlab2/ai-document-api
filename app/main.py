from fastapi import FastAPI

from routes.documents import router as documents_router

from database import Base, engine

import models

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "AI Document API"}


app.include_router(documents_router)


