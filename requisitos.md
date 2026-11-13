# Inventario de requerimientos

**Proyecto:** Programa de respuesta automática de correos electrónicos.

Se seleccionan cinco requisitos funcionales y tres no funcionales a partir del documento base suministrado. Todos tienen prioridad, fuente, responsable, versión, estado y fecha de registro.

## RF-01 - Funcional
- **Versión:** 1.0
- **Prioridad:** Alta
- **Fuente:** Documento base, funcional 01: Conexión al correo
- **Responsable:** Equipo del proyecto
- **Estado:** Analizado y corregido
- **Fecha:** 12/11/2026
- **Descripción:** El sistema debe permitir que un usuario autorizado conecte una cuenta de correo mediante el mecanismo de autenticación segura ofrecido por el proveedor. Debe informar si la conexión fue exitosa o si ocurrió un error. Si la autorización falla, la cuenta debe permanecer desconectada.
- **Criterio de aceptación resumido:** Con una autorización válida, la cuenta queda conectada y el sistema lo confirma. Con una autorización inválida, la cuenta no queda conectada y se muestra un mensaje de error.

## RF-02 - Funcional
- **Versión:** 1.0
- **Prioridad:** Alta
- **Fuente:** Documento base, funcional 02: Recepción de correos
- **Responsable:** Equipo del proyecto
- **Estado:** Analizado y corregido
- **Fecha:** 12/11/2026
- **Descripción:** El sistema debe consultar la cuenta conectada e identificar los mensajes nuevos recibidos. Cada mensaje debe registrarse usando el identificador que entrega el proveedor de correo, para evitar que el mismo mensaje se procese más de una vez.
- **Criterio de aceptación resumido:** Al detectar un mensaje nuevo, aparece una sola vez en la bandeja del sistema. Al consultar de nuevo el mismo mensaje, no se crea un segundo registro.

## RF-03 - Funcional
- **Versión:** 1.0
- **Prioridad:** Alta
- **Fuente:** Documento base, funcional 04: Clasificación de correos
- **Responsable:** Equipo del proyecto
- **Estado:** Analizado y corregido
- **Fecha:** 12/11/2026
- **Descripción:** El sistema debe asignar a cada mensaje recibido una de estas categorías: solicitudes, quejas, cotizaciones, pedidos o consultas generales. Cuando no tenga información suficiente para asignar una categoría, debe marcarlo como “Sin clasificar” y permitir que el usuario lo revise.
- **Criterio de aceptación resumido:** Cada mensaje queda asociado a una de las cinco categorías o a “Sin clasificar”; el usuario puede identificar la categoría en la bandeja.

## RF-04 - Funcional
- **Versión:** 1.0
- **Prioridad:** Alta
- **Fuente:** Documento base, funcional 05: Generación automática de respuestas
- **Responsable:** Equipo del proyecto
- **Estado:** Analizado y corregido
- **Fecha:** 12/11/2026
- **Descripción:** El sistema debe elaborar un borrador de respuesta relacionado con el asunto y el contenido del correo recibido. El borrador debe quedar identificado como “Borrador” y no debe enviarse por el solo hecho de haber sido generado.
- **Criterio de aceptación resumido:** Después del procesamiento, se muestra un texto de respuesta relacionado con el mensaje y con estado “Borrador”; no se realiza ningún envío automático.

## RF-05 - Funcional
- **Versión:** 1.2
- **Prioridad:** Alta
- **Fuente:** Documento base, funcional 09: Aprobación manual
- **Responsable:** Equipo del proyecto
- **Estado:** Analizado y corregido
- **Fecha:** 12/11/2026
- **Descripción:** El sistema debe permitir que un usuario autorizado consulte el remitente, el asunto, el contenido del mensaje, su categoría y el borrador de respuesta. El usuario puede editarlo, aprobarlo para su envío o rechazarlo. Solamente una respuesta aprobada puede enviarse. Una respuesta rechazada no se envía y su estado queda registrado.
- **Criterio de aceptación resumido:** El usuario puede editar el borrador. Al aprobarlo, el sistema registra la aprobación y el resultado del envío. Al rechazarlo, registra el estado “Rechazado” y no lo envía.

## RNF-01 - No funcional
- **Versión:** 1.0
- **Prioridad:** Alta
- **Fuente:** Documento base, no funcional 01: Seguridad
- **Responsable:** Equipo del proyecto
- **Estado:** Analizado; observación de diseño
- **Fecha:** 12/11/2026
- **Descripción:** El sistema debe proteger las credenciales y los datos de autorización de la cuenta de correo. No debe mostrar ni guardar contraseñas en texto plano y debe utilizar el mecanismo de autenticación segura y el canal cifrado que soporte el proveedor de correo.
- **Criterio de aceptación resumido:** En la revisión de configuración y almacenamiento no se encuentran contraseñas guardadas en texto plano; una conexión sin autenticación válida es rechazada.

## RNF-02 - No funcional
- **Versión:** 1.0
- **Prioridad:** Alta
- **Fuente:** Documento base, no funcional 02: Privacidad
- **Responsable:** Equipo del proyecto
- **Estado:** Analizado y corregido
- **Fecha:** 12/11/2026
- **Descripción:** El sistema debe permitir consultar el contenido de los correos únicamente a los usuarios que tengan el permiso correspondiente. Un usuario sin permiso no debe poder abrir ni consultar el contenido del mensaje.
- **Criterio de aceptación resumido:** Un usuario con permiso puede consultar el mensaje; un usuario sin permiso recibe acceso denegado y no visualiza el contenido.

## RNF-03 - No funcional
- **Versión:** 1.0
- **Prioridad:** Alta
- **Fuente:** Documento base, no funcional 06: Confiabilidad
- **Responsable:** Equipo del proyecto
- **Estado:** Analizado; observación de diseño
- **Fecha:** 12/11/2026
- **Descripción:** El sistema debe evitar el envío duplicado de una respuesta para un mismo mensaje. Antes de reintentar un envío, debe consultar si el envío anterior quedó registrado como exitoso. También debe guardar el estado de cada intento.
- **Criterio de aceptación resumido:** Al repetir una operación ya confirmada como enviada, el sistema no realiza un segundo envío y conserva el registro del estado.
