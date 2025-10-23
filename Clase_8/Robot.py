import Estrategias

class Robot:
    def __init__(self, robot_id, x, y, estrategia):
        self.robot_id = robot_id
        self.posicion = [x, y]
        self.estrategia = estrategia

        self.actuo = False

        # Límites del mapa
        self.max_x = 30
        self.max_y = 19


    def mover(self, direccion):
        """
        Mueve al robot una casilla en la dirección indicada.
        No permite salir de los límites del mapa.
        direccion: 'arriba', 'abajo', 'izquierda', 'derecha'
        """
        if direccion == "izquierda" and self.posicion[1] > 1:
            self.posicion[1] -= 1
        elif direccion == "derecha" and self.posicion[1] < self.max_x:
            self.posicion[1] += 1
        elif direccion == "abajo" and self.posicion[0] < self.max_y:
            self.posicion[0] += 1
        elif direccion == "arriba" and self.posicion[0] > 1:
            self.posicion[0] -= 1

    def actuar(self, mapa):
        if not self.actuo:
            mapa[self.posicion[0]][self.posicion[1]] = 0

            if self.estrategia == Estrategias.Estrategia.OFENSIVA.value:
                Estrategias.Ofensiva(self, mapa)
            elif self.estrategia == Estrategias.Estrategia.DEFENSIVA.value:
                Estrategias.Defensiva(self, mapa)

            mapa[self.posicion[0]][self.posicion[1]] = self
            self.actuo = True

    def descansar(self):
        self.actuo = False

