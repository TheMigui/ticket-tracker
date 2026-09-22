import os
import uuid
from fastapi import FastAPI, UploadFile, File
from app.schemas.ticket import Ticket

app = FastAPI(title="Ticket tracker")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/tickets/upload", response_model=Ticket)
async def upload_ticket(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        # De momento devolvemos un Ticket vacío marcado para revisión
        return Ticket(requiere_revision=True)

    extension = file.filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{extension}"
    filepath = os.path.join(UPLOAD_DIR, filename)

    contents = await file.read()
    with open(filepath, "wb") as f:
        f.write(contents)

    # TODO: aquí irá la llamada al pipeline de OCR + extracción
    # Por ahora devolvemos un Ticket "placeholder" con la imagen guardada
    ticket = Ticket(
        imagen_original=filename,
        requiere_revision=True,  # true porque aún no hay extracción real
    )

    return ticket