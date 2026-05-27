# Python Intermedio

Repositorio de prácticas y apuntes para consolidar Python a nivel intermedio, con foco en NumPy, Matplotlib y Pandas. Contiene retos guiados, ejemplos reutilizables y datos de apoyo para practicar localmente.

![Logo de Python](https://www.python.org/static/community_logos/python-logo.png)

> [!TIP]
> Usa la `Ruta rápida` para ir directo al módulo que quieras practicar.

## Ruta rápida

| Quieres practicar | Ve a |
| --- | --- |
| NumPy | [numpy/](numpy/) |
| Matplotlib | [matplotlib/](matplotlib/) |
| Pandas | [pandas/](pandas/) |
| Datos de apoyo | [data/](data/) |

## Qué encontrarás aquí

- Retos por bloques con soluciones y explicaciones.
- Ejemplos comentados listos para ejecutar.
- Datos de apoyo en `data/` para reproducir ejemplos.
- Documentación didáctica orientada a la práctica.

## Módulos principales

| Módulo | Enfoque |
| --- | --- |
| NumPy | Arreglos, indexado, operaciones vectorizadas. |
| Matplotlib | Visualización, personalización y subplots. |
| Pandas | Estructuras `DataFrame`, selección, joins y groupby. |

## Estructura general

```text
python_intermedio/
├── data/
│   ├── numpy/
│   ├── matplotlib/
│   └── pandas/
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
│       ├── bloque_2/
│       ├── bloque_3/
│       └── bloque_4/
└── README.md
```

La idea es que cada módulo mantenga una forma parecida para que puedas cambiar de tema sin perder contexto.

## Cómo empezar (rápido)

1. Clona el repositorio.
2. Entra al módulo que quieras practicar (por ejemplo `pandas/`).
3. Crea y activa un entorno virtual.
4. Instala las dependencias del módulo que usarás.

```bash
python3 -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -r pandas/requirements.txt
```

Ejecuta los scripts con `python archivos/script.py` o abre los notebooks si los hay.

## Buenas prácticas del repo

- Mantén un entorno virtual por módulo.
- Ejecuta los ejemplos paso a paso y revisa las salidas.
- Documenta cambios y añade ejemplos reproducibles.

## Actualizaciones recientes

- Añadido material de `pandas/retos/bloque_4` (joins y fusiones, self-merge).
- Normalizadas las plantillas de README por módulo y ejemplos con salidas.
- Agregadas vistas visuales en ejemplos para facilitar la lectura de resultados.

## Próximos pasos

- Más mini-proyectos que integren NumPy + Pandas + Matplotlib.
- Añadir notebooks interactivos y capturas de resultados.
- Revisión ortográfica y consistencia de estilo en todos los READMEs.

## Estado

Activo — en mejora continua. Pull requests y sugerencias son bienvenidas.

## Contribuir

1. Crea una rama nueva: `git checkout -b feat/mi-ejemplo`.
2. Haz tus cambios en la carpeta correspondiente.
3. Abre un PR describiendo el objetivo.

## Contacto

- GitHub: [hugofriasmtz](https://github.com/hugofriasmtz)
- LinkedIn: [hugofriasmtz](https://www.linkedin.com/in/hugofriasmtz)
- Correo: [hugofriasmtz@hotmail.com](mailto:hugofriasmtz@hotmail.com)
