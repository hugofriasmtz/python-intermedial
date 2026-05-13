"""Reto 3: Seleccion con corchetes, .loc e .iloc

Objetivo:
- Seleccionar columnas, filas y comparar .loc con .iloc.

Instrucciones:
1) Selecciona una columna (Series): nombre.
2) Selecciona tres columnas (DataFrame): nombre, equipo y goles.
3) Selecciona filas con .loc y .iloc para ver la diferencia entre etiqueta y posicion.
4) Ordena un subconjunto por goles de mayor a menor.
5) Imprime cada resultado con etiquetas claras.
"""

from pathlib import Path

import pandas as pd

csv_path = Path(__file__).resolve().parents[3] / "data" / "pandas" / "jugadores_futbol.csv"
df = pd.read_csv(csv_path)

df_indexado = df.set_index("nombre")

nombre_series = df["nombre"]

nombre_equipo_goles_df = df[["nombre", "equipo", "goles"]]

filas_loc = df_indexado.loc["Carlos Montes":"Alexis Vega", ["equipo", "goles"]]
filas_iloc = df.iloc[0:3][["nombre", "equipo", "goles"]]

subconjunto = df[["nombre", "equipo", "goles"]].sort_values(by="goles", ascending=False)
subconjunto_top = subconjunto.head(5)


print("Columna 'nombre' como Series:")
print(nombre_series)
print("\nColumnas 'nombre', 'equipo' y 'goles' como DataFrame:")
print(nombre_equipo_goles_df)
print("\nFilas seleccionadas con .loc (por etiqueta de nombre):")
print(filas_loc)
print("\nFilas seleccionadas con .iloc (por posicion):")
print(filas_iloc)
print("\nSubconjunto ordenado por goles (top 5):")
print(subconjunto_top)

