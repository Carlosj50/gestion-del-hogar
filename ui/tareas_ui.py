from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QLineEdit, QLabel, QHBoxLayout, QMessageBox, QComboBox
)
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from config import *
from modules.lista_tareas import ListaTareas


class TareasUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gestión de Tareas")
        self.setGeometry(100, 100, 600, 400)
        with open(UI_DIR + "style.qss", "r") as style_file:
            app.setStyleSheet(style_file.read())
        # Instancia del módulo ListaTareas
        self.tareas = ListaTareas()

        # Layout principal
        layout = QVBoxLayout()

        # Tabla para mostrar las tareas
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(5)
        self.tabla.setHorizontalHeaderLabels(["ID", "Título", "Prioridad", "Fecha y Hora", "Estado"])
        layout.addWidget(self.tabla)

        # Botones de acciones
        botones_layout = QHBoxLayout()
        btn_agregar = QPushButton("Agregar Tarea")
        btn_agregar.clicked.connect(self.agregar_tarea)
        botones_layout.addWidget(btn_agregar)

        btn_listar = QPushButton("Listar Tareas")
        btn_listar.clicked.connect(self.listar_tareas)
        botones_layout.addWidget(btn_listar)

        btn_eliminar = QPushButton("Eliminar Tarea")
        btn_eliminar.clicked.connect(self.eliminar_tarea)
        botones_layout.addWidget(btn_eliminar)

        layout.addLayout(botones_layout)

        # Campos para agregar una tarea
        self.campo_titulo = QLineEdit()
        self.campo_titulo.setPlaceholderText("Título de la tarea")
        layout.addWidget(self.campo_titulo)

        self.campo_prioridad = QComboBox()
        self.campo_prioridad.addItems(["Alta", "Media", "Baja"])
        layout.addWidget(self.campo_prioridad)

        self.campo_fecha_hora = QLineEdit()
        self.campo_fecha_hora.setPlaceholderText("Fecha y Hora (YYYY-MM-DD HH:MM)")
        layout.addWidget(self.campo_fecha_hora)

        self.campo_estado = QComboBox()
        self.campo_estado.addItems(["Pendiente", "En Progreso", "Completada"])
        layout.addWidget(self.campo_estado)

        self.setLayout(layout)

    def agregar_tarea(self):
        """Agrega una nueva tarea a la base de datos."""
        titulo = self.campo_titulo.text()
        prioridad = self.campo_prioridad.currentText()
        fecha_hora = self.campo_fecha_hora.text()
        estado = self.campo_estado.currentText()

        if titulo:
            try:
                self.tareas.agregar_tarea(titulo, "", prioridad, fecha_hora if fecha_hora else None, estado)
                QMessageBox.information(self, "Éxito", f"Tarea '{titulo}' agregada.")
                self.campo_titulo.clear()
                self.campo_fecha_hora.clear()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo agregar la tarea: {e}")
        else:
            QMessageBox.warning(self, "Advertencia", "Por favor, ingrese el título de la tarea.")

    def listar_tareas(self):
        """Muestra las tareas en la tabla."""
        try:
            tareas = self.tareas.listar_tareas()  # Método del módulo ListaTareas
            self.tabla.setRowCount(0)  # Limpia la tabla

            for fila, tarea in enumerate(tareas):
                self.tabla.insertRow(fila)
                self.tabla.setItem(fila, 0, QTableWidgetItem(str(tarea[0])))
                self.tabla.setItem(fila, 1, QTableWidgetItem(tarea[1]))
                self.tabla.setItem(fila, 2, QTableWidgetItem(tarea[3]))
                self.tabla.setItem(fila, 3, QTableWidgetItem(tarea[4] if tarea[4] else "Sin Fecha"))
                self.tabla.setItem(fila, 4, QTableWidgetItem(tarea[5]))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudieron listar las tareas: {e}")

    def eliminar_tarea(self):
        """Elimina una tarea seleccionada."""
        fila_seleccionada = self.tabla.currentRow()
        if fila_seleccionada >= 0:
            tarea_id = self.tabla.item(fila_seleccionada, 0).text()
            try:
                self.tareas.eliminar_tarea(int(tarea_id))
                QMessageBox.information(self, "Éxito", f"Tarea con ID {tarea_id} eliminada.")
                self.listar_tareas()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo eliminar la tarea: {e}")
        else:
            QMessageBox.warning(self, "Advertencia", "Seleccione una tarea para eliminar.")


if __name__ == "__main__":
    from PyQt6.QtWidgets import QApplication

    app = QApplication([])
    ventana = TareasUI()
    ventana.show()
    app.exec()
