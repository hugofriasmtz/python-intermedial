# RETO 5: Gráfico de área
# Visualiza cómo 4 categorías componen el total de ventas

import matplotlib.pyplot as plt

# Datos: ventas de 4 categorías
meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun"]
cafe = [100, 120, 110, 140, 160, 150]
te = [60, 65, 70, 75, 80, 78]
postres = [80, 85, 90, 95, 100, 98]
sandwiches = [50, 55, 60, 65, 70, 72]

# Crea figura
plt.figure(figsize=(10, 6))

# Stackplot apila áreas para mostrar composición
plt.stackplot(
    meses,
    cafe, te, postres, sandwiches,
    labels=["Café", "Té", "Postres", "Sandwiches"],
    colors=["#8B4513", "#D4A574", "#FFE4B5", "#F5DEB3"],
    alpha=0.8
)

# Títulos y etiquetas
plt.title("Composición de Ventas Totales por Mes")
plt.xlabel("Mes")
plt.ylabel("Ventas ($)")

# Leyenda
plt.legend(loc="upper left")

# Grilla
plt.grid(alpha=0.3, axis="y")
   )
   
   → stackplot apila las áreas
   → Cada color muestra una categoría
   → Altura total = suma de todas
   → Altura de cada sección = contribución de esa categoría

3. Personaliza:
   plt.title("Composición de Ventas en el Tiempo", fontsize=13)
   plt.xlabel("Mes")
   plt.ylabel("Ventas totales")

4. Leyenda:
   plt.legend(loc="upper left")

5. Grilla:
   plt.grid(alpha=0.3, axis="y")

6. Muestra:
   plt.show()

Pregunta para reflexionar:
¿Cuándo usar área vs. línea multiple?
- LÍNEA MÚLTIPLE: Comparar valores independientes (reto 5 bloque 1)
- ÁREA APILADA: Ver composición de un TOTAL (este reto)

DIFERENCIA VISUAL:

LÍNEA MÚLTIPLE (reto 5):
Café  ─────────────
Té    ─────────────
Postres ─────────────
(Líneas independientes, difícil comparar totales)

ÁREA APILADA:
█ █ █ █  ← Café (arriba)
█ █ █ █  ← Té
█ █ █ █  ← Postres
█ █ █ █  ← Sandwiches
(Composición clara, altura total visible)

PARÁMETROS IMPORTANTES:

alpha (transparencia):
- 0.5: Semitransparente (puedes ver superposiciones)
- 0.7: Más opaco
- 1: Completamente opaco

colors (lista de colores):
- ["tab:blue", "tab:red", "tab:green", "tab:orange"]
- Debe coincidir con número de series

labels (leyenda):
- ["Café", "Té", "Postres", "Sandwiches"]
- Identifican cada área

baseline (línea base):
- "zero": Área desde cero (default)
- "sym": Áreas simétricas (no común)

Desafío extra (opcional):
1. Experimenta: ¿se ve mejor alpha=0.5 o alpha=0.7?
2. Cambia colores: usa colores pastel
3. Agrega una LÍNEA NEGRA de bordes:
   plt.plot(meses, cafe + te + postres + sandwiches, color="black", linewidth=2)

4. Interpreta: ¿qué categoría crece más? ¿cuál disminuye?

5. Crea área con UNA SOLA SERIE (fill_between):
   plt.fill_between(meses, cafe, alpha=0.5)
   Esto rellena solo el área bajo Café

CUÁNDO USAR ÁREA APILADA:
✓ Datos temporales con componentes (ventas por categoría)
✓ Quieres ver COMPOSICIÓN TOTAL (no solo valores)
✓ Importante ver cómo CAMBIA cada parte en el tiempo
✗ NO usar si tienes muchas series (>5), se vuelve confuso
✗ NO usar si quieres enfoque en una serie específica

LECTURA:
1. Altura TOTAL = ventas totales de ese mes
2. Altura de CADA COLOR = cuánto vendió esa categoría
3. Si un color se ENSANCHA = esa categoría crece
4. Si un color se ESTRECHA = esa categoría disminuye
"""

import matplotlib.pyplot as plt

# Datos de ventas por categoría en 6 meses
meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun"]
cafe = [100, 120, 110, 140, 160, 150]
te = [60, 65, 70, 75, 80, 78]
postres = [80, 85, 90, 95, 100, 98]
sandwiches = [50, 55, 60, 65, 70, 72]

# TAREA 1: Crea figura
plt.figure(figsize=(10, 6))

# TAREA 2: Crea áreas apiladas
plt.stackplot(
    meses,
    cafe, te, postres, sandwiches,
    labels=["Café", "Té", "Postres", "Sandwiches"],
    alpha=0.7,
    colors=["tab:blue", "tab:orange", "tab:green", "tab:red"]
)

# TAREA 3: Personaliza
plt.title("Composición de Ventas en el Tiempo", fontsize=13, fontweight="bold")
plt.xlabel("Mes", fontsize=11)
plt.ylabel("Ventas totales", fontsize=11)

# TAREA 4: Leyenda
plt.legend(loc="upper left")

# TAREA 5: Grilla
plt.grid(alpha=0.3, axis="y")

# TAREA 6: Muestra
plt.show()

# ANÁLISIS:
# 1. Altura total de cada mes = ventas totales
# 2. Cada color = contribución de esa categoría
# 3. Si un color crece (se ensancha), esa categoría vende más
# 4. Patrón visual permite ver cómo evoluciona la mezcla de ventas
