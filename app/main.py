from fastapi import FastAPI
from app.api import upload

app = FastAPI(title="AI Document Intelligence API")

app.include_router(upload.router, prefix="/upload", tags=["Upload"])