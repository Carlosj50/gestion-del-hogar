import sqlite3


class DBManager:
    def __init__(self, db_path):
        """Inicializa el gestor de base de datos."""
        self.db_path = db_path

    def execute_query(self, query, params=None):
        """Ejecuta consultas como INSERT, UPDATE, DELETE."""
        conn = sqlite3.connect(self.db_path)
        try:
            cursor = conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            conn.commit()
        finally:
            conn.close()

    def fetch_query(self, query, params=None):
        """Ejecuta consultas SELECT."""
        conn = sqlite3.connect(self.db_path)
        try:
            cursor = conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor.fetchall()
        finally:
            conn.close()
