n = int(input("Enter a positive integer: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    total = n * (n + 1) // 2  # Integer division
    print(f"Sum of first {n} natural numbers is {total}")
