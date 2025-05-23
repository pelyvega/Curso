num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))
num3 = int(input("Ingresa el tercer numero: "))

if num1 > num3 and num2 < num3:
    print(f"{num1} es mayor; {num3} es el del MEDIO y {num2} es el MENOR")
elif num2 > num1 and num3 < num1:
    print(f"{num2} es mayor; {num1} es el del MEDIO y {num3} es el MENOR")
elif num3 > num2 and num1 < num2:
    print(f"{num3} es mayor; {num2} es el del MEDIO y {num1} es el MENOR")
"""
elif num1 == num2 > num3:
    print(f"{num1} y {num2} son mayores")
elif num3 == num2 > num1:
    print(f"{num3} y {num2} son mayores")
elif num1 == num3 > num2:
    print(f"{num1} y {num3} son mayores")
else:
    if num1 == num3 and num2 == num1:
        print("LOs numeros son iguales")
"""