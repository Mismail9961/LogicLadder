import random
from re import A

simple_words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
medium_words = ["pineapple", "strawberry", "watermelon", "orange", "pear", "plum", "peach"]
hard_words = ["pomegranate", "tangerine", "apricot", "mango", "nectarine", "papaya", "raspberry"]

print("Welcome to the Guessing Game!")
print("Choose a difficulty level: high, medium, low")

level = input("Enter the difficulty level: ").lower()
if level == "high":
    secret_word = random.choice(hard_words)
elif level == "medium":
    secret_word = random.choice(medium_words)
elif level == "low":
    secret_word = random.choice(simple_words)
else:
    print("Invalid difficulty level. Please choose high, medium, or low.")
    secret_word = random.choice(simple_words)

attempts = 0
print(f"Welcome to the Guessing Game! You have 5 attempts to guess the word.")

while True:
    guess = input("Enter your guess: ").lower()
    attempts += 1
    if guess == secret_word:
        print(f"Congratulations! You guessed the word in {attempts} attempts.")
        break
    hint = ""
    for letter in secret_word:
        if letter in guess:
            hint += letter
        else:
            hint += "_"
    print(f"Hint: {hint}")
    if attempts == 5:
        print(f"Sorry, you didn't guess the word. The word was {secret_word}.")
        break