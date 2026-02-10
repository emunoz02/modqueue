# ModQueue - Content Moderation Platform

## Project Overview
A full-stack content moderation platform where users can submit posts and admins can approve/reject content, manage users, and view analytics.

**Goal**: Build a portfolio-worthy project demonstrating full-stack skills, Docker, Git, and real-world features that companies care about.

## Tech Stack
- **Backend**: Flask (Python)
- **Frontend**: React
- **Database**: PostgreSQL
- **Containerization**: Docker
- **Version Control**: Git

## Learning Approach
- Student writes all code first
- Claude guides with questions and explanations
- Focus on understanding, not just working code
- Debug together without complete solutions

## Current Status
- ✅ Git repository initialized & pushed to GitHub (https://github.com/emunoz02/modqueue.git)
- ✅ Folder structure reorganized (backend/frontend separation)
- ✅ Feature branch created: `feature/database-schema`
- ✅ Virtual environment setup and dependencies installed
- ✅ **DATABASE MODELS COMPLETE**: User, Post, Moderation models fully implemented
- 🔄 **NEXT**: Commit models → Set up PostgreSQL → Configure Flask app → Run migrations
- ⏳ Pending: PostgreSQL setup, Flask app factory, API routes, user authentication, admin dashboard

## Project Structure
```
modqueue/
├── backend/
│   ├── app/
│   │   ├── __init__.py (TODO: Flask app factory)
│   │   ├── models.py ✅ (User, Post, Moderation models complete)
│   │   ├── config.py (TODO: Database config)
│   │   └── routes/ (TODO: API endpoints)
│   ├── .venv/ (virtual environment - activated)
│   ├── run.py (Flask entry point - needs update)
│   └── requirements.txt (TODO: generate with pip freeze)
├── .git/
├── .gitignore
└── CLAUDE.md
```

## Architecture Decisions

### Tech Stack Choices
- **Database**: PostgreSQL (production-ready, not SQLite)
- **ORM**: SQLAlchemy (Flask-SQLAlchemy)
- **Password Security**: bcrypt hashing
- **File Uploads**: Phase 2 (text-only posts for MVP)
- **Folder Structure**: Separate backend/frontend (monorepo style)

### Database Schema (Approved)

**Users Table:**
- id (PK)
- username (VARCHAR)
- email (VARCHAR, unique)
- password_hash (VARCHAR)
- first_name (VARCHAR)
- last_name (VARCHAR)
- is_admin (BOOLEAN) - admin vs regular user
- is_banned (BOOLEAN) - posting privileges
- created_at (TIMESTAMP)

**Posts Table:**
- id (PK)
- user_id (FK → Users)
- title (VARCHAR)
- content (TEXT)
- status (VARCHAR: pending/approved/rejected)
- created_at (TIMESTAMP)
- updated_at (TIMESTAMP)

**Moderation Table:**
- id (PK)
- post_id (FK → Posts)
- moderator_id (FK → Users)
- action (VARCHAR: approved/rejected)
- reason (TEXT, optional)
- moderated_at (TIMESTAMP)

## Key Files
- `backend/run.py` - Flask application entry point
- `backend/app/models.py` - Database models (SQLAlchemy)
- `CLAUDE.md` - Project context & progress tracker

## Git Workflow
- Main branch: `main` (stable)
- Current branch: `feature/database-schema`
- Remote: https://github.com/emunoz02/modqueue.git

## Token Usage Strategy
- Start fresh conversations for distinct features/phases
- Current conversation: Project setup & planning
- **Start new session when**: Token usage hits ~50%, or when switching to a major new feature (e.g., frontend build, Docker setup)
- This document persists across sessions - update it as you build!

## Implementation Notes

### Database Models - COMPLETED ✅
All three models implemented in `backend/app/models.py`:

1. **User Model** (`users` table)
   - Authentication ready (password_hash field)
   - Admin/user role system (is_admin boolean)
   - Ban system (is_banned boolean)
   - Uses `server_default=db.func.now()` for timestamps (not deprecated `utcnow`)

2. **Post Model** (`posts` table)
   - Foreign key to User (author)
   - Status tracking (pending/approved/rejected)
   - Auto-updating `updated_at` with `onupdate=db.func.now()`

3. **Moderation Model** (`moderations` table)
   - Two foreign keys: post_id and moderator_id
   - Action tracking (approved/rejected)
   - Optional reason field (nullable=True)

### Key Learnings This Session
- Virtual environments prevent package conflicts between projects
- `nullable=True` is default, but being explicit improves code clarity
- `server_default=db.func.now()` is modern replacement for deprecated `datetime.utcnow()`
- Foreign keys need both column type AND `db.ForeignKey()`: `db.Column(db.Integer, db.ForeignKey('table.id'))`
- `onupdate=db.func.now()` auto-updates timestamp on record modification

### Dependencies Installed (in .venv)
- flask-sqlalchemy
- flask-migrate
- psycopg2-binary

## Next Steps

### 1. Set Up PostgreSQL (Next Session)
- Install PostgreSQL locally
- Create database: `modqueue_dev`
- Create database user with password
- Test connection

### 2. Configure Flask App (Next Session)
- Create `backend/app/__init__.py` (Flask app factory pattern)
- Create `backend/app/config.py` (database connection string)
- Update `backend/run.py` to use app factory
- Set environment variables (.env file for DATABASE_URL)

### 3. Run Database Migrations
- Initialize Flask-Migrate: `flask db init`
- Create migration: `flask db migrate -m "Initial migration"`
- Apply migration: `flask db upgrade`
- Verify tables created in PostgreSQL

### 4. Build API Routes (Future)
- Authentication routes (signup, login)
- Post routes (create, read, update, delete)
- Admin routes (approve/reject posts, manage users)

### 5. Build React Frontend (Future)
### 6. Dockerize Application (Future)
### 7. Deploy (Future)
