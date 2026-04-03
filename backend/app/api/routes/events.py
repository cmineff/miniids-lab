from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.event import Event
from app.models.user import User
from app.schemas.event import EventCreate, EventResponse
from app.detection.engine import evaluate_event
from app.core.dependencies import get_current_user
from app.core.logging import setup_logger
from typing import List, Optional

logger = setup_logger("events")
router = APIRouter()

@router.post("/", response_model=EventResponse)
def create_event(event: EventCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_event = Event(**event.model_dump())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    logger.info(f"Evento criado: ID {db_event.id} | tipo={db_event.event_type} | ip={db_event.source_ip}")
    alerts = evaluate_event(db_event, db)
    if alerts:
        logger.warning(f"{len(alerts)} alerta(s) gerado(s) para o evento ID {db_event.id}")
    return db_event

@router.get("/", response_model=List[EventResponse])
def list_events(
    skip: int = 0,
    limit: int = 50,
    event_type: Optional[str] = None,
    source_ip: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    query = db.query(Event)
    if event_type:
        query = query.filter(Event.event_type == event_type)
    if source_ip:
        query = query.filter(Event.source_ip == source_ip)
    return query.order_by(Event.id.desc()).offset(skip).limit(limit).all()
