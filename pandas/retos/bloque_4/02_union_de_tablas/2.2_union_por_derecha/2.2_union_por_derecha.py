"""Reto 2.2: Union por derecha.

Objetivo:
- Practicar `right join` conservando toda la tabla derecha.
"""

from pathlib import Path

import pandas as pd


base_path = Path(__file__).resolve().parents[5]
csv_path = base_path / "data" / "pandas" / "bloque_4_union_tablas" / "socios_biblioteca.csv"

df_socios = pd.read_csv(csv_path)

df_sedes = pd.DataFrame(
    {
        "id_socio": [1, 2, 4, 6],
        "sede": ["Centro", "Norte", "Sur", "Oriente"],
    }
)

union_right = df_socios.merge(
    df_sedes,
    left_on="id",
    right_on="id_socio",
    how="right",
    indicator=True,
)

print("Union por derecha:")
print(union_right)
print("\nFilas solo de la derecha:")
print(union_right[union_right["_merge"] == "right_only"])