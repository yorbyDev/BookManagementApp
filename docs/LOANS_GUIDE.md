# Gestión de Préstamos

Este módulo controla la interacción entre usuarios y libros, manejando la lógica de disponibilidad y plazos de entrega.

## 1. Proceso de Préstamo (Transacción)
Cuando se solicita un préstamo (`POST /prestamos/`), el sistema ejecuta una operación atómica:
- **Validación**: Verifica que el libro exista y que `disponible` sea `true`.
- **Registro**: Crea una entrada en la tabla `prestamos` vinculando el `usuario_id` (extraído del token JWT) y el `libro_id`.
- **Estado**: Cambia automáticamente el campo `disponible` del libro a `false`.

## 2. Lógica de Fechas
El sistema automatiza el control de tiempos mediante la librería `datetime` de Python:
- **prestado_en**: Registra la fecha actual del servidor (`date.today()`).
- **devolver_en**: Calcula automáticamente la fecha límite sumando **14 días** a la fecha de préstamo.

## 3. Integridad Referencial
Gracias a las relaciones de SQLAlchemy (`relationship`), el modelo permite:
- Acceder a todos los préstamos de un usuario desde el objeto usuario.
- Consultar el historial de un libro desde el objeto libro.