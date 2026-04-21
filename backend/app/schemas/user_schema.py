from pydantic import BaseModel, EmailStr

# Schema para crear un usuario (lo que recibimos del frontend)
class UserCreate(BaseModel):
    nombre: str
    apellido: str
    email: EmailStr
    password: str

# Schema para mostrar un usuario (lo que devolvemos al frontend)
# No incluimos el password por seguridad
class UserOut(BaseModel):
    id: int
    nombre: str
    apellido: str
    email: EmailStr

    class Config:
        from_attributes = True