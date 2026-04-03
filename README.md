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
pip install fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv
pip install passlib[bcrypt] python-jose[cryptography] email-validator requests
pip install bcrypt==4.0.1

# Suba o banco de dados
docker-compose up -d

# Configure o .env
DATABASE_URL=postgresql://miniids:miniids123@localhost:5432/miniids_db
SECRET_KEY=sua-chave-secreta-aqui

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

## 🧪 Simulador de eventos

```bash
cd simulator
python generate_events.py
```

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
