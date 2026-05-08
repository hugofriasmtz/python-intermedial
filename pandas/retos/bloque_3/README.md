# Pandas Bloque 3 - Series, Estadisticas y Conteo

![pandas logo](https://pandas.pydata.org/static/img/pandas.svg)

> Este bloque se enfoca en leer mejor una Series: resumirla, medir su variacion, seguir acumulados y contar valores de forma clara.

---

## Objetivo del bloque

Al terminar este bloque deberias poder:

1. Calcular estadisticas descriptivas de una columna.
2. Entender la diferencia entre resumen central, dispersion y posicion.
3. Obtener estadisticas acumuladas paso a paso.
4. Contar valores unicos y comparar frecuencias.
5. Eliminar duplicados segun una o varias columnas.

---

## Cuanto encaja este bloque

Este bloque va despues de bloque 2 porque ya no trata solo de seleccionar, filtrar o combinar datos. Aqui empiezas a responder preguntas como:

- Cual es el valor tipico de una columna.
- Que tan dispersos estan los datos.
- Como cambia una serie a medida que avanza.
- Que valores se repiten mas.
- Que filas son realmente distintas.

---

## Ruta recomendada

1. Estadisticas basicas de Series.
2. Medidas de variacion.
3. Estadisticas acumuladas.
4. Conteo de valores.
5. Eliminacion de duplicados.

Regla mental: primero resumir, luego comparar, despues contar.

---

## 1. Estadisticas basicas de Series

Estos metodos se usan sobre una columna numerica o categórica.

### `median()`

Devuelve el valor central de la serie cuando los datos se ordenan.

Sirve para:

- Tener una medida de centro menos sensible a valores extremos que el promedio.
- Comparar la distribucion de una columna con sesgo.

Ejemplo:

```python
print(df["goles"].median())
```

### `mode()`

Devuelve el o los valores mas frecuentes.

Sirve para:

- Encontrar la categoria mas repetida.
- Identificar el valor mas comun en una columna numerica o textual.

Ejemplo:

```python
print(df["posicion"].mode())
```

Si hay mas de una moda, pandas devuelve varias.
Si quieres quedarte con una sola, puedes usar el primer valor o el menor segun el caso.

Ejemplo:

```python
print(df["posicion"].mode().min())
```

### `min()` y `max()`

Devuelven el valor minimo y maximo.

Sirven para:

- Ver el rango de una columna.
- Detectar extremos rapidamente.

Ejemplo:

```python
print(df["goles"].min())
print(df["goles"].max())
```

### `sum()`

Devuelve la suma total de los valores.

Sirve para:

- Calcular totales de una columna numerica.
- Medir volumen agregado.

Ejemplo:

```python
print(df["goles"].sum())
```

### `quantile()`

Devuelve un percentil de la serie.

Sirve para:

- Separar datos en partes.
- Comparar un valor con el resto de la distribucion.

Ejemplos:

```python
print(df["goles"].quantile(0.25))
print(df["goles"].quantile(0.5))
print(df["goles"].quantile(0.75))
```

La mediana es equivalente a `quantile(0.5)`.

---

## 2. Medidas de variacion

Estas medidas no te dicen solo "cuanto hay", sino "cuanto cambia" la columna.

### `var()`

Devuelve la varianza.

Sirve para:

- Medir que tan dispersos estan los datos respecto al promedio.
- Comparar la variabilidad entre columnas.

Ejemplo:

```python
print(df["goles"].var())
```

### `std()`

Devuelve la desviacion estandar.

Sirve para:

- Interpretar la dispersion en la misma unidad de los datos.
- Ver si una columna es estable o muy irregular.

Ejemplo:

```python
print(df["goles"].std())
```

Regla simple:

- `var()` resume la dispersión al cuadrado.
- `std()` resume la dispersion en la escala original.

---

## 3. Estadisticas acumuladas

Las estadisticas acumuladas muestran como va cambiando una serie fila por fila.

### `cummax()`

Devuelve el maximo acumulado.

Sirve para:

- Ver el mejor valor alcanzado hasta cada fila.
- Seguir records o hitos crecientes.

Ejemplo:

```python
print(df["goles"].cummax())
```

### `cummin()`

Devuelve el minimo acumulado.

Sirve para:

- Ver el minimo historico hasta cada fila.
- Detectar si aparece un valor mas bajo que los anteriores.

Ejemplo:

```python
print(df["goles"].cummin())
```

### `cumprod()`

Devuelve el producto acumulado.

Sirve para:

- Modelar crecimiento compuesto.
- Multiplicar factores en secuencia.

Ejemplo:

```python
print(df["factor"].cumprod())
```

Importante:

- Estas funciones dependen del orden de la serie.
- Si cambias el orden de filas, cambia el resultado acumulado.

---

## 4. Counting

Counting significa contar cuantas veces aparece cada valor.

### `value_counts()`

Cuenta la frecuencia de cada valor unico.

Sirve para:

- Saber que categoria aparece mas.
- Resumir distribuciones categoricas.
- Detectar desequilibrios en los datos.

Ejemplo:

```python
print(df["posicion"].value_counts())
```

### `value_counts(sort=True)`

Ordena el resultado por frecuencia de mayor a menor.

Sirve para:

- Ver rapidamente el ranking de categorias mas frecuentes.

Ejemplo:

```python
print(df["posicion"].value_counts(sort=True))
```

Nota: este es el comportamiento por defecto, asi que muchas veces no hace falta escribirlo.

### `value_counts(normalize=True)`

Devuelve proporciones en lugar de conteos absolutos.

Sirve para:

- Comparar distribuciones en forma de porcentaje.
- Entender el peso relativo de cada categoria.

Ejemplo:

```python
print(df["posicion"].value_counts(normalize=True))
```

Si quieres verlo como porcentaje, puedes multiplicar por 100.

---

## 5. Eliminar duplicados

Eliminar duplicados sirve para quedarte solo con filas repetidas una sola vez segun una clave.

### `drop_duplicates()`

Elimina filas duplicadas completas.

Sirve para:

- Limpiar registros repetidos.
- Preparar una tabla unica antes de analizarla.

Ejemplo:

```python
print(df.drop_duplicates())
```

### `drop_duplicates(subset="columna")`

Elimina duplicados usando solo una columna como referencia.

Sirve para:

- Conservar un registro por valor unico de una columna.

Ejemplo:

```python
print(df.drop_duplicates(subset="equipo"))
```

### `drop_duplicates(subset=["columna1", "columna2"])`

Elimina duplicados usando varias columnas al mismo tiempo.

Sirve para:

- Definir unicidad por combinacion de columnas.
- Quitar filas repetidas solo cuando coinciden todas las claves elegidas.

Ejemplo:

```python
print(df.drop_duplicates(subset=["equipo", "posicion"]))
```

Regla mental:

- Una columna define unicidad simple.
- Varias columnas definen unicidad compuesta.

---

## Como interpretar estos metodos

Piensa en tres preguntas:

1. Cual es el valor central? Usa `median()` o `mode()`.
2. Que tan dispersos estan los datos? Usa `var()` o `std()`.
3. Que se repite mas y que debo limpiar? Usa `value_counts()` y `drop_duplicates()`.

---

## Relacion con los retos del bloque

Ruta sugerida de retos:

1. `01_resumen_central.py`: media, mediana, moda y cuantiles.
2. `02_rango_y_dispersion.py`: min, max, varianza y desviacion estandar.
3. `03_acumulados.py`: maximo, minimo y producto acumulado.
4. `04_value_counts_basico.py`: conteo de categorias.
5. `05_value_counts_normalizado.py`: frecuencias relativas y ordenadas.
6. `06_drop_duplicates_simple.py`: deduplicar por una columna.
7. `07_drop_duplicates_compuesto.py`: deduplicar por varias columnas.

Este bloque puede crecer con ejercicios como:

1. Calcular resumen numerico de una columna.
2. Comparar media, mediana y moda.
3. Medir dispersion con varianza y desviacion estandar.
4. Seguir acumulados fila por fila.
5. Contar categorias y proporciones.
6. Eliminar duplicados simples y compuestos.

---

## Checklist de avance

1. Puedes explicar cuando usar median en lugar de mean.
2. Puedes distinguir mode, min, max, var y std.
3. Puedes interpretar una serie acumulada.
4. Puedes leer un value_counts normal y uno normalizado.
5. Puedes decidir que columnas usar como subset en drop_duplicates.
