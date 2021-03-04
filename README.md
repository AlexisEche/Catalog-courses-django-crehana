# Catálogo de exploración de cursos

Catálogo que permite explorar cursos utilizando filtros y paginación, mostrando la información de los cursos y poder realizar la compra del curso.

### Características

- Fueron utilizados Django + DjangoRestFramework 
- Python3.6.4 


### How to run the project for development
- Create yout virtual environment

```python3 -m venv venv```

- Active your virtual environment

```source venv/bin/activate```

- Install requirements

```pip install -r requirements.txt```

- Configure DATABASES in settings: 

``` DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
} 
```
  
- Run migrations

```python manage.py migrate```
  
- Run project

```python manage.py runserver```