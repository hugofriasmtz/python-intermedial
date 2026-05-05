# RETO 3: Escala logarítmica
# Compara escala lineal vs. logarítmica para datos exponenciales

import matplotlib.pyplot as plt

# Datos: usuarios creciendo exponencialmente
anios = ["Año1", "Año2", "Año3", "Año4", "Año5", "Año6"]
usuarios = [10, 100, 1000, 10000, 100000, 1000000]

# Crea figura con 2 subplots (1 fila, 2 columnas)
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Subplot 1: Escala LINEAL (normal)
axes[0].plot(anios, usuarios, marker="o", color="tab:blue", linewidth=2)
axes[0].set_title("Escala Normal (Lineal)")
axes[0].set_xlabel("Período")
axes[0].set_ylabel("Usuarios")
axes[0].grid(alpha=0.3)

# Subplot 2: Escala LOGARÍTMICA
axes[1].plot(anios, usuarios, marker="o", color="tab:purple", linewidth=2)
axes[1].set_yscale("log")  # ← Aplica escala logarítmica
axes[1].set_title("Escala Logarítmica")
axes[1].set_xlabel("Período")
axes[1].set_ylabel("Usuarios")
axes[1].grid(alpha=0.3, which="both")  # which="both" para grilla fina

# Título general
fig.suptitle("Comparación: Escala Normal vs. Logarítmica")
fig.tight_layout()
   → En escala log, esto facilita mucho la lectura

4. Agrega título general:
   fig.suptitle("Comparación: Escala Lineal vs. Logarítmica")

5. Ajusta espacios:
   fig.tight_layout()

6. Muestra:
   plt.show()

OBSERVACIONES CLAVE:
En escala LINEAL:
  - Puntos [10, 100, 1000, 10000, 100000, 1000000]
  - Se ven: casi en la misma línea, luego un salto GIGANTE

En escala LOGARÍTMICA:
  - Los mismos puntos se VEN uniformemente espaciados
  - Porque visualmente representa: ×10, ×10, ×10, ×10, ×10

Pregunta para reflexionar:
¿Por qué un gráfico lineal de 10 a 1,000,000 no muestra el patrón?
Respuesta: El rango es tan enorme que los primeros valores se pierden.
           La escala log COMPRIME la visualización, mostrando la TASA de crecimiento.

Desafío extra (opcional):
1. Aplica escala log también al eje X: axes[1].set_xscale("log")
2. Cambia which="both" a which="major" - ¿qué diferencia hay?
3. Agrega valores como [1, 10, 100, ...] en ambos ejes para ver el patrón

CONCEPTOS NUEVOS:
- set_yscale("log"): Cambia eje Y a escala logarítmica
- set_xscale("log"): Cambia eje X a escala logarítmica
- grid(which="both"): Grillas mayores (principales) y menores (secundarias)
- Escala LINEAL: espacios iguales = cambios iguales (1, 2, 3, 4, 5...)
- Escala LOG: espacios iguales = multiplicación igual (1, 10, 100, 1000...)

CUÁNDO USAR ESCALA LOGARÍTMICA:
✓ Crecimiento exponencial (bacterias, usuarios, dinero en inversiones)
✓ Cuando hay rango ENORME entre mínimo y máximo
✓ Para ver TASA de crecimiento en lugar de valores absolutos
✗ NO usar si tienes valores negativos o cero (log no funciona con esos)
"""

import matplotlib.pyplot as plt

# Datos de usuarios que crecen exponencialmente
# De 10 usuarios en año 1 a 1 millón en año 6
anio = [1, 2, 3, 4, 5, 6]
usuarios = [10, 100, 1000, 10000, 100000, 1000000]

import matplotlib.pyplot as plt

# Datos de usuarios que crecen exponencialmente
# De 10 usuarios en año 1 a 1 millón en año 6
anio = [1, 2, 3, 4, 5, 6]
usuarios = [10, 100, 1000, 10000, 100000, 1000000]

# TAREA 1: Crea figura con DOS SUBPLOTS (1 fila, 2 columnas)
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# TAREA 2: PRIMER SUBPLOT - Escala LINEAL (normal)
axes[0].plot(anio, usuarios, marker="o", color="tab:blue")
axes[0].set_title("Escala Lineal")
axes[0].set_xlabel("Año")
axes[0].set_ylabel("Usuarios")
axes[0].grid(alpha=0.3)

# OBSERVACIÓN: Sin cambio de escala, ves el rango enorme
# El valor 1,000,000 domina visualmente
# Los primeros valores (10, 100, 1000) casi desaparecen

# TAREA 3: SEGUNDO SUBPLOT - Escala LOGARÍTMICA
axes[1].plot(anio, usuarios, marker="o", color="tab:purple")

# ← AQUÍ ES EL CAMBIO CLAVE:
axes[1].set_yscale("log")  # Transforma eje Y a escala logarítmica

axes[1].set_title("Escala Logarítmica")
axes[1].set_xlabel("Año")
axes[1].set_ylabel("Usuarios")

# GRILLA especial para escala log
# which="both" muestra grillas mayores Y menores
# En escala log, esto facilita mucho la lectura
axes[1].grid(alpha=0.3, which="both")

# TAREA 4: Agrega título general
fig.suptitle("Comparación: Escala Lineal vs. Logarítmica")

# TAREA 5: Ajusta espacios
fig.tight_layout()

# TAREA 6: Muestra el gráfico
plt.show()


# DIFERENCIA VISUAL:
# 
# En escala LINEAL: [10, 100, 1000, 10000, 100000, 1000000]
# Se ven casi juntos, luego un salto GIGANTE
# 
# En escala LOGARÍTMICA: Los mismos puntos se ven uniformes
# Porque 10×10 = 100, 100×10 = 1000, etc.
# Todas son multiplicaciones por 10 (mismo "crecimiento relativo")
#
# CONCLUSIÓN: La escala log muestra la TASA de cambio, no los valores absolutos
