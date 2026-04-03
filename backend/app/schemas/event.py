from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict, Any

class EventCreate(BaseModel):
    timestamp: datetime
    source_ip: str
    destination_ip: Optional[str] = None
    source_port: Optional[int] = None
    destination_port: Optional[int] = None
    protocol: Optional[str] = None
    event_type: str
    username: Optional[str] = None
    hostname: Optional[str] = None
    message: str
    severity_hint: Optional[str] = None
    raw_data: Optional[Dict[str, Any]] = None

class EventResponse(EventCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
