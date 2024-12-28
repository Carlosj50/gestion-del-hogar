# Changelog

Todos los cambios relevantes en el proyecto se registrarán en este archivo.

## [0.1.0] - 2024-12-28
### Añadido
- **Estructura inicial del proyecto**:
  - Creación de carpetas: `modules/`, `ui/`, `database/`, `assets/`, `tests/`, y `docs/`.
  - Archivo principal `main.py` configurado como punto de entrada.
  - Archivo `db_manager.py` para manejar la base de datos SQLite.
  - Archivo `requirements.txt` con dependencias iniciales (`PyQt6`, `sqlite-utils`).
- **Base de datos**:
  - Creación del archivo `schema.sql` con la estructura de las tablas:
    - `opciones`: Menú dinámico para el proyecto.
    - `reparaciones`, `tareas`, `inventario`, `objetivos`, `plan_trabajo`, y `calendario`.
  - Ejecución inicial del script `db_manager.py` para generar el archivo de base de datos `app_data.db`.
- **Menú principal dinámico en `main.py`**:
  - Funcionalidad para mostrar el menú dinámico basado en la tabla `opciones`.
  - Gestión inicial de selección de opciones con mensajes de marcador para los módulos.

## Próximos pasos
- Implementar el primer módulo funcional (ejemplo: **Lista de Tareas** o **Reparaciones**).
- Diseñar la interfaz gráfica inicial en `ui/main_window.py`.
- Escribir pruebas iniciales para la base de datos y el menú principal.
# Changelog

Todos los cambios relevantes en el proyecto se registrarán en este archivo.

## [0.2.0] - 2024-12-28
### Añadido
- **Menú Principal (`main.py`)**:
  - Integración dinámica con la tabla `opciones` de la base de datos para generar el menú.
  - Llamada directa a cada módulo utilizando `os.system`.
  - Soporte para módulos almacenados en la carpeta `modules/`.

- **Módulos CRUD Finalizados**:
  - **Agenda**: Gestión de eventos con fechas y descripciones.
  - **Reparaciones**: Registro y seguimiento de reparaciones del hogar.
  - **Lista de Tareas**: Gestión de tareas con prioridades y estados.
  - **Inventario**: Control de artículos con cantidades, ubicaciones y fechas de caducidad.
  - **Lista de Objetivos**: Planificación y seguimiento de objetivos personales.
  - **Plan de Trabajo**: Organización de actividades con descripciones y fechas.
  - **Calendario**: Visualización cronológica de eventos y actividades.

### Cambiado
- Actualización en `manejar_opcion` para incluir el prefijo `modules/` en las rutas de los módulos llamados directamente desde el menú principal.

### Próximos pasos
- **Refinamiento**:
  - Mejorar la validación de entradas del usuario en todos los módulos.
  - Optimizar el manejo de errores en caso de fallos o rutas de módulos incorrectas.
- **Documentación**:
  - Ampliar el `README.md` para incluir instrucciones detalladas sobre la estructura y uso del proyecto.
- **Pruebas**:
  - Crear pruebas unitarias para cada módulo y para el menú principal.
