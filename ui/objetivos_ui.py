from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QLineEdit, QLabel, QHBoxLayout, QMessageBox
)
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from config import *
from modules.objetivos import ListaObjetivos


class ObjetivosUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gestión de Objetivos")
        self.setGeometry(100, 100, 600, 400)

        # Instancia del módulo Objetivos
        self.objetivos = ListaObjetivos()

        # Layout principal
        layout = QVBoxLayout()

        # Tabla para mostrar objetivos
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(4)
        self.tabla.setHorizontalHeaderLabels(["ID", "Objetivo", "Fecha Límite", "Progreso"])
        layout.addWidget(self.tabla)

        # Botones de acciones
        botones_layout = QHBoxLayout()
        btn_agregar = QPushButton("Agregar Objetivo")
        btn_agregar.clicked.connect(self.agregar_objetivo)
        botones_layout.addWidget(btn_agregar)

        btn_listar = QPushButton("Listar Objetivos")
        btn_listar.clicked.connect(self.listar_objetivos)
        botones_layout.addWidget(btn_listar)

        btn_eliminar = QPushButton("Eliminar Objetivo")
        btn_eliminar.clicked.connect(self.eliminar_objetivo)
        botones_layout.addWidget(btn_eliminar)

        layout.addLayout(botones_layout)

        # Campos para agregar un objetivo
        self.campo_objetivo = QLineEdit()
        self.campo_objetivo.setPlaceholderText("Nombre del objetivo")
        layout.addWidget(self.campo_objetivo)

        self.campo_fecha_limite = QLineEdit()
        self.campo_fecha_limite.setPlaceholderText("Fecha Límite (YYYY-MM-DD)")
        layout.addWidget(self.campo_fecha_limite)

        self.campo_progreso = QLineEdit()
        self.campo_progreso.setPlaceholderText("Progreso (%)")
        layout.addWidget(self.campo_progreso)

        self.setLayout(layout)

    def agregar_objetivo(self):
        """Agrega un nuevo objetivo a la base de datos."""
        objetivo = self.campo_objetivo.text()
        fecha_limite = self.campo_fecha_limite.text()
        progreso = self.campo_progreso.text()

        if objetivo and fecha_limite and progreso:
            try:
                self.objetivos.agregar_objetivo(objetivo, "", fecha_limite, int(progreso))
                QMessageBox.information(self, "Éxito", f"Objetivo '{objetivo}' agregado.")
                self.campo_objetivo.clear()
                self.campo_fecha_limite.clear()
                self.campo_progreso.clear()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo agregar el objetivo: {e}")
        else:
            QMessageBox.warning(self, "Advertencia", "Por favor, complete todos los campos.")

    def listar_objetivos(self):
        """Muestra los objetivos en la tabla."""
        try:
            objetivos = self.objetivos.listar_objetivos()  # Método del módulo Objetivos
            self.tabla.setRowCount(0)  # Limpia la tabla

            for fila, objetivo in enumerate(objetivos):
                self.tabla.insertRow(fila)
                self.tabla.setItem(fila, 0, QTableWidgetItem(str(objetivo[0])))
                self.tabla.setItem(fila, 1, QTableWidgetItem(objetivo[1]))
                self.tabla.setItem(fila, 2, QTableWidgetItem(objetivo[3]))
                self.tabla.setItem(fila, 3, QTableWidgetItem(str(objetivo[4]) + "%"))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudieron listar los objetivos: {e}")

    def eliminar_objetivo(self):
        """Elimina un objetivo seleccionado."""
        fila_seleccionada = self.tabla.currentRow()
        if fila_seleccionada >= 0:
            objetivo_id = self.tabla.item(fila_seleccionada, 0).text()
            try:
                self.objetivos.eliminar_objetivo(int(objetivo_id))
                QMessageBox.information(self, "Éxito", f"Objetivo con ID {objetivo_id} eliminado.")
                self.listar_objetivos()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo eliminar el objetivo: {e}")
        else:
            QMessageBox.warning(self, "Advertencia", "Seleccione un objetivo para eliminar.")


if __name__ == "__main__":
    from PyQt6.QtWidgets import QApplication

    app = QApplication([])
    ventana = ObjetivosUI()
    ventana.show()
    app.exec()
