"""Reto 6: Filtros basicos

Objetivo:
- Filtrar filas con condiciones combinadas y analizar resultados.

Instrucciones:
1) Filtra jugadores con goles > 10.
2) Filtra jugadores mexicanos con edad < 30.
3) Filtra jugadores que sean titulares y valor_millones >= 10.
4) Del filtro 3, ordena por valor_millones desc y muestra top 8.
"""

from pathlib import Path

import pandas as pd

csv_path = Path(__file__).resolve().parents[3] / "data" / "pandas" / "jugadores_futbol.csv"
df = pd.read_csv(csv_path)

# 1: filtro goles > 10
filtro_goles = df[df["goles"] > 10]
print("Jugadores con goles > 10")
print(filtro_goles)

filtro_mex_joven = df[(df["pais"] == "Mexico") & (df["edad"] < 30)]
print("\nMexicanos menores de 30")
print(filtro_mex_joven)

filtro_titulares_valor = df[(df["titular"] == True) & (df["valor_millones"] >= 10)]
top_8_valor = filtro_titulares_valor.sort_values(by="valor_millones", ascending=False).head(8)
print("\nTitulares con valor >= 10 (top 8 por valor)")
print(top_8_valor)
