# Registro de cambios

## CR-01 - Agregar rechazo de borrador
- **Requerimiento afectado:** RF-05.
- **Descripción:** incluir la opción de rechazar un borrador cuando no sea adecuado. Un borrador rechazado no se envía y su estado queda guardado.
- **Solicitante:** propuesta del equipo durante el walk-through; confirmar con la persona que participe en la validación.
- **Motivo:** evitar que una respuesta que no cumple la necesidad del usuario sea enviada por error.
- **Prioridad:** Alta.
- **Impacto:** interfaz de revisión, estado del mensaje, lógica de aprobación y pruebas.
- **Decisión:** Aprobado en la propuesta del equipo.
- **Nueva versión:** RF-05 versión 1.2.

## CR-SEG-01 - Cambio originado por seguridad
- **Escenario:** se detecta una vulnerabilidad importante en una dependencia utilizada para conectar o procesar correos.
- **Requerimientos afectados:** RF-01 y RNF-01; también se revisa RNF-03 por el comportamiento de reintentos.
- **Descripción:** revisar la dependencia, utilizar una versión corregida y verificar que la conexión y el procesamiento siguen funcionando sin exponer credenciales o duplicar envíos.
- **Solicitante:** hallazgo hipotético de una herramienta de análisis.
- **Motivo:** reducir el riesgo de acceso no autorizado o exposición de información.
- **Prioridad:** Alta.
- **Impacto:** dependencia, conexión, configuración, permisos y pruebas.
- **Decisión:** requiere revisión y aprobación del equipo antes de implementarse.
- **Nueva versión:** RNF-01 versión 1.1 y nuevo RNF-04 versión 1.0 propuesto.

## Registros de ejemplo para probar el notebook
CR-02 (mejorar el manejo de adjuntos, pendiente) y CR-03 (enviar automáticamente sin aprobación, rechazado) son ejemplos académicos incluidos únicamente para demostrar los conteos por estado y prioridad. No se presentan como solicitudes reales del proyecto.
