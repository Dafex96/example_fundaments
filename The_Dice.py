from random import randint

while True:
    try:
        print("---Welcome to---")
        print("---The Dice---")
        
        first_guess = int(input("¡Take a guess! "))
        
        while first_guess < 1 or first_guess > 6:
            
            first_guess = int(input("¡The dice does not that number, try again! "))
            
        
        win_num = randint(1,6)
        
        print(f"¡The winning number was {win_num}, your guess was {first_guess}!")
        
        again = input("¿Do you want to keep playing? (Y/N) ")
        
        if again.upper() == "N":
            
            print("¡Thanks for playing!")
            
            break
        
    
    except ValueError:
        print("¡The Dice only have numbers, not letters!")