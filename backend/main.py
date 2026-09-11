from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse

from backend import models  # noqa: F401 — register tables with Base
from backend.database import Base, init_engine
from backend.routes.user import router as user_router

STATIC_DIR = Path(__file__).resolve().parent / "static"

engine = init_engine()
if engine is not None:
    Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_router)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/")
def read_root():
    return FileResponse(STATIC_DIR / "index.html")

