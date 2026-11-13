# Requisitos - Programa de respuesta automática de correos electrónicos

Este repositorio organiza los requerimientos y evidencias del taller integrador de Gestión de Requisitos de Software.

## Contenido
- `requisitos.md`: inventario y descripción de los ocho requisitos seleccionados.
- `cambios.md`: registro CR-01 y escenario CR-SEG-01.
- `trazabilidad.csv`: matriz Necesidad -> Requisito -> Historia -> Caso de uso -> Diseño -> Código -> Prueba.
- `pruebas.md`: criterios de aceptación y pruebas relacionadas.
- `funcionales/` y `no_funcionales/`: clasificación de requisitos.
- `modelos/prototipo_respuestas.html`: prototipo navegable con datos ficticios.
- `cambios/`: fichas de cambios.
- `trazabilidad/`: copia de la matriz.
- `pruebas/`: criterios de aceptación.
- `notebooks/taller_trazabilidad_cambios.ipynb`: notebook para Google Colab.

## Cómo usar el notebook
1. Abrir Google Colab.
2. Seleccionar `Archivo > Subir cuaderno` y cargar `notebooks/taller_trazabilidad_cambios.ipynb`.
3. Ejecutar las celdas en orden. Se utilizan `pandas` y `matplotlib`, disponibles normalmente en Colab.
4. Revisar la matriz, la detección de campos faltantes, el resumen de cambios y los dos gráficos.

## Alcance y honestidad de las evidencias
Los nombres de archivos de código de la matriz son módulos propuestos para una futura implementación; este taller no entrega un sistema de correo conectado y funcionando. El prototipo usa mensajes ficticios y sus botones solo simulan decisiones. La entrevista de la parte 9 debe realizarse con una persona diferente al desarrollador y completarse con sus respuestas reales.
