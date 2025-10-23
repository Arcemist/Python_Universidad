import random
import time
import os
import Robot as Rob
import Estrategias as Est

# Tarea hecha por:
# Niver Arce
# David Lorenzo
# Mathias Campo

def clear_screen():
    """Clears the terminal screen."""
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

def crear_array_aleatorio(elementos_disponibles, cantidad):
    """Crea un array con elementos aleatorios con posible repetición"""
    return random.choices(elementos_disponibles, k=cantidad)

def generar_combinaciones_unicas(elementos_disponibles, tamaño_array, num_combinaciones):
    """Genera combinaciones únicas usando for loop"""
    combinaciones = set()

    # Intentar generar combinaciones hasta tener las suficientes
    for _ in range(num_combinaciones * 20):  # Suficientes intentos para garantizar unicidad
        nueva_combinacion = tuple(random.choices(elementos_disponibles, k=tamaño_array))
        combinaciones.add(nueva_combinacion)

        # Si ya tenemos suficientes combinaciones únicas, salir del loop
        if len(combinaciones) >= num_combinaciones:
            break

    # Convertir de vuelta a listas y tomar solo las que necesitamos
    return [list(combinacion) for combinacion in list(combinaciones)[:num_combinaciones]]

# Uso
elementos = [0, 1, 2, 3]

# Generar 6 combinaciones únicas de arrays de tamaño 3
combinaciones_unicas = generar_combinaciones_unicas(elementos, 3, 6)

posicion_pelota = [10,16]
posiciones = [[0,0],[4,4],[2,3],[6,3],[10,10],[15,10]]
mapa = []
for i in range(20):
    mapa.append([])
    for e in range(31):
        if [i,e] in posiciones:
            mapa[i].append(
                Rob.Robot(
                    combinaciones_unicas.pop(0),
                    e,
                    i,
                    random.choice(list(Est.Estrategia)).value
                )
            )
        elif [i,e] == posicion_pelota:
            mapa[i].append("o")
        else:
            mapa[i].append(0)

while True:
    for i in mapa:
        for e in i:
            if type(e) is Rob.Robot:
                e.actuar(mapa)

    clear_screen()
    for i in mapa:
        for e in i:
            if type(e) is Rob.Robot:
                print("X ", end="")
                e.descansar()
            else:
                print(f"{e} ", end="")
        print("")
    time.sleep(1)
