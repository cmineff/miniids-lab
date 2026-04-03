from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.event import Event
from app.models.alert import Alert
from datetime import datetime, timedelta

def evaluate_event(event: Event, db: Session):
    alerts = []

    if event.event_type == "login_failed":
        window_start = datetime.utcnow() - timedelta(seconds=120)

        recent_failures = db.query(func.count(Event.id)).filter(
            Event.source_ip == event.source_ip,
            Event.event_type == "login_failed",
            Event.created_at >= window_start
        ).scalar()

        print(f"DEBUG - IP: {event.source_ip} | Falhas: {recent_failures} | Janela desde: {window_start}")

        if recent_failures >= 5:
            alert = Alert(
                event_id=event.id,
                title="Possível ataque de Brute Force",
                description=f"IP {event.source_ip} gerou {recent_failures} falhas de login nos últimos 2 minutos.",
                severity="high",
                source_ip=event.source_ip
            )
            db.add(alert)
            db.commit()
            alerts.append(alert)

    return alerts
