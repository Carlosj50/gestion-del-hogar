import sqlite3
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from config import DB_NAME
class Inventario:
    def agregar_item(self, item, cantidad, ubicacion, fecha_caducidad):
        """Agrega un nuevo ítem al inventario."""
        try:
            with sqlite3.connect(DB_NAME) as conn:
                conn.execute("""
                    INSERT INTO inventario (item, cantidad, ubicacion, fecha_caducidad)
                    VALUES (?, ?, ?, ?)
                """, (item, cantidad, ubicacion, fecha_caducidad))
                print(f"Ítem '{item}' agregado con éxito.")
        except Exception as e:
            print(f"Error al agregar el ítem: {e}")

    def listar_items(self):
        """Lista todos los ítems en el inventario."""
        try:
            with sqlite3.connect(DB_NAME) as conn:
                cursor = conn.execute("SELECT id, item, cantidad, ubicacion, fecha_caducidad FROM inventario")
                items = cursor.fetchall()
                if items:
                    print("\n--- Inventario Registrado ---")
                    for id, item, cantidad, ubicacion, fecha_caducidad in items:
                        fecha_str = fecha_caducidad if fecha_caducidad else "Sin Fecha"
                        print(f"{id}. {item} - Cantidad: {cantidad}, Ubicación: {ubicacion}, Caducidad: {fecha_str}")
                else:
                    print("No hay ítems registrados en el inventario.")
        except Exception as e:
            print(f"Error al listar los ítems: {e}")

    def actualizar_item(self, item_id, nuevo_item, nueva_cantidad, nueva_ubicacion, nueva_fecha_caducidad):
        """Actualiza los detalles de un ítem existente."""
        try:
            with sqlite3.connect(DB_NAME) as conn:
                conn.execute("""
                    UPDATE inventario
                    SET item = ?, cantidad = ?, ubicacion = ?, fecha_caducidad = ?
                    WHERE id = ?
                """, (nuevo_item, nueva_cantidad, nueva_ubicacion, nueva_fecha_caducidad, item_id))
                print(f"Ítem con ID {item_id} actualizado con éxito.")
        except Exception as e:
            print(f"Error al actualizar el ítem: {e}")

    def eliminar_item(self, item_id):
        """Elimina un ítem del inventario."""
        try:
            with sqlite3.connect(DB_NAME) as conn:
                conn.execute("DELETE FROM inventario WHERE id = ?", (item_id,))
                print(f"Ítem con ID {item_id} eliminado con éxito.")
        except Exception as e:
            print(f"Error al eliminar el ítem: {e}")

# Prueba del módulo
if __name__ == "__main__":
    inventario = Inventario()

    while True:
        print("\n=== Módulo Inventario ===")
        print("1. Agregar Ítem")
        print("2. Listar Ítems")
        print("3. Actualizar Ítem")
        print("4. Eliminar Ítem")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            item = input("Nombre del ítem: ")
            cantidad = int(input("Cantidad: "))
            ubicacion = input("Ubicación: ")
            fecha_caducidad = input("Fecha de caducidad (YYYY-MM-DD o 'sin fecha'): ")
            fecha_caducidad = fecha_caducidad if fecha_caducidad.lower() != "sin fecha" else None
            inventario.agregar_item(item, cantidad, ubicacion, fecha_caducidad)
        elif opcion == "2":
            inventario.listar_items()
        elif opcion == "3":
            item_id = int(input("ID del ítem a actualizar: "))
            nuevo_item = input("Nuevo nombre del ítem: ")
            nueva_cantidad = int(input("Nueva cantidad: "))
            nueva_ubicacion = input("Nueva ubicación: ")
            nueva_fecha_caducidad = input("Nueva fecha de caducidad (YYYY-MM-DD o 'sin fecha'): ")
            nueva_fecha_caducidad = nueva_fecha_caducidad if nueva_fecha_caducidad.lower() != "sin fecha" else None
            inventario.actualizar_item(item_id, nuevo_item, nueva_cantidad, nueva_ubicacion, nueva_fecha_caducidad)
        elif opcion == "4":
            item_id = int(input("ID del ítem a eliminar: "))
            inventario.eliminar_item(item_id)
        elif opcion == "5":
            print("Saliendo del módulo Inventario...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")
