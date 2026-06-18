# Pandas Bloque 4 - Unir Datos en Pandas

![pandas secondary logo](https://pandas.pydata.org/static/img/pandas_secondary.svg)

> [!NOTE]
> "La práctica consistente transforma lo difícil en dominio. Cada línea de código es un paso adelante."

---

## Mapa del bloque

| Orden | Tema | Qué te deja hacer |
| --- | --- | --- |
| 01 | [01_merge_basico](01_merge_basico/README.md) | Unir dos tablas con `merge()` y `on` |
| 02 | [02_union_de_tablas](02_union_de_tablas) | Practicar distintos tipos de `merge()` sobre tablas relacionadas |
| 03 | [03_union_por_indices](03_union_por_indices/README.md) | Unir DataFrames usando índices simples y MultiIndex |
| 04 | [04_uniones_filtradas_y_concatenacion](04_uniones_filtradas_y_concatenacion/README.md) | Filtrar coincidencias, validar uniones y reestructurar datos |

![Diagrama de union tipo merge](https://miro.medium.com/v2/resize:fit:1200/1*9eH1_7VbTZPZd9jBiGIyNA.png)

> [!TIP]
> Si vienes de Bloque 1, 2 y 3, este bloque te ayudará a combinar información separada sin perder claridad.
> Aquí vas a ver salidas de consola completas para entender cómo cambia el resultado según el tipo de unión.
> También encontrarás una guía dedicada a unir por índices y otra a filtrar, validar y reestructurar datos.
> Ejecuta los retos con el entorno virtual del proyecto: `.venv/bin/python`.

---

## Checklist rapido

- [ ] Unir tablas con `merge()` y `on`.
- [ ] Usar `left_on`, `right_on`, `indicator` y `suffixes`.
- [ ] Unir DataFrames con índices simples y MultiIndex.
- [ ] Hacer semi-joins, anti-joins y concatenación vertical.
- [ ] Validar la cardinalidad de una unión con `validate`.
- [ ] Concatenar con `ignore_index` y `keys` cuando sea necesario.
- [ ] Usar `merge_ordered()` para datos ordenados.
- [ ] Usar `merge_asof()` para coincidencias cercanas.
- [ ] Filtrar filas con `query()`.
- [ ] Reestructurar tablas con `melt()`.

---
