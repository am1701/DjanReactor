# ⚛️ DjanReactor

> ⚡ Gere um projeto fullstack completo com Django + React + Docker em segundos.

---

## 🚀 Sobre

O **DjanReactor** é um automatizador de setup que cria do zero um ambiente profissional com:

- 🐍 Django (backend)
- ⚛️ React + Vite (frontend)
- 🐳 Docker (dev e produção)
- 🐘 PostgreSQL

Você não perde tempo configurando nada. Executa um script e começa a desenvolver.

---

## 📦 Instalação

Clone o repositório:

git clone https://github.com/am1701/djanreactor.git

cd djanreactor

Dê permissão de execução:

chmod +x setup.sh

Execute o setup:

./setup.sh

---

## ⚙️ O que acontece ao rodar o setup

O script automaticamente:

- Cria a pasta backend/
- Inicializa um projeto Django configurado
- Instala dependências essenciais
- Cria a pasta frontend/
- Inicializa um projeto React com Vite
- Integra frontend com backend
- Prepara tudo para rodar via Docker

---

## 🧱 Estrutura do projeto

DjanReactor/
├── infra/
│ ├── .utils/
│ ├── Dockerfile
│ ├── backend/
│ │ ├── Dockerfile.dev
│ │ └── Dockerfile.prod
│ ├── frontend/
│ │ ├── Dockerfile.dev
│ │ └── Dockerfile.prod
│ ├── env/
│ │ └── .env.dev
│ ├── docker-compose.dev.yml
│ └── docker-compose.prod.yml
│
├── backend/ # gerado automaticamente
├── frontend/ # gerado automaticamente
│
├── setup.sh
└── README.md

---

## 🐍 Backend (Django)

Já vem pronto com:

- Django REST Framework
- Autenticação JWT (SimpleJWT)
- CORS configurado
- PostgreSQL
- Variáveis de ambiente com python-decouple

Dependências:

- Django
- django-cors-headers
- django-extensions
- djangorestframework
- djangorestframework_simplejwt
- psycopg2-binary
- PyJWT
- python-decouple

---

## ⚛️ Frontend (React)

- Vite (build rápido)
- Tailwind CSS
- Estrutura escalável
- Comunicação pronta com API

---

## 🐳 Rodando o projeto

docker compose -f infra/docker-compose.dev.yml up --build

---

## 🌍 Acessos

Frontend → http://localhost:5173  
Backend → http://localhost:8000

---

## 🧠 Filosofia

- Zero setup manual
- Estrutura profissional desde o início
- Pronto para escalar
- Código limpo e organizado

---

## 📄 Licença

MIT

---

## ⚡ Resumo

DjanReactor é o ponto de partida para qualquer projeto fullstack sério.

Menos setup. Mais construção.
