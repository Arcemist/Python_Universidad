# Version adaptada del Ejercicio 10 de la lista 1:

class Horario():
    def __init__(self, nombre, horario):
        self.__nombre = nombre
        self.__horas = horario

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre_nuevo):
        self.__nombre == nombre_nuevo

    @nombre.deleter
    def nombre(self):
        del self.__nombre

    @property
    def horas(self):
        return self.__horas

    @horas.setter
    def horas(self, horario_nuevo):
        self.__horas == horario_nuevo

    @horas.deleter
    def horas(self):
        del self.__horas


class Manaña(Horario):
    def __init__(self):
        super().__init__("Mañana", "8AM - 11AM")

class Tarde(Horario):
    def __init__(self):
        super().__init__("Tarde", "1PM - 6PM")

class Noche(Horario):
    def __init__(self):
        super().__init__("Noche", "6PM - 11PM")

print("""
Introduce tu Horario segun esta regla:
    M - 
""")
