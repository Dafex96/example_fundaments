def menu():
    print("//-Cine Colo-Colo-\\")
    print("¡Welcome to Colo-Colo Cinema!")
    print(" ")
    print("1) See tickets stock")
    print(" ")
    print("2) Buy tickets")
    print(" ")
    print("3) Quit")
    print(" ")

while True:
    try:
        menu()
        opc = int(input("Insert an option: "))
        break
    except ValueError:
        print("You must enter a valid option, try again.")
        print(" ")

stock = 50

while True:
    if opc == 1:
        try:
            
            print(f"The ticket stock is {stock}")
            print(" ")
            menu()
            opc = int(input("Insert an option: "))
            
        except ValueError:
            print("You must enter a valid option, try again.")
        
    elif opc == 2:
        try:
        
            print(" ")
            buy = int(input("How many tickets do you want to buy? "))
            stock = stock - buy
            
            while buy > stock:
                stock = 50
                print("¡There are not that many tickets!")
                print(f"¡There are just {stock} tickets!")
                buy = int(input("How may tickets do you want to buy? "))
                stock = stock - buy
            print(f"¡Successful purchase! There are {stock} tickets left.")
            print(" ")
            menu()
            opc = int(input("Insert an option: "))
        
        except ValueError:
            print("You must enter a valid option, try again.")
        
    elif opc == 3:
        print("------------------------------")
        print("¡Thank you, see you soon!")
        print("------------------------------")
        break
    else:
        try:
            
            print("You must enter a valid option, try again.")
            print(" ")
            menu()
            opc = int(input("Insert an option: "))
            
        except ValueError:
            print("You need to enter a whole number, try again.")