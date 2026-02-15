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
- ✅ Feature branch merged to main (PR #1 - database models)
- ✅ Virtual environment setup and dependencies installed
- ✅ **DATABASE MODELS COMPLETE**: User, Post, Moderation models fully implemented and merged
- ✅ **PostgreSQL 18 INSTALLED & CONFIGURED**: Server running, database & user created with permissions
- ✅ **DATABASE SETUP COMPLETE**: `modqueue_dev` database and `modqueue_user` created
- ✅ **FLASK APP FACTORY COMPLETE**: config.py, __init__.py, run.py, .env configured
- ✅ **MIGRATIONS COMPLETE**: Initial migration created and applied - all tables exist in PostgreSQL!
- 🔄 **NEXT PHASE**: Build API routes (authentication, posts, moderation endpoints)
- ⏳ Pending: API routes, user authentication (JWT/bcrypt), admin dashboard, React frontend

## Project Structure
```
modqueue/
├── backend/
│   ├── app/
│   │   ├── __init__.py ✅ (Flask app factory with db and migrate)
│   │   ├── models.py ✅ (User, Post, Moderation models)
│   │   ├── config.py ✅ (Database config, environment variables)
│   │   └── routes/ (TODO: API endpoints)
│   ├── migrations/ ✅ (Flask-Migrate folder, initial migration applied)
│   ├── .env ✅ (Environment variables - not in git)
│   ├── run.py ✅ (Flask entry point with load_dotenv)
│   └── requirements.txt (TODO: update with pip freeze)
├── .venv/ (virtual environment at project root)
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
- Current branch: `main` (feature/database-schema merged via PR #1)
- Remote: https://github.com/emunoz02/modqueue.git
- Recent commits:
  - `1c70dde` - Add .claude to gitignore
  - `feecb3b` - Merge pull request #1 (database models)
  - `64b8fb6` - Add database models and reorganize project structure

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

### Flask App Configuration - COMPLETED ✅

**Session 3 Progress (Feb 15, 2026):**
- ✅ Created `backend/app/config.py` with Config class for database settings
- ✅ Updated `backend/app/__init__.py` to use app factory pattern
- ✅ Updated `backend/app/models.py` to import `db` from `__init__.py` (fixed circular dependency)
- ✅ Created `backend/.env` file for environment variables (DATABASE_URL, SECRET_KEY)
- ✅ Updated `backend/run.py` to load environment variables with `python-dotenv`
- ✅ Installed missing packages: `python-dotenv`, `flask-migrate`, `psycopg2-binary`
- ✅ Initialized Flask-Migrate: `python -m flask db init`
- ✅ Created initial migration: `python -m flask db migrate`
- ✅ Applied migration: `python -m flask db upgrade`
- ✅ Verified all 3 tables created in PostgreSQL (`users`, `posts`, `moderations`)
- ✅ Fixed PostgreSQL permissions for `modqueue_user` on `public` schema
- ✅ Updated `.claude/settings.local.json` with broader bash permissions

**Files Created/Modified This Session:**
- `backend/app/config.py` (NEW)
- `backend/app/__init__.py` (UPDATED - app factory)
- `backend/app/models.py` (UPDATED - import db)
- `backend/.env` (NEW - gitignored)
- `backend/run.py` (UPDATED - load_dotenv)
- `backend/migrations/` (NEW - entire folder)
- `.claude/settings.local.json` (UPDATED)

**Key Learnings:**
- **App Factory Pattern**: Create Flask app inside a function (`create_app()`) for flexibility
- **Two-Step Initialization**: Create extensions globally (`db = SQLAlchemy()`), initialize with app later (`db.init_app(app)`)
- **Circular Imports**: Models import `db` from `__init__.py`, `__init__.py` imports models after app creation
- **PostgreSQL Permissions**: Granting privileges on a DATABASE doesn't grant privileges on SCHEMAS - need both
- **Environment Variables**: Use `python-dotenv` to load `.env` file, keep secrets out of code
- **Flask CLI**: Use `python -m flask` instead of just `flask` to avoid PATH issues
- **Migrations**: `flask db init` (once), `flask db migrate` (create), `flask db upgrade` (apply)

### PostgreSQL Installation - COMPLETED ✅

**Installation & Setup:**
- ✅ PostgreSQL 18 installed via official Windows installer
- ✅ Added `C:\Program Files\PostgreSQL\18\bin` to Windows PATH
- ✅ PostgreSQL service (`postgresql-x64-18`) started and running
- ✅ Successfully authenticated with `postgres` user
- ✅ Created database: `modqueue_dev`
- ✅ Created user: `modqueue_user` with password: `pgemunoz`
- ✅ Granted all privileges on `modqueue_dev` to `modqueue_user`
- ✅ Verified connection: `PGPASSWORD='pgemunoz' psql -U modqueue_user -h 127.0.0.1 -d modqueue_dev`

**Database Credentials (for Flask config):**
- Database: `modqueue_dev`
- User: `modqueue_user`
- Password: `pgemunoz`
- Host: `localhost` (or `127.0.0.1`)
- Port: `5432`
- Connection String: `postgresql://modqueue_user:pgemunoz@localhost:5432/modqueue_dev`

**Key Learnings:**
- PostgreSQL runs as a Windows service (`postgresql-x64-18`)
- Need admin privileges to start/stop Windows services (`net start`/`net stop`)
- PATH must include PostgreSQL bin folder for `psql` command to work
- `pg_hba.conf` controls authentication methods (trust/scram-sha-256/md5)
- Connection methods: `local` (Unix sockets), `host` (TCP/IP IPv4/IPv6)
- Set password in environment: `PGPASSWORD='password' psql -U user`

## Next Steps

### 1. Set Up PostgreSQL - COMPLETED ✅
- ✅ Install PostgreSQL locally (PostgreSQL 18 installed)
- ✅ Start PostgreSQL service
- ✅ Connect to PostgreSQL via psql
- ✅ Create database: `modqueue_dev`
- ✅ Create database user: `modqueue_user` with password
- ✅ Grant permissions to `modqueue_user` on `modqueue_dev`
- ✅ Test connection with new user

### 2. Configure Flask App - COMPLETED ✅
- ✅ Create `backend/app/__init__.py` (Flask app factory pattern)
- ✅ Create `backend/app/config.py` (database connection string)
- ✅ Update `backend/run.py` to use app factory
- ✅ Create `.env` file for environment variables
- ✅ Set `DATABASE_URL` in format: `postgresql://modqueue_user:password@localhost:5432/modqueue_dev`
- ✅ `.env` already in `.gitignore`

### 3. Run Database Migrations - COMPLETED ✅
- ✅ Initialize Flask-Migrate: `python -m flask db init`
- ✅ Create migration: `python -m flask db migrate -m "Initial migration"`
- ✅ Apply migration: `python -m flask db upgrade`
- ✅ Verify tables created in PostgreSQL (users, posts, moderations)

### 4. Build API Routes (Future)
- Authentication routes (signup, login)
- Post routes (create, read, update, delete)
- Admin routes (approve/reject posts, manage users)

### 5. Build React Frontend (Future)
### 6. Dockerize Application (Future)
### 7. Deploy (Future)
