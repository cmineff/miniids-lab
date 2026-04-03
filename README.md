# 🛡️ MiniIDS Lab Platform

> Uma plataforma educacional de Detecção de Intrusão (IDS) para laboratório, construída com Python, FastAPI, PostgreSQL e dashboard web.

![Status](https://img.shields.io/badge/status-MVP%20concluído-brightgreen)
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
- ✅ Ativar/desativar regras sem alterar código
- ✅ Dashboard web com métricas em tempo real
- ✅ Telas de eventos, alertas e regras
- ✅ Filtros por severidade e status nos alertas
- ✅ Paginação de eventos e alertas
- ✅ Logs estruturados de todas as operações
- ✅ Simulador de eventos com cenários reais
- ✅ Documentação automática via Swagger UI

---

## 🧱 Arquitetura

    [ Fonte de Eventos / Simulador ]
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

---

## 🚀 Stack tecnológica

| Camada   | Tecnologia              |
| -------- | ----------------------- |
| Backend  | Python 3.14 + FastAPI   |
| Banco    | PostgreSQL 16 (Docker)  |
| Frontend | HTML + CSS + JavaScript |
| Infra    | Docker + Docker Compose |
| Auth     | JWT + bcrypt            |
| Logs     | Python logging          |

---

## 🗂️ Estrutura do projeto

    miniids-lab/
    ├── backend/
    │   ├── app/
    │   │   ├── api/routes/      # endpoints
    │   │   ├── core/            # segurança, logs e dependências
    │   │   ├── db/              # conexão e sessão
    │   │   ├── detection/       # motor de detecção
    │   │   ├── models/          # tabelas do banco
    │   │   └── schemas/         # validação de dados
    │   └── main.py
    ├── frontend/
    │   ├── login.html
    │   ├── index.html
    │   ├── events.html
    │   ├── alerts.html
    │   ├── rules.html
    │   ├── css/styles.css
    │   └── js/
    ├── simulator/
    │   ├── generate_events.py
    │   └── sample_events.json
    ├── docker-compose.yml
    └── README.md

---

## ⚙️ Como rodar localmente

1.  Clone o repositório

        git clone https://github.com/cmineff/miniids-lab.git
        cd miniids-lab

2.  Crie e ative o ambiente virtual

        python -m venv venv
        venv\Scripts\Activate.ps1

3.  Instale as dependências

        pip install -r backend/requirements.txt

4.  Suba o banco de dados

        docker-compose up -d

5.  Configure o arquivo `.env` na raiz do projeto

        DATABASE_URL=postgresql://miniids:miniids123@localhost:5432/miniids_db
        SECRET_KEY=sua-chave-secreta-aqui

6.  Rode a API

        cd backend
        uvicorn main:app --reload

7.  Acesse em `http://127.0.0.1:8000`

---

## 🔐 Primeiro acesso

Crie o usuário admin via Swagger em `http://127.0.0.1:8000/docs`:

    POST /auth/register
    {
      "name": "Seu Nome",
      "email": "seu@email.com",
      "password": "suasenha",
      "role": "admin"
    }

---

## 🧪 Simulador de eventos

    cd simulator
    python generate_events.py

Cenários disponíveis:

- SSH Brute Force — 7 tentativas de login falhado
- Admin login fora do horário
- Port scan — 12 tentativas de varredura
- Logins normais — ruído realista

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
| 7      | Simulador de eventos          | ✅ Concluído |
| 8      | Observabilidade e refinamento | ✅ Concluído |

---

## 🔮 Próximas evoluções

- [ ] Parsing de logs reais (auth.log, syslog)
- [ ] Integração com Suricata logs
- [ ] Tags MITRE ATT&CK nos alertas
- [ ] Score de risco por IP
- [ ] Notificações por email
- [ ] Frontend em React
- [ ] Deploy em nuvem (AWS)

---

## 👤 Autor

**Christian Mineff**
Technology Leader — Link School of Business
[GitHub](https://github.com/cmineff)

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
