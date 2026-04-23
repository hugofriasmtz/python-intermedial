"""Reto 1: Ordenamiento y Top N

Objetivo:
- Ordenar jugadores por distintas metricas y obtener top N.

Instrucciones:
1) Carga el CSV de jugadores.
2) Ordena por goles (descendente) y luego por valor_millones (descendente).
3) Muestra top 10 general.
4) Muestra top 5 de jugadores mexicanos por goles.
"""

from pathlib import Path

import pandas as pd

csv_path = Path(__file__).resolve().parents[3] / "data" / "pandas" / "jugadores_futbol.csv"
df = pd.read_csv(csv_path)

ordenado = df.sort_values(by=["goles", "valor_millones"], ascending=[False, False])
top_10 = ordenado.head(10)
top_5_mex = ordenado[ordenado["pais"] == "Mexico"].head(5)

print("Top 10 general por goles y valor:")
print(top_10[["nombre", "pais", "goles", "valor_millones"]])
print("\nTop 5 Mexico por goles:")
print(top_5_mex[["nombre", "equipo", "goles", "valor_millones"]])
