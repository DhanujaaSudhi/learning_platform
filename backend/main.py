from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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
allowed_origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:5173,http://127.0.0.1:5173").split(",")

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

@app.get("/")
def read_root():
    return {"message": "Welcome to PySolve Academy API"}
