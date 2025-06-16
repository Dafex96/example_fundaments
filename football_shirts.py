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
        quant = int(input("How many shirts do you want?: "))
        print(f"Purchase successful! You bought {quant} {h_a} version shirts")
        break
    elif user == 2:
        h_a = input("Do you want the home or away version?: ")
        quant = int(input("How many shirts do you want?: "))
        print(f"Purchase successful! You bought {quant} {h_a} version shirts")
        break