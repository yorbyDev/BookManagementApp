from pydantic import BaseModel, EmailStr

# Lo que el usuario envía para iniciar sesión
class LoginRequest(BaseModel):
    email: EmailStr
    password: str

# Lo que el servidor devuelve cuando el login es exitoso
class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    es_admin: bool
    