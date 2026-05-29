# 2.1 - Unión por Izquierda

![pandas secondary logo](https://pandas.pydata.org/static/img/pandas_secondary.svg)

> [!NOTE]
> "La práctica consistente transforma lo difícil en dominio. Cada línea de código es un paso adelante."

En las uniones de DataFrames importa el valor de la llave, cómo se combinan las filas y qué registros quedan sin coincidencia. Aquí aprenderás a identificar filas sin emparejar, auditar el origen de cada registro y manejar columnas repetidas para interpretar correctamente un `left join`.

---

## ¿Qué haremos?

Ahora que ya sabes unir dos tablas por una columna común, aquí vas a profundizar en la unión por izquierda: cómo conservar la tabla principal, cómo manejar columnas con nombres distintos y cómo seguir el origen de cada registro cuando faltan coincidencias.

- **¿Cómo conservo todos los socios aunque falte información relacionada?** -> `how='left'`
- **¿Y si la llave se llama distinto en cada tabla?** -> `left_on` y `right_on`
- **¿Cómo sé qué filas vinieron de qué tabla?** -> `indicator=True`
- **¿Cómo evitar confusiones cuando ambas tablas tienen columnas con el mismo nombre?** -> `suffixes`

> [!TIP]
> Aquí el foco es entender el `left join` con casos reales, no solo memorizar parámetros.

### Idea visual

![Diagrama de union por izquierda](https://static.pingcap.com/files/2024/05/23092316/left-outer-join.png)

> [!IMPORTANT]
> Estos parámetros aparecen mucho en proyectos reales porque las tablas no siempre vienen listas para unirlas directamente.
> El tema central aquí es la unión por izquierda; los demás parámetros aparecen como apoyo para casos reales.

---

## ¿Qué vas a aprender?

- Cómo usar `how='left'` como unión principal.
- Cómo usar `left_on` y `right_on`.
- Para qué sirve `indicator=True`.
- Cómo agregar `suffixes` para diferenciar columnas repetidas.
- Cómo interpretar resultados con coincidencias parciales.
- Cómo leer una salida con filas que solo aparecen en una tabla.

**Documentación:** [Guía — Merge, join y concatenate](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html) — [API: pandas.merge](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge.html)

---

## 1. Unir columnas con nombres distintos

A veces la llave no se llama igual en ambas tablas.

Vamos a trabajar con una biblioteca municipal donde tenemos socios y lectores asignados a diferentes sedes.

### Explicación de los parámetros clave

| Parámetro | Qué hace | Cuándo usarlo |
| --- | --- | --- |
| `left_on` | Nombre(s) de columna(s) en la tabla izquierda que actúan como llave para la unión. | Cuando la llave tiene distinto nombre entre los DataFrames. |
| `right_on` | Nombre(s) de columna(s) en la tabla derecha que coinciden con `left_on`. | Cuando la llave tiene distinto nombre entre los DataFrames. |
| `on` | Nombre(s) de columna(s) que existen con el mismo nombre en ambas tablas. | Cuando la columna llave comparte nombre en ambos DataFrames (simplifica la llamada). |
| `how` | Tipo de unión. Valores: `'left'`, `'inner'`, `'right'`, `'outer'`. | Elige según si quieres conservar filas de la izquierda, derecha, ambas, o solo coincidencias. |
| `indicator` | Agrega la columna `_merge` indicando el origen de cada fila (`left_only`, `right_only`, `both`). | Para auditar y verificar coincidencias en la unión. |
| `suffixes` | Sufijos para columnas repetidas en ambos DataFrames (ej. `('_socio','_sucursal')`). | Cuando hay columnas no llave con el mismo nombre y quieres diferenciarlas. |

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
    how="left"
)
print(resultado)
# Output:
#    socio_id    nombre             ciudad  id_socio    sede
# 0         1      Hugo  Ciudad de México       1.0   Centro
# 1         2     Karen       Guadalajara       2.0    Norte
# 2         3    Marcos         Monterrey       NaN      NaN
# 3         4    Felipe           Tijuana       4.0      Sur
# 4         5  Catalina             Mérida       NaN      NaN
```

### ¿Por qué sirve esto?

- Porque muchas bases reales no usan el mismo nombre de columna.
- Porque evita renombrar datos manualmente antes de unir.
- Porque un `left join` te deja conservar toda la lista de socios aunque falte una sede.

Ejemplo corto: si `left_on="socio_id"` y `right_on="id_socio"`, pandas empareja filas donde `df_socios.socio_id == df_sedes.id_socio`. Con `how='left'` se mantienen todos los `socio_id` de `df_socios` aunque no existan en `df_sedes`.

Si las columnas tienen el mismo nombre en ambas tablas puedes usar `on="socio_id"` en lugar de `left_on`/`right_on`.

Ejemplo con `on` (equivalente cuando la columna comparte nombre):

```python
resultado_on = df_socios.merge(
    df_sucursales,
    on="socio_id",
    how="left"
)
print(resultado_on)
# Output:
#    socio_id    nombre             ciudad  ciudad_sucursal    area
# 0         1      Hugo  Ciudad de México  Ciudad de México  Centro
# 1         2     Karen       Guadalajara       Guadalajara   Norte
# 2         3    Marcos         Monterrey               NaN      NaN
# 3         4    Felipe           Tijuana           Tijuana     Sur
# 4         5  Catalina             Mérida               NaN      NaN
```

Este último es más simple, pero `left_on`/`right_on` es necesario cuando las columnas llave se llaman distinto.

---

## 2. Ver de donde vino cada fila

`indicator=True` agrega una columna que muestra si la fila vino de la izquierda, de la derecha o de ambas.

```python
resultado = df_socios.merge(
    df_sedes,
    left_on="socio_id",
    right_on="id_socio",
    how="outer",
    indicator=True
)
print(resultado)
# Output:
#    socio_id    nombre             ciudad  id_socio    sede      _merge
# 0       1.0      Hugo  Ciudad de Mexico      1.0  Centro        both
# 1       2.0     Karen       Guadalajara      2.0   Norte        both
# 2       3.0    Marcos         Monterrey      NaN     NaN   left_only
# 3       4.0    Felipe           Tijuana      4.0     Sur        both
# 4       5.0  Catalina             Merida      NaN     NaN   left_only
# 5       NaN       NaN               NaN      6.0 Oriente  right_only
```

Posibles valores de `_merge`:

- `left_only`: solo estaba en la tabla izquierda.
- `right_only`: solo estaba en la tabla derecha.
- `both`: estaba en ambas.

Este parámetro es muy útil cuando quieres auditar una unión y confirmar que no perdiste registros.

---

## 3. Cuando ambas tablas tienen columnas repetidas

Si dos tablas comparten nombres de columnas que no son la llave, puedes usar `suffixes`.

En este ejemplo ambas tablas tienen una columna llamada `ciudad`.

```python
df_sucursales = pd.DataFrame({
    "socio_id": [1, 2, 4],
    "ciudad": ["Ciudad de Mexico", "Guadalajara", "Tijuana"],
    "area": ["Centro", "Norte", "Sur"]
})

resultado = df_socios.merge(
    df_sucursales,
    on="socio_id",
    how="left",
    suffixes=("_socio", "_sucursal")
)
print(resultado)
# Output:
#    socio_id    nombre   ciudad_socio   ciudad_sucursal    area
# 0         1      Hugo  Ciudad de Mexico  Ciudad de Mexico  Centro
# 1         2     Karen       Guadalajara       Guadalajara   Norte
# 2         3    Marcos         Monterrey               NaN      NaN
# 3         4    Felipe           Tijuana           Tijuana     Sur
# 4         5  Catalina             Merida               NaN      NaN
```

Esto ayuda a distinguir columnas con el mismo nombre en ambos DataFrames.

Si no usas `suffixes`, pandas te deja nombres ambiguos y luego cuesta leer el resultado.

---

## 4. ¿Cuándo usar estos parametros?

- Usa `how='left'` cuando quieras conservar la tabla principal.
- Usa `left_on` y `right_on` cuando las llaves tienen nombres distintos.
- Usa `indicator=True` cuando quieres auditar el resultado.
- Usa `suffixes` cuando hay columnas repetidas y quieres diferenciarlas.

Como regla práctica, empieza por responder estas preguntas:

- ¿La llave tiene el mismo nombre en ambas tablas?
- ¿Quiero conservar todas las filas de la izquierda?
- ¿Necesito saber de dónde salió cada fila?
- ¿Hay columnas repetidas que deban diferenciarse?

---

## Errores comunes (específicos a `left join`)

1. Confundir `left` con `inner`: usar `how='left'` conserva todas las filas de la izquierda (no filtra coincidencias). Revisa `_merge` si esperabas solo coincidencias.

2. Esperar valores no nulos en columnas de la derecha: las filas sin pareja quedan con `NaN`; maneja con `fillna()` o comprobaciones previas.

3. Mapear mal `left_on`/`right_on` (intercambiarlos): si inviertes las columnas obtendrás coincidencias incorrectas o muchos `NaN`. Verifica que `left_on` pertenezca al DataFrame izquierdo.

4. Duplicados en la tabla derecha que replican filas izquierdas: si la tabla derecha tiene varias filas por llave, la izquierda se repetirá. Solución: deduplicar o agregar la derecha antes del `merge`.

5. Olvidar `suffixes` cuando hay columnas no llave con el mismo nombre: puede crear columnas ambiguas; usa `suffixes=('_izq','_der')` o renombra antes.
