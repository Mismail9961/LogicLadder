def decimal_to_binary(num):
    if num == 0:
        return "0"
    
    binary = ""
    while num > 0:
        remainder = num % 2          # Get remainder (0 or 1)
        binary = str(remainder) + binary  # Add remainder to the front
        num //= 2                    # Divide by 2
    
    return binary

# Example usage
n = int(input("Enter a decimal number: "))
print(f"Binary of {n} is {decimal_to_binary(n)}")
