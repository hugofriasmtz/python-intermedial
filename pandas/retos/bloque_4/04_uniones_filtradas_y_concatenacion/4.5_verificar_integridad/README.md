# 4.5 - Verifying integrity

![pandas secondary logo](https://pandas.pydata.org/static/img/pandas_secondary.svg)

> [!NOTE]
> "La practica consistente transforma lo dificil en dominio. Cada linea de codigo es un paso adelante."

En integracion de datos, los errores silenciosos son comunes. Por eso conviene validar relaciones en `merge()` y revisar indices duplicados en `concat()`.

---

## ¿Que haremos?

Vamos a revisar dos validaciones utiles:

> [!TIP]
> Validar integridad te ayuda a detectar problemas temprano, antes de entrenar modelos o publicar reportes.

- `merge(validate=...)` para comprobar la cardinalidad esperada.
- `concat(verify_integrity=True)` para detectar indices duplicados.

- **¿Que valida `merge(validate=...)`?** -> tipo de relacion entre llaves
- **¿Que valida `verify_integrity`?** -> que el nuevo indice no tenga duplicados

> [!IMPORTANT]
> Los datos reales suelen traer duplicados o llaves inconsistentes, aunque parezcan limpios.

---

## ¿Que vas a aprender?

- Usar `validate='one_to_one'`, `one_to_many`, `many_to_one` y `many_to_many`.
- Interpretar errores de validacion en merges.
- Detectar duplicados de indice al concatenar.

**Documentacion:** [pandas.merge](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge.html) - [pandas.concat](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html)

---

## 1. Validar merges con `validate`

La validacion es util cuando quieres confirmar que la relacion entre llaves es la esperada.

```python
import pandas as pd

tracks = pd.DataFrame({
    "tid": [2, 3, 4],
    "name": ["Balls to the...", "Fast As a Shark", "Restless and..."],
    "aid": [2, 3, 3],
})

specs = pd.DataFrame({
    "tid": [2, 3, 2],
    "milliseconds": [342562, 230619, 252051],
})

tracks.merge(specs, on="tid", validate="one_to_one")
# Output:
# MergeError: Merge keys are not unique in right dataset; not a one-to-one merge
```

### Tipos comunes de validacion

- `one_to_one`
- `one_to_many`
- `many_to_one`
- `many_to_many`

Este chequeo te dice rapido si la cardinalidad coincide con tu expectativa.

---

## 2. Verificar una relacion correcta

Si la relacion esperada es `one_to_many`, la validacion debe pasar sin error.

```python
albums = pd.DataFrame({"aid": [2, 3], "title": ["X", "Y"]})
tracks = pd.DataFrame({"aid": [2, 3, 3], "tid": [2, 3, 4]})

ok = albums.merge(tracks, on="aid", validate="one_to_many")
print(ok)
# Output:
#    aid title  tid
# 0    2     X    2
# 1    3     Y    3
# 2    3     Y    4
```

---

## 3. Verificar integridad en concatenacion

`concat()` puede dejar indices repetidos si combinas tablas con el mismo indice original.

```python
inv_feb = pd.DataFrame({"cid": [38, 40, 42]}, index=[7, 8, 9])
inv_mar = pd.DataFrame({"cid": [17, 19, 21]}, index=[9, 15, 16])

pd.concat([inv_feb, inv_mar], verify_integrity=True)
# Output:
# ValueError: Indexes have overlapping values: Int64Index([9], dtype='int64')
```

Si no validas, `concat()` acepta indices duplicados y el problema puede pasar desapercibido.

---

## 4. ¿Por que verificar integridad?

- Porque datos reales pueden venir sucios.
- Porque evita relaciones no intencionales (`1:m` o `m:m`).
- Porque previene duplicados silenciosos al concatenar.

Como regla practica, preguntate esto antes de unir:

- ¿La llave deberia ser unica?
- ¿El tipo de relacion es el que espero?
- ¿Estoy apilando tablas con indices que se repiten?

---

## Errores comunes

1. Asumir `one_to_one` sin revisar duplicados.
2. Ignorar excepciones de `validate` o `verify_integrity`.
3. Forzar `many_to_many` sin analizar el impacto.
4. No limpiar llaves antes de unir.
