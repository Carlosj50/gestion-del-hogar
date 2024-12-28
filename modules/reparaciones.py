import sqlite3
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from config import DB_NAME
class Reparaciones:
    def __init__(self, db_name="database/app_data.db"):
        self.db_name = db_name

    def agregar_reparacion(self, descripcion, fecha, costo, estado):
        """Agrega una nueva reparación."""
        try:
            with sqlite3.connect(DB_NAME) as conn:
                conn.execute("""
                    INSERT INTO reparaciones (descripcion, fecha, costo, estado)
                    VALUES (?, ?, ?, ?)
                """, (descripcion, fecha, costo, estado))
                print(f"Reparación '{descripcion}' agregada con éxito.")
        except Exception as e:
            print(f"Error al agregar la reparación: {e}")

    def listar_reparaciones(self):
        """Lista todas las reparaciones."""
        try:
            with sqlite3.connect(DB_NAME) as conn:
                cursor = conn.execute("SELECT id, descripcion, fecha, costo, estado FROM reparaciones")
                reparaciones = cursor.fetchall()
                if reparaciones:
                    print("\n--- Reparaciones Registradas ---")
                    for id, descripcion, fecha, costo, estado in reparaciones:
                        print(f"{id}. {descripcion} - Fecha: {fecha}, Costo: {costo}, Estado: {estado}")
                else:
                    print("No hay reparaciones registradas.")
        except Exception as e:
            print(f"Error al listar reparaciones: {e}")

    def actualizar_reparacion(self, reparacion_id, nueva_descripcion, nueva_fecha, nuevo_costo, nuevo_estado):
        """Actualiza una reparación existente."""
        try:
            with sqlite3.connect(DB_NAME) as conn:
                conn.execute("""
                    UPDATE reparaciones
                    SET descripcion = ?, fecha = ?, costo = ?, estado = ?
                    WHERE id = ?
                """, (nueva_descripcion, nueva_fecha, nuevo_costo, nuevo_estado, reparacion_id))
                print(f"Reparación con ID {reparacion_id} actualizada con éxito.")
        except Exception as e:
            print(f"Error al actualizar la reparación: {e}")

    def eliminar_reparacion(self, reparacion_id):
        """Elimina una reparación."""
        try:
            with sqlite3.connect(DB_NAME) as conn:
                conn.execute("DELETE FROM reparaciones WHERE id = ?", (reparacion_id,))
                print(f"Reparación con ID {reparacion_id} eliminada con éxito.")
        except Exception as e:
            print(f"Error al eliminar la reparación: {e}")

# Prueba del módulo
if __name__ == "__main__":
    reparaciones = Reparaciones()

    while True:
        print("\n=== Módulo Reparaciones ===")
        print("1. Agregar Reparación")
        print("2. Listar Reparaciones")
        print("3. Actualizar Reparación")
        print("4. Eliminar Reparación")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            descripcion = input("Descripción: ")
            fecha = input("Fecha (YYYY-MM-DD): ")
            costo = float(input("Costo: "))
            estado = input("Estado (Pendiente/Completada): ")
            reparaciones.agregar_reparacion(descripcion, fecha, costo, estado)
        elif opcion == "2":
            reparaciones.listar_reparaciones()
        elif opcion == "3":
            reparacion_id = int(input("ID de la reparación a actualizar: "))
            nueva_descripcion = input("Nueva descripción: ")
            nueva_fecha = input("Nueva fecha (YYYY-MM-DD): ")
            nuevo_costo = float(input("Nuevo costo: "))
            nuevo_estado = input("Nuevo estado (Pendiente/Completada): ")
            reparaciones.actualizar_reparacion(reparacion_id, nueva_descripcion, nueva_fecha, nuevo_costo, nuevo_estado)
        elif opcion == "4":
            reparacion_id = int(input("ID de la reparación a eliminar: "))
            reparaciones.eliminar_reparacion(reparacion_id)
        elif opcion == "5":
            print("Saliendo del módulo Reparaciones...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")
