# Consigna:
# Hacer un programa que tenga un vector de 10 valores Int predefinidos, y que despues lea un valor entero
# del usuario y informe si ese valor se encuentra en el vector y en que posicion/es se encontro.
# Ademas al final tiene que mostrar el vector ordenado de forma decendiente.

vector = [ 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 ]

num = int( input("Ingrese el numero: ") )

for i in range(len(vector)):
    if vector[i] == num:
        print("Se encontro el valor", num, "en la posicion:", i);

vector.sort(reverse=True)

print("\nEl vector era:")
for n in vector:
    print(n)
