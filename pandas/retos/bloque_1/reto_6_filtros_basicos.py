"""Reto 6: Filtros basicos

Objetivo:
- Filtrar filas usando condiciones simples.

Instrucciones:
1) Filtra paises con population mayor a 200.
2) Filtra paises con area menor a 5.
3) Filtra con dos condiciones a la vez:
   - population > 100
   - area < 10
4) Imprime cada resultado.
"""

import pandas as pd

data = {
    "country": ["Brazil", "Russia", "India", "China", "South Africa"],
    "capital": ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
    "area": [8.516, 17.100, 3.286, 9.597, 1.221],
    "population": [200.4, 143.5, 1252.0, 1357.0, 52.98]
}

df = pd.DataFrame(data, index=["BR", "RU", "IN", "CH", "SA"])

# 1: filtro population > 200
print(df[df["population"] > 200])
# 2: filtro area < 5
print(df[df["area"] < 5])
# 3: filtro combinado con &
print(df[(df["population"] > 100) & (df["area"] < 10)])
# 4: imprime resultados
