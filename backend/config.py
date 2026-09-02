import os
from pathlib import Path

from dotenv import load_dotenv

BACKEND_DIR = Path(__file__).resolve().parent
load_dotenv(BACKEND_DIR / ".env")

SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")

if SQLALCHEMY_DATABASE_URL and SQLALCHEMY_DATABASE_URL.startswith("sqlite:///"):
    db_path = Path(SQLALCHEMY_DATABASE_URL.removeprefix("sqlite:///"))
    if not db_path.is_absolute():
        SQLALCHEMY_DATABASE_URL = f"sqlite:///{(BACKEND_DIR / db_path.name).resolve()}"
