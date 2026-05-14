# Pandas Bloque 1 - Guia de Inicio

![pandas mark](https://pandas.pydata.org/static/img/pandas_mark.svg)

> Esta guia te lleva desde cero en un orden simple: crear DataFrames, cargar datos, entenderlos y hacer analisis basico.

---

## Objetivo del bloque

Al terminar este bloque deberias poder:

1. Crear DataFrames desde estructuras de Python.
2. Leer y escribir archivos CSV.
3. Cargar datos en un DataFrame.
4. Revisar estructura y columnas.
5. Obtener resúmenes numericos clave.
6. Seleccionar columnas con corchetes.
7. Filtrar filas con condiciones.
8. Detectar valores nulos.

---

## Orden recomendado de aprendizaje

0. Crear DataFrames y trabajar con CSV.
1. Cargar datos.
2. Revisar estructura.
3. Resumir columnas numericas.
4. Seleccionar informacion.
5. Filtrar.
6. Revisar nulos.

Regla mental: primero entender los datos, despues transformarlos.

---

## Paso 0: crear DataFrames y trabajar con CSV

Pandas te deja crear DataFrames directamente desde estructuras de Python y luego leer o escribir archivos CSV reales.

### 0A. Lista de diccionarios

Cada diccionario representa una fila.

```python
datos = [
    {"nombre": "Ana", "edad": 28, "pais": "Mexico"},
    {"nombre": "Luis", "edad": 31, "pais": "Chile"},
]

df = pd.DataFrame(datos)
```

### 0B. Diccionario de listas

Cada clave representa una columna.

```python
datos = {
    "nombre": ["Ana", "Luis"],
    "edad": [28, 31],
    "pais": ["Mexico", "Chile"],
}

df = pd.DataFrame(datos)
```

### Como se estructuran

- En una lista de diccionarios, las llaves del diccionario se convierten en columnas.
- En un diccionario de listas, cada lista debe tener la misma longitud para formar filas completas.

### Para que sirve crear DataFrames asi

1. Te permite construir tablas desde cero.
2. Te ayuda a entender como se forma una tabla en pandas.
3. Te prepara para trabajar con datos reales.

Regla mental:

- `DataFrame(...)` para construir tablas.

### 0C. Leer un CSV real de la carpeta `data`

Cuando ya tienes un archivo en `data/pandas/`, puedes leerlo directamente con `read_csv(...)`.

Ejemplo:

```python
df = pd.read_csv("data/pandas/jugadores_futbol.csv")
```

### 0D. Escribir un CSV

Tambien puedes guardar una copia temporal o una version procesada con `to_csv(...)`.

Ejemplo:

```python
df.to_csv("data/pandas/copia_jugadores.csv", index=False)
```

### Para que sirve leer y escribir CSV

- Te permite usar archivos reales como entrada.
- Te ayuda a guardar resultados intermedios.
- Separa claramente la creacion de DataFrames de la lectura/escritura de archivos.

Regla mental:

- `read_csv(...)` para leer archivos.
- `to_csv(...)` para guardar archivos.

---

## Paso 1: cargar datos

Primero importas pandas con alias:

```python
import pandas as pd
```

Luego cargas tu CSV:

```python
df = pd.read_csv("data/pandas/jugadores_futbol.csv")
```

Por que es importante:

1. Sin DataFrame no hay analisis.
2. Cargar bien el archivo evita errores en todos los pasos siguientes.

---

## Paso 2: revisar estructura basica

```python
print(df.head())
print(df.shape)
print(df.columns)
print(df.index)
```

Que te responde:

1. `head()`: como se ven las primeras filas.
2. `shape`: cuantas filas y columnas hay.
3. `columns`: que nombres de columnas tienes disponibles.
4. `index`: como se identifican las filas.

---

## Paso 3: metodos de resumen (base numerica)

Los principales metodos de resumen son:

1. `sum()`: calcula el total de todos los valores.
2. `mean()`: calcula el valor medio (promedio).
3. `median()`: identifica el valor central cuando los datos estan ordenados.
4. `min()` y `max()`: encuentran el valor minimo o maximo.
5. `count()`: cuenta el numero de valores no nulos.
6. `nunique()`: cuenta el numero de valores unicos.

Ejemplo con `edad`:

```python
print("sum:", df["edad"].sum())
print("mean:", df["edad"].mean())
print("median:", df["edad"].median())
print("min:", df["edad"].min())
print("max:", df["edad"].max())
print("count:", df["edad"].count())
print("nunique:", df["edad"].nunique())
```

Para que sirve:

1. Entender rapido el comportamiento de una columna.
2. Detectar valores atipicos.
3. Mejorar tus decisiones al filtrar.

---

## Paso 4: seleccion basica con corchetes

```python
print(df["nombre"])
print(df[["nombre", "equipo", "goles"]])
```

Que haces:

1. Tomas una sola columna.
2. Tomas un subconjunto de columnas.

Para que sirve:

1. Enfocarte en la informacion relevante.
2. Reducir ruido antes del analisis.

### `.loc` y `.iloc`

Cuando quieres seleccionar filas o columnas de forma mas precisa, usas `.loc` o `.iloc`.

Regla rapida:

- `.loc` trabaja con etiquetas o nombres.
- `.iloc` trabaja con posiciones numericas.

Ejemplos:

```python
print(df.loc[0])
print(df.loc[0:3])
print(df.iloc[0])
print(df.iloc[0:3])
```

Si el DataFrame tiene un indice con nombres o categorias, `.loc` te deja seleccionar por esos valores.
Si quieres seleccionar por lugar exacto dentro de la tabla, `.iloc` es la opcion correcta.

Cuando hay rangos:

- `.loc[1:4]` incluye el valor final si ese valor existe en el indice.
- `.iloc[1:4]` sigue el estilo de slicing de Python y no incluye el final.

Idea simple para recordarlo:

- Corchetes `[]` para seleccionar columnas.
- `.loc` para cortar usando etiquetas.
- `.iloc` para cortar usando posiciones.

### Añadir columnas y conteos rápidos

Puedes crear columnas derivadas con asignación y usar `value_counts()` o `drop_duplicates()` para entender frecuencias o unicidad:

```python
# nueva columna derivada
df["goles_por_partido"] = df["goles"] / df["partidos"]
print(df[["nombre", "goles_por_partido"]].head())

# conteo por pais
print(df["pais"].value_counts())
print(df["pais"].value_counts(normalize=True))  # proporciones

# eliminar duplicados por columna
print(df.drop_duplicates(subset=["pais"]).shape)
```

---

## Paso 5: filtros basicos

```python
print(df[df["goles"] > 10])
print(df[(df["pais"] == "Mexico") & (df["edad"] < 30)])
```

Que haces:

1. Te quedas solo con filas que cumplen reglas.

Para que sirve:

1. Responder preguntas concretas con datos reales.

---

## Paso 6: nulos

```python
print(df.isna())
print(df.isna().sum())
```

Que haces:

1. Detectas celdas vacias.
2. Cuentas nulos por columna.

Para que sirve:

1. Saber si necesitas limpieza antes de analisis mas profundos.

---

## Relacion con los retos del bloque

0. `00_creacion_dataframes_y_csv.py`: crear DataFrames y leer/escribir CSV.
1. `01_dataframe_basico.py`: cargar CSV y crear DataFrame.
2. `02_revision_inicial.py`: revisar estructura inicial.
3. `03_seleccion_corchetes.py`: seleccionar columnas y filas basicas.
4. `04_resumen_numerico.py`: aplicar metodos de resumen en columnas numericas.
5. `05_subconjunto_y_contribucion.py`: crear un subconjunto y una metrica derivada.
6. `06_filtros_basicos.py`: aplicar filtros simples.
7. `07_nulos_basicos.py`: detectar y tratar nulos.

Nota: en esta etapa sigue el orden completo de 00 a 07 para subir dificultad gradualmente.

---

## Checklist de avance

1. Puedes crear un DataFrame desde una lista de diccionarios.
2. Puedes crear un DataFrame desde un diccionario de listas.
3. Puedes leer y escribir un CSV.
4. Puedes cargar el CSV sin ayuda.
5. Puedes explicar `shape`, `columns` e `index`.
6. Puedes usar al menos 3 metodos de resumen numerico.
7. Puedes seleccionar columnas con corchetes.
8. Puedes diferenciar entre `.loc` e `.iloc`.
9. Puedes aplicar un filtro simple.
10. Puedes detectar nulos por columna.
