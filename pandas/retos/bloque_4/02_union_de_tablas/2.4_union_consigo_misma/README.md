# 2.4 - Unión consigo misma

![pandas secondary logo](https://pandas.pydata.org/static/img/pandas_secondary.svg)

> [!NOTE]
> "La práctica consistente transforma lo difícil en dominio. Cada línea de código es un paso adelante."

En esta lección veremos self-joins (unir una tabla consigo misma) para resolver relaciones internas —p. ej. `referido_por`. Aprenderás a emparejar la tabla consigo misma con `left_on`/`right_on`, evitar ambigüedades con `suffixes` y auditar coincidencias con `indicator=True`.

## ¿Qué haremos?

Usaremos el ejemplo de la biblioteca municipal con filas que referencian otras filas (por ejemplo, `referido_por` apunta a otro `socio_id`). Aprenderás a:

- Resolver relaciones padre-hijo con `merge()` entre dos vistas del mismo `DataFrame`.
- Emparejar filas usando `left_on` / `right_on` cuando la llave difiere.
- Controlar nombres duplicados con `suffixes` y auditar coincidencias con `indicator=True`.

> Un self-join usa exactamente las mismas reglas que cualquier `merge()`; la diferencia es conceptual: las dos tablas son la misma fuente de datos.

### Idea visual

![Diagrama self-join](https://www.devart.com/dbforge/sql/sqlcomplete/images/self-join-schema-small.png)

> [!IMPORTANT]
> En un self-join presta especial atención a `suffixes` y a qué columna actúa como llave, porque los nombres coincidentes aparecen dos veces en el resultado.

---

## ¿Qué vas a aprender?

- Qué es un self-join y cuándo aplicarlo.
- Cómo usar `left_on` / `right_on` cuando unes la tabla consigo misma.
- Cómo interpretar `_merge` si usas `indicator=True` para auditar.
- Cómo evitar columnas ambiguas con `suffixes` y cuándo usar índices (`left_index`/`right_index`).

**Documentación:** [Guía — Merge, join y concatenate](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html) — [API: pandas.merge](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge.html)

---

## 1. Unir columnas con nombres distintos

Usaremos el ejemplo de socios adaptado a un caso donde una fila referencia a otra dentro de la misma tabla (socios y referentes).

### Explicación de los parámetros clave

| Parámetro | Qué hace | Cuándo usarlo |
| --- | --- | --- |
| `left_on` | Nombre(s) de columna(s) en la tabla izquierda que actúan como llave para la unión. | Cuando la llave tiene distinto nombre entre las dos vistas del DataFrame. |
| `right_on` | Nombre(s) de columna(s) en la tabla derecha que coinciden con `left_on`. | Cuando la llave tiene distinto nombre entre las dos vistas del DataFrame. |
| `on` | Nombre(s) de columna(s) que existen con el mismo nombre en ambas vistas. | Si la llave comparte nombre en ambas vistas. |
| `how` | Tipo de unión. Valores: `'left'`, `'inner'`, `'right'`, `'outer'`. | Elige según si quieres conservar filas de la izquierda, derecha, ambas, o solo coincidencias. |
| `indicator` | Agrega la columna `_merge` indicando el origen de cada fila (`left_only`, `right_only`, `both`). | Para auditar y verificar coincidencias en la unión. |
| `suffixes` | Sufijos para columnas repetidas en ambas vistas (ej. `('_emp','_mgr')`). | Cuando hay columnas no llave con el mismo nombre y quieres diferenciarlas. |

```python
import pandas as pd

df_socios = pd.DataFrame({
    "socio_id": [1, 2, 3, 4, 5],
    "nombre": ["Hugo", "Karen", "Marcos", "Felipe", "Catalina"],
    "referido_por": [None, 1, 1, 2, 2]
})

# Unión consigo misma: emparejamos referido_por con socio_id
resultado = df_socios.merge(
    df_socios,
    left_on="referido_por",
    right_on="socio_id",
    how="left",
    suffixes=("","_referente")
)

print(resultado[["socio_id","nombre","referido_por","nombre_referente"]])
# Output esperado:
#    socio_id  nombre  referido_por nombre_referente
# 0         1    Hugo          None              NaN
# 1         2    Karen           1.0             Hugo
# 2         3   Marcos           1.0             Hugo
# 3         4   Felipe           2.0             Karen
# 4         5   Catalina         2.0             Karen
```

### ¿Qué pasó?

- `left_on='referido_por'` se empareja con `right_on='socio_id'` en la misma tabla.
- `suffixes` evita que `nombre` se sobreescriba y nos ofrece `nombre_referente`.
- `how='left'` conserva todos los socios aunque no tengan referente.

---

## 2. Ver de dónde vino cada fila

Puedes usar `indicator=True` para agregar `_merge` y auditar coincidencias, igual que en merges entre tablas distintas.

```python
resultado = df_socios.merge(
    df_socios,
    left_on="referido_por",
    right_on="socio_id",
    how="left",
    indicator=True,
    suffixes=("","_referente")
)
print(resultado[["socio_id","nombre","_merge"]])

# Output esperado (columna _merge):
#    socio_id  nombre    _merge
# 0         1    Hugo   left_only
# 1         2    Karen  both
# 2         3   Marcos  both
# 3         4   Felipe  both
# 4         5   Catalina both

```

Posibles valores de `_merge`:

- `left_only`: solo estaba en la vista izquierda.
- `right_only`: solo estaba en la vista derecha.
- `both`: estaba en ambas.

---

## 3. Cuando ambas vistas tienen columnas repetidas

Si las columnas no llave coinciden en nombre, usa `suffixes` para diferenciarlas.

```python
resultado = df_socios.merge(
    df_socios,
    left_on="referido_por",
    right_on="socio_id",
    how="left",
    suffixes=("_emp","_referente")
)
# Output esperado (sufijos):
#    socio_id  nombre_emp  referido_por  nombre_referente
# 0         1       Hugo          None               NaN
# 1         2      Karen           1.0              Hugo
# 2         3     Marcos           1.0              Hugo
# 3         4     Felipe           2.0             Karen
# 4         5   Catalina           2.0             Karen
```

Esto produce columnas como `nombre_emp` y `nombre_referente` para evitar confusión.

---

## 4. ¿Cuándo usar estos parámetros?

- Usa `left_on`/`right_on` cuando las llaves difieran en nombre.
- Usa `indicator=True` para auditar y detectar filas `left_only`/`right_only`.
- Usa `suffixes` para evitar ambigüedad en columnas repetidas.
- Considera `left_index`/`right_index` si la llave está en el índice.

Como regla práctica, responde:

- ¿La llave está en la misma tabla pero con distinto nombre? -> `left_on`/`right_on`.
- ¿Necesitas auditar? -> `indicator=True`.

---

## Errores comunes (específicos a `self-joins`)

1. Confundir las dos vistas de la misma tabla: asegúrate de que `left_on` y `right_on` referencien las columnas correctas (p. ej. `referido_por` vs `id`).

2. Crear productos cartesianos por llaves no únicas: deduplica o agrega la vista derecha antes del `merge`.

3. Sobrescribir columnas con el mismo nombre: usa `suffixes=('_orig','_ref')` para diferenciarlas.

4. Usar `on` cuando necesitas unir columnas distintas dentro de la misma tabla: emplea `left_on`/`right_on` o `left_index`/`right_index`.

5. No gestionar referencias faltantes (None/NaN): las filas sin referente tendrán `NaN` — trata con `fillna()` o lógica condicional.
