# Consigna:
# Crear un programa que reciba 2 numeros del usuario y devuelva el mayor

num1 = int( input("Digite el primer numero: ") )
num2 = int( input("Digite el segundo numero: ") )

if num1 > num2:
    print("El numero mas grande es:", num1)
elif num1 != num2:
    print("El numero mas grande es:", num2)
else:
    print("Son numeros iguales")
