# 07 - Fechas y Resumen

![pandas secondary logo](https://pandas.pydata.org/static/img/pandas_secondary.svg)

> [!NOTE]
> "La práctica consistente transforma lo difícil en dominio. Cada línea de código es un paso adelante."

---

## ¿Qué haremos?

Practicaremos **trabajar con fechas y agrupar datos temporales** respondiendo preguntas académicas:

- **¿Cómo convierto strings a fechas?** → `pd.to_datetime()`
- **¿Cómo agrupo datos por mes o trimestre?** → `.dt.to_period()`
- **¿Cómo obtengo el resumen mensual de inscripciones?** → groupby + período

> [!IMPORTANT]
> Las fechas como strings no son ordenables correctamente. Siempre convierte con `to_datetime()` primero.

---

## Que vas a aprender

- Cómo pandas interpreta fechas en diferentes formatos.
- La diferencia entre `Timestamp` y `Period`.
- Cómo agrupar datos por períodos de tiempo.
- Cuándo usar `resample()` vs `to_period() + groupby()`.

---

## 1. Convertir strings a fechas

```python
import pandas as pd

# DataFrame con fechas como strings
df = pd.DataFrame({
    "estudiante": ["Hugo", "Karen", "Marcos", "Erwin", "Felipe"],
    "fecha_inscripcion": ["2024-01-01", "2024-01-02", "2024-01-05", "2024-02-01", "2024-02-02"],
    "creditos": [18, 15, 20, 16, 19]
})

# Sin conversión: strings (ordenamiento alfabético incorrecto)
print(df["fecha_inscripcion"].dtype)  # object

# Convertir a datetime
df["fecha_inscripcion"] = pd.to_datetime(df["fecha_inscripcion"])
print(df["fecha_inscripcion"].dtype)  # datetime64[ns]

print(df)
# Output:
#   estudiante fecha_inscripcion  creditos
# 0     Hugo        2024-01-01        18
# 1    Karen        2024-01-02        15
# 2   Marcos        2024-01-05        20
# 3    Erwin        2024-02-01        16
# 4   Felipe        2024-02-02        19
```

### Formatos comunes de fecha

```python
# ISO: 2024-01-15
pd.to_datetime("2024-01-15")

# US: 01/15/2024
pd.to_datetime("01/15/2024", format="%m/%d/%Y")

# Día/Mes/Año: 15-01-2024
pd.to_datetime("15-01-2024", format="%d-%m-%Y")
```

---

## 2. Agrupar por período (mes, trimestre, año)

```python
# Agrupar por mes
df["año_mes"] = df["fecha_inscripcion"].dt.to_period("M")

resultado = df.groupby("año_mes")["creditos"].sum()
print(resultado)
# Output:
# fecha
# 2024-01    53
# 2024-02    35
```

### Períodos disponibles

- `"D"`: día
- `"W"`: semana
- `"M"`: mes
- `"Q"`: trimestre
- `"Y"`: año

---

## 3. Componentes de la fecha

Extrae partes de una fecha con `.dt`.

```python
df["año"] = df["fecha_inscripcion"].dt.year
df["mes"] = df["fecha_inscripcion"].dt.month
df["día"] = df["fecha_inscripcion"].dt.day
df["nombre_mes"] = df["fecha_inscripcion"].dt.month_name()
df["nombre_día"] = df["fecha_inscripcion"].dt.day_name()

print(df[["fecha", "mes", "nombre_mes", "nombre_día"]])
# Output:
#        fecha  mes  nombre_mes nombre_día
# 0 2024-01-01    1     January     Monday
# 1 2024-01-02    2    February    Tuesday
# ...
```

---

## 4. Resample (agrupación automática por tiempo)

Más eficiente para datos de series temporales.

```python
# Establecer fecha como índice
df_ts = df.set_index("fecha_inscripcion")

# Resample por mes y suma
resultado = df_ts["creditos"].resample("M").sum()
print(resultado)
# Output: lo mismo que `.to_period() + groupby()`
```

---

## Errores comunes

- Dejar fechas como strings: ordenamiento y comparación fallan.
- Confundir `.to_period()` (para agrupación) con `.dt.date` (para extraer solo la fecha).
- No especificar `format` cuando la fecha no es ISO (YYYY-MM-DD).
- Confundir `.dt.month` (número del mes) con `.dt.month_name()` (nombre del mes).
