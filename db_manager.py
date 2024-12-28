import sqlite3

class DBManager:
    def __init__(self, db_name="database/app_data.db"):
        self.db_name = db_name

    def initialize_database(self, schema_file="database/schema.sql"):
        """Crea la base de datos y las tablas usando un archivo SQL."""
        try:
            with sqlite3.connect(self.db_name) as conn:
                print("Conexión exitosa a la base de datos.")
                with open(schema_file, "r") as file:
                    conn.executescript(file.read())
                    print("Base de datos inicializada con éxito.")
        except Exception as e:
            print(f"Error al inicializar la base de datos: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    db_manager = DBManager()
    db_manager.initialize_database()
