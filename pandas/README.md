# Guía de Pandas

Pandas es una biblioteca de análisis de datos en Python. Permite trabajar con tablas de información de forma práctica para explorar, filtrar, limpiar y resumir datos.

La idea de esta carpeta es aprender paso a paso: primero crear y revisar DataFrames, luego seleccionar datos y después combinar filtros y agrupaciones. Cada reto esta pensado para que puedas recordar la logica sin memorizarla a ciegas.

En esta guía verás:

1. Cómo preparar un entorno básico para Pandas.
2. Conceptos iniciales que debes dominar antes de seleccionar datos.
3. Diferencias entre `[]`, `loc` e `iloc`.
4. Errores comunes y práctica recomendada para nivel inicial.

## Preparando el Entorno

Para empezar, solo necesitas Python y Pandas instalados en un entorno virtual.

### 1) Crear y activar entorno virtual

```bash
python3 -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
```

### 2) Instalar Pandas

```bash
python -m pip install --upgrade pip
pip install pandas
```

### 3) Verificar instalación

```bash
python -c "import pandas as pd; print(pd.__version__)"
```

> [!TIP]
> Si tu proyecto crece, guarda dependencias con `pip freeze > requirements.txt`.

## Conceptos Iniciales

Antes de escribir consultas, entiende estas bases:

1. `DataFrame`: tabla completa.
2. `Series`: una columna de la tabla.
3. `Columna`: variable (por ejemplo, `country`).
4. `Índice`: identificador de cada fila.
5. `Fila`: cada registro de datos.

> [!TIP]
> Si dominas índice, columnas y filas, `loc` e `iloc` se vuelven mucho más fáciles.

## Crear tu Primer DataFrame

```python
import pandas as pd

data = {
    "country": ["Brazil", "Russia", "India"],
    "capital": ["Brasilia", "Moscow", "New Delhi"],
    "population": [200.4, 143.5, 1252.0]
}

df = pd.DataFrame(data)
print(df)
```

## Revisar la Tabla Antes de Seleccionar

Siempre revisa esto primero:

```python
df.shape      # tamaño: (filas, columnas)
df.columns    # nombres de columnas
df.index      # índice de filas
df.head()     # primeras filas
```

## Selección Básica con `[]`

Empieza por aquí:

```python
df["country"]
```

Devuelve una columna (`Series`).

```python
df[["country", "capital"]]
```

Devuelve varias columnas (`DataFrame`).

```python
df[0:2]
```

Devuelve filas por rango de posición.

## `loc` e `iloc`

Esta es la diferencia más importante en selección de datos.

### `loc` (por etiqueta)

Selecciona por nombre de fila/columna:

```python
df.loc[:, ["country", "capital"]]
```

### `iloc` (por posición)

Selecciona por número de fila/columna:

```python
df.iloc[:, [0, 1]]
```

## Regla Rápida para Memorizar

- `loc` -> labels (etiquetas)
- `iloc` -> integer location (posiciones)

## Errores Comunes al Empezar

1. Mezclar etiquetas y posiciones en el mismo método.
2. No revisar `df.columns` y `df.index` antes de seleccionar.
3. Pensar que `df["col"]` y `df[["col"]]` son iguales.
4. Saltar a temas avanzados sin practicar selección básica.

## Mini Práctica Recomendada

Haz estos pasos en orden:

1. Crea un DataFrame simple.
2. Revisa `head`, `shape`, `columns` e `index`.
3. Selecciona una columna con `[]`.
4. Selecciona dos columnas con `[]`.
5. Selecciona por etiqueta con `loc`.
6. Selecciona por posición con `iloc`.

## Cómo Leer los Retos

Los archivos de `retos/` usan comentarios cortos para ayudarte a entender que hace cada linea. La meta no es solo resolver el ejercicio, sino reconocer el patron para poder repetirlo despues sin mirar la solucion.

## ¿Qué Sigue Después?

Cuando domines esta parte inicial, continúa con:

- filtros con condiciones,
- ordenamiento,
- nulos y duplicados,
- agrupaciones con `groupby`.

Esta carpeta seguirá creciendo por bloques de práctica.
