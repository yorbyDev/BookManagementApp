from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.user_schema import UserCreate, UserOut
from app.repositories.user_repository import UserRepository
from app.core.dependencies import get_current_user, validate_admin # Importar el portero
from app.models.models import Usuario # Importar el modelo para el tipo de dato
from typing import List

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

@router.get("/perfil", response_model=UserOut)
def ver_mi_perfil(current_user: Usuario = Depends(get_current_user)):
    """
    Ruta protegida: Solo si el usuario envía un token válido
    en el header 'Authorization: Bearer <token>'
    """
    return current_user

@router.get("/admin/usuarios", response_model=List[UserOut])
def listar_usuarios_admin(
    db: Session = Depends(get_db),
    admin_user: Usuario = Depends(validate_admin) # Solo el jefe entra aquí
):
    return db.query(Usuario).all()