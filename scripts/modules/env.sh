#!/bin/bash

echo "🐍 Configurando ambiente Python"

cd backend

python3 -m venv venv

venv/bin/pip install \
  django \
  djangorestframework \
  python-decouple \
  psycopg2-binary \
  djangorestframework-simplejwt \
  django-cors-headers \
  django-extensions >> /tmp/trash

venv/bin/pip freeze > requirements.txt

cd ..