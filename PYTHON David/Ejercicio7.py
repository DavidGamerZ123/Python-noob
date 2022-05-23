print("Dime tu numero a")
a=float(input())

print("Dime tu numero b")
b=float(input())

suma = a + b

print(f"la suma es {suma}")

if suma == 0:
    print("es cero")

if suma < 0:
    print("es negativo")

if suma > 0:
    print("es positivo")
