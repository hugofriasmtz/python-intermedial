# 3.6 - Unir índice con columna (`left_index` / `right_on`)

![pandas secondary logo](https://pandas.pydata.org/static/img/pandas_secondary.svg)

> [!NOTE]
> "La práctica consistente transforma lo difícil en dominio. Cada línea de código es un paso adelante."

En esta última parte vas a combinar una tabla que tiene la llave en el índice con otra que conserva la llave como columna. Es una situación muy común cuando una tabla ya fue indexada y la otra todavía no.

---

## ¿Qué haremos?

Mostraremos cómo unir un índice con una columna sin tener que usar `reset_index()`. También veremos cómo revisar el resultado y cómo detectar llaves que quedaron solo de un lado.

- **¿Cómo uno índice con columna?** -> `left_index=True` y `right_on=...`
- **¿Cómo hago la unión inversa?** -> `right_index=True` y `left_on=...`
- **¿Cómo audito el origen de cada fila?** -> `indicator=True`
- **¿Cómo evito `reset_index()` innecesarios?** -> usando directamente `merge()`

> [!TIP]
> Esta técnica te ahorra pasos cuando una tabla ya está indexada y la otra todavía conserva la llave como columna.

> [!IMPORTANT]
> El emparejamiento depende de que el índice y la columna representen la misma llave y tengan el mismo tipo.

---

## ¿Qué vas a aprender?

- Cómo usar `left_index`/`right_on` para unir índice con columna.
- Cómo usar `right_index`/`left_on` cuando la dirección cambia.
- Cómo evitar `reset_index()` innecesarios.
- Cómo auditar el resultado con `indicator=True`.
- Cómo interpretar filas que solo existen en uno de los dos lados.

**Documentación:** [Guía — Merge, join y concatenate](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html) — [API: pandas.merge](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge.html)

---

## 1. Unir un índice con una columna

Cuando una tabla ya tiene la llave en el índice y la otra la conserva como columna, `merge()` permite combinarlas directamente.

Vamos a trabajar con socios y pagos.

### Parámetros clave

| Parámetro | Qué hace | Cuándo usarlo |
| --- | --- | --- |
| `left_index` | Usa el índice del DataFrame izquierdo como llave. | Cuando la llave está en el índice. |
| `right_on` | Usa una columna del DataFrame derecho como llave. | Cuando la otra tabla conserva la llave como columna. |
| `left_on` | Usa una columna del DataFrame izquierdo como llave. | Cuando la columna está del lado izquierdo. |
| `right_index` | Usa el índice del DataFrame derecho como llave. | Cuando la llave está en el índice derecho. |
| `indicator` | Agrega `_merge`. | Cuando quieres auditar el origen de cada fila. |

```python
import pandas as pd

df_socios = pd.DataFrame({
    "socio_id": [1, 2, 3, 4, 5],
    "nombre": ["Hugo", "Karen", "Marcos", "Felipe", "Catalina"]
}).set_index("socio_id")

df_pagos = pd.DataFrame({
    "socio_id": [1, 2, 4, 6],
    "monto": [250, 300, 180, 400]
})

resultado = pd.merge(
    df_socios,
    df_pagos,
    left_index=True,
    right_on="socio_id",
    how="left",
    indicator=True
)

print(resultado)
# Output:
#    socio_id   nombre    monto       _merge
# 0         1     Hugo    250.0        both
# 1         2    Karen    300.0        both
# 2         3   Marcos      NaN    left_only
# 3         4   Felipe    180.0        both
# 4         5 Catalina      NaN    left_only
```

### ¿Por qué sirve esto?

- Porque no necesitas volver a convertir el índice en columna.
- Porque te permite unir una estructura ya optimizada con otra más plana.
- Porque evita pasos intermedios cuando la tabla izquierda ya está lista para indexar.

Ejemplo corto: `left_index=True` le dice a pandas que use el índice del DataFrame izquierdo, mientras `right_on="socio_id"` toma la columna equivalente del derecho.

Si quieres hacer la unión en sentido contrario, puedes usar `right_index=True` y `left_on`.

```python
resultado_inverso = pd.merge(
    df_pagos,
    df_socios,
    left_on="socio_id",
    right_index=True,
    how="left",
    indicator=True
)
```

---

## 2. Revisar el resultado

`indicator=True` agrega una columna que ayuda a ver qué filas coincidieron.

```python
print(resultado["_merge"].value_counts())
```

Valores posibles de `_merge`:

- `left_only`: solo estaba en la tabla izquierda.
- `right_only`: solo estaba en la tabla derecha.
- `both`: estaba en ambas.

---

## 3. ¿Cuándo usar índice con columna?

- Usa `left_index` y `right_on` cuando la tabla izquierda ya está indexada.
- Usa `left_on` y `right_index` cuando la tabla derecha está indexada.
- Usa `indicator=True` para auditar coincidencias.
- Usa `how='outer'` si quieres revisar todas las llaves.

Como regla práctica, pregúntate esto antes de fusionar:

- ¿Cuál de las dos tablas ya tiene la llave en el índice?
- ¿La otra todavía conserva la llave como columna?
- ¿Necesito ver qué registros faltan en cada lado?

---

## Errores comunes

1. Intercambiar `left_index` y `right_on`: eso produce coincidencias incorrectas o vacías.

2. Tener tipos distintos entre índice y columna: por ejemplo, texto en un lado y enteros en el otro.

3. No usar `indicator=True` cuando quieres auditar la unión.

4. Hacer `reset_index()` sin necesidad: en este caso puedes unir directamente.

5. Olvidar que la dirección importa: `left_index=True, right_on=...` no es lo mismo que la combinación inversa.
