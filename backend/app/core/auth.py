import os
from datetime import datetime, timedelta, timezone
from typing import Optional
from jose import jwt
from dotenv import load_dotenv

load_dotenv()

# Cargar configuración desde .env
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

class AuthService:
    @staticmethod
    def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
        """Genera un token JWT firmado para un usuario."""
        to_encode = data.copy()
        
        # Obtenemos la hora actual en UTC de forma "aware"
        now = datetime.now(timezone.utc)
        
        # Calcular el tiempo de expiración
        if expires_delta:
            expire = now + expires_delta
        else:
            expire = now + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        
        # Añadir la expiración al cuerpo del token (payload)
        to_encode.update({"exp": expire})
        
        # Firmar y codificar el token
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt