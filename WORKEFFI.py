mapa_prioridad = {
    "alto": 3, 
    "medio": 2, 
    "bajo": 1
}

lista_tareas = []
tiempo_breaks_total = 0
tiempo_total_necesario = 0

print(" SISTEMA DE PLANIFICACIÓN DE TAREAS ")


# INPUT TIEMPO

tiempo_disponible = float(input("Ingresa tu tiempo disponible para realizar todas tus tareas: "))
unidad_disponible = input("¿En qué unidad está tu tiempo disponible? (min / hrs): ")

# Conversión de horas a minutos 
if unidad_disponible == "hrs":
    tiempo_disponible = tiempo_disponible * 60

# breaks
quiere_breaks = input("¿Deseas incluir breaks entre tus tareas? (si / no): ")
if quiere_breaks == "si":
    duracion_break = float(input("¿Cuánto tiempo durará cada break? (en min): "))
    cantidad_breaks = int(input("¿Cuántos breaks deseas agregar?: "))
    # tiempo total de los breaks
    tiempo_breaks_total = duracion_break * cantidad_breaks

agregando_tareas = "agregar"

while agregando_tareas == "agregar":
    print("\n-- Nueva Tarea --")
    nombre_tarea = input("Nombre de la tarea: ")
    tiempo_tarea = float(input("Tiempo que tardarás en realizar la tarea: "))
    unidad_tiempo = input("Unidad de tiempo de esta tarea (min / hrs): ")
    nivel_prioridad = input("Nivel de prioridad (alto / medio / bajo): ")

    # Conversión de horas a minutos para la nueva tarea
    if unidad_tiempo == "hrs":
        tiempo_tarea = tiempo_tarea * 60

    nueva_tarea = {
        "nombre": nombre_tarea,
        "tiempo": tiempo_tarea,
        "nivel": nivel_prioridad,
        "puntaje": mapa_prioridad[nivel_prioridad],
    } 