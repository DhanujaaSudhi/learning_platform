from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String, nullable=True)
    google_id = Column(String, nullable=True, index=True)
    auth_provider = Column(String, default="email")  # 'email' or 'google'
    avatar_url = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    progress = relationship("UserProgress", back_populates="user")
    bookmarks = relationship("Bookmark", back_populates="user")
    submissions = relationship("CodeSubmission", back_populates="user")

class Problem(Base):
    __tablename__ = "problems"
    id = Column(Integer, primary_key=True, index=True)
    phase = Column(Integer)
    category = Column(String)
    title = Column(String)
    difficulty = Column(String)
    description = Column(Text)
    concepts = Column(Text) # JSON string
    python_code = Column(Text)
    example_input = Column(Text)
    example_output = Column(Text)
    explanation = Column(Text) # JSON string
    dry_run = Column(Text) # JSON string
    time_complexity = Column(String)
    space_complexity = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    test_cases = relationship("TestCase", back_populates="problem")

class TestCase(Base):
    __tablename__ = "test_cases"
    id = Column(Integer, primary_key=True, index=True)
    problem_id = Column(Integer, ForeignKey("problems.id"))
    input_data = Column(Text)
    expected_output = Column(Text)
    
    problem = relationship("Problem", back_populates="test_cases")

class UserProgress(Base):
    __tablename__ = "user_progress"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    problem_id = Column(Integer, ForeignKey("problems.id"))
    status = Column(String) # Not Started, In Progress, Completed
    completed_at = Column(DateTime, nullable=True)
    
    user = relationship("User", back_populates="progress")
    problem = relationship("Problem")

class Bookmark(Base):
    __tablename__ = "bookmarks"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    problem_id = Column(Integer, ForeignKey("problems.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="bookmarks")
    problem = relationship("Problem")

class CodeSubmission(Base):
    __tablename__ = "code_submissions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    problem_id = Column(Integer, ForeignKey("problems.id"))
    code = Column(Text)
    input_data = Column(Text)
    output = Column(Text)
    status = Column(String)
    execution_time = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="submissions")
    problem = relationship("Problem")
