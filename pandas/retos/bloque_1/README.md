# Pandas Bloque 1 - Guia de Inicio

![pandas mark](https://pandas.pydata.org/static/img/pandas_mark.svg)

> Esta guia te lleva desde cero en un orden simple: cargar datos, entenderlos y hacer analisis basico.

---

## Objetivo del bloque

Al terminar este bloque deberias poder:

1. Cargar datos en un DataFrame.
2. Revisar estructura y columnas.
3. Obtener resúmenes numericos clave.
4. Seleccionar columnas con corchetes.
5. Filtrar filas con condiciones.
6. Detectar valores nulos.

---

## Orden recomendado de aprendizaje

1. Cargar datos.
2. Revisar estructura.
3. Resumir columnas numericas.
4. Seleccionar informacion.
5. Filtrar.
6. Revisar nulos.

Regla mental: primero entender los datos, despues transformarlos.

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

1. `01_dataframe_basico.py`: cargar CSV y crear DataFrame.
2. `02_revision_inicial.py`: revisar estructura inicial.
3. `03_seleccion_corchetes.py`: seleccionar columnas y filas basicas.
4. `04_resumen_numerico.py`: aplicar metodos de resumen en columnas numericas.
5. `05_subconjunto_y_contribucion.py`: crear un subconjunto y una metrica derivada.
6. `06_filtros_basicos.py`: aplicar filtros simples.
7. `07_nulos_basicos.py`: detectar y tratar nulos.

Nota: en esta etapa sigue el orden completo de 01 a 07 para subir dificultad gradualmente.

---

## Checklist de avance

1. Puedes cargar el CSV sin ayuda.
2. Puedes explicar `shape`, `columns` e `index`.
3. Puedes usar al menos 3 metodos de resumen numerico.
4. Puedes seleccionar columnas con corchetes.
5. Puedes aplicar un filtro simple.
6. Puedes detectar nulos por columna.
