# Módulo 9: Panel de Administración y Seguridad

Este módulo define las capacidades exclusivas para usuarios con el rol de administrador (`es_admin: true`).

## 1. Control de Acceso (RBAC)
Se ha implementado una distinción de privilegios basada en la columna `es_admin` de la tabla `usuarios`:
- **Usuario Estándar**: Puede ver el catálogo y gestionar sus propios préstamos.
- **Administrador**: Tiene acceso a la gestión de inventario, visualización global de préstamos y administración de usuarios.

### Dependencia de Seguridad
Todas las rutas administrativas están protegidas por la función `validate_admin`, que intercepta la petición y verifica el token JWT y el rango del usuario antes de permitir la ejecución.

## 2. Endpoints Administrativos

### 🔍 Estado Global de Préstamos (`GET /prestamos/admin/estado-global`)
Permite obtener una visión completa de la biblioteca.
- **Parámetros**: `solo_activos` (Boolean). Si es `true`, filtra solo los libros que no han sido devueltos.
- **Respuesta**: Una lista que incluye el nombre del usuario y el título del libro, resolviendo las relaciones de base de datos.

### 📚 Gestión de Inventario
- **POST /libros/**: Solo los administradores pueden añadir nuevos ejemplares al sistema.
- **PUT/DELETE /libros/{id}**: Restringido a administradores para mantener la integridad del catálogo.

## 3. Lógica de Mapeo de Datos
Para optimizar la respuesta de la API, se utiliza un mapeo explícito en el Repositorio/Ruta que transforma los objetos de SQLAlchemy en el esquema `LoanAdminView`, garantizando que el Frontend reciba nombres legibles en lugar de solo IDs numéricos.