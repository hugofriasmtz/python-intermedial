"""Reto 4: Barras comparativas

Objetivo:
- Comparar dos grupos de datos con barras agrupadas.

Instrucciones:
1) Crea un grafico de barras agrupadas.
2) Compara dos grupos en las mismas categorias.
3) Agrega titulo, ejes y leyenda.
4) Intenta que la lectura sea facil y limpia.

Pista:
- Piensa en un pequeno desplazamiento horizontal para separar las barras.
"""

import matplotlib.pyplot as plt

categorias = ["Cafe", "Te", "Postres", "Sandwiches"]
grupo_1 = [80, 45, 60, 35]
grupo_2 = [95, 50, 55, 40]

indices = list(range(len(categorias)))
ancho = 0.35

plt.figure(figsize=(8.5, 5))
plt.bar([i - ancho / 2 for i in indices], grupo_1, width=ancho, label="Grupo 1")
plt.bar([i + ancho / 2 for i in indices], grupo_2, width=ancho, label="Grupo 2")

plt.xticks(indices, categorias)
plt.title("Comparacion de ventas por categoria")
plt.xlabel("Categoria")
plt.ylabel("Ventas")
plt.legend()
plt.grid(axis="y", alpha=0.25)
plt.show()
