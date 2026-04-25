import httpx

class OpenLibraryService:
    @staticmethod
    async def get_book_info_by_isbn(isbn: str):
        """
        Consulta Open Library para obtener detalles del libro.
        """
        url = f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data"
        
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            data = response.json()
            
        key = f"ISBN:{isbn}"
        if key in data:
            book_data = data[key]
            publishers = book_data.get("publishers")
            editorial_name = publishers[0].get("name") if publishers else "Desconocida"
            return {
                "titulo": book_data.get("title"),
                "autor": book_data.get("authors")[0].get("name") if book_data.get("authors") else "Desconocido",
                "editorial": editorial_name,
                "isbn": isbn
            }
        return None