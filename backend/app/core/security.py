from passlib.context import CryptContext

# Configuramos passlib para usar el algoritmo bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Security:
    @staticmethod
    def hash_password(password: str) -> str:
        """Recibe texto plano y devuelve el hash de Bcrypt."""
        return pwd_context.hash(password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """Compara una contraseña en texto plano con un hash almacenado."""
        return pwd_context.verify(plain_password, hashed_password)