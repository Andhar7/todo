
```zsh
# Create virtual environment
python3 -m venv ckg
source ckg/bin/activate

# Install Django
pip install django

# Create django project
django-admin startproject todo_main

# Create django app
django-admin startapp todo_app

# Cteate models
# Add 'todo_app' to INSTALLED_APPS in todo_main/settings.py
# Define models in todo_app/models.py   


# Create migrations 
python3 manage.py makemigrations       
python3 manage.py migrate

# Create superuser
python3 manage.py createsuperuser
# Run server
python3 manage.py runserver

# Go to todo_main/views.py and create logic for the home page