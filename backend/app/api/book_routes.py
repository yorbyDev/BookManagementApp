from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.schemas.book_schema import BookCreate, BookOut
from app.repositories.book_repository import BookRepository
from app.core.external_api import OpenLibraryService

router = APIRouter(prefix="/libros", tags=["Libros"])

@router.post("/", response_model=BookOut, status_code=status.HTTP_201_CREATED)
def crear_libro(
    book: BookCreate, 
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user) # <--- ¡El Portero en acción!
):
    # Verificar si el ISBN ya existe
    db_book = BookRepository.get_book_by_isbn(db, isbn=book.isbn)
    if db_book:
        raise HTTPException(status_code=400, detail="El ISBN ya está registrado")
    
    return BookRepository.create_book(db, book.model_dump())

@router.get("/", response_model=List[BookOut])
def listar_libros(db: Session = Depends(get_db)):
    return BookRepository.get_all_books(db)

@router.get("/buscar-isbn/{isbn}")
async def buscar_por_isbn(isbn: str, current_user = Depends(get_current_user)):
    """
    Busca información de un libro en Open Library por su ISBN.
    Solo disponible para usuarios autenticados.
    """
    book_info = await OpenLibraryService.get_book_info_by_isbn(isbn)
    
    if not book_info:
        raise HTTPException(
            status_code=404, 
            detail="No se encontró información para este ISBN. Favor ingresar manualmente."
        )
    
    return book_info