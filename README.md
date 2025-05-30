# AI Document Intelligence API: Invoice Analyzer & ID Verifier

## About
The **AI Document Intelligence API** is a smart document processing system that combines invoice analysis and identity document verification in a unified backend. This project is built to address practical problems in **financial operations**, **document automation**, and **fraud detection** by leveraging OCR, vector search, and knowledge graphs.

Manual document validation is time-consuming and error-prone. This API offers automated pipelines for extracting structured data, detecting duplicate or suspicious documents, and matching key fields to existing records or knowledge graphs, making it useful for fintech, procurement, and KYC applications.

---

## Tech Stack

| Layer         | Tech Used                              | Purpose                                            |
|--------------|-----------------------------------------|----------------------------------------------------|
| Backend API  | FastAPI                                 | API server and document routing                    |
| Database     | Supabase (PostgreSQL)                   | Structured data + file storage                     |
| Embedding    | PgVector                                | Vector search and semantic similarity              |
| OCR          | DocTR / TrOCR                   | Multimodal text extraction from images/PDFs        |
| Graph        | Neo4j (optional)             | Fraud relationship analysis and vendor graphs      |
| Cloud        | Microsoft Azure                         | OCR inference hosting, file uploads                |

---

## Architecture Diagram

```mermaid
graph TD
    A[User Uploads Document] --> B[FastAPI Upload Endpoint]
    B --> C[OCR Module - DocTR or TrOCR]
    C --> D[Extracted Text]
    D --> E[Field Extraction and Classification]
    E --> F[Vector Embedding with PgVector]
    F --> G[Similarity Search and Duplicate Detection]
    E --> H[Save Fields to Supabase DB]
    B --> I[Upload Original File to Supabase Storage]
    G --> J[Optional Fraud and Vendor Graph - Neo4j]
```

---

## Database Schema (Supabase)

### `documents`
| Column        | Type        | Description                         |
|---------------|-------------|-------------------------------------|
| id            | UUID        | Primary key                         |
| user_id       | UUID        | Reference to user                   |
| doc_type      | TEXT        | 'invoice', 'id_card', 'certificate' |
| file_url      | TEXT        | Supabase storage URL                |
| upload_date   | TIMESTAMP   | Document upload date                |
| status        | TEXT        | 'processed', 'error', etc.          |

### `extracted_fields`
| Column        | Type        | Description                         |
|---------------|-------------|-------------------------------------|
| id            | UUID        | Primary key                         |
| doc_id        | UUID        | Foreign key to documents            |
| field_name    | TEXT        | e.g., 'vendor_name', 'amount'       |
| field_value   | TEXT        | Extracted value                     |
| confidence    | FLOAT       | Confidence score                    |

### `embeddings`
| Column        | Type        | Description                         |
|---------------|-------------|-------------------------------------|
| id            | UUID        | Primary key                         |
| doc_id        | UUID        | Foreign key to documents            |
| vector        | VECTOR      | PgVector-embedded representation    |
| type          | TEXT        | 'invoice_meta', 'id_identity'       |

---

## Key Features

- **Multimodal OCR**: Handles both printed and handwritten text in various document formats.
- **Auto Classification**: Determines if input is invoice, ID card, or certificate.
- **PgVector Search**: Detects similar documents (e.g. fake IDs, duplicate invoices).
- **Vendor Knowledge Graph (Optional)**: Build a graph of vendors and transaction patterns.
- **Modular Architecture**: Easily plug in new document types or rules.

---

## Example Use Cases
- Fintech platforms automating invoice uploads & verification
- KYC onboarding systems validating national ID or license
- Procurement automation tools preventing invoice fraud
- Academic verification for certificates and diplomas

---

## Coming Soon
- Graph dashboard with Neo4j or Graphistry
- React frontend for upload and results
- PDF highlighting of extracted fields
