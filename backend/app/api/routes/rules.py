from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.rule import Rule
from app.models.user import User
from app.schemas.rule import RuleCreate, RuleResponse
from app.core.dependencies import get_current_user, require_admin
from app.core.logging import setup_logger
from typing import List

logger = setup_logger("rules")
router = APIRouter()

@router.post("/", response_model=RuleResponse)
def create_rule(rule: RuleCreate, db: Session = Depends(get_db), current_user: User = Depends(require_admin)):
    db_rule = Rule(**rule.model_dump())
    db.add(db_rule)
    db.commit()
    db.refresh(db_rule)
    logger.info(f"Regra criada: ID {db_rule.id} | nome={db_rule.name} | usuário={current_user.email}")
    return db_rule

@router.get("/", response_model=List[RuleResponse])
def list_rules(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(Rule).all()

@router.get("/{rule_id}", response_model=RuleResponse)
def get_rule(rule_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    rule = db.query(Rule).filter(Rule.id == rule_id).first()
    if not rule:
        raise HTTPException(status_code=404, detail="Regra não encontrada")
    return rule

@router.patch("/{rule_id}/toggle", response_model=RuleResponse)
def toggle_rule(rule_id: int, db: Session = Depends(get_db), current_user: User = Depends(require_admin)):
    rule = db.query(Rule).filter(Rule.id == rule_id).first()
    if not rule:
        raise HTTPException(status_code=404, detail="Regra não encontrada")
    rule.is_active = not rule.is_active
    db.commit()
    db.refresh(rule)
    status = "ativada" if rule.is_active else "desativada"
    logger.info(f"Regra ID {rule_id} {status} | usuário={current_user.email}")
    return rule

@router.delete("/{rule_id}")
def delete_rule(rule_id: int, db: Session = Depends(get_db), current_user: User = Depends(require_admin)):
    rule = db.query(Rule).filter(Rule.id == rule_id).first()
    if not rule:
        raise HTTPException(status_code=404, detail="Regra não encontrada")
    db.delete(rule)
    db.commit()
    logger.warning(f"Regra ID {rule_id} removida | usuário={current_user.email}")
    return {"message": "Regra removida com sucesso"}
