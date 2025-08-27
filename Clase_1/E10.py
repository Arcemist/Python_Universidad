# Consigna:
# Hacer un programa que te pregunte tu turno en el que estudias,
# y segun un input de "M" o "V" o "T" muestre un mensaje de
# "Buen Dia!" o "Buenas Tardes!" o "Buenas Noches!"
# o "¡Valor no válido!", segun el caso.
# Fe de errata: cambiado para que se pueda usar la letra en minuscula
# Debido a la opiñon del profe en la siguiente clase

print("""
Introduce tu horario segun esta regla:
    M - Mañana
    V - Tarde
    N - Noche
""")

horario = input()

if horario == "M" or "m":
    print("Buen Dia!")
elif horario == "V" or "v":
    print("Buenas Tardes!")
elif horario == "N" or "n":
    print("Buenas Noches!")
else:
    print("¡Valor no válido!")
