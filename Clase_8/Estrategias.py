from enum import Enum

class Estrategia(Enum):
    OFENSIVA = 0
    DEFENSIVA = 1
    FINGIR = 2

def Ofensiva(robot, mapa):
    if mapa[robot.posicion[0]+1][robot.posicion[1]] == 'o':
        robot.mover("derecha")
        mapa[robot.posicion[0]+1][robot.posicion[1]] == 'o'
    else:
        robot.mover("derecha")

def Defensiva(robot, mapa):
    if mapa[robot.posicion[0]-1][robot.posicion[1]] == 'o':
        robot.mover("izquierda")
        mapa[robot.posicion[0]-1][robot.posicion[1]] == 'o'
    else:
        robot.mover("izquierda")

#def Fingir(robot, mapa):
