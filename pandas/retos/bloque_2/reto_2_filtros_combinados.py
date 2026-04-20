"""Reto 2: Filtros combinados

Objetivo:
- Aplicar filtros con operadores logicos.

Instrucciones:
1) Crea el DataFrame con los datos.
2) Filtra productos con precio > 50 y stock > 0.
3) Filtra productos de categoria 'Tecnologia' o 'Hogar'.
4) Filtra productos cuyo nombre contenga la letra 'a'.
"""

import pandas as pd

data = {
    "producto": ["Teclado", "Mouse", "Silla", "Lampara", "Monitor", "Cuaderno"],
    "categoria": ["Tecnologia", "Tecnologia", "Hogar", "Hogar", "Tecnologia", "Papeleria"],
    "precio": [45, 25, 90, 55, 220, 8],
    "stock": [10, 0, 6, 12, 4, 30]
}

df = pd.DataFrame(data)

filtro_precio_stock = df[(df["precio"] > 50) & (df["stock"] > 0)]
filtro_categoria = df[df["categoria"].isin(["Tecnologia", "Hogar"])]
filtro_nombre_con_a = df[df["producto"].str.contains("a", case=False, na=False)]

print("DataFrame original:")
print(df)
print("\nProductos con precio > 50 y stock > 0:")
print(filtro_precio_stock)
print("\nProductos de categoria Tecnologia o Hogar:")
print(filtro_categoria)
print("\nProductos cuyo nombre contiene la letra 'a':")
print(filtro_nombre_con_a)
