import re

def extract_fields(text):
    # Simple regex-based placeholder logic
    return {
        "invoice_id": re.search(r"Invoice\s*#?:?\s*(\w+)", text).group(1) if re.search(r"Invoice\s*#?:?\s*(\w+)", text) else None,
        "total": re.search(r"Total\s*:?\s*\$?(\d+[.,]?\d*)", text).group(1) if re.search(r"Total\s*:?\s*\$?(\d+[.,]?\d*)", text) else None
    }