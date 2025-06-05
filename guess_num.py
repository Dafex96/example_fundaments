from random import randint

while True:
    try:
        num1 = int(input("Guess a number between 1 and 10: "))
        break
    except ValueError:
        print("You should enter a number, try again")

num2 = randint(1,10)

try:
    while num1 == num2:
        print("¡You Win!")
        opt = input("¿Do you want to keep playing? (Yes/No) ")
        if opt.lower() ==  "no":
            break
    else:
        print("You lose")
        print(f"The winning number was {num2}, your number was {num1}")
except ValueError:
    print("You need to guess a number not a letter")