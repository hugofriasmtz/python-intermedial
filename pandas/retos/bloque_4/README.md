# Pandas Bloque 4 - Unir Datos en Pandas

![pandas secondary logo](https://pandas.pydata.org/static/img/pandas_secondary.svg)

> [!NOTE]
> Este bloque te enseña a combinar tablas con pandas usando ejemplos practicos de una biblioteca municipal.

---

## Mapa del bloque

| Orden | Tema | Que te deja hacer |
| --- | --- | --- |
| 01 | [Merge Basico](01_merge_basico/README.md) | Unir dos tablas con `merge()` y `on` |
| 02 | [Union por Izquierda](02_union_de_tablas/2.1_union_por_izquierda/README.md) | Unir por la izquierda y usar `left_on`, `right_on`, `indicator` y `suffixes` |
| 03 | [Union por Derecha](02_union_de_tablas/2.2_union_por_derecha/README.md) | Conservar filas de la derecha con `how='right'` |
| 04 | [Union Externa](02_union_de_tablas/2.3_union_externa/README.md) | Conservar todas las filas de ambas tablas (`how='outer'`) |

![Diagrama de union tipo merge](https://media.licdn.com/dms/image/v2/D4D22AQEo9Hlysrf9ig/feedshare-shrink_1280/B4DZiZv9XaHwAs-/0/1754926149542?e=1781136000&v=beta&t=B86F-QUTsXvmddGdtj7o4SNQ1Pdpqb8l2MtoU7p1xRI)

> [!TIP]
> Si vienes de Bloque 2 y 3, este bloque te ayudara a combinar informacion separada sin perder claridad.
> Aqui vas a ver salidas de consola completas para entender como cambia el resultado segun el tipo de union.
> Ejecuta los retos con el entorno virtual del proyecto: `.venv/bin/python`.

---

## Checklist rapido

- [ ] Unir dos tablas con una columna en comun.
- [ ] Entender por que `left join` conserva la tabla principal.
- [ ] Diferenciar `inner`, `left`, `right` y `outer`.
- [ ] Usar `left_on` y `right_on` cuando las columnas no tienen el mismo nombre.
- [ ] Revisar el origen de cada fila con `indicator=True`.
- [ ] Diferenciar columnas repetidas con `suffixes`.

> [!IMPORTANT]
> En este bloque los ejemplos son auto-contenidos y usan DataFrames creados en el propio README.
> Los nombres que vas a ver en los ejemplos son Hugo, Karen, Marcos, Felipe y Catalina.
> Si una combinacion puede duplicar filas, revisa primero si tus claves son unicas.
