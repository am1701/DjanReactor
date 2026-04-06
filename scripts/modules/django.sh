#!/bin/bash

echo "⚙️ Criando projeto Django"


cd backend

venv/bin/python -m django startproject core .

echo "🔧 Aplicando configurações"

cd ..