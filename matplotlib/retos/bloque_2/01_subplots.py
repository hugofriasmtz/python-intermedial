# RETO 1: Subplots
# Crea dos gráficas independientes en una misma figura

import matplotlib.pyplot as plt

# Datos
meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun"]
ventas = [100, 120, 110, 140, 160, 150]
gastos = [80, 85, 90, 95, 100, 110]

# Crea figura con 2 subplots (2 filas, 1 columna)
fig, axes = plt.subplots(2, 1, figsize=(8, 7), sharex=True)

# Subplot 1: Ventas
axes[0].plot(meses, ventas, marker="o", color="tab:blue")
axes[0].set_title("Ventas mensuales")
axes[0].set_ylabel("Monto ($)")
axes[0].grid(alpha=0.3)

# Subplot 2: Gastos
axes[1].plot(meses, gastos, marker="s", color="tab:red")
axes[1].set_title("Gastos mensuales")
axes[1].set_xlabel("Mes")
axes[1].set_ylabel("Monto ($)")
axes[1].grid(alpha=0.3)

# Título general de la figura
fig.suptitle("Comparación de Ventas y Gastos", fontsize=13, fontweight="bold")

# Ajusta espaciado
fig.tight_layout()
2. Cambia marker="o" a marker="s" (cuadrado) en ventas
3. Prueba sharex=False - ¿qué diferencia hay?

CONCEPTOS NUEVOS:
- fig, axes = plt.subplots(): Crea figura y subplots
- axes[0], axes[1]: Acceder a cada subplot individualmente
- axes[0].plot(): Usar métodos en cada subplot por separado
- set_title(): Título individual (vs. title() que es global)
- fig.suptitle(): Título GENERAL de la figura
- fig.tight_layout(): Ajusta espacios automáticamente
"""

import matplotlib.pyplot as plt

# Datos de ventas y gastos mensuales
meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun"]
ventas = [120, 150, 130, 170, 200, 190]
gastos = [80, 90, 85, 100, 110, 105]

# TAREA 1: Crea figura con subplots
# subplots(2, 1) = 2 filas, 1 columna = dos gráficas verticales
# figsize=(8, 7) controla el tamaño total de la figura
# sharex=True hace que ambos subplots compartan el eje X
fig, axes = plt.subplots(2, 1, figsize=(8, 7), sharex=True)

# TAREA 2: Personaliza el primer subplot (ventas)
# axes[0] es la primera gráfica (fila 0)
axes[0].plot(meses, ventas, marker="o", color="tab:blue")
axes[0].set_title("Ventas mensuales")
axes[0].set_ylabel("Monto")
axes[0].grid(alpha=0.3)

# TAREA 3: Personaliza el segundo subplot (gastos)
# axes[1] es la segunda gráfica (fila 1)
axes[1].plot(meses, gastos, marker="s", color="tab:red")
axes[1].set_title("Gastos mensuales")
axes[1].set_xlabel("Mes")
axes[1].set_ylabel("Monto")
axes[1].grid(alpha=0.3)

# TAREA 4: Agrega título general a la figura
# Responde: ¿qué preguntas responden estos dos gráficos juntos?
fig.suptitle("Comparacion de ventas y gastos")

# TAREA 5: Ajusta espaciado automáticamente
# Sin esto, títulos pueden superponerse
fig.tight_layout()

# TAREA 6: Muestra la figura
plt.show()


# RESUMEN DE CONCEPTOS:
# - fig, axes = plt.subplots(filas, columnas): Para qué: crear múltiples gráficas
# - axes[i].plot(), axes[i].set_title(): Para qué: personalizar cada subplot
# - fig.suptitle(): Para qué: título general que enmarca todos los subplots
# - fig.tight_layout(): Para qué: evitar sobreposición de textos
# - marker="o", marker="s": Para qué: diferenciar visualmente las líneas
# - grid(alpha=0.3): Para qué: facilitar lectura de valores

# DIFERENCIA IMPORTANTE:
# fig.suptitle() = título de la figura completa (general)
# axes[i].set_title() = título de cada subplot individual
