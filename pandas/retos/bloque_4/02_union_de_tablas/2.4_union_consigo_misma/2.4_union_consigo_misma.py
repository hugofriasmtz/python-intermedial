"""Reto 2.4: Union consigo misma.

Objetivo:
- Practicar un self-join usando una columna que apunta a otra fila de la misma tabla.
"""

from pathlib import Path

import pandas as pd


base_path = Path(__file__).resolve().parents[5]
csv_path = base_path / "data" / "pandas" / "socios_biblioteca.csv"

df_socios = pd.read_csv(csv_path)

df_socios["referido_por"] = [None, 1, 1, 2, 2, 3, 4]

df_referentes = df_socios.rename(
    columns={
        "id": "id_referente",
        "nombre": "nombre_referente",
        "ciudad": "ciudad_referente",
        "membresia": "membresia_referente",
    }
)

union_self = df_socios.merge(
    df_referentes,
    left_on="referido_por",
    right_on="id_referente",
    how="left",
    indicator=True,
)

print("Self join:")
print(
    union_self[
        [
            "id",
            "nombre",
            "referido_por",
            "nombre_referente",
            "_merge",
        ]
    ]
)