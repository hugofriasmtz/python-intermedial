"""Reto 2: Filtros combinados

Objetivo:
- Aplicar filtros con operadores logicos sobre jugadores.

Instrucciones:
1) Carga el CSV de jugadores.
2) Filtra titulares con goles >= 10.
3) Filtra jugadores de Mexico o Brasil que jueguen en Liga MX o Brasileirao.
4) Filtra jugadores cuyo nombre contenga la letra "a".
"""

from pathlib import Path

import pandas as pd

csv_path = Path(__file__).resolve().parents[3] / "data" / "pandas" / "jugadores_futbol.csv"
df = pd.read_csv(csv_path)

filtro_titulares_gol = df[(df["titular"] == True) & (df["goles"] >= 10)]
filtro_pais_liga = df[
    df["pais"].isin(["Mexico", "Brasil"])
    & df["liga"].isin(["Liga MX", "Brasileirao"])
]
filtro_nombre_a = df[df["nombre"].str.contains("a", case=False, na=False)]

print("Titulares con goles >= 10:")
print(filtro_titulares_gol[["nombre", "pais", "goles", "titular"]])
print("\nMexico o Brasil en Liga MX/Brasileirao:")
print(filtro_pais_liga[["nombre", "pais", "liga", "equipo"]])
print("\nNombres con letra 'a':")
print(filtro_nombre_a[["nombre", "pais", "equipo"]])
