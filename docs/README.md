# Gestión del Hogar

**Gestión del Hogar** es una aplicación modular de escritorio desarrollada en Python, diseñada para simplificar las tareas cotidianas y la gestión del hogar. La aplicación utiliza una base de datos centralizada y ofrece un menú principal dinámico que conecta con diferentes módulos funcionales.

## Funcionalidades Principales

- **Agenda**: Gestión de eventos y recordatorios.
- **Reparaciones**: Registro y seguimiento de reparaciones en el hogar.
- **Lista de Tareas**: Organización de tareas con prioridades y estados.
- **Inventario**: Control de artículos con cantidades, ubicaciones y fechas de caducidad.
- **Lista de Objetivos**: Planificación y seguimiento de metas personales.
- **Plan de Trabajo**: Organización de actividades con descripciones y fechas.
- **Calendario**: Visualización cronológica de eventos.

## Tecnologías Usadas

- **Lenguaje**: Python 3.12
- **Base de Datos**: SQLite
- **Gestión de Dependencias**: Archivo `requirements.txt`
- **Control de Versiones**: Git y GitHub

## Estructura del Proyecto

El proyecto sigue una arquitectura modular para facilitar la escalabilidad y el mantenimiento.

```plaintext
proyecto_app/
├── main.py              # Punto de entrada de la aplicación.
├── config.py            # Configuraciones globales del proyecto.
├── db_manager.py        # Módulo para gestionar la base de datos SQLite.
├── modules/             # Directorio para los módulos funcionales.
│   ├── agenda.py            # Gestión de eventos y recordatorios.
│   ├── reparaciones.py      # Gestión de reparaciones.
│   ├── lista_tareas.py      # Gestión de tareas pendientes.
│   ├── inventario.py        # Control del inventario del hogar.
│   ├── objetivos.py         # Seguimiento de objetivos personales.
│   ├── plan_trabajo.py      # Organización de actividades.
│   ├── calendario.py        # Visualización cronológica de eventos.
├── ui/                  # Directorio para la interfaz gráfica.
│   ├── main_window.py       # Ventana principal con el menú.
│   ├── reparaciones_ui.py   # Interfaz gráfica para reparaciones.
│   ├── agenda_ui.py         # Interfaz gráfica para la agenda.
│   ├── tareas_ui.py         # Interfaz gráfica para las tareas.
│   ├── inventario_ui.py     # Interfaz gráfica para el inventario.
│   ├── objetivos_ui.py      # Interfaz gráfica para los objetivos.
│   ├── calendario_ui.py     # Interfaz gráfica para el calendario.
├── database/            # Archivos relacionados con la base de datos.
│   ├── app_data.db          # Archivo SQLite que almacena los datos.
│   ├── schema.sql           # Script SQL para inicializar la base de datos.
│   ├── db_manager.py        # Módulo para gestionar la base de datos.
├── tests/               # Pruebas unitarias e integración.
│   ├── test_db_manager.py   # Pruebas para el manejo de la base de datos.
│   ├── test_modules.py      # Pruebas para los módulos funcionales.
│   ├── test_ui.py           # Pruebas para la interfaz gráfica.
├── assets/              # Recursos estáticos como imágenes e íconos.
│   ├── icons/               # Íconos usados en la interfaz gráfica.
│   ├── images/              # Imágenes usadas en la aplicación.
└── docs/                # Documentación del proyecto.
    ├── README.md            # Descripción general del proyecto.
    ├── changelog.md         # Registro de cambios y actualizaciones.
    ├── roadmap.md           # Planificación futura del proyecto.
