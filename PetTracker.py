while True:
    try:
        amount = int(input("¿How many pets do you want to register?: "))
        break
    except ValueError:
        print("You need to insert a number")

plus_5 = 0
eq_less_5 = 0

for _ in range(amount):
    pet_race = input("Insert the race of the animal: ")
    valid = False
    while not valid:
        try:
            age = int(input("Insert the age of your pet: "))
            valid = True
        except ValueError:
            print("The age should be a number")
    if age > 5:
        print(f"The race of the pet is: {pet_race}")
        print("Your pet should have vaccine type B")
        plus_5 += 1    ##The same as: plus_5 = plus_5 + 1##
    else:
        print(f"The race of the pet is: {pet_race}")
        print("Your pet should have vaccine type A")
        eq_less_5 += 1   ##The same as: plus_5 = plus_5 + 1##

print(f"There are {plus_5} pets with more than 5 years")
print(f"There are {eq_less_5} pets with 5 years or less")