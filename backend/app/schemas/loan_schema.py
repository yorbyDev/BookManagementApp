from pydantic import BaseModel
from datetime import date

class LoanCreate(BaseModel):
    libro_id: int

class LoanOut(BaseModel):
    id: int
    libro_id: int
    usuario_id: int
    prestado_en: date
    devolver_en: date
    devuelto: bool

    class Config:
        from_attributes = True
        
class LoanReturn(BaseModel):
    prestamo_id: int