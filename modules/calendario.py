import sqlite3
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from config import DB_NAME

class Calendario:
    def __init__(self, db_manager):
        """Inicializa la clase Agenda con una referencia al DBManager."""
        self.db_manager = db_manager
    def agregar_evento(self, evento, descripcion, fecha_hora):
        """Agrega un nuevo evento al calendario."""
        try:
            with sqlite3.connect(DB_NAME) as conn:
                conn.execute("""
                    INSERT INTO calendario (evento, descripcion, fecha_hora)
                    VALUES (?, ?, ?)
                """, (evento, descripcion, fecha_hora))
                print(f"Evento '{evento}' agregado con éxito.")
        except Exception as e:
            print(f"Error al agregar el evento: {e}")

    def listar_eventos(self):
        """Lista todos los eventos registrados en el calendario."""
        try:
            with sqlite3.connect(DB_NAME) as conn:
                cursor = conn.execute("SELECT id, evento, descripcion, fecha_hora FROM calendario")
                eventos = cursor.fetchall()  # Recupera todos los registros
                return eventos  # Devuelve la lista de eventos
        except Exception as e:
            print(f"Error al listar eventos: {e}")
            return []  # Devuelve una lista vacía en caso de error
    
    
    def actualizar_evento(self, evento_id, nuevo_evento, nueva_descripcion, nueva_fecha_hora):
        """Actualiza los detalles de un evento existente."""
        try:
            with sqlite3.connect(DB_NAME) as conn:
                conn.execute("""
                    UPDATE calendario
                    SET evento = ?, descripcion = ?, fecha_hora = ?
                    WHERE id = ?
                """, (nuevo_evento, nueva_descripcion, nueva_fecha_hora, evento_id))
                print(f"Evento con ID {evento_id} actualizado con éxito.")
        except Exception as e:
            print(f"Error al actualizar el evento: {e}")

    def eliminar_evento(self, evento_id):
        """Elimina un evento del calendario."""
        try:
            with sqlite3.connect(DB_NAME) as conn:
                conn.execute("DELETE FROM calendario WHERE id = ?", (evento_id,))
                print(f"Evento con ID {evento_id} eliminado con éxito.")
        except Exception as e:
            print(f"Error al eliminar el evento: {e}")

# Prueba del módulo
if __name__ == "__main__":
    calendario = Calendario()

    while True:
        print("\n=== Módulo Calendario ===")
        print("1. Agregar Evento")
        print("2. Listar Eventos")
        print("3. Actualizar Evento")
        print("4. Eliminar Evento")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            evento = input("Título del evento: ")
            descripcion = input("Descripción: ")
            fecha_hora = input("Fecha y hora (formato YYYY-MM-DD HH:MM): ")
            calendario.agregar_evento(evento, descripcion, fecha_hora)
        elif opcion == "2":
            calendario.listar_eventos()
        elif opcion == "3":
            evento_id = int(input("ID del evento a actualizar: "))
            nuevo_evento = input("Nuevo título del evento: ")
            nueva_descripcion = input("Nueva descripción: ")
            nueva_fecha_hora = input("Nueva fecha y hora (formato YYYY-MM-DD HH:MM): ")
            calendario.actualizar_evento(evento_id, nuevo_evento, nueva_descripcion, nueva_fecha_hora)
        elif opcion == "4":
            evento_id = int(input("ID del evento a eliminar: "))
            calendario.eliminar_evento(evento_id)
        elif opcion == "5":
            print("Saliendo del módulo Calendario...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")
