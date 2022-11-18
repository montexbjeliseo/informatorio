# Creación y configuración de un proyecto

1. Entorno virtual
    - Instalar: pip install virtualenv
    - Crear entorno: virtualenv entorno
    - Activar: entorno\scripts\activate
2. Django
    - Instalar: con el entorno activado, pip install django==3.2
    - Crear proyecto: django-admin startproject blog
    - Correr proyecto: python blog\manage.py runserver
    - Ver en el navegador: localhost:8000 o 127.0.0.1:8000