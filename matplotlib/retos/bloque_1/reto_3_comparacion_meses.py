import matplotlib.pyplot as plt

categorias = ["Cafe", "Te", "Postres", "Sandwiches"]
mes_1 = [80, 45, 60, 35]
mes_2 = [95, 50, 55, 40]

# TODO: construye la comparacion entre mes_1 y mes_2
plt.bar(categorias, mes_1, label="Mes 1", alpha=0.7)
plt.bar(categorias, mes_2, label="Mes 2", alpha=0.7)

# TODO: agrega titulo
plt.title("Comparacion de Ventas por Mes")

# TODO: agrega nombres de ejes
plt.xlabel("Categorias")
plt.ylabel("Ventas")

# TODO: agrega leyenda
plt.legend()

# TODO: muestra el grafico
plt.show()


# GLOSARIO
# - plt.bar(): crea un grafico de barras con los datos dados.
# - label: argumento que asigna una etiqueta a cada conjunto de barras para la leyenda.
# - alpha: argumento que ajusta la transparencia de las barras para facilitar la comparacion visual.
# - plt.title(): agrega un titulo al grafico.
# - plt.xlabel(): agrega un nombre al eje X.
# - plt.ylabel(): agrega un nombre al eje Y.
# - plt.legend(): muestra la leyenda del grafico.
# - plt.show(): muestra el grafico en pantalla.