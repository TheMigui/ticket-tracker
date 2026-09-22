from pydantic import BaseModel, Field
from typing import Optional
from datetime import date, time
from enum import Enum


class ExpenseCategory(str, Enum):
    ALIMENTACION = "alimentacion"
    RESTAURANTES = "restaurantes"
    TRANSPORTE = "transporte"
    OCIO = "ocio"
    HOGAR = "hogar"
    SALUD = "salud"
    TECNOLOGIA = "tecnologia"
    ROPA = "ropa"
    OTROS = "otros"


class TicketItem(BaseModel):
    nombre: str
    cantidad: float = 1.0
    precio_unitario: Optional[float] = None
    precio_total: float


class Ticket(BaseModel):
    comercio: Optional[str] = None
    fecha: Optional[date] = None
    hora: Optional[time] = None
    numero_ticket: Optional[str] = None

    productos: list[TicketItem] = Field(default_factory=list)

    subtotal: Optional[float] = None
    impuestos: Optional[float] = None
    descuento: Optional[float] = None
    total: Optional[float] = None

    categoria: Optional[ExpenseCategory] = None

    # Metadatos del proceso de extracción
    confianza_ocr: Optional[float] = None  # 0-1, qué tan segura está la extracción
    requiere_revision: bool = False
    imagen_original: Optional[str] = None  # nombre del archivo guardado