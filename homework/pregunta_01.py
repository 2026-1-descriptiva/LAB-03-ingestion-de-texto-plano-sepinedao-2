"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""


def pregunta_01():
    
    import pandas as pd

    with open("files/input/clusters_report.txt", "r", encoding="utf-8") as file:
        lineas = file.readlines()

    datos = []
    fila_actual = None

    for linea in lineas:
        linea = linea.strip()

        if linea == "":
            continue

        if linea.startswith("-"):
            continue

        partes = linea.split()

        if len(partes) == 0:
            continue

        primera_parte = partes[0]

        if primera_parte.isdigit():
            if fila_actual is not None:
                datos.append(fila_actual)

            cluster = int(partes[0])
            cantidad = int(partes[1])
            porcentaje_texto = float(partes[2].replace(",", "."))
            palabras_clave = ""

            for palabra in partes[4:]:
                palabras_clave = palabras_clave + " " + palabra

            palabras_clave = palabras_clave.strip()

            fila_actual = {
                "cluster": cluster,
                "cantidad_de_palabras_clave": cantidad,
                "porcentaje_de_palabras_clave": porcentaje_texto,
                "principales_palabras_clave": palabras_clave,
            }

        else:
            if fila_actual is not None:
                texto_adicional = " ".join(partes)
                fila_actual["principales_palabras_clave"] = (
                    fila_actual["principales_palabras_clave"] + " " + texto_adicional
                )

    if fila_actual is not None:
        datos.append(fila_actual)

    for fila in datos:
        texto = fila["principales_palabras_clave"]

        palabras = texto.split()
        texto_limpio = " ".join(palabras)

        partes = texto_limpio.split(",")
        partes_limpias = []

        for parte in partes:
            partes_limpias.append(parte.strip())

        texto_limpio = ", ".join(partes_limpias)

        if texto_limpio.endswith("."):
            texto_limpio = texto_limpio[:-1]

        fila["principales_palabras_clave"] = texto_limpio

    dataframe = pd.DataFrame(datos)

    return dataframe
"""
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """


print(pregunta_01())