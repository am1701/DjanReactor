#!/bin/sh

echo "Aguardando o banco ficar disponível..."

while ! nc -z db 5432; do
  sleep 1
done

echo "Banco disponível!"
exec "$@"
