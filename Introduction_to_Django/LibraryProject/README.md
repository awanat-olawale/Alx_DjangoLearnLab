# LIBRARY PROJECT

This is a test project to test understanding on project creation and files structure in Django

## PROJECT STRUCTURE
```
LibraryProject/
├── manage.py 
├── Pipfile 
├── Pipfile.lock 
└──LibraryProject/ 
    ├── __init__.py 
    ├── asgi.py 
    ├── settings.py 
    ├── urls.py 
    └──wsgi.py
```

- The **outer folder** is the project root (contains `manage.py`)
- The **inner folder** is the Django settings/config package

## STEPS TAKEN
1. Navigated into Introduction_to_Django folder and used pipenv to manage environment:

    ```
    pipenv install django
    ```

    `pipenv shell` to launch virtual environment

2. Created the project using:

    `django-admin startproject LibraryProject`

3. Ran the development server in the LibraryProject folder

    `cd LibraryProject`

    `python manage.py runserver`

4. File structure and roles:
    - `manage.py`: Command-line utility for Django tasks
    - `settings.py`: Project settings
    - `urls.py`: Main URL configuration
    - `wsgi.py` and `asgi.py`: Entry points for deployment


