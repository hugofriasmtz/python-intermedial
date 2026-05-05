# RETO 3: Superponer dos series de barras
# Compara ventas de dos meses usando transparencia (alpha)

import matplotlib.pyplot as plt

# Datos
categorias = ["Cafe", "Te", "Postres", "Sandwiches"]
mes_1 = [80, 45, 60, 35]
mes_2 = [95, 50, 55, 40]

# Crea primera barra (70% opaca)
plt.bar(categorias, mes_1, label="Mes 1", alpha=0.7)

# Crea segunda barra (70% opaca)
plt.bar(categorias, mes_2, label="Mes 2", alpha=0.7)

# Títulos y etiquetas
plt.title("Comparacion de Ventas por Mes")
plt.xlabel("Categorias")
plt.ylabel("Ventas")

# Muestra leyenda para identificar cada serie
plt.legend()