# PySolve Academy - Deployment Guide

This guide will help you deploy your PySolve Academy application to production.

## Architecture
- **Frontend**: React + Vite + Tailwind CSS
- **Backend**: FastAPI + SQLite
- **Authentication**: JWT + Google OAuth

## Deployment Options

### Option 1: Free Tier Hosting (Recommended for Testing)

#### Frontend - Vercel (Free)
1. Create account at [vercel.com](https://vercel.com)
2. Install Vercel CLI: `npm i -g vercel`
3. From frontend directory: `vercel`
4. Follow the prompts
5. Set environment variables in Vercel dashboard:
   - `VITE_GOOGLE_CLIENT_ID`: Your Google Client ID
   - `VITE_API_URL`: Your deployed backend URL (e.g., `https://your-backend.vercel.app/api`)

#### Backend - Render (Free)
1. Create account at [render.com](https://render.com)
2. Create new "Web Service"
3. Connect your GitHub repository
4. Build command: `pip install -r requirements.txt`
5. Start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
6. Set environment variables:
   - `SECRET_KEY`: Your secret key
   - `DATABASE_URL`: For production, use PostgreSQL (Render provides free PostgreSQL)
   - `GOOGLE_CLIENT_ID`: Your Google Client ID
   - `GOOGLE_CLIENT_SECRET`: Your Google Client Secret

### Option 2: Railway (Both Frontend + Backend)
1. Create account at [railway.app](https://railway.app)
2. Create new project
3. Add PostgreSQL database
4. Add backend service (FastAPI)
5. Add frontend service (React + Vite)
6. Configure environment variables for each service

### Option 3: Single VPS (DigitalOcean, AWS, etc.)
For more control, deploy to a VPS.

## Pre-Deployment Steps

### 1. Update Google OAuth Console
Add your production URLs to Google Cloud Console:
- Authorized JavaScript origins: `https://your-frontend-domain.com`
- Authorized redirect URIs: `https://your-frontend-domain.com`

### 2. Database Migration
For production, switch from SQLite to PostgreSQL:
```bash
# Update requirements.txt
pip install psycopg2-binary

# Update .env
DATABASE_URL=postgresql://user:password@host:port/dbname
```

### 3. Environment Variables
Create production environment files:

**Backend (.env.production):**
```
SECRET_KEY=your-production-secret-key
DATABASE_URL=postgresql://...
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
```

**Frontend (.env.production):**
```
VITE_GOOGLE_CLIENT_ID=your-google-client-id
VITE_API_URL=https://your-backend-domain.com/api
```

## Deployment Commands

### Frontend Build
```bash
cd frontend
npm run build
```

### Backend Production Server
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

## Quick Deploy - Free Option

### Step 1: Deploy Backend to Render
1. Push code to GitHub
2. Go to render.com → New + → Web Service
3. Connect your GitHub repo
4. Settings:
   - Name: pysolve-backend
   - Region: Singapore (or closest to you)
   - Branch: main
   - Runtime: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Add Environment Variables
6. Deploy

### Step 2: Deploy Frontend to Vercel
1. Push code to GitHub
2. Go to vercel.com → New Project
3. Import your GitHub repo
4. Settings:
   - Framework Preset: Vite
   - Root Directory: frontend
5. Add Environment Variables
6. Deploy

### Step 3: Update CORS
Update backend CORS settings to allow your frontend domain:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-frontend-domain.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Post-Deployment Checklist
- [ ] Test authentication (email/password)
- [ ] Test Google Sign-In
- [ ] Test problem solving
- [ ] Test bookmark functionality
- [ ] Check database connectivity
- [ ] Monitor error logs
- [ ] Set up monitoring/alerts

## Troubleshooting

### Common Issues:
1. **CORS errors**: Update allowed origins in backend
2. **Database connection**: Check DATABASE_URL format
3. **Google OAuth errors**: Verify redirect URIs in Google Console
4. **Environment variables**: Ensure all required variables are set

## Security Notes
- Never commit `.env` files to Git
- Use strong SECRET_KEY in production
- Enable HTTPS in production
- Regularly update dependencies
- Set up database backups

## Monitoring
- Use Render's built-in monitoring for backend
- Use Vercel Analytics for frontend
- Consider Sentry for error tracking
