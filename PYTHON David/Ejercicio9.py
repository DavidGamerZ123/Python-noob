from ast import While
from operator import truediv


print("dime un numero entre 1 al 12 ten en cueta que dará error si pasa de 12 o menos de 1")


pregunta = True


while pregunta == True:
    numero = int(input("Dame el num: "))
    if numero < 1 or numero > 12:
        print("ERROR DAME UN NUMERO ENTRO 1 Al 12")
    else:
        pregunta = False






meses = [ 'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

if numero == 1:
    print(meses[1-1])

if numero == 2:
    print(meses[2-1])

if numero == 3:
    print(meses[3-1])

if numero == 4:
    print(meses[4-1])

if numero == 5:
    print(meses[5-1])

if numero == 6:
    print(meses[6-1])

if numero == 7:
    print(meses[7-1])

if numero == 8:
    print(meses[8-1])

if numero == 9:
    print(meses[9-1])

if numero == 10:
    print(meses[10-1])

if numero == 11:
    print(meses[11-1])

if numero == 12:
    print(meses[12-1])
