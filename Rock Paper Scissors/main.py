import random
choices = ['r', 'p', 's']


while True:
    game = input("Rock Paper Scissors shoot (r/p/s) : ").lower()
    game = str(game)

    computer = random.choice(choices)
    print("Computer makes a choice " , computer)

    if game == 'r' and computer == 'p':
        print("You Lose")
    elif game == 'r' and computer == 's':
        print("You win")
    elif game == 'p' and computer == 'r':
        print("You win")
    elif game == 'p' and computer == 's':
        print("You Lose")
    elif game == 's' and computer == 'r':
        print("You Lose")
    elif game == 's' and computer == 'p':
        print("You win")
    elif game == computer:
        print("Draw")
    else:
        print("Invalid input, please try again.")

