"""Reto 3: Groupby basico

Objetivo:
- Resumir jugadores por pais con metricas clave.

Instrucciones:
1) Carga el CSV de jugadores.
2) Agrupa por pais.
3) Calcula: total_goles, promedio_goles, jugadores.
4) Ordena el resultado final de mayor a menor.
"""

from pathlib import Path

import pandas as pd

csv_path = Path(__file__).resolve().parents[3] / "data" / "pandas" / "jugadores_futbol.csv"
df = pd.read_csv(csv_path)

resumen = (
    df.groupby("pais", as_index=False)
    .agg(
        total_goles=("goles", "sum"),
        promedio_goles=("goles", "mean"),
        jugadores=("id", "count"),
    )
    .sort_values(by="total_goles", ascending=False)
)

print("Resumen por pais (ordenado por total_goles desc):")
print(resumen)
