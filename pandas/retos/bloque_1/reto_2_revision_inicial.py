"""Reto 2: Revisar estructura inicial

Objetivo:
- Practicar revision inicial de un DataFrame.

Instrucciones:
1) Crea el DataFrame usando los datos de ejemplo.
2) Muestra shape, columns, index y head().
"""

import pandas as pd

data = {
    "country": ["Brazil", "Russia", "India", "China", "South Africa"],
    "capital": ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
    "population": [200.4, 143.5, 1252.0, 1357.0, 52.98]
}
# Index personalizado con codigos de paises es como una etiqueta para
#  cada fila, en lugar de usar numeros secuenciales.
df = pd.DataFrame(data, index=["BR", "RU", "IN", "CH", "SA"])

# TODO: muestra df.shape
print(df.shape) 
# TODO: muestra df.columns
print(df.columns)
# TODO: muestra df.index
print(df.index)
# TODO: muestra df.head()
print(df.head())
