"""Reto 6: Pivot table

Objetivo:
- Resumir informacion cruzando filas y columnas.

Instrucciones:
1) Crea el DataFrame con ventas por mes y categoria.
2) Construye una tabla dinamica:
   - index: mes
   - columns: categoria
   - values: ventas
   - aggfunc: suma
3) Completa faltantes con 0.
"""

import pandas as pd

data = {
    "mes": ["Ene", "Ene", "Feb", "Feb", "Mar", "Mar", "Mar"],
    "categoria": ["Tecnologia", "Hogar", "Tecnologia", "Hogar", "Tecnologia", "Hogar", "Papeleria"],
    "ventas": [500, 300, 650, 280, 700, 320, 120]
}

df = pd.DataFrame(data)

tabla_pivot = pd.pivot_table(
    df,
    index="mes",
    columns="categoria",
    values="ventas",
    aggfunc="sum",
    fill_value=0,
)

print("DataFrame original:")
print(df)
print("\nTabla dinamica de ventas por mes y categoria:")
print(tabla_pivot)
