"""Reto 5: Merge basico

Objetivo:
- Unir dos tablas por una clave comun.

Instrucciones:
1) Crea dos DataFrames a partir del CSV: base_jugadores y bonos.
2) Une ambos por `id`.
3) Prueba al menos dos tipos de merge (inner y left).
4) Compara resultados e indica que cambio entre ambos.
"""

from pathlib import Path

import pandas as pd

csv_path = Path(__file__).resolve().parents[3] / "data" / "pandas" / "jugadores_futbol.csv"
df = pd.read_csv(csv_path)

base_jugadores = df[["id", "nombre", "equipo", "goles"]].copy()

bonos = pd.DataFrame(
    {
        "id": [1, 3, 10, 21, 24, 31, 37, 46, 48],
        "bono_rendimiento": [0.5, 0.7, 1.1, 1.8, 1.3, 2.0, 2.4, 1.5, 1.2],
    }
)

merge_inner = pd.merge(base_jugadores, bonos, on="id", how="inner")
merge_left = pd.merge(base_jugadores, bonos, on="id", how="left")

print("Base jugadores:")
print(base_jugadores.head())
print("\nBonos:")
print(bonos)
print("\nMerge inner (solo coincidencias):")
print(merge_inner)
print("\nMerge left (todos los jugadores, con o sin bono):")
print(merge_left)
