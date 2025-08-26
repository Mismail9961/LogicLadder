def sum_of_even(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:  # Check if even
            total += num
    return total

# Example usage
nums = [10, 15, 20, 25, 30, 35]
print("Sum of even numbers:", sum_of_even(nums))
