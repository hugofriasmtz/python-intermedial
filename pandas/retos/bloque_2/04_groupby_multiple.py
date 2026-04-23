"""Reto 4: Groupby con multiples agregaciones

Objetivo:
- Aplicar varias metricas sobre agrupacion doble.

Instrucciones:
1) Carga el CSV de jugadores.
2) Agrupa por pais y posicion.
3) Calcula para goles: promedio, maximo y suma.
4) Calcula para valor_millones: promedio.
5) Renombra columnas para que se entiendan mejor.
"""

from pathlib import Path

import pandas as pd

csv_path = Path(__file__).resolve().parents[3] / "data" / "pandas" / "jugadores_futbol.csv"
df = pd.read_csv(csv_path)

resumen = (
    df.groupby(["pais", "posicion"])
    .agg({"goles": ["mean", "max", "sum"], "valor_millones": "mean"})
    .reset_index()
)

resumen.columns = [
    "pais",
    "posicion",
    "goles_promedio",
    "goles_maximos",
    "goles_totales",
    "valor_promedio_millones",
]

resumen = resumen.sort_values(by="goles_totales", ascending=False)

print("Resumen por pais y posicion:")
print(resumen)
