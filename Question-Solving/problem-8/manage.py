# Take input from the user
text = input("Enter a string: ")

# Define vowels
vowels = "aeiouAEIOU"

# Count vowels
count = 0
for char in text:
    if char in vowels:
        count += 1

print(f"Number of vowels: {count}")
