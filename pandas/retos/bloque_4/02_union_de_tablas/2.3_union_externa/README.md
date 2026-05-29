# 2.3 - Unión Externa

![pandas secondary logo](https://pandas.pydata.org/static/img/pandas_secondary.svg)

> [!NOTE]
> "La práctica consistente transforma lo difícil en dominio. Cada línea de código es un paso adelante."

En esta lección aprenderás la unión externa (`outer`) para conservar el universo completo de registros de ambas tablas. Cubriremos cómo interpretar los `NaN` cuando no hay coincidencias, auditar el origen de cada fila con `indicator=True`, usar `suffixes` para distinguir columnas duplicadas y limpiar o filtrar el resultado tras la unión.

**Documentación:** [Guía — Merge, join y concatenate](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html) — [API: pandas.merge](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge.html)

---

## ¿Qué haremos?

Trabajaremos con la biblioteca municipal. Aquí queremos conservar todos los socios y todas las sedes: cuando ninguna de las tablas tiene coincidencia, las columnas faltantes aparecerán como `NaN`.

- **¿Qué pasa si un socio o una sede no tiene pareja en la otra tabla?** -> `how='outer'`
-- **¿Y si la llave tiene distinto nombre?** -> `left_on` / `right_on`
- **¿Cómo auditar la unión?** -> `indicator=True`

> [!TIP]
> La unión externa es útil para obtener el universo completo de registros cuando ninguna de las tablas debe perderse.

### Idea visual

![Diagrama de union tipo merge](https://jtr13.github.io/cc19/resources/group38/full_join.png)

> [!IMPORTANT]
> `outer` conserva todas las filas de ambas tablas; donde no hay coincidencia, pandas rellena con `NaN`.

---

## ¿Qué vas a aprender?

- Qué significa `how='outer'`.
- Cómo usar `left_on`/`right_on` cuando las columnas llave difieren.
- Cómo interpretar `_merge` con `indicator=True` para auditar coincidencias.
- Qué sucede si hay duplicados de llave en cualquiera de las tablas.

---

## 1. Unir columnas con nombres distintos

Vamos a usar el mismo ejemplo de socios y sedes.

### Explicación de los parámetros clave

| Parámetro | Qué hace | Cuándo usarlo |
| --- | --- | --- |
| `left_on` | Nombre(s) de columna(s) en la tabla izquierda que actúan como llave para la unión. | Cuando la llave tiene distinto nombre entre los DataFrames. |
| `right_on` | Nombre(s) de columna(s) en la tabla derecha que coinciden con `left_on`. | Cuando la llave tiene distinto nombre entre los DataFrames. |
| `on` | Nombre(s) de columna(s) que existen con el mismo nombre en ambas tablas. | Si la llave comparte nombre en ambos DataFrames. |
| `how` | Tipo de unión. `'outer'` conserva todas las filas de ambas tablas. | Cuando quieres el universo completo de registros. |
| `indicator` | Agrega `_merge` indicando el origen (`left_only`, `right_only`, `both`). | Para auditar la unión. |
| `suffixes` | Sufijos para columnas repetidas en ambos DataFrames. | Para evitar nombres ambiguos en columnas compartidas. |

```python
import pandas as pd

df_socios = pd.DataFrame({
    "socio_id": [1, 2, 3, 4, 5],
    "nombre": ["Hugo", "Karen", "Marcos", "Felipe", "Catalina"],
    "ciudad": ["Ciudad de México", "Guadalajara", "Monterrey", "Tijuana", "Mérida"]
})

df_sedes = pd.DataFrame({
    "id_socio": [1, 2, 4, 6],
    "sede": ["Centro", "Norte", "Sur", "Oriente"]
})

resultado = df_socios.merge(
    df_sedes,
    left_on="socio_id",
    right_on="id_socio",
    how="outer"
)
print(resultado)
# Output esperado:
#    socio_id    nombre             ciudad  id_socio    sede
# 0       1.0      Hugo  Ciudad de México       1.0   Centro
# 1       2.0     Karen       Guadalajara       2.0    Norte
# 2       3.0    Marcos         Monterrey       NaN      NaN
# 3       4.0    Felipe           Tijuana       4.0      Sur
# 4       5.0  Catalina             Mérida       NaN      NaN
# 5       NaN       NaN               NaN       6.0  Oriente
```

### ¿Qué pasó?

- `how='outer'` conserva todas las filas de `df_socios` y `df_sedes`.
- Las filas que no encuentran pareja en la otra tabla aparecen con `NaN` en las columnas que faltan.
- Si alguna fila tiene múltiples coincidencias, se replicará según el número de coincidencias.

---

## 2. Ver de dónde vino cada fila

Usa `indicator=True` para añadir `_merge` y auditar resultados.

```python
resultado = df_socios.merge(
    df_sedes,
    left_on="socio_id",
    right_on="id_socio",
    how="outer",
    indicator=True
)
print(resultado)
# Output esperado (columna _merge):
#    socio_id    nombre             ciudad  id_socio    sede      _merge
# 0       1.0      Hugo  Ciudad de México       1.0   Centro        both
# 1       2.0     Karen       Guadalajara       2.0    Norte        both
# 2       3.0    Marcos         Monterrey       NaN      NaN   left_only
# 3       4.0    Felipe           Tijuana       4.0      Sur        both
# 4       5.0  Catalina             Mérida       NaN      NaN   left_only
# 5       NaN       NaN               NaN       6.0  Oriente  right_only
```

Posibles valores de `_merge`:

- `left_only`: solo estaba en la tabla izquierda.
- `right_only`: solo estaba en la tabla derecha.
- `both`: estaba en ambas.

---

## 3. Cuando ambas tablas tienen columnas repetidas

Si las tablas comparten columnas no llave, usa `suffixes` para distinguirlas.

```python
df_sucursales = pd.DataFrame({
    "socio_id": [1, 2, 4],
    "ciudad": ["Ciudad de México", "Guadalajara", "Tijuana"],
    "area": ["Centro", "Norte", "Sur"]
})

resultado = df_socios.merge(
    df_sucursales,
    on="socio_id",
    how="outer",
    suffixes=("_socio", "_sucursal")
)
print(resultado)
# Output:
#    socio_id    nombre   ciudad_socio   ciudad_sucursal    area
# 0         1      Hugo  Ciudad de México  Ciudad de México  Centro
# 1         2     Karen       Guadalajara       Guadalajara   Norte
# 2         3    Marcos         Monterrey               NaN      NaN
# 3         4    Felipe           Tijuana           Tijuana     Sur
# 4         5  Catalina             Mérida               NaN      NaN
# 5         NaN       NaN               NaN       Tijuana      Sur
```

---

## 4. ¿Cuándo usar estos parámetros?

- Usa `how='outer'` cuando necesites conservar todos los registros de ambas tablas.
- Usa `left_on`/`right_on` cuando las llaves difieran en nombre.
- Usa `indicator=True` para auditar y detectar filas `left_only`/`right_only`.
- Usa `suffixes` para evitar ambigüedad en columnas repetidas.

Como regla práctica, responde:

- ¿Necesitas el universo completo de registros? -> `how='outer'`.
- ¿Las llaves comparten nombre? -> usa `on`.
- ¿Necesitas auditar? -> `indicator=True`.

---

## Errores comunes (específicos a `outer join`)

1. Esperar que no aparezcan `NaN`: `how='outer'` preserva todas las filas; las ausencias aparecen como `NaN` y deben limpiarse o rellenarse.

2. Mezclar tipos en la llave (int vs str): causa no coincidencias; normaliza con `astype()` antes del `merge`.

3. Duplicados en cualquiera de las tablas que multiplican filas: audita con `value_counts()` y decide deduplicar o agregar.

4. Columnas con el mismo nombre en ambas tablas que confunden el resultado: usa `suffixes` o renombra antes.

5. No auditar el resultado tras el outer: usa `indicator=True` y revisa `resultado['_merge'].value_counts()` y `head()`.
