"""Reto 00: Crear DataFrames y leer/escribir CSV

Objetivo:
- Practicar la creacion de DataFrames desde estructuras de Python.
- Leer y escribir archivos CSV reales de la carpeta data.

Instrucciones:
1) Crea un DataFrame desde una lista de diccionarios.
2) Crea otro DataFrame desde un diccionario de listas.
3) Lee el CSV real de la carpeta data.
4) Guarda una copia temporal de ese CSV.
5) Lee esa copia nuevamente.
5) Imprime los resultados con etiquetas claras.
"""

from pathlib import Path
import tempfile

import pandas as pd

lista_diccionarios = [
    {"nombre": "Ana", "edad": 28, "pais": "Mexico"},
    {"nombre": "Luis", "edad": 31, "pais": "Chile"},
    {"nombre": "Sofia", "edad": 26, "pais": "Colombia"},
]

diccionario_listas = {
    "nombre": ["Ana", "Luis", "Sofia"],
    "edad": [28, 31, 26],
    "pais": ["Mexico", "Chile", "Colombia"],
}

df_lista_diccionarios = pd.DataFrame(lista_diccionarios)
df_diccionario_listas = pd.DataFrame(diccionario_listas)

print("=== Seccion 1: DataFrames creados desde estructuras de Python ===")
print("DataFrame creado desde lista de diccionarios:")
print(df_lista_diccionarios)

print("\nDataFrame creado desde diccionario de listas:")
print(df_diccionario_listas)

print("\n=== Seccion 2: CSV reales de la carpeta data ===")

csv_origen = Path(__file__).resolve().parents[3] / "data" / "pandas" / "jugadores_futbol.csv"
df_csv_real = pd.read_csv(csv_origen)

print("\nCSV original leido desde data/pandas/jugadores_futbol.csv:")
print(df_csv_real.head())

with tempfile.TemporaryDirectory() as tmp_dir:
    csv_copia = Path(tmp_dir) / "jugadores_futbol_copia.csv"
    df_csv_real.to_csv(csv_copia, index=False)

    df_leido = pd.read_csv(csv_copia)

    print("\nCSV guardado temporalmente en:")
    print(csv_copia)

    print("\nCopia leida de nuevo con read_csv:")
    print(df_leido)

