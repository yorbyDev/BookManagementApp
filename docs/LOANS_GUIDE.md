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

## 4. Proceso de Devolución (`PATCH /devolucion`)
Cierra el ciclo del préstamo mediante las siguientes acciones:
- **Finalización**: Cambia el estado `devuelto` a `true` en el registro del préstamo.
- **Restauración**: El libro vinculado recupera su estado `disponible: true`.
- **Seguridad**: Solo usuarios autenticados pueden procesar devoluciones (el bibliotecario o el sistema).

## 5. Sistema de Historial
El sistema mantiene un registro permanente de cada transacción. 
- Un registro con `devuelto: false` representa un préstamo activo.
- Un registro con `devuelto: true` representa un préstamo finalizado (histórico).
Esta estructura permite auditar quién tuvo qué libro y en qué fechas, independientemente de si el libro está disponible ahora.