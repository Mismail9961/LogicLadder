import random
from datetime import datetime

score = 0
history = []

while True:
    choice = input("Press 'r' to roll the dice or 'q' to quit: ").lower()
    if choice == "r":
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        total = die1 + die2
        score += total
        time = datetime.now().strftime("%H:%M:%S")
        history.append((die1,die2,total,time))
        print(f"You rolled {die1} and {die2}. Total this round: {total}. Score: {score}")
    elif choice == "q":
        print("\nGame Over!")
        print(f"Final Score: {score}")
        print("Roll History:")
        for h in history:
            print(f"Rolled {h[0]} + {h[1]} = {h[2]} at {h[3]}")
        break
    else:
        print("Invalid input.")