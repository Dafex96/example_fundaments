def functions(num1,num2,option):
    if option == 1:
        return(num1 + num2)
    elif option == 2:
        return(num1 - num2)
    elif option == 3:
        return(num1 * num2)
    elif option == 4:
        return(num1 // num2)
    elif option == 5:
        return("Goodbye, see you soon.")
    else:
        return("Invalid option, try again")

def menu():
    print("--Calculator--")
    print("1) Addition")
    print("2) Subtraction")
    print("3) Multiplication")
    print("4) Division")
    print("5) Exit")

menu()

while True:
    try:
        option = int(input("Insert an option: "))
        break
    except ValueError:
        print("Invalid option, try again.")