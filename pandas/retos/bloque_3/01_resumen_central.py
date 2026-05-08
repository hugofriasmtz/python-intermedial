"""Reto 1: Resumen central de una Series

Objetivo:
- Comparar medidas de tendencia central y cuantiles en una columna numerica.

Instrucciones:
1) Carga el CSV de jugadores.
2) Calcula sum, mean, median y mode de la columna goles.
3) Calcula min, max y quantile(0.25), quantile(0.5), quantile(0.75).
4) Imprime resultados con etiquetas claras.
"""

from pathlib import Path

import pandas as pd

csv_path = Path(__file__).resolve().parents[3] / "data" / "pandas" / "jugadores_futbol.csv"
df = pd.read_csv(csv_path)

goles = df["goles"]

print("sum goles:", goles.sum())
print("mean goles:", goles.mean())
print("median goles:", goles.median())
print("mode goles:", list(goles.mode()))
print("min goles:", goles.min())
print("max goles:", goles.max())
print("quantile 0.25:", goles.quantile(0.25))
print("quantile 0.5:", goles.quantile(0.5))
print("quantile 0.75:", goles.quantile(0.75))
