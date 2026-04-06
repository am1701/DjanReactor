#!/bin/bash

echo "⚙️ Configurando ambiente (.env e Docker)"

cp -r "$DJANREACTOR_ROOT/config/templates/env" ./config/
cp -r "$DJANREACTOR_ROOT/config/templates/docker" ./config/


# gerar .env
backend/venv/bin/python "$DJANREACTOR_ROOT/config/utils/generate_env.py"
mv "$DJANREACTOR_ROOT/config/infra/env/.env.dev" ./config/env/env.dev.example

