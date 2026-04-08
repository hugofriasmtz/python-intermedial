import matplotlib.pyplot as plt

categorias = ["Cafe", "Te", "Postres", "Sandwiches"]
pedidos = [80, 45, 60, 35]

# TODO: crea el grafico de barras
plt.bar(categorias, pedidos)

# TODO: agrega titulo
plt.title("Pedidos por Categoria")

# TODO: agrega nombres de ejes
plt.xlabel("Categorias")
plt.ylabel("Pedidos")

# TODO: muestra el grafico
plt.show()

# GLOSARIO
# - plt.bar(): crea un grafico de barras con los datos dados.
# - plt.title(): agrega un titulo al grafico.
# - plt.xlabel(): agrega un nombre al eje X.
# - plt.ylabel(): agrega un nombre al eje Y.
# - plt.show(): muestra el grafico en pantalla.