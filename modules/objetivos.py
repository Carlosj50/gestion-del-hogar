import sqlite3
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from config import DB_NAME
class ListaObjetivos:
    def __init__(self, db_manager):
        """Inicializa la clase Agenda con una referencia al DBManager."""
        self.db_manager = db_manager
    def agregar_objetivo(self, objetivo, descripcion, fecha_limite, progreso):
        """Agrega un nuevo objetivo a la lista."""
        try:
            with sqlite3.connect(DB_NAME) as conn:
                conn.execute("""
                    INSERT INTO objetivos (objetivo, descripcion, fecha_limite, progreso)
                    VALUES (?, ?, ?, ?)
                """, (objetivo, descripcion, fecha_limite, progreso))
                print(f"Objetivo '{objetivo}' agregado con éxito.")
        except Exception as e:
            print(f"Error al agregar el objetivo: {e}")

    def listar_objetivos(self):
        """
        Lista todos los objetivos registrados y los devuelve como una lista.
        """
        try:
            with sqlite3.connect(DB_NAME) as conn:
                cursor = conn.execute("SELECT id, objetivo, descripcion, fecha_limite, progreso FROM objetivos")
                objetivos = cursor.fetchall()  # Recupera todos los registros de la tabla
                return objetivos  # Devuelve la lista de objetivos
        except Exception as e:
            print(f"Error al listar los objetivos: {e}")
            return []  # Devuelve una lista vacía en caso de error

    def actualizar_objetivo(self, objetivo_id, nuevo_objetivo, nueva_descripcion, nueva_fecha_limite, nuevo_progreso):
        """Actualiza los detalles de un objetivo existente."""
        try:
            with sqlite3.connect(DB_NAME) as conn:
                conn.execute("""
                    UPDATE objetivos
                    SET objetivo = ?, descripcion = ?, fecha_limite = ?, progreso = ?
                    WHERE id = ?
                """, (nuevo_objetivo, nueva_descripcion, nueva_fecha_limite, nuevo_progreso, objetivo_id))
                print(f"Objetivo con ID {objetivo_id} actualizado con éxito.")
        except Exception as e:
            print(f"Error al actualizar el objetivo: {e}")

    def eliminar_objetivo(self, objetivo_id):
        """Elimina un objetivo de la lista."""
        try:
            with sqlite3.connect(DB_NAME) as conn:
                conn.execute("DELETE FROM objetivos WHERE id = ?", (objetivo_id,))
                print(f"Objetivo con ID {objetivo_id} eliminado con éxito.")
        except Exception as e:
            print(f"Error al eliminar el objetivo: {e}")

# Prueba del módulo
if __name__ == "__main__":
    lista_objetivos = ListaObjetivos()

    while True:
        print("\n=== Módulo Lista de Objetivos ===")
        print("1. Agregar Objetivo")
        print("2. Listar Objetivos")
        print("3. Actualizar Objetivo")
        print("4. Eliminar Objetivo")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            objetivo = input("Nombre del objetivo: ")
            descripcion = input("Descripción: ")
            fecha_limite = input("Fecha límite (YYYY-MM-DD): ")
            progreso = int(input("Progreso inicial (0-100%): "))
            lista_objetivos.agregar_objetivo(objetivo, descripcion, fecha_limite, progreso)
        elif opcion == "2":
            lista_objetivos.listar_objetivos()
        elif opcion == "3":
            objetivo_id = int(input("ID del objetivo a actualizar: "))
            nuevo_objetivo = input("Nuevo nombre del objetivo: ")
            nueva_descripcion = input("Nueva descripción: ")
            nueva_fecha_limite = input("Nueva fecha límite (YYYY-MM-DD): ")
            nuevo_progreso = int(input("Nuevo progreso (0-100%): "))
            lista_objetivos.actualizar_objetivo(objetivo_id, nuevo_objetivo, nueva_descripcion, nueva_fecha_limite, nuevo_progreso)
        elif opcion == "4":
            objetivo_id = int(input("ID del objetivo a eliminar: "))
            lista_objetivos.eliminar_objetivo(objetivo_id)
        elif opcion == "5":
            print("Saliendo del módulo Lista de Objetivos...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")
