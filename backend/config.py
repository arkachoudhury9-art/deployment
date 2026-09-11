import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


def get_database_url() -> str | None:
    url = os.getenv("SQLALCHEMY_DATABASE_URL")
    if url and url.startswith("sqlite:///"):
        db_path = Path(url.removeprefix("sqlite:///"))
        if not db_path.is_absolute():
            url = f"sqlite:///{(Path(__file__).resolve().parent / db_path.name).resolve()}"
    return url
