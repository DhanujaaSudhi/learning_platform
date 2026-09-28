from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import models
from database import engine
from routers import auth_router, problems_router, compiler_router, progress_router, bookmark_router
from seed_problems import seed_problems
import os
from dotenv import load_dotenv

load_dotenv()

models.Base.metadata.create_all(bind=engine)

# Only seed problems in development or if explicitly requested
if os.getenv("SEED_PROBLEMS", "true").lower() == "true":
    seed_problems()

app = FastAPI(title="PySolve Academy API")

# Get allowed origins from environment variable or default to localhost
allowed_origins = [
    origin.strip()
    for origin in os.getenv(
        "ALLOWED_ORIGINS",
        "http://localhost:5173,http://127.0.0.1:5173",
    ).split(",")
    if origin.strip()
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router.router)
app.include_router(problems_router.router)
app.include_router(compiler_router.router)
app.include_router(progress_router.router)
app.include_router(bookmark_router.router)

FRONTEND_DIST = Path(os.getenv("FRONTEND_DIST", Path(__file__).resolve().parent / "frontend_dist"))


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/")
def read_root():
    index_file = FRONTEND_DIST / "index.html"
    if index_file.exists():
        return FileResponse(index_file)
    return {"message": "Welcome to PySolve Academy API"}


if FRONTEND_DIST.exists():
    assets_dir = FRONTEND_DIST / "assets"
    if assets_dir.exists():
        app.mount("/assets", StaticFiles(directory=assets_dir), name="assets")

    @app.get("/{full_path:path}")
    def serve_spa(full_path: str):
        if full_path.startswith("api/") or full_path == "api":
            from fastapi import HTTPException
            raise HTTPException(status_code=404, detail="API endpoint not found")
        candidate = FRONTEND_DIST / full_path
        if candidate.is_file():
            return FileResponse(candidate)
        return FileResponse(FRONTEND_DIST / "index.html")

