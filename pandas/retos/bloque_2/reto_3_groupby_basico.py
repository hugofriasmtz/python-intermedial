"""Reto 3: Groupby basico

Objetivo:
- Resumir datos por una categoria.

Instrucciones:
1) Crea el DataFrame con los datos.
2) Calcula ventas totales por region.
3) Calcula promedio de ventas por region.
4) Ordena el resultado final de mayor a menor.
"""

import pandas as pd

data = {
    "region": ["Norte", "Sur", "Norte", "Centro", "Sur", "Centro", "Norte"],
    "ventas": [1200, 850, 1430, 990, 1670, 1110, 920]
}

df = pd.DataFrame(data)

resumen = (
    df.groupby("region", as_index=False)
    .agg(ventas_totales=("ventas", "sum"), ventas_promedio=("ventas", "mean"))
    .sort_values(by="ventas_totales", ascending=False)
)

print("DataFrame original:")
print(df)
print("\nResumen por region (ordenado por ventas totales desc):")
print(resumen)
