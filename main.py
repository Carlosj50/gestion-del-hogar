import sqlite3
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from config import *
def obtener_opciones():
    """Obtiene las opciones del menú desde la tabla opciones en la base de datos."""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.execute("SELECT clave, valor FROM opciones")
        opciones = cursor.fetchall()
        conn.close()
        return opciones
    except Exception as e:
        print(f"Error al obtener opciones: {e}")
        return []

def manejar_opcion(opcion):
    """Ejecuta directamente el módulo correspondiente según la opción seleccionada."""
    modulos = {
        1: MODULES_DIR + "reparaciones.py",
        2: MODULES_DIR + "agenda.py",
        3: MODULES_DIR + "lista_tareas.py",
        4: MODULES_DIR + "inventario.py",
        5: MODULES_DIR + "objetivos.py",
        6: MODULES_DIR + "plan_trabajo.py",
        7: MODULES_DIR + "calendario.py"
    }

    script = modulos.get(opcion)
    if script:
        os.system(f"python {script}")
    else:
        print("Opción no válida, intenta de nuevo.")

def mostrar_menu():
    """Muestra el menú principal y gestiona la navegación entre módulos."""
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
    mostrar_menu()
