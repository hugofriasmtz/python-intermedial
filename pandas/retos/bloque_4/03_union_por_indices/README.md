# 03 - Unión por índices

![pandas secondary logo](https://pandas.pydata.org/static/img/pandas_secondary.svg)

> [!NOTE]
> La práctica consistente transforma lo difícil en dominio. Cada línea de código es un paso adelante.

En este bloque aprenderás a usar índices como llave para unir DataFrames: cuándo usar `set_index()`, `join()` o `merge()` con `left_index/right_index`, y cómo trabajar con `MultiIndex`.

---

## ¿Qué haremos?

Mostraremos técnicas prácticas para unir datos cuando la llave está en el índice: crear índices, unir tablas que comparten índice, fusionar por índices simples o múltiples, y mezclar índice con columnas.

## Mapa del bloque

| Orden | Tema | Qué te permite hacer |
| --- | --- | --- |
| 01 | [Configurar un índice](3.1_configurar_un_indice/README.md) | Convertir columnas en índice y validar unicidad |
| 02 | [Unir datasets por índice](3.2_unir_datasets_por_indice/README.md) | Unir datasets que ya comparten el mismo índice usando `join()` |
| 03 | [Fusionar sobre el índice](3.3_fusionar_sobre_el_indice/README.md) | Fusionar usando `left_index=True` y `right_index=True` con `merge()` |
| 04 | [Datasets con MultiIndex](3.4_datasets_multiindice/README.md) | Crear y trabajar con `MultiIndex` (llaves compuestas) |
| 05 | [Fusión con MultiIndex](3.5_fusion_multiindice/README.md) | Unir tablas con índices múltiples y auditar coincidencias |
| 06 | [Unir índice con columna](3.6_unir_indice_con_columna/README.md) | Unir un índice con una columna sin resetear el índice |

> [!TIP]
> Si vienes de las uniones por columnas, aquí verás los mismos conceptos aplicados al índice. Ejecuta los ejemplos con el intérprete del entorno del proyecto: `.venv/bin/python`.

---

## Checklist rápido

- [ ] Convertir una columna en índice con `set_index()`.
- [ ] Unir dos tablas que comparten el mismo índice con `join()`.
- [ ] Usar `merge()` con `left_index=True` y `right_index=True`.
- [ ] Crear y consultar un `MultiIndex`.
- [ ] Combinar tablas con índices múltiples.
- [ ] Unir un índice con una columna usando `left_on`/`right_on`.

> [!IMPORTANT]
> Los ejemplos son auto-contenidos y usan DataFrames en el propio README. Antes de unir, valida la unicidad de tus llaves para evitar productos cartesianos.
---
