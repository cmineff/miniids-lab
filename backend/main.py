from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.db.base import Base
from app.db.session import engine
from app.api.routes import events, alerts, rules, auth
from app.models import event, alert, rule, user

Base.metadata.create_all(bind=engine)

app = FastAPI(title="MiniIDS Lab Platform")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(events.router, prefix="/events", tags=["events"])
app.include_router(alerts.router, prefix="/alerts", tags=["alerts"])
app.include_router(rules.router, prefix="/rules", tags=["rules"])

app.mount("/", StaticFiles(directory="../frontend", html=True), name="frontend")

@app.get("/api")
def root():
    return {"message": "MiniIDS Lab Platform API"}

@app.get("/api/health")
def health():
    return {"status": "ok"}
