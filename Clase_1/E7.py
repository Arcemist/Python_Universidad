# Consigna:
# Hacer un programa que reciba 3 numeros y muestre numero el mayor y menor

num1 = float( input("Ingrese el primer numero: ") )
num2 = float( input("Ingrese el segundo numero: ") )
num3 = float( input("Ingrese el tercer numero: ") )

if num1 > num2:
    if num1 > num3:
        print("El numero mayor es:", num1)

        if num3 > num2:
            print("El numero menor es:", num2)
        else:
            print("El numero menor es:", num3)

    else:
        # num3 >= num1 > num2
        print("El numero mayor es:", num3)
        print("El numero menor es:", num2)

else:
    if num2 > num3:
        print("El numero mayor es:", num2)

        if num3 > num1:
            print("El numero menor es:", num1)
        else:
            print("El numero menor es:", num3)

    else:
        # num3 >= num2 >= num1
        print("El numero mayor es:", num3)
        print("El numero menor es:", num1)
