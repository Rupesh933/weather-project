# Weather Project

A beginner-friendly Django web application for checking current weather by city name.

### Project Name

**Weather Project**

### What This Project Does

This project is a simple weather checker website. A user enters a city name, submits the form, and the application shows current weather information for that city.

The displayed weather data includes:

- City and country
- Temperature in Celsius
- Feels-like temperature
- Weather description
- Weather icon
- Humidity
- Wind speed
- Atmospheric pressure

### Why This Project Exists

This project exists as a practical Django learning project. It demonstrates how to:

- Build a basic Django app
- Create a view and URL route
- Render HTML templates
- Serve static CSS files
- Read environment variables
- Call an external API
- Display API data in a browser
- Use Django's built-in admin and authentication system

### Main Purpose / Use Case

The main use case is quick current-weather lookup by city name.

Example:

1. Open the website.
2. Type `Delhi`.
3. Click **Get Weather**.
4. See the current weather returned from OpenWeatherMap.

### Who This Project Is For

This project is useful for:

- Beginner Django developers
- Students learning Django project structure
- Developers practicing API integration
- Future maintainers returning to this project after a long break

## Tech Stack

### Programming Language

- **Python 3**
  - The local environment used during analysis was Python `3.13.12`.
  - Because this project uses Django `6.0.4`, use a modern Python version that supports Django 6.

### Backend Framework

- **Django 6.0.4**

### Database

- **SQLite**
  - Configured in `weather_project/weather_project/settings.py`
  - Database file: `weather_project/db.sqlite3`
  - The file is ignored by Git through `.gitignore`.

### Frontend Technologies

- HTML
- CSS
- Django Template Language
- Font Awesome CDN for icons/styles support

### APIs Used

- **OpenWeatherMap Current Weather API**
  - Endpoint used internally by the app:

```text
https://api.openweathermap.org/data/2.5/weather
```

### Third-Party Packages / Libraries

From `requirements.txt`:

```text
Django==6.0.5
python-decouple==3.8
requests==2.31.0
python-dotenv>=1.0.0
```

Package purpose:

- `Django`: Web framework used to build the application.
- `python-decouple`: Reads configuration values from environment variables or `.env`.
- `requests`: Sends HTTP requests to OpenWeatherMap.
- `python-dotenv`: Helps load environment variables from `.env` files. This package is listed, although the current settings file uses `python-decouple`.

## Features

### User Features

- Search current weather by city name.
- View temperature in Celsius.
- View feels-like temperature.
- View weather description.
- View weather icon from OpenWeatherMap.
- View humidity percentage.
- View wind speed.
- View atmospheric pressure.
- See a friendly message when no city has been searched yet.
- See an error message when:
  - The city field is empty.
  - The city cannot be found.
  - The weather API request fails.

### Admin Features

This project currently uses Django's built-in admin site.

Admin route:

```text
/admin/
```

There are currently no custom models registered in `weather_app/admin.py`, so the admin is mainly useful for Django's built-in authentication models such as users and groups.

## Project Structure

Current repository structure:

```text
Weather_project/
├── .env
├── .gitignore
├── README.md
├── requirements.txt
└── weather_project/
    ├── manage.py
    ├── weather_app/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations/
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── static/
    │   │   └── weather_app/
    │   │       └── style.css
    │   ├── templates/
    │   │   └── weather_app/
    │   │       └── index.html
    │   ├── tests.py
    │   ├── urls.py
    │   ├── utils.py
    │   └── views.py
    └── weather_project/
        ├── __init__.py
        ├── asgi.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
```

### Important Files and Folders

| Path | Purpose |
| --- | --- |
| `README.md` | Project documentation. You are reading it now. |
| `requirements.txt` | Python dependencies required to run the project. |
| `.env` | Local environment variables such as secret keys and API keys. This file should not be committed. |
| `.gitignore` | Tells Git which files to ignore, such as `.env`, `db.sqlite3`, and Python cache files. |
| `weather_project/manage.py` | Django command-line entry point. Use it to run the server, migrations, tests, and admin commands. |
| `weather_project/weather_project/settings.py` | Main Django configuration file. Contains installed apps, database settings, static files, API key loading, and security settings. |
| `weather_project/weather_project/urls.py` | Main project URL configuration. It sends `/admin/` to Django admin and `/` to `weather_app`. |
| `weather_project/weather_project/asgi.py` | ASGI application entry point for async-capable deployment servers. |
| `weather_project/weather_project/wsgi.py` | WSGI application entry point for traditional deployment servers. |
| `weather_project/weather_app/` | Main Django application folder. |
| `weather_project/weather_app/views.py` | Contains the main page logic. Handles form submission and prepares weather data for the template. |
| `weather_project/weather_app/utils.py` | Contains helper logic for calling the OpenWeatherMap API. |
| `weather_project/weather_app/urls.py` | URL routes for the weather app. Currently maps `/` to the `index` view. |
| `weather_project/weather_app/models.py` | Place for database models. Currently no custom models exist. |
| `weather_project/weather_app/admin.py` | Place to register custom models for Django admin. Currently no custom models are registered. |
| `weather_project/weather_app/templates/weather_app/index.html` | Main HTML page shown to users. |
| `weather_project/weather_app/static/weather_app/style.css` | CSS styling for the weather page. |
| `weather_project/weather_app/migrations/` | Database migration files for the app. Currently only contains `__init__.py` because there are no custom models yet. |
| `weather_project/weather_app/tests.py` | Place for automated tests. Currently empty except for Django's starter import. |

## Installation Guide

Follow these steps from a fresh machine or after cloning the project again later.

### 1. Prerequisites

Install these first:

- Python 3.12 or newer recommended
- `pip`
- Git
- An OpenWeatherMap API key

You can get an API key from:

```text
https://openweathermap.org/api
```

### 2. Clone the Repository

```bash
git clone <your-repository-url>
cd Weather_project
```

Replace `<your-repository-url>` with the real Git repository URL.

### 3. Create a Virtual Environment

From the repository root:

```bash
python -m venv venv
```

Activate it:

On macOS/Linux:

```bash
source venv/bin/activate
```

On Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

On Windows Command Prompt:

```bat
venv\Scripts\activate.bat
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Create the `.env` File

Create a file named `.env` in the repository root:

```text
Weather_project/.env
```

Recommended `.env` example:

```env
SECRET_KEY="replace-this-with-a-new-django-secret-key"
DEBUG=True
OPENWEATHER_API_KEY="replace-this-with-your-openweathermap-api-key"
```

Generate a new Django secret key:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Important:

- Do not commit `.env`.
- Do not share real API keys publicly.
- The current `settings.py` reads `SECRET_KEY`, not `DJANGO_SECRET_KEY`.

### 6. Move Into the Django Project Folder

The `manage.py` file is inside the inner `weather_project` folder:

```bash
cd weather_project
```

### 7. Run Database Migrations

```bash
python manage.py migrate
```

This creates the SQLite database and Django's built-in tables for users, groups, sessions, and admin support.

### 8. Create a Superuser

This is optional for using the weather page, but required for admin access:

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin username, email, and password.

### 9. Run the Development Server

```bash
python manage.py runserver
```

Open the app in your browser:

```text
http://127.0.0.1:8000/
```

Open Django admin:

```text
http://127.0.0.1:8000/admin/
```

## Configuration

Configuration is mainly handled in:

```text
weather_project/weather_project/settings.py
```

### Environment Variables

The project uses `python-decouple`:

```python
from decouple import config
```

Environment variables are read with:

```python
config("VARIABLE_NAME", default=...)
```

### Required / Recommended Variables

| Variable | Required? | Purpose | Example |
| --- | --- | --- | --- |
| `SECRET_KEY` | Recommended | Django cryptographic signing key. Required for secure production use. | `SECRET_KEY="your-secret-key"` |
| `DEBUG` | Recommended | Enables or disables Django debug mode. | `DEBUG=True` |
| `OPENWEATHER_API_KEY` | Required for weather search | API key used to call OpenWeatherMap. | `OPENWEATHER_API_KEY="abc123"` |

### Secret Key Notes

In `settings.py`, the project currently uses:

```python
SECRET_KEY = config('SECRET_KEY', default='...')
```

That means the `.env` file should use:

```env
SECRET_KEY="your-secret-key"
```

If the `.env` file uses `DJANGO_SECRET_KEY` instead, Django will not read it with the current code.

### Debug Settings

Current setting:

```python
DEBUG = config('DEBUG', default=True, cast=bool)
```

For local development:

```env
DEBUG=True
```

For production:

```env
DEBUG=False
```

Never run production with `DEBUG=True`, because error pages may expose sensitive information.

### Allowed Hosts

Current setting:

```python
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '*']
```

This allows all hosts because of `'*'`.

For production, replace it with the real domain:

```python
ALLOWED_HOSTS = ['your-domain.com', 'www.your-domain.com']
```

### Database Configuration

Current database:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

This is good for local development and small learning projects.

For production, consider PostgreSQL or another production-grade database.

### Static Files

Current setting:

```python
STATIC_URL = "static/"
```

Static CSS file:

```text
weather_project/weather_app/static/weather_app/style.css
```

The template loads it with:

```django
{% load static %}
<link rel="stylesheet" href="{% static 'weather_app/style.css' %}">
```

### Media Files

This project currently does not define `MEDIA_URL` or `MEDIA_ROOT`, and it does not upload user media files.

## Usage Instructions

### Use the Weather Page

1. Start the development server:

```bash
cd weather_project
python manage.py runserver
```

2. Open:

```text
http://127.0.0.1:8000/
```

3. Type a city name in the input box.

Examples:

```text
Delhi
Noida
London
New York
Tokyo
```

4. Click **Get Weather**.

5. Review the weather card.

### Expected Result

For a valid city, the page shows:

- City and country
- Weather icon
- Temperature
- Feels-like temperature
- Weather description
- Humidity
- Wind speed
- Pressure

### Invalid City Behavior

If the city is invalid or OpenWeatherMap does not return a successful response, the app shows:

```text
Could not find weather city '<city>', Check city name and try again!
```

### Missing City Behavior

If no city is submitted, the app shows:

```text
Please enter a city name
```

## Authentication

### Does the Weather Page Require Login?

No. The main weather search page is public.

Users do not need to create an account or log in to search for weather.

### Django Admin Authentication

Django admin is enabled at:

```text
/admin/
```

Admin users must log in with a superuser account.

Create a superuser:

```bash
cd weather_project
python manage.py createsuperuser
```

### User Roles and Permissions

This project currently uses Django's built-in roles:

- **Anonymous user**: Can access the weather search page.
- **Admin / superuser**: Can log into `/admin/`.

There are no custom user roles or custom permissions in the current codebase.

## API Documentation

This project does not expose a JSON REST API for other applications.

It has a normal Django HTML route and uses OpenWeatherMap as an external API behind the scenes.

### Internal Web Routes

| Route | Method | Purpose | View |
| --- | --- | --- | --- |
| `/` | `GET` | Show the weather search page. | `weather_app.views.index` |
| `/` | `POST` | Submit a city name and display weather data. | `weather_app.views.index` |
| `/admin/` | `GET/POST` | Django admin login and admin pages. | Django admin |

### Route: `/`

#### GET `/`

Purpose:

Shows the search form.

Request body:

None.

Response:

HTML page rendered from:

```text
weather_project/weather_app/templates/weather_app/index.html
```

#### POST `/`

Purpose:

Accepts a city name, calls OpenWeatherMap, and renders weather data.

Form body:

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `city` | string | Yes | City name to search. |

Example form body:

```text
city=Delhi
```

Response:

HTML page with either:

- A weather card, or
- An error message

The view passes this context to the template:

```python
{
    "weather": {
        "city": "Delhi",
        "country": "IN",
        "tempreature": 30.0,
        "feel_like": 31.0,
        "humidity": 40,
        "pressure": 1012,
        "wind_speed": 3.5,
        "description": "Clear sky",
        "icon": "01d",
    },
    "error": None,
}
```

Note:

The context key is currently spelled `tempreature` in the Python code and template. This works because both files use the same spelling, but it should be renamed carefully if cleaned up later.

### External API: OpenWeatherMap

The helper function `get_weather(city_name)` calls:

```text
GET https://api.openweathermap.org/data/2.5/weather
```

Query parameters:

| Parameter | Purpose |
| --- | --- |
| `q` | City name |
| `appid` | OpenWeatherMap API key |
| `units` | Unit system. Current value is `metric`, so temperature is Celsius. |

Example external request:

```text
https://api.openweathermap.org/data/2.5/weather?q=Delhi&appid=<api-key>&units=metric
```

Simplified sample external response:

```json
{
  "name": "Delhi",
  "sys": {
    "country": "IN"
  },
  "main": {
    "temp": 30.0,
    "feels_like": 31.0,
    "humidity": 40,
    "pressure": 1012
  },
  "wind": {
    "speed": 3.5
  },
  "weather": [
    {
      "description": "clear sky",
      "icon": "01d"
    }
  ]
}
```

## Database Explanation

### Current Database

The project uses SQLite:

```text
weather_project/db.sqlite3
```

This file is created after running:

```bash
python manage.py migrate
```

### Custom Models

There are currently no custom database models.

`weather_project/weather_app/models.py` contains only:

```python
from django.db import models

# Create your models here.
```

### Built-In Django Tables

Even without custom models, Django creates tables for built-in apps, including:

- Users
- Groups
- Permissions
- Sessions
- Admin log entries

These come from installed apps such as:

```python
django.contrib.admin
django.contrib.auth
django.contrib.contenttypes
django.contrib.sessions
```

### Relationships

There are no custom app relationships yet.

Django's built-in authentication system includes relationships such as:

- Users can belong to groups.
- Users and groups can have permissions.
- Admin log entries relate to users.

### Schema Overview

Current schema is basically:

```text
Django built-in auth/admin/session tables
No weather_app custom tables yet
```

Weather search results are not saved to the database. Each search calls OpenWeatherMap live.

## Code Explanation

### Main Request Flow

The main flow is:

```text
Browser
  -> GET or POST /
  -> weather_project/urls.py
  -> weather_app/urls.py
  -> weather_app.views.index
  -> weather_app.utils.get_weather
  -> OpenWeatherMap API
  -> render index.html
```

### URL Routing

Main project URLs are in:

```text
weather_project/weather_project/urls.py
```

Important routes:

```python
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('weather_app.urls')),
]
```

This means:

- `/admin/` opens Django admin.
- `/` is handled by `weather_app`.

App URLs are in:

```text
weather_project/weather_app/urls.py
```

Current app route:

```python
urlpatterns = [
    path('', views.index, name='weather_index')
]
```

### Main View: `index`

File:

```text
weather_project/weather_app/views.py
```

The `index` view:

1. Starts with empty `weather_data` and `error_message`.
2. Checks if the request method is `POST`.
3. Reads the city from the submitted form.
4. Calls `get_weather(city)`.
5. If data is returned, extracts only the fields needed by the template.
6. If data is missing, prepares an error message.
7. Renders `weather_app/index.html`.

Important code idea:

```python
data = get_weather(city)
```

The view does not directly call the external API. It delegates that work to `utils.py`, which keeps the view simpler.

### Weather API Helper: `get_weather`

File:

```text
weather_project/weather_app/utils.py
```

Purpose:

Fetch current weather data from OpenWeatherMap.

Important behavior:

- Reads `OPENWEATHER_API_KEY` from Django settings.
- Raises `ValueError` if the API key is missing.
- Sends a GET request using `requests.get`.
- Uses a timeout of 10 seconds.
- Returns parsed JSON only when OpenWeatherMap returns status code `200`.
- Returns `None` for failed requests or network errors.

Implementation decision:

The external API call is separated into `utils.py` instead of being written directly inside the view. This makes the code easier to test and maintain.

### Template

File:

```text
weather_project/weather_app/templates/weather_app/index.html
```

Purpose:

- Shows the page title.
- Loads static CSS.
- Shows the city search form.
- Displays errors.
- Displays weather data when available.

Important Django template features used:

```django
{% load static %}
{% csrf_token %}
{% if error %}
{% if weather %}
{{ weather.city }}
```

`{% csrf_token %}` is important because Django protects POST forms from cross-site request forgery attacks.

### Static CSS

File:

```text
weather_project/weather_app/static/weather_app/style.css
```

Purpose:

Styles the weather page with:

- Gradient background
- Centered container
- Rounded search input and button
- Weather result card
- Error and info message styling

### Settings

File:

```text
weather_project/weather_project/settings.py
```

Important settings:

- `INSTALLED_APPS` includes `weather_app`.
- `OPENWEATHER_API_KEY` is loaded from environment variables.
- SQLite is used as the database.
- Static files are served from `STATIC_URL = "static/"`.
- Templates are enabled with `APP_DIRS = True`, so Django can find app templates.

## Common Commands

Run these commands from the folder containing `manage.py`:

```bash
cd weather_project
```

### Run Development Server

```bash
python manage.py runserver
```

### Run Migrations

```bash
python manage.py migrate
```

### Create New Migrations

Use this after adding or changing models:

```bash
python manage.py makemigrations
```

### Create Admin User

```bash
python manage.py createsuperuser
```

### Run Tests

```bash
python manage.py test
```

### Check Project Configuration

```bash
python manage.py check
```

This was run during README creation and Django reported no system check issues.

### Collect Static Files

Usually used before production deployment:

```bash
python manage.py collectstatic
```

Note:

`STATIC_ROOT` is not currently configured in `settings.py`, so configure it before using `collectstatic` for a real deployment.

### Open Django Shell

```bash
python manage.py shell
```

## Troubleshooting

### Problem: `OPENWEATHER_API_KEY is not set in environment`

Cause:

`OPENWEATHER_API_KEY` is missing or not loaded.

Fix:

Add this to `.env`:

```env
OPENWEATHER_API_KEY="your-openweathermap-api-key"
```

Then restart the development server.

### Problem: Weather Search Always Fails

Possible causes:

- Invalid city name
- Invalid OpenWeatherMap API key
- API key not activated yet
- Internet connection issue
- OpenWeatherMap rate limit

Fix:

1. Check `.env`.
2. Restart the server.
3. Try a common city such as `London`.
4. Test the API key directly in a browser:

```text
https://api.openweathermap.org/data/2.5/weather?q=London&appid=<your-api-key>&units=metric
```

### Problem: Secret Key From `.env` Is Not Being Used

Cause:

`settings.py` reads `SECRET_KEY`, but the current `.env` may use `DJANGO_SECRET_KEY`.

Fix:

Use this variable name:

```env
SECRET_KEY="your-secret-key"
```

### Problem: `ModuleNotFoundError: No module named 'django'`

Cause:

Dependencies are not installed or the virtual environment is not active.

Fix:

```bash
source venv/bin/activate
pip install -r requirements.txt
```

On Windows, activate the environment using the Windows activation command shown earlier.

### Problem: Migration Errors

Try:

```bash
python manage.py makemigrations
python manage.py migrate
```

If the database is only local development data and can be safely recreated, you can delete `db.sqlite3` and run migrations again. Do not delete a production database.

### Problem: Static CSS Not Loading

Check:

- `weather_app` is in `INSTALLED_APPS`.
- The CSS file exists at:

```text
weather_project/weather_app/static/weather_app/style.css
```

- The template has:

```django
{% load static %}
<link rel="stylesheet" href="{% static 'weather_app/style.css' %}">
```

### Problem: Admin Login Does Not Work

Cause:

No superuser exists yet.

Fix:

```bash
python manage.py createsuperuser
```

### Problem: Package Version Conflicts

Fix:

Use a clean virtual environment:

```bash
deactivate
rm -rf venv
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

On Windows, remove the `venv` folder manually or use the appropriate command for your shell.

## Deployment Notes

This project is currently configured mostly for local development.

Before deploying to production:

1. Set `DEBUG=False`.
2. Replace `ALLOWED_HOSTS = ['localhost', '127.0.0.1', '*']` with real domain names.
3. Use a strong `SECRET_KEY` from environment variables.
4. Keep `OPENWEATHER_API_KEY` private.
5. Configure `STATIC_ROOT`.
6. Run `python manage.py collectstatic`.
7. Consider using PostgreSQL instead of SQLite.
8. Use a production server such as Gunicorn, uWSGI, or Daphne.
9. Put the app behind a web server or platform that handles HTTPS.

Example production environment variables:

```env
SECRET_KEY="a-secure-production-secret-key"
DEBUG=False
OPENWEATHER_API_KEY="your-production-api-key"
```

Possible deployment platforms:

- Render
- Railway
- PythonAnywhere
- Heroku-style platforms
- VPS with Nginx and Gunicorn

## Future Improvements

Possible enhancements:

- Save search history in the database.
- Add a `WeatherSearch` model.
- Add tests for `views.py` and `utils.py`.
- Mock OpenWeatherMap in tests so tests do not depend on the internet.
- Add better error messages for invalid API keys and rate limits.
- Add loading states on the frontend.
- Add support for 5-day forecasts.
- Add country selection for cities with duplicate names.
- Add user accounts and saved favorite cities.
- Add production-ready static file settings.
- Rename `tempreature` to `temperature` in both the view and template.
- Fix small text typos in the UI such as `Humanity` to `Humidity`.
- Use HTTPS for weather icon URLs.
- Move `ALLOWED_HOSTS` into environment-based configuration.

## Contributing Guide

### 1. Create a Branch

```bash
git checkout -b feature/your-feature-name
```

### 2. Make Changes

Keep changes focused. Examples:

- One branch for styling changes
- One branch for model changes
- One branch for API logic changes

### 3. Run Checks

```bash
cd weather_project
python manage.py check
python manage.py test
```

### 4. Run Migrations If Models Changed

```bash
python manage.py makemigrations
python manage.py migrate
```

Commit migration files if they were created intentionally.

### 5. Commit Changes

```bash
git add .
git commit -m "Describe your change clearly"
```

### 6. Open a Pull Request

In the pull request, explain:

- What changed
- Why it changed
- How it was tested
- Any setup or migration notes

## Developer Notes for Future Me

### Important Architecture Decisions

- The project uses one Django app: `weather_app`.
- The main page is server-rendered with a Django template.
- Weather data is fetched live from OpenWeatherMap on each POST request.
- Weather results are not stored in the database.
- API-calling logic lives in `utils.py`, separate from the view.
- SQLite is used for simple local development.

### Hidden Gotchas

- `settings.py` reads `SECRET_KEY`, but the current `.env` may contain `DJANGO_SECRET_KEY`. Use `SECRET_KEY` unless the settings code is changed.
- The template and view use the misspelled key `tempreature`. It works only because both sides use the same spelling.
- The CSS class is also spelled `.tempreture`. Rename carefully if cleaning up.
- The UI text currently says `Humanity`; it should probably say `Humidity`.
- `ALLOWED_HOSTS` includes `'*'`, which is not appropriate for production.
- `DEBUG` defaults to `True`, which is not appropriate for production.
- `OPENWEATHER_API_KEY` defaults to an empty string. If it is missing, `get_weather()` raises `ValueError`.
- The OpenWeatherMap icon URL in the template uses `http://`. Prefer `https://` in production.

### Setup Warnings

- Always activate the virtual environment before running Django commands.
- Run commands from the folder that contains `manage.py`, which is:

```text
weather_project/
```

- Do not commit `.env`.
- Do not commit `db.sqlite3`.
- If an OpenWeatherMap API key was created recently, it may take time before it works.

### Assumptions

- This is currently a learning or small utility project.
- The app is intended to show current weather only, not forecasts.
- The database is only needed for Django's built-in admin/auth features right now.
- No custom user-facing authentication is required for the weather page.

### Fragile Parts of the Code

Be careful when editing:

- `weather_project/weather_project/settings.py`
  - Environment variable names and security settings live here.
- `weather_project/weather_app/utils.py`
  - External API request behavior lives here.
- `weather_project/weather_app/views.py`
  - The template depends on the exact context keys created here.
- `weather_project/weather_app/templates/weather_app/index.html`
  - The form field name `city` must match `request.POST.get('city')` in the view.
- `weather_project/weather_app/static/weather_app/style.css`
  - Class names must match the HTML template.

### Debugging Tips

- If the page loads but weather does not appear, check the API key first.
- If the form POST fails, make sure `{% csrf_token %}` is still inside the form.
- If the CSS disappears, check the static file path and `{% load static %}`.
- If admin does not work, run migrations and create a superuser.
- If OpenWeatherMap returns unexpected data, print or log the `response.status_code` and `response.text` in `utils.py` during local debugging.
- Use this command before assuming Django itself is broken:

```bash
python manage.py check
```
## License

This project is licensed under the MIT License.te / proprietary license if the project should not be reused

```text
Maintainer: Rupesh Rana
Email: rupeshrana20274@gmail.com
GitHub: https://github.com/Rupesh933
```
