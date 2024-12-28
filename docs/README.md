# Gestión del Hogar

**Gestión del Hogar** es una aplicación de escritorio desarrollada en Python para ayudar a organizar y gestionar las tareas del día a día. El proyecto está diseñado para ser modular, escalable y fácil de mantener.

## Funcionalidades Principales

- **Agenda**: Gestión de eventos y recordatorios con fechas y descripciones.
- **Reparaciones**: Registro de reparaciones del hogar, incluyendo costos y estados.
- **Lista de Tareas**: Seguimiento de tareas con prioridades, fechas y estados.
- **Inventario**: Control de artículos con cantidades, ubicaciones y fechas de caducidad.
- **Lista de Objetivos**: Planificación y seguimiento de metas personales.
- **Plan de Trabajo**: Organización de actividades para alcanzar objetivos.
- **Calendario**: Visualización cronológica de eventos y actividades.

## Tecnologías Usadas

- **Lenguaje**: Python 3.12
- **Base de Datos**: SQLite
- **Gestión de Dependencias**: Archivo `requirements.txt`
- **Control de Versiones**: Git y GitHub

## Estructura del Proyecto

El proyecto sigue una arquitectura modular para facilitar la escalabilidad y el mantenimiento. Las principales carpetas y archivos son:

```plaintext
proyecto_app/
├── main.py              # Punto de entrada para la aplicación.
├── modules/             # Directorio para los módulos funcionales.
│   ├── agenda.py            # Gestión de eventos.
│   ├── reparaciones.py      # Gestión de reparaciones.
│   ├── lista_tareas.py      # Gestión de tareas pendientes.
│   ├── inventario.py        # Gestión del inventario del hogar.
│   ├── objetivos.py         # Gestión de metas personales.
│   ├── plan_trabajo.py      # Organización de actividades.
│   ├── calendario.py        # Gestión de eventos cronológicos.
├── database/            # Archivos relacionados con la base de datos.
│   ├── app_data.db          # Archivo SQLite con los datos del proyecto.
│   ├── schema.sql           # Script SQL para inicializar la base de datos.
├── tests/               # Pruebas unitarias y de integración.
│   ├── test_modules.py      # Pruebas para los módulos funcionales.
│   ├── test_integration.py  # Pruebas para la integración general.
├── requirements.txt     # Dependencias del proyecto.
└── README.md            # Documentación del proyecto.

