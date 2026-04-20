"""Reto 1: Subplots

Objetivo:
- Comparar dos series de datos en una misma figura usando subplots.

Instrucciones:
1) Crea una figura con dos graficos en fila o en columna.
2) En el primero, muestra una serie de lineas.
3) En el segundo, muestra otra serie relacionada.
4) Agrega titulo a cada subplot y un titulo general si lo consideras necesario.

Pista:
- Usa la idea de dividir la figura en partes para comparar mejor.
"""

import matplotlib.pyplot as plt

meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun"]
ventas = [120, 150, 130, 170, 200, 190]
gastos = [80, 90, 85, 100, 110, 105]

fig, axes = plt.subplots(2, 1, figsize=(8, 7), sharex=True)

axes[0].plot(meses, ventas, marker="o", color="tab:blue")
axes[0].set_title("Ventas mensuales")
axes[0].set_ylabel("Monto")
axes[0].grid(alpha=0.3)

axes[1].plot(meses, gastos, marker="s", color="tab:red")
axes[1].set_title("Gastos mensuales")
axes[1].set_xlabel("Mes")
axes[1].set_ylabel("Monto")
axes[1].grid(alpha=0.3)

fig.suptitle("Comparacion de ventas y gastos")
fig.tight_layout()
plt.show()
