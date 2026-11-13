# Requisitos no funcionales

- **RNF-01** (Alta): El sistema debe proteger las credenciales y los datos de autorización de la cuenta de correo. No debe mostrar ni guardar contraseñas en texto plano y debe utilizar el mecanismo de autenticación segura y el canal cifrado que soporte el proveedor de correo.
- **RNF-02** (Alta): El sistema debe permitir consultar el contenido de los correos únicamente a los usuarios que tengan el permiso correspondiente. Un usuario sin permiso no debe poder abrir ni consultar el contenido del mensaje.
- **RNF-03** (Alta): El sistema debe evitar el envío duplicado de una respuesta para un mismo mensaje. Antes de reintentar un envío, debe consultar si el envío anterior quedó registrado como exitoso. También debe guardar el estado de cada intento.
