import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from config import *
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from ui.agenda_ui import AgendaUI
from ui.reparaciones_ui import ReparacionesUI
from ui.tareas_ui import TareasUI
from ui.inventario_ui import InventarioUI
from ui.objetivos_ui import ObjetivosUI
from ui.calendario_ui import CalendarioUI
from ui.plan_trabajo_ui import PlanTrabajoUI



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gestión del Hogar")
        self.setGeometry(100, 100, 800, 600)
        with open(UI_DIR + "style.qss", "r") as style_file:
            app.setStyleSheet(style_file.read())
        # Layout principal
        layout = QVBoxLayout()

        # Botones para los módulos
        botones = [
            ("Reparaciones", self.abrir_reparaciones),
            ("Agenda", self.abrir_agenda),
            ("Lista de Tareas", self.abrir_lista_tareas),
            ("Inventario", self.abrir_inventario),
            ("Lista de Objetivos", self.abrir_lista_objetivos),
            ("Plan de Trabajo", self.abrir_plan_trabajo),
            ("Calendario", self.abrir_calendario),
        ]

        for texto, funcion in botones:
            boton = QPushButton(texto)
            boton.clicked.connect(funcion)
            layout.addWidget(boton)

        # Contenedor principal
        contenedor = QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

    # Métodos para abrir las ventanas de los módulos
    def abrir_agenda(self):
        self.ventana_agenda = AgendaUI()
        self.ventana_agenda.show()

    def abrir_reparaciones(self):
        self.ventana_reparaciones = ReparacionesUI()
        self.ventana_reparaciones.show()

    def abrir_lista_tareas(self):
        self.ventana_tareas = TareasUI()
        self.ventana_tareas.show()

    def abrir_inventario(self):
        self.ventana_inventario = InventarioUI()
        self.ventana_inventario.show()

    def abrir_lista_objetivos(self):
        self.ventana_objetivos = ObjetivosUI()
        self.ventana_objetivos.show()

    def abrir_calendario(self):
        self.ventana_calendario = CalendarioUI()
        self.ventana_calendario.show()
    def abrir_plan_trabajo(self):
        self.ventana_plan_trabajo = PlanTrabajoUI()
        self.ventana_plan_trabajo.show()

if __name__ == "__main__":
    app = QApplication([])
    ventana_principal = MainWindow()
    ventana_principal.show()
    app.exec()
