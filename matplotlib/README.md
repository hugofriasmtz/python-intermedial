# Matplotlib: introduccion visual

![matplotlib logo](https://upload.wikimedia.org/wikipedia/commons/8/84/Matplotlib_icon.svg)

> De una linea simple a una grafica clara y presentable: este modulo te lleva paso a paso por lo esencial de matplotlib.

---

## Tabla de contenido

1. [Que es matplotlib](#que-es-matplotlib)
2. [Que puedes lograr con matplotlib](#que-puedes-lograr-con-matplotlib)
3. [Ruta de aprendizaje de este modulo](#ruta-de-aprendizaje-de-este-modulo)
4. [Como ejecutar los retos](#como-ejecutar-los-retos)
5. [Convencion de nombres](#convencion-de-nombres)
6. [Datos del modulo](#datos-del-modulo)
7. [Recursos oficiales](#recursos-oficiales)
8. [Estado del modulo](#estado-del-modulo)

---

## Que es matplotlib

matplotlib es la libreria de Python para crear graficas de datos.

Con matplotlib puedes:

- Explorar datos rapidamente.
- Comparar valores entre categorias.
- Mostrar tendencias en el tiempo.
- Resaltar hallazgos con anotaciones.
- Preparar graficas para reportes o presentaciones.

En palabras simples: matplotlib convierte datos en historias visuales.

---

## Que puedes lograr con matplotlib

### Analisis de ventas

- Ver como cambian las ventas por mes.
- Comparar productos o categorias.
- Detectar picos y caidas.

### Analisis de comportamiento

- Comparar dos periodos.
- Encontrar relaciones entre variables.
- Revisar distribuciones y patrones.

### Presentacion de resultados

- Crear graficas limpias y entendibles.
- Resaltar un hallazgo importante.
- Ajustar el diseño para que se vea mejor.

---

## Ruta de aprendizaje de este modulo

Este modulo esta organizado en dos bloques:

1. `retos/bloque_1` - fundamentos de visualizacion.
2. `retos/bloque_2` - visualizacion intermedia.

### Bloque 1: fundamentos

- Retos 1-2: primeras graficas con lineas y barras.
- Reto 3: comparacion de dos series con transparencia.
- Retos 4-5: personalizacion y multiples series.
- Retos 6-7: histogramas y scatter plots.

### Bloque 2: intermedio

- Retos 1-2: subplots y anotaciones.
- Reto 3: escala logaritmica.
- Reto 4: barras agrupadas.
- Retos 5-7: area apilada, ejes duales y diseño profesional.

---

## Como ejecutar los retos

Desde la raiz de este modulo:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r matplotlib/requirements.txt
python matplotlib/retos/bloque_1/01_lineas.py
```

Puedes cambiar el ultimo archivo por cualquiera de los otros retos.

Si estas en Linux y `plt.show()` no abre una ventana, instala soporte grafico con:

```bash
sudo apt install python3-tk
```

Tambien puedes guardar la figura con `plt.savefig()` si no quieres abrir ventana.

---

## Convencion de nombres

Los retos siguen este formato:

- `01_tema.py`
- `02_tema.py`
- `03_tema.py`

Esto ayuda a mantener el orden y a resolverlos en secuencia.

---

## Datos del modulo

Si un reto necesita datos de entrada, los encontraras en:

- `data/matplotlib/`

Archivo disponible:

- `ventas_cafeteria.csv` - ventas mensuales de una cafetería por categoria.

---

## Recursos oficiales

- [Sitio oficial de matplotlib](https://matplotlib.org/)
- [Galeria de ejemplos](https://matplotlib.org/stable/gallery/index.html)
- [Documentacion de pyplot](https://matplotlib.org/stable/api/pyplot_summary.html)
- [Colores nombrados](https://matplotlib.org/stable/gallery/color/named_colors.html)

---

## Estado del modulo

- Los README de cada bloque explican que haras en cada bloque y cada reto.
- Los archivos `.py` contienen solo lo necesario para resolver cada ejercicio.
- La idea es aprender por etapas, con poco ruido y con una ruta clara.
