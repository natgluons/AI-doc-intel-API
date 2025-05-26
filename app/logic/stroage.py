from app.core.supabase_client import supabase

def upload_to_storage(filename, content):
    supabase.storage.from_("documents").upload(filename, content)
    return f"https://{supabase.url}/storage/v1/object/public/documents/{filename}"

