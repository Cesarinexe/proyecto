num1 = int(input("numero 1: ")) 
num2 = int(input("numero 2: ")) 

while True:
    print("""seleccione opcion
            1- Sumar 
            2- Restar
            3- Multiplicar
            4- Dividir 
        """)

    valor = int(input("Elige una opcion: ") )     

    if valor == 1:
        print("La suma es", num1 + num2)
        break
    elif valor == 2:
        print("La resta es", num1 - num2)
        break
    elif valor == 3:
        print("La multiplicacion es", num1 * num2)
        break
    elif valor == 4:
        print("La division es", num1 / num2)
        break
    else:
        print("Opcion incorrecta, por favor intente de nuevo.")
