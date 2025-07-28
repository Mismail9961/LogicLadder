import random  # Step 1

# Step 2: Function to roll dice
def roll_dice(num_dice):
    results = []  # empty list to store dice results
    for _ in range(num_dice):  # repeat for number of dice
        result = random.randint(1, 6)  # generate random number between 1 and 6
        results.append(result)  # add result to list
    return results  # return all results

# Step 3: Main function to run the program
def main():
    print("🎲 Welcome to the Dice Roller! 🎲")

    total_rolls = 0  # Step 4: Counter for how many times the dice were rolled

    while True:  # Step 5: Repeat until user says no
        try:
            # Step 6: Ask how many dice the user wants to roll
            num_dice = int(input("How many dice do you want to roll? "))
        except ValueError:
            # Step 7: If the user types something that's not a number
            print("Please enter a valid number.")
            continue  # go back to start of the loop

        # Step 8: Call the function to roll the dice
        results = roll_dice(num_dice)

        # Step 9: Show the result to the user
        print("You rolled:", results)

        # Step 10: Increase the total rolls counter
        total_rolls += 1
        print("Total rolls so far:", total_rolls)

        # Step 11: Ask if the user wants to roll again
        roll_again = input("Do you want to roll again? (yes/no): ").lower()

        # Step 12: If user says no, break the loop
        if roll_again != "yes":
            print("Thanks for playing! 👋")
            break  # exit the loop and end the program

# Step 13: Call the main function to start the program
main()
