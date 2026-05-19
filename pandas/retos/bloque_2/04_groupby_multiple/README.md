# 04 - Groupby Múltiple

![pandas secondary logo](https://pandas.pydata.org/static/img/pandas_secondary.svg)

> [!NOTE]
> "La práctica consistente transforma lo difícil en dominio. Cada línea de código es un paso adelante."

---

## ¿Qué haremos?

Practicaremos **agrupar por múltiples columnas** para responder preguntas más detalladas:

- **¿Cuál es el promedio por ciudad y carrera?** → `groupby(['ciudad', 'carrera'])`
- **¿Cuántos estudiantes de cada carrera hay en cada ciudad?** → combinar groupby + count
- **¿Cómo cruzo análisis de dos dimensiones?** → groupby anidado

> [!IMPORTANT]
> El orden de las columnas en `groupby()` importa: la primera es el grupo principal, la segunda es el subgrupo.

---

## Que vas a aprender

- Cómo interpretar un resultado agrupado por dos columnas.
- Por qué el orden de columnas en `groupby()` cambia la estructura del resultado.
- Cuándo necesitas aplanar un resultado jerárquico.
- Cómo nombrar filas y columnas en resultados complejos.

---

## 1. Groupby de dos columnas

```python
import pandas as pd

df = pd.DataFrame({
    "nombre": ["Hugo", "Karen", "Marcos", "Erwin", "Felipe", "Catalina"],
    "carrera": ["Ingeniería de Sistemas", "Economía", "Psicología", "Arquitectura", "Medicina", "Derecho"],
    "promedio": [4.8, 4.1, 4.5, 3.9, 4.9, 4.0],
    "ciudad": ["Bogotá", "Ciudad de México", "Santiago", "Medellín", "La Paz", "Caracas"],
    "semestre": [8, 6, 5, 7, 9, 4]
})

# Promedio por ciudad y carrera
result = df.groupby(["ciudad", "carrera"])["promedio"].mean()
print(result)
# Output (estructura jerárquica):
# ciudad              carrera
# Bogotá              Ingeniería de Sistemas    4.8
# Caracas             Derecho                   4.0
# Ciudad de México    Economía                  4.1
# La Paz              Medicina                  4.9
# Medellín            Arquitectura              3.9
# Santiago            Psicología                4.5
```

### Interpretar el resultado

- Cada grupo es único: la combinación de (ciudad, puesto).
- Si hubiera múltiples empleados con la misma ciudad y puesto, `mean()` promediaría sus salarios.

---

## 2. Aplanar el resultado

Los índices jerárquicos son potentes pero incómodos. Convierte a DataFrame normal con `reset_index()`.

```python
# Aplanar resultado
result = df.groupby(["ciudad", "carrera"])["promedio"].mean().reset_index()
result.columns = ["ciudad", "carrera", "promedio_academico"]
print(result)
# Output:
#                  ciudad        carrera  promedio_academico
# 0               Bogotá       Programador            4500.0
# 1               Caracas       Ama de casa            3100.0
# ...
```

---

## 3. Contar grupos

¿Cuántos empleados de cada puesto hay en cada ciudad?

```python
# Contar estudiantes por ciudad y carrera
result = df.groupby(["ciudad", "carrera"]).size().reset_index(name="cantidad")
print(result)
# Output:
#                  ciudad        carrera  cantidad
# 0               Bogotá       Programador         1
# 1               Caracas       Ama de casa        1
# ...
```

---

## 4. Múltiples agregaciones en dos dimensiones

```python
# Promedio, máximo y cantidad de estudiantes por ciudad y carrera
result = df.groupby(["ciudad", "carrera"]).agg({
    "promedio": ["mean", "max"],
    "semestre": "mean",
    "nombre": "count"
}).reset_index()
print(result)
# Output: columnas jerárquicas con (agregación, función)
```

---

## Errores comunes

- Olvidar que el resultado es jerárquico (multi-índice).
- No usar `reset_index()` cuando necesitas un DataFrame plano para merge o visualización.
- Confundir el orden de las columnas en `groupby()`: `groupby(['A','B'])` vs `groupby(['B','A'])` pueden dar resultados visualmente diferentes.
