"""Reto 6: Eliminar duplicados con una sola columna

Objetivo:
- Usar drop_duplicates() para quedarte con una fila por valor unico.

Instrucciones:
1) Carga el CSV de jugadores.
2) Elimina duplicados usando la columna equipo como referencia.
3) Compara cuantas filas hay antes y despues.
4) Muestra el resultado con columnas utiles.
"""

from pathlib import Path

import pandas as pd

csv_path = Path(__file__).resolve().parents[3] / "data" / "pandas" / "jugadores_futbol.csv"
df = pd.read_csv(csv_path)

sin_duplicados = df.drop_duplicates(subset="equipo")

print("Filas originales:", len(df))
print("Filas sin duplicados por equipo:", len(sin_duplicados))
print(
    sin_duplicados[[
        "equipo",
        "nombre",
        "pais",
        "posicion",
        "goles",
    ]]
)
