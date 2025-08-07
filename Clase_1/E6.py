# Consigna:
# Hacer un programa que tome 3 numeros y devuelva el mas grande

num1 = float( input("Ingrese el primer numero: ") )
num2 = float( input("Ingrese el segundo numero: ") )
num3 = float( input("Ingrese el tercer numero: ") )

if num1 > num2:
    if num1 > num3:
        print("El numero mayor es:", num1)
    else:
        print("El numero mayor es:", num3)
else:
    if num2 > num3:
        print("El numero mayor es:", num2)
    else:
        print("El numero mayor es", num3)
