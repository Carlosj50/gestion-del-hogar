import unittest
import sqlite3
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from config import *
from db_manager import DBManager


class TestDBManager(unittest.TestCase):
    def setUp(self):
        """Configuración inicial antes de cada prueba."""
        self.test_db = "test_database.db"
        self.db_manager = DBManager(self.test_db)

        # Crear una tabla de ejemplo para las pruebas
        with sqlite3.connect(self.test_db) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS ejemplo (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    descripcion TEXT
                )
            """)

    def tearDown(self):
        """Limpieza después de cada prueba."""
        import gc
        self.db_manager = None
    
        # Fuerza la recolección de basura para cerrar conexiones SQLite abiertas
        gc.collect()
    
        if os.path.exists(self.test_db):
            try:
                os.remove(self.test_db)
            except PermissionError as e:
                print(f"Error eliminando {self.test_db}: {e}")
    def test_insert_data(self):
        """Prueba la inserción de datos."""
        query = "INSERT INTO ejemplo (nombre, descripcion) VALUES (?, ?)"
        self.db_manager.execute_query(query, ("Prueba", "Descripción de prueba"))

        # Verificar que los datos se insertaron correctamente
        query = "SELECT * FROM ejemplo WHERE nombre = ?"
        result = self.db_manager.fetch_query(query, ("Prueba",))
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][1], "Prueba")

    def test_update_data(self):
        """Prueba la actualización de datos."""
        # Insertar un registro para actualizar
        query = "INSERT INTO ejemplo (nombre, descripcion) VALUES (?, ?)"
        self.db_manager.execute_query(query, ("Prueba", "Descripción inicial"))

        # Actualizar el registro
        update_query = "UPDATE ejemplo SET descripcion = ? WHERE nombre = ?"
        self.db_manager.execute_query(update_query, ("Descripción actualizada", "Prueba"))

        # Verificar la actualización
        query = "SELECT descripcion FROM ejemplo WHERE nombre = ?"
        result = self.db_manager.fetch_query(query, ("Prueba",))
        self.assertEqual(result[0][0], "Descripción actualizada")

    def test_delete_data(self):
        """Prueba la eliminación de datos."""
        # Insertar un registro para eliminar
        query = "INSERT INTO ejemplo (nombre, descripcion) VALUES (?, ?)"
        self.db_manager.execute_query(query, ("Prueba", "Descripción para eliminar"))

        # Eliminar el registro
        delete_query = "DELETE FROM ejemplo WHERE nombre = ?"
        self.db_manager.execute_query(delete_query, ("Prueba",))

        # Verificar que el registro fue eliminado
        query = "SELECT * FROM ejemplo WHERE nombre = ?"
        result = self.db_manager.fetch_query(query, ("Prueba",))
        self.assertEqual(len(result), 0)

    def test_fetch_data(self):
        """Prueba la recuperación de datos."""
        # Insertar múltiples registros
        query = "INSERT INTO ejemplo (nombre, descripcion) VALUES (?, ?)"
        self.db_manager.execute_query(query, ("Prueba1", "Descripción 1"))
        self.db_manager.execute_query(query, ("Prueba2", "Descripción 2"))

        # Recuperar todos los registros
        fetch_query = "SELECT * FROM ejemplo"
        result = self.db_manager.fetch_query(fetch_query)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0][1], "Prueba1")
        self.assertEqual(result[1][1], "Prueba2")

    def test_table_creation(self):
        """Prueba la creación de una tabla."""
        table_query = """
            CREATE TABLE IF NOT EXISTS nueva_tabla (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                dato TEXT NOT NULL
            )
        """
        self.db_manager.execute_query(table_query)

        # Verificar que la tabla existe
        query = "SELECT name FROM sqlite_master WHERE type='table' AND name='nueva_tabla'"
        result = self.db_manager.fetch_query(query)
        self.assertEqual(len(result), 1)


if __name__ == "__main__":
    unittest.main()
