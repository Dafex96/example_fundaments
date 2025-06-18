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

option = 0
num1 = 0
num2 = 0


while True:
    try:
        option = int(input("Insert an option: "))
        break
    except ValueError:
        print("Invalid option, try again.")

while option > 0 and option < 6:
    if option == 1:
        
        print("--Addition--")
        num1 = int(input("Insert the first number: "))
        num2 = int(input("Insert the second number: "))
        ans = num1 + num2
        
        print(f"The answer is: {ans}")
        
        menu()
        option = int(input("Insert an option: "))
        
    elif option == 2:
        
        print("--Subtraction--")
        num1 = int(input("Insert the first number: "))
        num2 = int(input("Insert the second number: "))
        ans = num1 - num2
        
        print(f"The answer is: {ans}")
        menu()
        
        option = int(input("Insert an option: "))
        
    elif option == 3:
        
        print("--Multiplication--")
        num1 = int(input("Insert the first number: "))
        num2 = int(input("Insert the second number: "))
        ans = num1 * num2
        
        print(f"The answer is: {ans}")
        menu()
        
        option = int(input("Insert an option: "))
        
    elif option == 4:
        
        print("--Division--")
        num1 = int(input("Insert the first number: "))
        num2 = int(input("Insert the second number: "))
        ans = num1 // num2
        
        print(f"The answer is: {ans}")
        menu()
        
        option = int(input("Insert an option: "))
        
    elif option == 5:
        
        print("Thank you, see you soon")
        
    else:
        print("Invalid option, try again")