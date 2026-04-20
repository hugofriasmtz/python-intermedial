"""Reto 5: Merge basico

Objetivo:
- Unir dos tablas por una clave comun.

Instrucciones:
1) Crea dos DataFrames: clientes y pedidos.
2) Une ambos por `cliente_id`.
3) Prueba al menos dos tipos de merge (inner y left).
4) Compara resultados e indica que cambio entre ambos.
"""

import pandas as pd

clientes_data = {
    "cliente_id": [1, 2, 3, 4],
    "nombre": ["Ana", "Luis", "Carla", "Pedro"],
    "ciudad": ["Bogota", "Quito", "Santiago", "Lima"]
}

pedidos_data = {
    "pedido_id": [101, 102, 103, 104, 105],
    "cliente_id": [1, 2, 2, 4, 5],
    "monto": [200, 150, 300, 180, 90]
}

clientes = pd.DataFrame(clientes_data)
pedidos = pd.DataFrame(pedidos_data)

merge_inner = pd.merge(clientes, pedidos, on="cliente_id", how="inner")
merge_left = pd.merge(clientes, pedidos, on="cliente_id", how="left")

print("Clientes:")
print(clientes)
print("\nPedidos:")
print(pedidos)
print("\nMerge inner (solo coincidencias en ambas tablas):")
print(merge_inner)
print("\nMerge left (todos los clientes, tengan o no pedidos):")
print(merge_left)
