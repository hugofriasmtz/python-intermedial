"""Reto 1: Carga y lectura inicial

Objetivo:
- Cargar el CSV real y comprobar que el DataFrame esta listo.

Instrucciones:
1) Carga data/pandas/jugadores_futbol.csv.
2) Muestra head(), tipo y shape.
3) Muestra tambien el nombre de las columnas.
"""

from pathlib import Path

import pandas as pd

csv_path = Path(__file__).resolve().parents[3] / "data" / "pandas" / "jugadores_futbol.csv"
df = pd.read_csv(csv_path)

print(df.head())
print(type(df))
print("shape:", df.shape)
print("columnas:", list(df.columns))
