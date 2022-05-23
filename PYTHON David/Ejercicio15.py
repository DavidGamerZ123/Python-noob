import random


print(" .........................................")
print("........... ADIVINATOR DAVID ..............")
print(" .........................................")

print("dime tu numero")

numerodado = int(input())

print("Vale voy a decirte numeros y me tienes que decir si acerté")
print("si acerte escribe (si) si no, (no)")


random.seed(10)


print (f"{random.random()}")

print("es tu numero")

respuesta = input()

if respuesta == "si":
    print ("Yupi adivine tu numero")
    
while respuesta == "no":
    print(f"es este? {random.random()} ")
    respuesta = input()
    print("vale")
    


