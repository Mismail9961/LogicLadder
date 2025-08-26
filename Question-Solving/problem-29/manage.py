def is_prime(num):
    if num <= 1:
        return False  # 0 and 1 are not prime
    for i in range(2, int(num ** 0.5) + 1):  # check till square root
        if num % i == 0:
            return False
    return True

# Example usage
n = int(input("Enter a number: "))
if is_prime(n):
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")
