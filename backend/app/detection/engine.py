from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.event import Event
from app.models.alert import Alert
from app.models.rule import Rule
from datetime import datetime, timedelta

def evaluate_event(event: Event, db: Session):
    alerts = []

    rules = db.query(Rule).filter(
        Rule.event_type == event.event_type,
        Rule.is_active == True
    ).all()

    for rule in rules:
        window_start = datetime.utcnow() - timedelta(seconds=rule.window_seconds)

        if rule.condition_type == "count_by_source_ip":
            count = db.query(func.count(Event.id)).filter(
                Event.source_ip == event.source_ip,
                Event.event_type == event.event_type,
                Event.created_at >= window_start
            ).scalar()

            print(f"DEBUG - Regra: {rule.name} | IP: {event.source_ip} | Count: {count} | Threshold: {rule.threshold}")

            if count >= rule.threshold:
                alert = Alert(
                    event_id=event.id,
                    title=f"Alerta: {rule.name}",
                    description=f"IP {event.source_ip} ativou a regra '{rule.name}' com {count} ocorrências nos últimos {rule.window_seconds} segundos.",
                    severity=rule.severity,
                    source_ip=event.source_ip
                )
                db.add(alert)
                db.commit()
                alerts.append(alert)

    return alerts
