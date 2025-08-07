# Consigna:
# Hacer un programa que te pregunte tu turno en el que estudias,
# y segun un input de "M" o "V" o "T" muestre un mensaje de
# "Buen Dia!" o "Buenas Tardes!" o "Buenas Noches!"
# o "¡Valor no válido!", segun el caso.

print("""
Introduce tu horario segun esta regla:
    M para Mañana
    V para Tarde
    N para Noche
""")

horario = input()


if horario == "M":
    print("Buen Dia!")
elif horario == "V":
    print("Buenas Tardes!")
elif horario == "N":
    print("Buenas Noches!")
else:
    print("¡Valor no válido!")
