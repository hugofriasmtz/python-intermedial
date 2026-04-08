import matplotlib.pyplot as plt

meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun"]
ventas = [120, 150, 130, 170, 200, 190]

# TODO: crea el grafico de lineas
plt.plot(meses, ventas)

# TODO: agrega titulo
plt.title("Ventas Mensuales")

# TODO: agrega nombres de ejes
plt.xlabel("Meses")
plt.ylabel("Ventas")

# TODO: ajusta ticks del eje X
plt.xticks(meses) 

# TODO: muestra el grafico
plt.show()


# GLOSARIO 
# - plt.plot(): crea un grafico de lineas con los datos dados.
# - plt.title(): agrega un titulo al grafico.
# - plt.xlabel(): agrega un nombre al eje X.
# - plt.ylabel(): agrega un nombre al eje Y.
# - plt.xticks(): ajusta los ticks del eje X con los meses.
# - plt.show(): muestra el grafico en pantalla.
