import random

random_number = random.randint(1,100)

while True:

    try:
        number = int(input("Take a guess : "))
    
    except ValueError:
        print("Only numbers ")

    
    if number == random_number:
        print("You win the game . ")
        break
    elif number > random_number :
        print("Too high . ")
    elif number < random_number :
        print("Too Low . ")
    else:
        pass
