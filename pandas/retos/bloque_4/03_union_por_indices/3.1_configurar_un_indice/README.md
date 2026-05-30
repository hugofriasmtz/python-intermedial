# 3.1 - Configurar un índice

![pandas secondary logo](https://pandas.pydata.org/static/img/pandas_secondary.svg)

> [!NOTE]
> "La práctica consistente transforma lo difícil en dominio. Cada línea de código es un paso adelante."

En este punto del bloque vas a preparar DataFrames para trabajar con índices como llave. La idea es convertir una columna en índice, revisar si ese índice sirve para unir datos después y evitar errores por duplicados o tipos inconsistentes.

---

## ¿Qué haremos?

Partiremos de una tabla sencilla y la convertiremos en un DataFrame indexado. Después veremos cuándo conviene dejar la columna original, cuándo eliminarla y cómo validar que el índice quedó listo para operaciones como `join()` o `merge()` por índice.

- **¿Cómo convierto una columna en índice?** -> `set_index()`
- **¿Qué pasa con la columna original?** -> `drop=True` o `drop=False`
- **¿Cómo verifico que el índice no tenga duplicados?** -> `index.is_unique`
- **¿Cómo preparo un índice para unir tablas después?** -> revisar tipo, nombre y unicidad

> [!TIP]
> Si el índice queda limpio desde el inicio, las uniones por índice después son más simples y menos propensas a errores.

### Idea visual

![Diagrama de indice en pandas](https://pandas.pydata.org/docs/_images/02_04.svg)

> [!IMPORTANT]
> Un índice no es solo una etiqueta visual: pandas lo usa para localizar, alinear y combinar filas.

---

## ¿Qué vas a aprender?

- Cómo usar `set_index()` para mover una columna al índice.
- Cómo conservar la columna original con `drop=False` cuando todavía la necesitas.
- Cómo validar la unicidad del índice con `index.is_unique`.
- Cómo revisar el nombre del índice con `index.name`.
- Cómo preparar datos para uniones por índice más adelante.

**Documentación:** [Guía — Indexing and selecting data](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html) — [API: pandas.DataFrame.set_index](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.set_index.html)

---

## 1. Convertir una columna en índice

La forma más común de preparar un DataFrame para uniones por índice es elegir una columna que identifique cada fila de forma clara.

Vamos a trabajar con una tabla de socios de una biblioteca municipal.

### Parámetros clave de `set_index()`

| Parámetro | Qué hace | Cuándo usarlo |
| --- | --- | --- |
| `keys` | Columna o lista de columnas que pasarán a formar el índice. | Cuando quieres usar una llave como índice. |
| `drop` | Elimina la columna original después de convertirla en índice. | Usa `True` si ya no la necesitas como columna; `False` si quieres conservarla. |
| `append` | Agrega las nuevas claves al índice existente. | Cuando quieres construir un índice compuesto sin perder el actual. |
| `inplace` | Modifica el DataFrame original directamente. | Úsalo solo si quieres evitar crear una copia. |
| `verify_integrity` | Verifica que las nuevas claves no tengan duplicados. | Cuando necesitas asegurar unicidad desde el principio. |

```python
import pandas as pd

df_socios = pd.DataFrame({
    "socio_id": [101, 102, 103, 104],
    "nombre": ["Hugo", "Karen", "Mariana", "Lucía"],
    "ciudad": ["Ciudad de México", "Guadalajara", "Monterrey", "Mérida"]
})

# Convertimos socio_id en índice porque identifica cada fila de forma única.
df_socios_indexados = df_socios.set_index("socio_id")

print(df_socios_indexados)
# Output:
#             nombre             ciudad
# socio_id
# 101          Hugo  Ciudad de México
# 102         Karen       Guadalajara
# 103       Mariana         Monterrey
# 104         Lucía             Mérida
```

### ¿Por qué sirve esto?

- Porque deja la llave en un lugar más natural para unir y localizar filas.
- Porque muchas operaciones de pandas se vuelven más limpias cuando el índice representa la identidad de cada registro.
- Porque más adelante podrás usar `join()` o `merge(..., left_index=True, right_index=True)` sin tener que rehacer la estructura.

Ejemplo corto: si `socio_id` identifica unívocamente a cada socio, convertirlo en índice facilita búsquedas como `df.loc[102]` y uniones por índice.

Si quieres conservar la columna original, usa `drop=False`.

```python
df_socios_con_columna = df_socios.set_index("socio_id", drop=False)

print(df_socios_con_columna)
# Output:
#           socio_id   nombre             ciudad
# socio_id
# 101            101     Hugo  Ciudad de México
# 102            102    Karen       Guadalajara
# 103            103  Mariana         Monterrey
# 104            104    Lucía             Mérida
```

Este enfoque es útil cuando todavía quieres ver la columna en la tabla, pero ya necesitas trabajar con el índice.

---

## 2. Revisar si el índice quedó bien

Después de configurar el índice, conviene validarlo antes de seguir.

```python
indice_unico = df_socios_indexados.index.is_unique
nombre_indice = df_socios_indexados.index.name

print(indice_unico)
print(nombre_indice)
# Output:
# True
# socio_id
```

Posibles revisiones útiles:

- `index.is_unique`: confirma que no hay llaves repetidas.
- `index.name`: confirma que el índice tiene un nombre claro.
- `index.dtype`: confirma que el tipo sea consistente con otras tablas.

Este paso importa porque un índice con duplicados o tipos distintos suele causar uniones confusas más adelante.

---

## 3. Índices compuestos cuando una sola columna no alcanza

A veces una sola columna no identifica de forma única cada fila. En ese caso puedes crear un índice compuesto.

```python
df_visitas = pd.DataFrame({
    "ciudad": ["Ciudad de México", "Ciudad de México", "Guadalajara", "Guadalajara"],
    "sucursal": ["Centro", "Sur", "Norte", "Poniente"],
    "visitas": [1200, 900, 800, 700]
})

# Usamos dos columnas porque juntas identifican la fila con más precisión.
df_visitas_indexado = df_visitas.set_index(["ciudad", "sucursal"])

print(df_visitas_indexado)
# Output:
#                               visitas
# ciudad            sucursal
# Ciudad de México  Centro        1200
#                   Sur            900
# Guadalajara       Norte          800
#                   Poniente       700
```

Este patrón te deja preparado para trabajar con `MultiIndex` en el siguiente subtema.

---

## 4. ¿Cuándo usar `set_index()`?

- Usa `set_index()` cuando una columna identifica mejor a cada fila que un número de posición.
- Usa `drop=False` cuando todavía necesitas la columna como dato visible.
- Usa `verify_integrity=True` cuando quieres detectar llaves repetidas de inmediato.
- Usa un índice compuesto cuando una sola columna no basta para identificar registros.

Como regla práctica, pregúntate esto antes de indexar:

- ¿Esta columna representa una llave real?
- ¿Voy a unir esta tabla con otra más adelante?
- ¿Necesito evitar duplicados desde el inicio?
- ¿Me conviene un índice simple o uno compuesto?

---

## Errores comunes

1. Elegir una columna con duplicados para usarla como índice: eso complica búsquedas y uniones. Revisa `index.is_unique` antes de seguir.

2. Olvidar que `set_index()` crea una copia por defecto: si esperabas modificar el DataFrame original, usa `inplace=True` o reasigna el resultado.

3. Perder una columna que todavía necesitas: si quieres conservarla, usa `drop=False`.

4. Construir un índice con tipos inconsistentes entre tablas: si luego vas a unir, asegúrate de que ambas llaves tengan el mismo tipo.

5. Usar una llave incompleta para identificar filas: si una sola columna no alcanza, crea un índice compuesto con varias columnas.
