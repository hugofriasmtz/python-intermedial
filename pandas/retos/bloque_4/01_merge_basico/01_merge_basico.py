"""Reto 1: Merge basico

Objetivo:
- Unir dos tablas por una clave comun.

Instrucciones:
1) Carga un CSV con la tabla principal de socios.
2) Crea una segunda tabla con los prestamos.
3) Une ambas tablas con `merge()` usando `id`.
"""

from pathlib import Path

import pandas as pd


base_path = Path(__file__).resolve().parents[4]
csv_path = base_path / "data" / "pandas" / "socios_biblioteca.csv"

socios = pd.read_csv(csv_path)

prestamos = pd.DataFrame(
    {
        "id": [1, 2, 4, 6],
        "libro": [
            "Cien anios de soledad",
            "La ciudad y los perros",
            "Rayuela",
            "El principito",
        ],
        "dias_prestamo": [7, 14, 10, 5],
    }
)

merge_inner = socios.merge(prestamos, on="id", how="inner")


print("Tabla de socios:")
print(socios)
print("\nTabla de prestamos:")
print(prestamos)
print("\nMerge inner (solo coincidencias):")
print(merge_inner)
