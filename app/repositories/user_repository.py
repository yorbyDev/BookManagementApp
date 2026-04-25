from sqlalchemy.orm import Session
from app.models.models import Usuario
from app.schemas.user_schema import UserCreate
from app.core.security import Security

class UserRepository:
    @staticmethod
    def create_user(db: Session, user_data: UserCreate):
        """
        Recibe los datos del esquema, cifra la contraseña y 
        guarda el registro en la base de datos.
        """
        # 1. Cifrar la contraseña antes de guardar
        hashed_pwd = Security.hash_password(user_data.password)
        
        # 2. Crear la instancia del modelo SQLAlchemy
        new_user = Usuario(
            nombre=user_data.nombre,
            apellido=user_data.apellido,
            email=user_data.email,
            password=hashed_pwd
        )
        
        # 3. Persistir en la BD
        db.add(new_user)
        db.commit()
        db.refresh(new_user) # Refresca para obtener el ID generado
        return new_user

    @staticmethod
    def get_user_by_email(db: Session, email: str):
        """Busca un usuario por email para evitar duplicados o para login."""
        return db.query(Usuario).filter(Usuario.email == email).first()