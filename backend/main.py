from fastapi import FastAPI

app = FastAPI(title="MiniIDS Lab Platform")

@app.get("/")
def root():
    return {"message": "MiniIDS Lab Platform API"}

@app.get("/health")
def health():
    return {"status": "ok"}
