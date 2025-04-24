import random

while True:
    choice = input("Roll the dice? (y/n) ").lower()
    if choice == 'y':
        a = random.randint(1,6)
        b = random.randint(1,6)
        print(f"[{a} , {b}]")
    elif choice == 'n':
        print("Thanks for playing")
        break
    else:
        print("Invalid choice")

    
