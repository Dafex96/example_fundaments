# league = {"01":["Colo-Colo"], "02":["Universidad de Chile"],
# "03":["Universidad Católica"], "04":["Union Española"], "05":["Magallanes"]}

teams = ["Colo-Colo","Universidad de Chile","Universidad Católica","Magallanes","Curicó Unido"]

def menu():
    print("--Football Teams Shits--")
    print("1) Colo-Colo")
    print("2) Universidad de Chile")
    print("3) Universidad Católica")
    print("4) Magallanes")
    print("5) Curicó Unido")
    print("6) Quit")

while True:
    try:
        menu()
        user = int(input("Choose your team: "))
        break
    except ValueError:
        print("You need to enter a valid option, try again.")

while True:
    if user == 1:
        h_a = input("Do you want the home or away version?: ")
        try:
            quant = int(input("How many shirts do you want?: "))
        except ValueError:
            print("You need to enter a valid option, try again.")
        print(" ")
        print(f"Purchase successful! You bought {quant} {teams[0]} {h_a} version shirts")
        print(" ")
        menu()
        user = int(input("Choose your team: "))
    elif user == 2:
        h_a = input("Do you want the home or away version?: ")
        try:
            quant = int(input("How many shirts do you want?: "))
        except ValueError:
            print("You need to enter a valid option, try again.")
        print(" ")
        print(f"Purchase successful! You bought {quant} {teams[1]} {h_a} version shirts")
        print(" ")
        menu()
        user = int(input("Choose your team: "))
    elif user == 3:
        h_a = input("Do you want the home or away version?: ")
        try:
            quant = int(input("How many shirts do you want?: "))
        except ValueError:
            print("You need to enter a valid option, try again.")
        print(" ")
        print(f"Purchase successful! You bought {quant} {teams[2]} {h_a} version shirts")
        print(" ")
        menu()
        user = int(input("Choose your team: "))
    elif user == 4:
        h_a = input("Do you want the home or away version?: ")
        try:
            quant = int(input("How many shirts do you want?: "))
        except ValueError:
            print("You need to enter a valid option, try again.")
        print(" ")
        print(f"Purchase successful! You bought {quant} {teams[3]} {h_a} version shirts")
        print(" ")
        menu()
        user = int(input("Choose your team: "))
    elif user == 5:
        h_a = input("Do you want the home or away version?: ")
        try:
            quant = int(input("How many shirts do you want?: "))
        except ValueError:
            print("You need to enter a valid option, try again.")
        print(" ")
        print(f"Purchase successful! You bought {quant} {teams[4]} {h_a} version shirts")
        print(" ")
        menu()
        user = int(input("Choose your team: "))
    elif user == 6:
        print("Goodbye, See you soon!")
        break
    else:
        print("Invalid option, try again.")
        menu()
        user = int(input("Choose your team: "))

#Uknown error :(  ,  to be fixed...