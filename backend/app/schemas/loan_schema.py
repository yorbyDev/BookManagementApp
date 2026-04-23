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

    class Config:
        from_attributes = True