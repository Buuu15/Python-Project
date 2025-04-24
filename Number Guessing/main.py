import random

guess = random.randint(1, 100)

while True:
    number = input("Enter a number between 1 and 100: ")
    number = int(number)
    if number == guess:
        print("You guessed it right!")
        break
    elif number < guess:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")