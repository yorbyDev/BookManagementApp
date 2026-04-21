# backend/app/main.py
from fastapi import FastAPI
from app.models import models
from app.core.database import engine

# Esta línea le dice a SQLAlchemy que cree las tablas definidas en 'models'
# basándose en la configuración del 'engine'
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Sistema de Préstamos de Libros",
    description="API para la gestión de biblioteca con arquitectura modular",
    version="1.0.0"
)

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Bienvenido a la API de la Biblioteca"}