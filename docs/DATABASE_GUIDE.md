# Guía de Base de Datos

## Configuración del ORM
Se utiliza **SQLAlchemy** con el patrón de diseño de "Sesión por Petición". Esto significa que cada vez que la API recibe una solicitud, se abre una conexión y se cierra automáticamente al terminar.

## Modelos y Tablas
1. **Usuarios:** Almacena credenciales. La contraseña se guarda mediante un Hash, nunca en texto plano.
2. **Libros:** Controla el inventario. El campo `disponible` es un booleano que actúa como bandera para la lógica de préstamos.
3. **Préstamos:** Tabla relacional que une usuarios con libros, registrando fechas clave de compromiso.

## Cómo migrar cambios
Por ahora, utilizaremos `Base.metadata.create_all(bind=engine)` en el arranque de la aplicación para generar las tablas automáticamente si no existen.

## Generación de Esquema:
El sistema utiliza "Lazy Initialization". Al iniciar el servidor FastAPI, el motor de SQLAlchemy escanea las clases que heredan de Base y ejecuta los comandos CREATE TABLE necesarios en MySQL.

## Verificación de Datos (QA)
Para confirmar que los registros se están guardando correctamente:
1. Conectarse al servidor MySQL mediante HeidiSQL.
2. Ejecutar la consulta: `SELECT id, nombre, email FROM usuarios;`.
3. Validar que la columna `password` contenga un hash (ej: `$2b$12$...`) y no la contraseña original.