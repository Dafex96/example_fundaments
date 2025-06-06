def menu():
    print("//-Cine Colo-Colo-\\")
    print("¡Bienvenido al Cine Colo-Colo!")
    print(" ")
    print("1) Ver stock de entradas")
    print(" ")
    print("2) Comprar entradas")
    print(" ")
    print("3) Salir")
    print(" ")

while True:
    try:
        menu()
        opc = int(input("Ingrese la opcion que desea: "))
        break
    except ValueError:
        print("Debe ingresar una opcion valida, intente nuevamente")
        print(" ")

stock = 50

while True:
    if opc == 1:
        try:
            
            print(f"El stock de entradas es de {stock}")
            print(" ")
            menu()
            opc = int(input("Ingrese la opcion que desea: "))
            
        except ValueError:
            print("Debe ingresar una opcion valida, intente nuevamente")
        
    elif opc == 2:
        try:
        
            print(" ")
            compra = int(input("¿Cuantas entradas desea comprar? "))
            stock = stock - compra
            
            while compra > stock:
                stock = 50
                print("¡Estas comprando mas entradas de las que hay!")
                print(f"¡Solo hay {stock} entradas!")
                compra = int(input("¿Cuantas entradas desea comprar? "))
                stock = stock - compra
            print(f"¡Compra satisfactoria! Quedan {stock} entradas.")
            print(" ")
            menu()
            opc = int(input("Ingrese la opcion que desea: "))
        
        except ValueError:
            print("Debe ingresar un numero entero, intente nuevamente")
        
    elif opc == 3:
        print("------------------------------")
        print("¡Muchas gracias, hasta pronto!")
        print("------------------------------")
        break
    else:
        try:
            
            print("Opcion ingresada no valida, intente nuevamente ")
            print(" ")
            menu()
            opc = int(input("Ingrese la opcion que desea: "))
            
        except ValueError:
            print("Debe ingresar un numero entero, intente nuevamente")