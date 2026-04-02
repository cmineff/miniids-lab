# 🛡️ MiniIDS Lab Platform

> Uma plataforma educacional de Detecção de Intrusão (IDS) para laboratório, construída com Python, FastAPI e PostgreSQL.

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Python](https://img.shields.io/badge/python-3.14-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

---

## 📌 Sobre o projeto

O **MiniIDS Lab Platform** é uma plataforma web de detecção de intrusão desenvolvida com foco educacional. Ela permite ingerir eventos de segurança, aplicar regras de detecção, gerar alertas e visualizar tudo em um dashboard web.

O projeto foi criado para preencher uma lacuna real no mercado: ferramentas profissionais como Suricata, Snort e SIEMs são poderosas, mas inacessíveis para quem está aprendendo. O MiniIDS é simples o suficiente para entender, e estruturado o suficiente para ser real.

---

## 🎯 Objetivos

- Receber e armazenar eventos de segurança via API
- Aplicar regras de detecção configuráveis
- Gerar alertas automáticos com severidade
- Exibir dados em dashboard web
- Servir como laboratório prático de cibersegurança

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
| Banco    | PostgreSQL              |
| Frontend | HTML + CSS + JavaScript |
| Infra    | Docker + Docker Compose |
| Auth     | JWT                     |

---

## 📦 Funcionalidades previstas

- [x] API base com FastAPI
- [x] Endpoint `/health`
- [x] Documentação automática Swagger
- [ ] Conexão com PostgreSQL
- [ ] Cadastro e listagem de eventos
- [ ] Motor de detecção com regras
- [ ] Geração de alertas
- [ ] CRUD de regras
- [ ] Autenticação JWT
- [ ] Dashboard web
- [ ] Simulador de eventos
- [ ] Docker Compose

---

## 🗂️ Estrutura do projeto

```
miniids-lab/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── db/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── detection/
│   └── main.py
├── frontend/
├── simulator/
├── docs/
├── docker-compose.yml
└── README.md
```

---

## ⚙️ Como rodar localmente

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/miniids-lab.git
cd miniids-lab

# Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\Activate.ps1  # Windows

# Instale as dependências
pip install fastapi uvicorn

# Rode a API
uvicorn backend.main:app --reload
```

Acesse em: `http://127.0.0.1:8000/docs`

---

## 🗺️ Roadmap

| Sprint | Objetivo                      | Status       |
| ------ | ----------------------------- | ------------ |
| 0      | Preparação do ambiente        | ✅ Concluído |
| 1      | Primeira API FastAPI          | ✅ Concluído |
| 2      | Banco de dados e persistência | 🔄 Em breve  |
| 3      | Motor de detecção             | 🔄 Em breve  |
| 4      | Regras dinâmicas              | 🔄 Em breve  |
| 5      | Autenticação JWT              | 🔄 Em breve  |
| 6      | Dashboard web                 | 🔄 Em breve  |
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
