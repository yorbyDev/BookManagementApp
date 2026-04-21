# backend/app/main.py
from fastapi import FastAPI

app = FastAPI(
    title="Sistema de Préstamos de Libros",
    description="API para la gestión de biblioteca con arquitectura modular",
    version="1.0.0"
)

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Bienvenido a la API de la Biblioteca"}