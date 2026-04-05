#!/bin/bash

set -e
echo 'Iniciando o projeto django'

mkdir backend
cd backend
python3 -m venv venv

venv/bin/pip install django djangorestframework python-decouple psycopg2-binary djangorestframework-simplejwt django-cors-headers django-extensions
venv/bin/pip freeze > requirements.txt


echo 'Gerando o arquivo .env.dev'
venv/bin/python ../infra/.utils/generate_env.py


echo 'Iniciando um novo projeto django'
venv/bin/python -m django startproject core .


cp ../infra/.utils/reconfigure_settings.py .
venv/bin/python reconfigure_settings.py

venv/bin/python -m django startapp api
cd api
touch urls.py
cd ..