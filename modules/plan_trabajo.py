import sqlite3

class PlanTrabajo:
    def __init__(self, db_name="database/app_data.db"):
        self.db_name = db_name

    def agregar_actividad(self, titulo, descripcion, fecha_hora):
        """Agrega una nueva actividad al plan de trabajo."""
        try:
            with sqlite3.connect(self.db_name) as conn:
                conn.execute("""
                    INSERT INTO plan_trabajo (titulo, descripcion, fecha_hora)
                    VALUES (?, ?, ?)
                """, (titulo, descripcion, fecha_hora))
                print(f"Actividad '{titulo}' agregada con éxito.")
        except Exception as e:
            print(f"Error al agregar la actividad: {e}")

    def listar_actividades(self):
        """Lista todas las actividades del plan de trabajo."""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.execute("SELECT id, titulo, descripcion, fecha_hora FROM plan_trabajo")
                actividades = cursor.fetchall()
                if actividades:
                    print("\n--- Plan de Trabajo ---")
                    for id, titulo, descripcion, fecha_hora in actividades:
                        print(f"{id}. {titulo} - {descripcion} (Fecha y Hora: {fecha_hora})")
                else:
                    print("No hay actividades registradas en el plan de trabajo.")
        except Exception as e:
            print(f"Error al listar las actividades: {e}")

    def actualizar_actividad(self, actividad_id, nuevo_titulo, nueva_descripcion, nueva_fecha_hora):
        """Actualiza los detalles de una actividad existente."""
        try:
            with sqlite3.connect(self.db_name) as conn:
                conn.execute("""
                    UPDATE plan_trabajo
                    SET titulo = ?, descripcion = ?, fecha_hora = ?
                    WHERE id = ?
                """, (nuevo_titulo, nueva_descripcion, nueva_fecha_hora, actividad_id))
                print(f"Actividad con ID {actividad_id} actualizada con éxito.")
        except Exception as e:
            print(f"Error al actualizar la actividad: {e}")

    def eliminar_actividad(self, actividad_id):
        """Elimina una actividad del plan de trabajo."""
        try:
            with sqlite3.connect(self.db_name) as conn:
                conn.execute("DELETE FROM plan_trabajo WHERE id = ?", (actividad_id,))
                print(f"Actividad con ID {actividad_id} eliminada con éxito.")
        except Exception as e:
            print(f"Error al eliminar la actividad: {e}")

# Prueba del módulo
if __name__ == "__main__":
    plan_trabajo = PlanTrabajo()

    while True:
        print("\n=== Módulo Plan de Trabajo ===")
        print("1. Agregar Actividad")
        print("2. Listar Actividades")
        print("3. Actualizar Actividad")
        print("4. Eliminar Actividad")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            titulo = input("Título de la actividad: ")
            descripcion = input("Descripción: ")
            fecha_hora = input("Fecha y hora (formato YYYY-MM-DD HH:MM): ")
            plan_trabajo.agregar_actividad(titulo, descripcion, fecha_hora)
        elif opcion == "2":
            plan_trabajo.listar_actividades()
        elif opcion == "3":
            actividad_id = int(input("ID de la actividad a actualizar: "))
            nuevo_titulo = input("Nuevo título: ")
            nueva_descripcion = input("Nueva descripción: ")
            nueva_fecha_hora = input("Nueva fecha y hora (formato YYYY-MM-DD HH:MM): ")
            plan_trabajo.actualizar_actividad(actividad_id, nuevo_titulo, nueva_descripcion, nueva_fecha_hora)
        elif opcion == "4":
            actividad_id = int(input("ID de la actividad a eliminar: "))
            plan_trabajo.eliminar_actividad(actividad_id)
        elif opcion == "5":
            print("Saliendo del módulo Plan de Trabajo...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")
