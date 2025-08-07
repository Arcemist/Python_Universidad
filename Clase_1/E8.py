# Consigna:
# Hacer un programa que reciba el precio de 3 productos y te recomiende el mas barato

p1 = float( input("Introduce el precio de el primer producto: ") )
p2 = float( input("Introduce el precio de el segundo producto: ") )
p3 = float( input("Introduce el precio de el tercer producto: ") )

if p1 == p2 == p3:
    print("Recommendaria los tres productos")

elif p1 > p2:
    if p2 == p3:
        print("Recommendaria el segundo y tercer producto")

    elif p2 > p3:
        print("Recommendaria el tercer producto")

    else:
        print("Recommendaria el segundo producto")

elif p3 > p2:
    if p2 == p1:
        print("Recommendaria el segundo y primer producto")
    else:
        print("Recommendaria el segundo producto")

else:
    if p3 == p1:
        print("Recommendaria el tercer y primer producto")

    elif p1 > p3:
        print("Recommendaria el tercer producto")

    else:
        print("Recommendaria el primer producto")
