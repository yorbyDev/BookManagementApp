Flujo de Seguridad:

Registro: La contraseña se recibe en texto plano, se procesa con passlib usando el algoritmo bcrypt y se almacena el hash resultante en MySQL.

Autenticación: El usuario envía sus credenciales; comparamos el hash. Si es correcto, generamos un JWT firmado con una SECRET_KEY.

Autorización: El frontend envía el token en el encabezado Authorization: Bearer <token>. FastAPI valida el token antes de permitir el acceso a rutas protegidas.