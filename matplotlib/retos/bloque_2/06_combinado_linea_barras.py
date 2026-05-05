# RETO 6: Combinado línea + barras
# Usa dos ejes Y para comparar ventas ($) vs. cantidad de clientes

import matplotlib.pyplot as plt

# Datos
meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun"]
ventas = [120, 135, 125, 155, 180, 170]  # en dólares
clientes = [45, 50, 48, 62, 75, 72]      # cantidad

# Crea figura
fig, ax1 = plt.subplots(figsize=(10, 6))

# Eje 1 (izquierda): Barras de ventas
ax1.bar(meses, ventas, color="tab:blue", alpha=0.7, label="Ventas")
ax1.set_xlabel("Mes")
ax1.set_ylabel("Ventas ($)", color="tab:blue")
ax1.tick_params(axis="y", labelcolor="tab:blue")

# Eje 2 (derecha): Línea de clientes
ax2 = ax1.twinx()
ax2.plot(meses, clientes, color="tab:red", marker="o", linewidth=2.5, label="Clientes")
ax2.set_ylabel("Cantidad de clientes", color="tab:red")
ax2.tick_params(axis="y", labelcolor="tab:red")

# Leyenda combinada de ambos ejes
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left")

# Títulos
fig.suptitle("Ventas vs. Cantidad de Clientes")
fig.tight_layout()
