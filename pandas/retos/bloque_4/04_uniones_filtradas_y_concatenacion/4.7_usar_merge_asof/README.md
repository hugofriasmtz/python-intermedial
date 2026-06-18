# 4.7 - Using merge_asof()

![pandas secondary logo](https://pandas.pydata.org/static/img/pandas_secondary.svg)

> [!NOTE]
> "La practica consistente transforma lo dificil en dominio. Cada linea de codigo es un paso adelante."

`merge_asof()` une por la coincidencia mas cercana en una llave ordenada. Es util cuando no hay igualdad exacta entre marcas de tiempo, pero si quieres el valor mas proximo.

---

## ¿Que haremos?

Tomaremos dos tablas temporales y las uniremos por la llave mas cercana, primero de forma basica y luego cambiando la direccion de busqueda.

> [!TIP]
> Es muy util cuando dos fuentes registran eventos en momentos ligeramente distintos.

- **¿Que tipo de match hace?** -> cercano, no exacto
- **¿Que requisito clave tiene?** -> la columna `on` debe estar ordenada
- **¿Como cambia la busqueda?** -> `direction='backward'|'forward'|'nearest'`

> [!IMPORTANT]
> Si la columna temporal no esta ordenada, `merge_asof()` puede fallar o devolver resultados incorrectos.

---

## ¿Que vas a aprender?

- Como funciona el emparejamiento mas cercano.
- Diferencia entre `backward`, `forward` y `nearest`.
- Como aplicarlo en datos de mercado o de sensores.

**Documentacion:** [pandas.merge_asof](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge_asof.html)

---

## 1. Ejemplo base con series temporales

La idea es unir una serie de operaciones con el precio mas cercano de referencia.

```python
import pandas as pd

visa = pd.DataFrame({
    "date_time": [
        "2017-11-17 16:00:00", "2017-11-17 17:00:00", "2017-11-17 18:00:00",
        "2017-11-17 19:00:00", "2017-11-17 20:00:00", "2017-11-17 21:00:00",
        "2017-11-17 22:00:00",
    ],
    "close": [110.32, 110.24, 110.065, 110.04, 110.0, 109.9966, 109.82],
})

ibm = pd.DataFrame({
    "date_time": [
        "2017-11-17 15:35:12", "2017-11-17 15:40:34", "2017-11-17 15:45:50",
        "2017-11-17 15:50:20", "2017-11-17 15:55:10", "2017-11-17 16:00:03",
        "2017-11-17 16:05:06", "2017-11-17 16:10:12", "2017-11-17 16:15:30",
        "2017-11-17 16:20:32", "2017-11-17 16:25:47",
    ],
    "close": [149.3, 149.13, 148.98, 148.99, 149.11, 149.25, 149.5175, 149.57, 149.59, 149.82, 149.96],
})

visa["date_time"] = pd.to_datetime(visa["date_time"])
ibm["date_time"] = pd.to_datetime(ibm["date_time"])

visa = visa.sort_values("date_time")
ibm = ibm.sort_values("date_time")

res = pd.merge_asof(visa, ibm, on="date_time", suffixes=("_visa", "_ibm"))
print(res)
# Output:
#             date_time  close_visa  close_ibm
# 0 2017-11-17 16:00:00    110.3200    149.25
# 1 2017-11-17 17:00:00    110.2400    149.96
# ...
```

### ¿Por que sirve esto?

- Porque busca el valor mas cercano en lugar de exigir una coincidencia exacta.
- Porque funciona muy bien con tablas temporales que no estan sincronizadas al segundo.
- Porque reduce la necesidad de preprocesar tiempos manualmente.

---

## 2. Cambiar la direccion del emparejamiento

Si quieres controlar si busca hacia atras o hacia adelante, usa `direction`.

```python
res_forward = pd.merge_asof(
    visa,
    ibm,
    on="date_time",
    suffixes=("_visa", "_ibm"),
    direction="forward",
)
print(res_forward)
# Output:
#             date_time  close_visa  close_ibm
# 0 2017-11-17 16:00:00    110.3200    149.25
# 1 2017-11-17 17:00:00    110.2400    149.57
# ...
```

Este ajuste cambia la regla de proximidad y te deja decidir que lado temporal tiene prioridad.

---

## 3. ¿Cuando usar `merge_asof()`?

- Datos muestreados de un proceso continuo.
- Construccion de datasets sin fuga de informacion.
- Uniones donde la llave exacta rara vez coincide.

Como regla practica, preguntate esto antes de unir:

- ¿La llave temporal esta ordenada?
- ¿Necesito la coincidencia mas cercana y no la exacta?
- ¿Tiene sentido mirar hacia atras o hacia adelante?

---

## Errores comunes

1. No ordenar por la columna `on`.
2. Usar texto en lugar de `datetime` en series temporales.
3. Elegir `direction` incorrecta para el objetivo analitico.
4. Confundir `merge_asof()` con `merge()` exacto.
