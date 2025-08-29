def find_missing_number(lst, N):
    expected_sum = N * (N + 1) // 2
    actual_sum = sum(lst)
    return expected_sum - actual_sum


# Example usage
numbers = [1, 2, 4, 5]  # Missing 3
N = 5
print("Missing number is:", find_missing_number(numbers, N))
