# Take input from the user
ch = input("Enter a single character: ").lower()

if len(ch) != 1 or not ch.isalpha():
    print("Please enter a single alphabetic character.")
elif ch in "aeiou":
    print(f"'{ch}' is a vowel.")
else:
    print(f"'{ch}' is a consonant.")
