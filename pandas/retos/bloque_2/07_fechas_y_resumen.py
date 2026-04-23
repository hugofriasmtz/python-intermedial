"""Reto 7: Fechas y resumen mensual

Objetivo:
- Crear una columna de fecha, convertirla y resumir por mes.

Instrucciones:
1) Carga el CSV de jugadores.
2) Crea una columna `fecha_evento` sintetica a partir del id.
3) Convierte `fecha_evento` a datetime.
4) Crea una columna `mes` a partir de la fecha.
5) Resume goles totales por mes.
6) Ordena el resultado por mes.
"""

from pathlib import Path

import pandas as pd

csv_path = Path(__file__).resolve().parents[3] / "data" / "pandas" / "jugadores_futbol.csv"
df = pd.read_csv(csv_path)

# Genera una fecha semanal iniciando en 2025-01-01 para simular eventos.
df["fecha_evento"] = pd.to_datetime("2025-01-01") + pd.to_timedelta(df["id"] * 7, unit="D")
df["mes"] = df["fecha_evento"].dt.to_period("M").astype(str)

resumen_mensual = (
    df.groupby("mes", as_index=False)["goles"]
    .sum()
    .rename(columns={"goles": "goles_totales"})
    .sort_values(by="mes", ascending=True)
)

print("Resumen mensual de goles:")
print(resumen_mensual)

# Resumen adicional de la columna goles.
print("\nResumen de goles:")
print("sum:", df["goles"].sum())
print("mean:", df["goles"].mean())
print("median:", df["goles"].median())
print("min:", df["goles"].min())
print("max:", df["goles"].max())
print("count:", df["goles"].count())
print("nunique:", df["goles"].nunique())
