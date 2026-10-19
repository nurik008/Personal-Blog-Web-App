# Personal Blog

A small Django application for publishing and managing blog articles. Visitors can browse the article list and read individual posts. Signed-in users can create, edit, and delete articles.

## Features

- Public article list and article detail pages
- Account registration, login, and logout
- Authenticated article management
- SQLite database
- Django admin integration for articles

## Requirements

- Python 3.13
- Django 6.1.2

There is no dependency manifest in the repository yet; Django can be installed directly as shown below.

## Getting started

From the repository root, create and activate a virtual environment, then install Django:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install Django==6.1.2
```

If PowerShell prevents activation, you can run the commands below using the virtual environment's Python executable instead:

```powershell
.\.venv\Scripts\python.exe -m pip install Django==6.1.2
```

Move into the Django project directory and initialize the database:

```powershell
cd PersonalBlog
python manage.py migrate
```

Start the development server:

```powershell
python manage.py runserver
```

Open <http://127.0.0.1:8000/> in your browser. To stop the server, press `Ctrl+C`.

## Using the application

- `/` — browse published articles
- `/article/<id>/` — view an article
- `/register/` — create an account
- `/login/` and `/logout/` — sign in and out
- `/admin_page/` — manage articles when signed in
- `/admin/` — Django's built-in administration site

Registration is open, and every signed-in account can manage articles through `/admin_page/`. Use Django's built-in admin to create a superuser for `/admin/`:

```powershell
python manage.py createsuperuser
```

## Database and migrations

The app uses SQLite, stored in `PersonalBlog/db.sqlite3`. Django migrations create and update the database schema:

```powershell
python manage.py makemigrations
python manage.py migrate
```

## Tests

Run the Django test suite from the `PersonalBlog` directory:

```powershell
python manage.py test
```

## Project structure

```text
PersonalBlog/
├── Blogs/              # Articles, views, forms, URLs, and templates
├── PersonalBlog/       # Django project settings and URL configuration
├── db.sqlite3          # Local SQLite database (created on first migration)
└── manage.py           # Django management commands
```

## Production deployment

The checked-in Django settings are configured for local development. Before deploying, set a private `SECRET_KEY`, disable `DEBUG`, configure `ALLOWED_HOSTS`, and follow Django's deployment checklist for database, static files, HTTPS, and other security settings.
