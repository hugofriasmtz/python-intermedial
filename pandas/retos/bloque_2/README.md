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
