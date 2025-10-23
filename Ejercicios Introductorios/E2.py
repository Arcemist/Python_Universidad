# Consigna:
# Hacer un programa que reciba un valor del usuario y indique si este es positivo o negativo

num = int( input("Ingrese el numero: ") ) 

if num > 0:
    print("El numero es positivo")
elif num != 0:
    print("El numero es negativo")
else:
    print("El numero es 0")
