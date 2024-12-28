from datetime import datetime

tareas = []

def agregar_tarea():
    print("\n--- Agregar Nueva Tarea ---")
    titulo = input("Título: ")
    descripcion = input("Descripción (opcional): ")
    prioridad = input("Prioridad (Alta, Media, Baja): ").capitalize()
    fecha = input("Fecha y hora (formato YYYY-MM-DD HH:MM) o 'sin fecha': ")

    if fecha.lower() != "sin fecha":
        try:
            fecha_hora = datetime.strptime(fecha, "%Y-%m-%d %H:%M")
        except ValueError:
            print("Formato de fecha/hora inválido.")
            return
    else:
        fecha_hora = None

    tarea = {
        "titulo": titulo,
        "descripcion": descripcion,
        "prioridad": prioridad,
        "fecha_hora": fecha_hora,
        "estado": "Pendiente"
    }
    tareas.append(tarea)
    print("Tarea agregada con éxito.")

def listar_tareas():
    print("\n--- Lista de Tareas ---")
    if not tareas:
        print("No hay tareas registradas.")
        return

    for i, tarea in enumerate(tareas, start=1):
        fecha_str = tarea["fecha_hora"].strftime("%Y-%m-%d %H:%M") if tarea["fecha_hora"] else "Sin Fecha"
        print(f"{i}. {tarea['titulo']} | {fecha_str} | Prioridad: {tarea['prioridad']} | Estado: {tarea['estado']}")

def marcar_tarea_realizada():
    listar_tareas()
    if not tareas:
        return

    try:
        numero = int(input("\nSelecciona el número de la tarea que has completado: "))
        if 1 <= numero <= len(tareas):
            tarea = tareas[numero - 1]
            tarea["estado"] = "Completada"
            print(f"Tarea '{tarea['titulo']}' marcada como completada.")
        else:
            print("Número de tarea inválido.")
    except ValueError:
        print("Por favor, introduce un número válido.")

def menu_tareas():
    while True:
        print("\n--- Menú de Lista de Tareas ---")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Marcar tarea como realizada")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            listar_tareas()
        elif opcion == "3":
            marcar_tarea_realizada()
        elif opcion == "4":
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción inválida, intenta nuevamente.")

menu_tareas()
