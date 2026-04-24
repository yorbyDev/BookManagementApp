from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.auth import SECRET_KEY, ALGORITHM
from app.repositories.user_repository import UserRepository
from app.models.models import Usuario

# Esta línea le dice a FastAPI dónde buscar el token (en la ruta /auth/login)
# y habilita el botón de "Authorize" (el candadito) en Swagger.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """
    Esta función actúa como el 'portero'. 
    Valida el token y devuelve el usuario de la base de datos.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudo validar el carnet (token) de acceso",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        # 1. Decodificar el token usando nuestra SECRET_KEY
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub") # 'sub' es donde guardamos el email
        
        if email is None:
            raise credentials_exception
            
    except JWTError:
        # Si el token expiró o fue manipulado, lanzará este error
        raise credentials_exception

    # 2. Buscar al usuario en la BD para asegurar que aún existe
    user = UserRepository.get_user_by_email(db, email=email)
    if user is None:
        raise credentials_exception
        
    return user

def validate_admin(current_user: Usuario = Depends(get_current_user)):
    if not current_user.es_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tienes permisos suficientes para realizar esta acción."
        )
    return current_user