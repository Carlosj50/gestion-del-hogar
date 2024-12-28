import sqlite3
from db_manager import DBManager

def obtener_opciones():
    """Obtiene las opciones del menú desde la base de datos."""
    try:
        conn = sqlite3.connect("database/app_data.db")
        cursor = conn.execute("SELECT clave, valor FROM opciones")
        opciones = cursor.fetchall()
        conn.close()
        return opciones
    except Exception as e:
        print(f"Error al obtener opciones: {e}")
        return []

def manejar_opcion(opcion):
    """Llama al módulo correspondiente según la opción seleccionada."""
    if opcion == 1:
        print("Reparaciones - Funcionalidad en desarrollo")
        # Aquí se importará y ejecutará el módulo reparaciones
    elif opcion == 2:
        print("Agenda - Funcionalidad en desarrollo")
        # Aquí se importará y ejecutará el módulo agenda
    elif opcion == 3:
        print("Lista de Tareas - Funcionalidad en desarrollo")
        # Aquí se importará y ejecutará el módulo lista_tareas
    elif opcion == 4:
        print("Inventario - Funcionalidad en desarrollo")
        # Aquí se importará y ejecutará el módulo inventario
    elif opcion == 5:
        print("Lista de Objetivos - Funcionalidad en desarrollo")
        # Aquí se importará y ejecutará el módulo objetivos
    elif opcion == 6:
        print("Plan de Trabajo - Funcionalidad en desarrollo")
        # Aquí se importará y ejecutará el módulo plan_trabajo
    elif opcion == 7:
        print("Calendario - Funcionalidad en desarrollo")
        # Aquí se importará y ejecutará el módulo calendario
    else:
        print("Opción no válida, por favor intenta de nuevo.")

def mostrar_menu():
    """Muestra el menú principal y gestiona la selección del usuario."""
    while True:
        print("\n=== Menú Principal ===")
        opciones = obtener_opciones()
        if not opciones:
            print("No hay opciones disponibles en la base de datos.")
            break

        for clave, valor in opciones:
            print(f"{clave}. {valor}")
        print("0. Salir")

        try:
            opcion = int(input("Selecciona una opción: "))
            if opcion == 0:
                print("¡Hasta luego!")
                break
            manejar_opcion(opcion)
        except ValueError:
            print("Por favor, introduce un número válido.")

if __name__ == "__main__":
    # Inicializamos la conexión a la base de datos y mostramos el menú
    db_manager = DBManager()
    mostrar_menu()
