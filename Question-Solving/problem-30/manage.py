def display_cubes(n):
    for i in range(1, n + 1):
        print(f"Number is: {i} and cube of {i} is: {i ** 3}")

# Example usage
num = int(input("Enter an integer: "))
display_cubes(num)
