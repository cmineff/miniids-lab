from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from app.api.routes import events

Base.metadata.create_all(bind=engine)

app = FastAPI(title="MiniIDS Lab Platform")

app.include_router(events.router, prefix="/events", tags=["events"])

@app.get("/")
def root():
    return {"message": "MiniIDS Lab Platform API"}

@app.get("/health")
def health():
    return {"status": "ok"}
