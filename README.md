# Sistema de Gestión de Préstamos de Libros

Plataforma modular para la administración de bibliotecas, permitiendo el registro de usuarios, gestión de inventario y control de préstamos mediante una API segura.

## 1. Stack Tecnológico
* **Backend:** Python 3.x con FastAPI.
* **Base de Datos:** MySQL.
* **Seguridad:** JWT (JSON Web Tokens) y Bcrypt para hashing de contraseñas.
* **Frontend:** HTML5, JavaScript (ES6+) y Tailwind CSS.
* **Documentación API:** Swagger/OpenAPI (autogenerado por FastAPI).

## 2. Arquitectura del Proyecto (Capas)
Se implementa una arquitectura desacoplada para facilitar el mantenimiento:
* **Core:** Configuraciones globales, seguridad y constantes.
* **Models:** Representación de las tablas de la base de datos.
* **Schemas:** Definiciones de entrada/salida de datos (Pydantic).
* **Repositories:** Capa de acceso a datos (Queries SQL).
* **Services:** Lógica de negocio (reglas de préstamos).
* **API/Routes:** Definición de los puntos de acceso (Endpoints).