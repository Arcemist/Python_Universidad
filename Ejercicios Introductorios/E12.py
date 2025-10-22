# Consigna:
# Hacer un programa que reciba 5 nombres y 5 edades, que las guarde en un vector de nombres y de edades,
# para despues mostrar el nombre de la persona mayor y menor.

nombres = []
edades = []

for i in range(5):
    nombres.append(input("Ingrese un nombre: "))

for i in range(5):
    edades.append(int( input("Ingrese una edad: ")))

p_maxima = edades.index(max(edades))
p_minima = edades.index(min(edades))

print("La persona mas vieja es:", nombres[p_maxima])
print("La persona mas joven es:", nombres[p_minima])
