# Justificación del Stack Tecnológico

Este documento detalla las librerías seleccionadas y su función dentro del proyecto de Gestión de Biblioteca.

## Base de Datos y Persistencia
* **SQLAlchemy (ORM):** Se utiliza como capa de abstracción para la base de datos. Permite interactuar con las tablas mediante objetos de Python, facilitando la mantenibilidad y protegiendo la aplicación contra inyección SQL.
* **PyMySQL (Driver):** Actúa como el conector de bajo nivel que permite a SQLAlchemy comunicarse con el servidor MySQL.

## Seguridad y Autenticación
* **Passlib [Bcrypt]:** Encargada del hashing de contraseñas. Bcrypt es un algoritmo diseñado para ser lento y resistente a ataques de fuerza bruta.
* **Python-jose:** Implementación de JSON Web Tokens (JWT) para manejar sesiones de usuario de forma segura y sin estado (stateless).
* **Cryptography:** Biblioteca base que proporciona las primitivas criptográficas necesarias para que los tokens y hashes funcionen correctamente.

## Comunicación y API
* **FastAPI:** Framework moderno de alto rendimiento para construir la API.
* **Python-multipart:** Necesario para procesar datos enviados a través de formularios (como el inicio de sesión), permitiendo que la API sea compatible con los métodos estándar de envío de datos de los navegadores.