from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.user_schema import UserCreate, UserOut
from app.repositories.user_repository import UserRepository

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.post("/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def registrar_usuario(user: UserCreate, db: Session = Depends(get_db)):
    # 1. Verificar si el email ya existe
    db_user = UserRepository.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=400, 
            detail="El correo electrónico ya está registrado"
        )
    
    # 2. Crear el usuario
    return UserRepository.create_user(db=db, user_data=user)