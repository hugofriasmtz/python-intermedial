"""Reto 2.3: Union externa.

Objetivo:
- Practicar `outer join` para conservar todas las filas de ambas tablas.
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

union_outer = df_socios.merge(
    df_sedes,
    left_on="id",
    right_on="id_socio",
    how="outer",
    indicator=True,
)

print("Union externa:")
print(union_outer)
print("\nConteo por origen:")
print(union_outer["_merge"].value_counts())