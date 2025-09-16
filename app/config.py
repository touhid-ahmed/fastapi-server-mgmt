import os
from pathlib import Path
from dotenv import load_dotenv

# Load project-root .env (works when running from repo root)
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set. Create .env from .env.example.")
