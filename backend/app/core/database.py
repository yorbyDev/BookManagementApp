from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración de la URL de conexión (Sustituye con tus credenciales de MySQL)
# Formato: mysql+pymysql://usuario:password@host:puerto/nombre_db
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:password@localhost:3306/biblioteca_db"

# El motor (engine) es el encargado de la comunicación con el driver PyMySQL
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

# Creamos una fábrica de sesiones para interactuar con la DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Clase base para que nuestros modelos hereden de ella
Base = declarative_base()

# Función para obtener la sesión de base de datos en cada petición (Dependency Injection)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()