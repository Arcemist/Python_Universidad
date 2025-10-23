# Consigna:
# Leer las notas de 2 parciales y devolver:
#  -"Aprobado", si el promedio es mayor o igual a 7
#  -"No aprobado", si el promedio es menor a 7
#  -"Aprobado con 10", si el promedio es 10

e1 = float( input("Ingrese la nota del primer parcial: ") )
e2 = float( input("Ingrese la nota del segundo parcial: ") )

promedio = (e1 + e2) / 2

if promedio == 10:
    print("Aprobado con 10")
elif promedio >= 7:
    print("Aprobado")
else:
    print("Reprobado")
