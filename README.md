# PySolve Academy 🐍

A full-stack Python Problem-Solving Learning Platform with **505 problems**, a live Python compiler, step-by-step dry runs, and progress tracking.

---

## Project Structure

```
learning platform/
├── backend/                  ← FastAPI Python backend
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── auth.py
│   ├── requirements.txt
│   ├── sql_app.db            ← SQLite database (auto-created)
│   └── routers/
│       ├── auth_router.py
│       ├── problems_router.py
│       ├── compiler_router.py
│       ├── progress_router.py
│       └── bookmark_router.py
└── frontend/                 ← React + TypeScript + Tailwind
    ├── src/
    │   ├── App.tsx
    │   ├── main.tsx
    │   ├── index.css
    │   ├── context/
    │   │   └── AuthContext.tsx
    │   ├── services/
    │   │   └── api.ts
    │   ├── components/
    │   │   ├── Navbar.tsx
    │   │   └── Sidebar.tsx
    │   └── pages/
    │       ├── Landing.tsx
    │       ├── Login.tsx
    │       ├── Register.tsx
    │       ├── Dashboard.tsx
    │       ├── ProblemList.tsx
    │       ├── ProblemDetails.tsx
    │       ├── Compiler.tsx
    │       └── Bookmarks.tsx
    └── package.json
```

---

## Quick Start

### 1. Start the Backend

```powershell
cd "d:\learning platform\backend"
.\venv\Scripts\activate
uvicorn main:app --reload
```

Backend runs at: **http://127.0.0.1:8000**
API Docs: **http://127.0.0.1:8000/docs**

### 2. Start the Frontend

```powershell
cd "d:\learning platform\frontend"
npm run dev
```

Frontend runs at: **http://localhost:5173**

---

## Features

|| Feature | Status |
||---------|--------|
|| Landing page | ✅ |
|| Register / Login | ✅ |
|| JWT Authentication | ✅ |
|| Google Sign-In | ✅ |
|| Dashboard with stats | ✅ |
|| Problem List (505 problems) | ✅ |
|| Problem Details with explanation | ✅ |
|| Dry Run table | ✅ |
|| Monaco Code Editor | ✅ |
|| Live Python Compiler | ✅ |
|| Input/Output panel | ✅ |
|| Progress Tracking | ✅ |
|| Mark problem completed | ✅ |
|| Bookmark problems | ✅ |
|| Search & filter problems | ✅ |
|| Pagination | ✅ |

---

## API Endpoints

|| Method | Endpoint | Description |
||--------|----------|-------------|
|| POST | `/api/auth/register` | Register |
|| POST | `/api/auth/login` | Login (JWT) |
|| POST | `/api/auth/google/auth` | Google Sign-In |
|| GET | `/api/auth/me` | Current user |
|| GET | `/api/problems` | List problems |
|| GET | `/api/problems/{id}` | Problem detail |
|| POST | `/api/code/run` | Execute Python code |
|| GET | `/api/progress` | User progress |
|| PUT | `/api/progress/{id}` | Update status |
|| GET | `/api/bookmarks` | Get bookmarks |
|| POST | `/api/bookmarks/{id}` | Add bookmark |
|| DELETE | `/api/bookmarks/{id}` | Remove bookmark |
|| GET | `/api/bookmarks/check/{id}` | Check bookmarked |

---

## Tech Stack

- **Frontend**: React 18, TypeScript, Tailwind CSS v4, Monaco Editor
- **Backend**: FastAPI, SQLAlchemy, Pydantic v2, JWT Auth
- **Database**: SQLite (dev) — PostgreSQL-ready
- **Authentication**: JWT + Google OAuth

---

## Deployment

See [DEPLOYMENT.md](./DEPLOYMENT.md) for detailed deployment instructions.
