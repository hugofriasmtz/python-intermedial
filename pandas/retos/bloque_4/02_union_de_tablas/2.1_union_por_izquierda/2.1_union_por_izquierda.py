"""Reto 2.1: Union por izquierda.

Objetivo:
- Practicar `left join` con llaves de distinto nombre, columnas repetidas e indicador de origen.
"""

from pathlib import Path

import pandas as pd


base_path = Path(__file__).resolve().parents[5]
csv_path = base_path / "data" / "pandas" / "socios_biblioteca.csv"

df_socios = pd.read_csv(csv_path)

df_sedes = pd.DataFrame(
    {
        "id_socio": [1, 2, 4, 6],
        "sede": ["Centro", "Norte", "Sur", "Oriente"],
    }
)

df_sucursales = pd.DataFrame(
    {
        "socio_id": [1, 2, 4],
        "ciudad": ["Ciudad de Mexico", "Guadalajara", "Tijuana"],
        "area": ["Centro", "Norte", "Sur"],
    }
)

union_left = df_socios.merge(
    df_sedes,
    left_on="id",
    right_on="id_socio",
    how="left",
    indicator=True,
)

union_con_sufijos = df_socios.merge(
    df_sucursales,
    left_on="id",
    right_on="socio_id",
    how="left",
    suffixes=("_socio", "_sucursal"),
)

print("Union por izquierda:")
print(union_left)
print("\nOrigen de filas:")
print(union_left["_merge"].value_counts())
print("\nUnion con suffixes:")
print(union_con_sufijos)