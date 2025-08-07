# Consigna:
# Escribir un programa que verifique si una letra es una vocal o consonante

letra = input("Ingrese la letra a ser checkeada: ")

vocales = [ "A" , "E", "I", "O", "U", "a", "e", "i", "o", "u" ]
if letra in vocales:
    print("Es una vocal")
else: 
    # Asumiendo que el usuario no usa mal el programa
    print("Es una consonante")
