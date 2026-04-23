"""Reto 4: Resumen numerico del dataset

Objetivo:
- Dominar metodos de resumen basicos en columnas numericas.

Instrucciones:
1) Calcula sum, mean y median de la columna goles.
2) Calcula min y max de valor_millones.
3) Calcula count y nunique de la columna pais.
4) Imprime resultados con etiquetas claras.
"""

from pathlib import Path

import pandas as pd

csv_path = Path(__file__).resolve().parents[3] / "data" / "pandas" / "jugadores_futbol.csv"
df = pd.read_csv(csv_path)

print("sum goles:", df["goles"].sum())
print("mean goles:", df["goles"].mean())
print("median goles:", df["goles"].median())
print("min valor_millones:", df["valor_millones"].min())
print("max valor_millones:", df["valor_millones"].max())
print("count pais:", df["pais"].count())
print("nunique pais:", df["pais"].nunique())
