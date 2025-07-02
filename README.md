# Taskmaster Django Project

A Django-based task management application.

## Setup Instructions

1. **Clone the repository** and navigate to the project directory

2. **Create a virtual environment** (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   - Copy `env.py.example` to `env.py`
   - Update the `SECRET_KEY` in `env.py` with a new secret key
   - Generate a new secret key with:

     ```bash
     python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
     ```

5. **Run migrations**:

   ```bash
   python manage.py migrate
   ```

6. **Start the development server**:

   ```bash
   python manage.py runserver
   ```

The application will be available at `http://127.0.0.1:8000/`

## Project Structure

- `taskmaster/` - Main Django project settings
- `tasks/` - Tasks application
- `env.py` - Environment variables (not tracked in git)
- `requirements.txt` - Python dependencies

## Security Note

The `env.py` file contains sensitive information and is not tracked in version control. Make sure to keep your secret keys secure and never commit them to the repository.
