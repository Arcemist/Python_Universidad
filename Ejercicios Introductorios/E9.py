# Consigna:
# Hacer un programa que reciba 3 numeros y los devuelva en orden decendiente

numeros = []

numeros.append(float( input("Introduzca un numero: ") ))
numeros.append(float( input("Introduzca un numero: ") ))
numeros.append(float( input("Introduzca un numero: ") ))

numeros.sort(reverse=True)

for num in numeros:
    print(num)
