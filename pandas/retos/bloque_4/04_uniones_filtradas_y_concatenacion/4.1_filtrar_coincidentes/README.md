# 4.1 - Semi-join (Filtrar coincidencias)

![pandas secondary logo](https://pandas.pydata.org/static/img/pandas_secondary.svg)

> [!NOTE]
> "La práctica consistente transforma lo difícil en dominio. Cada línea de código es un paso adelante."

En este punto del bloque vas a trabajar con un patrón de filtrado por coincidencia. La idea es conservar en la tabla izquierda únicamente las filas que también existen en la tabla derecha y evitar traer columnas adicionales.

---

## ¿Qué haremos?

Partiremos de dos tablas sencillas y aplicaremos un filtrado por coincidencia. Después veremos cuándo conviene usar `isin()` directamente, cuándo usar `merge()` para auditar coincidencias y cómo comprobar que el resultado solo conserve las filas deseadas.

- **¿Cómo me quedo solo con las filas que sí coinciden?** -> `isin()`
- **¿Qué tabla se conserva al final?** -> solo la de la izquierda
- **¿En qué se diferencia de un `inner join`?** -> no agrega columnas nuevas ni repite filas de la derecha

> [!TIP]
> Si solo necesitas filtrar filas manteniendo la estructura de la tabla izquierda, `isin()` es la opción más clara y eficiente.
> [!IMPORTANT]
> Un semi-join filtra filas; si necesitas columnas de ambas tablas, usa `merge(..., how='inner')`.

---

## ¿Qué vas a aprender?

- Aplicar `isin()` para filtrar por coincidencia.
- Auditar coincidencias con `merge()` antes de filtrar.
- Verificar tipos y unicidad de claves para evitar resultados inesperados.

**Documentación:** [pandas.Series.isin](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.isin.html) — [pandas.DataFrame.merge](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge.html)

---

## 1. Convertir una columna en índice

La forma más común de trabajar un semi-join es elegir una columna que identifique cada fila de forma clara y que exista en ambas tablas.

Vamos a trabajar con una tabla de socios de una biblioteca municipal y una tabla de préstamos.

### Parámetros clave de `set_index()`

| Parámetro | Qué hace | Cuándo usarlo |
| --- | --- | --- |
| `keys` | Columna o lista de columnas que pasarán a formar la llave de comparación. | Cuando quieres usar una columna común para filtrar coincidencias. |
| `drop` | Elimina la columna original después de convertirla en índice. | Usa `True` si ya no la necesitas como columna; `False` si quieres conservarla. |
| `append` | Agrega las nuevas claves al índice existente. | Cuando quieres construir una llave compuesta sin perder la actual. |
| `inplace` | Modifica el DataFrame original directamente. | Úsalo solo si quieres evitar crear una copia. |
| `verify_integrity` | Verifica que las nuevas claves no tengan duplicados. | Cuando necesitas asegurar unicidad desde el principio. |

```python
import pandas as pd

df_socios = pd.DataFrame({
    "id": [1, 2, 3, 4, 5, 6],
    "nombre": ["Hugo", "Karen", "Felipe", "Catalina", "Marcos", "Arturo"],
    "ciudad": ["Ciudad de México", "Guadalajara", "Monterrey", "Tijuana", "Mérida", "Puebla"]
})

df_prestamos = pd.DataFrame({
    "id": [1, 2, 4, 6],
    "libro": ["Cien años de soledad", "Rayuela", "El principito", "La sombra del viento"]
})

# Aplicamos la máscara booleana para conservar solo las coincidencias.
ids_con_prestamo = df_socios["id"].isin(df_prestamos["id"])
semi_join = df_socios[ids_con_prestamo]

print(semi_join)
# Output:
#    id    nombre              ciudad
# 0   1      Hugo  Ciudad de México
# 1   2     Karen       Guadalajara
# 3   4  Catalina            Tijuana
# 5   6    Arturo             Puebla
```

### ¿Por qué sirve esto?

- Porque deja la coincidencia de claves en un lugar claro para filtrar filas.
- Porque muchas operaciones de pandas se vuelven más limpias cuando la comparación se hace con una llave compartida.
- Porque más adelante podrás usar `merge()` para auditar coincidencias antes de filtrar.

Ejemplo corto: si `id` identifica unívocamente a cada socio, comparar con `isin()` facilita quedarte solo con los registros que aparecen en la otra tabla.

Si quieres auditar primero las coincidencias, usa `merge()`.

```python
auditoria = df_socios.merge(df_prestamos, on="id", how="inner")
semi_from_merge = auditoria[df_socios.columns] if not auditoria.empty else pd.DataFrame(columns=df_socios.columns)

print(semi_from_merge)
# Output:
#    id    nombre              ciudad
# 0   1      Hugo  Ciudad de México
# 1   2     Karen       Guadalajara
# 2   4  Catalina            Tijuana
# 3   6    Arturo             Puebla
```

Este enfoque es útil cuando quieres ver las coincidencias antes de decidir si solo filtras o si además mezclas columnas.

---

## 2. Revisar si el índice quedó bien

Después de comparar las claves, conviene validar el resultado antes de seguir.

```python
coincidencias = ids_con_prestamo.sum()
no_coincidencias = (~ids_con_prestamo).sum()

print(coincidencias)
print(no_coincidencias)
# Output:
# 4
# 2
```

Posibles revisiones útiles:

- `ids_con_prestamo.sum()`: cuenta cuántas filas sí coinciden.
- `(~ids_con_prestamo).sum()`: cuenta cuántas filas no coinciden.
- `df_socios['id'].dtype` y `df_prestamos['id'].dtype`: confirma que el tipo sea consistente.

Este paso importa porque comparar claves con tipos distintos o con duplicados inesperados suele causar resultados confusos más adelante.

---

## 3. Índices compuestos cuando una sola columna no alcanza

A veces una sola columna no identifica de forma única cada coincidencia. En ese caso puedes comparar dos columnas al mismo tiempo.

```python
df_visitas = pd.DataFrame({
    "ciudad": ["Ciudad de México", "Ciudad de México", "Guadalajara", "Guadalajara"],
    "sucursal": ["Centro", "Sur", "Norte", "Poniente"],
    "visitas": [1200, 900, 800, 700]
})

df_eventos = pd.DataFrame({
    "ciudad": ["Ciudad de México", "Guadalajara", "Guadalajara"],
    "sucursal": ["Centro", "Norte", "Poniente"],
    "eventos": [5, 3, 2]
})

# Usamos dos columnas porque juntas identifican la coincidencia con más precisión.
mascara_multi = df_visitas[["ciudad", "sucursal"]].apply(tuple, axis=1).isin(
    df_eventos[["ciudad", "sucursal"]].apply(tuple, axis=1)
)
df_visitas_filtrado = df_visitas[mascara_multi]

print(df_visitas_filtrado)
# Output:
#               ciudad sucursal  visitas
# 0  Ciudad de México   Centro     1200
# 2      Guadalajara   Norte      800
```

Este patrón te deja preparado para comparar más de una clave cuando una sola columna no alcanza.

---

## 4. ¿Cuándo usar `set_index()`?

- Usa `isin()` cuando una columna identifica mejor las coincidencias entre dos tablas.
- Usa `merge()` cuando todavía necesitas auditar las filas que coinciden.
- Usa `drop_duplicates()` cuando necesitas evitar claves repetidas antes de filtrar.
- Usa una comparación compuesta cuando una sola columna no basta para identificar coincidencias.

Como regla práctica, pregúntate esto antes de filtrar:

- ¿Esta columna representa una llave real que aparece en ambas tablas?
- ¿Voy a usar solo las filas que coinciden o también necesito columnas nuevas?
- ¿Necesito evitar duplicados desde el inicio?
- ¿Me conviene una coincidencia simple o una compuesta?

---

## Errores comunes

1. Elegir una columna con tipos distintos entre tablas: eso complica la comparación. Revisa `df['id'].dtype` antes de seguir.

2. Olvidar que `isin()` crea una máscara booleana: si esperabas un DataFrame completo, usa esa máscara para filtrar.

3. Perder una coincidencia porque la llave no está limpia: si quieres evitar problemas, usa `drop_duplicates()` o normaliza tipos.

4. Construir una comparación con claves inconsistentes entre tablas: si luego vas a filtrar, asegúrate de que ambas llaves tengan el mismo tipo.

5. Usar una llave incompleta para identificar coincidencias: si una sola columna no alcanza, compara varias columnas al mismo tiempo.
