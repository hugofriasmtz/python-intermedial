# RETO 2: Gráfico de barras
# Compara pedidos entre categorías de productos

import matplotlib.pyplot as plt

# Datos
categorias = ["Cafe", "Te", "Postres", "Sandwiches"]
pedidos = [80, 45, 60, 35]

# Crea barras
plt.bar(categorias, pedidos)

# Títulos y etiquetas
plt.title("Pedidos por Categoria")
plt.xlabel("Categorias")
plt.ylabel("Pedidos")

# TAREA 4: Muestra el gráfico
plt.show()

# RESUMEN DE MÉTODOS USADOS:
# - plt.bar(categorias, valores): Crea barras - para qué: comparar valores en categorías
# - plt.title(): Agrega título - para qué: contexto
# - plt.xlabel(): Etiqueta eje X - para qué: claridad
# - plt.ylabel(): Etiqueta eje Y - para qué: claridad
# - plt.show(): Visualiza - para qué: ver el resultado

# DATO INTERESANTE:
# Líneas son para TENDENCIAS en el tiempo (plot)
# Barras son para COMPARACIONES entre categorías (bar)