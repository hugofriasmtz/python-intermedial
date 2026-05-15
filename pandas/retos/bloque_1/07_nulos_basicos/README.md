# 07 - Nulos Basicos

![pandas secondary logo](https://pandas.pydata.org/static/img/pandas_secondary.svg)

> [!NOTE]
> "La práctica consistente transforma lo difícil en dominio. Cada línea de código es un paso adelante."

---

## ¿Qué haremos?

Responderemos estas preguntas sobre datos faltantes:

1. **¿Qué columnas tienen nulos?** → `isna().sum()`
2. **¿Cuántos nulos hay (cantidad y porcentaje)?** → `isna().sum()` e `isna().mean() * 100`
3. **¿Es un problema grave?** → Decide si tolerar, eliminar filas o rellenar

> [!CAUTION]
> Los nulos pueden causar errores silenciosos en cálculos. Revisa siempre antes de usar datos numéricos.

---

## Que vas a aprender

- Por qué ignorar nulos causa errores silenciosos (cálculos incorrectos).
- Cuándo es mejor eliminar filas vs rellenar (imputar) valores.
- Cómo 16% de nulos es preocupante pero 2% puede ser tolerable según el contexto.

---

## 1. Contar nulos

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "nombre": ["Hugo", "Karen", np.nan, "Erwin", "Felipe", "Catalina"],
    "puesto": ["Programador", "Administradora", "Backend", np.nan, "Constructor", "Ama de casa"],
    "salario": [4500, 3200, 3800, 3500, np.nan, 3100],
    "ciudad": ["Bogotá", "Ciudad de México", "Santiago", "Medellín", "La Paz", "Caracas"],
    "años_experiencia": [8, 5, 3, 6, 4, 7]
})

# Contar nulos por columna
print(df.isna().sum())
# Output:
# nombre                  1
# puesto                  1
# salario                 1
# ciudad                  0
# años_experiencia        0
```

### Para qué sirve contar nulos

- Saber qué columnas necesitan limpieza.
- Detectar problemas en la calidad de datos rápidamente.

> [!TIP]
> Para imputación rápida en columnas numéricas, prueba `df['col'] = df['col'].fillna(df['col'].median())`.

---

## 2. Porcentaje de nulos

```python
# Calcular porcentaje de nulos por columna
print((df.isna().mean() * 100).round(2))
# Output:
# nombre                16.67
# puesto                16.67
# salario               16.67
# ciudad                 0.00
# años_experiencia       0.00
```

### Para qué sirve el porcentaje de nulos

- Entender qué tan grave es la falta de datos.
- Decidir si es mejor eliminar una columna o llenarla.
- Comparar la calidad entre columnas.

**Documentación:** [Missing data](https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html)

---

## 3. Mini practica

Identifica las columnas con nulos y piensa si conviene llenar, eliminar o dejar esos datos.
