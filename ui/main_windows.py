from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from config import *
from ui.agenda_ui import AgendaUI
from ui.reparaciones_ui import ReparacionesUI
from ui.tareas_ui import TareasUI
from ui.inventario_ui import InventarioUI
from ui.objetivos_ui import ObjetivosUI
from ui.calendario_ui import CalendarioUI
from ui.plan_trabajo_ui import PlanTrabajoUI
from db_manager import DBManager


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gestión del Hogar")
        self.setGeometry(100, 100, 800, 600)

        # Instancia de DBManager
        self.db_manager = DBManager("app_data.db")
        
        # Cargar estilos desde un archivo QSS
        self.aplicar_estilo()

        # Layout principal
        layout = QVBoxLayout()

        # Botones para los módulos
        botones = [
            ("Agenda", self.abrir_agenda),
            ("Reparaciones", self.abrir_reparaciones),
            ("Lista de Tareas", self.abrir_lista_tareas),
            ("Inventario", self.abrir_inventario),
            ("Lista de Objetivos", self.abrir_lista_objetivos),
            ("Calendario", self.abrir_calendario),
            ("Plan de Trabajo", self.abrir_plan_trabajo),
        ]

        for texto, funcion in botones:
            boton = QPushButton(texto)
            boton.clicked.connect(funcion)
            layout.addWidget(boton)

        # Contenedor principal
        contenedor = QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)
        
    def aplicar_estilo(self):
        """Carga y aplica un archivo de estilo QSS."""
        try:
            with open("ui/style.qss", "r") as archivo_estilo:
                estilo = archivo_estilo.read()
                self.setStyleSheet(estilo)
        except FileNotFoundError:
            print("Archivo de estilo 'style.qss' no encontrado. Usando estilos predeterminados.")

    def abrir_agenda(self):
        """Abre la ventana del módulo Agenda."""
        self.ventana_agenda = AgendaUI(self.db_manager)
        self.ventana_agenda.show()

    def abrir_reparaciones(self):
        """Abre la ventana del módulo Reparaciones."""
        self.ventana_reparaciones = ReparacionesUI(self.db_manager)
        self.ventana_reparaciones.show()

    def abrir_lista_tareas(self):
        """Abre la ventana del módulo Lista de Tareas."""
        self.ventana_tareas = TareasUI(self.db_manager)
        self.ventana_tareas.show()

    def abrir_inventario(self):
        """Abre la ventana del módulo Inventario."""
        self.ventana_inventario = InventarioUI(self.db_manager)
        self.ventana_inventario.show()

    def abrir_lista_objetivos(self):
        """Abre la ventana del módulo Lista de Objetivos."""
        self.ventana_objetivos = ObjetivosUI(self.db_manager)
        self.ventana_objetivos.show()

    def abrir_calendario(self):
        """Abre la ventana del módulo Calendario."""
        self.ventana_calendario = CalendarioUI(self.db_manager)
        self.ventana_calendario.show()

    def abrir_plan_trabajo(self):
        """Abre la ventana del módulo Plan de Trabajo."""
        self.ventana_plan_trabajo = PlanTrabajoUI(self.db_manager)
        self.ventana_plan_trabajo.show()


if __name__ == "__main__":
    app = QApplication([])
    ventana_principal = MainWindow()
    ventana_principal.show()
    app.exec()
