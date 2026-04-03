import json
import requests
import time
from datetime import datetime, timezone

API_URL = "http://127.0.0.1:8000"
EMAIL = "c.mineff@lsb.com.br"
PASSWORD = "miniids@2026"

def login():
    response = requests.post(f"{API_URL}/auth/login", json={
        "email": EMAIL,
        "password": PASSWORD
    })
    if response.status_code == 200:
        token = response.json()["access_token"]
        print(f"✅ Login realizado com sucesso")
        return token
    else:
        print(f"❌ Erro no login: {response.text}")
        return None

def send_event(token, event_data):
    headers = {"Authorization": f"Bearer {token}"}
    event_data["timestamp"] = datetime.now(timezone.utc).isoformat()
    response = requests.post(f"{API_URL}/events/", json=event_data, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"❌ Erro ao enviar evento: {response.text}")
        return None

def run_simulation():
    print("🛡️  MiniIDS Lab — Simulador de Eventos")
    print("=" * 45)

    token = login()
    if not token:
        return

    with open("sample_events.json", "r", encoding="utf-8") as f:
        scenarios = json.load(f)

    total_events = 0
    for scenario in scenarios:
        print(f"\n📡 Cenário: {scenario['description']}")
        for _ in range(scenario["repeat"]):
            for event in scenario["events"]:
                result = send_event(token, event.copy())
                if result:
                    total_events += 1
                    print(f"   → Evento #{result['id']} enviado | {event['event_type']} | {event['source_ip']}")
                time.sleep(0.3)

    print(f"\n✅ Simulação concluída — {total_events} eventos enviados")
    print("🔍 Acesse o dashboard para ver os alertas gerados")
    print(f"   http://127.0.0.1:8000")

if __name__ == "__main__":
    run_simulation()
