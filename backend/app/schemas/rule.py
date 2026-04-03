from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class RuleCreate(BaseModel):
    name: str
    description: Optional[str] = None
    event_type: str
    condition_type: str
    threshold: int
    window_seconds: int
    severity: str
    is_active: bool = True

class RuleResponse(RuleCreate):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
