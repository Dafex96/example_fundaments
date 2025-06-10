
while True:
    try:
        cant = int(input("Insert the amount of employees to register: "))
        break
    except ValueError:
        print("You must enter a whole number, try again.")

plus_10 = 0
less_eq_10 = 0

for _ in range(cant):
    
    name = input("Insert the name of the employee: ")
    
    while True:
        try:
            years = int(input("Insert the antiquity years of the employee: "))
            break
        except ValueError:
            print("You must enter a whole number, try again.")
    
    if years > 10:
        print("More than 10 years of antiquity")
        plus_10 += 1
    else:
        print("Less than 10 years of antiquity")
        less_eq_10 += 1

print(f"{plus_10} employees have more than 10 years of antiquity")
print(f"{less_eq_10} employees have 10 years or less of antiquity")