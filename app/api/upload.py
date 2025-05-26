from fastapi import APIRouter, UploadFile, File
from app.ocr.processor import process_document
from app.logic.extractor import extract_fields
from app.logic.vectorizer import embed_text
from app.logic.storage import upload_to_storage
from app.logic.db_writer import insert_metadata

router = APIRouter()

@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    ocr_text = process_document(content)
    fields = extract_fields(ocr_text)
    vector = embed_text(ocr_text)
    file_url = upload_to_storage(file.filename, content)
    insert_metadata(fields, vector, file_url)
    return {"status": "success", "fields": fields, "url": file_url}

