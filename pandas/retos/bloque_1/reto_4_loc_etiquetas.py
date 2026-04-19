"""Reto 4: Seleccion con loc (etiquetas)

Objetivo:
- Seleccionar datos por nombre de indice y columna.

Instrucciones:
1) Selecciona una fila por etiqueta: RU.
2) Selecciona varias filas: RU, IN, CH.
3) Selecciona columnas country y capital para todas las filas.
4) Selecciona filas y columnas al mismo tiempo.
"""

import pandas as pd

data = {
    "country": ["Brazil", "Russia", "India", "China", "South Africa"],
    "capital": ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
    "area": [8.516, 17.100, 3.286, 9.597, 1.221],
    "population": [200.4, 143.5, 1252.0, 1357.0, 52.98]
}

df = pd.DataFrame(data, index=["BR", "RU", "IN", "CH", "SA"])

# 1
print(df.loc[["RU"]])
# 2
print(df.loc[["RU", "IN", "CH"]])
# 3
print(df.loc[:, ["country", "capital"]])
# 4
print(df.loc[["RU", "IN", "CH"], ["country", "capital"]])
