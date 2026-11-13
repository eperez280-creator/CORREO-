# Pruebas y criterios de aceptación

Los criterios se expresan en Given / When / Then (Dado / Cuando / Entonces). Los cuatro requisitos funcionales elegidos son RF-02, RF-03, RF-04 y RF-05. Para cada uno se incluye un escenario exitoso, uno alternativo y uno de error.

## RF-02 - Recepción de mensajes
- **Exitoso:** Dado que la cuenta está conectada y existe un correo nuevo, cuando el sistema consulta la bandeja, entonces registra el mensaje una sola vez.
- **Alternativo:** Dado que no hay mensajes nuevos, cuando se consulta la bandeja, entonces el sistema informa que no hay novedades y no crea registros.
- **Error:** Dado que el proveedor de correo no responde, cuando el sistema intenta consultar, entonces informa el error y no crea un registro incompleto.

## RF-03 - Clasificación
- **Exitoso:** Dado un mensaje que solicita un precio, cuando el sistema lo clasifica, entonces asigna la categoría “Cotizaciones”.
- **Alternativo:** Dado un mensaje cuyo contenido no permite reconocer una categoría, cuando se procesa, entonces queda como “Sin clasificar” para revisión.
- **Error:** Dado que no se puede leer el contenido, cuando se intenta clasificar, entonces el sistema informa que no fue posible clasificarlo y no inventa una categoría.

## RF-04 - Generación del borrador
- **Exitoso:** Dado un mensaje con asunto y contenido legibles, cuando se solicita generar una respuesta, entonces aparece un borrador relacionado con el mensaje y marcado “Borrador”.
- **Alternativo:** Dado un mensaje sin nombre del remitente, cuando se genera la respuesta, entonces el texto no inventa un nombre y utiliza un saludo general.
- **Error:** Dado que ocurre un error durante la generación, cuando se procesa el mensaje, entonces se informa el error y el sistema no envía ninguna respuesta.

## RF-05 - Aprobación manual
- **Exitoso:** Dado un borrador revisado por un usuario autorizado, cuando el usuario lo aprueba, entonces el sistema registra la aprobación y procesa un solo envío.
- **Alternativo:** Dado un borrador que el usuario considera incorrecto, cuando lo rechaza, entonces queda con estado “Rechazado” y no se envía.
- **Error:** Dado que el proveedor falla durante el envío, cuando el usuario aprueba el borrador, entonces se registra el error y se verifica el estado anterior antes de permitir un reintento.

## Relación con las pruebas
| Requisito | Prueba | Resultado que debe comprobarse |
|---|---|---|
| RF-01 | TC-01 | Conexión válida confirmada; conexión inválida rechazada. |
| RF-02 | TC-02 | El mensaje nuevo aparece una vez; no se duplica. |
| RF-03 | TC-03 | Se asigna categoría válida o “Sin clasificar”. |
| RF-04 | TC-04 | Se crea borrador y no se envía automáticamente. |
| RF-05 | TC-05 | Se edita, aprueba o rechaza; rechazo no envía. |
| RNF-01 | TC-06 | No se guardan contraseñas en texto plano y se rechaza autenticación inválida. |
| RNF-02 | TC-07 | Solo usuarios autorizados consultan contenido. |
| RNF-03 | TC-08 | No se produce un segundo envío de un mensaje ya enviado. |
