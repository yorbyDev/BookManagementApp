from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.schemas.loan_schema import LoanCreate, LoanOut
from app.repositories.loan_repository import LoanRepository
from app.models.models import Usuario

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