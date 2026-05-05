# RETO 4: Personalización visual
# Crea 3 líneas con colores, estilos y marcadores distintos

import matplotlib.pyplot as plt

# Datos
meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun"]
ventas_mes1 = [100, 120, 110, 140, 160, 150]
ventas_mes2 = [80, 95, 100, 110, 130, 125]
ventas_mes3 = [90, 100, 95, 105, 120, 115]

# Crea figura
plt.figure(figsize=(10, 5))

# Primera línea: azul, sólida, círculos
plt.plot(meses, ventas_mes1, color="tab:blue", linestyle="-", marker="o", label="Mes 1")

# Segunda línea: roja, guiones, cuadrados
plt.plot(meses, ventas_mes2, color="tab:red", linestyle="--", marker="s", label="Mes 2")

# Tercera línea: verde, punto-guión, triángulos
plt.plot(meses, ventas_mes3, color="tab:green", linestyle="-.", marker="^", label="Mes 3")

# Títulos y etiquetas
plt.title("Ventas con Estilos Personalizados")
plt.xlabel("Meses")
plt.ylabel("Ventas")

# Grilla y leyenda
plt.grid(alpha=0.3)
plt.legend()
