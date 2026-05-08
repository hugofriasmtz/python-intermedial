# pandas: Introduccion Visual para Principiantes

![pandas logo](https://pandas.pydata.org/static/img/pandas.svg)

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-data%20analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Nivel](https://img.shields.io/badge/Nivel-Principiante-0A7E07?style=for-the-badge)

> De datos sueltos a decisiones claras: esta carpeta te enseña la base de pandas paso a paso.

---

## Tabla de Contenido

1. [Que es pandas](#que-es-pandas)
2. [Que puedes lograr con pandas](#que-puedes-lograr-con-pandas)
3. [Donde se usa en el mundo real](#donde-se-usa-en-el-mundo-real)
4. [Ruta de aprendizaje del modulo](#ruta-de-aprendizaje-del-modulo)
5. [Como ejecutar los retos](#como-ejecutar-los-retos)
6. [Convencion de nombres de retos](#convencion-de-nombres-de-retos)
7. [Datos del modulo](#datos-del-modulo)
8. [Recursos oficiales](#recursos-oficiales)
9. [Imagenes y creditos](#imagenes-y-creditos)

---

## Que es pandas

pandas es una libreria de Python para trabajar con datos en formato tabular.

Con pandas puedes:

- Explorar informacion rapidamente.
- Limpiar datos incompletos o inconsistentes.
- Transformar columnas y formatos.
- Resumir resultados en minutos.
- Preparar informacion para reportes y visualizacion.

En palabras simples: pandas te ayuda a convertir tablas desordenadas en respuestas utiles.

---

## Que puedes lograr con pandas

![pandas secondary logo](https://pandas.pydata.org/static/img/pandas_secondary.svg)

### Analisis de ventas

- Encontrar que ciudad vende mas.
- Comparar meses buenos y meses bajos.
- Detectar productos con baja rotacion.

### Analisis de negocio digital

- Medir resultados por canal.
- Identificar clientes frecuentes.
- Evaluar tendencias por temporada.

### Analisis en educacion y salud

- Resumir desempeno por grupo.
- Revisar evolucion en el tiempo.
- Detectar patrones para mejorar decisiones.

---

## Donde se usa en el mundo real

![pandas mark](https://pandas.pydata.org/static/img/pandas_mark.svg)

pandas se usa en:

- Fintech y banca: monitoreo de transacciones y riesgo.
- Marketing: analisis de campanas y retorno de inversion.
- Logistica: seguimiento de rutas, tiempos y costos.
- Investigacion: limpieza y validacion de datos experimentales.
- Educacion: reportes academicos y seguimiento estudiantil.

Si tu trabajo involucra tablas o reportes, pandas es una habilidad clave.

---

## Ruta de aprendizaje del modulo

Este modulo esta pensado para avanzar con estructura clara:

1. `retos/bloque_1`: fundamentos (estructura, seleccion, filtros basicos).
2. `retos/bloque_2`: operaciones intermedias (groupby, merge, pivot, fechas).
3. `retos/bloque_3`: estadisticas de Series y conteo (resumen numerico, acumulados, duplicados y frecuencias).

Recomendacion de uso:

- Lee primero el README del bloque.
- Resuelve el reto por tu cuenta.
- Compara y mejora tu solucion.

Si estas ampliando el contenido, mi recomendacion es crear un bloque 3 en lugar de sobrecargar el bloque 2. Los temas de estadisticas de Series y conteo forman una familia propia y se entienden mejor como una etapa posterior.

---

## Como ejecutar los retos

Desde la raiz del repo:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r pandas/requirements.txt
python pandas/retos/bloque_1/01_dataframe_basico.py
```

Puedes cambiar el archivo final por cualquier otro reto del bloque 1, 2 o 3.

---

## Convencion de nombres de retos

Los ejercicios de pandas usan el formato:

- `01_tema.py`
- `02_tema.py`
- `03_tema.py`

Esto ayuda a mantener orden consistente y facilita ejecutarlos en secuencia.

---

## Datos del modulo

Si un reto requiere archivos de entrada, puedes colocarlos en:

- `data/pandas/`

Asi evitas duplicar datasets en varias carpetas.

---

## Recursos oficiales

- [Sitio oficial de pandas](https://pandas.pydata.org/)
- [Documentacion oficial](https://pandas.pydata.org/docs/)
- [Getting Started](https://pandas.pydata.org/docs/getting_started/index.html)
- [API Reference](https://pandas.pydata.org/docs/reference/index.html)
- [Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)

---

## Imagenes y creditos

Imagenes usadas por referencia visual de la libreria pandas:

- Logo principal: `https://pandas.pydata.org/static/img/pandas.svg`
- Logo principal (fondo oscuro): `https://pandas.pydata.org/static/img/pandas_white.svg`
- Logo secundario: `https://pandas.pydata.org/static/img/pandas_secondary.svg`
- Marca (icono): `https://pandas.pydata.org/static/img/pandas_mark.svg`

Fuente de marca y lineamientos:

- [Citing and logo - pandas](https://github.com/pandas-dev/pandas/blob/main/web/pandas/about/citing.md)

---

**Estado:** En construccion
