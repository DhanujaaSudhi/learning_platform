from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models, database, auth

router = APIRouter(prefix="/api/bookmarks", tags=["bookmarks"])


@router.get("/")
def get_bookmarks(
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user),
):
    bookmarks = (
        db.query(models.Bookmark)
        .filter(models.Bookmark.user_id == current_user.id)
        .order_by(models.Bookmark.created_at.desc())
        .all()
    )
    result = []
    for b in bookmarks:
        problem = db.query(models.Problem).filter(models.Problem.id == b.problem_id).first()
        result.append({
            "id": b.id,
            "problem_id": b.problem_id,
            "problem_title": problem.title if problem else "Unknown",
            "problem_difficulty": problem.difficulty if problem else "Unknown",
            "problem_phase": problem.phase if problem else 0,
            "created_at": b.created_at,
        })
    return result


@router.post("/{problem_id}")
def add_bookmark(
    problem_id: int,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user),
):
    existing = (
        db.query(models.Bookmark)
        .filter(
            models.Bookmark.user_id == current_user.id,
            models.Bookmark.problem_id == problem_id,
        )
        .first()
    )
    if existing:
        raise HTTPException(status_code=400, detail="Already bookmarked")

    problem = db.query(models.Problem).filter(models.Problem.id == problem_id).first()
    if not problem:
        raise HTTPException(status_code=404, detail="Problem not found")

    bookmark = models.Bookmark(user_id=current_user.id, problem_id=problem_id)
    db.add(bookmark)
    db.commit()
    return {"message": "Bookmarked successfully"}


@router.delete("/{problem_id}")
def remove_bookmark(
    problem_id: int,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user),
):
    bookmark = (
        db.query(models.Bookmark)
        .filter(
            models.Bookmark.user_id == current_user.id,
            models.Bookmark.problem_id == problem_id,
        )
        .first()
    )
    if not bookmark:
        raise HTTPException(status_code=404, detail="Bookmark not found")

    db.delete(bookmark)
    db.commit()
    return {"message": "Bookmark removed"}


@router.get("/check/{problem_id}")
def check_bookmark(
    problem_id: int,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user),
):
    bookmark = (
        db.query(models.Bookmark)
        .filter(
            models.Bookmark.user_id == current_user.id,
            models.Bookmark.problem_id == problem_id,
        )
        .first()
    )
    return {"bookmarked": bookmark is not None}
