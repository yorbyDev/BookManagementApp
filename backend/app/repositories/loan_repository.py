from sqlalchemy.orm import Session
from app.models.models import Prestamo, Libro
from datetime import date, timedelta

class LoanRepository:
    @staticmethod
    def create_loan(db: Session, usuario_id: int, libro_id: int):
        # 1. Verificar disponibilidad del libro
        libro = db.query(Libro).filter(Libro.id == libro_id).first()
        
        if not libro or not libro.disponible:
            return None

        # 2. Definir fechas (usando date para coincidir con la columna Date)
        hoy = date.today()
        fecha_devolucion = hoy + timedelta(days=14)
        
        # 3. Crear el registro con nombres exactos de columnas
        nuevo_prestamo = Prestamo(
            libro_id=libro_id,
            usuario_id=usuario_id,
            prestado_en=hoy,
            devolver_en=fecha_devolucion
        )
        
        # 4. Actualizar estado del libro
        libro.disponible = False
        
        db.add(nuevo_prestamo)
        db.commit()
        db.refresh(nuevo_prestamo)
        
        return nuevo_prestamo
    
    @staticmethod
    def return_book(db: Session, prestamo_id: int):
        # 1. Buscar el préstamo activo
        prestamo = db.query(Prestamo).filter(Prestamo.id == prestamo_id, Prestamo.devuelto == False).first()
        
        if not prestamo:
            return None # No existe el préstamo o ya fue devuelto

        # 2. Marcar como devuelto
        prestamo.devuelto = True
        prestamo.devuelto_el = date.today()
        
        # 3. RESTAURAR ESTADO: El libro vuelve a estar disponible
        libro = db.query(Libro).filter(Libro.id == prestamo.libro_id).first()
        if libro:
            libro.disponible = True
        
        db.commit()
        db.refresh(prestamo)
        
        return prestamo