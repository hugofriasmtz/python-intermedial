# 05 - Merge Básico

![pandas secondary logo](https://pandas.pydata.org/static/img/pandas_secondary.svg)

> [!NOTE]
> "La práctica consistente transforma lo difícil en dominio. Cada línea de código es un paso adelante."

---

## ¿Qué haremos?

Practicaremos **combinar dos DataFrames** respondiendo preguntas que requieren datos de múltiples tablas:

- **¿Cómo agrego información de otra tabla basándome en un ID?** → `pd.merge()` con `on='columna'`
- **¿Qué diferencia hay entre inner, left, right y outer?** → tipos de join
- **¿Cómo aseguro que no pierdo datos en la combinación?** → elegir el tipo correcto

> [!IMPORTANT]
> `merge()` por defecto es un INNER JOIN: solo mantiene filas que existen en ambas tablas.

---

## ¿Qué vas a aprender?

- Los cuatro tipos de join: inner, left, right, outer.
- Cómo elegir el tipo de join según tu pregunta.
- Por qué `.left_on` y `.right_on` existen (cuando las columnas tienen nombres diferentes).
- Cómo detectar y manejar duplicados tras un merge.

**Documentación:** [merge](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge.html)

---

## 1. Inner join (merge por defecto)

Combina dos tablas y mantiene solo las filas que existen en **ambas**.

```python
import pandas as pd

# DataFrame de estudiantes
df_estudiantes = pd.DataFrame({
    "id": [1, 2, 3, 4, 5, 6],
    "nombre": ["Hugo", "Karen", "Marcos", "Erwin", "Felipe", "Catalina"],
    "carrera": ["Ingeniería de Sistemas", "Economía", "Psicología", "Arquitectura", "Medicina", "Derecho"],
    "promedio": [4.8, 4.1, 4.5, 3.9, 4.9, 4.0],
})

# DataFrame de becas (solo algunos estudiantes tienen beca)
df_becas = pd.DataFrame({
    "id": [1, 2, 4],
    "beca": [500, 300, 400]
})

# Merge inner (solo estudiantes con beca)
result = pd.merge(df_estudiantes, df_becas, on="id", how="inner")
print(result)
# Output:
#    id   nombre                carrera  promedio  beca
# 0   1   Hugo  Ingeniería de Sistemas       4.8   500
# 1   2  Karen                Economía       4.1   300
# 2   4  Erwin           Arquitectura       3.9   400
```

### ¿Cuándo usarlo?

- Quieres solo datos completos de ambas tablas.
- Quieres eliminar estudiantes sin información coincidente.

---

## 2. Left join

Mantiene **todas las filas de la tabla izquierda** y añade datos de la derecha si existen.

```python
# Merge left (todos los estudiantes, con beca si la tienen)
result = pd.merge(df_estudiantes, df_becas, on="id", how="left")
print(result)
# Output:
#    id   nombre                carrera  promedio   beca
# 0   1   Hugo  Ingeniería de Sistemas       4.8  500.0
# 1   2  Karen                Economía       4.1  300.0
# 2   3 Marcos              Psicología       4.5    NaN
# 3   4  Erwin           Arquitectura       3.9  400.0
# 4   5  Felipe                Medicina       4.9    NaN
# 5   6  Catalina                Derecho       4.0    NaN
```

### ¿Cuándo usar left join?

- Quieres mantener todas las filas de la tabla principal.
- Está bien si algunos valores en las nuevas columnas son `NaN`.

---

## 3. Right join y outer join

```python
# Right join: todas las filas de la tabla derecha
result = pd.merge(df_estudiantes, df_becas, on="id", how="right")

# Outer join: todas las filas de ambas tablas
result = pd.merge(df_estudiantes, df_becas, on="id", how="outer")
```

---

## 4. Merge con columnas de nombres diferentes

Si las columnas a unir tienen nombres distintos en cada tabla.

```python
# Tabla de tutorías con "estudiante_id" en lugar de "id"
df_proyectos = pd.DataFrame({
    "estudiante_id": [1, 2, 4],
    "tutoria": ["Python", "Álgebra", "Web"]
})

# Merge usando left_on y right_on
result = pd.merge(df_estudiantes, df_proyectos, left_on="id", right_on="estudiante_id", how="left")
print(result)
```

---

## Errores comunes

- Confundir inner, left, right: inner es restrictivo; left/right mantienen una tabla completa.
- No revisar duplicados tras merge: si hay múltiples filas con el mismo ID, el resultado puede multiplicarse.
- Olvidar que `NaN` aparece en left/right/outer cuando no hay coincidencia.
