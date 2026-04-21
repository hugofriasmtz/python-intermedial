# Guía de Matplotlib

Matplotlib es una biblioteca de visualización de datos en Python que permite crear gráficos estáticos, animados e interactivos. Es ampliamente utilizada para explorar datos, comunicar resultados y crear visualizaciones personalizadas.

En esta carpeta los ejercicios estan organizados para que primero entiendas el grafico mas simple y luego le vayas agregando detalles. La idea es que cada reto te ayude a recordar la intencion de cada parametro, no solo a copiar sintaxis.

En esta guía verás:

1. Cómo preparar un entorno de trabajo limpio.
2. Tipos de gráficos básicos y cuándo usar cada uno.
3. Personalizaciones esenciales para mejorar la lectura.

## Preparando el Entorno

Antes de crear gráficos, conviene trabajar en un entorno virtual para no instalar librerías en todo el sistema.
Esto te ayuda a mantener cada proyecto aislado, ordenado y reproducible.

Buenas prácticas que vamos a seguir:

1. Crear una carpeta para el proyecto.
2. Crear un entorno virtual dentro del proyecto.
3. Activar el entorno antes de instalar librerías.
4. Guardar dependencias en un archivo `requirements.txt`.

### 1) Crear proyecto y entorno virtual

```bash
mkdir mi_proyecto_graficos
cd mi_proyecto_graficos
python3 -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
```

Si todo salió bien, tu terminal mostrará algo como `(.venv)` al inicio.

### 2) Instalar Matplotlib en el entorno

```bash
python -m pip install --upgrade pip
pip install matplotlib
```

> [!NOTE]
> Si usas Linux o WSL2 y `plt.show()` no abre una ventana, probablemente te falta soporte gráfico de Tk/Tkinter.
> En Ubuntu/Debian puedes instalarlo con:
> `sudo apt install python3-tk`
> Si usas Python instalado con pyenv u otra compilación personalizada, podría requerir recompilar Python con soporte Tk.
> Como alternativa universal, guarda la gráfica en archivo con `plt.savefig("grafico.png")`.

### 3) Verificar que la librería quedó en el entorno

```bash
python -c "import matplotlib; print(matplotlib.__version__)"
which python  # En Windows: where python
```

### 4) Guardar dependencias del proyecto

```bash
pip freeze > requirements.txt
```

Esto permite que otra persona (o tú en el futuro) reconstruya el entorno con:

```bash
pip install -r requirements.txt
```

### 5) Salir del entorno cuando termines

```bash
deactivate
```

> [!TIP]
> Agrega `.venv/` a tu archivo `.gitignore` para no subir el entorno al repositorio.

## Gráfico de Líneas

El gráfico de líneas conecta puntos consecutivos y permite ver la evolución de una variable a través del tiempo.

> [!TIP]
> **Cuándo usarla:** cuando los datos siguen una secuencia (tiempo, días, meses, etapas).
> **Qué te ayuda a ver:** si los valores suben, bajan o se mantienen estables.
> **Ejemplo típico:** ventas por mes, temperatura por hora, progreso de estudio por semana.

```python
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
plt.plot(x, y)
plt.title("Gráfico de Líneas")
plt.show()
```

## Cómo Practicar los Retos

En `retos/` veras archivos con objetivos cortos y comentarios de apoyo. Leelos como una receta: primero mira el objetivo, luego ubica los datos y finalmente completa el codigo en el orden que te piden.

Ejemplo visual del resultado:

![Ejemplo de gráfico de líneas](https://commons.wikimedia.org/wiki/Special:FilePath/Pushkin_population_history.svg)

## Diagrama de Dispersión

El diagrama de dispersión muestra cada dato como un punto independiente.
Es ideal para analizar la relación entre dos variables y detectar patrones u outliers.

> [!TIP]
> **Cuándo usarla:** cuando comparas dos variables numéricas al mismo tiempo.
> **Qué te ayuda a ver:** si existe relación entre ambas variables y si hay puntos atípicos (outliers).
> **Ejemplo típico:** horas de estudio vs calificación, altura vs peso, precio vs tamaño.

```python
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
plt.scatter(x, y)
plt.title("Diagrama de Dispersión")
plt.show()
```

Ejemplo visual del resultado:

![Ejemplo de diagrama de dispersión](https://commons.wikimedia.org/wiki/Special:FilePath/Speed_of_cars_and_distance_to_stop.png)

## Histogramas

El histograma muestra la distribución de una variable numérica agrupando valores por intervalos.

> [!TIP]
> **Cuándo usarla:** cuando analizas una sola variable numérica con muchos datos.
> **Qué te ayuda a ver:** en qué rangos se concentran los valores y cómo es su distribución.
> **Ejemplo típico:** edades de un grupo, tiempos de entrega, notas de un examen.

```python
import matplotlib.pyplot as plt
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
plt.hist(data, bins=4)
plt.title("Histograma")
plt.show()
```

Ejemplo visual del resultado:

![Ejemplo de histograma](https://commons.wikimedia.org/wiki/Special:FilePath/Black_cherry_tree_histogram.svg)

## Personalizar los Gráficos

En esta sección veremos cuatro personalizaciones básicas y muy útiles para empezar:

Un tick es cada marca visible en los ejes (X o Y), junto con su etiqueta; sirve para leer correctamente la escala de la gráfica.

1. Dar nombre al eje X con `plt.xlabel()`.
2. Dar nombre al eje Y con `plt.ylabel()`.
3. Agregar un título con `plt.title()`.
4. Ajustar las marcas de los ejes (ticks) con `plt.xticks()` y `plt.yticks()`.

> [!TIP]
> Usa etiquetas y título desde el inicio. Un gráfico sin contexto puede verse bien, pero no siempre se entiende rápido.

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y)

# Título y nombres de ejes
plt.title("Crecimiento de valores")
plt.xlabel("Tiempo (días)")
plt.ylabel("Valor")

# Ticks (marcas visibles en los ejes)
plt.xticks([1, 2, 3, 4, 5])
plt.yticks([0, 2, 4, 6, 8, 10, 12])

plt.show()
```

Ejemplo visual del resultado:

![Ejemplo de gráfico personalizado](https://commons.wikimedia.org/wiki/Special:FilePath/ScientificGraphSpeedVsTime.svg)

## Más Personalización Básica

Cuando ya tienes título, ejes y ticks, el siguiente paso es mejorar la lectura visual.

1. Agregar texto dentro del gráfico con `plt.text()`.
2. Cambiar color y estilo de línea con `color` y `linestyle`.
3. Activar cuadrícula con `plt.grid()`.

> [!TIP]
> Estas opciones no cambian tus datos; mejoran la claridad y facilitan la interpretación.

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Color y estilo de línea
plt.plot(x, y, color="teal", linestyle="--", marker="o", label="Serie A")

# Título y ejes
plt.title("Ejemplo con texto, color y grid")
plt.xlabel("Tiempo")
plt.ylabel("Valor")

# Texto dentro del gráfico (x, y, "mensaje")
plt.text(3, 5.2, "Punto medio")

# Cuadrícula
plt.grid(True)

# Leyenda
plt.legend()

plt.show()
```
