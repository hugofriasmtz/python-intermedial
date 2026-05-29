# 08 - Componentes de Fecha

![pandas secondary logo](https://pandas.pydata.org/static/img/pandas_secondary.svg)

> [!NOTE]
> "La práctica consistente transforma lo difícil en dominio. Cada línea de código es un paso adelante."

---

## ¿Qué haremos?

Practicaremos **extraer componentes de fechas** para análisis temporal detallado en estudiantes:

- **¿Cómo obtengo el año, mes, o día por separado?** → `.dt.year`, `.dt.month`, `.dt.day`
- **¿Cómo sé en qué día de la semana cae una fecha?** → `.dt.day_name()`
- **¿Cómo calculo diferencias entre fechas?** → operaciones aritméticas
- **¿Cómo filtro por trimestre o año?** → combina `.dt` con filtros

> [!IMPORTANT]
> `.dt` es un accessor que **solo funciona con dtype datetime64**. Convierte con `pd.to_datetime()` primero.

---

## ¿Qué vas a aprender?

- Todos los extractores disponibles en `.dt`.
- Cómo filtrar y agrupar usando componentes de fechas.
- Cómo calcular diferencias entre fechas (duración).
- Cuándo usar `.dt` vs `.astype(str)`.

**Documentación:** [Series.dt](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.dt.html), [to_datetime](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html) y [day_name](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.dt.day_name.html)

---

## 1. Extractores básicos

```python
import pandas as pd

df = pd.DataFrame({
    "estudiante": ["Hugo", "Karen", "Marcos"],
    "fecha_matricula": pd.to_datetime(["2024-01-15", "2024-06-20", "2024-12-31"])
})

# Componentes individuales
df["año"] = df["fecha_matricula"].dt.year
df["mes"] = df["fecha_matricula"].dt.month
df["día"] = df["fecha_matricula"].dt.day
df["día_año"] = df["fecha_matricula"].dt.dayofyear  # día 1-365 del año
df["semana"] = df["fecha_matricula"].dt.isocalendar().week  # número de semana

print(df[["fecha_matricula", "año", "mes", "día", "semana"]])
# Output:
#   fecha_matricula  año  mes  día  semana
# 0      2024-01-15 2024    1   15       3
# 1      2024-06-20 2024    6   20      25
# 2      2024-12-31 2024   12   31       1
```

---

## 2. Nombres de día y mes

```python
df["nombre_mes"] = df["fecha_matricula"].dt.month_name()
df["nombre_día"] = df["fecha_matricula"].dt.day_name()
df["trimestre"] = df["fecha_matricula"].dt.quarter  # Q1, Q2, Q3, Q4

print(df[["fecha_matricula", "nombre_mes", "nombre_día", "trimestre"]])
# Output:
#        fecha nombre_mes nombre_día  trimestre
# 0 2024-01-15    January     Monday          1
# 1 2024-06-20      June     Thursday          2
# 2 2024-12-31   December     Tuesday          4
```

### Extractores comunes

- `.dt.year`: año (2024, etc.).
- `.dt.month`: mes (1-12).
- `.dt.day`: día del mes (1-31).
- `.dt.dayofweek`: día de la semana (0=lunes, 6=domingo).
- `.dt.day_name()`: nombre del día.
- `.dt.month_name()`: nombre del mes.
- `.dt.quarter`: trimestre (1-4).

---

## 3. Filtrar por componentes

```python
# Estudiantes matriculados en enero
df_enero = df[df["fecha_matricula"].dt.month == 1]

# Estudiantes matriculados en lunes
df_lunes = df[df["fecha_matricula"].dt.day_name() == "Monday"]

# Estudiantes matriculados en Q1 (primeros 3 meses)
df_q1 = df[df["fecha_matricula"].dt.quarter == 1]

print(df_enero)
# Output: solo el evento del 15 de enero
```

---

## 4. Diferencias entre fechas

```python
# DataFrame con dos fechas
df_temporal = pd.DataFrame({
    "estudiante": ["Hugo", "Hugo"],
    "fecha": pd.to_datetime(["2024-01-01", "2024-01-15"])
})

# Diferencia en días
df_temporal["diferencia_días"] = (df_temporal["fecha"].max() - df_temporal["fecha"].min()).days
print(df_temporal)

# Diferencia dentro del DataFrame (entre filas)
df_temporal["tiempo_desde_inicio"] = df_temporal["fecha"] - df_temporal["fecha"].iloc[0]
print(df_temporal)
# Output:
#                fecha tiempo_desde_inicio
# 0 2024-01-01 0 days
# 1 2024-01-15 14 days
```

---

## 5. Agrupar por componente

```python
# Contar matrículas por mes
resultado = df.groupby(df["fecha_matricula"].dt.month)["estudiante"].count()
print(resultado)
# Output:
# fecha
# 1    1
# 6    1
# 12   1
```

---

## Errores comunes

- Usar `.dt` en columnas string (no datetime): convierte primero con `to_datetime()`.
- Confundir `.dayofweek` (0-6) con `.day_name()` (string de nombre).
- Olvidar que `.month_name()` devuelve strings (no funciona bien para cálculos numéricos).
- No documentar unidades: `.days` en diferencias de fecha, no siempre implícito.
