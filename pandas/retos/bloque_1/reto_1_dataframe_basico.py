"""Reto 1: Crear un DataFrame basico

Objetivo:
- Construir un DataFrame desde un diccionario.

Instrucciones:
1) Crea un diccionario con columnas: nombre, edad, ciudad.
2) Construye un DataFrame con pandas.
3) Imprime el DataFrame.
4) Imprime tambien el tipo de la variable creada.
"""

import pandas as pd

# TODO: crea el diccionario con datos
data = {
    "nombre": ["Hugo", "Felipe", "Karen", "Marcos"],
    "edad": [23, 52, 23, 29],
    "ciudad": ["Tehucan", "CDMX", "Puebla", "Paris"]
}
# TODO: construye el DataFrame
df = pd.DataFrame(data)
# TODO: imprime el DataFrame
print(df)
# TODO: imprime el tipo de la variable
print(type(df))
