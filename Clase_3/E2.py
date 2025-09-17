# Tarea:
# Leer los datos proveidos e realizar algunas operaciones
# basicas de procesamiento de datos, como limpiar los datos
# eliminando filas incompletas y consegir el pais con mayor
# cantidad de premios

from enum import Enum

# Dataset
data = [
    "Team Name,Country,Awards,Members\n",
    "TigerBots,Germany,22,15\n",
    "Erlangen Robotics,Germany,18,12\n",
    "Boston Dynamics,USA,30,20\n",
    "Robotics Club of MIT,USA,25,14\n",
    "FIRST Team 254,USA,20,12\n",
    "CyberKnights,China,,16\n",
    "RoboMaster Team,China,24,14\n",
    "Team Indus,India,16,10\n",
    "VEX Robotics Team,India,,8\n",
    "RoboCup Team,Australia,19,13\n",
    "Team Australia,Australia,15,11\n",
    "Robotika,Russia,23,17\n",
    "RoboZon,Japan,21,14\n",
    "Team 341: Miss Daisy,USA,17,\n",
    "RoboSense,France,12,9\n",
    "Team 1114: Simbotics,Canada,28,18\n",
    "RoboGenius,UK,20,13\n",
    "Team 148: Robowranglers,USA,25,16\n",
    "Robotic Vision,,15,10\n",
    "RoboCup Champions,Argentina,14,9\n",
    "Team 118: The Robonauts,USA,,13\n",
    "RoboMinds,Colombia,11,8\n",
    "Team 133: B.E.R.T.,USA,13,9\n"
]

class Field(Enum):
    NAME = 0
    COUNTRY = 1
    AWARDS = 2
    MEMBERS = 3
    QUANTITY = 4

pre_processed_data = []
for i in data[1:]:
    saltear = False
    e = i.strip().split(",")

    for campo in e:
        if campo == '':
            saltear = True

    if saltear:
        continue

    if len(e) == Field.QUANTITY.value:
        pre_processed_data.append(e)

premios = {}
for i in pre_processed_data:
    if i[Field.COUNTRY.value] in premios:
        premios[i[Field.COUNTRY.value]] += int(i[Field.AWARDS.value])
    else:
        premios[i[Field.COUNTRY.value]] = 0
        premios[i[Field.COUNTRY.value]] += int(i[Field.AWARDS.value])

premios_maximos = 0
for pais in premios:
    if premios[pais] > premios_maximos:
        premios_maximos = premios[pais]
        pais_premios_maximos = pais

print("El pais con mayor cantidad de premios es " + pais_premios_maximos + " con " + str(premios_maximos))
