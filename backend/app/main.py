# backend/app/main.py
from fastapi import FastAPI
from app.models import models
from app.core.database import engine
# Importar rutas
from app.api.user_routes import router as user_router
from app.api.auth_routes import router as auth_router
from app.api.book_routes import router as book_router

# Esta línea le dice a SQLAlchemy que cree las tablas definidas en 'models'
# basándose en la configuración del 'engine'
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Sistema de Préstamos de Libros",
    description="API para la gestión de biblioteca con arquitectura modular",
    version="1.0.0"
)

# Registrar las rutas de la API
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(book_router)

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Bienvenido a la API de la Biblioteca"}