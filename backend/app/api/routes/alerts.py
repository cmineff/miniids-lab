from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.alert import Alert
from app.schemas.alert import AlertResponse
from typing import List

router = APIRouter()

@router.get("/", response_model=List[AlertResponse])
def list_alerts(db: Session = Depends(get_db)):
    return db.query(Alert).all()

@router.get("/{alert_id}", response_model=AlertResponse)
def get_alert(alert_id: int, db: Session = Depends(get_db)):
    return db.query(Alert).filter(Alert.id == alert_id).first()
