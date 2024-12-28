from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QLineEdit, QLabel, QHBoxLayout, QMessageBox
)
from PyQt6.QtCore import Qt
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from config import *
from modules.plan_trabajo import PlanTrabajo


class PlanTrabajoUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gestión de Plan de Trabajo")
        self.setGeometry(100, 100, 600, 400)

        # Instancia del módulo PlanTrabajo
        self.plan_trabajo = PlanTrabajo()

        # Layout principal
        layout = QVBoxLayout()

        # Tabla para mostrar las actividades
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(3)
        self.tabla.setHorizontalHeaderLabels(["ID", "Título", "Fecha y Hora"])
                        # Aplica el estilo a la tabla
        self.tabla.setStyleSheet("""
            QTableWidget {
                background-color: #F8F9FA;
                border: 1px solid #CED4DA;
            }

            QTableWidget::item {
                border: 0px;
            }
        """)
        self.tabla.setGridStyle(Qt.PenStyle.SolidLine)
        layout.addWidget(self.tabla)

        # Botones de acciones
        botones_layout = QHBoxLayout()
        btn_agregar = QPushButton("Agregar Actividad")
        btn_agregar.clicked.connect(self.agregar_actividad)
        botones_layout.addWidget(btn_agregar)

        btn_listar = QPushButton("Listar Actividades")
        btn_listar.clicked.connect(self.listar_actividades)
        botones_layout.addWidget(btn_listar)

        btn_eliminar = QPushButton("Eliminar Actividad")
        btn_eliminar.clicked.connect(self.eliminar_actividad)
        botones_layout.addWidget(btn_eliminar)

        layout.addLayout(botones_layout)

        # Campos para agregar una actividad
        self.campo_titulo = QLineEdit()
        self.campo_titulo.setPlaceholderText("Título de la actividad")
        layout.addWidget(self.campo_titulo)

        self.campo_fecha_hora = QLineEdit()
        self.campo_fecha_hora.setPlaceholderText("Fecha y Hora (YYYY-MM-DD HH:MM)")
        layout.addWidget(self.campo_fecha_hora)

        self.setLayout(layout)

    def agregar_actividad(self):
        """Agrega una nueva actividad al plan de trabajo."""
        titulo = self.campo_titulo.text()
        fecha_hora = self.campo_fecha_hora.text()

        if titulo and fecha_hora:
            try:
                self.plan_trabajo.agregar_actividad(titulo, "", fecha_hora)
                QMessageBox.information(self, "Éxito", f"Actividad '{titulo}' agregada.")
                self.campo_titulo.clear()
                self.campo_fecha_hora.clear()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo agregar la actividad: {e}")
        else:
            QMessageBox.warning(self, "Advertencia", "Por favor, complete todos los campos.")

    def listar_actividades(self):
        """Muestra las actividades en la tabla."""
        try:
            actividades = self.plan_trabajo.listar_actividades()  # Método del módulo PlanTrabajo
            self.tabla.setRowCount(0)  # Limpia la tabla

            for fila, actividad in enumerate(actividades):
                self.tabla.insertRow(fila)
                self.tabla.setItem(fila, 0, QTableWidgetItem(str(actividad[0])))
                self.tabla.setItem(fila, 1, QTableWidgetItem(actividad[1]))
                self.tabla.setItem(fila, 2, QTableWidgetItem(actividad[3]))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudieron listar las actividades: {e}")

    def eliminar_actividad(self):
        """Elimina una actividad seleccionada."""
        fila_seleccionada = self.tabla.currentRow()
        if fila_seleccionada >= 0:
            actividad_id = self.tabla.item(fila_seleccionada, 0).text()
            try:
                self.plan_trabajo.eliminar_actividad(int(actividad_id))
                QMessageBox.information(self, "Éxito", f"Actividad con ID {actividad_id} eliminada.")
                self.listar_actividades()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo eliminar la actividad: {e}")
        else:
            QMessageBox.warning(self, "Advertencia", "Seleccione una actividad para eliminar.")


if __name__ == "__main__":
    from PyQt6.QtWidgets import QApplication

    app = QApplication([])
    ventana = PlanTrabajoUI()
    ventana.show()
    app.exec()
