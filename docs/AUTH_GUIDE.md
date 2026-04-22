# Manual de Autenticación (JWT)

Este sistema utiliza **OAuth2 con Password Bearer** para proteger los recursos.

## Flujo de Acceso
1. **Login**: Enviar `username` (email) y `password` a `/auth/login`.
2. **Token**: El servidor devuelve un `access_token` y un `token_type: bearer`.
3. **Uso**: Incluir el token en el header de cada petición protegida:
   `Authorization: Bearer <tu_token>`

## Variables de Seguridad (en .env)
- `SECRET_KEY`: Clave para firmar los tokens.
- `ALGORITHM`: HS256.
- `ACCESS_TOKEN_EXPIRE_MINUTES`: Tiempo de vida del carnet.

## Cómo probar en Swagger
1. Click en el botón **Authorize** (candado).
2. Ingresar credenciales.
3. El candado se cerrará y todas las peticiones enviarán el token automáticamente.