"""Reto 7: Nulos basicos

Objetivo:
- Detectar y resumir valores nulos en el DataFrame.

Instrucciones:
1) Carga el CSV de jugadores.
2) Muestra que columnas tienen valores nulos.
3) Cuenta nulos por columna.
4) Muestra porcentaje de nulos por columna.
5) Imprime las columnas con algun nulo.
"""

from pathlib import Path

import pandas as pd

csv_path = Path(__file__).resolve().parents[3] / "data" / "pandas" / "jugadores_futbol.csv"
df = pd.read_csv(csv_path)

nulos = df.isna().sum()
porcentaje_nulos = (df.isna().mean() * 100).round(2)
columnas_con_nulos = nulos[nulos > 0]

print("Nulos por columna:")
print(nulos)

print("\nPorcentaje de nulos por columna:")
print(porcentaje_nulos)

print("\nColumnas con al menos un nulo:")
print(columnas_con_nulos)
