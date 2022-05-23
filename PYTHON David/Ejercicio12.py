print("Dime un caracter y te dire si es o no mayuscula")

caracter = input()

if caracter.islower():
    print("es minuscula")
if caracter.isupper():
    print("Es mayuscula")