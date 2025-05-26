invoice-api/
│
├── app/                            # Main application logic
│   ├── api/                        # FastAPI routes
│   │   ├── __init__.py
│   │   └── upload.py               # /upload endpoint
│   │
│   ├── core/                       # Core configs & setup
│   │   ├── __init__.py
│   │   ├── config.py               # Secrets/env setup
│   │   └── supabase_client.py      # Supabase connection init
│   │
│   ├── ocr/                        # OCR model logic
│   │   ├── __init__.py
│   │   ├── processor.py            # TrOCR or Donut runner
│   │   └── preprocessor.py         # (optional) image preprocess
│   │
│   ├── logic/                      # Business logic
│   │   ├── __init__.py
│   │   ├── extractor.py            # Rule-based field extractor
│   │   ├── vectorizer.py           # SentenceTransformer embedder
│   │   ├── storage.py              # Upload to Supabase bucket
│   │   └── db_writer.py            # Insert metadata, vectors, fields
│   │
│   ├── graph/                      # Optional: Neo4j graph handler
│   │   ├── __init__.py
│   │   └── vendor_graph.py
│   │
│   └── main.py                     # FastAPI app entry point
│
├── scripts/                        # Testing or batch scripts
│   └── test_upload.py              # Manual test for API
│
├── requirements.txt                # All dependencies
├── .env                            # Secrets, API keys
├── README.md
└── run.sh                          # (optional) start server script

File/Folder	Purpose
main.py	Runs FastAPI app, includes routes
upload.py	Defines /upload route and processing steps
config.py	Loads environment variables / API keys securely
supabase_client.py	Initializes Supabase client
processor.py	OCR using Donut, TrOCR, etc
extractor.py	Extracts structured fields from raw text (e.g., invoice ID, name, etc)
vectorizer.py	Embeds text using SentenceTransformer
storage.py	Uploads original files to Supabase Storage
db_writer.py	Inserts processed data and embeddings into Supabase Postgres
vendor_graph.py	(Optional) Interacts with Neo4j graph for linking vendors