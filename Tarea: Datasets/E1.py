# Tarea:
# Leer los datos proveidos sobre paises, poblacion y tamaño e
# realizar algunas operaciones basicas de procesamiento de datos,
# como limpiar los datos eliminando filas incompletas y
# consegir el pais con mayor tamaño y poblacion

from enum import Enum

# Dataset
data = [
    "Country,Population,Area (km²)\n",
    "USA,331002651,9833517\n",
    "Canada,37742154,9976140\n",
    "China,1439323776,9596961\n",
    "India,1380004385,3287263\n",
    "Brazil,212559417,8515767\n",
    "Australia,25409881,7692024\n",
    "Russia,145912025,17098242\n",
    "Japan,126476461,377973\n",
    "Germany,83783942,357022\n",
    "France,65273511,551695\n",
    "UK,67886011,243610\n",
    "Italy,60244639,301340\n",
    "Mexico,128932753,1972550\n",
    "South Africa,59308690,1219090\n",
    "Egypt,91250000,1001450\n",
    "Nigeria,206139589,923768\n",
    "Kenya,53771296,580367\n",
    "Argentina,45195777,2780400\n",
    "Colombia,50882891,1141748\n",
    "Chile,19116201,756102\n",
    "Peru,32971854,1285216\n"
]

class Field(Enum):
    NAME = 0
    POPULATION = 1
    AREA = 2
    QUANTITY = 3

pre_processed_data = []
for i in data[1:]:
    saltear = False
    e = i.strip().split(",")

    for campo in e:
        if campo == '':
            saltear = True

    if saltear:
        continue

    # Eliminar paises con valores faltantes
    if len(e) == Field.QUANTITY.value:
        pre_processed_data.append(e)

mayor_tamaño = 0
for i in pre_processed_data:
    if int(i[Field.AREA.value]) > mayor_tamaño:
        nombre_mayor_tamaño = i[Field.NAME.value]
        mayor_tamaño = int(i[Field.AREA.value])

mayor_poblacion = 0
for i in pre_processed_data:
    if int(i[Field.POPULATION.value]) > mayor_poblacion:
        nombre_mayor_poblacion = i[Field.NAME.value]
        mayor_poblacion = int(i[Field.POPULATION.value])


print("El pais mas grande es " + nombre_mayor_tamaño + " con " + str(mayor_tamaño) + "Km²")
print("El pais con mas poblacion es " + nombre_mayor_poblacion + " con " + str(mayor_poblacion) + " personas")
