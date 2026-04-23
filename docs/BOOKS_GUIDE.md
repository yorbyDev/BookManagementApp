# Gestión de Libros e Integración con Open Library

El sistema permite la administración del catálogo de libros con una funcionalidad de autocompletado inteligente.

## 1. Integración con Open Library
Para facilitar el registro, se ha implementado un servicio que consulta la API de Open Library.
- **Endpoint**: `GET /libros/buscar-isbn/{isbn}`
- **Funcionamiento**: Extrae automáticamente el Título, Autor y Editorial.
- **Nota**: Si el libro no existe en la base de datos de Open Library, el sistema notificará que el registro debe ser manual.

## 2. Lógica de Disponibilidad
A diferencia de un inventario comercial, este sistema utiliza un estado booleano:
- `disponible: true` -> El libro está en estantería y puede ser prestado.
- `disponible: false` -> El libro está actualmente en préstamo.

## 3. Seguridad en el Catálogo
- **Lectura (`GET`)**: Pública (cualquier usuario puede ver el catálogo).
- **Escritura (`POST`)**: Protegida. Solo usuarios con un Token JWT válido pueden registrar libros nuevos.