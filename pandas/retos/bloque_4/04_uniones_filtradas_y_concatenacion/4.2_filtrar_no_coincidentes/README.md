# 4.2 - Anti-join

![pandas secondary logo](https://pandas.pydata.org/static/img/pandas_secondary.svg)

> [!NOTE]
> "La práctica consistente transforma lo difícil en dominio. Cada línea de código es un paso adelante."

En los DataFrames podemos ver este resultado porque no solo importa el valor típico de una columna, sino también qué tan separadas están sus observaciones; por eso usamos medidas de dispersión que nos ayudan a entender si los precios, el stock o cualquier otra variable están muy concentrados o demasiado variados.

## ¿Qué haremos?

Un anti-join te deja ver qué filas no encontraron pareja en la otra tabla y devuelve solo las columnas de la tabla izquierda.

- **¿Cómo encuentro filas sin coincidencia?** -> `merge(..., indicator=True)` + filtro por `_merge`
- **¿Qué conservas al final?** -> solo la tabla izquierda
- **¿Para qué sirve?** -> detectar ausencias, gaps o registros sin relación

> [!TIP]
> Es muy util cuando revisas cobertura de datos o quieres detectar socios sin actividad.

---

## ¿Qué vas a aprender?

- Cómo usar `indicator=True` para auditar el origen de cada fila.
- Cómo filtrar las filas `left_only`.
- Cómo construir un anti-join sin agregar columnas innecesarias.
- Cómo reconocer que un anti-join también es un join de filtrado.

---

## Errores comunes

- Crear listas de distinto largo en un diccionario de listas.
- Olvidar `index=False` al guardar CSV.
- No revisar el `head()` luego de leer un archivo.
