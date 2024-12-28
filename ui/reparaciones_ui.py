from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QLineEdit, QLabel, QHBoxLayout, QMessageBox
)
from PyQt6.QtCore import Qt
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from config import *
from modules.reparaciones import Reparaciones


class ReparacionesUI(QWidget):
    def __init__(self, db_manager):
        super().__init__()

        self.setWindowTitle("Gestión de Reparaciones")
        self.setGeometry(100, 100, 600, 400)

        # Instancia del módulo Reparaciones
        self.reparaciones = Reparaciones(db_manager)

        # Layout principal
        layout = QVBoxLayout()
        
                # Aplicar estilo
        self.aplicar_estilo()

        # Tabla para mostrar reparaciones
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(4)
        self.tabla.setHorizontalHeaderLabels(["ID", "Descripción", "Fecha", "Costo"])
                        # Aplica el estilo a la tabla

        self.tabla.setGridStyle(Qt.PenStyle.SolidLine)
        layout.addWidget(self.tabla)

        # Botones de acciones
        botones_layout = QHBoxLayout()
        btn_agregar = QPushButton("Agregar Reparación")
        btn_agregar.clicked.connect(self.agregar_reparacion)
        botones_layout.addWidget(btn_agregar)

        btn_listar = QPushButton("Listar Reparaciones")
        btn_listar.clicked.connect(self.listar_reparaciones)
        botones_layout.addWidget(btn_listar)

        btn_eliminar = QPushButton("Eliminar Reparación")
        btn_eliminar.clicked.connect(self.eliminar_reparacion)
        botones_layout.addWidget(btn_eliminar)

        layout.addLayout(botones_layout)

        # Campos para agregar una reparación
        self.campo_descripcion = QLineEdit()
        self.campo_descripcion.setPlaceholderText("Descripción de la reparación")
        layout.addWidget(self.campo_descripcion)

        self.campo_fecha = QLineEdit()
        self.campo_fecha.setPlaceholderText("Fecha (YYYY-MM-DD)")
        layout.addWidget(self.campo_fecha)

        self.campo_costo = QLineEdit()
        self.campo_costo.setPlaceholderText("Costo")
        layout.addWidget(self.campo_costo)

        self.setLayout(layout)
        
    def aplicar_estilo(self):
        """Carga y aplica un archivo de estilo QSS."""
        try:
            with open("ui/style.qss", "r") as archivo_estilo:
                estilo = archivo_estilo.read()
                self.setStyleSheet(estilo)
        except FileNotFoundError:
            print("Archivo de estilo 'style.qss' no encontrado. Usando estilos predeterminados.")

    def agregar_reparacion(self):
        """Agrega una nueva reparación a la base de datos."""
        descripcion = self.campo_descripcion.text()
        fecha = self.campo_fecha.text()
        costo = self.campo_costo.text()

        if descripcion and fecha and costo:
            try:
                self.reparaciones.agregar_reparacion(descripcion, fecha, float(costo), "Pendiente")
                QMessageBox.information(self, "Éxito", f"Reparación '{descripcion}' agregada.")
                self.campo_descripcion.clear()
                self.campo_fecha.clear()
                self.campo_costo.clear()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo agregar la reparación: {e}")
        else:
            QMessageBox.warning(self, "Advertencia", "Por favor, complete todos los campos.")

    def listar_reparaciones(self):
        """Muestra las reparaciones en la tabla."""
        try:
            reparaciones = self.reparaciones.listar_reparaciones()  # Método del módulo Reparaciones
            self.tabla.setRowCount(0)  # Limpia la tabla

            for fila, reparacion in enumerate(reparaciones):
                self.tabla.insertRow(fila)
                self.tabla.setItem(fila, 0, QTableWidgetItem(str(reparacion[0])))
                self.tabla.setItem(fila, 1, QTableWidgetItem(reparacion[1]))
                self.tabla.setItem(fila, 2, QTableWidgetItem(reparacion[2]))
                self.tabla.setItem(fila, 3, QTableWidgetItem(str(reparacion[3])))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudieron listar las reparaciones: {e}")

    def eliminar_reparacion(self):
        """Elimina una reparación seleccionada."""
        fila_seleccionada = self.tabla.currentRow()
        if fila_seleccionada >= 0:
            reparacion_id = self.tabla.item(fila_seleccionada, 0).text()
            try:
                self.reparaciones.eliminar_reparacion(int(reparacion_id))
                QMessageBox.information(self, "Éxito", f"Reparación con ID {reparacion_id} eliminada.")
                self.listar_reparaciones()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo eliminar la reparación: {e}")
        else:
            QMessageBox.warning(self, "Advertencia", "Seleccione una reparación para eliminar.")


if __name__ == "__main__":
    from PyQt6.QtWidgets import QApplication

    app = QApplication([])
    ventana = ReparacionesUI()
    ventana.show()
    app.exec()
