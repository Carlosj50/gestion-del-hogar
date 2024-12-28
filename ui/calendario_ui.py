from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QLineEdit, QLabel, QHBoxLayout, QMessageBox
)
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from config import *
from modules.calendario import Calendario


class CalendarioUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gestión de Calendario")
        self.setGeometry(100, 100, 600, 400)

        # Instancia del módulo Calendario
        self.calendario = Calendario()

        # Layout principal
        layout = QVBoxLayout()

        # Tabla para mostrar eventos del calendario
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(3)
        self.tabla.setHorizontalHeaderLabels(["ID", "Evento", "Fecha y Hora"])
        layout.addWidget(self.tabla)

        # Botones de acciones
        botones_layout = QHBoxLayout()
        btn_agregar = QPushButton("Agregar Evento")
        btn_agregar.clicked.connect(self.agregar_evento)
        botones_layout.addWidget(btn_agregar)

        btn_listar = QPushButton("Listar Eventos")
        btn_listar.clicked.connect(self.listar_eventos)
        botones_layout.addWidget(btn_listar)

        btn_eliminar = QPushButton("Eliminar Evento")
        btn_eliminar.clicked.connect(self.eliminar_evento)
        botones_layout.addWidget(btn_eliminar)

        layout.addLayout(botones_layout)

        # Campos para agregar un evento
        self.campo_evento = QLineEdit()
        self.campo_evento.setPlaceholderText("Título del evento")
        layout.addWidget(self.campo_evento)

        self.campo_fecha_hora = QLineEdit()
        self.campo_fecha_hora.setPlaceholderText("Fecha y Hora (YYYY-MM-DD HH:MM)")
        layout.addWidget(self.campo_fecha_hora)

        self.setLayout(layout)

    def agregar_evento(self):
        """Agrega un nuevo evento al calendario."""
        evento = self.campo_evento.text()
        fecha_hora = self.campo_fecha_hora.text()

        if evento and fecha_hora:
            try:
                self.calendario.agregar_evento(evento, "", fecha_hora)
                QMessageBox.information(self, "Éxito", f"Evento '{evento}' agregado.")
                self.campo_evento.clear()
                self.campo_fecha_hora.clear()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo agregar el evento: {e}")
        else:
            QMessageBox.warning(self, "Advertencia", "Por favor, complete todos los campos.")

    def listar_eventos(self):
        """Muestra los eventos en la tabla."""
        try:
            eventos = self.calendario.listar_eventos()  # Método del módulo Calendario
            self.tabla.setRowCount(0)  # Limpia la tabla

            for fila, evento in enumerate(eventos):
                self.tabla.insertRow(fila)
                self.tabla.setItem(fila, 0, QTableWidgetItem(str(evento[0])))
                self.tabla.setItem(fila, 1, QTableWidgetItem(evento[1]))
                self.tabla.setItem(fila, 2, QTableWidgetItem(evento[3]))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudieron listar los eventos: {e}")

    def eliminar_evento(self):
        """Elimina un evento seleccionado."""
        fila_seleccionada = self.tabla.currentRow()
        if fila_seleccionada >= 0:
            evento_id = self.tabla.item(fila_seleccionada, 0).text()
            try:
                self.calendario.eliminar_evento(int(evento_id))
                QMessageBox.information(self, "Éxito", f"Evento con ID {evento_id} eliminado.")
                self.listar_eventos()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo eliminar el evento: {e}")
        else:
            QMessageBox.warning(self, "Advertencia", "Seleccione un evento para eliminar.")


if __name__ == "__main__":
    from PyQt6.QtWidgets import QApplication

    app = QApplication([])
    ventana = CalendarioUI()
    ventana.show()
    app.exec()
