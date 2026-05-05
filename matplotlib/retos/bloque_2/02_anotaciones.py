# RETO 2: Anotaciones
# Destaca el punto máximo con una anotación y flecha

import matplotlib.pyplot as plt

# Datos de tendencia con picos
meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun"]
datos = [100, 150, 120, 180, 140, 160]

# Crea figura
plt.figure(figsize=(8, 5))

# Grafica línea
plt.plot(meses, datos, marker="o", color="tab:green", linewidth=2)

# Encuentra el máximo
max_index = datos.index(max(datos))
max_value = max(datos)

# Agrega anotación con flecha
plt.annotate(
    f"Pico: {max_value}",
    xy=(max_index, max_value),
    xytext=(max_index - 0.5, max_value + 15),
    arrowprops=dict(arrowstyle="->", color="red", lw=2),
    fontsize=11,
    bbox=dict(boxstyle="round,pad=0.5", facecolor="yellow", alpha=0.7)
)

# Títulos y etiquetas
plt.title("Tendencia con Punto Máximo Destacado")
plt.xlabel("Período")
plt.ylabel("Valor")
plt.grid(alpha=0.3)

Desafío extra (opcional):
1. Encuentra el MÍNIMO en lugar del máximo
2. Cambia arrowstyle de "->" a "<-" (flecha invertida)
3. Cambia el color de la flecha a "red"
4. Agrega MÚLTIPLES anotaciones (máximo Y mínimo)

CONCEPTOS NUEVOS:
- plt.annotate(): Agrega etiqueta con flecha
- xy=(x, y): Punto al cual la flecha apunta
- xytext=(x, y): Dónde aparece el texto de la anotación
- arrowprops: Propiedades de la flecha (estilo, color, grosor)
- max(), min(): Encontrar valores extremos
- Cálculo de índice: x[y.index(max_y)] para encontrar posición
"""

import matplotlib.pyplot as plt

# Datos de una métrica que fluctúa (ej: engagement, conversiones)
x = [1, 2, 3, 4, 5, 6]
y = [3, 5, 4, 7, 9, 8]

# TAREA 1: Crea figura con tamaño controlado
# figsize=(8, 4.5) proporciona suficiente espacio para anotaciones
plt.figure(figsize=(8, 4.5))

# TAREA 2: Grafica los datos
# marker="o" marca cada punto para facilitar la identificación
plt.plot(x, y, marker="o", color="tab:green")

# TAREA 3: Encuentra el valor máximo
max_y = max(y)
max_x = x[y.index(max_y)]

# TAREA 4: Agrega anotación con flecha
# xy=(max_x, max_y) es el punto a apuntar
# xytext=(max_x - 1.5, max_y + 1.2) es dónde poner el texto
# arrowprops crea la flecha
plt.annotate(
    f"Pico maximo: {max_y}",
    xy=(max_x, max_y),
    xytext=(max_x - 1.5, max_y + 1.2),
    arrowprops={"arrowstyle": "->", "color": "black"},
)

# TAREA 5: Personaliza la gráfica
plt.title("Tendencia con punto destacado")
plt.xlabel("Periodo")
plt.ylabel("Valor")
plt.grid(alpha=0.3)

# TAREA 6: Muestra el gráfico
plt.show()


# RESUMEN DE CONCEPTOS:
# - plt.annotate(): Agrega etiqueta con flecha - para qué: destacar un hallazgo
#   - xy: punto a apuntar
#   - xytext: dónde poner el texto
#   - arrowprops: propiedades de la flecha
# - marker="o": Marca puntos - para qué: claridad visual
# - grid(alpha=0.3): Grilla suave - para qué: facilita lectura

# ESTRATEGIA:
# Una anotación transmite "aquí pasó algo importante"
# Sin ella, el lector ve el pico pero no sabe si es relevante
