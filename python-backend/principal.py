import operaciones

#programa con un MENU de opciones
numero1 = int(input("ingrese el numero: "))
numero2 = int(input("ingrese el numero: "))

print("----- MENU PRINCIPAL -----")
print("----- 1. Suma Estatica -----")
print("----- 2. Suma Optimizada -----")
print("----- 3. Resta Estatica -----")
print("----- 4. Resta Optimizada -----")
print("----- 5. Dision Optimizada -----")
print("----- Seleccione su opcion -----")
opcion = input("Digite la opción que desea usar: ")

match opcion:
    case "1":
        operaciones.sumNumEst()
    case "2":
        operaciones.sumNumopt(numero1,numero2)
    case "3":
        operaciones.restNumEst()
    case "4":
        operaciones.restNumopt(numero1,numero2)
    case "5":
        operaciones.divNumopt(numero1,numero2)
    case _:
        print("NO existe esa opción")
print("Fin del programa")
    
