# RETO 5: Múltiples series (4 líneas)
# Grafica 4 categorías de productos en la misma figura

import matplotlib.pyplot as plt

# Datos de ventas por categoría
meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun"]
cafe = [100, 120, 110, 140, 160, 150]
te = [60, 65, 70, 75, 80, 78]
postres = [80, 85, 90, 95, 100, 98]
sandwiches = [50, 55, 60, 65, 70, 72]

# Crea figura
plt.figure(figsize=(11, 6))

# 4 líneas con colores, estilos y marcadores diferentes
plt.plot(meses, cafe, color="tab:blue", linestyle="-", marker="o", label="Café")
plt.plot(meses, te, color="tab:orange", linestyle="--", marker="s", label="Té")
plt.plot(meses, postres, color="tab:green", linestyle="-.", marker="^", label="Postres")
plt.plot(meses, sandwiches, color="tab:red", linestyle=":", marker="D", label="Sandwiches")

# Títulos y etiquetas
plt.title("Ventas por Categoría - Comparación Completa")
plt.xlabel("Mes")
plt.ylabel("Ventas")

# Grilla y leyenda
plt.grid(alpha=0.35, linestyle="--")
plt.legend(loc="upper left")
