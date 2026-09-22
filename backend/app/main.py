from fastapi import FastAPI

app = FastAPI(title="Ticket tracker")

@app.get("/health")
def health():
    return {"status": "ok"}