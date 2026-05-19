# Pandas Bloque 2 - Transformaciones y Operaciones Aplicadas

![pandas secondary logo](https://pandas.pydata.org/static/img/pandas_secondary.svg)

> [!NOTE]
> Este bloque consolida operaciones intermedias de `pandas` usando ejemplos practicos con estudiantes.

Este README solo sirve como mapa del bloque. Para aprender cada tema, entra al README de su carpeta.

---

## Mapa del bloque

| Orden | Tema | Que te deja hacer |
| --- | --- | --- |
| 01 | [Ordenamiento y Top](01_ordenamiento_y_top/README.md) | Ordenar datos y obtener top/bottom N |
| 02 | [Filtros Combinados](02_filtros_combinados/README.md) | Filtrar con multiples condiciones y texto |
| 03 | [Groupby Basico](03_groupby_basico/README.md) | Resumir metricas por una categoria |
| 04 | [Groupby Multiple](04_groupby_multiple/README.md) | Agrupar por dos o mas dimensiones |
| 05 | [Merge Basico](05_merge_basico/README.md) | Unir DataFrames con distintos tipos de join |
| 06 | [Pivot Table](06_pivot_table/README.md) | Construir tablas cruzadas para comparar |
| 07 | [Fechas y Resumen](07_fechas_y_resumen/README.md) | Convertir fechas y resumir por periodos |
| 08 | [Componentes de Fecha](08_componentes_fecha/README.md) | Extraer partes de fecha con `.dt` |

> [!TIP]
> Si vienes de Bloque 1, sigue el orden de arriba hacia abajo.
> Ejecuta los retos con el entorno virtual del proyecto: `.venv/bin/python`.

---

## Checklist rapido

- [ ] Ordenar un DataFrame por una columna numerica ascendente y descendente.
- [ ] Obtener top N y bottom N con `nlargest()` y `nsmallest()`.
- [ ] Construir filtros con `isin()`, `str.contains()`, `&`, `|` y `~`.
- [ ] Resumir datos con `groupby()` y `agg()`.
- [ ] Agrupar por dos columnas y aplanar con `reset_index()`.
- [ ] Combinar tablas con `merge()` usando `inner` y `left`.
- [ ] Crear una `pivot_table()` con `index`, `columns` y `aggfunc`.
- [ ] Convertir texto a fecha con `to_datetime()`.
- [ ] Extraer ano, mes y dia con accesores `.dt`.

> [!IMPORTANT]
> En este bloque los ejemplos son auto-contenidos y usan un DataFrame de estudiantes.
> Si modificas columnas durante una practica, guarda una copia cuando necesites conservar el estado original.
