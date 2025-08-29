# Program to find the second highest number in a list

numbers = [10, 25, 8, 45, 32, 45]

# Remove duplicates using set, then sort
unique_numbers = list(set(numbers))
unique_numbers.sort()

# Second highest will be at -2 position
second_highest = unique_numbers[-2]

print("The second highest number is:", second_highest)
