from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.event import Event
from app.models.user import User
from app.schemas.event import EventCreate, EventResponse
from app.detection.engine import evaluate_event
from app.core.dependencies import get_current_user
from typing import List

router = APIRouter()

@router.post("/", response_model=EventResponse)
def create_event(event: EventCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_event = Event(**event.model_dump())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    evaluate_event(db_event, db)
    return db_event

@router.get("/", response_model=List[EventResponse])
def list_events(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(Event).all()
