from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import models, schemas, auth, database
from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter(prefix="/api/auth", tags=["auth"])

@router.post("/register", response_model=schemas.UserResponse)
def register(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    try:
        hashed_password = auth.get_password_hash(user.password)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    new_user = models.User(name=user.name, email=user.email, password_hash=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.post("/login", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == form_data.username).first()
    if not user or not auth.verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=schemas.UserResponse)
def get_me(current_user: models.User = Depends(auth.get_current_user)):
    return current_user


class GoogleAuthRequest(BaseModel):
    id_token: str


@router.post("/google/auth")
async def google_auth(request: GoogleAuthRequest, db: Session = Depends(database.get_db)):
    # Verify the Google ID token
    try:
        # Verify token with Google
        response = requests.get(
            f"https://oauth2.googleapis.com/tokeninfo?id_token={request.id_token}"
        )
        
        if response.status_code != 200:
            raise HTTPException(status_code=400, detail="Invalid Google token")
        
        user_info = response.json()
        
        email = user_info.get('email')
        name = user_info.get('name')
        google_id = user_info.get('sub')
        avatar_url = user_info.get('picture')
        
        if not email or not google_id:
            raise HTTPException(status_code=400, detail="Invalid token data")
        
        # Check if user exists by Google ID
        user = db.query(models.User).filter(models.User.google_id == google_id).first()
        
        if not user:
            # Check if user exists by email (merge accounts if email matches)
            user = db.query(models.User).filter(models.User.email == email).first()
            if user:
                # Update existing user with Google info
                user.google_id = google_id
                user.auth_provider = 'google'
                if avatar_url:
                    user.avatar_url = avatar_url
                db.commit()
                db.refresh(user)
            else:
                # Create new user
                new_user = models.User(
                    name=name,
                    email=email,
                    google_id=google_id,
                    auth_provider='google',
                    avatar_url=avatar_url,
                    password_hash=None
                )
                db.add(new_user)
                db.commit()
                db.refresh(new_user)
                user = new_user
        
        # Create JWT token
        access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = auth.create_access_token(
            data={"sub": user.email}, expires_delta=access_token_expires
        )
        
        return {"access_token": access_token, "token_type": "bearer"}
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Google authentication failed: {str(e)}")
