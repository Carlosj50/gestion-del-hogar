from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QLineEdit, QLabel, QHBoxLayout, QMessageBox
)
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from config import *
from modules.inventario import Inventario


class InventarioUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gestión de Inventario")
        self.setGeometry(100, 100, 600, 400)
        with open(UI_DIR + "style.qss", "r") as style_file:
            app.setStyleSheet(style_file.read())
        # Instancia del módulo Inventario
        self.inventario = Inventario()

        # Layout principal
        layout = QVBoxLayout()

        # Tabla para mostrar el inventario
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(4)
        self.tabla.setHorizontalHeaderLabels(["ID", "Item", "Cantidad", "Fecha de Caducidad"])
        layout.addWidget(self.tabla)

        # Botones de acciones
        botones_layout = QHBoxLayout()
        btn_agregar = QPushButton("Agregar Ítem")
        btn_agregar.clicked.connect(self.agregar_item)
        botones_layout.addWidget(btn_agregar)

        btn_listar = QPushButton("Listar Ítems")
        btn_listar.clicked.connect(self.listar_items)
        botones_layout.addWidget(btn_listar)

        btn_eliminar = QPushButton("Eliminar Ítem")
        btn_eliminar.clicked.connect(self.eliminar_item)
        botones_layout.addWidget(btn_eliminar)

        layout.addLayout(botones_layout)

        # Campos para agregar un ítem
        self.campo_item = QLineEdit()
        self.campo_item.setPlaceholderText("Nombre del ítem")
        layout.addWidget(self.campo_item)

        self.campo_cantidad = QLineEdit()
        self.campo_cantidad.setPlaceholderText("Cantidad")
        layout.addWidget(self.campo_cantidad)

        self.campo_fecha_caducidad = QLineEdit()
        self.campo_fecha_caducidad.setPlaceholderText("Fecha de Caducidad (YYYY-MM-DD)")
        layout.addWidget(self.campo_fecha_caducidad)

        self.setLayout(layout)

    def agregar_item(self):
        """Agrega un nuevo ítem al inventario."""
        item = self.campo_item.text()
        cantidad = self.campo_cantidad.text()
        fecha_caducidad = self.campo_fecha_caducidad.text()

        if item and cantidad:
            try:
                cantidad = int(cantidad)
                self.inventario.agregar_item(item, cantidad, "", fecha_caducidad if fecha_caducidad else None)
                QMessageBox.information(self, "Éxito", f"Ítem '{item}' agregado.")
                self.campo_item.clear()
                self.campo_cantidad.clear()
                self.campo_fecha_caducidad.clear()
            except ValueError:
                QMessageBox.warning(self, "Advertencia", "La cantidad debe ser un número entero.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo agregar el ítem: {e}")
        else:
            QMessageBox.warning(self, "Advertencia", "Por favor, complete los campos obligatorios (Nombre y Cantidad).")

    def listar_items(self):
        """Muestra los ítems del inventario en la tabla."""
        try:
            items = self.inventario.listar_items()  # Método del módulo Inventario
            self.tabla.setRowCount(0)  # Limpia la tabla

            for fila, item in enumerate(items):
                self.tabla.insertRow(fila)
                self.tabla.setItem(fila, 0, QTableWidgetItem(str(item[0])))
                self.tabla.setItem(fila, 1, QTableWidgetItem(item[1]))
                self.tabla.setItem(fila, 2, QTableWidgetItem(str(item[2])))
                self.tabla.setItem(fila, 3, QTableWidgetItem(item[4] if item[4] else "Sin Fecha"))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudieron listar los ítems: {e}")

    def eliminar_item(self):
        """Elimina un ítem seleccionado."""
        fila_seleccionada = self.tabla.currentRow()
        if fila_seleccionada >= 0:
            item_id = self.tabla.item(fila_seleccionada, 0).text()
            try:
                self.inventario.eliminar_item(int(item_id))
                QMessageBox.information(self, "Éxito", f"Ítem con ID {item_id} eliminado.")
                self.listar_items()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo eliminar el ítem: {e}")
        else:
            QMessageBox.warning(self, "Advertencia", "Seleccione un ítem para eliminar.")


if __name__ == "__main__":
    from PyQt6.QtWidgets import QApplication

    app = QApplication([])
    ventana = InventarioUI()
    ventana.show()
    app.exec()
