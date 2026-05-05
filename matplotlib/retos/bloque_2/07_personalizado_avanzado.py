# RETO 7: Personalización avanzada
# Crea una gráfica profesional con diseño pulido

import matplotlib.pyplot as plt

# Datos: ventas reales vs. proyección
meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun"]
ventas_reales = [120, 135, 128, 155, 180, 172]
proyeccion = [125, 130, 140, 150, 165, 170]

# Crea figura
fig, ax = plt.subplots(figsize=(12, 7), dpi=100)

# Grafica series
ax.plot(meses, ventas_reales, marker="o", linewidth=2.5, 
        color="tab:blue", label="Ventas Reales")

ax.plot(meses, proyeccion, marker="s", linewidth=2, linestyle="--", 
        color="tab:orange", label="Proyección")

# Grid refinado
ax.grid(alpha=0.25, linestyle="-", linewidth=0.5)
ax.set_axisbelow(True)

# Personaliza bordes (spines)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_color("gray")
ax.spines["bottom"].set_color("gray")

# Personaliza ticks
ax.tick_params(axis="both", which="major", labelsize=10)
ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position("left")

# Caja de texto anotativa
ax.text(0.02, 0.95, "Q1 2024: Análisis de desempeño",
        transform=ax.transAxes, fontsize=11, verticalalignment="top",
        bbox=dict(boxstyle="round,pad=0.7", facecolor="lightyellow", 
                  edgecolor="black", linewidth=1.5))

# Leyenda profesional
ax.legend(loc="lower right", framealpha=0.95, shadow=True, fontsize=11)

# Títulos y etiquetas
ax.set_title("Análisis de Ventas: Real vs. Proyección", 
             fontsize=15, fontweight="bold", pad=20)
ax.set_xlabel("Mes", fontsize=12)
ax.set_ylabel("Ventas ($)", fontsize=12)

# Ajusta layout
fig.tight_layout()
