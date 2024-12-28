import unittest
import os
import sys
import sqlite3
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from config import *
from db_manager import DBManager
from modules.agenda import Agenda
from modules.reparaciones import Reparaciones
from modules.lista_tareas import ListaTareas
from modules.inventario import Inventario
from modules.objetivos import ListaObjetivos
from modules.calendario import Calendario
from modules.plan_trabajo import PlanTrabajo


class TestModules(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Configura una base de datos de prueba para todos los módulos."""
        cls.test_db = "test_modules.db"
        cls.db_manager = DBManager(cls.test_db)

        # Crear la tabla agenda si no existe
        cls.db_manager.execute_query("""
            CREATE TABLE IF NOT EXISTS agenda (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descripcion TEXT,
                fecha_hora TEXT NOT NULL
            )
        """)

        # Limpia la tabla agenda antes de las pruebas
        try:
            cls.db_manager.execute_query("DELETE FROM agenda")
        except sqlite3.OperationalError as e:
            print(f"Error al limpiar la tabla agenda: {e}")
            # Crear la tabla calendario si no existe
        cls.db_manager.execute_query("""
            CREATE TABLE IF NOT EXISTS calendario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                evento TEXT NOT NULL,
                descripcion TEXT,
                fecha_hora TEXT NOT NULL
            )
        """)

        # Limpia la tabla calendario antes de las pruebas
        try:
            cls.db_manager.execute_query("DELETE FROM calendario")
        except sqlite3.OperationalError as e:
            print(f"Error al limpiar la tabla calendario: {e}")
            # Crear la tabla reparaciones si no existe
        cls.db_manager.execute_query("""
            CREATE TABLE IF NOT EXISTS reparaciones (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descripcion TEXT NOT NULL,
                fecha TEXT NOT NULL,
                costo REAL NOT NULL,
                estado TEXT NOT NULL
            )
        """)

        # Limpia la tabla reparaciones antes de las pruebas
        try:
            cls.db_manager.execute_query("DELETE FROM reparaciones")
        except sqlite3.OperationalError as e:
            print(f"Error al limpiar la tabla reparaciones: {e}")
            # Crear la tabla tareas si no existe
        cls.db_manager.execute_query("""
            CREATE TABLE IF NOT EXISTS tareas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descripcion TEXT,
                prioridad TEXT,
                fecha_hora TEXT,
                estado TEXT
            )
        """)

        # Limpia la tabla tareas antes de las pruebas
        try:
            cls.db_manager.execute_query("DELETE FROM tareas")
        except sqlite3.OperationalError as e:
            print(f"Error al limpiar la tabla tareas: {e}")
        
            # Crear la tabla inventario si no existe
        cls.db_manager.execute_query("""
            CREATE TABLE IF NOT EXISTS inventario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item TEXT NOT NULL,
                cantidad INTEGER NOT NULL,
                ubicacion TEXT,
                fecha_caducidad TEXT
            )
        """)
    
        # Limpia la tabla inventario antes de las pruebas
        try:
            cls.db_manager.execute_query("DELETE FROM inventario")
        except sqlite3.OperationalError as e:
            print(f"Error al limpiar la tabla inventario: {e}")

        # Instanciar todos los módulos con la base de datos
        cls.agenda = Agenda(cls.db_manager)
        cls.reparaciones = Reparaciones(cls.db_manager)
        cls.lista_tareas = ListaTareas(cls.db_manager)
        cls.inventario = Inventario(cls.db_manager)
        cls.objetivos = ListaObjetivos(cls.db_manager)
        cls.calendario = Calendario(cls.db_manager)
        cls.plan_trabajo = PlanTrabajo(cls.db_manager)

    @classmethod
    def tearDownClass(cls):
        """Elimina la base de datos de prueba al finalizar las pruebas."""
        import os
        if cls.db_manager:
            del cls.db_manager
        if os.path.exists(cls.test_db):
            os.remove(cls.test_db)

    def test_agenda(self):
        """Prueba las operaciones CRUD del módulo Agenda."""
        # Limpia la tabla al inicio de la prueba
        self.db_manager.execute_query("DELETE FROM agenda")

        # Inserta un evento en la base de datos
        self.agenda.agregar_evento("Reunión", "Revisión de proyecto", "2024-12-30 10:00")

        # Lista los eventos y verifica que haya exactamente uno
        eventos = self.agenda.listar_eventos()
        self.assertEqual(len(eventos), 1)
        self.assertEqual(eventos[0][1], "Reunión")  # Verifica el título del evento

        # Elimina el evento y verifica que la tabla quede vacía
        self.agenda.eliminar_evento(eventos[0][0])
        eventos = self.agenda.listar_eventos()
        self.assertEqual(len(eventos), 0)


    def test_reparaciones(self):
        """Prueba las operaciones CRUD del módulo Reparaciones."""
        # Limpia la tabla al inicio de la prueba
        self.db_manager.execute_query("DELETE FROM reparaciones")

        # Inserta una reparación en la base de datos
        self.reparaciones.agregar_reparacion("Cambio de grifo", "2024-12-29", 50.0, "Pendiente")

        # Lista las reparaciones y verifica que haya exactamente una
        reparaciones = self.reparaciones.listar_reparaciones()
        self.assertEqual(len(reparaciones), 1)
        self.assertEqual(reparaciones[0][1], "Cambio de grifo")  # Verifica la descripción de la reparación

        # Elimina la reparación y verifica que la tabla quede vacía
        self.reparaciones.eliminar_reparacion(reparaciones[0][0])
        reparaciones = self.reparaciones.listar_reparaciones()
        self.assertEqual(len(reparaciones), 0)


    def test_lista_tareas(self):
        """Prueba las operaciones CRUD del módulo Lista de Tareas."""
        # Limpia la tabla al inicio de la prueba
        self.db_manager.execute_query("DELETE FROM tareas")

        # Inserta una tarea en la base de datos
        self.lista_tareas.agregar_tarea("Terminar informe", "Alta", "2024-12-28 18:00", "Pendiente")

        # Verifica que haya exactamente un registro en la tabla
        tareas = self.lista_tareas.listar_tareas()
        self.assertEqual(len(tareas), 1)
        self.assertEqual(tareas[0][1], "Terminar informe")

        # Elimina la tarea y verifica que la tabla quede vacía
        self.lista_tareas.eliminar_tarea(tareas[0][0])
        tareas = self.lista_tareas.listar_tareas()
        self.assertEqual(len(tareas), 0)

    def test_inventario(self):
        """Prueba las operaciones CRUD del módulo Inventario."""
        # Limpia la tabla al inicio de la prueba
        self.db_manager.execute_query("DELETE FROM inventario")

        # Inserta un ítem en la base de datos
        self.inventario.agregar_item("Leche", 3, "Refrigerador", "2024-12-31")

        # Lista los ítems y verifica que haya exactamente uno
        items = self.inventario.listar_items()
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0][1], "Leche")  # Verifica el nombre del ítem

        # Elimina el ítem y verifica que la tabla quede vacía
        self.inventario.eliminar_item(items[0][0])
        items = self.inventario.listar_items()
        self.assertEqual(len(items), 0)


    def test_objetivos(self):
        """Prueba las operaciones CRUD del módulo Objetivos."""
        self.objetivos.agregar_objetivo("Aprender Python", "Completar curso avanzado", "2024-12-31", 50)
        objetivos = self.objetivos.listar_objetivos()
        self.assertEqual(len(objetivos), 1)
        self.assertEqual(objetivos[0][1], "Aprender Python")

        self.objetivos.eliminar_objetivo(objetivos[0][0])
        objetivos = self.objetivos.listar_objetivos()
        self.assertEqual(len(objetivos), 0)

    def test_calendario(self):
        """Prueba las operaciones CRUD del módulo Calendario."""
        # Limpia la tabla al inicio de la prueba
        self.db_manager.execute_query("DELETE FROM calendario")

        # Inserta un evento en la base de datos
        self.calendario.agregar_evento("Cumpleaños", "Celebración en casa", "2024-12-30 20:00")

        # Lista los eventos y verifica que haya exactamente uno
        eventos = self.calendario.listar_eventos()
        self.assertEqual(len(eventos), 1)
        self.assertEqual(eventos[0][1], "Cumpleaños")  # Verifica el título del evento

        # Elimina el evento y verifica que la tabla quede vacía
        self.calendario.eliminar_evento(eventos[0][0])
        eventos = self.calendario.listar_eventos()
        self.assertEqual(len(eventos), 0)


    def test_plan_trabajo(self):
        """Prueba las operaciones CRUD del módulo Plan de Trabajo."""
        self.plan_trabajo.agregar_actividad("Planificar proyecto", "Organizar tareas iniciales", "2024-12-28 12:00")
        actividades = self.plan_trabajo.listar_actividades()
        self.assertEqual(len(actividades), 1)
        self.assertEqual(actividades[0][1], "Planificar proyecto")

        self.plan_trabajo.eliminar_actividad(actividades[0][0])
        actividades = self.plan_trabajo.listar_actividades()
        self.assertEqual(len(actividades), 0)


if __name__ == "__main__":
    unittest.main()
