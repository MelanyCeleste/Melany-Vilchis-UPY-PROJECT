import os
import logging

if not os.path.exists('logs'):
    os.makedirs('logs')

logging.basicConfig(
    filename='logs/app.log',
    level=logging.INFO,
    format='%(asctime)s — [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class ValortiempoError(Exception):
    pass

mapa_prioridad = {
    "alto": 3, 
    "medio": 2, 
    "bajo": 1
}
#contenedores vacios para almacenar las tareas y los tiempos
lista_tareas = []
duracion_break = 0
cantidad_breaks = 0
tiempo_breaks_total = 0
tiempo_total_necesario = 0

print(" SISTEMA DE PLANIFICACIÓN DE TAREAS ")
logging.info("El sistema de planificación de tareas WORKEFFI ha iniciado correctamente.")

# INPUT TIEMPO
while True:
    try:
        tiempo_disponible = float(input("Ingresa tu tiempo disponible para realizar todas tus tareas: "))
        if tiempo_disponible < 0:
            raise ValortiempoError("El tiempo no puede ser negativo.")
        break 
    except (ValueError, ValortiempoError) as e:
        print(f"Error: Ingresa un número válido. ({e})")
        logging.warning(f"Intento fallido de ingresar tiempo disponible: {e}")

unidad_disponible = input("¿En qué unidad está tu tiempo disponible? (min / hrs): ")
# Conversión de horas a minutos
if unidad_disponible == "hrs":
    tiempo_disponible = tiempo_disponible * 60

# BREAKS
quieres_breaks = input("¿Deseas incluir breaks entre tus tareas? (si / no): ").lower().strip()
if quieres_breaks == "si":
    while True:
        try:
            try:
                duracion_break = float(input("¿Cuánto tiempo durará cada break? (en min): "))
            except ValueError:
                raise ValueError("Debes ingresar un número válido en dígitos.")

            try:
                cantidad_breaks = int(input("¿Cuántos breaks deseas agregar?: "))
            except ValueError:
                raise ValueError("Debes ingresar un número entero en dígitos.")

            if duracion_break < 0 or cantidad_breaks < 0:
                raise ValortiempoError("El tiempo y la cantidad de breaks no pueden ser negativos.")

            break

        except (ValueError, ValortiempoError) as e:
            print(f"Error: {e}")
            logging.warning(f"Error en configuración de breaks: {e}")
# tiempo total de los breaks
tiempo_breaks_total = duracion_break * cantidad_breaks

agregando_tareas = "agregar"

while agregando_tareas == "agregar":
    print("\n-- Nueva Tarea --")
    nombre_tarea = input("Nombre de la tarea: ")
    
    while True:
        try:
            tiempo_tarea = float(input("Tiempo que tardarás en realizar la tarea: "))
            if tiempo_tarea < 0:
                raise ValortiempoError("El tiempo de la tarea no puede ser negativo")
            break
        except (ValueError, ValortiempoError) as e:
            print(f"Error de valor: Ingresa un número válido. ({e})")
            logging.warning(f"Error de validación de tiempo en tarea: {e}")
            
    unidad_tiempo = input("Unidad de tiempo de esta tarea (min / hrs): ")
    
    while True:
        try:
            nivel_prioridad = input("Nivel de prioridad (alto / medio / bajo): ").lower().strip()
            
            if nivel_prioridad not in mapa_prioridad:
                raise KeyError(f"La prioridad '{nivel_prioridad}' no es válida")
                
            puntaje_prioridad = mapa_prioridad[nivel_prioridad]
            break
        except KeyError as e:
            print(f"Error de clave: Por favor, escribe solo 'alto', 'medio' o 'bajo'")
            logging.warning(f"Intento de entrada de prioridad inválida: {nivel_prioridad}")
# Conversión de horas a minutos para la nueva tarea
    if unidad_tiempo == "hrs":
        tiempo_tarea = tiempo_tarea * 60

    nueva_tarea = {
        "nombre": nombre_tarea,
        "tiempo": tiempo_tarea,
        "nivel": nivel_prioridad,
        "puntaje": puntaje_prioridad,
        "estado": "activa",
    } 
# Agregar los datos de la nueva tarea a la lista principal    
    lista_tareas.append(nueva_tarea)
    logging.info(f"Tarea agregada exitosamente: '{nombre_tarea}' ({nivel_prioridad}, {tiempo_tarea} min)")

    agregando_tareas = input("\n¿Deseas 'agregar' otra tarea, 'modificar' la última o 'terminar'?: ").lower().strip()

    if agregando_tareas == "modificar":
        nombre_modificar = input("Escribe el nombre exacto de la tarea a modificar: ")
#buscar la tarea en la lista y actualizarla
        for tarea_actual in lista_tareas:
            if tarea_actual["nombre"] == nombre_modificar:
                while True:
                    try:
                        nuevo_tiempo = float(input("Ingresa el nuevo tiempo (en min): "))
                        if nuevo_tiempo < 0:
                            print("El tiempo no puede ser negativo.")
                            continue
                        old_time = tarea_actual["tiempo"]
                        tarea_actual["tiempo"] = nuevo_tiempo
                        print("¡Tiempo modificado con éxito!")
                        logging.info(f"Tarea '{nombre_modificar}' modificada. Tiempo cambió de {old_time} min a {nuevo_tiempo} min.")
                        break
                    except ValueError:
                        print("Error de valor: El tiempo debe ser un valor numérico.")
                        
        while True:
            # Volver a preguntar para que el ciclo no se rompa
            agregando_tareas = input("¿Deseas 'agregar' otra tarea o 'terminar'?: ").lower().strip()
            if agregando_tareas in ["agregar", "terminar"]:
                break
            else:
                print("Opción no válida. Escribe 'agregar' o 'terminar'.")
#ordenar la lista de tareas según prioridad y tiempo
cantidad_tareas = len(lista_tareas)

for i in range(cantidad_tareas):
    for j in range(0, cantidad_tareas - i - 1):
        tarea_actual = lista_tareas[j]
        tarea_siguiente = lista_tareas[j + 1]

        if tarea_actual["puntaje"] < tarea_siguiente["puntaje"]:
            lista_tareas[j] = tarea_siguiente
            lista_tareas[j + 1] = tarea_actual
        elif tarea_actual["puntaje"] == tarea_siguiente["puntaje"]:
            if tarea_actual["tiempo"] > tarea_siguiente["tiempo"]:
                lista_tareas[j] = tarea_siguiente
                lista_tareas[j + 1] = tarea_actual

tiempo_total_necesario = tiempo_breaks_total

for tarea in lista_tareas:
    tiempo_total_necesario = tiempo_total_necesario + tarea["tiempo"]

print("\n=====RESUMEN DE PLANIFICACIÓN=====")

if tiempo_total_necesario <= tiempo_disponible:
    print("¡ÉXITO! Sí puedes realizar todas tus tareas en tiempo y en orden")
    logging.info(f"Planificación exitosa. Tiempo total requerido: {tiempo_total_necesario} min de {tiempo_disponible} min disponibles")
else:
    tiempo_faltante = tiempo_total_necesario - tiempo_disponible
    print("ALERTA: Te faltan", tiempo_faltante, "minutos para poder realizar todo.")
    logging.info(f"Planificación con sobrecarga. Faltan {tiempo_faltante} min. ")
    
    tiempo_recuperado = 0
    #revisar desde la última tarea de la lista (las menos importantes)
    indice = cantidad_tareas - 1
    
    while tiempo_recuperado < tiempo_faltante and indice >= 0:
        tarea_a_posponer = lista_tareas[indice]
        tarea_a_posponer["estado"] = "pospuesta"
        tiempo_recuperado = tiempo_recuperado + tarea_a_posponer["tiempo"]
        
        print("-> Sugerencia: Posponer o eliminar la tarea '" + tarea_a_posponer["nombre"] + "' para recuperar", tarea_a_posponer["tiempo"], "minutos")
        logging.info(f"Tarea pospuesta por falta de tiempo: '{tarea_a_posponer['nombre']}'")
        indice = indice - 1

print("\n--- ORDEN FINAL ---")
#ddetectar y mostrar al usuario cuando hubo un empate en prioridad
for i in range(cantidad_tareas - 1):
    tarea_actual = lista_tareas[i]
    tarea_siguiente = lista_tareas[i + 1]
#solo mostrar el mensaje si ambas tareas siguen activas   
    if tarea_actual["estado"] == "activa" and tarea_siguiente["estado"] == "activa":
        if tarea_actual["puntaje"] == tarea_siguiente["puntaje"]:
            print("* NOTA: Las tareas '" + tarea_actual["nombre"] + "' y '" + tarea_siguiente["nombre"] + "' tienen la misma prioridad.")
            if tarea_actual["tiempo"] < tarea_siguiente["tiempo"]:
                print("  Se tomó primero '" + tarea_actual["nombre"] + "' porque toma menos tiempo de realizar (" + str(tarea_actual["tiempo"]) + " min).")
            else:
                print("  Ambas toman el mismo tiempo")
#lista final acomodada
for tarea in lista_tareas:
    if tarea["estado"] == "activa":
        print("[PROGRAMADA] " + tarea["nombre"] + " (" + str(tarea["tiempo"]) + " min)")
    else:
        print("[POSPUESTA]  " + tarea["nombre"] + " (No alcanzó el tiempo)")