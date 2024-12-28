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
