def second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    unique_number = list(set(numbers))
    if len(unique_number) < 2:
        return None
    unique_number.sort()
    return unique_number[-2]


nums = [9,4,7,2,5,9,1,6]
print("Second largest number:", second_largest_num(nums))