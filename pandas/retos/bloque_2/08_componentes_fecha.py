"""Reto 8: Componentes de fecha con .dt

Objetivo:
- Practicar el uso de .dt para extraer partes de una fecha.

Instrucciones:
1) Carga el CSV de jugadores.
2) Crea una columna fecha_evento sintetica a partir del id.
3) Convierte fecha_evento a datetime.
4) Extrae ano, mes, dia, trimestre y dia de la semana.
5) Muestra las columnas creadas.
"""

from pathlib import Path

import pandas as pd

csv_path = Path(__file__).resolve().parents[3] / "data" / "pandas" / "jugadores_futbol.csv"
df = pd.read_csv(csv_path)

# Se crea una fecha ficticia para poder practicar accesores .dt.
df["fecha_evento"] = pd.to_datetime("2025-01-01") + pd.to_timedelta(df["id"] * 7, unit="D")

# Extrae componentes de la fecha para resumir y comparar.
df["anio"] = df["fecha_evento"].dt.year
df["mes"] = df["fecha_evento"].dt.month
df["dia"] = df["fecha_evento"].dt.day
df["trimestre"] = df["fecha_evento"].dt.quarter
df["nombre_dia"] = df["fecha_evento"].dt.day_name()
df["semana_iso"] = df["fecha_evento"].dt.isocalendar().week

print("Componentes de fecha:")
print(
    df[[
        "id",
        "nombre",
        "fecha_evento",
        "anio",
        "mes",
        "dia",
        "trimestre",
        "nombre_dia",
        "semana_iso",
    ]]
)

# Ejemplo extra de ordenamiento temporal.
print("\nJugadores ordenados por fecha_evento:")
print(df.sort_values(by="fecha_evento")[["nombre", "fecha_evento", "anio", "mes", "dia"]])
