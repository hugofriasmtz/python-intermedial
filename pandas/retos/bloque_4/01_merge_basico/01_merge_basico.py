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
data_path = base_path / "data" / "pandas" / "bloque_4_union_tablas"
csv_socios_path = data_path / "socios_biblioteca.csv"
csv_prestamos_path = data_path / "prestamos_biblioteca.csv"

socios = pd.read_csv(csv_socios_path)
prestamos = pd.read_csv(csv_prestamos_path)

merge_inner = socios.merge(prestamos, on="id", how="inner")


print("Tabla de socios:")
print(socios)
print("\nTabla de prestamos:")
print(prestamos)
print("\nMerge inner (solo coincidencias):")
print(merge_inner)
