# 05 - Subconjunto y Metrica Derivada

![pandas secondary logo](https://pandas.pydata.org/static/img/pandas_secondary.svg)

> [!NOTE]
> "La práctica consistente transforma lo difícil en dominio. Cada línea de código es un paso adelante."

---

## ¿Qué haremos?

Responderemos estas preguntas de forma secuencial:

1. **¿Cómo extraigo solo los datos que necesito?** → Filtrar filas y seleccionar columnas
2. **¿Cómo creo una métrica nueva combinando columnas existentes?** → `df["nueva_col"] = ...`
3. **¿Cómo veo los mejores/peores primero?** → `sort_values()`

---

## Que vas a aprender

- Cuándo `.copy()` es obligatorio y por qué (SettingWithCopyWarning).
- Cómo las métricas derivadas responden preguntas que los datos originales no pueden.
- Por qué `ascending=False` es esencial para ver "mejores primero".

> [!IMPORTANT]
> Siempre usa `df.copy()` cuando crees un subconjunto que vas a modificar. Evita sorpresas.
---

## 1. Seleccionar un subconjunto

```python
import pandas as pd

df = pd.DataFrame({
    "nombre": ["Hugo", "Karen", "Marcos", "Erwin", "Felipe", "Catalina"],
    "puesto": ["Programador", "Administradora", "Backend", "Frontend", "Constructor", "Ama de casa"],
    "salario": [4500, 3200, 3800, 3500, 2800, 3100],
    "ciudad": ["Bogotá", "Ciudad de México", "Santiago", "Medellín", "La Paz", "Caracas"],
    "años_experiencia": [8, 5, 3, 6, 4, 7]
})

# Seleccionar solo las columnas que nos interesan
subset = df[["nombre", "puesto", "salario", "años_experiencia"]]

# Filtrar solo empleados con más de 5 años de experiencia
empleados_senior = subset[subset["años_experiencia"] > 5].copy()
print(empleados_senior)
# Output:
#     nombre      puesto          salario       años_experiencia
# 0  Hugo         Programador     4500                 8
# 5  Catalina     Ama de casa     3100                 7
```

> [!WARNING] Si omites `.copy()`, podrías modificar `subset` sin querer, lo que a su vez modifica `df` debido a que `subset` es una vista, no una copia independiente.

### Por qué usar `copy()`

- Evita advertencias.
- Deja claro que trabajas sobre una copia.
- Impide modificar el DataFrame original accidentalmente.


---

## 2. Crear una columna nueva

```python
# Crear una métrica: bono anual basado en experiencia
empleados_senior["bono_anual"] = empleados_senior["salario"] * (empleados_senior["años_experiencia"] * 0.05)

print(empleados_senior)
# Output:
#     nombre      puesto  salario   años_experiencia        bono_anual
# 0  Hugo          Gerente     4500        8                 1800.0
# 5  Catalina      RH          3100        7                 1085.0
```

### Para qué sirve

- Combinar columnas existentes para crear nuevas métricas.
- Crear una columna más útil que las originales.
- Responder preguntas como "¿cuál sería el bono?" sin necesidad de nueva fuente de datos.

**Documentación:** [copy](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.copy.html) y [sort_values](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html)

---

## 3. Ordenar

```python
print(empleados_senior.sort_values(by="bono_anual", ascending=False))
# Output: empleados ordenados por bono anual de mayor a menor
#     nombre      puesto  salario  años_experiencia  bono_anual
# 0     Hugo     Gerente     4500                 8       1800.0
# 5  Catalina         RH     3100                 7       1085.0
```

### Para qué sirve ordenar

- Ver los valores más altos o más bajos.
- Responder preguntas como "¿quién tiene el bono más alto?"
- Preparar datos para ranking o comparaciones.
