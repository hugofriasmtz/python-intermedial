"""Reto 7: Eliminar duplicados con varias columnas

Objetivo:
- Usar drop_duplicates() con subset compuesto para definir unicidad por combinacion.

Instrucciones:
1) Carga el CSV de jugadores.
2) Elimina duplicados usando pais y posicion como criterio.
3) Compara cuantas filas hay antes y despues.
4) Muestra el resultado ordenado por pais y posicion.
"""

from pathlib import Path

import pandas as pd

csv_path = Path(__file__).resolve().parents[3] / "data" / "pandas" / "jugadores_futbol.csv"
df = pd.read_csv(csv_path)

sin_duplicados = df.drop_duplicates(subset=["pais", "posicion"]).sort_values(by=["pais", "posicion"])

print("Filas originales:", len(df))
print("Filas sin duplicados por pais y posicion:", len(sin_duplicados))
print(
    sin_duplicados[[
        "pais",
        "posicion",
        "nombre",
        "equipo",
        "goles",
        "valor_millones",
    ]]
)
