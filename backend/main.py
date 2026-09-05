from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse

from backend import models  # noqa: F401 — register tables with Base
from backend.database import Base, engine
from backend.routes.user import router as user_router

STATIC_DIR = Path(__file__).resolve().parent / "static"

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_router)


@app.get("/")
def read_root():
    return FileResponse(STATIC_DIR / "index.html")
