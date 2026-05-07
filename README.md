# Python Intermedio

Repositorio de prácticas y apuntes para reforzar Python intermedio con un enfoque práctico: análisis de datos, visualización y uso de librerías clave del ecosistema científico.

![Logo de Python](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png)

## Qué vas a encontrar

- Ejercicios cortos y progresivos.
- Retos organizados por bloques para avanzar sin saltos bruscos.
- Apuntes con ejemplos concretos y listos para reutilizar.
- Material pensado para practicar en un entorno aislado por módulo.

## Mapa del proyecto

Este mapa sigue el orden actual del repositorio: NumPy, Matplotlib y Pandas.

```text
python_intermedio/
├── data/
│   ├── numpy/
│   │   ├── README.md
│   │   └── *.csv
│   ├── matplotlib/
│   │   ├── README.md
│   │   └── *.csv
│   └── pandas/
│       ├── README.md
│       └── *.csv
├── numpy/
│   ├── README.md
│   ├── requirements.txt
│   └── retos/
│       ├── bloque_1/
│       └── bloque_2/
├── matplotlib/
│   ├── README.md
│   ├── requirements.txt
│   └── retos/
│       ├── bloque_1/
│       └── bloque_2/
├── pandas/
│   ├── README.md
│   ├── requirements.txt
│   └── retos/
│       ├── bloque_1/
│       └── bloque_2/
└── README.md
```

Cada módulo mantiene una estructura parecida para que puedas moverte entre temas sin perder el contexto.

## Bloques principales

| Módulo | Enfoque |
| --- | --- |
| NumPy | Arreglos, tipos de datos, indexado y operaciones vectorizadas. |
| Matplotlib | Gráficos, personalización visual, subplots y combinaciones. |
| Pandas | DataFrames, selección, filtros, resúmenes y agrupaciones. |

## Cómo empezar

1. Clona el repositorio.
2. Entra a la carpeta del módulo que quieras practicar, por ejemplo `matplotlib/`.
3. Crea y activa un entorno virtual.
4. Instala las dependencias del módulo.
5. Resuelve los retos y anota tus aprendizajes.

Comandos base:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r numpy/requirements.txt
```

Si vas a trabajar con Pandas o Matplotlib, cambia la ruta del archivo `requirements.txt` al módulo correspondiente.

## Convenciones

- Una carpeta por librería o tema.
- Retos ordenados por bloques (`bloque_1`, `bloque_2`, etc.).
- Dependencias separadas por módulo.
- Entorno virtual fuera de control de versiones (`.venv/`).

## Próximas ideas

- Limpieza y transformación de datos.
- Mini proyectos integrando varias librerías.
- Más ejemplos visuales con capturas y resultados reales.

## Estado

En construcción. La idea es ir sumando prácticas, mejoras visuales y material de apoyo de forma continua.
