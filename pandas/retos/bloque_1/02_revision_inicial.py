"""Reto 2: Revisar estructura inicial

Objetivo:
- Practicar revision inicial de un DataFrame real con mas detalle.

Instrucciones:
1) Carga el DataFrame desde jugadores_futbol.csv.
2) Muestra shape, columns, index y dtypes.
3) Muestra nulos por columna.
"""

from pathlib import Path

import pandas as pd

csv_path = Path(__file__).resolve().parents[3] / "data" / "pandas" / "jugadores_futbol.csv"
df = pd.read_csv(csv_path)

print(df.shape)
print(df.columns)
print(df.index)
print(df.dtypes)
print(df.isna().sum())
