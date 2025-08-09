# Consigna:
# Hacer un programa que calcule el indice de masa corporal de el usuario
# y le diga en que clasificacion se encuentra.

peso = float( input("Ingrese su peso en KG: ") )
altura = float( input("Ingrese su altura en metros:") )

imc = peso / (altura * altura)

# Se uso esta tabla: https://www.nutreteconmigoamigo.com/wp-content/uploads/2013/01/Tabla-IMC-300x226.jpg
if imc < 18.5:
    print("Usted tiene bajo peso")
elif imc < 24.9:
    print("Usted tiene un peso normal")
elif imc < 26.9:
    print("Usted tiene sobrepeso grado 1")
elif imc < 29.9:
    print("Usted tiene sobrepeso grado 2")
elif imc < 34.9:
    print("Usted tiene obesidad tipo 1")
elif imc < 39.9:
    print("Usted tiene obesidad tipo 2")
elif imc < 49.9:
    print("Usted tiene obesidad tipo 3")
else:
    print("Usted tiene obesidad tipo 4")
