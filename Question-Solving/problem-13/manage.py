# Function to check if a number is prime
def is_prime(num):
    # Numbers less than 2 are not prime
    if num < 2:
        return False
    # Check for divisibility from 2 to num-1
    for i in range(2, num):
        if num % i == 0:  # If num is divisible by i, it's not prime
            return False
    return True  # If no divisors found, it's prime

# Loop through numbers 1 to 100
for num in range(1, 101):
    if is_prime(num):
        print(num, end=" ")  # Print prime numbers with a space