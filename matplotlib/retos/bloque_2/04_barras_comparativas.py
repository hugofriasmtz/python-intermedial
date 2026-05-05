# RETO 4: Barras agrupadas
# Crea barras lado a lado para comparar dos períodos en 4 categorías

import matplotlib.pyplot as plt

# Datos
categorias = ["Cafe", "Te", "Postres", "Sandwiches"]
mes_1 = [80, 45, 60, 35]
mes_2 = [95, 50, 55, 40]

# Prepara índices y ancho
indices = list(range(len(categorias)))
ancho = 0.35

# Crea figura
plt.figure(figsize=(8.5, 5))

# Barras del Mes 1 desplazadas a la izquierda
plt.bar([i - ancho / 2 for i in indices], mes_1, width=ancho, label="Mes 1")

# Barras del Mes 2 desplazadas a la derecha
plt.bar([i + ancho / 2 for i in indices], mes_2, width=ancho, label="Mes 2")

# Títulos y etiquetas
plt.xticks(indices, categorias)
plt.title("Comparación de Ventas por Categoría")
plt.xlabel("Categoría")
plt.ylabel("Ventas ($)")

# Leyenda y grilla
plt.legend()
plt.grid(axis="y", alpha=0.25)
# - Barras simples: Una serie de datos
