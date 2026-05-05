# RETO 1: Gráfico de líneas
# Visualiza cómo cambian las ventas mes a mes

import matplotlib.pyplot as plt

# Datos
meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun"]
ventas = [120, 150, 130, 170, 200, 190]

# Crea línea
plt.plot(meses, ventas)

# Títulos y etiquetas
plt.title("Ventas Mensuales")
plt.xlabel("Meses")
plt.ylabel("Ventas")
plt.xticks(meses) 

# TAREA 5: Muestra el gráfico
# Sin esto, matplotlib prepara la figura pero no la visualiza
plt.show()


# RESUMEN DE MÉTODOS USADOS:
# - plt.plot(x, y): Crea líneas conectando puntos - para qué: mostrar tendencias
# - plt.title(): Agrega título - para qué: que el lector entienda el tema
# - plt.xlabel(): Etiqueta eje X - para qué: claridad
# - plt.ylabel(): Etiqueta eje Y - para qué: claridad
# - plt.xticks(): Controla qué se muestra en eje X - para qué: flexibilidad
# - plt.show(): Visualiza en pantalla - para qué: ver el resultado
