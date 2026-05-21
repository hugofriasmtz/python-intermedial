"""Reto 5: Counting normalizado

Objetivo:
- Comparar frecuencias absolutas y relativas.

Instrucciones:
1) Carga el CSV de jugadores.
2) Calcula value_counts(sort=True) para la columna posicion.
3) Calcula value_counts(normalize=True) para la misma columna.
4) Convierte el resultado normalizado a porcentaje si quieres leerlo mejor.
"""

from pathlib import Path

import pandas as pd

csv_path = Path(__file__).resolve().parents[3] / "data" / "pandas" / "jugadores_futbol.csv"
df = pd.read_csv(csv_path)

conteo_posiciones = df["posicion"].value_counts(sort=True)
porcentaje_posiciones = (df["posicion"].value_counts(normalize=True) * 100).round(2)

print("Conteo ordenado de posiciones:")
print(conteo_posiciones)

print("\nPorcentaje de posiciones:")
print(porcentaje_posiciones)
