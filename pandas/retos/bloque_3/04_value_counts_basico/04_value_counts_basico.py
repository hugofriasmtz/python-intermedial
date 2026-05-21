"""Reto 4: Counting basico

Objetivo:
- Contar cuantas veces aparece cada categoria en una columna.

Instrucciones:
1) Carga el CSV de jugadores.
2) Usa value_counts() sobre la columna posicion.
3) Usa value_counts() sobre la columna pais.
4) Imprime ambos resultados.
"""

from pathlib import Path

import pandas as pd

csv_path = Path(__file__).resolve().parents[3] / "data" / "pandas" / "jugadores_futbol.csv"
df = pd.read_csv(csv_path)

print("Frecuencia de posiciones:")
print(df["posicion"].value_counts())

print("\nFrecuencia de paises:")
print(df["pais"].value_counts())
