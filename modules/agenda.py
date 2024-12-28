import sqlite3
from datetime import datetime

class Agenda:
    def __init__(self, db_name="database/app_data.db"):
        self.db_name = db_name

    def agregar_evento(self, evento, descripcion, fecha_hora):
        """Agrega un nuevo evento al calendario."""
        try:
            with sqlite3.connect(self.db_name) as conn:
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
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.execute("SELECT id, evento, descripcion, fecha_hora FROM calendario")
                eventos = cursor.fetchall()
                if eventos:
                    print("\n--- Eventos Registrados ---")
                    for id, evento, descripcion, fecha_hora in eventos:
                        print(f"{id}. {evento} - {descripcion} (Fecha y Hora: {fecha_hora})")
                else:
                    print("No hay eventos registrados.")
        except Exception as e:
            print(f"Error al listar eventos: {e}")

    def actualizar_evento(self, evento_id, nuevo_evento, nueva_descripcion, nueva_fecha_hora):
        """Actualiza un evento existente."""
        try:
            with sqlite3.connect(self.db_name) as conn:
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
            with sqlite3.connect(self.db_name) as conn:
                conn.execute("DELETE FROM calendario WHERE id = ?", (evento_id,))
                print(f"Evento con ID {evento_id} eliminado con éxito.")
        except Exception as e:
            print(f"Error al eliminar el evento: {e}")

# Prueba del módulo
if __name__ == "__main__":
    agenda = Agenda()

    while True:
        print("\n=== Módulo Agenda ===")
        print("1. Agregar Evento")
        print("2. Listar Eventos")
        print("3. Actualizar Evento")
        print("4. Eliminar Evento")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            evento = input("Nombre del evento: ")
            descripcion = input("Descripción: ")
            fecha_hora = input("Fecha y hora (formato YYYY-MM-DD HH:MM): ")
            agenda.agregar_evento(evento, descripcion, fecha_hora)
        elif opcion == "2":
            agenda.listar_eventos()
        elif opcion == "3":
            evento_id = int(input("ID del evento a actualizar: "))
            nuevo_evento = input("Nuevo nombre del evento: ")
            nueva_descripcion = input("Nueva descripción: ")
            nueva_fecha_hora = input("Nueva fecha y hora (formato YYYY-MM-DD HH:MM): ")
            agenda.actualizar_evento(evento_id, nuevo_evento, nueva_descripcion, nueva_fecha_hora)
        elif opcion == "4":
            evento_id = int(input("ID del evento a eliminar: "))
            agenda.eliminar_evento(evento_id)
        elif opcion == "5":
            print("Saliendo del módulo Agenda...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")
