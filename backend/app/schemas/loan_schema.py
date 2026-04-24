from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Optional

# --- 1. Base Común ---
# Aquí ponemos lo que casi todos comparten
class LoanBase(BaseModel):
    prestado_en: date
    devolver_en: date
    devuelto: bool

    model_config = ConfigDict(from_attributes=True)

# --- 2. Esquemas de Salida (Lectura) ---

# El LoanOut estándar (con IDs)
class LoanOut(LoanBase):
    id: int
    libro_id: int
    usuario_id: int
    devuelto_el: Optional[date] = None

# Vista para el Usuario (con Título)
class MyLoanOut(LoanBase):
    id: int
    libro_titulo: str
    devuelto_el: Optional[date] = None

# Vista para el Admin (con Título y Nombre)
class LoanAdminView(LoanBase):
    id: int
    usuario_nombre: str
    libro_titulo: str

# --- 3. Esquemas de Entrada (Acciones) ---

class LoanCreate(BaseModel):
    libro_id: int

class LoanReturn(BaseModel):
    prestamo_id: int