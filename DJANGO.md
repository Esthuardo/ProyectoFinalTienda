# DJANGO

```sh
pip install Django
```

1º Crear un proyecto de Django

```sh
django-admin startproject <nombre_proyecto> .
```

2º Iniciar un proyecto de Django

```sh
python manage.py runserver
```

3º Crear super usuario

```sh
python manage.py createsuperuser
```

4º Crear una app

```sh
python manage.py startapp <nombre_app>
```

5º Crear las migraciones

```sh
python manage.py makemigrations
python manage.py makemigrations <nombre_app>
```

6º Sincronizar migraciones

```sh
python manage.py migrate
```
