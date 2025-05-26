from doctr.io import DocumentFile
from doctr.models import ocr_predictor

def process_document(file_bytes):
    doc = DocumentFile.from_pdf(file_bytes)
    model = ocr_predictor(pretrained=True)
    result = model(doc)
    return result.export()['text']