import random

# Best score tracker (set to None initially)
best_score = None

def play_game():
    global best_score

    print("\n🎯 Welcome to the Number Guessing Game! 🎯")

    # Let the user choose the number range
    try:
        min_val = int(input("Enter the minimum number: "))
        max_val = int(input("Enter the maximum number: "))
    except ValueError:
        print("Please enter valid numbers!")
        return

    if min_val >= max_val:
        print("Minimum should be less than maximum.")
        return

    # Let the user set a limit on the number of guesses
    try:
        guess_limit = int(input("How many guesses would you like to have? "))
    except ValueError:
        print("Please enter a valid number of guesses.")
        return

    # Generate the secret number
    secret_number = random.randint(min_val, max_val)
    attempts = 0

    print(f"\nI'm thinking of a number between {min_val} and {max_val}. Can you guess it?")

    # Game loop
    while attempts < guess_limit:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess == secret_number:
            print(f"🎉 Correct! You guessed it in {attempts} attempts.")
            
            # Update best score
            if best_score is None or attempts < best_score:
                best_score = attempts
                print("🏆 New Best Score!")
            else:
                print(f"Best Score so far: {best_score} attempts")

            break

        elif guess < secret_number:
            print("Too low ⬇️")
        else:
            print("Too high ⬆️")

    else:
        print(f"❌ Out of guesses! The number was {secret_number}.")

# Main game loop
while True:
    play_game()
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing! 👋")
        break
