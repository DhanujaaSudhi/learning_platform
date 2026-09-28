from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, database, auth
from typing import List

router = APIRouter(prefix="/api/problems", tags=["problems"])

@router.get("", response_model=List[schemas.ProblemResponse])
@router.get("/", response_model=List[schemas.ProblemResponse])
def get_problems(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    return db.query(models.Problem).offset(skip).limit(limit).all()

@router.get("/{id}", response_model=schemas.ProblemResponse)
def get_problem(id: int, db: Session = Depends(database.get_db)):
    problem = db.query(models.Problem).filter(models.Problem.id == id).first()
    if not problem:
        raise HTTPException(status_code=404, detail="Problem not found")
    return problem

@router.get("/phase/{phase}", response_model=List[schemas.ProblemResponse])
def get_problems_by_phase(phase: int, db: Session = Depends(database.get_db)):
    return db.query(models.Problem).filter(models.Problem.phase == phase).all()
