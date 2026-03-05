# Student Management System

A small Django-based Student Management System for tracking and marking attendance.

## Requirements
- Python 3.11+ (use a virtual environment)
- See `requirements.txt` for Python package versions (Django 6.0.1, etc.)

## Quick setup

1. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies

```powershell
pip install -r requirements.txt
```

3. Apply migrations (the repository includes a default SQLite at `student_data/db.sqlite3`)

```powershell
# from the repository root
python student_data/manage.py migrate
```

4. (Optional) Create a superuser

```powershell
python student_data/manage.py createsuperuser
```

5. Run the development server

```powershell
python student_data/manage.py runserver
```

Then open http://127.0.0.1:8000/ in your browser.

## Tests

Run the Django test suite:

```powershell
python student_data/manage.py test
```

## Project structure (high level)

- `student_data/` — Django project root
	- `settings.py`, `urls.py`, `wsgi.py`, `asgi.py`
- `records/` — main app for student/attendance features
	- `models.py`, `views.py`, `urls.py`, `templates/` (contains `mark_attendance.html`, `view_attendance.html`)
- `db.sqlite3` — development database (included)

## Notes
- The project is configured for local development using SQLite. The `requirements.txt` includes `psycopg2` for Postgres if you choose to switch databases.
- If you use PowerShell and encounter execution policy issues when activating the venv, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

## Next steps
- Run the server and verify the attendance UI at the app routes.
- Ask me to add a `Makefile` or PowerShell script for one-command setup if you'd like.

