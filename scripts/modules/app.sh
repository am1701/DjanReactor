#!/bin/bash

echo "📦 Criando app base"

cd backend

venv/bin/python -m django startapp api

cd api
touch urls.py
cd ..

cd ..