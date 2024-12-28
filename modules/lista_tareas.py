import sqlite3
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from config import DB_NAME
from datetime import datetime

class ListaTareas:
    def agregar_tarea(self, titulo, descripcion, prioridad, fecha_hora):
        """Agrega una nueva tarea a la lista."""
        try:
            with sqlite3.connect(DB_NAME) as conn:
                conn.execute("""
                    INSERT INTO tareas (titulo, descripcion, prioridad, fecha_hora, estado)
                    VALUES (?, ?, ?, ?, ?)
                """, (titulo, descripcion, prioridad, fecha_hora, "Pendiente"))
                print(f"Tarea '{titulo}' agregada con éxito.")
        except Exception as e:
            print(f"Error al agregar la tarea: {e}")

    def listar_tareas(self, filtro_estado=None, filtro_prioridad=None):
        """Lista todas las tareas, filtrando por estado o prioridad si se especifica."""
        try:
            with sqlite3.connect(DB_NAME) as conn:
                query = "SELECT id, titulo, descripcion, prioridad, fecha_hora, estado FROM tareas"
                params = []
                if filtro_estado or filtro_prioridad:
                    query += " WHERE"
                    if filtro_estado:
                        query += " estado = ?"
                        params.append(filtro_estado)
                    if filtro_estado and filtro_prioridad:
                        query += " AND"
                    if filtro_prioridad:
                        query += " prioridad = ?"
                        params.append(filtro_prioridad)
                cursor = conn.execute(query, params)
                tareas = cursor.fetchall()

                if tareas:
                    print("\n--- Tareas Registradas ---")
                    for id, titulo, descripcion, prioridad, fecha_hora, estado in tareas:
                        fecha_str = fecha_hora if fecha_hora else "Sin Fecha"
                        print(f"{id}. {titulo} - {descripcion} (Prioridad: {prioridad}, Fecha: {fecha_str}, Estado: {estado})")
                else:
                    print("No hay tareas registradas.")
        except Exception as e:
            print(f"Error al listar las tareas: {e}")

    def actualizar_tarea(self, tarea_id, nuevo_titulo, nueva_descripcion, nueva_prioridad, nueva_fecha_hora, nuevo_estado):
        """Actualiza los detalles de una tarea existente."""
        try:
            with sqlite3.connect(DB_NAME) as conn:
                conn.execute("""
                    UPDATE tareas
                    SET titulo = ?, descripcion = ?, prioridad = ?, fecha_hora = ?, estado = ?
                    WHERE id = ?
                """, (nuevo_titulo, nueva_descripcion, nueva_prioridad, nueva_fecha_hora, nuevo_estado, tarea_id))
                print(f"Tarea con ID {tarea_id} actualizada con éxito.")
        except Exception as e:
            print(f"Error al actualizar la tarea: {e}")

    def eliminar_tarea(self, tarea_id):
        """Elimina una tarea por su ID."""
        try:
            with sqlite3.connect(DB_NAME) as conn:
                conn.execute("DELETE FROM tareas WHERE id = ?", (tarea_id,))
                print(f"Tarea con ID {tarea_id} eliminada con éxito.")
        except Exception as e:
            print(f"Error al eliminar la tarea: {e}")

# Prueba del módulo
if __name__ == "__main__":
    lista_tareas = ListaTareas()

    while True:
        print("\n=== Módulo Lista de Tareas ===")
        print("1. Agregar Tarea")
        print("2. Listar Tareas")
        print("3. Filtrar Tareas por Estado")
        print("4. Actualizar Tarea")
        print("5. Eliminar Tarea")
        print("6. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            descripcion = input("Descripción: ")
            prioridad = input("Prioridad (Alta, Media, Baja): ").capitalize()
            fecha_hora = input("Fecha y hora (formato YYYY-MM-DD HH:MM o 'sin fecha'): ")
            fecha_hora = fecha_hora if fecha_hora.lower() != "sin fecha" else None
            lista_tareas.agregar_tarea(titulo, descripcion, prioridad, fecha_hora)
        elif opcion == "2":
            lista_tareas.listar_tareas()
        elif opcion == "3":
            filtro_estado = input("Estado (Pendiente/En Progreso/Completada): ").capitalize()
            filtro_prioridad = input("Prioridad (Alta, Media, Baja o presiona Enter para omitir): ").capitalize()
            lista_tareas.listar_tareas(filtro_estado=filtro_estado, filtro_prioridad=filtro_prioridad if filtro_prioridad else None)
        elif opcion == "4":
            tarea_id = int(input("ID de la tarea a actualizar: "))
            nuevo_titulo = input("Nuevo Título: ")
            nueva_descripcion = input("Nueva Descripción: ")
            nueva_prioridad = input("Nueva Prioridad (Alta, Media, Baja): ").capitalize()
            nueva_fecha_hora = input("Nueva Fecha y hora (formato YYYY-MM-DD HH:MM o 'sin fecha'): ")
            nueva_fecha_hora = nueva_fecha_hora if nueva_fecha_hora.lower() != "sin fecha" else None
            nuevo_estado = input("Nuevo Estado (Pendiente/En Progreso/Completada): ").capitalize()
            lista_tareas.actualizar_tarea(tarea_id, nuevo_titulo, nueva_descripcion, nueva_prioridad, nueva_fecha_hora, nuevo_estado)
        elif opcion == "5":
            tarea_id = int(input("ID de la tarea a eliminar: "))
            lista_tareas.eliminar_tarea(tarea_id)
        elif opcion == "6":
            print("Saliendo del módulo Lista de Tareas...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")
