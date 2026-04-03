# 🛡️ MiniIDS Lab Platform

> Uma plataforma educacional de Detecção de Intrusão (IDS) para laboratório, construída com Python, FastAPI, PostgreSQL e dashboard web.

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Python](https://img.shields.io/badge/python-3.14-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

---

## 📌 Sobre o projeto

O **MiniIDS Lab Platform** é uma plataforma web de detecção de intrusão desenvolvida com foco educacional. Ela permite ingerir eventos de segurança, aplicar regras de detecção configuráveis, gerar alertas automáticos e visualizar tudo em um dashboard web completo.

O projeto foi criado para preencher uma lacuna real no mercado: ferramentas profissionais como Suricata, Snort e SIEMs são poderosas, mas inacessíveis para quem está aprendendo. O MiniIDS é simples o suficiente para entender, e estruturado o suficiente para ser real.

---

## 🎯 Funcionalidades

- ✅ Autenticação JWT com controle de acesso por papel (admin / analyst)
- ✅ Ingestão de eventos de segurança via API
- ✅ Motor de detecção com regras configuráveis
- ✅ Geração automática de alertas
- ✅ CRUD completo de regras de detecção
- ✅ Dashboard web com métricas em tempo real
- ✅ Telas de eventos, alertas e regras
- ✅ Ativar/desativar regras sem alterar código
- ✅ Documentação automática via Swagger UI

---

## 🧱 Arquitetura

```
[ Fonte de Eventos ]
        |
        v
[ API de Ingestão ]
        |
        v
[ Motor de Detecção ]
        |
   +---------+
   |         |
   v         v
[Eventos] [Alertas]
        |
        v
[ PostgreSQL ]
        |
        v
[ Dashboard Web ]
```

---

## 🚀 Stack tecnológica

| Camada   | Tecnologia              |
| -------- | ----------------------- |
| Backend  | Python 3.14 + FastAPI   |
| Banco    | PostgreSQL 16 (Docker)  |
| Frontend | HTML + CSS + JavaScript |
| Infra    | Docker + Docker Compose |
| Auth     | JWT + bcrypt            |

---

## 🗂️ Estrutura do projeto

```
miniids-lab/
├── backend/
│   ├── app/
│   │   ├── api/routes/      # endpoints
│   │   ├── core/            # segurança e dependências
│   │   ├── db/              # conexão e sessão
│   │   ├── detection/       # motor de detecção
│   │   ├── models/          # tabelas do banco
│   │   └── schemas/         # validação de dados
│   └── main.py
├── frontend/
│   ├── login.html
│   ├── index.html           # dashboard
│   ├── events.html
│   ├── alerts.html
│   ├── rules.html
│   ├── css/styles.css
│   └── js/
├── docker-compose.yml
└── README.md
```

---

## ⚙️ Como rodar localmente

```bash
# Clone o repositório
git clone https://github.com/cmineff/miniids-lab.git
cd miniids-lab

# Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\Activate.ps1  # Windows

# Instale as dependências
pip install fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv passlib[bcrypt] python-jose[cryptography] email-validator
pip install bcrypt==4.0.1

# Suba o banco de dados
docker-compose up -d

# Configure o .env
cp .env.example .env

# Rode a API
cd backend
uvicorn main:app --reload
```

Acesse em: `http://127.0.0.1:8000`

---

## 🔐 Primeiro acesso

Crie o usuário admin via Swagger em `http://127.0.0.1:8000/docs`:

```json
POST /auth/register
{
  "name": "Seu Nome",
  "email": "seu@email.com",
  "password": "suasenha",
  "role": "admin"
}
```

---

## 🗺️ Roadmap

| Sprint | Objetivo                      | Status       |
| ------ | ----------------------------- | ------------ |
| 0      | Preparação do ambiente        | ✅ Concluído |
| 1      | Primeira API FastAPI          | ✅ Concluído |
| 2      | Banco de dados e persistência | ✅ Concluído |
| 3      | Motor de detecção             | ✅ Concluído |
| 4      | Regras dinâmicas              | ✅ Concluído |
| 5      | Autenticação JWT              | ✅ Concluído |
| 6      | Dashboard web                 | ✅ Concluído |
| 7      | Simulador de eventos          | 🔄 Em breve  |
| 8      | Observabilidade e refinamento | 🔄 Em breve  |

---

## 👤 Autor

**Christian Mineff**
Technology Leader — Link School of Business
[GitHub](https://github.com/cmineff)

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
