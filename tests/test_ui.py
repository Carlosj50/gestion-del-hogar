import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from config import *
from PyQt6.QtWidgets import QApplication
from ui.agenda_ui import AgendaUI
from ui.reparaciones_ui import ReparacionesUI
from ui.tareas_ui import TareasUI
from ui.inventario_ui import InventarioUI
from ui.objetivos_ui import ObjetivosUI
from ui.calendario_ui import CalendarioUI
from ui.plan_trabajo_ui import PlanTrabajoUI

app = QApplication([])  # Necesario para las pruebas de PyQt6


class TestUI(unittest.TestCase):
    def test_agenda_ui(self):
        """Prueba que la ventana de Agenda se abra correctamente."""
        ventana = AgendaUI()
        self.assertIsNotNone(ventana, "La ventana de Agenda no se creó correctamente.")
        ventana.show()
        self.assertTrue(ventana.isVisible(), "La ventana de Agenda no es visible.")
        ventana.close()

    def test_reparaciones_ui(self):
        """Prueba que la ventana de Reparaciones se abra correctamente."""
        ventana = ReparacionesUI()
        self.assertIsNotNone(ventana, "La ventana de Reparaciones no se creó correctamente.")
        ventana.show()
        self.assertTrue(ventana.isVisible(), "La ventana de Reparaciones no es visible.")
        ventana.close()

    def test_tareas_ui(self):
        """Prueba que la ventana de Lista de Tareas se abra correctamente."""
        ventana = TareasUI()
        self.assertIsNotNone(ventana, "La ventana de Lista de Tareas no se creó correctamente.")
        ventana.show()
        self.assertTrue(ventana.isVisible(), "La ventana de Lista de Tareas no es visible.")
        ventana.close()

    def test_inventario_ui(self):
        """Prueba que la ventana de Inventario se abra correctamente."""
        ventana = InventarioUI()
        self.assertIsNotNone(ventana, "La ventana de Inventario no se creó correctamente.")
        ventana.show()
        self.assertTrue(ventana.isVisible(), "La ventana de Inventario no es visible.")
        ventana.close()

    def test_objetivos_ui(self):
        """Prueba que la ventana de Objetivos se abra correctamente."""
        ventana = ObjetivosUI()
        self.assertIsNotNone(ventana, "La ventana de Objetivos no se creó correctamente.")
        ventana.show()
        self.assertTrue(ventana.isVisible(), "La ventana de Objetivos no es visible.")
        ventana.close()

    def test_calendario_ui(self):
        """Prueba que la ventana de Calendario se abra correctamente."""
        ventana = CalendarioUI()
        self.assertIsNotNone(ventana, "La ventana de Calendario no se creó correctamente.")
        ventana.show()
        self.assertTrue(ventana.isVisible(), "La ventana de Calendario no es visible.")
        ventana.close()

    def test_plan_trabajo_ui(self):
        """Prueba que la ventana de Plan de Trabajo se abra correctamente."""
        ventana = PlanTrabajoUI()
        self.assertIsNotNone(ventana, "La ventana de Plan de Trabajo no se creó correctamente.")
        ventana.show()
        self.assertTrue(ventana.isVisible(), "La ventana de Plan de Trabajo no es visible.")
        ventana.close()


if __name__ == "__main__":
    unittest.main()
