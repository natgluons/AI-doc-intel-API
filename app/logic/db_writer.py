from app.core.supabase_client import supabase
import uuid

def insert_metadata(fields, vector, file_url):
    supabase.table("documents").insert({
        "id": str(uuid.uuid4()),
        "fields": fields,
        "embedding": vector.tolist(),
        "file_url": file_url
    }).execute()