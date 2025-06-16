def functions(num1,num2,option):
    if option == 1:
        return(num1 + num2)
    elif option == 2:
        return(num1 - num2)
    elif option == 3:
        return(num1 * num2)
    elif option == 4:
        return(num1 // num2)

def menu():
    print("--Calculator--")
    print("1) Addition")
    print("2) Subtraction")
    print("3) Multiplication")
    print("4) Division")


option = int(input("Insert an option: "))