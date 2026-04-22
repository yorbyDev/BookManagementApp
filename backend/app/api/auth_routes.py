from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import Security
from app.core.auth import AuthService
from app.repositories.user_repository import UserRepository
from app.schemas.auth_schema import LoginRequest, TokenResponse

router = APIRouter(prefix="/auth", tags=["Autenticación"])

@router.post("/login", response_model=TokenResponse)
def login(credentials: LoginRequest, db: Session = Depends(get_db)):
    # 1. Buscar al usuario por email
    user = UserRepository.get_user_by_email(db, email=credentials.email)
    
    # 2. Validar existencia y contraseña
    if not user or not Security.verify_password(credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # 3. Generar el Token (usamos el email como identificador en el payload)
    access_token = AuthService.create_access_token(data={"sub": user.email})
    
    return {"access_token": access_token, "token_type": "bearer"}