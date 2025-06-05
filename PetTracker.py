
while True:
    try:
        print("--PetTracker--")
        
        print("1) Dog")
        print("2) Cat")
        print("3) Hamster")
        
        try:
            pet = int(input("Insert the type of pet do you have: "))
        except ValueError:
            print("You need to insert a number")
        pet_name = input("Insert the name of your pet: ")
        
        pet_age = int(input("Insert the age of your pet: "))
        
        vac = int(input("¿Is your pet vaccinated? (1:Yes, 2:No): "))
        
    except:
        print("end")