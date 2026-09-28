from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class GoogleUserCreate(BaseModel):
    name: str
    email: str
    google_id: str
    avatar_url: Optional[str] = None

class UserResponse(BaseModel):
    id: int
    name: Optional[str] = "User"
    email: str
    auth_provider: Optional[str] = "email"
    avatar_url: Optional[str] = None
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

class ProblemBase(BaseModel):
    title: str
    difficulty: str
    phase: int
    category: str

class ProblemResponse(ProblemBase):
    id: int
    description: str
    concepts: str
    python_code: str
    example_input: str
    example_output: str
    explanation: str
    dry_run: Optional[str]
    time_complexity: str
    space_complexity: str
    class Config:
        from_attributes = True

class CodeRunRequest(BaseModel):
    code: str
    input_data: Optional[str] = ""

class CodeRunResponse(BaseModel):
    output: str
    error: Optional[str]
    execution_time: float
