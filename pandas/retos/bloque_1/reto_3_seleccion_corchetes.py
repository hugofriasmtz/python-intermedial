"""Reto 3: Seleccion con corchetes []

Objetivo:
- Seleccionar columnas y un rango simple de filas.

Instrucciones:
1) Selecciona una columna (Series): country.
2) Selecciona dos columnas (DataFrame): country y capital.
3) Selecciona filas con slicing [1:4].
4) Imprime cada resultado.
"""

import pandas as pd

data = {
    "country": ["Brazil", "Russia", "India", "China", "South Africa"],
    "capital": ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
    "population": [200.4, 143.5, 1252.0, 1357.0, 52.98]
}

df = pd.DataFrame(data, index=["BR", "RU", "IN", "CH", "SA"])

# TODO: una columna con []
country_series = df["country"]
print(country_series)
# TODO: dos columnas con [[]]
country_capital_df = df[["country", "capital"]]
print(country_capital_df)
# TODO: filas por slicing [1:4]
rows_slicing = df[1:4]
print(rows_slicing)

# TODO: imprime resultados
print("Columna 'country' como Series:")
print(country_series)
print("\nColumnas 'country' y 'capital' como DataFrame:")
print(country_capital_df)
print("\nFilas 1 a 3:")
print(rows_slicing)

