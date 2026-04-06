# CheckInly

CheckInly is a Django-based student management system for keeping a simple student roster and marking daily attendance.

## Features

- Add and manage students through Django admin.
- Mark attendance for all students for the current day.
- View attendance history for an individual student.
- Prevent duplicate attendance entries for the same student on the same date.

## Requirements

- Python 3.11+
- A virtual environment is recommended
- See `requirements.txt` for the exact package versions, including Django 6.0.1, Daphne, `python-dotenv`, and PostgreSQL drivers

## Database setup

The current Django settings use PostgreSQL and read credentials from environment variables loaded with `python-dotenv`.

Create a `.env` file in the repository root with values like:

```env
your_database=checkinly
your_username=postgres
your_pass=your_password
```

If you want to use a different database backend, update `student_data/student_data/settings.py` accordingly.

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

3. Run migrations

```powershell
python student_data/manage.py migrate
```

4. Create a superuser for the admin site

```powershell
python student_data/manage.py createsuperuser
```

5. Start the development server

```powershell
python student_data/manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

## App routes

- `/` - view attendance page
- `/mark/` - mark attendance page
- `/admin/` - Django admin

## Project structure

- `student_data/manage.py` - Django management entry point
- `student_data/student_data/` - project settings, URL configuration, ASGI and WSGI modules
- `student_data/records/` - main app for students and attendance
- `student_data/records/models.py` - `Student` and `Attendance` models
- `student_data/records/views.py` - attendance views
- `student_data/records/templates/` - `mark_attendance.html` and `view_attendance.html`

## Tests

Run the Django test suite with:

```powershell
python student_data/manage.py test
```

## Notes

- The project uses the `records` app for the attendance workflow.
- If PowerShell blocks script execution when activating the virtual environment, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

