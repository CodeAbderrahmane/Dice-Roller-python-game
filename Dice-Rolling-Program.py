import random

dice_art = {
    1: (
        "┌─────┐",
        "│     │",
        "│  •  │",
        "│     │",
        "└─────┘"
    ),
    2: (
        "┌─────┐",
        "│ •   │",
        "│     │",
        "│   • │",
        "└─────┘"
    ),
    3: (
        "┌─────┐",
        "│ •   │",
        "│  •  │",
        "│   • │",
        "└─────┘"
    ),
    4: (
        "┌─────┐",
        "│ • • │",
        "│     │",
        "│ • • │",
        "└─────┘"
    ),
    5: (
        "┌─────┐",
        "│ • • │",
        "│  •  │",
        "│ • • │",
        "└─────┘"
    ),
    6: (
        "┌─────┐",
        "│ • • │",
        "│ • • │",
        "│ • • │",
        "└─────┘"
    ),
}


dice = []

MAX_DICE = 15

running = True

while running:
    n = input("How many times would you like to roll: ") 
    total = 0
    if n.isdigit() and int(n) > 0 and int(n) < MAX_DICE :
            n = int(n)
            dice.clear()
            for x in range(n):
                roll = random.randint(1,6)
                dice.append(roll)
                total += roll
            print(dice)

            for x in range(5):
                for j in range(n):
                    print(dice_art[dice[j]][x], end=" ")
                print()
            print(f"Your total is: {total}")
            if input("Would you like to play again (y/n): ").lower() != "y":
                print("Thank you for playing!!!")
                running = False
    else:
        print(f"Please enter a number thats less than {MAX_DICE} and greater than 0")
    