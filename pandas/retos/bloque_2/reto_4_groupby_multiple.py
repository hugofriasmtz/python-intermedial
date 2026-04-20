"""Reto 4: Groupby con multiples agregaciones

Objetivo:
- Aplicar varias metricas sobre una agrupacion.

Instrucciones:
1) Crea el DataFrame con los datos.
2) Agrupa por categoria.
3) Calcula para `precio`: promedio, maximo y minimo.
4) Calcula para `stock`: suma total.
5) Renombra columnas para que se entiendan mejor.
"""

import pandas as pd

data = {
    "categoria": ["Tecnologia", "Tecnologia", "Hogar", "Hogar", "Tecnologia", "Papeleria"],
    "precio": [45, 25, 90, 55, 220, 8],
    "stock": [10, 0, 6, 12, 4, 30]
}

df = pd.DataFrame(data)

resumen = (
    df.groupby("categoria")
    .agg({"precio": ["mean", "max", "min"], "stock": "sum"})
    .reset_index()
)

resumen.columns = [
    "categoria",
    "precio_promedio",
    "precio_maximo",
    "precio_minimo",
    "stock_total",
]

print("DataFrame original:")
print(df)
print("\nResumen por categoria:")
print(resumen)
