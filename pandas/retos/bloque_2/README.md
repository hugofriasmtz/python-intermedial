# Pandas Bloque 2 - Guia Intermedia Aplicada

![pandas logo](https://pandas.pydata.org/static/img/pandas.svg)

> En este bloque pasas de operaciones basicas a analisis con criterio: ordenar, filtrar, agrupar, combinar y resumir.

---

## Objetivo del bloque

Al terminar este bloque deberias poder:

1. Priorizar jugadores con ordenamientos y top N.
2. Crear filtros combinados con varias condiciones.
3. Resumir informacion con groupby.
4. Aplicar multiples agregaciones en una sola salida.
5. Combinar tablas con merge.
6. Construir tablas dinamicas con pivot_table.
7. Trabajar fechas para resumen mensual.

---

## Dataset de trabajo

Todos los retos usan el mismo archivo:

- `data/pandas/jugadores_futbol.csv`

Esto te ayuda a aprender metodos nuevos sin cambiar de contexto de datos.

---

## Metodos clave que aprenderas

1. `sort_values()` y `head()` para ranking.
2. `isin()`, operadores `&` y `|` para filtros combinados.
3. `groupby()` + `agg()` para resumen por categoria.
4. `merge()` para unir tablas por clave.
5. `pivot_table()` para resumen cruzado.
6. `to_datetime()` + `.dt` para trabajar con fechas.

---

## Guia rapida de uso

### `sort_values()` y `head()`

`sort_values()` ordena un DataFrame por una o varias columnas. `head()` devuelve las primeras filas del resultado.

Sirven para:

- Encontrar los valores mas altos o mas bajos.
- Crear rankings rapidos.
- Quedarte con un top N.

Ejemplo:

```python
ordenado = df.sort_values(by="goles", ascending=False)
print(ordenado.head(5))
```

### `isin()` y operadores `&` / `|`

`isin()` comprueba si un valor pertenece a una lista. `&` significa "y" y `|` significa "o".

Sirven para:

- Filtrar varias categorias a la vez.
- Combinar condiciones sin perder claridad.

Ejemplo:

```python
filtro = df[(df["pais"].isin(["Mexico", "Brazil"])) & (df["goles"] > 5)]
print(filtro)
```

### `groupby()`

`groupby()` separa el DataFrame en grupos segun una columna o combinacion de columnas.

Sirve para:

- Resumir por categoria.
- Comparar grupos entre si.
- Responder preguntas como "cuanto hay por tipo" o "cual es el promedio por pais".

Ejemplo:

```python
por_pais = df.groupby("pais")["goles"].sum()
print(por_pais)
```

### `agg()`

`agg()` aplica varias funciones de resumen sobre los grupos creados por `groupby()`.

Sirve para:

- Calcular varias metricas en una sola pasada.
- Obtener min, max, media y mediana al mismo tiempo.

Ejemplo:

```python
resumen = df.groupby("pais")["goles"].agg(["min", "max", "mean", "median"])
print(resumen)
```

Ejemplo con varias columnas y funciones diferentes:

```python
sales = df.groupby(["pais", "posicion"]).agg({
    "goles": ["sum", "mean"],
    "valor_millones": "mean",
})
print(sales)
```

### `merge()`

`merge()` une dos DataFrames usando una columna comun.

Sirve para:

- Enriquecer una tabla con informacion de otra.
- Combinar datos de distintos archivos.

Ejemplo:

```python
resultado = df1.merge(df2, on="id", how="inner")
print(resultado)
```

### `pivot_table()`

`pivot_table()` reorganiza datos para cruzar una categoria por filas con otra por columnas.

Sirve para:

- Ver patrones de forma mas visual.
- Crear tablas de resumen tipo matriz.

Ejemplo:

```python
tabla = df.pivot_table(values="goles", index="pais", columns="posicion", aggfunc="mean")
print(tabla)
```

### `to_datetime()` y `.dt`

`to_datetime()` convierte texto a formato fecha. `.dt` permite extraer partes de esa fecha.

Sirven para:

- Trabajar con meses, anos o dias.
- Hacer resúmenes temporales.
- Extraer componentes de una fecha sin crear columnas manualmente.

Ejemplo:

```python
df["fecha"] = pd.to_datetime(df["fecha"])
df["mes"] = df["fecha"].dt.month
print(df[["fecha", "mes"]])
```

Los accesores mas utiles de `.dt` son:

- `.dt.year`: extrae el ano.
- `.dt.month`: extrae el mes como numero.
- `.dt.day`: extrae el dia del mes.
- `.dt.day_name()`: devuelve el nombre del dia.
- `.dt.month_name()`: devuelve el nombre del mes.
- `.dt.quarter`: devuelve el trimestre.
- `.dt.weekday`: devuelve el dia de la semana como numero.
- `.dt.dayofweek`: devuelve el dia de la semana como numero, de lunes a domingo.
- `.dt.dayofyear`: devuelve el dia del ano.
- `.dt.isocalendar().week`: devuelve la semana ISO.
- `.dt.hour`, `.dt.minute` y `.dt.second`: extraen la hora si la fecha incluye tiempo.
- `.dt.strftime("%Y-%m")`: da formato personalizado de fecha.

Ejemplo con varias partes:

```python
df["anio"] = df["fecha"].dt.year
df["mes"] = df["fecha"].dt.month
df["dia"] = df["fecha"].dt.day
df["trimestre"] = df["fecha"].dt.quarter
df["nombre_dia"] = df["fecha"].dt.day_name()
print(df[["fecha", "anio", "mes", "dia", "trimestre", "nombre_dia"]])

### Quick plot (optional)

Si quieres una visual rápida usa `matplotlib` (instalar `matplotlib` en `requirements.txt` si no está):

```python
import matplotlib.pyplot as plt

totales_por_pais = df.groupby("pais")["goles"].sum().sort_values(ascending=False)
totales_por_pais.head(10).plot(kind="bar", figsize=(8,4))
plt.title("Goles totales por pais (top 10)")
plt.ylabel("Goles")
plt.tight_layout()
plt.show()
```

Importante:

- No existe un `dt.component` general para fechas; lo normal es usar propiedades como `year`, `month`, `day` o `quarter`.
- `.dt` solo funciona en columnas con datos tipo fecha o tiempo.
- Si tu columna es texto, primero debes usar `to_datetime()`.
- Si quieres resumir por mes, a veces conviene usar `to_period("M")`.

---

## Ruta recomendada (de menor a mayor dificultad)

1. `01_ordenamiento_y_top.py`
2. `02_filtros_combinados.py`
3. `03_groupby_basico.py`
4. `04_groupby_multiple.py`
5. `05_merge_basico.py`
6. `06_pivot_table.py`
7. `07_fechas_y_resumen.py`

---

## Que practica cada reto

1. `01_ordenamiento_y_top.py`
Enfocado en ordenar por metricas (`goles`, `valor_millones`) y quedarte con top N.

2. `02_filtros_combinados.py`
Enfocado en filtros con varias reglas a la vez y uso de `isin()`.

3. `03_groupby_basico.py`
Enfocado en resumen por una sola categoria (por ejemplo, pais).

4. `04_groupby_multiple.py`
Enfocado en agrupacion por dos dimensiones (`pais` y `posicion`).

5. `05_merge_basico.py`
Enfocado en unir una tabla principal con otra auxiliar para enriquecer analisis.

6. `06_pivot_table.py`
Enfocado en construir una matriz de resumen para lectura rapida.

7. `07_fechas_y_resumen.py`
Enfocado en convertir texto a fecha, extraer mes y resumir por periodo.

8. `08_componentes_fecha.py`
Enfocado en practicar `.dt.year`, `.dt.month`, `.dt.day`, `.dt.day_name()`, `.dt.quarter` y `.dt.weekday`.

---

## Como estudiar este bloque

Antes de ejecutar:

1. Que pregunta de negocio intenta responder este reto?
2. Que metodo principal toca practicar?
3. Que columnas necesitas para responder esa pregunta?

Despues de ejecutar:

1. El resultado es interpretable para alguien no tecnico?
2. Puedes explicar por que ese metodo era el correcto?
3. Que cambiaria si ajustas una condicion o agrupacion?

---

## Errores comunes en nivel intermedio

1. Ordenar sin definir si el orden debe ser ascendente o descendente.
2. Aplicar filtros sin parentesis en condiciones compuestas.
3. Usar groupby sin definir bien que metricas calcular.
4. Hacer merge sin revisar la clave de union.
5. Tratar fechas como texto y no como datetime.

---

## Checklist de avance

1. Puedes obtener un top 10 ordenado correctamente.
2. Puedes crear 2 filtros compuestos distintos.
3. Puedes resumir por una y por dos categorias.
4. Puedes unir tablas y explicar diferencia entre inner y left.
5. Puedes construir un pivot table legible.
6. Puedes generar un resumen mensual con fechas.
7. Puedes extraer ano, mes, dia y otras partes de una fecha con `.dt`.
