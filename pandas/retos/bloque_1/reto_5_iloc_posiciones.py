"""Reto 5: Seleccion con iloc (posiciones)

Objetivo:
- Seleccionar datos por posicion numerica.

Instrucciones:
1) Selecciona una fila por posicion: 1.
2) Selecciona varias filas: 1, 2, 3.
3) Selecciona columnas por posicion: 0 y 1.
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

# TODO: df.iloc[[1]]
# TODO: df.iloc[[1, 2, 3]]
# TODO: df.iloc[:, [0, 1]]
# TODO: df.iloc[[1, 2, 3], [0, 1]]
