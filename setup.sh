#!/bin/bash

set -e
set -o pipefail

# =========================
# VALIDAÇÃO INICIAL
# =========================

PROJECT_NAME=$1

if [ -z "$PROJECT_NAME" ]; then
  echo "❌ Informe o nome do projeto"
  echo "Uso: ./setup.sh meu_projeto"
  exit 1
fi

BASE_DIR=$(pwd)
TARGET_DIR="$BASE_DIR/../$PROJECT_NAME"

echo ""
echo "🚀 DjanReactor"
echo ""
echo "📦 Projeto: $PROJECT_NAME"
echo ""
echo "📁 Será criado em:"
echo "   $TARGET_DIR"
echo ""

read -p "Continuar? (y/n): " CONFIRM

if [ "$CONFIRM" != "y" ]; then
  echo "❌ Cancelado"
  exit 1
fi

# =========================
# CRIA PASTA DO PROJETO
# =========================

mkdir -p "$TARGET_DIR"
cd "$TARGET_DIR"


DJANREACTOR_ROOT="$BASE_DIR"

source "$DJANREACTOR_ROOT/scripts/modules/base.sh"
source "$DJANREACTOR_ROOT/scripts/modules/env.sh"
source "$DJANREACTOR_ROOT/scripts/modules/config.sh"
source "$DJANREACTOR_ROOT/scripts/modules/django.sh"
source "$DJANREACTOR_ROOT/scripts/modules/app.sh"