"""Reto 5: Subconjunto y metrica derivada

Objetivo:
- Subir dificultad combinando seleccion, filtro y calculo nuevo.

Instrucciones:
1) Selecciona columnas: nombre, pais, goles, asistencias.
2) Filtra solo jugadores de Mexico.
3) Crea una columna nueva llamada contribucion = goles + asistencias.
4) Ordena por contribucion de mayor a menor y muestra top 10.
"""

from pathlib import Path

import pandas as pd

csv_path = Path(__file__).resolve().parents[3] / "data" / "pandas" / "jugadores_futbol.csv"
df = pd.read_csv(csv_path)

subset = df[["nombre", "pais", "goles", "asistencias"]]
mexico = subset[subset["pais"] == "Mexico"].copy()
mexico["contribucion"] = mexico["goles"] + mexico["asistencias"]

top_10_mex = mexico.sort_values(by="contribucion", ascending=False).head(10)
print(top_10_mex)
