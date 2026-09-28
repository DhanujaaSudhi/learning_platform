from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, database, auth
from datetime import datetime

router = APIRouter(prefix="/api/progress", tags=["progress"])

@router.get("/")
def get_progress(db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    progress = db.query(models.UserProgress).filter(models.UserProgress.user_id == current_user.id).all()
    return progress

@router.put("/{problem_id}")
def update_progress(problem_id: int, status: str, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    progress = db.query(models.UserProgress).filter(
        models.UserProgress.user_id == current_user.id,
        models.UserProgress.problem_id == problem_id
    ).first()
    
    if progress:
        progress.status = status
        if status == "Completed":
            progress.completed_at = datetime.utcnow()
    else:
        progress = models.UserProgress(
            user_id=current_user.id,
            problem_id=problem_id,
            status=status,
            completed_at=datetime.utcnow() if status == "Completed" else None
        )
        db.add(progress)
    db.commit()
    return {"message": "Progress updated"}
