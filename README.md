Gestión del Hogar

Gestión del Hogar es una aplicación de escritorio desarrollada en Python para ayudar a organizar y gestionar las tareas del día a día de manera eficiente. El proyecto está diseñado para ser modular y escalable, integrando diferentes funcionalidades que se ajustan a las necesidades del hogar y la vida personal.

Funcionalidades Principales:


Reparaciones: Registro de reparaciones del hogar, incluyendo descripción, costos y estado.

Agenda: Organización de eventos y recordatorios importantes.

Lista de Tareas: Gestión de tareas pendientes con prioridades y fechas.

Inventario: Control de elementos del hogar, incluyendo cantidades y fechas de caducidad.

Lista de Objetivos: Planificación de metas personales y seguimiento del progreso.

Plan de Trabajo: Organización de actividades para cumplir objetivos a corto y largo plazo.

Calendario: Visualización de eventos y tareas en un formato cronológico.


Tecnologías Usadas
Lenguaje: Python 3.12
Base de Datos: SQLite
Interfaz Gráfica: PyQt6
Control de Versiones: Git y GitHub

Estructura del Proyecto

El proyecto sigue una arquitectura modular para facilitar la escalabilidad y el mantenimiento. Las principales carpetas son:

modules/: Contiene los módulos funcionales de la aplicación (CRUD para cada funcionalidad).
ui/: Código relacionado con la interfaz gráfica.
database/: Archivos relacionados con la base de datos, incluyendo el esquema y el archivo SQLite.
assets/: Recursos estáticos como íconos e imágenes.
tests/: Scripts para pruebas unitarias y de integración.
docs/: Documentación adicional sobre el proyecto.

Instalación y Ejecución:
Clona el repositorio:
git clone https://github.com/tu-usuario/gestion-del-hogar.git
cd gestion-del-hogar

Instala las dependencias: Asegúrate de tener Python 3.12 instalado y ejecuta:
pip install -r requirements.txt

Inicia la aplicación: Ejecuta el archivo principal:
python main.py

Roadmap

 Implementar los módulos base (Reparaciones, Agenda, etc.).
 
 Diseñar la interfaz gráfica inicial.
 
 Integrar inteligencia artificial para automatización y análisis de datos.
 
 Mejorar el soporte para exportación de datos (CSV, PDF).
 

Contribución
¡Contribuciones son bienvenidas! Si quieres colaborar, por favor abre un issue o envía un pull request con tus mejoras.
