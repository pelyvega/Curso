name = input("Ingresa el nombre: ")
age = int(input("Ingresa la edad: "))
if age < 12:
    print(f"{name} es un niño")
elif age >= 12 and age <= 17:
    print(f"{name} es un adolescente")
elif age >= 18 and age <= 30:
    print(f"{name} es un joven adulto!")
