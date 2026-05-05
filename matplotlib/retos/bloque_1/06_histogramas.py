# RETO 6: Histogramas
# Visualiza la distribución de tiempos de permanencia de clientes

import matplotlib.pyplot as plt
import random

# Datos: tiempo de permanencia de 100 clientes (en minutos)
random.seed(42)
tiempo_clientes = [random.gauss(30, 10) for _ in range(100)]
tiempo_clientes = [t for t in tiempo_clientes if t > 0]

# Crea histograma
plt.figure(figsize=(10, 5))
plt.hist(tiempo_clientes, bins=10, color="tab:cyan", edgecolor="black", alpha=0.7)

# Títulos y etiquetas
plt.title("Distribución del Tiempo de Permanencia")
plt.xlabel("Tiempo (minutos)")
plt.ylabel("Cantidad de clientes")

# Grilla
plt.grid(alpha=0.3, axis="y")
