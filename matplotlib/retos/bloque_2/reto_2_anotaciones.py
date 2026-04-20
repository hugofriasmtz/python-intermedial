"""Reto 2: Anotaciones

Objetivo:
- Resaltar un punto importante dentro de una grafica.

Instrucciones:
1) Crea una grafica de lineas con los datos dados.
2) Agrega una anotacion para marcar el valor mas alto.
3) Usa titulo, nombres de ejes y grid si lo necesitas.
4) Haz que el mensaje de la anotacion sea claro.

Pista:
- Piensa en una etiqueta que ayude a entender por que ese punto es importante.
"""

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [3, 5, 4, 7, 9, 8]

plt.figure(figsize=(8, 4.5))
plt.plot(x, y, marker="o", color="tab:green")

max_y = max(y)
max_x = x[y.index(max_y)]

plt.annotate(
	f"Pico maximo: {max_y}",
	xy=(max_x, max_y),
	xytext=(max_x - 1.5, max_y + 1.2),
	arrowprops={"arrowstyle": "->", "color": "black"},
)

plt.title("Tendencia con punto destacado")
plt.xlabel("Periodo")
plt.ylabel("Valor")
plt.grid(alpha=0.3)
plt.show()
