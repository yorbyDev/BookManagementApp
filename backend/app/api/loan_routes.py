from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.dependencies import get_current_user, validate_admin
from app.schemas.loan_schema import LoanCreate, LoanOut, LoanReturn, LoanAdminView
from app.repositories.loan_repository import LoanRepository, Prestamo
from app.models.models import Usuario
from typing import List

router = APIRouter(prefix="/prestamos", tags=["Préstamos"])

@router.post("/", response_model=LoanOut)
def solicitar_prestamo(
    loan_data: LoanCreate, 
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
):
    # Intentamos crear el préstamo
    prestamo = LoanRepository.create_loan(
        db, 
        usuario_id=current_user.id, 
        libro_id=loan_data.libro_id
    )
    
    if not prestamo:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El libro no existe o no está disponible para préstamo."
        )
        
    return prestamo

@router.patch("/devolucion", response_model=LoanOut)
def devolver_libro(
    data: LoanReturn, 
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
):
    # Intentamos procesar la devolución
    prestamo = LoanRepository.return_book(db, prestamo_id=data.prestamo_id)
    
    if not prestamo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Préstamo no encontrado o ya ha sido devuelto anteriormente."
        )
        
    return prestamo

@router.get("/admin/estado-global", response_model=List[LoanAdminView])
def ver_estado_global(
    solo_activos: bool = Query(True, description="Si es True, solo muestra libros no devueltos"),
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(validate_admin)
):  
    query = db.query(Prestamo)
    
    if solo_activos:
        query = query.filter(Prestamo.devuelto == False)
    
    prestamos = query.all()
    
    # Transformamos los datos para incluir nombres de usuario y títulos
    # Gracias a las 'relationship' que definimos, esto es muy fácil:
    
    resultado = []
    for p in prestamos:
        resultado.append({
            "id": p.id,
            "prestado_en": p.prestado_en,
            "devolver_en": p.devolver_en,
            "devuelto": p.devuelto,
            "usuario_nombre": p.usuario.nombre,
            "libro_titulo": p.libro.titulo
        })
    
    return resultado