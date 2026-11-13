import pandas as pd
import matplotlib.pyplot as plt

# Matriz de trazabilidad
datos = [
    {"Necesidad":"N-01: conectar una cuenta", "Requisito":"RF-01", "Historia":"US-01", "Caso_Uso":"CU-01", "Diseño":"DS-01", "Codigo":"src/auth_mail.py", "Prueba":"TC-01"},
    {"Necesidad":"N-02: identificar mensajes nuevos", "Requisito":"RF-02", "Historia":"US-02", "Caso_Uso":"CU-02", "Diseño":"DS-02", "Codigo":"src/mail_reader.py", "Prueba":"TC-02"},
    {"Necesidad":"N-03: organizar correos", "Requisito":"RF-03", "Historia":"US-03", "Caso_Uso":"CU-03", "Diseño":"DS-03", "Codigo":"src/classifier.py", "Prueba":"TC-03"},
    {"Necesidad":"N-04: reducir redacción manual", "Requisito":"RF-04", "Historia":"US-04", "Caso_Uso":"CU-04", "Diseño":"DS-04", "Codigo":"src/response_generator.py", "Prueba":"TC-04"},
    {"Necesidad":"N-05: revisar antes de enviar", "Requisito":"RF-05", "Historia":"US-05", "Caso_Uso":"CU-05", "Diseño":"DS-05", "Codigo":"src/approval_view.py", "Prueba":"TC-05"},
    {"Necesidad":"N-06: proteger la cuenta", "Requisito":"RNF-01", "Historia":"US-06", "Caso_Uso":"CU-01", "Diseño":"DS-01", "Codigo":"src/auth_mail.py", "Prueba":"TC-06"},
    {"Necesidad":"N-07: restringir el acceso al correo", "Requisito":"RNF-02", "Historia":"US-07", "Caso_Uso":"CU-06", "Diseño":"DS-06", "Codigo":"src/access_control.py", "Prueba":"TC-07"},
    {"Necesidad":"N-08: evitar respuestas duplicadas", "Requisito":"RNF-03", "Historia":"US-08", "Caso_Uso":"CU-07", "Diseño":"DS-07", "Codigo":"src/send_control.py", "Prueba":"TC-08"}
]
df = pd.DataFrame(datos)
print("MATRIZ DE TRAZABILIDAD")
print(df.to_string(index=False))

def revisar_trazabilidad(matriz):
    columnas = ["Historia", "Caso_Uso", "Codigo", "Prueba"]
    faltantes = []
    for _, fila in matriz.iterrows():
        for columna in columnas:
            valor = fila[columna]
            if pd.isna(valor) or str(valor).strip() == "":
                faltantes.append({"Requisito": fila["Requisito"], "Elemento faltante": columna})
    resultado = pd.DataFrame(faltantes, columns=["Requisito", "Elemento faltante"])
    if resultado.empty:
        print("\nNo se encontraron requerimientos con trazabilidad incompleta.")
    else:
        print("\nElementos sin relacionar:")
        print(resultado.to_string(index=False))
    return resultado

revisar_trazabilidad(df)

# Demostración: se vacía temporalmente la prueba de RNF-03 para comprobar la función
matriz_prueba = df.copy()
matriz_prueba.loc[matriz_prueba["Requisito"] == "RNF-03", "Prueba"] = ""
print("\nComprobación con un dato faltante:")
revisar_trazabilidad(matriz_prueba)

# Control de cambios: CR-02 y CR-03 son ejemplos académicos; CR-SEG-01 es el escenario hipotético de seguridad
cambios = [
    {"id":"CR-01", "requisito":"RF-05", "version_anterior":"1.1", "version_nueva":"1.2", "prioridad":"Alta", "impacto":"Medio", "estado":"Aprobado"},
    {"id":"CR-02", "requisito":"RF-02", "version_anterior":"1.0", "version_nueva":"1.1", "prioridad":"Media", "impacto":"Medio", "estado":"Pendiente"},
    {"id":"CR-03", "requisito":"RF-05", "version_anterior":"1.2", "version_nueva":"1.3", "prioridad":"Baja", "impacto":"Alto", "estado":"Rechazado"},
    {"id":"CR-SEG-01", "requisito":"RNF-01", "version_anterior":"1.0", "version_nueva":"1.1", "prioridad":"Alta", "impacto":"Alto", "estado":"Pendiente"}
]
cambios_df = pd.DataFrame(cambios)
print("\nREGISTRO DE CAMBIOS")
print(cambios_df.to_string(index=False))
print("\nCantidad total:", len(cambios_df))
print("Aprobados:", (cambios_df["estado"] == "Aprobado").sum())
print("Rechazados:", (cambios_df["estado"] == "Rechazado").sum())
print("Pendientes:", (cambios_df["estado"] == "Pendiente").sum())
print("\nPor prioridad:")
print(cambios_df["prioridad"].value_counts())
print("\nRequisitos más modificados:")
print(cambios_df["requisito"].value_counts())

# Gráfico 1: cambios por estado
orden = ["Aprobado", "Rechazado", "Pendiente"]
conteo = cambios_df["estado"].value_counts().reindex(orden, fill_value=0)
plt.figure(figsize=(6,4))
conteo.plot(kind="bar")
plt.title("Cambios por estado")
plt.xlabel("Estado")
plt.ylabel("Cantidad")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Gráfico 2: cambios por prioridad
orden = ["Alta", "Media", "Baja"]
conteo = cambios_df["prioridad"].value_counts().reindex(orden, fill_value=0)
plt.figure(figsize=(6,4))
conteo.plot(kind="bar")
plt.title("Cambios por prioridad")
plt.xlabel("Prioridad")
plt.ylabel("Cantidad")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
