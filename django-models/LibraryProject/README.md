# LIBRARY PROJECT

This is a test project to test understanding on project creation and files structure in Django

## Project Structure
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

## Steps Taken
1. **Navigated into Introduction_to_Django folder and used pipenv to manage environment:**

    ```
    pipenv install django
    ```
    ```
    pipenv shell
    ``` 

   `pipenv shell` to launch virtual environment

2. **Created the project using:**

    ```
    django-admin startproject LibraryProject
    ```

3. **Ran the development server in the LibraryProject folder**

    ```
    cd LibraryProject
    ```
    ```
    python manage.py runserver
    ```

4. **File structure and roles:**
    - `manage.py`: Command-line utility for Django tasks
    - `settings.py`: Project settings
    - `urls.py`: Main URL configuration
    - `wsgi.py` and `asgi.py`: Entry points for deployment

5. **Django Admin Configuration for Book Model**

    **Setup Instructions**
        - Register Book Model in `bookshelf/admin.py` using the `@admin.register(Book)` decorator
        - Configurations are implemented in the `BookAdmin` class
        _ Create a superuser acccount with:
        ```
        python manage.py createsuperuser
        ```
        - Run the development server:
        ```
        python manage.py runserver
        ```
        - Access the admin interface at `http://localhost:8000/admin/` and login with superuser credentials to     manage Book entries


