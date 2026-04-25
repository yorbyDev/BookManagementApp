from pydantic import BaseModel
from typing import Optional

# Lo que pedimos para crear un libro
class BookCreate(BaseModel):
    titulo: str
    autor: str
    isbn: str
    editorial: Optional[str] = None
    disponible: bool = True

# Lo que devolvemos al cliente
class BookOut(BookCreate):
    id: int

    class Config:
        from_attributes = True