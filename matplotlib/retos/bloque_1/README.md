# Bloque 1 - Fundamentos de Visualización

![matplotlib logo](https://upload.wikimedia.org/wikipedia/commons/8/84/Matplotlib_icon.svg)

> Aprende a crear gráficos simples que comuniquen información clara y efectiva.

---

## Objetivo del bloque

Al completar este bloque, serás capaz de:

1. **Crear gráficos de líneas** - Para visualizar tendencias y cambios en el tiempo
2. **Crear gráficos de barras** - Para comparar valores entre categorías
3. **Combinar múltiples series** - Mostrar dos o más datasets en una misma gráfica
4. **Personalizar títulos y etiquetas** - Hacer que tus gráficos sean autodescriptivos
5. **Entender escalas y distribución** - Elegir las proporciones correctas para cada dato
6. **Aplicar propiedades visuales** - Usar colores, transparencia y marcadores

---

## Métodos clave que aprenderás

- **`plt.plot()`** - Crea líneas para mostrar tendencias y relaciones continuas
  - *Para qué:* Cuando necesitas ver cómo cambia una métrica a lo largo del tiempo
  
- **`plt.bar()`** - Crea barras para comparar valores entre categorías
  - *Para qué:* Cuando quieres comparar "manzanas con manzanas" - valores discretos sin orden temporal

- **`plt.title()`, `plt.xlabel()`, `plt.ylabel()`** - Etiquetan tu gráfica
  - *Para qué:* Quien vea tu gráfica debe entender qué representa sin pedirte explicaciones

- **`alpha=` (transparencia)** - Ajusta cuánto se "ven a través" los elementos
  - *Para qué:* Cuando superpones gráficas, la transparencia permite ver líneas que se cruzan

- **`plt.legend()`** - Muestra las etiquetas de cada serie de datos
  - *Para qué:* Diferenciar entre múltiples líneas o barras en una misma gráfica

- **`plt.show()`** - Muestra la gráfica en pantalla
  - *Para qué:* Visualizar el resultado de tu trabajo

---

## Ruta de aprendizaje recomendada

Completa los retos **en este orden** para construir progresivamente tus habilidades:

1. **Reto 1 (Líneas simples)** - Entiende cómo plt.plot() dibuja una tendencia
2. **Reto 2 (Barras simples)** - Aprende la diferencia entre líneas y barras
3. **Reto 3 (Comparación)** - Practica superponer dos series con transparencia
4. **Reto 4 (Personalización)** - Domina colores, estilos y marcadores
5. **Reto 5 (Múltiples series)** - Maneja 4+ líneas en una gráfica
6. **Reto 6 (Histogramas)** - Visualiza distribuciones de datos
7. **Reto 7 (Scatter)** - Encuentra relaciones entre variables

---

## Detalle de cada reto

---

### Reto 1: `01_lineas.py` [Nivel 1] - Tu primer gráfico de líneas

**Qué harás**: Crear una gráfica de líneas que muestre cómo cambian las ventas mes a mes.

**Concepto clave**: Las LÍNEAS conectan puntos para mostrar TENDENCIAS a lo largo del tiempo.

**Datos**: Ventas mensuales (`["Ene", "Feb", "Mar", "Abr", "May", "Jun"]` y `[120, 150, 130, 170, 200, 190]`)

**Instrucciones paso a paso**:

1. Llama `plt.plot(meses, ventas)` - conecta los puntos con una línea
2. Agrega `plt.title("Ventas Mensuales")` - todo gráfico necesita un título descriptivo
3. Etiqueta ejes con `plt.xlabel("Meses")` y `plt.ylabel("Ventas")`
4. Usa `plt.xticks(meses)` para asegurar que se muestren todos los meses
5. Cierra con `plt.show()`

**Desafío extra**: Cambia `color="teal"` en `plt.plot()` y observa cómo cambia la línea.

**Reflexión**: ¿En qué mes se observa el pico de ventas? ¿Por qué una línea es mejor que puntos aislados?

---

### Reto 2: `02_barras.py` [Nivel 1] - Comparar categorías

**Qué harás**: Crear un gráfico de BARRAS para comparar pedidos entre productos.

**Concepto clave**: Las BARRAS se usan para comparar CATEGORÍAS distintas, no para mostrar tendencias en tiempo.

| Tipo | Cuándo usar | Ejemplo |
|------|-------------|---------|

| **Líneas** | Ver cambio en el tiempo | Ventas enero → junio |

| **Barras** | Comparar categorías | ¿Qué producto vende más? |

**Datos**: Categorías (`["Cafe", "Te", "Postres", "Sandwiches"]`) y pedidos (`[80, 45, 60, 35]`)

**Instrucciones paso a paso**:

1. Usa `plt.bar(categorias, pedidos)` para crear las barras
2. Agrega título con `plt.title("Pedidos por Categoria")`
3. Etiqueta con `plt.xlabel()` y `plt.ylabel()`
4. Usa `plt.show()`

**Desafío extra**: Prueba `color="tab:green"` para cambiar el color de todas las barras.

**Reflexión**: ¿Cuál categoría lidera? ¿Sería mejor mostrar esto con una línea? ¿Por qué no?

---

### Reto 3: `03_comparacion_meses.py` [Nivel 2] - Superponer series

**Qué harás**: Mostrar DOS series de barras en la MISMA gráfica usando TRANSPARENCIA para verlas claras.

**Concepto clave**: El parámetro `alpha` controla la transparencia (0=invisible, 1=opaco). Permite ver series que se sobrelapan.

**Datos**: Dos meses de ventas por categoría

**Instrucciones paso a paso**:

1. Primera serie: `plt.bar(categorias, mes1, label="Mes 1", alpha=0.7)`
   - `label=` te permite distinguir las series
   - `alpha=0.7` hace que sea 70% opaco (30% transparente)
2. Segunda serie: `plt.bar(categorias, mes2, label="Mes 2", alpha=0.7)`
3. Agrega `plt.legend()` para mostrar cuál es cuál
4. Títulos y etiquetas

**Desafío extra**: Experimenta con diferentes valores de `alpha` (0.5, 0.3, 0.9). ¿Cuál es mejor?

**Reflexión**: ¿Qué categorías crecieron? ¿Cuáles bajaron? ¿Por qué la transparencia es importante aquí?

---

### Reto 4: `04_personalizacion.py` [Nivel 2] - Personalización visual

**Qué harás**: Crear 3 líneas, cada una con COLOR, ESTILO y MARCADOR distintos.

**Concepto clave**: Combinar colores, estilos y marcadores hace gráficas:

- Más profesionales
- Comprensibles para personas con daltonismo
- Claras incluso en blanco y negro

**Datos**: Ventas de 3 meses diferentes

**Instrucciones paso a paso**:

Para cada `plt.plot()`:

```python
plt.plot(meses, ventas,
         color="tab:blue",    # Color: tab:blue, tab:red, tab:green, #FF5733, etc.
         linestyle="-",       # Estilo: "-" (sólido), "--" (guiones), "-." (punto-guión), ":" (puntos)
         marker="o",          # Marcador: "o" (círculo), "s" (cuadrado), "^" (triángulo), "D" (diamante)
         linewidth=2,         # Grosor de línea
         markersize=8,        # Tamaño del marcador
         label="Mes 1")       # Para la leyenda
```

**Desafío extra**: Crea 4 líneas. ¿Cuántas combinaciones de color+estilo+marcador necesitas para que sean diferenciables?

**Reflexión**: ¿Por qué usar los tres parámetros juntos es mejor que solo cambiar color?

---

### Reto 5: `05_multiples_series.py` [Nivel 2] - Múltiples series (4+)

**Qué harás**: Graficar 4 categorías de productos en la MISMA figura sin que se vea caótica.

**Concepto clave**: Cuando tienes muchas series, necesitas una ESTRATEGIA:

- Colores distintos
- Estilos de línea variados
- Leyenda clara

**Datos**: 4 productos (Café, Té, Postres, Sandwiches) durante 6 meses

**Instrucciones paso a paso**:

1. Define datos para cada producto
2. Llama `plt.plot()` cuatro veces, una por producto
3. Usa colores: `"tab:blue"`, `"tab:red"`, `"tab:green"`, `"tab:orange"`
4. Agrega `plt.legend(loc="best")` - matplotlib elige el mejor lugar
5. `plt.grid(alpha=0.3)` para hacer la grilla más visible

**Desafío extra**: Agrega `plt.figure(figsize=(12, 6))` al inicio para hacer la figura más ancha. ¿Mejora?

**Reflexión**: ¿A partir de cuántas líneas se vuelve confusa una gráfica? ¿Cuándo deberías usar subplots en lugar de superposición?

---

### Reto 6: `06_histogramas.py` [Nivel 2] - Histogramas (distribuciones)

**Qué harás**: Visualizar una DISTRIBUCIÓN - cómo se distribuyen 100 tiempos de permanencia de clientes.

**Concepto clave**: HISTOGRAMAS ≠ BARRAS

- **Histogramas**: Ven distribución de datos continuos (tiempo, edad, peso)
- **Barras**: Comparan categorías distintas

**Datos**: 100 tiempos de permanencia (generados aleatoriamente entre 10 y 120 minutos)

**Instrucciones paso a paso**:

1. `plt.hist(datos, bins=20)` - crea histograma con 20 intervalos
   - `bins=20`: divide los datos en 20 contenedores
   - Más bins = más detalle (pero puede verse ruidoso)
2. `edgecolor="black"` - agrega borde a los contenedores
3. `alpha=0.7` - transparencia
4. Títulos y etiquetas

**Desafío extra**: Experimenta con `bins=10`, `bins=30`, `bins=50`. ¿Cuál muestra mejor la distribución?

**Reflexión**: ¿Dónde se concentran más clientes? ¿Hay una distribución normal (campana)? ¿Qué significa eso?

---

### Reto 7: `07_scatter.py` [Nivel 2] - Scatter (dispersión)

**Qué harás**: Buscar RELACIÓN entre EDAD (variable X) y GASTO (variable Y).

**Concepto clave**: Scatter plots muestran si dos variables están correlacionadas:

- Puntos suben (derecha): correlación positiva (edad ↑ → gasto ↑)
- Puntos bajan (derecha): correlación negativa
- Puntos dispersos: sin relación

**Datos**: 50 clientes con edad, gasto total y frecuencia de visitas

**Instrucciones paso a paso**:

1. `plt.scatter(edad, gasto)` - crea los puntos
2. Colorea por tercera variable: `c=frecuencia` + `cmap="viridis"`
   - `c=`: valores para colorear puntos
   - `cmap="viridis"`: paleta de colores (también: "cool", "hot", "winter")
3. `plt.colorbar()` - muestra la escala de colores
4. `s=100` - tamaño de los puntos

**Desafío extra**: Prueba `s=edad` para que tamaño = edad. ¿Se ve mejor? ¿Por qué?

**Reflexión**: ¿Hay correlación entre edad y gasto? ¿Hay outliers (puntos fuera del patrón)?

---

## Estrategia de estudio

### Antes de ejecutar cada reto

1. **Lee el código y los comentarios TODO** - ¿Qué hace cada línea?
2. **Pregúntate**: ¿Para qué necesito cada parámetro?
3. **Predice**: ¿Cómo se verá el gráfico?

### Después de ejecutar

1. **Verifica**: ¿Salió como esperabas?
2. **Experimenta**: Cambia colores, valores, títulos - ¿Cómo cambia?
3. **Compara**: ¿Cuándo usarías líneas vs. barras?

---

## Errores comunes en este bloque

- **Gráfica vacía o sin color**: Olvidaste `plt.show()`
- **Leyenda no aparece**: Necesitas `label=` en plot/bar Y luego `plt.legend()`
- **Texto superpuesto o cortado**: Usa `plt.tight_layout()` al final
- **Datos no visibles**: Aumenta `figsize` en `plt.figure()`

---

## Checklist de finalización

- [ ] Completé el Reto 1 y entiendo cómo `plt.plot()` crea líneas
- [ ] Completé el Reto 2 y distingo cuándo usar barras vs. líneas
- [ ] Completé el Reto 3 y sé usar `alpha` y `legend`
- [ ] Completé el Reto 4 y domino colores, estilos y marcadores
- [ ] Completé el Reto 5 y puedo graficar 4+ series sin confusión
- [ ] Completé el Reto 6 y entiendo histogramas vs. barras
- [ ] Completé el Reto 7 y sé buscar relaciones con scatter plots
- [ ] Puedo crear gráficas simples o complejas sin ver soluciones
- [ ] Entiendo para qué sirve cada parámetro en mis gráficas
- [ ] He experimentado para descubrir qué funciona mejor
