# RETO 7: Scatter (dispersión)
# Busca relaciones entre edad y gasto de clientes

import matplotlib.pyplot as plt
import random

# Datos: edad vs. gasto (con correlación)
random.seed(42)
n = 50
edad = [random.randint(18, 70) for _ in range(n)]
gasto = [5 + 0.15 * e + random.gauss(0, 3) for e in edad]
gasto = [max(1, g) for g in gasto]
frecuencia = [random.randint(1, 30) for _ in range(n)]

# Crea scatter
plt.figure(figsize=(10, 6))
scatter = plt.scatter(edad, gasto, s=100, c=frecuencia, cmap="viridis", 
                      alpha=0.6, edgecolors="black", linewidth=0.5)

# Barra de color
plt.colorbar(scatter, label="Visitas al mes")

# Títulos y etiquetas
plt.title("Relación entre Edad y Gasto en la Cafetería")
plt.xlabel("Edad (años)")
plt.ylabel("Gasto ($)")

# Grilla
plt.grid(alpha=0.3)
