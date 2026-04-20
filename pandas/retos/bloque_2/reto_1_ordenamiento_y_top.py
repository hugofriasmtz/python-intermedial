"""Reto 1: Ordenamiento y Top N

Objetivo:
- Ordenar datos y obtener los registros mas altos.

Instrucciones:
1) Crea el DataFrame con los datos.
2) Ordena por la columna `ventas` de mayor a menor.
3) Obtén el top 3 de vendedores por ventas.
4) Imprime resultados intermedios.
"""

import pandas as pd

data = {
    "vendedor": ["Ana", "Luis", "Carla", "Pedro", "Sofia", "Mario"],
    "ventas": [1200, 850, 1430, 990, 1670, 1110],
    "region": ["Norte", "Sur", "Norte", "Centro", "Sur", "Centro"]
}

df = pd.DataFrame(data)

ordenado = df.sort_values(by="ventas", ascending=False)
top_3 = ordenado.head(3)

print("DataFrame original:")
print(df)
print("\nVentas ordenadas (desc):")
print(ordenado)
print("\nTop 3 vendedores por ventas:")
print(top_3)
