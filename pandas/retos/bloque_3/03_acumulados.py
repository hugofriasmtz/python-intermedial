"""Reto 3: Estadisticas acumuladas

Objetivo:
- Seguir la evolucion de una serie fila por fila con cummax, cummin y cumprod.

Instrucciones:
1) Carga el CSV de jugadores.
2) Ordena por id para mantener una secuencia estable.
3) Calcula cummax y cummin sobre goles.
4) Crea un factor de crecimiento simple y calcula su cumprod.
5) Muestra las columnas relevantes.
"""

from pathlib import Path

import pandas as pd

csv_path = Path(__file__).resolve().parents[3] / "data" / "pandas" / "jugadores_futbol.csv"
df = pd.read_csv(csv_path).sort_values(by="id").copy()

df["factor_crecimiento"] = 1 + (df["goles"] / 100)
df["goles_max_acumulado"] = df["goles"].cummax()
df["goles_min_acumulado"] = df["goles"].cummin()
df["factor_acumulado"] = df["factor_crecimiento"].cumprod()

print("Evolucion acumulada:")
print(
    df[[
        "id",
        "nombre",
        "goles",
        "goles_max_acumulado",
        "goles_min_acumulado",
        "factor_crecimiento",
        "factor_acumulado",
    ]]
)
