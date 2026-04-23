"""Reto 3: Seleccion con corchetes []

Objetivo:
- Seleccionar columnas, filas y ordenar un subconjunto.

Instrucciones:
1) Selecciona una columna (Series): nombre.
2) Selecciona tres columnas (DataFrame): nombre, equipo y goles.
3) Selecciona filas con slicing [1:4].
4) Ordena ese subconjunto por goles de mayor a menor.
5) Imprime cada resultado.
"""

from pathlib import Path

import pandas as pd

csv_path = Path(__file__).resolve().parents[3] / "data" / "pandas" / "jugadores_futbol.csv"
df = pd.read_csv(csv_path)


nombre_series = df["nombre"]

nombre_equipo_goles_df = df[["nombre", "equipo", "goles"]]

rows_slicing = df[1:4]
rows_slicing_ordenado = rows_slicing.sort_values(by="goles", ascending=False)


print("Columna 'nombre' como Series:")
print(nombre_series)
print("\nColumnas 'nombre', 'equipo' y 'goles' como DataFrame:")
print(nombre_equipo_goles_df)
print("\nFilas 1 a 3:")
print(rows_slicing)
print("\nFilas 1 a 3 ordenadas por goles (desc):")
print(rows_slicing_ordenado)

