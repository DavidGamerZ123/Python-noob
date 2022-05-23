#Crea una aplicación que pida un número y calcule su factorial (El factorial de un número es
#l producto de todos los enteros entre 1 y el propio número y se representa por el número
#seguido de un signo de exclamación. Por ejemplo 5! = 1x2x3x4x5=120

print("Dame un numero y calculo el factorial")

numerorecibido = int(input())

#ahora importo esto para calcular solo el factorial es decir importo la funcion matematica
from math import factorial

print ("Factorial is", factorial(numerorecibido))