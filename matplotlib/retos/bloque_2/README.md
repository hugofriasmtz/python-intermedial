# Bloque 2 - Visualización Intermedia

![matplotlib logo](https://upload.wikimedia.org/wikipedia/commons/8/84/Matplotlib_icon.svg)

> Comunica historias complejas dividiendo gráficas, anotando puntos clave y eligiendo escalas inteligentes.

---

## Objetivo del bloque

Al completar este bloque, dominarás:

1. **Subplots** - Dividir una figura en múltiples gráficas para comparación
2. **Anotaciones** - Resaltar puntos específicos con etiquetas y flechas
3. **Escalas logarítmicas** - Visualizar datos que crecen exponencialmente
4. **Gráficos avanzados** - Barras agrupadas y otros formatos complejos
5. **Diseño visual** - Grillas, figuras escaladas y layouts ajustados
6. **Narrativa visual** - Hacer que cada elemento de tu gráfica cuente una parte de la historia

---

## Métodos clave que aprenderás

- **`plt.subplots()`** - Crea múltiples gráficas en una figura
  - *Para qué:* Comparar dos datasets lado a lado sin confundir la vista
  
- **`plt.annotate()`** - Agrega etiquetas con flechas a puntos específicos
  - *Para qué:* Destacar un hallazgo importante: "aquí es donde pasó algo"

- **`plt.yscale("log")` / `plt.xscale("log")`** - Cambiar a escala logarítmica
  - *Para qué:* Cuando los datos varían muchísimo (de 10 a 1 millón), lineal no muestra el patrón

- **`fig, axes = plt.subplots()`** - Acceder a subplots individuales
  - *Para qué:* Personalizar cada gráfica por separado (títulos, grillas, colores)

- **`fig.suptitle()` vs `axes.set_title()`** - Títulos generales vs. específicos
  - *Para qué:* Título general: "¿Qué pregunta responden estos 4 gráficos?" | Títulos específicos: "¿Qué ve aquí?"

- **`fig.tight_layout()`** - Ajusta espaciado automáticamente
  - *Para qué:* Evitar que títulos o etiquetas se superpongan

---

## Ruta de aprendizaje recomendada

Completa los retos **en este orden**:

1. **Reto 1 (Subplots)** - Aprende a dividir figuras para comparación clara
2. **Reto 2 (Anotaciones)** - Destaca puntos clave con flechas y textos
3. **Reto 3 (Escala logarítmica)** - Maneja datos que varían exponencialmente
4. **Reto 4 (Barras agrupadas)** - Crea comparaciones complejas profesionalmente
5. **Reto 5 (Gráfico de área)** - Visualiza composición de un total en el tiempo
6. **Reto 6 (Combinado línea+barras)** - Usa dos ejes Y para métricas distintas
7. **Reto 7 (Personalizado avanzado)** - Domina diseño profesional

---

## Detalle de cada reto

---

### Reto 1: `01_subplots.py` [Nivel 2-3] - Dividir figura en subplots

**Qué harás**: Crear DOS gráficas independientes en una misma figura (una arriba, otra abajo).

**Concepto clave**: Usa `plt.subplots()` para obtener `fig` (figura completa) y `axes` (lista de gráficas).

- **fig**: Toda la ventana
- **axes**: Cada gráfica individual que puedes personalizar por separado

**Datos**: Ventas y gastos mensuales

**Instrucciones paso a paso**:

```python
fig, axes = plt.subplots(2, 1, figsize=(10, 8))  # 2 filas, 1 columna

# Gráfica 1 (arriba)
axes[0].plot(meses, ventas, color="tab:green", marker="o")
axes[0].set_title("Ventas Mensuales")
axes[0].set_xlabel("Mes")
axes[0].set_ylabel("Ventas ($)")

# Gráfica 2 (abajo)
axes[1].plot(meses, gastos, color="tab:red", marker="s")
axes[1].set_title("Gastos Mensuales")
axes[1].set_xlabel("Mes")
axes[1].set_ylabel("Gastos ($)")

# Título general
fig.suptitle("Comparación: Ventas vs. Gastos", fontsize=14, fontweight="bold")

# Ajustar espacios
fig.tight_layout()
```

**Desafío extra**: Cambia a `plt.subplots(1, 2)` para que las gráficas estén LADO A LADO.

**Reflexión**: ¿Cuándo es mejor lado a lado vs. arriba abajo? ¿Depende del tipo de comparación?

---

### Reto 2: `02_anotaciones.py` [Nivel 2-3] - Resaltar puntos clave

**Qué harás**: Marcar el MÁXIMO de una serie con una anotación y una flecha roja.

**Concepto clave**: `plt.annotate()` te permite poner un "post-it" con flecha en cualquier punto.

**Datos**: Una línea de tendencia con picos

**Instrucciones paso a paso**:

```python
# Grafica línea
plt.plot(meses, datos, color="tab:blue", marker="o")

# Encuentra el máximo
max_index = datos.index(max(datos))
max_value = max(datos)

# Anota el máximo con flecha
plt.annotate(
    f"Pico: ${max_value}",        # Texto
    xy=(max_index, max_value),     # Posición del punto
    xytext=(max_index-1, max_value+10),  # Posición del texto
    arrowprops=dict(arrowstyle="->", color="red", lw=2),  # Flecha roja
    fontsize=10,
    bbox=dict(boxstyle="round,pad=0.5", facecolor="yellow", alpha=0.7)
)

plt.title("Ventas con Punto Máximo Destacado")
plt.xlabel("Mes")
plt.ylabel("Ventas ($)")
```

**Desafío extra**: Agrega OTRA anotación para el MÍNIMO con flecha azul.

**Reflexión**: ¿Por qué destacar máximos y mínimos? ¿Qué pregunta responden?

---

### Reto 3: `03_escala_logaritmica.py` [Nivel 3] - Escala logarítmica

**Qué harás**: Comparar dos gráficas: una con escala NORMAL y otra con escala LOGARÍTMICA.

**Concepto clave**: Escala logarítmica comprime grandes números. Útil cuando datos varían de 10 a 1 millón.

| Escala | Cuándo usar |
|--------|-------------|

| **Lineal** | Datos entre 100 y 500 (variación pequeña) |
| **Logarítmica** | Datos entre 10 y 1,000,000 (variación ENORME) |

**Datos**: Usuarios creciendo exponencialmente (10 → 100 → 1,000 → 1,000,000)

**Instrucciones paso a paso**:

```python
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Gráfica 1: Escala LINEAL
axes[0].plot(meses, usuarios, color="tab:blue", marker="o", linewidth=2)
axes[0].set_title("Escala Normal (Lineal)")
axes[0].set_ylabel("Usuarios")
axes[0].grid(alpha=0.3)

# Gráfica 2: Escala LOGARÍTMICA
axes[1].plot(meses, usuarios, color="tab:blue", marker="o", linewidth=2)
axes[1].set_yscale("log")  # ← AQUÍ ESTÁ LA DIFERENCIA
axes[1].set_title("Escala Logarítmica")
axes[1].grid(alpha=0.3, which="both")  # which="both" muestra grilla fina en log

fig.suptitle("Comparación: Escala Normal vs. Logarítmica")
fig.tight_layout()
```

**Desafío extra**: Usa `axes[1].set_xscale("log")` para escala log en el eje X también.

**Reflexión**: ¿En cuál escala es MÁS FÁCIL ver que el crecimiento es ACELERADO?

---

### Reto 4: `04_barras_comparativas.py` [Nivel 3] - Barras agrupadas

**Qué harás**: Crear BARRAS LADO A LADO para comparar dos períodos en 4 categorías.

**Concepto clave**: Desplazar las posiciones de las barras para que no se superpongan.

**Datos**: Ventas de 4 categorías en Mes 1 y Mes 2

**Instrucciones paso a paso**:

```python
categorias = ["Café", "Té", "Postres", "Sandwiches"]
mes1 = [100, 60, 80, 50]
mes2 = [110, 65, 75, 55]

# Crear posiciones desplazadas
x = np.arange(len(categorias))  # [0, 1, 2, 3]
ancho = 0.35

# Barras del Mes 1 en posiciones 0, 1, 2, 3
plt.bar(x - ancho/2, mes1, ancho, label="Mes 1", color="tab:blue")

# Barras del Mes 2 desplazadas 0.35 unidades (para no solaparse)
plt.bar(x + ancho/2, mes2, ancho, label="Mes 2", color="tab:red")

# Etiquetas en posiciones correctas
plt.xticks(x, categorias)

plt.title("Ventas por Categoría - Comparación Mes 1 vs. Mes 2")
plt.xlabel("Categoría")
plt.ylabel("Ventas ($)")
plt.legend()
plt.grid(alpha=0.3, axis="y")
```

**Desafío extra**: Agrega una TERCERA serie para Mes 3.

**Reflexión**: ¿Por qué barras lado a lado es mejor que superpuestas con alpha?

---

### Reto 5: `05_grafico_area.py` [Nivel 3] - Gráfico de área

**Qué harás**: Crear ÁREAS APILADAS que muestren cómo 4 categorías componen un total a lo largo del tiempo.

**Concepto clave**: `plt.stackplot()` apila áreas. Útil para ver composición: "¿Qué % de ventas viene de cada categoría?"

**Datos**: Ventas de 4 productos durante 6 meses

**Instrucciones paso a paso**:

```python
meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun"]
cafe = [100, 120, 110, 140, 160, 150]
te = [60, 65, 70, 75, 80, 78]
postres = [80, 85, 90, 95, 100, 98]
sandwiches = [50, 55, 60, 65, 70, 72]

plt.figure(figsize=(10, 6))

# stackplot apila las áreas automáticamente
plt.stackplot(
    meses,
    cafe, te, postres, sandwiches,
    labels=["Café", "Té", "Postres", "Sandwiches"],
    colors=["#8B4513", "#D4A574", "#FFE4B5", "#F5DEB3"],
    alpha=0.8
)

plt.title("Composición de Ventas Totales por Mes")
plt.xlabel("Mes")
plt.ylabel("Ventas ($)")
plt.legend(loc="upper left")
plt.grid(alpha=0.3, axis="y")
```

**Desafío extra**: Cambia `alpha=0.8` a `alpha=0.5` y observa la diferencia.

**Reflexión**: ¿Cuál categoría crece más? ¿Cuál mantiene proporción constante?

---

### Reto 6: `06_combinado_linea_barras.py` [Nivel 3] - Ejes Y duales

**Qué harás**: Combinar BARRAS (en eje Y izquierdo) + LÍNEA (en eje Y derecho) porque tienen escalas muy diferentes.

**Concepto clave**: Usa `ax.twinx()` para crear un segundo eje Y con otra escala.

**Datos**: Ventas en $ vs. Cantidad de clientes (escalas completamente diferentes)

**Instrucciones paso a paso**:

```python
meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun"]
ventas = [1000, 1200, 1100, 1400, 1600, 1500]  # en $
clientes = [50, 55, 60, 65, 70, 72]  # en cantidad

fig, ax1 = plt.subplots(figsize=(10, 6))

# Eje 1 (izquierda): Barras de ventas
ax1.bar(meses, ventas, color="tab:blue", alpha=0.7, label="Ventas")
ax1.set_ylabel("Ventas ($)", color="tab:blue")
ax1.set_xlabel("Mes")

# Eje 2 (derecha): Línea de clientes (escala diferente)
ax2 = ax1.twinx()  # ← Crea segundo eje Y
ax2.plot(meses, clientes, color="tab:red", marker="o", linewidth=2, label="Clientes")
ax2.set_ylabel("Cantidad de Clientes", color="tab:red")

# Leyenda combinada
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left")

fig.suptitle("Ventas vs. Clientes (Ejes con Escalas Diferentes)")
fig.tight_layout()
```

**Desafío extra**: Intenta con `ax2.bar()` en lugar de línea.

**Reflexión**: ¿Hay correlación entre clientes y ventas? ¿Cuando sube uno, sube el otro?

---

### Reto 7: `07_personalizado_avanzado.py` [Nivel 3] - Personalización profesional

**Qué harás**: Crear una gráfica COMPLETAMENTE PULIDA lista para una presentación ejecutiva.

**Concepto clave**: Detalles visuales importan: spines, grid refinado, cajas de texto, DPI alta.

**Datos**: Ventas reales vs. proyectadas

**Instrucciones paso a paso**:

```python
import matplotlib.pyplot as plt

meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun"]
real = [100, 120, 110, 140, 160, 150]
proyectado = [100, 115, 125, 135, 155, 170]

fig, ax = plt.subplots(figsize=(12, 7), dpi=300)  # Alta resolución

# Gráficas
ax.plot(meses, real, color="#2E86AB", marker="o", linewidth=3, label="Real", markersize=8)
ax.plot(meses, proyectado, color="#A23B72", marker="s", linewidth=3, linestyle="--", label="Proyectado", markersize=8)

# Personalización de spines (bordes)
ax.spines["top"].set_visible(False)    # Quitar borde superior
ax.spines["right"].set_visible(False)  # Quitar borde derecho
ax.spines["left"].set_color("#CCCCCC")
ax.spines["bottom"].set_color("#CCCCCC")

# Grid refinado
ax.grid(alpha=0.4, linestyle="--", axis="y", color="#EEEEEE")

# Titles y labels
ax.set_title("Comparación: Ventas Reales vs. Proyectadas", fontsize=16, fontweight="bold", pad=20)
ax.set_xlabel("Mes", fontsize=12, fontweight="bold")
ax.set_ylabel("Ventas ($)", fontsize=12, fontweight="bold")

# Caja de texto con insight
textbox = ax.text(0.02, 0.95, "Variación Observada: -3.2% en Mar", 
                  transform=ax.transAxes,
                  fontsize=11,
                  verticalalignment="top",
                  bbox=dict(boxstyle="round,pad=0.8", facecolor="#FFF3CD", edgecolor="#FFC107", linewidth=2))

# Leyenda refinada
ax.legend(loc="lower right", frameon=True, fancybox=True, shadow=True, fontsize=11)

fig.tight_layout()

# Guardar en alta resolución
plt.savefig("ventas_profesional.png", dpi=300, bbox_inches="tight")
```

**Desafío extra**: Agrega más cajas de texto con insights clave.

**Reflexión**: ¿Cuál es la diferencia visual entre una gráfica "básica" y una "profesional"?

---

## Estrategia de estudio

### Antes de cada reto

1. **Ejecuta el código existente** - ¿Qué ya funciona?
2. **Lee los comentarios** - Entiende qué cada línea intenta hacer
3. **Dibuja mentalmente** - Visualiza qué debería verse

### Después de cada reto

1. **Experimenta**: Cambia `figsize`, colores, cantidad de subplots
2. **Compara métodos**: ¿Qué diferencia hay entre `plt.plot()` y `axes[0].plot()`?
3. **Aplica aprendizaje**: Usa el método en nuevos datos

---

## Errores comunes en este bloque

- **Subplots sin título**: Usa `fig.suptitle()` para el título general
- **Textos superpuestos**: Agrega `fig.tight_layout()` antes de `plt.show()`
- **Anotaciones fuera del gráfico**: Ajusta `xytext` si la etiqueta no se ve
- **Escala log con valores negativos o 0**: Solo funciona con valores positivos > 0

---

## Checklist de finalización

- [ ] Completé el Reto 1 y entiendo `fig, axes = plt.subplots()`
- [ ] Completé el Reto 2 y sé marcar puntos con `annotate()`
- [ ] Completé el Reto 3 y entiendo cuándo usar escala logarítmica (comparé lineal vs log)
- [ ] Completé el Reto 4 y puedo crear barras agrupadas con desplazamiento
- [ ] Completé el Reto 5 y entiendo `stackplot()` para áreas apiladas
- [ ] Completé el Reto 6 y sé usar `twinx()` para ejes Y duales
- [ ] Completé el Reto 7 y domino spines, grid y diseño profesional
- [ ] Puedo explicar para qué sirve cada método avanzado
- [ ] He experimentado modificando parámetros para entender efectos
- [ ] Puedo crear gráficas listas para presentación ejecutiva
