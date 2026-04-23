from sqlalchemy import Column, Integer, String, Date, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.core.database import Base # Crearemos este archivo a continuación

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(45), nullable=False)
    apellido = Column(String(45), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False) # Necesario para login
    password = Column(String(255), nullable=False) # Aumentado para el hash de Bcrypt

    prestamos = relationship("Prestamo", back_populates="usuario")

class Libro(Base):
    __tablename__ = "libros"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(45), nullable=False)
    autor = Column(String(45), nullable=False)
    isbn = Column(String(45), unique=True, nullable=False)
    editorial = Column(String(100), nullable=True)
    disponible = Column(Boolean, default=True) # TINYINT en MySQL es Boolean en Python

    prestamos = relationship("Prestamo", back_populates="libro")

class Prestamo(Base):
    __tablename__ = "prestamos"

    id = Column(Integer, primary_key=True, index=True)
    libro_id = Column(Integer, ForeignKey("libros.id"))
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    prestado_en = Column(Date, nullable=False)
    devolver_en = Column(Date, nullable=False)
    devuelto = Column(Boolean, default=False)
    devuelto_el = Column(Date, nullable=True)

    usuario = relationship("Usuario", back_populates="prestamos")
    libro = relationship("Libro", back_populates="prestamos")