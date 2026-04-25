from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.user_schema import UserCreate, UserOut, UserUpdate
from app.repositories.user_repository import UserRepository
from app.core.dependencies import get_current_user, validate_admin # Importar el portero
from app.models.models import Usuario # Importar el modelo para el tipo de dato
from app.core.security import Security
from typing import List

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

# Router para crear un usuario nuevo
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

# Router para que un usuario una vez dentro del sistema pueda ver su perfil
@router.get("/perfil", response_model=UserOut)
def ver_mi_perfil(current_user: Usuario = Depends(get_current_user)):
    """
    Ruta protegida: Solo si el usuario envía un token válido
    en el header 'Authorization: Bearer <token>'
    """
    return current_user

# Router para que un usuario pueda actualizar su cuenta
@router.put("/me", response_model=UserOut)
def actualizar_mi_perfil(
    user_update: UserUpdate,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
):
    # 1. Si el usuario quiere cambiar el correo, verificar que no esté en uso por otro
    if user_update.email and user_update.email != current_user.email:
        email_exists = db.query(Usuario).filter(Usuario.email == user_update.email).first()
        if email_exists:
            raise HTTPException(
                status_code=400, 
                detail="El correo electrónico ya está registrado por otro usuario"
            )
        current_user.email = user_update.email

    # 2. Actualizar nombre si se proporciona
    if user_update.nombre:
        current_user.nombre = user_update.nombre

    # 3. Actualizar contraseña si se proporciona (Hasheándola primero)
    if user_update.password:
        current_user.password = Security.hash_password(user_update.password)

    db.commit()
    db.refresh(current_user)
    return current_user

# Router para que un administrador pueda ver el listado de usuarios registrados
@router.get("/admin/usuarios", response_model=List[UserOut])
def listar_usuarios_admin(
    db: Session = Depends(get_db),
    admin_user: Usuario = Depends(validate_admin) # Solo el jefe entra aquí
):
    return db.query(Usuario).all()

# Router para que un administrador pueda eliminar usuarios registrados
@router.delete("/admin/usuarios/{usuario_id}")
def eliminar_usuario(
    usuario_id: int,
    db: Session = Depends(get_db),
    admin_user: Usuario = Depends(validate_admin)
):
    """Elimina un usuario (Usar con precaución por la integridad referencial)."""
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    db.delete(usuario)
    db.commit()
    return {"message": f"Usuario {usuario_id} eliminado correctamente"}
