"""
name = input("Escriba su nombre: ")
print(f"Bienvenido {name}!")
"""

number1 = int(input("ingrese el primer numero: "))
number2 = int(input("ingrese el segundo numero: "))

print(f"La suma de {number1} y {number2} es: {number1 + number2}")
print(f"La resta de {number1} y {number2} es: {number1 - number2}")
print(f"La multiplicacion de {number1} y {number2} es: {number1 * number2}")
if number2 == 0:
    print("NO se puede dividir entre 0")
else:
    print(f"La division de {number1} y {number2} es: {number1 / number2}")