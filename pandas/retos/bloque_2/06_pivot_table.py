"""Reto 6: Pivot table

Objetivo:
- Resumir informacion cruzando filas y columnas.

Instrucciones:
1) Carga el CSV de jugadores.
2) Construye una tabla dinamica:
   - index: pais
   - columns: posicion
   - values: goles
   - aggfunc: suma
3) Completa faltantes con 0.
"""

from pathlib import Path

import pandas as pd

csv_path = Path(__file__).resolve().parents[3] / "data" / "pandas" / "jugadores_futbol.csv"
df = pd.read_csv(csv_path)

tabla_pivot = pd.pivot_table(
    df,
    index="pais",
    columns="posicion",
    values="goles",
    aggfunc="sum",
    fill_value=0,
)

print("Tabla dinamica de goles por pais y posicion:")
print(tabla_pivot)
