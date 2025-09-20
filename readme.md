
# Project67: FastAPI + React

Fullstack app with FastAPI backend and React frontend. Supports user registration/login with PostgreSQL.

## Quick Start

### Backend
1. `cd backend && python3 -m venv venv && source venv/bin/activate`
2. `pip install -r requirements.txt -r db_requirements.txt python-dotenv`
3. Set up PostgreSQL and `.env`
4. `uvicorn main:app --reload`

### Frontend
1. `cd frontend && npm install`
2. `cp .env.example .env && npm run dev`

Open http://localhost:5173 (frontend) and http://localhost:8000 (backend).

## Structure
- `backend/app/` — FastAPI code
- `frontend/src/` — React code

## License
MIT
