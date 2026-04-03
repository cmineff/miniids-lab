from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from app.api.routes import events, alerts, rules, auth
from app.models import event, alert, rule, user

Base.metadata.create_all(bind=engine)

app = FastAPI(title="MiniIDS Lab Platform")

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(events.router, prefix="/events", tags=["events"])
app.include_router(alerts.router, prefix="/alerts", tags=["alerts"])
app.include_router(rules.router, prefix="/rules", tags=["rules"])

@app.get("/")
def root():
    return {"message": "MiniIDS Lab Platform API"}

@app.get("/health")
def health():
    return {"status": "ok"}
