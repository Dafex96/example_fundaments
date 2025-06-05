import random

rps = ["rock", "paper", "scissors"]

user = input("Choose rock, paper or scissors: ").lower()

while True:
    if user not in rps:
        print("You need to enter one of the three options")
        user = input("Choose rock, paper or scissors: ").lower()
    else:
        break

ai = random.choice(rps)

print(f"¡The AI chose {ai}, you chose {user}")

if user == ai:
    print("¡It is a tie!")
elif (user == "rock" and ai == "scissors") or \
        (user == "paper" and ai == "rock") or \
        (user == "scissors" and ai == "paper"):
        print("You win!")
else:
        print("AI wins!")