# 00 - Crear DataFrames y Leer/Escribir CSV

![pandas secondary logo](https://pandas.pydata.org/static/img/pandas_secondary.svg)

> [!NOTE]
> "La práctica consistente transforma lo difícil en dominio. Cada línea de código es un paso adelante."

---

## ¿Qué haremos?

Responderemos 3 preguntas prácticas:

1. **¿Cómo construyo un DataFrame desde cero con datos en Python?** → Listas de diccionarios y diccionarios de listas
2. **¿Cómo traigo datos desde un archivo CSV?** → `read_csv()`
3. **¿Cómo guardo mi DataFrame para compartirlo o reutilizarlo?** → `to_csv()`

---

## Que es un DataFrame

Un **DataFrame** es una tabla bidimensional (filas y columnas) que organiza datos de forma estructurada. Es la estructura principal de `pandas` para trabajar con datos.

### Estructura de un DataFrame

Todo DataFrame tiene:

- **Filas (rows)**: cada fila representa un registro o observación
- **Columnas (columns)**: cada columna representa una característica o variable
- **Índice (index)**: etiqueta o número que identifica cada fila (por defecto: 0, 1, 2, ...)
- **Datos**: pueden ser numéricos, texto, fechas, etc.

### Visualización simple

```python
   nombre   edad   pais
0  Ana      28    Mexico
1  Luis     31    Chile
2  Maria    26    Colombia
```

- Columnas: `nombre`, `edad`, `pais`
- Filas: 3 registros
- Índice: 0, 1, 2

> [!NOTE]
> Un DataFrame es como una hoja de cálculo en Excel, pero que puedes controlar con Python.

---

## Que vas a aprender

- Por qué una lista de diccionarios difiere de un diccionario de listas (pero producen el mismo resultado).
- Cuándo es mejor crear datos en Python vs cargarlos desde archivo.
- Cómo CSV es el formato universal para intercambiar datos tabulares.

---

## 1. Crear DataFrames desde Python

### Lista de diccionarios

Cada diccionario es una fila.

```python
import pandas as pd

datos = [
    {"nombre": "Hugo", "puesto": "Programador", "salario": 4500},
    {"nombre": "Karen", "puesto": "Administradora", "salario": 3200},
    {"nombre": "Marcos", "puesto": "Backend", "salario": 3800},
]

df = pd.DataFrame(datos)
# Output:
#    nombre         puesto  salario
# 0   Hugo      Programador     4500
# 1  Karen   Administradora     3200
# 2 Marcos         Backend     3800
```

> [!IMPORTANT]
> Asegúrate de que todas las filas compartan las mismas claves; si faltan claves, `pandas` rellenará con `NaN`.

### Diccionario de listas

Cada clave es una columna.

```python
import pandas as pd

datos = {
    "nombre": ["Hugo", "Karen", "Marcos"],
    "puesto": ["Programador", "Administradora", "Backend"],
    "salario": [4500, 3200, 3800],
}

df = pd.DataFrame(datos)
# Output:
#    nombre         puesto  salario
# 0   Hugo      Programador     4500
# 1  Karen   Administradora     3200
# 2 Marcos         Backend     3800
```

### Como se interpreta la estructura

- En la lista de diccionarios, pandas lee cada diccionario como una fila.
- En el diccionario de listas, pandas arma filas usando la posicion de cada valor.
- Todas las listas deben tener el mismo largo.

### Para que sirve crear DataFrames

- Construir tablas desde cero.
- Entender como se forma una tabla en pandas.
- Prepararte para trabajar con datos reales.

---

## 2. Leer un CSV real

Un **CSV** es un archivo de texto donde cada fila representa un registro y cada columna se separa con comas. Es un formato simple, liviano y muy usado para intercambiar datos entre programas.

Cuando lees un CSV con `pandas`, el archivo se convierte en un DataFrame para que puedas analizarlo, filtrarlo y resumirlo.

```python
import pandas as pd

df = pd.read_csv("data/pandas/jugadores_futbol.csv")
print(df.head())
```

> [!TIP]
> Usa `Path(__file__).resolve().parents[...]` para rutas portables.

### Para que sirve leer CSV

- Trabajar con datos reales.
- Evitar escribir tablas a mano.
- Empezar el analisis desde un archivo guardado.

> [!CAUTION]
> Leer CSVs grandes consume mucha memoria; prueba con `nrows` o `usecols`.

---

## 3. Escribir un CSV

Guardar un CSV te permite dejar un resultado listo para compartir, volver a abrirlo más tarde o usarlo en otra herramienta.

```python
import pandas as pd

df = pd.read_csv("data/pandas/jugadores_futbol.csv")
df.to_csv("data/pandas/copia_jugadores.csv", index=False)
```

### Para que sirve escribir CSV

- Guardar resultados.
- Compartir tablas con otras personas.
- Exportar datos limpios para otros procesos.

---

## 4. Mini practica

Crea un DataFrame con nombre, edad y pais. Luego guardalo en CSV y vuelve a leerlo.

---

## Errores comunes

- Crear listas de distinto largo en un diccionario de listas.
- Olvidar `index=False` al guardar CSV.
- No revisar el `head()` luego de leer un archivo.
