from sqlalchemy.orm import Session
from app.models.models import Libro

class BookRepository:
    @staticmethod
    def create_book(db: Session, book_data: dict):
        nuevo_libro = Libro(**book_data)
        db.add(nuevo_libro)
        db.commit()
        db.refresh(nuevo_libro)
        return nuevo_libro

    @staticmethod
    def get_all_books(db: Session, skip: int = 0, limit: int = 100):
        return db.query(Libro).offset(skip).limit(limit).all()
    
    @staticmethod
    def get_book_by_isbn(db: Session, isbn: str):
        return db.query(Libro).filter(Libro.isbn == isbn).first()